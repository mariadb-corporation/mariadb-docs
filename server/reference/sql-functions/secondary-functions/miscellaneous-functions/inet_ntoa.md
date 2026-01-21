---
description: >-
  Convert an integer to an IPv4 address. This function takes a numeric IP value
  and returns its dotted-quad string representation.
---

# INET\_NTOA

## Syntax

```sql
INET_NTOA(expr)
```

## Description

Given a numeric IPv4 network address in network byte order (4 or 8 byte), returns the dotted-quad representation of the address as a string.

## Examples

```sql
SELECT INET_NTOA(3232235777);
+-----------------------+
| INET_NTOA(3232235777) |
+-----------------------+
| 192.168.1.1           |
+-----------------------+
```

192.168.1.1 corresponds to 3232235777 since 192 x 2563 + 168 x 256 2 + 1 x 256 + 1 = 3232235777.

## See Also

* [INET6\_NTOA()](inet6_ntoa.md)
* [INET\_ATON()](inet_aton.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
