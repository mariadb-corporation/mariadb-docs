---
description: >-
  Choose how MariaDB Shell prints query results: table, tabbed, vertical, JSON,
  and newline-delimited JSON, with column type information and result
  formatting from Python.
---

# Output Formats

MariaDB Shell prints query results in one of several formats. Tables suit reading at the prompt, tab-separated output suits shell pipelines, and JSON suits programs that consume the results.

## Available Formats

| Format | Description |
| --- | --- |
| `table` | Rows in a grid framed with ASCII characters. The default in interactive sessions. |
| `tabbed` | A header line and one line per row, with values separated by tabs and no frame. The default in batch mode. |
| `vertical` | Each row as a block, with one `column: value` line per column. |
| `json` | Same as `json/pretty`. |
| `json/pretty` | Each row as an indented JSON object. |
| `ndjson` | Same as `json/raw`. |
| `json/raw` | Each row as a compact JSON object on one line (newline-delimited JSON). |
| `json/array` | Compact JSON objects, one per line, enclosed in a JSON array. |

## Choosing the Format

| Method | Scope |
| --- | --- |
| `--result-format=<format>` | The whole session. Accepts all formats in the table above. |
| `--table` | Same as `--result-format=table`. Use it to get tables in batch mode. |
| `--tabbed` | Same as `--result-format=tabbed`. Use it to get tab-separated output in an interactive session. |
| `-E`, `--vertical` | Same as `--result-format=vertical`. |
| `--json[=pretty\|raw\|off]` | Wraps all shell output in JSON documents. See [JSON Output for Programs](#json-output-for-programs). |
| `resultFormat` option | Changes the format during the session with `\option resultFormat <format>`, or persists it with `\option --persist resultFormat <format>`. |
| `\G` terminator | Prints the result of one statement vertically, or in another format with a suffix. See [Format for One Statement](#format-for-one-statement). |

```sh
mariadb-shell mariadb://dba@localhost/shop --result-format=ndjson -e "SELECT id, email FROM customer"
```

If you don't choose a format, the shell uses `table` when it runs interactively and `tabbed` in batch mode. A format that you set explicitly applies in both.

### Format for One Statement

In SQL mode, the `\G` terminator selects a format for a single statement without changing the `resultFormat` option. On its own, `\G` prints the result vertically. A letter after it selects another format:

| Terminator | Output |
| --- | --- |
| `\G` | Vertical. |
| `\Gj` | A JSON array with one object per row. |
| `\GJ` | A JSON document with the rows and the result metadata, as described in [JSON Output for Programs](#json-output-for-programs). |
| `\GT` | Tab-separated values with a header line. |
| `\Gt` | Tab-separated values without a header line. |

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT id, email FROM customer\Gj
[
    {
        "id": 1,
        "email": "ana@example.com"
    },
    {
        "id": 2,
        "email": "li@example.com"
    }
]
```

The terminators work in interactive and batch mode. `\GT` and `\Gt` have no effect when the shell runs with `--json`.

## Examples

The examples use the following query on a small `customer` table.

{% tabs %}
{% tab title="table" %}
```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT * FROM customer;
+----+-----------------+------------+
| id | email           | created    |
+----+-----------------+------------+
|  1 | ana@example.com | 2026-01-12 |
|  2 | li@example.com  | 2026-03-02 |
+----+-----------------+------------+
2 rows in set (0.0002 sec)
```

Numbers are right-aligned, other values left-aligned.
{% endtab %}

{% tab title="tabbed" %}
```text
id	email	created
1	ana@example.com	2026-01-12
2	li@example.com	2026-03-02
```

In batch mode, the row count line isn't printed.
{% endtab %}

{% tab title="vertical" %}
```text
*************************** 1. row ***************************
     id: 1
  email: ana@example.com
created: 2026-01-12
*************************** 2. row ***************************
     id: 2
  email: li@example.com
created: 2026-03-02
2 rows in set (0.0001 sec)
```
{% endtab %}

{% tab title="json" %}
```json
{
    "id": 1,
    "email": "ana@example.com",
    "created": "2026-01-12"
}
{
    "id": 2,
    "email": "li@example.com",
    "created": "2026-03-02"
}
```

The output is a sequence of JSON objects, not a single JSON document.
{% endtab %}

{% tab title="ndjson" %}
```json
{"id":1,"email":"ana@example.com","created":"2026-01-12"}
{"id":2,"email":"li@example.com","created":"2026-03-02"}
```
{% endtab %}

{% tab title="json/array" %}
```json
[
{"id":1,"email":"ana@example.com","created":"2026-01-12"},
{"id":2,"email":"li@example.com","created":"2026-03-02"}
]
```

The output of each statement is one valid JSON document.
{% endtab %}
{% endtabs %}

## Value Conversion in JSON Formats

In the JSON formats, the shell maps column values to JSON types:

| Column type | JSON value |
| --- | --- |
| Integer types | Number |
| `FLOAT`, `DOUBLE` | Number |
| `DECIMAL` | Number, with all the digits of the value, such as `24.90` |
| `NULL` | `null` |
| `JSON` | The JSON value itself, embedded as object or array. |
| Date and time types | String, such as `"2026-01-12"` or `"2026-01-01 10:00:00"` |
| Binary types (`BINARY`, `VARBINARY`, `BLOB`) | Base64-encoded string |
| Other types | String |

## JSON Output for Programs

`--json` goes further than `--result-format=json`: it turns all output of the shell into JSON, including messages, warnings, errors, and text printed by Python code. Each item is a separate JSON document. A program that runs the shell can then parse everything it reads from standard output.

| Value | Output |
| --- | --- |
| `--json` or `--json=pretty` | Indented JSON documents. |
| `--json=raw` | One compact JSON document per line. |
| `--json=off` | Normal output. |

For an SQL statement, the document describes the whole result:

```sh
$ mariadb-shell mariadb://dba@localhost/shop --json=raw -e "SELECT id, email FROM customer"
{"hasData":true,"rows":[{"id":1,"email":"ana@example.com"},{"id":2,"email":"li@example.com"}],"executionTime":"0.0001 sec","affectedItemsCount":0,"warningsCount":0,"warnings":[],"info":"","autoIncrementValue":0}
```

| Field | Description |
| --- | --- |
| `hasData` | `true` if the statement returned a result set. |
| `rows` | The rows, as JSON objects. |
| `executionTime` | The execution time. |
| `affectedItemsCount` | Rows changed by a DML statement. |
| `warningsCount`, `warnings` | The number of warnings and the warnings themselves. |
| `info` | The server's information string, such as `Rows matched: 3  Changed: 0  Warnings: 0`. |
| `autoIncrementValue` | The `AUTO_INCREMENT` value generated by an `INSERT`. |

Other output has its own documents, keyed by type:

```json
{"warning":"Using a password on the command line interface can be insecure.\n"}
{"info":"hi"}
{"error":{"code":1146,"line":1,"message":"Table 'shop.nope' doesn't exist","state":"42S02","type":"MySQL Error"}}
```

## Column Type Information

`--column-type-info` prints the metadata of each result column before the result, in SQL mode. Use it to check how the server types an expression, or which collation a column uses. The option `showColumnTypeInfo` does the same and can be changed during the session.

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT id, price FROM product WHERE id = 1;
Field 1
Name:      `id`
Org_name:  `id`
Catalog:   `def`
Database:  `shop`
Table:     `product`
Org_table: `product`
Type:      Integer
DbType:    LONG
Collation: binary (63)
Length:    11
Decimals:  0
Flags:     NOT_NULL PRI_KEY AUTO_INCREMENT NUM PART_KEY

Field 2
Name:      `price`
Org_name:  `price`
Catalog:   `def`
Database:  `shop`
Table:     `product`
Org_table: `product`
Type:      Decimal
DbType:    NEWDECIMAL
Collation: binary (63)
Length:    10
Decimals:  2
Flags:     NUM

+----+-------+
| id | price |
+----+-------+
|  1 | 24.90 |
+----+-------+
1 row in set (0.0001 sec)
```

`Name` and `Table` show the names as they appear in the result, which can be aliases. `Org_name` and `Org_table` show the underlying column and table. `Type` is the shell's type name and `DbType` the protocol type the server reported.

In Python, the same metadata is available from the `columns` property of a result. See [SQL and Python Modes](sql-and-python-modes.md#column-metadata).

## Formatting Results in Python

`shell.dump_rows(result[, format])` prints a result object from `session.run_sql()` in any of the formats above and returns the number of rows it printed. Without a format, it uses `table`, regardless of the `resultFormat` option:

```text
MariaDB localhost:3306 ssl  shop  Py > shell.dump_rows(session.run_sql("SELECT id, name FROM product WHERE id < 3"), "vertical")
*************************** 1. row ***************************
  id: 1
name: Desk lamp
*************************** 2. row ***************************
  id: 2
name: Office chair
2
```

`dump_rows()` reads the rows from the result, so you can't fetch them again afterward. Use it in reports and scripts that print query results:

{% code title="stock_report.py" %}
```python
res = session.run_sql("SELECT name, price FROM product WHERE in_stock = 0")
count = shell.dump_rows(res, "tabbed")
print(f"{count} products out of stock")
```
{% endcode %}
