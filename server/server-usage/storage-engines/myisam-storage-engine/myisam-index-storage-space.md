---
description: >-
  This page explains how MyISAM stores and compresses indexes, detailing space
  usage for different key types and compression strategies.
---

# MyISAM Index Storage Space

Regular [MyISAM](./) tables make use of [B-tree indexes](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md#b-tree-indexes).

String indexes are space-compressed, which reduces the size of [VARCHARs](../../../reference/data-types/string-data-types/varchar.md) that don't use the full length, or a string that has trailing spaces. String indexes also make use of prefix-compression, where strings with identical prefixes are compressed.

Numeric indexes can also be prefix-compressed compressed if the [PACK\_KEYS=1](../../../reference/sql-statements/data-definition/create/create-table.md#table-options) option is used. Regardless, the high byte is always stored first, which allows a reduced index size.

In the worst case, with no strings being space-compressed, the total index storage space are (index\_length+4)/0.67 per index.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
