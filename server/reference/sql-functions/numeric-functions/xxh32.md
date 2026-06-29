---
description: >-
  Compute a fast 32-bit xxHash. XXH32 returns the XXH32 hash of a text value as
  a 32-bit unsigned integer.
---

# XXH32

{% hint style="info" %}
`XXH32` was added in MariaDB 13.1.
{% endhint %}

## Syntax

```bnf
XXH32(expr)
```

## Description

`XXH32` returns a fast, non-cryptographic [xxHash](https://xxhash.com/) of a text value as a 32-bit number (`INT UNSIGNED`). It's useful for checksums, change detection, and grouping or bucketing rows. For a 64-bit result, use [XXH3()](xxh3.md).

The argument must be a text value: a string, `BLOB`/`TEXT`, `JSON`, `ENUM`, or `SET`. Numbers, dates, and other non-text values are rejected with an error; [CAST()](../string-functions/cast.md) them to a string first.

Hashing `NULL` returns `NULL`. Hashing an empty string returns `0`.

The result depends on the [collation](../../data-types/string-data-types/character-sets/), not on the raw bytes. Values that count as equal under the collation hash to the same number (for example, `'abc'` and `'ABC'` under a case-insensitive collation). The same text in a different character set or collation gives a different number.

{% hint style="warning" %}
When comparing a column to a value, keep both sides in the same collation. If the hashed column and the value use different collations, they won't match, so a hash-based index or lookup can quietly find nothing. Hash the binary form with `CAST(... AS BINARY)` (or the `BINARY` operator) when you want a byte-exact hash that ignores collation.
{% endhint %}

### Predicting the partition for KEY partitioning

The same XXH32 algorithm is available as a [KEY partitioning](../../../server-usage/partitioning-tables/partitioning-types/key-partitioning-type.md) algorithm (`PARTITION BY KEY ALGORITHM=XXH32`). For a table partitioned on a single column, the partition a value lands in is `MOD(XXH32(value), number_of_partitions)` — handy for knowing where a row will go, or for partition pruning. The collation rule above still applies: the value must use the column's collation to predict correctly.

This shortcut holds only for a plain, single-column `KEY`. It doesn't apply to [LINEAR KEY](../../../server-usage/partitioning-tables/partitioning-types/linear-key-partitioning-type.md) (unless the number of partitions is a power of two), to multi-column keys, or to `NULL` values (the server places those itself).

{% hint style="info" %}
`XXH3` is the 64-bit variant. The `XXH64()` and `XXH128()` functions are not part of this release.
{% endhint %}

## Examples

```sql
SELECT XXH32('abc');
+--------------+
| XXH32('abc') |
+--------------+
|    560666315 |
+--------------+
```

The result depends on the session collation, so a bare literal reproduces only under the same collation (the result above is for the default `utf8mb4_uca1400_ai_ci`). For a byte-exact hash that doesn't depend on collation, hash the binary form:

```sql
SELECT XXH32(CAST('abc' AS BINARY));
+------------------------------+
| XXH32(CAST('abc' AS BINARY)) |
+------------------------------+
|                    852579327 |
+------------------------------+
```

`NULL` and the empty string:

```sql
SELECT XXH32(NULL), XXH32('');
+-------------+-----------+
| XXH32(NULL) | XXH32('') |
+-------------+-----------+
|        NULL |         0 |
+-------------+-----------+
```

Equal values under a case-insensitive collation hash to the same number:

```sql
SELECT XXH32(_utf8mb4'ABC' COLLATE utf8mb4_general_ci)
     = XXH32(_utf8mb4'abc' COLLATE utf8mb4_general_ci) AS equal_ci;
+----------+
| equal_ci |
+----------+
|        1 |
+----------+
```

A non-text argument is rejected:

```sql
SELECT XXH32(11223344);
ERROR 4079 (HY000): Illegal parameter data type int for operation 'XXH32'
```

## See Also

* [XXH3()](xxh3.md) - the 64-bit variant
* [CRC32()](crc32.md), [CRC32C()](crc32c.md) - other non-cryptographic checksums

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
