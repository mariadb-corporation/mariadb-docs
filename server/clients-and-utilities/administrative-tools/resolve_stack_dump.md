---
description: >-
  resolve_stack_dump resolves the numeric stack trace from a mariadbd crash
  into symbol names, using a symbols file produced by nm.
---

# resolve\_stack\_dump

`resolve_stack_dump` is a tool that resolves numeric stack strace dumps into symbols.

## Usage

```bash
resolve_stack_dump [OPTIONS] symbols-file [numeric-dump-file]
```

The symbols-file should include the output from: `nm --numeric-sort mariadbd`. The numeric-dump-file should contain a numeric stack trace from mariadbd. If the numeric-dump-file is not given, the stack trace is read from stdin.

## Options

| Option                         | Description                          |
| ------------------------------ | ------------------------------------ |
| -h, --help                     | Display this help and exit.          |
| -V, --version                  | Output version information and exit. |
| -s, --symbols-file=_name_      | Use specified symbols file.          |
| -n, --numeric-dump-file=_name_ | Read the dump from specified file.   |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
