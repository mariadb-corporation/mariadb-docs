---
title: JSON Arrow Operators
description: >-
  The MariaDB 13.1 JSON arrow operators -> and ->>: shorthand for
  JSON_EXTRACT() and JSON_UNQUOTE(JSON_EXTRACT()), added for MySQL 5.7
  compatibility. Syntax, string-literal path restriction, chaining, and
  quoting behavior.
# EDITORIAL NOTE (remove before publishing): Feature is on the
# preview-13.1-preview branch only and not yet merged to main as of this
# writing. Confirm the "MariaDB 13.1" version against the release notes
# before this page goes live.
---

# JSON Arrow Operators

## Syntax

```bnf
json_doc -> path
json_doc ->> path
```

## Description

{% hint style="info" %}
The `->` and `->>` operators were introduced in **MariaDB 13.1** for MySQL 5.7 compatibility.
{% endhint %}

The `->` and `->>` operators are shorthand for extracting a value from a JSON document by a [JSONPath expression](jsonpath-expressions.md):

* `json_doc -> path` is equivalent to [`JSON_EXTRACT(json_doc, path)`](json_extract.md).
* `json_doc ->> path` is equivalent to [`JSON_UNQUOTE`](json_unquote.md)`(`[`JSON_EXTRACT`](json_extract.md)`(json_doc, path))`.

Both operators are purely syntactic sugar: they build the same expression as the equivalent function calls and inherit their `NULL` and error behavior. On the left, `json_doc` is any JSON expression — typically a column, a function result, or a JSON literal.

The two operators differ only in quoting:

* `->` returns the extracted value in its JSON representation, so a matched string keeps its surrounding double quotes (for example, `"Alice"`).
* `->>` additionally unquotes the result, returning the raw value (for example, `Alice`). Use `->>` when comparing against, sorting by, or displaying scalar values.

The following caveats apply and distinguish the operators from the underlying functions:

* **The path must be a string literal.** Unlike [`JSON_EXTRACT()`](json_extract.md), which accepts any expression as its path argument, the right-hand side of `->` and `->>` must be a literal string. A column, user variable (`data -> @path`), or placeholder (`data -> ?`) will not parse.
* **Chaining requires parentheses.** The operators do not chain directly; `col -> '$.a' -> '$.b'` is a syntax error. Wrap the intermediate result in parentheses instead: `(col -> '$.a') -> '$.b'`.
* **Precedence** is higher than the arithmetic and comparison operators, so `col ->> '$.age' = 30` is evaluated as `(col ->> '$.age') = 30`.

## Examples

Before MariaDB 13.1, only the function form (`JSON_EXTRACT()` / `JSON_UNQUOTE(JSON_EXTRACT())`) worked in MariaDB; the `->` and `->>` operator form was accepted only by MySQL. As of MariaDB 13.1 both forms work, so queries written for MySQL 5.7+ port across unchanged.

The function form works in both MySQL and MariaDB:

```sql
SELECT JSON_EXTRACT('{"id":"1", "name":"Name"}', '$.name') `name`;
+--------+
| name   |
+--------+
| "Name" |
+--------+

SELECT JSON_UNQUOTE(JSON_EXTRACT('{"id":"1", "name":"Name"}', '$.name')) `name`;
+------+
| name |
+------+
| Name |
+------+
```

The equivalent operator form worked only in MySQL before MariaDB 13.1, and now works in MariaDB too:

```sql
SELECT '{"id":"1", "name":"Name"}'->'$.name' `name`;
+--------+
| name   |
+--------+
| "Name" |
+--------+

SELECT '{"id":"1", "name":"Name"}'->>'$.name' `name`;
+------+
| name |
+------+
| Name |
+------+
```

As with the function form, `->` keeps the JSON quoting (`"Name"`) while `->>` returns the unquoted value (`Name`).

The operators can be used anywhere an expression is allowed, such as in a `WHERE` clause:

```sql
CREATE TABLE t1 (id INT, data JSON);
INSERT INTO t1 VALUES (1, '{"id":"1", "name":"Name"}');

SELECT id FROM t1 WHERE data->>'$.name' = 'Name';
+------+
| id   |
+------+
|    1 |
+------+
```

## See Also

* [JSON\_EXTRACT](json_extract.md) — the function `->` is shorthand for.
* [JSON\_UNQUOTE](json_unquote.md) — combined with `JSON_EXTRACT`, the function `->>` is shorthand for.
* [JSONPath Expressions](jsonpath-expressions.md) — the path syntax used on the right-hand side.
* [JSON\_VALUE](json_value.md) — related, but *not* equivalent: returns only scalar values, always unquoted.
* [JSON\_QUERY](json_query.md) — related, but *not* equivalent: returns only objects or arrays.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
