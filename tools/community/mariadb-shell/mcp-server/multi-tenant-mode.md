---
description: >-
  Serve several users from one MariaDB MCP server, each authenticated with an
  API key or OAuth2 and each with their own database connections and allowed
  directories.
---

# Multi-Tenant Mode

By default, the MCP server serves one person: everyone who can reach it uses the same connections and directories, and the server doesn't authenticate its clients. In multi-tenant mode, one server serves several users. Each user authenticates every request, and each user has their own connections, passwords, and allowed directories, which no other user can see or use.

Use multi-tenant mode when one MCP server is shared, for example by a team, by a hosted AI application, or by a gateway such as [Arcade](oauth-authentication.md#connecting-through-a-gateway-such-as-arcade) that calls the server on behalf of many people.

## How It Differs from a Single-User Server

| | Single-user server | Multi-tenant server |
| --- | --- | --- |
| Authentication | None | A bearer token on every request: an API key, or an [OAuth2 access token](oauth-authentication.md) |
| Connections and passwords | One list, shared by every client | One list per user |
| Allowed directories | One list, shared by every client | One list per user |
| Transport | `stdio` or `streamable-http` | `streamable-http` only |
| Function groups | `db`, `msm`, `mrs`, `sandbox`, `migrator`, `util`, `rest` | `db` |
| Paths outside the allowed directories | The server asks the client whether to trust them | Refused |
| Configured with | `mcp setup` | `mcp setup`, and `mcp setup-oauth` for OAuth2 |

Switching between the modes moves nothing. The connections and directories of the single-user configuration stay where they are while multi-tenant mode is on, and they apply again when you turn it off.

## Requirements

* A MariaDB Shell release that stores secrets in groups. Multi-tenant mode keeps each user's secrets in a group of their own, and refuses to start on a shell without this feature.
* A server that clients reach over HTTPS, either served by the MCP server itself with a certificate or behind a reverse proxy that terminates TLS. Every request carries a user's credentials.
* An operating system account that only the MCP server uses. See [Secrets Are Separated, Not Protected](#secrets-are-separated-not-protected).

## Set Up a Multi-Tenant Server

The following steps set up a server for two users. The examples use the command-line options of `mcp setup`; you can also run `mcp setup` without options and use its menu.

1.  Turn on multi-tenant mode:

    ```bash
    mariadb-shell -- mcp setup --multiTenant=true
    ```

    ```text
    Multi-tenant mode on.
    ```
2.  Add a user. The setup creates the user, issues an API key, and prints it:

    ```bash
    mariadb-shell -- mcp setup --addUser=ada@example.com --name="Ada Lovelace"
    ```

    ```text
    User Ada Lovelace (ac28066a-df09-44d3-868c-41e7ab32fc80) added.
    API key: mdbmcp_ac28066adf0944d3868c41e7ab32fc80_x79vpwmddRcNrk1eznDUJq-U36_4vhi8OrkYWRmCCFU
    Hand it to the user; mcp setup --showApiKey shows it again.
    ```

    Pass the API key to the user through a secure channel. If users sign in with [OAuth2](oauth-authentication.md) instead, they don't need an API key, and the server can create their users automatically at their first sign-in.
3.  Give the user a connection and a directory. `--user` names the user whose configuration the options change:

    ```bash
    mariadb-shell -- mcp setup --user=ada@example.com \
      --addConnection='mariadb://ada@db.example.com:3306' --passwordEnv=ADA_DB_PASSWORD
    mariadb-shell -- mcp setup --user=ada@example.com --addPaths=/srv/projects/ada
    ```

    The setup verifies and stores the connection exactly as described in [Configuring Access](configuring-access.md#connections), but in the user's own list.
4.  Start the server over HTTPS:

    ```bash
    mariadb-shell -- mcp start-server --host=0.0.0.0 --port=8443 \
      --sslCertfile=/etc/mariadb-mcp/server.pem --sslKeyfile=/etc/mariadb-mcp/server-key.pem
    ```
5.  Register the server with the user's MCP client, with the API key, as described in [Connect a Client with an API Key](#connect-a-client-with-an-api-key).

## Users

A user consists of a user ID, which the setup generates, and one or more identities by which you and the server recognize the user. The user ID is a UUID, for example `ac28066a-df09-44d3-868c-41e7ab32fc80`. It never changes and is never reused.

### Identities

Every identity belongs to one user only. In the options of `mcp setup`, you can name a user by their user ID or by any of their identities:

| Identity | Written as | Example |
| --- | --- | --- |
| Email address | The address, or `email:<address>` | `ada@example.com` |
| User ID of your choice | `userId:<id>`, or a value without `@` | `userId:ada`, `ada` |
| OAuth2 identity | `oauth:<issuer>\|<subject>` | `oauth:https://kc.example.com/realms/mariadb\|6b1f…` |
| MariaDB account | `mariadb:<server>\|<account>` | `mariadb:mariadb://db.example.com:3306\|ada@%` |

Email addresses are compared without regard to case. The server adds OAuth2 and MariaDB account identities itself when a user signs in with [OAuth2](oauth-authentication.md), but you can also add them beforehand, for example to give one user several MariaDB accounts.

```bash
mariadb-shell -- mcp setup --user=ada@example.com --addIdentity=userId:ada
mariadb-shell -- mcp setup --user=ada --removeIdentity=userId:ada
```

A user always keeps at least one identity.

### Scopes

Scopes decide which tool groups a user may call:

| Scope | Tools |
| --- | --- |
| `mcp:db` | The `db` tools: connections, schemas, objects, and SQL. |

A new user is granted `mcp:db`. To set a user's scopes, pass `--scopes` when you add the user, or change them later with `--setScopes`:

```bash
mariadb-shell -- mcp setup --addUser=bob@example.com --scopes=mcp:db
mariadb-shell -- mcp setup --user=bob@example.com --setScopes=mcp:db
```

Earlier versions also had the scope `mcp:msm`, for the `msm` tools. The server now ignores it where a user's configuration or a token still has it, and refuses it in `--scopes` and `--setScopes`.

A client sees only the tools of the scopes its token grants, and a call to another tool fails. A change of a user's scopes applies at once, to API keys and to existing OAuth2 sign-ins alike: a token never grants a scope that the user doesn't have at the time of the request.

### Default Role

To run all database sessions of a user under a MariaDB role, set it as the user's default role. The server runs `SET ROLE` every time it opens a session for the user:

```bash
mariadb-shell -- mcp setup --user=ada@example.com --setDefaultRole=analyst
```

The role must be granted to the account of each of the user's connections. Without a default role, a session runs under the account's own `DEFAULT ROLE` on the server. To clear the setting, pass an empty value: `--setDefaultRole=`.

{% hint style="info" %}
MariaDB adds the privileges of the account itself to those of the active role. For a role to limit what a user can do, grant the account no privileges of its own beyond the role.
{% endhint %}

### API Keys

An API key has the form `mdbmcp_<user ID>_<random part>`. It contains 256 random bits. The server stores it in the user's secret group, so that you can show it again:

```bash
mariadb-shell -- mcp setup --showApiKey=ada@example.com
```

To replace a key, issue a new one. The previous key stops working immediately, also on a running server:

```bash
mariadb-shell -- mcp setup --rotateApiKey=ada@example.com
```

```text
New API key for Ada Lovelace (ac28066a-df09-44d3-868c-41e7ab32fc80): mdbmcp_ac28066adf0944d3868c41e7ab32fc80_6q3-iz-8fvAYnOM5ddWPlLScz1Ekfb5n4DMbgXVSOM0
The previous key no longer works.
```

API keys keep working when you turn on OAuth2, so you can give a key to scripts while people sign in with OAuth2.

### Disable or Remove a User

A disabled user keeps their configuration, but the server refuses their requests and closes their open database connections:

```bash
mariadb-shell -- mcp setup --disableUser=bob@example.com
mariadb-shell -- mcp setup --enableUser=bob@example.com
```

Removing a user deletes the user, their API key, and all their connection passwords:

```bash
mariadb-shell -- mcp setup --removeUser=bob@example.com
```

Both take effect with the user's next request, without a restart of the server.

## Connections and Directories of a User

In multi-tenant mode, every connection and every allowed directory belongs to a user. The options that add or delete them require `--user`, and refuse to run without it:

```bash
mariadb-shell -- mcp setup --user=ada@example.com --addConnection='mariadb://ada@db.example.com:3306'
mariadb-shell -- mcp setup --user=ada@example.com --deleteConnections='mariadb://ada@db.example.com:3306'
mariadb-shell -- mcp setup --user=ada@example.com --addPaths=/srv/projects/ada
mariadb-shell -- mcp setup --user=ada@example.com --deletePaths=/srv/projects/ada
```

A user's connections behave like the connections of a single-user server, described in [Configuring Access](configuring-access.md#connections), with these differences:

* A user lists and opens only their own connections. The same URI can be configured for several users, each with their own password.
* A connection that a user opens is bound to that user and to the client authorization they opened it with. No other user, and no other client of the same user, can use it. The binding doesn't depend on the MCP session or the address, so a gateway that opens a new session for every tool call keeps using the connection. See [Connections Belong to the Client That Opened Them](security-and-session-handling.md#connections-belong-to-the-client-that-opened-them).
* Each user can have at most 32 open connections, across all their clients.

Use a separate database account for each user wherever possible, so that the database's own privileges and audit logs apply per person.

A user's allowed directories are where `db.execute_sql_script` may read a script file from. A path outside them is refused. Unlike a single-user server, a multi-tenant server never asks the client whether to trust such a path, because the client is the party that the list restricts.

If two users are allowed the same directory, they can read each other's files in it.

## Show the Configuration

To list all users with their identities, scopes, connections, and directories, run:

```bash
mariadb-shell -- mcp setup --show --allUsers
```

```text
=== MariaDB MCP Server configuration ===
Configuration is stored in: /home/mcp/.mariadb-shell/plugin_data/mcp_plugin
Multi-tenant mode: on
Public URL:        (none)
OAuth mode:        none (mcp setup-oauth --show)

Users:
  Ada Lovelace
    id:            ac28066a-df09-44d3-868c-41e7ab32fc80
    identities:    email:ada@example.com, userId:ada
    scopes:        mcp:db
    API key:       yes
    connections:   mariadb://ada@db.example.com:3306
    allowed paths: /srv/projects/ada
  0d7160a9-fb8f-4a8b-87aa-e7f13f66f626 (disabled)
    id:            0d7160a9-fb8f-4a8b-87aa-e7f13f66f626
    identities:    email:bob@example.com
    scopes:        mcp:db
    API key:       yes
    connections:   none
    allowed paths: none
```

To show one user, pass `--user` instead of `--allUsers`. Add `--json` for machine-readable output. The output never contains passwords or API keys.

`--show --allUsers` also lists secret groups that hold secrets but belong to no user, for example after a removal that was interrupted. To delete them, run `mcp setup --purgeOrphanGroups`.

## Start a Multi-Tenant Server

Start the server as described in [Starting the MCP Server](starting-the-mcp-server.md). In multi-tenant mode, the server:

* serves only over `streamable-http`, and refuses to start with `--transport=stdio`, because a `stdio` server has no request that could carry a user's credentials;
* refuses `--gui`;
* provides only the `db` group, and refuses to start if `--functionGroups` names another one: the `sandbox`, `migrator`, `util`, and `rest` tools run local servers and long jobs on the server's machine, and the `msm` and `mrs` tools work on schema project folders and other files on the developer's own machine;
* refuses to start if there is no enabled user, unless an [OAuth2](oauth-authentication.md) mode creates users at their first sign-in (`--autoProvision`, the default), because then the first sign-in adds the first user.

```text
ERROR: Error: Shell Error: This server is configured for multi-tenant mode, which serves authenticated users over HTTP only: stdio has no request to carry a user's credentials. Use --transport=streamable-http, or turn multi-tenant mode off with mcp setup --multiTenant=false.
```

### Serve HTTPS

Every request carries a user's API key or access token. Serve HTTPS with a certificate and its private key in PEM format:

```bash
mariadb-shell -- mcp start-server --host=0.0.0.0 --port=8443 \
  --sslCertfile=/etc/mariadb-mcp/server.pem --sslKeyfile=/etc/mariadb-mcp/server-key.pem
```

Alternatively, keep the server on `127.0.0.1` and put a reverse proxy in front of it that terminates TLS. Add the name that clients use to `--allowedHosts`, or set it as the [public URL](oauth-authentication.md#the-public-url), which the server accepts automatically.

When a multi-tenant server listens on a non-loopback address without TLS, it prints a warning to standard error:

```text
WARNING: the multi-tenant MariaDB MCP server is about to listen on 0.0.0.0:8080 over plain HTTP.
         Every request carries a user's API key or access token, which anyone on the network
         path can read. Serve HTTPS with --sslCertfile and --sslKeyfile, or put a TLS-terminating
         reverse proxy in front of the server.
```

### Size the Server for Its Users

The server holds at most 64 open database connections for all users together. For many users, raise the limit with `--maxConnections`, and check that the database servers' `max_connections` allows it:

```bash
mariadb-shell -- mcp start-server --host=0.0.0.0 --port=8443 --maxConnections=256 ...
```

{% hint style="warning" %}
Run a multi-tenant server as a single instance. Some of its state, such as rate limits and, with the [built-in authorization server](oauth-authentication.md#using-the-built-in-authorization-server), pending sign-ins, is kept in the server process. Several instances behind a load balancer don't share it.
{% endhint %}

## Connect a Client with an API Key

A client sends the API key in the `Authorization` header of every request, as a bearer token. Register the server's URL with the header.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --scope user --transport http mariadb https://mcp.example.com:8443/mcp \
  --header "Authorization: Bearer mdbmcp_ac28066a..."
```
{% endtab %}

{% tab title="Visual Studio Code" %}
{% code title=".vscode/mcp.json" %}
```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "mariadb-api-key",
      "description": "MariaDB MCP API key",
      "password": true
    }
  ],
  "servers": {
    "mariadb": {
      "type": "http",
      "url": "https://mcp.example.com:8443/mcp",
      "headers": { "Authorization": "Bearer ${input:mariadb-api-key}" }
    }
  }
}
```
{% endcode %}
{% endtab %}

{% tab title=".mcp.json" %}
{% code title=".mcp.json" %}
```json
{
  "mcpServers": {
    "mariadb": {
      "type": "http",
      "url": "https://mcp.example.com:8443/mcp",
      "headers": { "Authorization": "Bearer ${MARIADB_MCP_API_KEY}" }
    }
  }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

Don't commit an API key to version control. Use the client's mechanisms for secrets, such as an input prompt or an environment variable, as in the examples.

To sign in with OAuth2 instead of an API key, register only the URL; the client then runs the sign-in itself. See [OAuth Authentication](oauth-authentication.md).

## Requests Without a Valid Token

The server answers a request without a valid token with status `401 Unauthorized`, before any tool runs:

```text
HTTP/1.1 401 Unauthorized
www-authenticate: Bearer error="invalid_token", error_description="Authentication required"
```

Each refused token is logged with the address it came from, without the token and without the user it claims to belong to:

```text
2026-10-06T17:13:44+0200 [mcp] auth: REFUSED a bearer token from address=203.0.113.24
```

After 10 refused tokens within a minute from one address for one user (for an OAuth2 token, the user it names), the server answers that address and user with status `429 Too Many Requests` for the rest of the minute. One address can cause at most 200 refusals a minute in total. The limits apply per address and user, so that one user's wrong key doesn't lock out other users who reach the server through the same gateway or proxy.

## Secrets Are Separated, Not Protected

The server stores each user's API key and connection passwords in a secret group of the MariaDB Shell [credential store](../connecting/credential-store.md), named by the user's ID. Groups keep the users' secrets apart within the MCP server, but they aren't a protection against other programs: any process that runs as the same operating system user can read every group, including the API keys, which are stored as they are so that `--showApiKey` can show them.

* Run the MCP server under an operating system account of its own, which no person and no other program uses.
* On Linux, the default credential store helper, `login-path`, only obfuscates its file. Prefer `secret-service` where it is available, and restrict access to the server's home directory.

## Where the Configuration Is Stored

| What | Location |
| --- | --- |
| Multi-tenant mode on or off | `settings.json` in the plugin data directory |
| Users, identities, scopes, default roles, and allowed directories | `users.json` in the plugin data directory |
| API keys and connection passwords | The credential store, in a secret group per user, named by the user ID |

The plugin data directory is `~/.mariadb-shell/plugin_data/mcp_plugin/` on Linux and macOS, as described in [Configuring Access](configuring-access.md#where-the-configuration-is-stored). `users.json` contains no secrets.

## Options of mcp setup for Multi-Tenant Mode

These options complement the options described in [Automated Setup](automated-setup.md#options):

| Option | Description |
| --- | --- |
| `--multiTenant=<bool>` | Turns multi-tenant mode on or off. Moves no configuration. |
| `--addUser=<identities>` | Adds a user, known by the given comma-separated identities, and prints their API key. |
| `--name=<name>` | The name to show for the user that `--addUser` adds. |
| `--scopes=<list>` | The scopes that the user `--addUser` adds may be granted. Default: `mcp:db`. |
| `--removeUser=<list>` | Removes users, with their API keys and connection passwords. |
| `--user=<user>` | The user that `--addConnection`, `--deleteConnections`, `--addPaths`, `--deletePaths`, `--addIdentity`, `--removeIdentity`, `--setScopes`, and `--setDefaultRole` change, or that `--show` reports. Required for the connection and path options in multi-tenant mode, and refused for them otherwise. |
| `--addIdentity=<list>` | Adds identities to the user. |
| `--removeIdentity=<list>` | Removes identities from the user. |
| `--setScopes=<list>` | Sets the scopes the user may be granted. |
| `--setDefaultRole=<role>` | Sets the MariaDB role the user's sessions run under. An empty value clears it. |
| `--disableUser=<list>` | Disables users. |
| `--enableUser=<list>` | Enables users. |
| `--rotateApiKey=<list>` | Issues new API keys. The previous keys stop working immediately. |
| `--showApiKey=<list>` | Prints the API keys of users. |
| `--allUsers` | With `--show`, reports every user and the secret groups that belong to no user. |
| `--purgeOrphanGroups` | Deletes the secret groups that belong to no user. |
| `--json` | Also prints the user IDs and API keys of `--addUser`, `--rotateApiKey`, and `--showApiKey` as JSON, when they are the only options. |

The setup carries the options out in this order: the mode, user removals, user additions, identity changes, disabling and enabling, scopes, key rotation, default roles, and then connections and paths as described in [Order of Operations](automated-setup.md#order-of-operations). You can therefore add a user and give them a connection in one call, naming them by the identity you just added.

## Troubleshooting

| Message or symptom | Cause | Solution |
| --- | --- | --- |
| *Multi-tenant mode needs a MariaDB Shell that keeps secrets in groups* | The shell doesn't support secret groups. | Upgrade MariaDB Shell. |
| *Multi-tenant mode is on, but there is no enabled user to serve.* | No user exists, or all users are disabled, and no OAuth2 mode creates users at sign-in. | Add a user with `--addUser`, enable one, or turn on `--autoProvision` of the OAuth2 mode. |
| *In multi-tenant mode connections and allowed paths belong to a user* | A connection or path option was given without `--user`. | Add `--user`. |
| *--user only applies to … in multi-tenant mode, which is off.* | `--user` was given while multi-tenant mode is off. | Turn on multi-tenant mode, or leave out `--user`. |
| *The function group(s) msm, sandbox, migrator are not available in multi-tenant mode* | `--functionGroups` names a group that tenants can't use. | Leave out `--functionGroups`, or pass `db`. |
| The client receives `401 Unauthorized`. | The request has no API key, or the key is wrong, rotated, or belongs to a disabled or removed user. | Check the key with `--showApiKey`, and the user with `--show --user`. |
| The client receives `429 Too Many Requests`. | Too many refused tokens from the address. | Correct the key and wait a minute. |
| *The tool … needs the scope '…', which your access was not granted.* | The user's scopes don't include the tool's group. | Grant the scope with `--setScopes`. |
| *Access to path '…' is not allowed. Ask the administrator to add it …* | The path isn't in the user's allowed directories. | Add it with `--user=… --addPaths`. |
