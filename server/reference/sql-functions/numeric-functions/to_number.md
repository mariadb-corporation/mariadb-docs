---
description: >-
  Convert a string to a number. This Oracle-compatible function parses a string
  using a specified format and returns a numeric value.
---

# TO\_NUMBER

{% hint style="info" %}
`TO_NUMBER` is available from [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.2/mariadb-12.2-changes-and-improvements).
{% endhint %}

`TO_NUMBER` converts an expression to the [NUMERIC](../../data-types/numeric-data-types/numeric.md) data type.

## Syntax

```sql
TO_NUMBER(number_or_string_subject)
TO_NUMBER(string_subject,string_format)
```

## Description

The function returns the `DOUBLE` data type for all signatures and input data types.

The format parser understands the following components:

* Digits: 0, 9
* Hex digits: X
* Group separators: comma (`,`) and G
* Decimal delimiters: period (`.`) and D
* Approximate number signature: EEEE
* Currency/numeric flags: $ and B
* Currency signatures: C, L, U
* Sign signatures: S, MI, PR
* Special format signatures: V, TM, TM9, TME
* Format flag: FM

The function was introduced for Oracle compatibility, but does not include the following features:

* The `ON CONVERSION ERROR` clause
* The third parameter (nlsparam)
* Internationalized components: G, D, C, L, U

These features are planned to be be implemented via [MDEV-36978](https://jira.mariadb.org/browse/MDEV-36978).

## Examples

```sql
SELECT TO_NUMBER('100.00');
+---------------------+
| TO_NUMBER('100.00') |
+---------------------+
|                 100 |
+---------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
