---
description: >-
  Return the length of a JSON document. This function returns the length of a
  JSON document or, if a path is given, the length of the value within the path.
---

# JSON\_LENGTH

## Syntax

```sql
JSON_LENGTH(json_doc[, path])
```

## Description

Returns the length of a JSON document, or, if the optional path argument is given, the length of the value within the document specified by the path.

Returns `NULL` if any of the arguments argument are null or the path argument does not identify a value in the document.

An error occurs if the JSON document is invalid, the path is invalid or if the path contains a `*` or `**` wildcard.

Length will be determined as follow:

* A scalar's length is always 1.
* If an array, the number of elements in the array.
* If an object, the number of members in the object.

The length of nested arrays or objects are not counted.

## Examples

```
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
