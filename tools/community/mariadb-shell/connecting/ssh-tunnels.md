---
description: >-
  Reach a MariaDB server that is only accessible through SSH, with a
  mariadb+ssh:// URI or with the --ssh options.
---

# SSH Tunnels

Database servers are often not reachable from your workstation: they listen only on their loopback interface, or sit in a private network behind a bastion host. MariaDB Shell can open an SSH tunnel for such a connection itself, so you don't need to run `ssh -L` in another terminal.

You can describe a tunnel in two ways:

* With a `mariadb+ssh://` URI, which carries the whole connection, tunnel included, in one string. This is the recommended form.
* With the older `--ssh` command-line options or the `ssh` dictionary key, which describe the tunnel separately from the database URI.

MariaDB Shell uses its built-in SSH client for the tunnel. It doesn't need the `ssh` command.

## Tunnel URIs

Add `+ssh` to the scheme to tunnel a connection: `mariadb+ssh://`, or `mysql+ssh://` for the same thing written the MySQL way. In a tunnel URI, the user, host, and port always describe the **database**: the account, the database server, and its port. The SSH connection is described by `ssh-*` options in the query string.

There are two cases, depending on where the database runs:

```text
mariadb+ssh://dba@db1.example.com:3306
mariadb+ssh://dba@db-01.internal:3306?ssh-host=bastion.example.com
```

* **The database runs on the SSH host.** Leave out `ssh-host`. MariaDB Shell opens the SSH connection to the host in the URI, `db1.example.com`, and forwards the database connection to `127.0.0.1` on that machine. This works for a server that listens only on its loopback interface, which is a common reason to use a tunnel.
* **The database runs behind the SSH host.** Set `ssh-host` to the SSH host, such as a bastion. MariaDB Shell opens the SSH connection to `bastion.example.com`, and forwards the database connection from there to `db-01.internal:3306`. The SSH host resolves the database host name, so you can use names and addresses of the private network.

Because the host in the URI always means the database server, whether `ssh-host` is set or not, a tunnel URI has only one reading.

### SSH Options

| Option | Default | Description |
| --- | --- | --- |
| `ssh-host` | The host in the URI | The SSH host. When you set it, the tunnel forwards to the host in the URI instead of to `127.0.0.1`. |
| `ssh-user` | The operating system user that runs MariaDB Shell | The user on the SSH host. A `User` setting for the host in the OpenSSH configuration file takes precedence over this default. |
| `ssh-port` | `22` | The SSH port, from 1 to 65535. |
| `ssh-identity-file` | The default keys and the SSH agent | The private key file to authenticate with. |
| `ssh-config-file` | The `ssh.configFile` shell option, or `~/.ssh/config` | An OpenSSH configuration file to read the settings for the SSH host from. |

The database port defaults to `3306`. Encode file paths in the query string, or enclose them in parentheses. A leading `~` in a path is expanded to your home directory. The identity file must exist when the URI is parsed.

The `ssh-*` options are valid only with a `+ssh` scheme. On a `mariadb://` URI, MariaDB Shell rejects them:

```text
Invalid URI: The connection option 'ssh-user' requires an SSH tunnel. Use the '+ssh' scheme extension, as in 'mariadb+ssh://'.
```

### Passwords Aren't Part of the URI

A URI can't contain the SSH password or the passphrase of a key. The options `ssh-password` and `ssh-identity-file-password` are rejected in a URI with `The connection option '...' cannot be set in a URI.` A URI names a connection, and MariaDB Shell displays it and writes it to logs, so the SSH secrets are kept out of it. MariaDB Shell prompts for the secrets it needs instead, or takes them from the [credential store](credential-store.md). See [Authentication](#authentication).

### Examples

A server that listens only on `127.0.0.1`, reached by SSH on the server itself:

```text
mariadb+ssh://dba@db1.example.com
```

A server in a private network behind a bastion host, with a dedicated user and key for the tunnel:

```text
mariadb+ssh://dba@db-01.internal:3306?ssh-host=bastion.example.com&ssh-user=tunnel&ssh-identity-file=(~/.ssh/tunnel_ed25519)
```

An SSH host defined in your OpenSSH configuration, which also supplies the user, port, and key:

{% code title="~/.ssh/config" %}
```text
Host bastion
    HostName bastion.example.com
    User tunnel
    Port 2222
    IdentityFile ~/.ssh/tunnel_ed25519
```
{% endcode %}

```text
mariadb+ssh://dba@db-01.internal?ssh-host=bastion
```

### Using a Tunnel URI

Pass a tunnel URI to `shell.connect()`, `shell.open_session()`, or any other Python function that takes connection data:

```python
shell.connect("mariadb+ssh://dba@db-01.internal?ssh-host=bastion.example.com")
```

MariaDB Shell reports the tunnel before it prompts for the database password:

```text
Opening SSH tunnel to bastion.example.com:22...
Please provide the password for 'dba@db-01.internal:3306':
```

`session.uri` and `\status` show the defaulted SSH settings that were filled in:

```text
MariaDB db-01.internal:3306 ssl  Py > session.uri
mariadb+ssh://dba@db-01.internal:3306?ssh-host=bastion.example.com&ssh-user=jdoe&ssh-port=22
```

A tunnel URI keeps its tunnel through `shell.parse_uri()` and `shell.unparse_uri()`. The dictionary carries `mariadb+ssh` as the scheme, and only the SSH settings that were set.

{% hint style="warning" %}
In MariaDB Shell 26.9.5, the `mariadb-shell` command line and the `\connect` command don't accept tunnel URIs yet: they fail with `Scheme extension [ssh] is not supported`. To open a tunnel from the command line, use the [older SSH options](#the-older-ssh-options). In a script run with `mariadb-shell --py -f`, or after starting `mariadb-shell --py`, call `shell.connect()` with the tunnel URI.
{% endhint %}

## Authentication

MariaDB Shell tries the following SSH authentication methods, in this order, until one succeeds:

1. Public key authentication. With `ssh-identity-file`, MariaDB Shell uses that key, and prompts for its passphrase if the key is encrypted. Without it, MariaDB Shell tries the keys that the SSH agent offers and your default key files, such as `~/.ssh/id_ed25519` and `~/.ssh/id_rsa`.
2. Password authentication. MariaDB Shell looks for a stored password for `ssh://user@host:port` in the credential store, and otherwise prompts for it.
3. Keyboard-interactive authentication, which shows the prompts that the SSH server sends. This method is skipped when MariaDB Shell runs with `--no-wizard`.

Each method runs only if the SSH server offers it. SSH passwords and key passphrases that you type can be saved in the credential store like database passwords. If a stored SSH password is rejected, MariaDB Shell deletes it.

For scripts and other runs without a terminal, use a key that MariaDB Shell can use without a prompt: an unencrypted key file, or a key loaded into the SSH agent.

### Host Keys

MariaDB Shell checks the SSH host's key against your known-hosts file, `~/.ssh/known_hosts`. If the host is unknown, it shows the key fingerprint and asks whether to continue:

```text
The authenticity of host 'bastion.example.com' can't be established.
Server key fingerprint is ...
Are you sure you want to continue connecting?
```

If you answer `Yes`, MariaDB Shell adds the key to the known-hosts file. Without a terminal to ask, it refuses the connection to an unknown host. If the host key has changed since it was recorded, MariaDB Shell warns that the public key has changed and refuses the connection. To prepare a host for scripts, add the host key beforehand, for example with `ssh-keyscan bastion.example.com >> ~/.ssh/known_hosts`, after you have checked the fingerprint.

## Listing Open Tunnels

MariaDB Shell keeps a tunnel open while sessions use it. When you open another session with the same SSH settings and target, MariaDB Shell reuses the existing tunnel. `shell.list_ssh_connections()` lists the open tunnels:

```text
MariaDB db-01.internal:3306 ssl  Py > shell.list_ssh_connections()
[
    {
        "remote": "db-01.internal:3306",
        "timeCreated": "2026-10-05T16:55:46",
        "uri": "jdoe@bastion.example.com:22"
    }
]
```

The `uri` entry is the SSH endpoint, and `remote` is the database address that the tunnel forwards to.

## The Older SSH Options

Before tunnel URIs existed, a tunnel was described separately from the database URI. These forms still work, and they are the way to open a tunnel from the `mariadb-shell` command line.

On the command line:

| Option | Description |
| --- | --- |
| `--ssh=<[user@]host[:port]>` | The SSH host to tunnel through. |
| `--ssh-identity-file=<file>` | The private key file. |
| `--ssh-config-file=<file>` | The OpenSSH configuration file. Sets the `ssh.configFile` shell option for the session. |

```sh
mariadb-shell --ssh tunnel@bastion.example.com dba@db-01.internal:3306 --sql
```

`\connect` accepts `--ssh` in the same way:

```text
\connect --ssh tunnel@bastion.example.com dba@db-01.internal:3306
```

In a connection dictionary:

| Key | Description |
| --- | --- |
| `ssh` | The SSH host, as `[user@]host[:port]`. |
| `ssh-password` | The SSH password. |
| `ssh-identity-file` | The private key file. |
| `ssh-identity-file-password` | The passphrase of the key file. |
| `ssh-config-file` | The OpenSSH configuration file. |

```python
session = shell.open_session({
    "uri": "dba@db-01.internal:3306",
    "ssh": "tunnel@bastion.example.com:22",
    "ssh-identity-file": "~/.ssh/tunnel_ed25519",
})
```

In these forms, the database host is always resolved by the SSH host, as with `ssh-host` in a tunnel URI. To reach a server that listens on the SSH host's loopback interface, use `127.0.0.1` as the database host.

{% hint style="info" %}
Always include the user in `--ssh` and in the `ssh` key. Without it, these older forms can fall back to a different account than the one you are logged in as, such as `root`, in sessions that were opened by another account, for example by a CI runner. Tunnel URIs don't have this problem: they default to the user that runs MariaDB Shell.
{% endhint %}

## Related Shell Options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `ssh.configFile` | string | empty | The default OpenSSH configuration file. If it is empty, `~/.ssh/config` is used. |
| `ssh.bufferSize` | integer | `10240` | The buffer size for tunnel data transfer, in bytes. |
