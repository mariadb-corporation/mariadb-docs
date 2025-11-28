---
description: >-
  Check validity of an IPv4 address. This function returns 1 if the argument is
  a valid IPv4 address string, and 0 otherwise.
---

# IS\_IPV4

## Syntax

```sql
IS_IPV4(expr)
```

## Description

If the expression is a valid IPv4 address, returns 1, otherwise returns 0.

`IS_IPV4()` is stricter than [INET\_ATON()](inet_aton.md), but as strict as [INET6\_ATON()](inet6_aton.md), in determining the validity of an IPv4 address. This implies that if IS\_IPV4 returns 1, the same expression will always return a non-`NULL` result when passed to `INET_ATON()`, but that the reverse may not apply.

## Examples

```sql
SELECT IS_IPV4('1110.0.1.1');
+-----------------------+
| IS_IPV4('1110.0.1.1') |
+-----------------------+
|                     0 |
+-----------------------+

SELECT IS_IPV4('48f3::d432:1431:ba23:846f');
+--------------------------------------+
| IS_IPV4('48f3::d432:1431:ba23:846f') |
+--------------------------------------+
|                                    0 |
+--------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
