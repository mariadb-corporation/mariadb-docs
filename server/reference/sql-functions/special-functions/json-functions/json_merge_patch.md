---
description: >-
  Learn about JSON_MERGE_PATCH in MariaDB. This RFC 7396-compliant function
  merges JSON documents by overwriting duplicate keys, serving as a modern
  replacement for the deprecated JSON_MERGE.
---

# JSON\_MERGE\_PATCH

## Syntax

```sql
JSON_MERGE_PATCH(json_doc, json_doc[, json_doc] ...)
```

## Description

Merges the given JSON documents, returning the merged result, or `NULL` if any argument is `NULL`.

`JSON_MERGE_PATCH` is an RFC 7396-compliant replacement for [JSON\_MERGE](json_merge.md), which is deprecated.

Unlike [JSON\_MERGE\_PRESERVE](json_merge_preserve.md), members with duplicate keys are not preserved.

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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
