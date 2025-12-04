---
description: >-
  Discover JSON_DEPTH in MariaDB. This function returns the maximum depth of a
  JSON document, assigning a depth of 1 to scalars and empty structures, and
  higher values for nested data.
---

# JSON\_DEPTH

## Syntax

```sql
JSON_DEPTH(json_doc)
```

## Description

Returns the maximum depth of the given JSON document, or `NULL` if the argument is null. An error occurs if the argument is an invalid JSON document.

* Scalar values or empty arrays or objects have a depth of 1.
* Arrays with only scalar values and objects with only scalar values for all keys have depth of 1.
* In all other cases, the depth can be 2 or greater.

{% tabs %}
{% tab title="12.2" %}
There is no maximum depth level — it's unlimited.

For more information, see [this blog post](https://mariadb.org/make-json-depth-unlimited-new-feature-in-mariadb-12-1/).
{% endtab %}

{% tab title="< 12.2" %}
The maximum depth is 32.
{% endtab %}
{% endtabs %}

## Examples

```sql
SELECT JSON_DEPTH('[]'), JSON_DEPTH('true'), JSON_DEPTH('{}');
+------------------+--------------------+------------------+
| JSON_DEPTH('[]') | JSON_DEPTH('true') | JSON_DEPTH('{}') |
+------------------+--------------------+------------------+
|                1 |                  1 |                1 |
+------------------+--------------------+------------------+

SELECT JSON_DEPTH('[1, 2, 3]'), JSON_DEPTH('[[], {}, []]');
+-------------------------+----------------------------+
| JSON_DEPTH('[1, 2, 3]') | JSON_DEPTH('[[], {}, []]') |
+-------------------------+----------------------------+
|                       2 |                          2 |
+-------------------------+----------------------------+

SELECT JSON_DEPTH('[1, 2, [3, 4, 5, 6], 7]');
+---------------------------------------+
| JSON_DEPTH('[1, 2, [3, 4, 5, 6], 7]') |
+---------------------------------------+
|                                     3 |
+---------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
