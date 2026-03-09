---
description: >-
  Learn about LINEAR KEY partitioning, which combines the internal key hashing
  with a linear algorithm for efficient partition handling.
---

# LINEAR KEY Partitioning Type

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
PARTITION BY LINEAR KEY [ALGORITHM={MYSQL51|MYSQL55|BASE31|CRC32C|XXH32|XXH3}]
([column_names])
[PARTITIONS (number_of_partitions)]
```

For a description of the different `ALGORITHM` types, see [KEY Partitioning](key-partitioning-type.md).
{% endtab %}

{% tab title="< 12.3" %}
```sql
PARTITION BY LINEAR KEY ([column_names])
[PARTITIONS (number_of_partitions)]
```
{% endtab %}
{% endtabs %}

## Description

`LINEAR KEY` partitioning is a form of [partitioning](../), similar to [KEY partitioning](key-partitioning-type.md).

`LINEAR KEY` partitioning makes use of a powers-of-two algorithm, while `KEY` partitioning uses modulo arithmetic to determine the partition number.

Adding, dropping, merging and splitting partitions is much faster than with the [KEY partitioning type](key-partitioning-type.md); however, data is less likely to be evenly distributed over the partitions.

## Example

```sql
CREATE OR REPLACE TABLE t1 (v1 INT)
  PARTITION BY LINEAR KEY (v1)
  PARTITIONS 2;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
