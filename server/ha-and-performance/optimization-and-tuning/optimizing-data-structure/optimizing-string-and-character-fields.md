---
description: >-
  Optimizing string and character columns, including matching character sets
  and collations for faster comparisons.
---

# Optimizing String and Character Fields

## Comparing String Columns

When values from different columns are compared, the comparison runs more quickly when the columns are of the same character set and collation. If they are different, the strings need to be converted while the query runs. So, where possible, declare string columns using the same character set and collation when you may need to compare them.

## VARCHAR vs BLOB

ORDER BY and GROUP BY clauses can generate temporary tables in memory (see [MEMORY Storage Engine](../../../server-usage/storage-engines/memory-storage-engine.md)) if the original table doesn't contain any BLOB fields. If a column is less than 8KB, you can make use of a Binary VARCHAR rather than a BLOB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
