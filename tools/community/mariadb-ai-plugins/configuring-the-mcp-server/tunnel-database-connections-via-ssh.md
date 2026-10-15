---
description: >-
  Connect the mariadb-shell MCP server to a MariaDB server that is only
  reachable through an SSH host, with a mariadb+ssh:// connection URI.
---

# Tunnel Database Connections via SSH

Database servers are often not reachable directly from a developer machine, but only through an SSH host, such as a bastion host in front of a private network. The MCP server can reach such a server through an SSH tunnel, which MariaDB Shell sets up when the MCP server opens a session for the connection.

You request a tunnel with the `mariadb+ssh://` scheme in the connection URI. Everything else about the connection, such as the allow-list, the stored password, and the database account, works as for any other connection.

## Requirements

* MariaDB Shell 26.9.3 or later. The current plugins require a later version already.
* SSH access to the SSH host with a key that the MCP server can use without a prompt. See [SSH Authentication](#ssh-authentication).
* The host key of the SSH host in your known-hosts file. See [Host Keys](#host-keys).
* A MariaDB account for the MCP server on the database server. See [Database Accounts for the MCP Server](database-accounts-for-the-mcp-server.md).

## The Model

In a `mariadb+ssh://` URI, the user, host, and port always describe the database: the database account, and the database server with its port. The `ssh-*` options in the query string describe how the server is reached. There are two cases:

```text
mariadb+ssh://dba@remote-host.com:3306
mariadb+ssh://dba@db-01.internal:3306?ssh-host=bastion.example.com
```

* **Without `ssh-host`**, the database runs on the machine you connect to over SSH. The SSH connection goes to the host in the URI, and the tunnel forwards to the loopback address, `127.0.0.1`, on that machine. Forwarding to the host name instead wouldn't work for a server that only listens on `127.0.0.1`, which is a common reason to use a tunnel in the first place. This case needs no options at all.
* **With `ssh-host`**, the database runs on another machine behind the SSH host, such as a bastion host. The SSH connection goes to the host in `ssh-host`, and the tunnel forwards to the host in the URI, as the SSH host resolves it. This case needs one option.

The host in the URI therefore always means the database server, whether `ssh-host` is given or not. If it meant the SSH host in one case and the database server in the other, the same URI could be read in two ways.

The options `ssh-user`, `ssh-port`, `ssh-config-file`, and `ssh-identity-file` complete the description of the SSH connection. The SSH password and the passphrase of a key can't be part of a URI. A URI identifies a connection: it names the connection, serves as the key under which its password is stored, and appears in logs and messages. For the same reason, the database password isn't part of the URI either.

## Structure of a Tunnel URI

The following URI uses the most common options:

```text
mariadb+ssh://mcp@db.internal:3306?ssh-host=bastion.example.com&ssh-user=tunnel
```

This URI connects to `bastion.example.com` over SSH as the user `tunnel`, and forwards the database connection from there to `db.internal:3306`, where it signs in as `mcp`. The SSH host resolves `db.internal`, so you can use host names of the private network.

| Option | Description |
| --- | --- |
| `ssh-host` | The SSH host. If you omit it, the database host is also the SSH host, and the tunnel connects to `127.0.0.1` on that machine. |
| `ssh-user` | The user on the SSH host. Default: the operating system user that runs MariaDB Shell. A `User` setting in the SSH configuration file takes precedence over this default. |
| `ssh-port` | The SSH port. Default: `22`. |
| `ssh-identity-file` | The private key file to authenticate with. If you omit it, the default keys and the SSH agent are used. |
| `ssh-config-file` | An OpenSSH configuration file to read the settings of the SSH host from. |

If you omit the database port, `3306` is used. The `ssh-*` options are only valid on a `mariadb+ssh://` URI; on a `mariadb://` URI, MariaDB Shell rejects them.

### Examples

A database server in a private network, reached through a bastion host, with a dedicated key:

```text
mariadb+ssh://mcp@db.internal:3306?ssh-host=bastion.example.com&ssh-user=tunnel&ssh-identity-file=/home/dev/.ssh/mcp_tunnel
```

A database server that only listens on its loopback interface, reached by SSH on the server itself:

```text
mariadb+ssh://mcp@db1.example.com?ssh-user=tunnel
```

An SSH host defined in your OpenSSH configuration, which also provides the user, port, and key:

```text
mariadb+ssh://mcp@db.internal?ssh-host=bastion&ssh-config-file=/home/dev/.ssh/config
```

For connections to MySQL servers, for example as the source of a migration, use `mysql+ssh://` in the same way.

## SSH Authentication

The MCP server runs without a terminal and can't prompt for anything. It tries the following authentication methods in this order:

1. Public key authentication, with the key given in `ssh-identity-file`, or else with the default keys in `~/.ssh` and the keys in the SSH agent.
2. Password authentication, with a password stored in the MariaDB Shell credential store.
3. Keyboard-interactive authentication. This method requires a prompt, so it's not available to the MCP server.

In practice, use one of these options:

* **A dedicated key without a passphrase**, used only for the tunnel, and referenced with `ssh-identity-file`. Protect the key file with file permissions, and restrict what the key can do on the SSH host, as described in [Restrict the Tunnel Key](#restrict-the-tunnel-key).
* **A key in the SSH agent**, on Linux and macOS. Load the key into the agent before you start the harness, for example:

  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```

  The MCP server runs as a child process of the harness, so the harness must have access to the agent, typically through the `SSH_AUTH_SOCK` environment variable.

{% hint style="warning" %}
A key protected by a passphrase only works through the SSH agent. The MCP server can't ask for the passphrase, and a URI can't contain it.
{% endhint %}

## Host Keys

Before it opens a tunnel, MariaDB Shell checks the host key of the SSH host against your known-hosts file, `~/.ssh/known_hosts`. Because the MCP server can't ask you to confirm an unknown host key, it refuses the connection in this case:

```text
The authenticity of host 'bastion.example.com' can't be established.
```

Add the host key before the agent uses the connection. `mcp setup` does this for you: when you add a `mariadb+ssh://` connection, the setup opens the tunnel to verify the connection, shows the fingerprint of an unknown host key, and asks you to confirm it. If you confirm, it stores the key in the known-hosts file. Compare the fingerprint with the one your administrator provides before you confirm.

Alternatively, connect to the SSH host once with `ssh`, and accept the host key there:

```bash
ssh tunnel@bastion.example.com
```

If the host key changes later, MariaDB Shell always refuses the connection with `Invalid fingerprint detected`, because a changed key can mean that the connection is being intercepted. Check with your administrator whether the key was changed, then remove the old entry and accept the new key:

```bash
ssh-keygen -R bastion.example.com
```

## Add the Connection

Add the connection with `mcp setup`, and enter the `mariadb+ssh://` URI when the setup asks for a connection URI:

```bash
mariadb-shell -- mcp setup
```

The password that the setup asks for is the password of the database account, not an SSH password. The setup verifies the connection through the tunnel before it stores the password.

You can also pass the URI on the command line. The setup then asks only for the password. Put the URI in single quotes, because the `?` and `&` characters have a special meaning in the shell:

```bash
mariadb-shell -- mcp setup \
  --addConnection='mariadb+ssh://mcp@db.internal:3306?ssh-host=bastion.example.com&ssh-user=tunnel'
```

Always enter the password at the prompt. Don't pass it on the command line or in an environment variable. For details, see [Adding Database Connections](adding-database-connections.md).

## Use the Connection

The agent finds the connection with `db.list_connections` and connects to it with its `mariadb+ssh://` URI. For the agent, a tunneled connection works like any other connection. MariaDB Shell sets up the tunnel as part of opening the session, including when the MCP server reopens a session that was closed for being idle.

The scheme is part of the connection. A `mariadb://` URI with the same user and host is a different connection, and the MCP server refuses it unless it's also configured. This way, the agent can't bypass the tunnel by accident.

## Restrict the Tunnel Key

An SSH key that can open a tunnel can usually also open a shell on the SSH host. If the key is only used for the tunnel, restrict it in the `~/.ssh/authorized_keys` file of the tunnel user on the SSH host:

{% code title="~/.ssh/authorized_keys" %}
```text
restrict,port-forwarding,permitopen="db.internal:3306" ssh-ed25519 AAAA... mcp-tunnel
```
{% endcode %}

`restrict` disables everything the key could otherwise do, `port-forwarding` allows port forwarding again, and `permitopen` limits the forwarding to the database server. With these options, the key can't open a shell and can't forward connections to other hosts.

The tunnel controls how the agent reaches the server, not what it can do there. Use a dedicated database account with limited privileges as well, as described in [Database Accounts for the MCP Server](database-accounts-for-the-mcp-server.md).

## Troubleshooting

| Message | Cause | Solution |
| --- | --- | --- |
| *The authenticity of host '…' can't be established.* | The host key of the SSH host isn't in the known-hosts file. | Add the connection with `mcp setup` and confirm the key, or connect once with `ssh`. |
| *Invalid fingerprint detected.* | The host key of the SSH host has changed. | Verify the new key with your administrator, then remove the old entry with `ssh-keygen -R`. |
| *Authentication error opening SSH tunnel* or *Access denied* | The SSH host didn't accept any of the keys, or the key needs a passphrase. | Check `ssh-user` and `ssh-identity-file`, or load the key into the SSH agent. |
| *Interactive auth mode is disabled when in disabled wizards mode.* | The SSH host only offers keyboard-interactive authentication. | Configure public key authentication for the tunnel user. |
| *The connection option '…' requires an SSH tunnel.* | An `ssh-*` option is used on a URI without `+ssh`. | Use the `mariadb+ssh://` scheme. |
| *not a configured connection* | The agent used a URI that differs from the configured one, for example `mariadb://` instead of `mariadb+ssh://`. | Use the URI that `db.list_connections` reports. |
