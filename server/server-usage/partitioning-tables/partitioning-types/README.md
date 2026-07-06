---
description: >-
  Explore different partitioning types for MariaDB Server tables. Understand
  range, list, hash, and key partitioning to optimize data management and
  improve query performance.
---

# Partitioning Types

{% columns %}
{% column %}
{% content-ref url="partitioning-types-overview.md" %}
[partitioning-types-overview.md](partitioning-types-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to the various partitioning strategies available in MariaDB, helping you choose the right method for your data distribution needs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hash-partitioning-type.md" %}
[hash-partitioning-type.md](hash-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about HASH partitioning, which distributes data based on a user-defined expression to ensure an even spread of rows across partitions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="key-partitioning-type.md" %}
[key-partitioning-type.md](key-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand KEY partitioning, similar to HASH but using MariaDB's internal hashing function on one or more columns to distribute data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="linear-hash-partitioning-type.md" %}
[linear-hash-partitioning-type.md](linear-hash-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore LINEAR HASH partitioning, a variation of HASH that uses a powers-of-two algorithm for faster partition management at the cost of distribution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="linear-key-partitioning-type.md" %}
[linear-key-partitioning-type.md](linear-key-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about LINEAR KEY partitioning, which combines the internal key hashing with a linear algorithm for efficient partition handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="list-partitioning-type.md" %}
[list-partitioning-type.md](list-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand LIST partitioning, where rows are assigned to partitions based on whether a column value matches one in a defined list of values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="range-columns-and-list-columns-partitioning-types.md" %}
[range-columns-and-list-columns-partitioning-types.md](range-columns-and-list-columns-partitioning-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover these variants that allow partitioning based on multiple columns and non-integer types, offering greater flexibility than standard RANGE/LIST.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="range-partitioning-type.md" %}
[range-partitioning-type.md](range-partitioning-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The RANGE partitioning type assigns rows to partitions based on whether column values fall within contiguous, non-overlapping ranges.
{% endcolumn %}
{% endcolumns %}
