---
description: >-
  Available from version 11.2, this function compares two JSON arrays and
  returns a new array containing only the items present in both.
---

# JSON\_ARRAY\_INTERSECT

{% hint style="info" %}
`JSON_ARRAY_INTERSECT` is available from MariaDB 11.2.
{% endhint %}

## Syntax

```sql
JSON_ARRAY_INTERSECT(arr1, arr2)
```

## Description

Finds intersection between two json arrays and returns an array of items found in both array.

## Examples

```sql
SET @json1= '[1,2,3]';
SET @json2= '[1,2,4]';

SELECT json_array_intersect(@json1, @json2); 
+--------------------------------------+
| json_array_intersect(@json1, @json2) |
+--------------------------------------+
| [1, 2]                               |
+--------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
