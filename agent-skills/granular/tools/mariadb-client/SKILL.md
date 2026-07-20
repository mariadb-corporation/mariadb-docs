---
name: mariadb-client
description: "MariaDB-specific behavior of the `mariadb` command-line client — batch mode auto-enables silent/tab output, `\\G`/`\\g` and client-side `DELIMITER` for stored-routine bodies, `--safe-updates` sets `max_join_size` (no `sql_` prefix) not `sql_max_join_size`, default charset auto-detects from locale rather than defaulting to latin1, and `mysql` is a kept symlink for the same binary. Use when writing, generating, or reviewing shell commands, scripts, or docs that invoke the mariadb CLI."
---

# mariadb Command-Line Client

*Last updated: 2026-07-20*

`mariadb` is the interactive/batch SQL shell for MariaDB, built on GNU readline. The binary is `mariadb` (since 10.5); a symlink named `mysql` is kept on Unix for compatibility, and `mysql.exe` ships as an alternate binary on Windows — both invoke the identical client.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Pipes a script and expects the usual box-drawn table output | Non-interactive input (piped stdin, `< file.sql`, `-e`, `--batch`) auto-switches to **tab-separated, unboxed** output and disables the history file — this is `--batch`'s effect, triggered automatically, not just via the flag. Force table output back with `--table`/`-t` |
| Sets `--safe-updates` and then writes `SET sql_max_join_size=...` to raise the join-size cap | That variable name **doesn't exist** — the session variable is `max_join_size` (no `sql_` prefix). `--safe-updates` itself sends `SET SQL_SAFE_UPDATES=1, SQL_SELECT_LIMIT=n, MAX_JOIN_SIZE=n` as an init command; only two of the three carry the `sql_` prefix |
| Assumes the client defaults to `latin1` because older docs said so | The client auto-detects the character set from the OS locale (`LC_CTYPE` on Unix) at connect time; if that fails, it falls back to the server's compiled-in default, **`utf8mb4`** — not `latin1`. Force one explicitly with `--default-character-set=name` |
| Writes a stored routine body over the CLI and lets each internal `;` end the statement | The client, not the server, splits statements on the delimiter. Wrap `BEGIN…END` blocks: `DELIMITER //` … body ending `END //` … `DELIMITER ;`. `DELIMITER` is a client-side command, invisible to the server and to other clients |
| Ends every statement the same way and expects table output for one long row | Terminate that one statement with `\G` (or `ego`) instead of `;` for vertical (one-line-per-column) output — no flag needed, and it works even under a custom `DELIMITER` |
| Puts `-p mypassword` (space before the password) on the command line | `-p` takes no separated argument — `-p mypassword` is parsed as `-p` (prompts) plus a positional `mypassword` database name. Use `-pmypassword` (no space) or, better, `--password` with no value to be prompted; a password on the command line is visible in shell history and briefly in the process list |
| Assumes `-e "sql"` behaves like interactive mode, just non-interactive | `-e`/`--execute` forces batch output, disables `--force`, and skips the history file — same code path as `--batch` (`status.batch=1`) |
| Writes `UPDATE`/`DELETE` scripts for an agent to run unsupervised and worries about a missing `WHERE` | `--safe-updates` (alias `--i-am-a-dummy`, `-U`) blocks `UPDATE`/`DELETE` unless the `WHERE` uses a key or a `LIMIT` is given, caps `SELECT` at `select_limit` rows (default 1000) and joins at `max_join_size` row combinations (default 1,000,000) |
| Assumes TLS server-certificate verification is opt-in like older MariaDB versions | *(since 11.4)* `--ssl` is on by default, and `--ssl-verify-server-cert` is now **on by default** too (previously off) — use `--skip-ssl-verify-server-cert` to opt out |
| Reaches for `mysql_history` env var name to disable the history file | The variable is `MYSQL_HISTFILE` (default `~/.mysql_history`); point it at `/dev/null` or symlink the file there |

## Invocation & Naming

```bash
mariadb db_name
mariadb --user=user_name --password db_name   # prompts for the password
mariadb db_name < script.sql > output.tab      # batch: tab-separated output
```

Companion option groups read from option files: `[mysql]`, `[mariadb-client]`, `[client]`, `[client-server]`, `[client-mariadb]` — in that order, so a `mariadb-client` group entry can override a broader `[client]` one for this binary specifically.

## Connection Options

| Flag | Short | Notes |
|---|---|---|
| `--host=` | `-h` | Connect to a host; `localhost` triggers the Unix socket, `127.0.0.1` forces TCP |
| `--port=` | `-P` | Default `3306`, resolved via option file / `$MYSQL_TCP_PORT` / built-in default |
| `--socket=` | `-S` | Unix socket path (or named-pipe name on Windows) |
| `--user=` | `-u` | Defaults to the current OS user |
| `--password[=]` | `-p` | No value → prompt. `-p` (short form) must **not** have a space before the value |
| `--protocol=` | | `tcp`, `socket`, `pipe`, or `memory` — forces the transport |
| `--ssl` / `--ssl-ca=` / `--ssl-cert=` / `--ssl-key=` | | TLS is enabled automatically once any `--ssl-*` option is set |
| `--ssl-verify-server-cert` | | On by default *(since 11.4)*; `--skip-ssl-verify-server-cert` to disable |
| `--default-character-set=` | | Force a charset instead of auto-detecting from the locale |
| `--defaults-file=` / `--no-defaults` / `--defaults-extra-file=` / `--defaults-group-suffix=` | | Must be the **first** argument if given |
| `--max-allowed-packet=` | | Default 16 MiB, min 4 KiB, max 2 GiB |
| `--reconnect` | | On by default: auto-reconnects once on a dropped connection, silently losing session state (temp tables, `@vars`, current transaction). Disable with `--skip-reconnect` to fail loudly instead |
| `--connect-timeout=` | | Seconds before giving up; default `0` (no timeout) |

## Batch vs. Interactive

Interactive use (a TTY) defaults to boxed table output and keeps a history file (`~/.mysql_history`, override via `$MYSQL_HISTFILE`). Batch mode — triggered by `--batch`/`-B`, `-e`/`--execute`, or simply piping/redirecting input — switches to tab-separated output, disables the history file, and enables `--silent`. Force table-style output back in batch mode with `--table`/`-t`; force vertical with `--vertical`/`-E` or a trailing `\G`.

```bash
mariadb appdb -e "SELECT id, name FROM users LIMIT 5"   # batch-style output, no TTY needed
mariadb appdb < migration.sql                            # runs a script, non-interactively
```

`--force`/`-f` continues past SQL errors in a script instead of aborting (also flips `--abort-source-on-error` off for the `source` command); `--verbose`/`-v` (repeatable, `-vvv` = table format) and `--unbuffered`/`-n` (flush after every query) are the other common batch-script flags.

## Client Commands

These run inside the shell, not sent to the server; each has a backslash shortcut and, unless `--binary-mode` is set, must start the line:

| Command | Shortcut | Effect |
|---|---|---|
| `go` | `\g` | Send the statement (default terminator, same as `;`) |
| `ego` | `\G` | Send the statement, display the result **vertically** |
| `delimiter` | `\d` | Change the statement terminator — client-side only, needed for `BEGIN…END` bodies |
| `source` | `\.` | Run a `.sql` script file |
| `tee` | `\T` | Append all output to a file (`notee`/no-arg `\t` to stop) |
| `pager` | `\P` | Pipe result output through a pager (Unix only; falls back to `$PAGER`) |
| `edit` | `\e` | Open the current statement in `$EDITOR` |
| `status` | `\s` | Show connection info, including which protocol was actually used |
| `system` | `\!` | Run a shell command (Unix only) |
| `prompt` | `\R` | Change the prompt (see sequences below) |
| `charset` | `\C` | Switch the client's session character set |
| `use` | `\u` | Switch the default database |
| `connect` | `\r` | Reconnect, optionally to a different db/host |
| `clear` | `\c` | Discard the statement typed so far |
| `warnings`/`nowarning` | `\W`/`\w` | Toggle auto-`SHOW WARNINGS` after every statement |
| `help` | `\h` | In-client help; `help <topic>` also queries server-side `HELP` |

`prompt` sequences worth knowing: `\d` current database, `\h` host, `\u` user, `\p` port/socket, `\R`/`\r` time (24h/12h), `\v` server version, `\_` space, `\n` newline. Set a persistent one with `--prompt=` or the `PROMPT` environment variable.

*(since 12.0)* `--script-dir=` scopes where `source` looks for script files, instead of the working directory. *(since 10.6.18, backported across all current branches)* `--sandbox` / the `\-` command disable filesystem-touching commands (`system`, `tee`, `source`, `pager` with an argument) for the rest of the session — useful when piping untrusted SQL through the client.

## Output Formats

| Flag | Short | Effect |
|---|---|---|
| `--batch` | `-B` | Tab-separated, one row per line; implies `--silent`, skips history |
| `--table` | `-t` | Boxed ASCII table (interactive default) |
| `--vertical` | `-E` | One column per line, per row — same as ending a statement with `\G` |
| `--xml` | `-X` | XML output |
| `--html` | `-H` | HTML `<table>` output |
| `--raw` | `-r` | In batch/silent output, stop escaping `\n \t \0 \\` — needed for exact-bytes piping |
| `--skip-column-names` | `-N` | Omit the header row |
| `--silent` | `-s` | Less chatty; repeatable for progressively less output |

## Safety for Scripted/Unattended Use

`--safe-updates` (aka `--i-am-a-dummy`, both map to `-U`) is the guardrail for agent-generated `UPDATE`/`DELETE`: it refuses to run either statement unless the `WHERE` clause references a key or a `LIMIT` is present, and it issues `SET SQL_SAFE_UPDATES=1, SQL_SELECT_LIMIT=<n>, MAX_JOIN_SIZE=<n>` as the connection's init command. Tune the caps with `--select-limit=` (default 1000) and `--max-join-size=` (default 1,000,000) — note the session variable behind the second one is `max_join_size`, without the `sql_` prefix that `sql_safe_updates`/`sql_select_limit` carry.

```bash
mariadb --safe-updates --select-limit=500 --max-join-size=10000 appdb
```

`--local-infile[=0|1]` toggles whether `LOAD DATA LOCAL INFILE` is even offered to the server (it also needs server-side `local_infile=1` to actually work) — leave it off for scripts that ingest untrusted file paths.

## Character Set

The client does **not** hardcode `latin1`. At connect time it resolves the charset from, in order: an explicit `--default-character-set=`, then the OS locale (`LC_CTYPE` on Unix, the console code page on Windows), then the compiled-in server default (`utf8mb4`). If terminal output looks mangled, set `--default-character-set=utf8mb4` (or `auto`) explicitly rather than assuming a `latin1` default that no longer applies.

## Examples

```bash
# One-shot query, script-friendly output:
mariadb appdb -e "SELECT COUNT(*) FROM orders"

# Run a migration, stop on the first error, log everything:
mariadb --force appdb < migration.sql | tee migration.log

# Safe interactive session for ad hoc fixes on production:
mariadb --safe-updates -h prod-db -u app_ro appdb

# Vertical output for a wide row, custom delimiter for a routine body:
mariadb appdb <<'SQL'
DELIMITER //
CREATE PROCEDURE demo() BEGIN SELECT 1; END //
DELIMITER ;
SELECT * FROM orders WHERE id = 42\G
SQL
```

## See Also

- **`mariadb-dump`** / **`mariadb-import`** — the round-trip partners; dumps are restored by piping into this client (`mariadb dbname < dump.sql`)
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/clients-and-utilities/mariadb-client/mariadb-command-line-client>
  - <https://mariadb.com/docs/server/clients-and-utilities/mariadb-client/mysql-command-line-client>
  - <https://mariadb.com/docs/server/clients-and-utilities/mariadb-client>
