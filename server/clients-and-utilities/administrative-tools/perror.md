---
description: >-
  perror displays the description for a system or storage engine error code.
---

# perror

_perror_ is a utility that displays descriptions for system or storage engine error codes.

See [MariaDB Error Codes](../../reference/error-codes/) for a full list of MariaDB error codes, and [Operating System Error Codes](../../reference/error-codes/operating-system-error-codes.md) for a list of Linux and Windows error codes.

## Usage

```ini
perror [OPTIONS] [ERRORCODE [ERRORCODE...]]
```

If you need to describe a negative error code, use `--` before the first error code to end the options.

## Options

| Option        | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| -?, --help    | Display help and exit.                                                                   |
| -I, --info    | Synonym for --help.                                                                      |
| -s, --silent  | Only print the error message.                                                            |
| -v, --verbose | Print error code and message (default). (Defaults to on; use --skip-verbose to disable.) |
| -V, --version | Displays version information and exits.                                                  |

## Examples

System error code:

```bash
shell> perror 96
OS error code  96:  Protocol family not supported
```

MariaDB/MySQL error code:

```bash
shell> perror 1005 1006
MySQL error code 1005 (ER_CANT_CREATE_TABLE): Can't create table %`s.%`s (errno: %M)
MySQL error code 1006 (ER_CANT_CREATE_DB): Can't create database '%-.192s' (errno: %M)
```

```bash
shell> perror --silent 1979
You are not owner of query %lu
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
