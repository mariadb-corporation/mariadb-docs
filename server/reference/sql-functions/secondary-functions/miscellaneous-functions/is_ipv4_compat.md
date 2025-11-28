---
description: >-
  Check if an IPv6 address is IPv4-compatible. This function returns 1 if the
  binary IPv6 address represents an IPv4-compatible address.
---

# IS\_IPV4\_COMPAT

## Syntax

```sql
IS_IPV4_COMPAT(expr)
```

## Description

Returns 1 if a given numeric binary string IPv6 address, such as returned by [INET6\_ATON()](inet6_aton.md), is IPv4-compatible, otherwise returns 0.

{% tabs %}
{% tab title="Current" %}
When the argument is not [INET6](../../../data-types/string-data-types/inet6.md), automatic implicit [CAST](../../string-functions/cast.md) to INET6 is applied. As a consequence, `IS_IPV4_COMPAT` now understands arguments in both text representation and binary(16) representation.
{% endtab %}

{% tab title="< 10.5" %}
The function understands only binary(16) representation.
{% endtab %}
{% endtabs %}

## Examples

```sql
SELECT IS_IPV4_COMPAT(INET6_ATON('::10.0.1.1'));
+------------------------------------------+
| IS_IPV4_COMPAT(INET6_ATON('::10.0.1.1')) |
+------------------------------------------+
|                                        1 |
+------------------------------------------+

SELECT IS_IPV4_COMPAT(INET6_ATON('::48f3::d432:1431:ba23:846f'));
+-----------------------------------------------------------+
| IS_IPV4_COMPAT(INET6_ATON('::48f3::d432:1431:ba23:846f')) |
+-----------------------------------------------------------+
|                                                         0 |
+-----------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
