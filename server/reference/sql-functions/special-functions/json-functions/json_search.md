---
description: >-
  Search for a value in a JSON document. This function returns the path to the
  given string within a JSON document.
---

# JSON\_SEARCH

## Syntax

```sql
JSON_SEARCH(json_doc, return_arg, search_str[, escape_char[, path] ...])
```

## Description

Returns the path to the given string within a JSON document, or `NULL` if any of _json\_doc_, _search\_str_ or a path argument is `NULL`; if the search string is not found, or if no path exists within the document.

A warning will occur if the JSON document is not valid, any of the path arguments are not valid, if _return\_arg_ is neither _one_ nor _all_, or if the escape character is not a constant. `NULL` will be returned.

_return\_arg_ can be one of two values:

* `'one`: Terminates after finding the first match, so will return one path string. If there is more than one match, it is undefined which is considered first.
* `all`: Returns all matching path strings, without duplicates. Multiple strings are autowrapped as an array. The order is undefined.

## Examples

```sql
SET @json = '["A", [{"B": "1"}], {"C":"AB"}, {"D":"BC"}]';

SELECT JSON_SEARCH(@json, 'one', 'AB');
+---------------------------------+
| JSON_SEARCH(@json, 'one', 'AB') |
+---------------------------------+
| "$[2].C"                        |
+---------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
