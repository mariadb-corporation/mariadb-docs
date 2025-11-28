---
description: >-
  Get comprehensive query plans in JSON format. This output provides detailed
  optimizer data, including costs and attached conditions, not found in the
  tabular view.
---

# EXPLAIN FORMAT=JSON

## Synopsis

`EXPLAIN FORMAT=JSON` is a variant of [EXPLAIN](explain.md) command that produces output in JSON form. The output always has one row which has only one column titled "`JSON`". The contents are a JSON representation of the query plan:

```sql
EXPLAIN FORMAT=JSON SELECT * FROM t1 WHERE col1=1\G
```

```
*************************** 1. row ***************************
EXPLAIN: {
  "query_block": {
    "select_id": 1,
    "table": {
      "table_name": "t1",
      "access_type": "ALL",
      "rows": 1000,
      "filtered": 100,
      "attached_condition": "(t1.col1 = 1)"
    }
  }
}
```

## Output is different from MySQL

The output of MariaDB's `EXPLAIN FORMAT=JSON` is different from `EXPLAIN FORMAT=JSON` in MySQL. The reasons for that are:

* MySQL's output has deficiencies.
* The output of MySQL's `EXPLAIN FORMAT=JSON` is not defined. Even MySQL Workbench has trouble parsing it (see this [blog post](https://s.petrunia.net/blog/?p=93)).
* MariaDB has query optimizations that MySQL does not have. This means that MariaDB generates query plans that MySQL does not generate.

## Output Format

TODO: MariaDB's output format description.

## See Also

* [ANALYZE FORMAT=JSON](analyze-format-json.md) produces output like `EXPLAIN FORMAT=JSON`, but amended with the data from query execution.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
