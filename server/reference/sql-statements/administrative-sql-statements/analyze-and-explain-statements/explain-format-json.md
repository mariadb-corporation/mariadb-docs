---
description: >-
  Get comprehensive query plans in JSON format. This output provides detailed
  optimizer data, including costs and attached conditions, not found in the
  tabular view.
---

# EXPLAIN FORMAT=JSON

## Synopsis

`EXPLAIN FORMAT=JSON` is a variant of the [EXPLAIN](explain.md) command that produces output in JSON form. The output always has one row with a single column titled `EXPLAIN`. The contents are a JSON representation of the query plan:

{% hint style="info" %}
For [ANALYZE FORMAT=JSON](analyze-format-json.md), the column is titled `ANALYZE` instead.
{% endhint %}

Given a table `t1` holding 100 rows, with a case-insensitive collation:

```sql
CREATE TABLE t1 (
  col1 VARCHAR(32),
  col2 VARCHAR(32),
  col3 CHAR(32),
  col4 TEXT,
  KEY(col1),
  KEY(col2),
  KEY(col3),
  KEY(col4(32))
) COLLATE utf8mb3_general_ci;
```

```sql
EXPLAIN FORMAT=JSON SELECT * FROM t1 WHERE UPPER(col1)=UPPER(col2)\G
```

```
*************************** 1. row ***************************
EXPLAIN: {
  "query_block": {
    "select_id": 1,
    "cost": 0.0256761,
    "nested_loop": [
      {
        "table": {
          "table_name": "t1",
          "access_type": "ALL",
          "loops": 1,
          "rows": 100,
          "cost": 0.0256761,
          "filtered": 100,
          "attached_condition": "t1.col2 = t1.col1"
        }
      }
    ]
  }
}
```

Table access is nested inside a `nested_loop` array, except in a plan that only carries a message, such as `{"table": {"message": "Impossible WHERE"}}`.

Because `t1` uses a case-insensitive collation, `UPPER()` does not change the result of the comparison, so the optimizer removes it from the indexed columns to make the condition sargable. `attached_condition` therefore reports the simplified condition. This rewrite is controlled by the `sargable_casefold` [optimizer switch](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch.md), which is enabled by default.

Cost values depend on the data, the server build, and the hardware, so the exact figures vary between servers.

## Output is different from MySQL

The output of MariaDB's `EXPLAIN FORMAT=JSON` is different from `EXPLAIN FORMAT=JSON` in MySQL. The reasons for that are:

* MySQL's output has deficiencies.
* The output of MySQL's `EXPLAIN FORMAT=JSON` is not defined. Even MySQL Workbench has trouble parsing it (see this [blog post](https://web.archive.org/web/20200218115814/http://s.petrunia.net:80/blog/?p=93)).
* MariaDB has query optimizations that MySQL does not have. This means that MariaDB generates query plans that MySQL does not generate.

## Output Format

TODO: MariaDB's output format description.

## See Also

* [ANALYZE FORMAT=JSON](analyze-format-json.md) produces output like `EXPLAIN FORMAT=JSON`, but amended with the data from query execution.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
