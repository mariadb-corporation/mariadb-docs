---
description: >-
  Call util, shell, and sandbox operations directly from the operating system
  shell with mariadb-shell -- <object> <operation>, passing positional, named,
  list, and dictionary arguments.
---

# Command Line Integration

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

Command line integration runs one operation of a MariaDB Shell global object straight from the operating system shell, without a prompt and without writing a Python script. It maps a command such as

```sh
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop --output-url=/backups/shop --threads=8
```

to the Python call

```python
util.dump_schemas("shop", {"outputUrl": "/backups/shop", "threads": 8})
```

Use it in shell scripts, cron jobs, and CI pipelines, where a single operation with a few options is all you need.

## Syntax

```text
mariadb-shell [options] [URI] -- <object> [<nested object>] <operation> [arguments]
```

* Everything before `--` is a normal shell option, such as the connection URI, `--log-level`, or `--passwords-from-stdin`.
* After `--` come the object, the operation, and its arguments. No other shell options can follow.
* Operations that work on a server, such as dumps and diagnostics, use the global session from the URI. Operations that don't need a server, such as `sandbox deploy` or `shell list-credential-helpers`, need no URI.

The shell runs the operation, prints its return value, if any, and exits. Lists and dictionaries are printed as JSON.

## Available Objects and Operations

| Object | Operations |
| --- | --- |
| `util` | `copy-instance`, `copy-schemas`, `copy-tables`, `dump-instance`, `dump-schemas`, `dump-tables`, `export-table`, `import-table`, `load-dump` |
| `util debug` | `collect-diagnostics`, `collect-high-load-diagnostics`, `collect-slow-query-diagnostics` |
| `shell` | `status`, `list-credential-helpers`, `list-credentials`, `store-credential`, `delete-credential`, `delete-all-credentials`, `list-secrets`, `read-secret`, `store-secret`, `delete-secret`, `delete-all-secrets`, `list-sql-handlers` |
| `shell options` | `set-persist`, `unset-persist` |
| `sandbox` | `deploy`, `start`, `stop`, `kill`, `delete`, `vendor`, `version`, `get-path` |

Other global objects, such as `mysql` and `plugins`, aren't available on the command line. Plugins can make their own functions available by registering them with `cli=True`. See [Plugins](../extending-mariadb-shell/plugins.md).

A nested object follows its parent after a space: write `util debug collect-diagnostics` and `shell options set-persist`, not `util.debug` or `shell.options`.

### Getting Help

Add `--help` at any level to list what's available or to show the arguments of an operation:

```sh
mariadb-shell -- --help
mariadb-shell -- util --help
mariadb-shell -- util debug --help
mariadb-shell -- util dump-schemas --help
```

The help of an operation shows its syntax in command line form, such as `util dump-schemas <schemas> --outputUrl=<str> [<options>]`, and lists each option with its type.

## Naming Styles

Operation and option names can be written in camelCase, as in the help, or in kebab-case. The following commands are equivalent:

```sh
mariadb-shell mariadb://dba@localhost -- util dumpSchemas shop --outputUrl=/backups/shop --dryRun
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop --output-url=/backups/shop --dry-run
```

## Arguments

Arguments are positional or named. Positional arguments fill the parameters of the operation in order. Named arguments, which start with `--`, become the keys of the options dictionary that most operations take as their last parameter.

```text
[positional argument]* [{ named argument* }]* [named argument]*
```

### Positional Arguments

A positional argument is a single value. The shell converts it to the type that the parameter expects:

| Value | Type |
| --- | --- |
| `shop`, `"Desk lamp"` | String. Quote values that contain spaces, as your operating system shell requires. |
| `42` | Integer |
| `0.5` | Float |
| `true`, `false`, `1`, `0` | Boolean |
| `null` | `null`. Only a parameter that accepts any type takes it; a parameter with a declared type, such as a string or an integer, rejects it. |
| `[1,"a"]`, `{"key":1}` | List or dictionary, written as JSON. Quote it so that the operating system shell passes it unchanged. |

A value that is valid JSON takes its JSON type, and anything else is a string: `-` is the string `-`, not `null`.

### Named Arguments

A named argument has one of these forms:

| Form | Meaning |
| --- | --- |
| `--name=value` | Sets the option to the value. |
| `--name value` | Same as `--name=value`. |
| `--name` | Sets a Boolean option to `true`. |
| `--name:type=value` | Sets the option and states the type of the value explicitly. The types are `str`, `int`, `uint`, `float`, `bool`, `null`, `list`, `dict`, and `json`. |

The shell checks each named argument against the options that the operation accepts. An unknown option or a value of the wrong type stops the call with exit code `10`:

```text
ERROR: Argument error at '--threads=abc': UInteger expected, but value is String
```

Without an explicit type, the shell converts the value to the type that the option expects. The explicit type matters for options that accept values of more than one type.

### Lists

For a parameter or option that takes a list, pass the items separated by commas. To use a comma inside an item, escape it as `\,` or quote the item:

```sh
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop,sakila --output-url=/backups/two
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop --output-url=/backups/shop \
  --exclude-tables=shop.audit_log,shop.session_cache
```

You can also repeat the option. Each occurrence adds items to the list:

```sh
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop --output-url=/backups/shop \
  --exclude-tables=shop.audit_log --exclude-tables=shop.session_cache
```

A JSON array works as well. Quote it so that the operating system shell passes it unchanged:

```sh
mariadb-shell mariadb://dba@localhost -- util dump-schemas '["shop","sakila"]' --output-url=/backups/two
```

### Dictionaries

For an option that takes a dictionary, pass each entry as `key=value`, and repeat the option for more entries. The following command imports a CSV file into `shop.product` and doubles the value of the third field on the way:

```sh
mariadb-shell mariadb://dba@localhost -- util import-table products.csv \
  --schema=shop --table=product --dialect=csv-unix \
  --columns=id,name,1,in_stock --decode-columns=price='@1 * 2'
```

You can also pass the whole dictionary as JSON, quoted so that the operating system shell passes it unchanged. The entries are merged with any given as `key=value`. A key can contain dots, as in the `schema.table` keys of the dump `where` option:

```sh
mariadb-shell mariadb://dba@localhost -- util dump-tables shop orders \
  --output-url=/backups/recent-orders --where='{"shop.orders": "id > 1000"}'
```

### Grouping Named Arguments

Named arguments at the end of the command go into the last parameter. When an operation takes more than one dictionary, enclose the named arguments for an earlier one in braces, separated by spaces. The braces are separate arguments and must be quoted in most operating system shells:

```sh
mariadb-shell mariadb://dba@localhost -- util dump-schemas shop '{' --output-url=/backups/shop --dry-run '}'
```

## Examples

### Dump Schemas

```sh
mariadb-shell mariadb://backup@db1.example.com -- util dump-schemas shop,sakila \
  --output-url=/backups/$(date +%F) --threads=8 --compression=zstd
```

### Load a Dump

```sh
mariadb-shell mariadb://dba@db2.example.com -- util load-dump /backups/2026-10-01 \
  --threads=8 --ignore-version
```

### Export a Table to CSV

```sh
mariadb-shell mariadb://dba@localhost -- util export-table shop.product /tmp/product.csv \
  --dialect=csv-unix
```

### Collect Diagnostics

```sh
mariadb-shell mariadb://dba@db1.example.com -- util debug collect-diagnostics /tmp/db1-diag.zip \
  --schema-stats
```

See [Diagnostics Utilities](../utilities/diagnostics-utilities.md) for the options.

### Show the Connection Status

```sh
mariadb-shell mariadb://dba@db1.example.com -- shell status
```

The output is the same as that of `\status`. See [Shell Commands](shell-commands.md#status).

### Persist a Shell Option

```sh
mariadb-shell -- shell options set-persist resultFormat vertical
mariadb-shell -- shell options unset-persist resultFormat
```

### Manage Sandboxes

```sh
mariadb-shell -- sandbox deploy 3310 --password=sandbox-pw
mariadb-shell -- sandbox stop 3310
mariadb-shell -- sandbox delete 3310
```

See [Sandbox Instances](../sandbox-instances.md).

## Exit Codes

| Exit code | Meaning |
| --- | --- |
| `0` | The operation succeeded. |
| `1` | The operation failed, for example because of a server error or an invalid path. |
| `10` | The command line was invalid: an unknown object, operation, or option, or a value of the wrong type. |

For other exit codes of the shell, see [Batch Execution](batch-execution.md#exit-codes).

<sub>_This page is licensed: GPLv2_</sub>
