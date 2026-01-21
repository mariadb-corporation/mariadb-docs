---
description: >-
  Convert an IPv4 address to an integer. This function takes a dotted-quad IP
  string (e.g., '1.2.3.4') and returns its numeric representation.
---

# INET\_ATON

## Syntax

```sql
INET_ATON(expr)
```

## Description

Given the dotted-quad representation of an IPv4 network address as a string, returns an integer that represents the numeric value of the address. Addresses may be 4- or 8-byte addresses.

Returns `NULL` if the argument is not understood.

## Examples

```sql
SELECT INET_ATON('192.168.1.1');
+--------------------------+
| INET_ATON('192.168.1.1') |
+--------------------------+
|               3232235777 |
+--------------------------+
```

This is calculated as follows: 192 x 2563 + 168 x 256 2 + 1 x 256 + 1.

## See Also

* [INET6\_ATON()](inet6_aton.md)
* [INET\_NTOA()](inet_ntoa.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
