---
description: >-
  Check validity of an IPv6 address. This function returns 1 if the argument is
  a valid IPv6 address string, and 0 otherwise.
---

# IS\_IPV6

## Syntax

```sql
IS_IPV6(expr)
```

## Description

Returns 1 if the expression is a valid IPv6 address specified as a string, otherwise returns 0. Does not consider IPv4 addresses to be valid IPv6 addresses.

## Examples

```sql
SELECT IS_IPV6('48f3::d432:1431:ba23:846f');
+--------------------------------------+
| IS_IPV6('48f3::d432:1431:ba23:846f') |
+--------------------------------------+
|                                    1 |
+--------------------------------------+
1 row in set (0.02 sec)

SELECT IS_IPV6('10.0.1.1');
+---------------------+
| IS_IPV6('10.0.1.1') |
+---------------------+
|                   0 |
+---------------------+
```

## See Also

* [INET6](../../../data-types/string-data-types/inet6.md) data type
* [INET6\_ATON](inet6_aton.md)
* [INET6\_NTOA](inet6_ntoa.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
