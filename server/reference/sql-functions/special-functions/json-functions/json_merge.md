---
description: >-
  Merge JSON documents. This function merges two or more JSON documents into a
  single JSON document, preserving all keys and values.
---

# JSON\_MERGE

## Syntax

```sql
JSON_MERGE(json_doc, json_doc[, json_doc] ...)
```

## Description

Merges the given JSON documents.

Returns the merged result, or `NULL` if any argument is `NULL`.

An error occurs if any of the arguments are not valid JSON documents.

{% hint style="warning" %}
`JSON_MERGE` is deprecated. [JSON\_MERGE\_PATCH](json_merge_patch.md) is an RFC 7396-compliant replacement, and [JSON\_MERGE\_PRESERVE](json_merge_preserve.md) is a synonym.
{% endhint %}

## Example

```sql
SET @json1 = '[1, 2]';
SET @json2 = '[3, 4]';

SELECT JSON_MERGE(@json1,@json2);
+---------------------------+
| JSON_MERGE(@json1,@json2) |
+---------------------------+
| [1, 2, 3, 4]              |
+---------------------------+
```

## See Also

* [JSON\_MERGE\_PATCH](json_merge_patch.md)
* [JSON\_MERGE\_PRESERVE](json_merge_preserve.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
