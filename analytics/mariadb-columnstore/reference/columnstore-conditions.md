---
description: >-
  Reference for the conditions and operators usable in MariaDB ColumnStore
  WHERE clauses, including comparison, IN, BETWEEN, IS NULL, LIKE pattern
  matching, and EXISTS subqueries.
---

# ColumnStore Conditions

A condition is a combination of expressions and operators that return `TRUE`, `FALSE` or `NULL. The` following syntax shows the conditions that can be used to return a `TRUE`, `FALSE`, or `NULL` condition.

## Filter

```sql
filter:
column| literal| function [=|!=|<>|<|<=|>=|>] column| literal| function | select_statement
column| function [NOT] IN (select_statement | literal, literal,...)
column| function [NOT] BETWEEN (select_statement | literal, literal,...)
column| function  IS [NOT] NULL
string_column|string_function [NOT] LIKE pattern
EXISTS (select_statement)

NOT (filter)
(filter|function) [AND|OR] (filter|function)
```

{% hint style="info" %}
Note: A ‘literal’ may be a constant (e.g. 3) or an expression that evaluates to a constant \[e.g. 100 - (27 \* 3)]. For date columns, you may use the SQL ‘interval’ syntax to perform date arithmetic, as long as all the components of the expression are constants (e.g. ‘1998-12-01’ - interval ‘1’ year)
{% endhint %}

### String Comparisons

ColumnStore, unlike the MyISAM engine, is case sensitive for string comparisons used in filters. For the most accurate results, and to avoid confusing results, make sure string filter constants are no longer than the column width itself.

### Pattern Matching

Pattern matching as described with the LIKE condition allows you to use “_” to match any single character and “%” to match an arbitrary number of characters (including zero characters). To test for literal instances of a wildcard character, (“%” or “_”), precede it by the “\” character.

### OR Processing

OR Processing has the following restrictions:

* Only column comparisons against a literal are allowed in conjunction with an OR. The following query would be allowed since all comparisons are against literals. `SELECT count(*) from lineitem WHERE l_partkey < 100 OR l_linestatus =‘F‘;`
* ColumnStore binds AND’s more tightly than OR’s, just like any other SQLparser. Therefore you must enclose OR-relations in parentheses, just like in any other SQL parser.

```sql
SELECT COUNT(*) FROM orders, lineitem 
  WHERE (lineitem.l_orderkey < 100 OR lineitem.l_linenumber > 10) 
    AND lineitem.l_orderkey =orders.o_orderkey;
```

## table filter

The following syntax shows the conditions you can use when executing a condition against two columns. Note that the columns must be from the same table.

```sql
col_name_1 [=|!=|<>|<|<=|>=|>] col_name_2
```

## Join

The following syntax shows the conditions you can use when executing a join on two tables.

```sql
join_condition [AND join_condition]
join_condition:
           [col_name_1|function_name_1] = [col_name_2|function_name_2]
```

Notes:

* ColumnStore tables can only be joined with non-ColumnStore tables in table mode only. See Operating Mode for information.
* ColumnStore will require a join in the `WHERE` clause for each set of tables in the `FROM` clause. No cartesian product queries will be allowed.
* ColumnStore requires that joins must be on the same datatype. In addition, numeric datatypes (`INT` variations, `NUMERIC`, `DECIMAL`) may be mixed in the join if they have the same scale.
* Circular joins are not supported in ColumnStore. See the Troubleshooting section
* When the join memory limit is exceeded, a disk-based join will be used for processing if this option has been enabled.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
