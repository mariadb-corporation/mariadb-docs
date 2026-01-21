---
description: >-
  Overview of the SHOW statement syntax. Learn how to use patterns and WHERE
  clauses to filter output from various SHOW statements.
---

# About SHOW

`SHOW` provides information about various aspects of MariaDB Server. A list of the various `SHOW` statements is [here](./).

The general syntax is:

```sql
SHOW LIKE 'pattern' | WHERE expr
```

The `LIKE` and `WHERE` clauses make sense only for particular `SHOW` statements, though. See [Extended SHOW](extended-show.md) for what `SHOW` statements benefit from using those clauses.

If the syntax for a given `SHOW` statement includes `LIKE 'pattern'` , `'pattern'` is a\
string that can contain the SQL `%` and `_` wildcard characters. The pattern is useful for\
restricting statement output to matching values.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
