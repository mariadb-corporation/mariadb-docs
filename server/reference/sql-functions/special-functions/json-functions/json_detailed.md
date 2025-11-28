---
description: >-
  Explore JSON_DETAILED in MariaDB. Also known as JSON_PRETTY, this function
  formats JSON documents with indentation and newlines to emphasize nested
  structures for readability.
---

# JSON\_DETAILED

## Syntax

```sql
JSON_DETAILED(json_doc[, tab_size])
JSON_PRETTY(json_doc[, tab_size])
```

## Description

Represents JSON in the most understandable way emphasizing nested structures.

{% tabs %}
{% tab title="Current" %}
`JSON_PRETTY` is an alias for `JSON_DETAILED` .
{% endtab %}

{% tab title="< 10.10.3 / 10.9.5 / 10.8.7 / 10.7.8 / 10.6.12 / 10.5.19 / 10.4.28" %}
`JSON_PRETTY` is **not** available as an alias for `JSON_DETAILED` .
{% endtab %}
{% endtabs %}

## Example

```sql
SET @j = '{ "A":1,"B":[2,3]}';

SELECT @j;
+--------------------+
| @j                 |
+--------------------+
| { "A":1,"B":[2,3]} |
+--------------------+

SELECT JSON_DETAILED(@j);
+------------------------------------------------------------+
| JSON_DETAILED(@j)                                          |
+------------------------------------------------------------+
| {
    "A": 1,
    "B": 
    [
        2,
        3
    ]
} |
+------------------------------------------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_DETAILED.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
