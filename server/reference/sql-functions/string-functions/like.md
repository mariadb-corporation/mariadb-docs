---
description: >-
  Pattern matching operator. This function tests whether a string matches a
  specified SQL pattern using wildcards like '%' and '_'.
---

# LIKE

## Syntax

```
expr LIKE pat [ESCAPE 'escape_char']
expr NOT LIKE pat [ESCAPE 'escape_char']
```

## Description

Tests whether _expr_ matches the pattern _pat_. Returns either 1 (`TRUE`) or 0 (`FALSE`).\
Both _expr_ and _pat_ may be any valid expression and are evaluated to strings.\
Patterns may use the following wildcard characters:

* `%` matches any number of characters, including zero.
* `_` matches any single character.

Use `NOT LIKE` to test if a string does not match a pattern. This is equivalent to using\
the [NOT](../../sql-structure/operators/comparison-operators/) operator on the entire `LIKE` expression.

If either the expression or the pattern is `NULL`, the result is `NULL`.

`LIKE` performs case-insensitive substring matches if the collation for the expression and pattern is case-insensitive. For case-sensitive matches, declare either argument to use a binary collation using collate, or coerce either of them to a [BINARY](../../data-types/string-data-types/binary.md) string using [CAST](cast.md). Use [SHOW COLLATION](../../sql-statements/administrative-sql-statements/show/show-collation.md) to get a list of\
available collations. Collations ending in `_bin` are case-sensitive.

Numeric arguments are coerced to binary strings.

The `_` wildcard matches a single character, not byte. It will only match a multi-byte character\
if it is valid in the expression's character set. For example, `_` will match `_utf8"€"`, but it\
will not match `_latin1"€"` because the Euro sign is not a valid latin1 character. If necessary,\
use [CONVERT](convert.md) to use the expression in a different character set.

If you need to match the characters `_` or `%`, you must escape them. By default, you can prefix the wildcard characters the backslash character `\` to escape them. The backslash is used both to encode special characters like newlines when a string is parsed as well as to escape wildcards in a pattern after parsing. Thus, to match an actual backslash, you sometimes need to double-escape it as `"\``\``\``\"`.

To avoid difficulties with the backslash character, you can change the wildcard escape character using `ESCAPE` in a `LIKE` expression. The argument to `ESCAPE` must be a single-character string.

## Examples

Select the days that begin with "T":

```sql
CREATE TABLE t1 (d VARCHAR(16));
INSERT INTO t1 VALUES 
  ("Monday"), ("Tuesday"), ("Wednesday"), 
  ("Thursday"), ("Friday"), ("Saturday"), ("Sunday");
SELECT * FROM t1 WHERE d LIKE "T%";
```

```sql
SELECT * FROM t1 WHERE d LIKE "T%";
+----------+
| d        |
+----------+
| Tuesday  |
| Thursday |
+----------+
```

Select the days that contain the substring "es":

```sql
SELECT * FROM t1 WHERE d LIKE "%es%";
```

```sql
SELECT * FROM t1 WHERE d LIKE "%es%";
+-----------+
| d         |
+-----------+
| Tuesday   |
| Wednesday |
+-----------+
```

Select the six-character day names:

```sql
SELECT * FROM t1 WHERE d like "___day";
```

```sql
SELECT * FROM t1 WHERE d like "___day";
+---------+
| d       |
+---------+
| Monday  |
| Friday  |
| Sunday  |
+---------+
```

With the default collations, `LIKE` is case-insensitive:

```sql
SELECT * FROM t1 WHERE d like "t%";
```

```sql
SELECT * FROM t1 where d like "t%";
+----------+
| d        |
+----------+
| Tuesday  |
| Thursday |
+----------+
```

Use [collate](../secondary-functions/information-functions/collation.md) to specify a binary collation, forcing case-sensitive matches:

```sql
SELECT * FROM t1 WHERE d like "t%" COLLATE latin1_bin;
```

```sql
SELECT * FROM t1 WHERE d like "t%" COLLATE latin1_bin;
Empty SET (0.00 sec)
```

You can include functions and operators in the expression to match. Select dates based on their day name:

```sql
CREATE TABLE t2 (d DATETIME);
INSERT INTO t2 VALUES
    ("2007-01-30 21:31:07"),
    ("1983-10-15 06:42:51"),
    ("2011-04-21 12:34:56"),
    ("2011-10-30 06:31:41"),
    ("2011-01-30 14:03:25"),
    ("2004-10-07 11:19:34");
SELECT * FROM t2 WHERE DAYNAME(d) LIKE "T%";
```

```sql
SELECT * FROM t2 WHERE DAYNAME(d) LIKE "T%";
+------------------+
| d                |
+------------------+
| 2007-01-30 21:31 |
| 2011-04-21 12:34 |
| 2004-10-07 11:19 |
+------------------+
3 rows in set, 7 warnings (0.00 sec)
```

## Optimizing LIKE

* MariaDB can use indexes for `LIKE` on string columns in the case where the LIKE doesn't start with `%` or `_`.
* You can set the [optimizer\_use\_condition\_selectivity](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_use_condition_selectivity) variable to 5. If this is done, then the optimizer will read [optimizer\_selectivity\_sampling\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_selectivity_sampling_limit) rows to calculate the selectivity of the `LIKE` expression before starting to calculate the query plan. This can help speed up some `LIKE` queries by providing the optimizer with more information about your data.

## See Also

* For searches on text columns, with results sorted by relevance, see [full-text](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) indexes.
* For more complex searches and operations on strings, you can use [regular expressions](regular-expressions-functions/), which were enhanced in MariaDB 10 (see [PCRE Regular Expressions](regular-expressions-functions/pcre.md)).
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
