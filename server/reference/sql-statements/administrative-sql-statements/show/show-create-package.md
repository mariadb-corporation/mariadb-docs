---
description: >-
  View the CREATE PACKAGE statement. This statement returns the interface
  definition of a stored package in MariaDB.
---

# SHOW CREATE PACKAGE

## Syntax

```sql
SHOW CREATE PACKAGE  [ db_name . ] package_name
```

## Description

The `SHOW CREATE PACKAGE` statement can be used when [Oracle SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) is set. It shows the `CREATE` statement that creates the given package specification.

`SHOW CREATE PACKAGE` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.

## Examples

```sql
SHOW CREATE PACKAGE employee_tools\G
*************************** 1. row ***************************
             Package: employee_tools
            sql_mode: PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ORACLE,NO_KEY_OPTIONS,NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER
      Create Package: CREATE DEFINER="root"@"localhost" PACKAGE "employee_tools" AS
  FUNCTION getSalary(eid INT) RETURN DECIMAL(10,2);
  PROCEDURE raiseSalary(eid INT, amount DECIMAL(10,2));
  PROCEDURE raiseSalaryStd(eid INT);
  PROCEDURE hire(ename TEXT, esalary DECIMAL(10,2));
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## See Also

* [CREATE PACKAGE](../../data-definition/create/create-package.md)
* [DROP PACKAGE](../../data-definition/drop/drop-package.md)
* [CREATE PACKAGE BODY](../../data-definition/create/create-package-body.md)
* [SHOW CREATE PACKAGE BODY](show-create-package-body.md)
* [DROP PACKAGE BODY](../../data-definition/drop/drop-package-body.md)
* [Oracle SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
