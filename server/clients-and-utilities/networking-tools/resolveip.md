---
description: >-
  Resolve host names to IP addresses and the reverse with the resolveip
  utility, useful when configuring host-based privileges.
---

# resolveip

resolveip is a utility for resolving IP addresses to host names and vice versa.

## Usage

```
resolveip [OPTIONS] hostname or IP-address
```

## Options

| Option | Description |
| - | - |
| Option | Description |
| -?, --help | Display help and exit. |
| -I, --info | Synonym for --help. |
| -s, --silent# | Be more silent. |
| -V, --version | Display version information and exit. |

## Examples

```bash
shell> resolveip mariadb.org
IP address of mariadb.org is 166.78.144.191
```

```bash
resolveip 166.78.144.191
Host name of 166.78.144.191 is mariadb.org
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
