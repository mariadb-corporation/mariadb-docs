---
description: >-
  Convert an IPv6 address to binary. This function takes an IPv6 (or IPv4)
  address string and returns it as a VARBINARY(16) string.
---

# INET6\_ATON

## Syntax

```sql
INET6_ATON(expr)
```

## Description

Given an IPv6 or IPv4 network address as a string, returns a binary string that represents the numeric value of the address.

No trailing zone ID's or traling network masks are permitted. For IPv4 addresses, or IPv6 addresses with IPv4 address parts, no classful addresses or trailing port numbers are permitted and octal numbers are not supported.

The returned binary string will be [VARBINARY(16)](../../../data-types/string-data-types/varbinary.md) or [VARBINARY(4)](../../../data-types/string-data-types/varbinary.md) for IPv6 and IPv4 addresses respectively.

Returns `NULL` if the argument is not understood.

**MariaDB starting with** [**10.5.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes)

{% tabs %}
{% tab title="Current" %}
`INET6_ATON` can take [INET6](../../../data-types/string-data-types/inet6.md) as an argument.
{% endtab %}

{% tab title="< 10.5" %}
`INET6_ATON` **cannot** take [INET6](../../../data-types/string-data-types/inet6.md) as an argument.
{% endtab %}
{% endtabs %}

## Examples

```sql
SELECT HEX(INET6_ATON('10.0.1.1'));
+-----------------------------+
| HEX(INET6_ATON('10.0.1.1')) |
+-----------------------------+
| 0A000101                    |
+-----------------------------+

SELECT HEX(INET6_ATON('48f3::d432:1431:ba23:846f'));
+----------------------------------------------+
| HEX(INET6_ATON('48f3::d432:1431:ba23:846f')) |
+----------------------------------------------+
| 48F3000000000000D4321431BA23846F             |
+----------------------------------------------+
```

## See Also

* [INET6\_NTOA()](inet6_ntoa.md)
* [INET\_ATON()](inet_aton.md)
* [INET6](../../../data-types/string-data-types/inet6.md) Data Type

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
