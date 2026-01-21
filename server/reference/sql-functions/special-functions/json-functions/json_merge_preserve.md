---
description: >-
  Explore JSON_MERGE_PRESERVE in MariaDB. This function merges JSON documents
  while keeping all members, including those with duplicate keys, effectively
  acting as a synonym for the legacy JSON_MERGE.
---

# JSON\_MERGE\_PRESERVE

## Syntax

```sql
JSON_MERGE_PRESERVE(json_doc, json_doc[, json_doc] ...)
```

## Description

Merges the given JSON documents, returning the merged result, or `NULL` if any argument is `NULL`.

`JSON_MERGE_PRESERVE` is a synonym for [JSON\_MERGE](json_merge.md), which has been deprecated.

Unlike [JSON\_MERGE\_PATCH](json_merge_patch.md), members with duplicate keys are preserved.

## Example

```sql
SET @json1 = '[1, 2]';
SET @json2 = '[2, 3]';
SELECT JSON_MERGE_PATCH(@json1,@json2),JSON_MERGE_PRESERVE(@json1,@json2);
+---------------------------------+------------------------------------+
| JSON_MERGE_PATCH(@json1,@json2) | JSON_MERGE_PRESERVE(@json1,@json2) |
+---------------------------------+------------------------------------+
| [2, 3]                          | [1, 2, 2, 3]                       |
+---------------------------------+------------------------------------+
```

## See Also

* [JSON\_MERGE\_PATCH](json_merge_patch.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
