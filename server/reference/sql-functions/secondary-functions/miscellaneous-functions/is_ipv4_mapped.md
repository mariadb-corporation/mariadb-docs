---
description: >-
  Check if an IPv6 address is IPv4-mapped. This function returns 1 if the binary
  IPv6 address represents an IPv4-mapped address.
---

# IS\_IPV4\_MAPPED

## Syntax

```sql
IS_IPV4_MAPPED(expr)
```

## Description

Returns 1 if a given a numeric binary string IPv6 address, such as returned by [INET6\_ATON()](inet6_aton.md), is a valid IPv4-mapped address, otherwise returns 0.

{% tabs %}
{% tab title="Current" %}
When the argument is not [INET6](../../../data-types/string-data-types/inet6.md), automatic implicit [CAST](../../string-functions/cast.md) to INET6 is applied. As a consequence, `IS_IPV4_MAPPED` now understands arguments in both text representation and binary(16) representation.
{% endtab %}

{% tab title="< 10.5" %}
The function understands only binary(16) representation.
{% endtab %}
{% endtabs %}

## Examples

```sql
SELECT IS_IPV4_MAPPED(INET6_ATON('::10.0.1.1'));
+------------------------------------------+
| IS_IPV4_MAPPED(INET6_ATON('::10.0.1.1')) |
+------------------------------------------+
|                                        0 |
+------------------------------------------+

SELECT IS_IPV4_MAPPED(INET6_ATON('::ffff:10.0.1.1'));
+-----------------------------------------------+
| IS_IPV4_MAPPED(INET6_ATON('::ffff:10.0.1.1')) |
+-----------------------------------------------+
|                                             1 |
+-----------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
