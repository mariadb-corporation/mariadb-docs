---
description: >-
  CREATE PROCEDURE for MariaDB ColumnStore defines a stored procedure with
  named IN, OUT, and INOUT parameters and a routine body containing SQL
  statements.
---

# ColumnStore CREATE PROCEDURE

Creates a stored routine in ColumnStore.

## Syntax

```sql
CREATE
    [DEFINER = { user | CURRENT_USER }]
    PROCEDURE sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body

proc_parameter:
    [ IN | OUT | INOUT ] param_name type

type:
    Any valid MariaDB ColumnStore data type

routine_body:
    Valid SQL procedure statement
```

ColumnStore currently accepts definition of stored procedures with only input arguments and a single `SELECT` query while in Operating Mode = 1 (VTABLE mode). However, while in the Operating Mode = 0 (TABLE mode), ColumnStore will allow additional complex definition of stored procedures (i.e., OUT parameter, declare, cursors, etc.)

See Operating Mode for information on [Operating Modes](../columnstore-operating-mode.md).

The following statements create and call the `sp_complex_variable` stored procedure:

```sql
CREATE PROCEDURE sp_complex_variable(IN arg_key INT, IN arg_date DATE)
  BEGIN
    SELECT *
    FROM lineitem, orders
    WHERE o_custkey < arg_key
    AND l_partkey < 10000
    AND l_shipdate>arg_date
    AND l_orderkey = o_orderkey
    ORDER BY l_orderkey, l_linenumber;
  END

CALL sp_complex_variable(1000, '1998-10-10');
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
