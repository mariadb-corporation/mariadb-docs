---
description: >-
  This function escapes special characters in a string to make it safe for use
  in Mroonga full-text search queries.
---

# mroonga\_escape

## Syntax

```
mroonga_escape (string [,special_characters])
```

* `string` - required parameter specifying the text you want to escape
* `special_characters` - optional parameter specifying the characters to escape

## Description

`mroonga_escape` is a [user-defined function](../../../user-defined-functions/) (UDF) included with the [Mroonga storage engine](../), used for escaping a string. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

If no `special_characters` parameter is provided, by default `+-<>*()":` are escaped.

Returns the escaped string.

## Example

```sql
SELECT mroonga_escape("+-<>~*()\"\:");
'\\+\\-\\<\\>\\~\\*\\(\\)\\"\\:
```

## See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
