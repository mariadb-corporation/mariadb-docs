---
description: >-
  How the credential helpers of the MariaDB Shell credential store work, where
  they keep passwords, which characters they accept, and how to run them
  directly.
---

# Credential Helpers

The [credential store](../connecting/credential-store.md) hands passwords and secrets to a credential helper. This page describes the helpers themselves. For choosing a helper and managing stored passwords, see [Credential Store](../connecting/credential-store.md).

## Helper Executables

The helpers are separate executables named `mariadb-secret-store-<helper>`, installed next to the `mariadb-shell` binary. MariaDB Shell starts the helper for each operation and exchanges the data with it over standard input and output.

A development build may also include a `plaintext` helper. It is a test fixture, isn't part of the packages, and must not be used for real passwords.

## The login-path File

The `login-path` helper needs no daemon and no external tool: MariaDB Shell reads and writes `~/.mylogin.cnf` itself, in the format that MySQL's `mysql_config_editor` uses, so that tool and MariaDB Shell can read each other's entries. On Windows, the file is `%AppData%\MySQL\.mylogin.cnf`.

The file is AES-encrypted, but the key is stored in the file itself, so anyone who can read the file can recover the passwords. Its only protection is the file permissions. MariaDB Shell creates the file with mode `0600`. If you have an older file with looser permissions, tighten them with `chmod 600 ~/.mylogin.cnf`.

MariaDB Shell doesn't apply the connection settings in `~/.mylogin.cnf` at startup, and has no `--login-path` option. See [Option Files and Login Paths](../connecting/option-files-and-login-paths.md#login-paths).

## Password Characters

The helpers restrict which characters a stored password may contain. These limits don't apply to values stored with `shell.store_secret()`.

| Helper | Not allowed |
| --- | --- |
| `login-path` | The control characters `\0`, `0x03`, `0x04`, `\n`, `\r`, `0x0F`, `0x11`, `0x12`, `0x13`, `0x15`, `0x16`, `0x17`, `0x19`, `0x1A`, `0x1C`, and `0x7F`. |
| `keychain` | `\0` and `\n`. |
| `secret-service` | Anything that isn't valid UTF-8. |

## Running a Helper Directly

To find out why a helper doesn't work, run it with the `version` command. It exits with `0` when it is healthy, and otherwise prints the reason:

```sh
mariadb-secret-store-login-path version; echo "exit=$?"
mariadb-secret-store-secret-service version; echo "exit=$?"
```

For the messages that the helpers print and how to fix them, see [Troubleshooting](../connecting/credential-store.md#troubleshooting).
