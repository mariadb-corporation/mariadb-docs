---
description: >-
  Control operator precedence. Parentheses are used to group expressions and
  enforce the order of evaluation in complex operations.
---

# Parentheses

Parentheses are sometimes called precedence operators - this means that they can be used to change the other [operator's precedence](../../../sql-structure/operators/operator-precedence.md) in an expression. The expressions that are written between parentheses are computed before the expressions that are written outside. Parentheses must always contain an expression (that is, they cannot be empty), and can be nested.

For example, the following expressions could return different results:

* `NOT a OR b`
* `NOT (a OR b)`

In the first case, `NOT` applies to `a`, so if `a` is `FALSE` or `b` is `TRUE`, the expression returns `TRUE`. In the second case, `NOT` applies to the result of `a OR b`, so if at least one of `a` or `b` is `TRUE`, the expression is `TRUE`.

When the precedence of operators is not intuitive, you can use parentheses to make it immediately clear for whoever reads the statement.

The precedence of the `NOT` operator can also be affected by the `HIGH_NOT_PRECEDENCE` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) flag.

## Other uses

Parentheses must always be used to enclose [subqueries](../../../sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/).

Parentheses can also be used in a [JOIN](../../../sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) statement between multiple tables to determine which tables must be joined first.

Also, parentheses are used to enclose the list of parameters to be passed to built-in functions, user-defined functions and stored routines. However, when no parameter is passed to a stored procedure, parentheses are optional. For builtin functions and user-defined functions, spaces are not allowed between the function name and the open parenthesis, unless the `IGNORE_SPACE` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) is set. For stored routines (and for functions if `IGNORE_SPACE` is set) spaces are allowed before the open parenthesis, including tab characters and new line characters.

## Syntax errors

If there are more open parentheses than closed parentheses, the error usually looks like this:

```sql
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that
corresponds to your MariaDB server version for the right syntax to use near '' a
t line 1
```

Note the empty string.

If there are more closed parentheses than open parentheses, the error usually looks like this:

```sql
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that
corresponds to your MariaDB server version for the right syntax to use near ')'
at line 1
```

Note the quoted closed parenthesis.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
