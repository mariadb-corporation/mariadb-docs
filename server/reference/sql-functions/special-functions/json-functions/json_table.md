---
description: >-
  Convert JSON data to a relational table. This table function extracts data
  from a JSON document and returns it as a relational table with columns.
---

# JSON\_TABLE

{% hint style="info" %}
`JSON_TABLE` is available from MariaDB 10.6.
{% endhint %}

`JSON_TABLE` is a table function that converts JSON data into a relational form.

## Syntax

```sql
JSON_TABLE(json_doc, 
          context_path COLUMNS (column_list)
) [AS] alias
```

```sql
column_list:
    column[, column][, ...]
```

```sql
column:
    name FOR ORDINALITY
    |  name type PATH path_str [on_empty] [on_error]
    |  name type EXISTS PATH path_str
    |  NESTED PATH path_str COLUMNS (column_list)
```

```sql
on_empty:
    {NULL | DEFAULT string | ERROR} ON EMPTY
```

```sql
on_error:
    {NULL | DEFAULT string | ERROR} ON ERROR
```

## Description

`JSON_TABLE` can be used in contexts where a table reference can be used; in the `FROM` clause of a [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) statement, and in multi-table [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md)/[DELETE](../../../sql-statements/data-manipulation/changing-deleting-data/delete.md) statements.

`json_doc` is the JSON document to extract data from. In the simplest case, it is a string literal containing JSON. In more complex cases it can be an arbitrary expression returning JSON. The expression may have references to columns of other tables. However, one can only refer to tables that precede this JSON\_TABLE invocation. For RIGHT JOIN, it is assumed that its outer side precedes the inner. All tables in outer selects are also considered preceding.

`context_path` is a [JSON Path](jsonpath-expressions.md) expression pointing to a collection of nodes in `json_doc` that will be used as the source of rows.

The `COLUMNS` clause declares the names and types of the columns that JSON\_TABLE returns, as well as how the values of the columns are produced.

### Column Definitions

The following types of columns are supported:

#### Path Columns

```sql
name type PATH path_str [on_empty] [on_error]
```

Locates the JSON node pointed to by `path_str` and returns its value. The path\_str is evaluated using the current row source node as the context node.

```sql
SET @json='
[
  {"name":"Laptop", "color":"black", "price":"1000"},
  {"name":"Jeans",  "color":"blue"}
]';

SELECT * FROM json_table(@json, '$[*]' 
  COLUMNS(
   name  VARCHAR(10) path '$.name', 
   color VARCHAR(10) path '$.color',
   price DECIMAL(8,2) path '$.price' ) 
) AS jt;
+--------+-------+---------+
| name   | color | price   |
+--------+-------+---------+
| Laptop | black | 1000.00 |
| Jeans  | blue  |    NULL |
+--------+-------+---------+
```

The `on_empty` and `on_error` clauses specify the actions to be performed when the value was not found or there was an error condition. See the `ON EMPTY` and `ON ERROR` clauses section for details.

#### ORDINALITY Columns

```sql
name FOR ORDINALITY
```

Counts the rows, starting from 1.

Example:

```sql
set @json='
[
  {"name":"Laptop", "color":"black"},
  {"name":"Jeans",  "color":"blue"}
]';

select * from json_table(@json, '$[*]' 
  columns(
   id for ordinality, 
   name  varchar(10) path '$.name')
) as jt;
+------+--------+
| id   | name   |
+------+--------+
|    1 | Laptop |
|    2 | Jeans  |
+------+--------+
```

#### EXISTS PATH Columns

```sql
name type EXISTS PATH path_str
```

Checks whether the node pointed to by `value_path` exists. The `value_path` is evaluated using the current row source node as the context node.

```sql
set @json='
[
  {"name":"Laptop", "color":"black", "price":1000},
  {"name":"Jeans",  "color":"blue"}
]';

select * from json_table(@json, '$[*]' 
  columns(
   name  varchar(10) path '$.name',
   has_price integer exists path '$.price')
) as jt;
+--------+-----------+
| name   | has_price |
+--------+-----------+
| Laptop |         1 |
| Jeans  |         0 |
+--------+-----------+
```

#### NESTED PATHs

NESTED PATH converts nested JSON structures into multiple rows.

```sql
NESTED PATH path COLUMNS (column_list)
```

It finds the sequence of JSON nodes pointed to by `path` and uses it to produce rows. For each found node, a row is generated with column values as specified by the NESTED PATH's COLUMNS clause. If `path` finds no nodes, only one row is generated with all columns having NULL values.

For example, consider a JSON document that contains an array of items, and each item, in turn, is expected to have an array of its available sizes:

```json
SET @json='
[
  {"name":"Jeans",  "sizes": [32, 34, 36]},
  {"name":"T-Shirt", "sizes":["Medium", "Large"]},
  {"name":"Cellphone"}
]';
```

NESTED PATH allows one to produce a separate row for each size each item has:

```sql
select * from json_table(@json, '$[*]' 
  columns(
    name  varchar(10) path '$.name', 
    nested path '$.sizes[*]' columns (
      size varchar(32) path '$'
    )
  )
) as jt;
+-----------+--------+
| name      | size   |
+-----------+--------+
| Jeans     | 32     |
| Jeans     | 34     |
| Jeans     | 36     |
| T-Shirt   | Medium |
| T-Shirt   | Large  |
| Cellphone | NULL   |
+-----------+--------+
```

`NESTED PATH` clauses can be nested within one another. They can also be located next to each other. In that case, the nested path clauses will produce records one at a time. The ones that are not producing records will have all columns set to `NULL`.

Example:

```sql
set @json='
[
  {"name":"Jeans",  "sizes": [32, 34, 36], "colors":["black", "blue"]}
]';

select * from json_table(@json, '$[*]' 
  columns(
    name  varchar(10) path '$.name', 
    nested path '$.sizes[*]' columns (
      size varchar(32) path '$'
    ),
    nested path '$.colors[*]' columns (
      color varchar(32) path '$'
    )
  )
) as jt;

+-------+------+-------+
| name  | size | color |
+-------+------+-------+
| Jeans | 32   | NULL  |
| Jeans | 34   | NULL  |
| Jeans | 36   | NULL  |
| Jeans | NULL | black |
| Jeans | NULL | blue  |
+-------+------+-------+
```

### ON EMPTY and ON ERROR Clauses

The ON EMPTY clause specifies what will be done when the element specified by the search path is missing in the JSON document.

```sql
on_empty:
    {NULL | DEFAULT string | ERROR} ON EMPTY
```

When `ON EMPTY` clause is not present, `NULL ON EMPTY` is implied.

```sql
on_error:
    {NULL | DEFAULT string | ERROR} ON ERROR
```

The ON ERROR clause specifies what should be done if a JSON structure error occurs when trying to extract the value pointed to by the path expression. A JSON structure error here occurs only when one attempts to convert a JSON non-scalar (array or object) into a scalar value. When the `ON ERROR` clause is not present, `NULL ON ERROR` is implied.

**Note**: A datatype conversion error (e.g. attempt to store a non-integer value into an [integer](../../../data-types/numeric-data-types/int.md) field, or a [varchar](../../../data-types/string-data-types/varchar.md) column being truncated) is not considered a JSON error and so will not trigger the `ON ERROR` behavior. It will produce warnings, in the same way as [CAST(value AS datatype)](../../string-functions/cast.md) would.

### Replication

In the current code, evaluation of `JSON_TABLE` is deterministic, that is, for a given input string `JSON_TABLE` will always produce the same set of rows in the same order. However, one can think of JSON documents that one can consider identical which will produce different output. In order to be future-proof and withstand changes like

* sorting JSON object members by name (like MySQL does);
* changing the way duplicate object members are handled the function is marked as [unsafe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

### Extracting a Subdocument into a Column

{% tabs %}
{% tab title="Current" %}
```sql
SELECT * FROM JSON_TABLE('{"foo": [1,2,3,4]}','$' columns( jscol json path '$.foo') ) AS T;
+-----------+
| jscol     |
+-----------+
| [1,2,3,4] |
+-----------+
```
{% endtab %}

{% tab title="< 10.6.9" %}
`JSON_TABLE` does not allow to extract a JSON "subdocument" into a JSON column.

```sql
SELECT * FROM JSON_TABLE('{"foo": [1,2,3,4]}','$' columns( jscol json path '$.foo') ) AS T;
+-------+
| jscol |
+-------+
| NULL  |
+-------+
```
{% endtab %}
{% endtabs %}

## See Also

* [JSON Support](https://www.youtube.com/watch?v=ZkmwHPqA790) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
