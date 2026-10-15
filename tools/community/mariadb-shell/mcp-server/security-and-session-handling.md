---
description: >-
  How the MariaDB MCP server limits what an AI agent can reach, how to expose
  it on a network safely, and how it binds, recycles, and expires the database
  sessions it opens for clients.
---

# Security and Session Handling

The MCP server gives an AI agent access to databases and files with your credentials. Several layers limit that access:

| Layer | What it limits | Configured with |
| --- | --- | --- |
| Authentication | Who can use the server at all; only in [multi-tenant mode](multi-tenant-mode.md) | `mcp setup`, `mcp setup-oauth` |
| Network binding | Which machines can reach an HTTP server | `--host`, `--allowedHosts` |
| Connection allow-list | Which servers and accounts the agent can open | `mcp setup` |
| Account privileges | What the agent can do on a server | `CREATE USER` and `GRANT` on the server |
| Allowed paths | Which local directories tools can read and write | `mcp setup` |
| Function groups | Which kinds of tools the agent has | `--functionGroups` |

None of these layers restricts the SQL statements themselves. Within a configured connection, the agent can run any statement that the account's privileges allow. Use [a dedicated account with limited privileges](configuring-access.md#use-a-dedicated-account) for every connection.

## Network Exposure

A server in [multi-tenant mode](multi-tenant-mode.md) authenticates every request with an API key or an [OAuth2](oauth-authentication.md) access token, and serves each user only their own connections and directories. Serve it over HTTPS. The rest of this section applies to a single-user server.

A single-user MCP server has no authentication: no token, no password, and no client certificate. Any client that can reach the server can list the configured connections and open them, and the server signs in with the stored passwords. With the `sandbox` and `msm` tools, such a client can also start database servers and write files in the allowed paths.

Where the server listens is therefore its only access control:

* **`stdio`** opens no port. Only the client that started the server can talk to it. Prefer this transport whenever the client can start a command.
* **`streamable-http`** binds to `127.0.0.1` by default, so only processes on the same machine can connect. That includes every process of every user on the machine.

When you bind the server to an address that other machines can reach, it prints a warning to standard error:

```text
WARNING: the MariaDB MCP server is about to listen on 0.0.0.0:8080, which is reachable from other machines.
         The server has NO AUTHENTICATION: anyone who can reach this port can list the
         configured database connections and open them, using the stored credentials.
         Bind to 127.0.0.1 (the default) and put a tunnel or an authenticating proxy in
         front of it if it has to be reachable remotely.
```

{% hint style="danger" %}
Don't bind the MCP server to a public or shared network address. If a client on another machine must use it, keep the server on `127.0.0.1`, and give the client access through an SSH port forward or a reverse proxy that authenticates every request.
{% endhint %}

An SSH port forward makes a server on a remote machine available on the local machine. Run it on the client machine:

```bash
ssh -N -L 8080:127.0.0.1:8080 dev@mcp-host.example.com
```

The client then connects to `http://127.0.0.1:8080/mcp`, and only users who can sign in to `mcp-host.example.com` with SSH can reach the server.

## Host and Origin Validation

Because the server has no authentication, a web page open in a browser on the same machine could otherwise send requests to it. The browser's same-origin rules normally stop a page from reading the answers, but a DNS rebinding attack can work around them: the attacker's domain is made to resolve to the address of the server, so the page counts as same-origin.

The server prevents this by checking two HTTP headers of every request:

* **`Host`** must be one of the names that the server answers to. Otherwise, the server refuses the request with status `421 Misdirected Request`. A page loaded from an attacker's domain sends that domain as `Host`.
* **`Origin`**, if present, must belong to one of these names. Otherwise, the server refuses the request with status `403 Forbidden`. Clients other than browsers don't send `Origin`, so they aren't affected.

The accepted names follow from `--host`:

| `--host` | Accepted `Host` values |
| --- | --- |
| A loopback address, such as the default `127.0.0.1` | `127.0.0.1`, `localhost`, and `[::1]`, each with and without the port |
| A single address or host name | That address or name, with and without the port |
| `0.0.0.0` or `::` | The loopback names, plus the host name, the fully qualified domain name, and the addresses of the machine |

If clients reach the server under another name, for example through a reverse proxy, a port forward to another port, or a DNS alias, add the name with `--allowedHosts`. Without it, the server refuses their requests:

```bash
mariadb-shell -- mcp start-server --allowedHosts=mcp.example.com
```

The value is compared with the complete `Host` header. If clients send a port in the header, add the name with the port as well, for example `--allowedHosts=mcp.example.com,mcp.example.com:8443`.

A refused request appears in the server output:

```text
Invalid Host header: evil.example.com
INFO:     127.0.0.1:62229 - "POST /mcp HTTP/1.1" 421 Misdirected Request
```

## Connections Belong to the Client That Opened Them

When an agent opens a configured connection with `db.connect`, it receives a connection ID, which it passes to the other `db` tools. Over HTTP, several clients can use the same server, so the server binds each connection to the client that opened it:

* **The MCP session ID.** The server assigns this ID when a client initializes its MCP session, and only that client knows it. It keeps clients apart even when they share an IP address, as all local clients do.
* **The IP address** of the network connection that the request arrived on. The server never takes the address from a header such as `X-Forwarded-For`, which a client could forge.

A request with a connection ID that doesn't match both is answered as if the ID didn't exist, so another client can't take over a connection by guessing its ID. Behind a reverse proxy, all clients share the proxy's address, and the MCP session ID keeps them apart.

On a [multi-tenant server](multi-tenant-mode.md), every request is authenticated, and the server binds a connection to these instead:

* **The user** that the request was authenticated as.
* **The authorization** that the request's access token belongs to. For the built-in authorization server, that is the user's grant to one client. For a Keycloak token or an API key, it is the client that the token was issued to.

The MCP session and the IP address aren't part of the binding on a multi-tenant server, because a gateway such as Arcade opens a new MCP session for every tool call, and can call from different addresses. Another user, or another client of the same user, can't use the connection.

Over `stdio`, the server has only one client, which always matches.

### Clients Without MCP Sessions

Revision 2026-07-28 of the MCP specification has no sessions, so clients that use it, such as current versions of Claude Code, never send an MCP session ID. How the server binds their connections depends on the mode:

* On a **multi-tenant server**, the session ID isn't needed: the connection is bound to the user and their authorization, as described above.
* On a **single-user server**, which doesn't authenticate, the session ID is the only thing that tells clients on the same machine apart. Over HTTP, the server therefore refuses to open a connection for such a client:

  ```text
  This client uses MCP without sessions (protocol revision 2026-07-28), and this server does not authenticate its clients, so a connection opened over HTTP could not be bound to this client. Connect over stdio, or have the server run in multi-tenant mode (mcp setup --multiTenant=true), where every client signs in.
  ```

  Connect such clients over `stdio`, or use multi-tenant mode for HTTP.

{% hint style="info" %}
The binding prevents one client from using another client's connection. It isn't authentication: any client that can reach the server can open connections of its own.
{% endhint %}

## Session Lifetime

The server limits how long database sessions and connection IDs live:

| Limit | Value | Transport | Effect |
| --- | --- | --- | --- |
| Idle session | 30 minutes | HTTP only | A background task closes the database session of a connection that hasn't been used for 30 minutes. The connection ID stays valid. |
| Connection lifetime | 12 hours | Both | A connection ID stops working 12 hours after `db.connect` returned it, however much it was used. The agent must call `db.connect` again. |

After an idle session was closed, the next tool call with the same connection ID opens a new session. Anything that only existed in the old session is lost: temporary tables, session variables, the current schema, and an open transaction. The result of that tool call contains `session_restarted: true`, so that the agent can tell. This matters in particular for transactions, because a `COMMIT` in a new session succeeds without committing anything.

An expired connection ID is reported in the same way as an ID that never existed.

### Lost Sessions

A database session can also end without the MCP server closing it, for example when the database server restarts, an administrator runs `KILL`, or a firewall drops an idle connection. The statement that hits the lost session fails with an error such as `MySQL Error (2013): Lost connection to server during query`, and the server doesn't retry it, because it might have run partially. The next tool call with the same connection ID opens a new session and works.

## Connection Limits

A client can have at most 16 open connections, and the server at most 64 for all clients together. On a multi-tenant server, each user can also have at most 32 open connections across all their clients. To raise the limit for all clients, start the server with `--maxConnections`. A `db.connect` call over either limit is refused before the server opens a database session, with a message that tells the agent to close connections with `db.close`. Over `stdio`, the limit of 16 applies, because all requests come from one client.

The limits protect the database server's `max_connections` and the memory of the MCP server from an agent that opens connections in a loop. To also limit the sessions on the database server, set `MAX_USER_CONNECTIONS` on the account.

## Revoking Access

When you remove a connection with `mcp setup`, the server refuses to open new sessions for it. It checks the configured connections each time it opens a session, including when it reopens a session after an idle period, so existing connection IDs stop working as well.

A session that is in continuous use isn't checked for every statement, so it can outlive the removal by up to its 12-hour lifetime. If a removal must take effect immediately, restart the MCP server. To take away access completely, also lock the account or change its password on the database server.

Removing a directory from the allowed paths takes effect with the next tool call.

On a multi-tenant server, removing or disabling a user, or replacing their API key, takes effect with the user's next request, without a restart, and closes the user's open connections. To end a user's OAuth2 access, see [Revoking Access](oauth-authentication.md#revoking-access).

## Connections Created by Sandboxes

`sandbox.deploy` adds a connection to the allow-list for the `root` account of the new instance, `mariadb://root@127.0.0.1:<port>`, with the password that the agent chose, so that the agent can connect to it. This is the only case in which the server adds a connection without `mcp setup`, and the connection always points to a local sandbox. `sandbox.delete` removes the connection again, along with the instance.

To prevent an agent from deploying sandboxes, leave out the `sandbox` group with `--functionGroups`.

## Credentials

The passwords of the configured connections are stored in the MariaDB Shell [credential store](../connecting/credential-store.md), separately from the passwords of your own MariaDB Shell connections. The server reads them when it opens a session and never returns them to the client. The tools of the `migrator` group refuse passwords in the migration configuration, and read them from the credential store when a migration runs.

The server's log output contains neither passwords nor SQL statements, and it shortens connection IDs and MCP session IDs, because these identify a client's connection. See [Log Output](starting-the-mcp-server.md#log-output).

## Checklist

* Use `stdio` when the client can start a command.
* To share a server among several people, use [multi-tenant mode](multi-tenant-mode.md) over HTTPS, and run the server under an operating system account of its own.
* Keep an HTTP server on `127.0.0.1`. For remote clients, use an SSH port forward or an authenticating reverse proxy.
* Create a dedicated account for each connection, with read-only access to production schemas and resource limits.
* Allow only the project directories the agent works in.
* Provide only the function groups the agent needs.
* Remove connections and directories that the agent no longer needs, and restart the server if the removal must take effect immediately.
