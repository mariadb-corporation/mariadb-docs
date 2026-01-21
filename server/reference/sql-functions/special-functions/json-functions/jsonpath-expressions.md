---
description: >-
  Understand JSONPath syntax. This guide explains how to use JSONPath to select
  and extract specific elements, objects, or arrays from JSON documents.
---

# JSONPath Expressions

A number of [JSON functions](./) accept JSON Path expressions. MariaDB defines this path as follows:

## JSON Path Syntax

```sql
path : ['lax'] '$' [step]*
```

The path starts with an optional _path mode_. At the moment, MariaDB supports only the "lax" mode, which is also the mode that is used when it is not explicitly specified.

The `$` symbol represents the context item. The search always starts from the context item; because of that, the path always starts with `$`.

Then, it is followed by zero or more steps, which select element(s) in the JSON document. A step may be one of the following:

* Object member selector.
* Array element selector.
* Wildcard selector.

### Object Member Selector

To select member(s) in a JSON object, one can use one of the following:

* `.memberName` selects the value of the member with name memberName.
* `."memberName"` - the same as above but allows one to select a member with a name that's not a valid identifier (that is, has space, dot, and/or other characters).
* `.*` - selects the values of all members of the object.

If the current item is an array (instead of an object), nothing will be selected.

### Array Element Selector

To select elements of an array, one can use one of the following:

* `[N]` selects element number N in the array. The elements are counted from zero.
* `[*]` selects all elements in the array.

If the current item is an object (instead of an array), nothing will be selected.

{% tabs %}
{% tab title="Current" %}
JSON path supports negative indexes in an array, 'last' keyword and range notation ('to' keyword) for accessing array elements. Negative indexes start from -1.

* `[-N]` selects n th element from end.
* `[last-N]` selects n th element from the last element.
* `[M to N]` selects range of elements starting from index M to N.

Example:

```sql
SET @json='{
            "A": [0,
                  [1, 2, 3],
                  [4, 5, 6],
                  "seven",
                   0.8,
                   true,
                   false,
                   "eleven",
                  [12, [13, 14], {"key1":"value1"},[15]],
                  true],
            "B": {"C": 1},
            "D": 2
           }';
SELECT JSON_EXTRACT(@json, '$.A[-8][1]');
+--------------------------------------------------+
| JSON_EXTRACT(@json, '$.A[-8][1]')                |
+--------------------------------------------------+
| 5                                                |
+--------------------------------------------------+

SELECT JSON_EXTRACT(@json, '$.A[last-7][1]');
+-----------------------------------------------+
| SELECT JSON_EXTRACT(@json, '$.A[last-7][1]'); |
+-----------------------------------------------+
| 5                                             |
+-----------------------------------------------+


SET @json= '[
             [1, {"key1": "value1"}, 3],
             [false, 5, 6],
             [7, 8, [9, {"key2": 2}, 11]],
             [15, 1.34, [14], ["string1", [16, {"key1":[1,2,3,[4,5,6]]}, 18]]],
             [19, 20],
             21, 22
            ]';

SELECT JSON_EXTRACT(@json, '$[0 to 3][2]');
+-----------------------------------------------+
| JSON_EXTRACT(@json, '$[0 to 3][2]')           |
+-----------------------------------------------+
| [3, 6, [9, {"key2": 2}, 11], [14]]            |
+-----------------------------------------------+
```
{% endtab %}

{% tab title="< 10.9" %}
JSON path does **not** support negative indexes in an array.
{% endtab %}
{% endtabs %}

This produces output for first index of eighth from last element of a two dimensional array.

Note: In range notation, when M > N ( when M,N are greater than or equal to 0) or (size of array - M or size of array - N when M, N are less than 0), then it is treated as an impossible range and `NULL` is returned.

```sql
SET @json= '[1, 2, 3, 4, 5]';
SELECT JSON_EXTRACT(@json, '$[4 to 2]');
+-----------------------------------+
| JSON_EXTRACT(@json, '$[4 to 2]')  |
+-----------------------------------+
| NULL                              |
+-----------------------------------+
```

### Wildcard

The wildcard step, `**`, recursively selects all child elements of the current element. Both array elements and object members are selected.

The wildcard step must not be the last step in the JSONPath expression. It must be followed by an array or object member selector step.

For example, this query selects all object members named `price` in the document:

```sql
SELECT json_extract(@json_doc, '$**.price');
```

This query, however, selects the second element in each of the arrays present in the document:

```sql
SELECT json_extract(@json_doc, '$**[2]');
```

## Compatibility

MariaDB's JSONPath syntax supports a subset of JSON Path's definition in the SQL Standard. The most notable things not supported are the `strict` mode and filters.

MariaDB's JSONPath is close to MySQL's JSONPath. The wildcard step ( `**` ) is a non-standard extension that has the same meaning as in MySQL. The difference between MariaDB and MySQL's JSONPath is: MySQL doesn't allow one to specify the mode explicitly (but uses `lax` mode implicitly).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
