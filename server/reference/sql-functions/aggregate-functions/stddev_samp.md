---
description: >-
  Calculate sample standard deviation. This function computes the standard
  deviation assuming the set of values represents a sample of the population.
---

# STDDEV\_SAMP

## Syntax

```sql
STDDEV_SAMP(expr)
```

## Description

Returns the sample standard deviation of `expr` (the square root of [VAR\_SAMP()](var_samp.md)).

It is an [aggregate function](./), and so can be used with the [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md) clause.

`STDDEV_SAMP()` can be used as a [window function](../special-functions/window-functions/).

`STDDEV_SAMP()` returns `NULL` if there were no matching rows.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
