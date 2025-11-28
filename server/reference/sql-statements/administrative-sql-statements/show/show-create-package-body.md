---
description: >-
  Display the CREATE statement for a package body. This Oracle-compatible
  statement shows the implementation code of a stored package.
---

# SHOW CREATE PACKAGE BODY

## Syntax

```sql
SHOW CREATE PACKAGE BODY  [ db_name . ] package_name
```

## Description

{% tabs %}
{% tab title="Current" %}
The `SHOW CREATE PACKAGE BODY` statement shows the `CREATE PACKAGE BODY` statement that creates the given package body (that is, the implementation of the package).
{% endtab %}

{% tab title="< 11.4" %}
The `SHOW CREATE PACKAGE BODY` statement shows the `CREATE PACKAGE BODY` statement that creates the given package body (that is, the implementation of the package). `CREATE PACKAGE BODY` can be used when [Oracle SQL\_MODE](https://kb-archive.mariadb.net/kb/en/sql_modeoracle-from-mariadb-103/) is set.
{% endtab %}
{% endtabs %}

`SHOW CREATE PACKAGE BODY` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.

## Examples

```sql
SHOW CREATE PACKAGE BODY employee_tools\G
*************************** 1. row ***************************
        Package body: employee_tools
            sql_mode: PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ORACLE,NO_KEY_OPTIONS,NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER
 Create Package Body: CREATE DEFINER="root"@"localhost" PACKAGE BODY "employee_tools" AS
  
  stdRaiseAmount DECIMAL(10,2):=500;
  
  PROCEDURE log (eid INT, ecmnt TEXT) AS
  BEGIN
    INSERT INTO employee_log (id, cmnt) VALUES (eid, ecmnt);
  END;
  
  PROCEDURE hire(ename TEXT, esalary DECIMAL(10,2)) AS
    eid INT;
  BEGIN
    INSERT INTO employee (name, salary) VALUES (ename, esalary);
    eid:= last_insert_id();
    log(eid, 'hire ' || ename);
  END;

  FUNCTION getSalary(eid INT) RETURN DECIMAL(10,2) AS
    nSalary DECIMAL(10,2);
  BEGIN
    SELECT salary INTO nSalary FROM employee WHERE id=eid;
    log(eid, 'getSalary id=' || eid || ' salary=' || nSalary);
    RETURN nSalary;
  END;

  PROCEDURE raiseSalary(eid INT, amount DECIMAL(10,2)) AS
  BEGIN
    UPDATE employee SET salary=salary+amount WHERE id=eid;
    log(eid, 'raiseSalary id=' || eid || ' amount=' || amount);
  END;

  PROCEDURE raiseSalaryStd(eid INT) AS
  BEGIN
    raiseSalary(eid, stdRaiseAmount);
    log(eid, 'raiseSalaryStd id=' || eid);
  END;

BEGIN  
  log(0, 'Session ' || connection_id() || ' ' || current_user || ' started');
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## See Also

* [CREATE PACKAGE](../../data-definition/create/create-package.md)
* [SHOW CREATE PACKAGE](show-create-package.md)
* [DROP PACKAGE](../../data-definition/drop/drop-package.md)
* [CREATE PACKAGE BODY](../../data-definition/create/create-package-body.md)
* [DROP PACKAGE BODY](../../data-definition/drop/drop-package-body.md)
* [Oracle SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
