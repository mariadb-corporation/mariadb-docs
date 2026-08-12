---
description: >-
  Define the interface for a stored package. This Oracle-compatible statement
  declares the public variables and subroutines of a package.
---

# CREATE PACKAGE

{% tabs %}
{% tab title="Current" %}
The `CREATE PACKAGE` statement can be used in any mode.
{% endtab %}

{% tab title="< 11.4" %}
The `CREATE PACKAGE` statement can be used when [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.
{% endtab %}
{% endtabs %}

In [Oracle SQL mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), the PL/SQL dialect is used, while if Oracle mode is not set (the default), SQL/PSM is used.

## Syntax (Oracle mode)

```sql
CREATE
    [ OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PACKAGE [ IF NOT EXISTS ]
    [ db_name . ] package_name
    [ package_characteristic ... ]
{ AS | IS }
    [ package_specification_element ... ]
END [ package_name ]


package_characteristic:
    COMMENT 'string'
  | SQL SECURITY { DEFINER | INVOKER }


package_specification_element:
    FUNCTION_SYM package_specification_function ;
  | PROCEDURE_SYM package_specification_procedure ;
  | type_declaration ;


package_specification_function:
    func_name [ ( func_param [, func_param]... ) ]
    RETURN type
    [ package_routine_characteristic... ]

package_specification_procedure:
    proc_name [ ( proc_param [, proc_param]... ) ]
    [ package_routine_characteristic... ]

func_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

proc_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

type:
    Any valid MariaDB explicit or anchored data type


package_routine_characteristic:
      COMMENT  'string'
    | LANGUAGE SQL
    | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
    | SQL SECURITY { DEFINER | INVOKER }
```

## Syntax (non-Oracle mode)

```sql
CREATE
    [ OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PACKAGE [ IF NOT EXISTS ]
    [ db_name . ] package_name
    [ package_characteristic ... ]
    [ package_specification_element ... ]
END


package_characteristic:
    COMMENT 'string'
  | SQL SECURITY { DEFINER | INVOKER }


package_specification_element:
    FUNCTION_SYM package_specification_function ;
  | PROCEDURE_SYM package_specification_procedure ;


package_specification_function:
    func_name [ ( func_param [, func_param]... ) ]
    RETURNS type
    [ package_routine_characteristic... ]

package_specification_procedure:
    proc_name [ ( proc_param [, proc_param]... ) ]
    [ package_routine_characteristic... ]

func_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

proc_param:
    param_name [ IN | OUT | INOUT | IN OUT ] type

type:
    Any valid MariaDB explicit or anchored data type


package_routine_characteristic:
      COMMENT  'string'
    | LANGUAGE SQL
    | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
    | SQL SECURITY { DEFINER | INVOKER }
```

## Description

`CREATE PACKAGE` creates the specification for a stored package (a collection of logically related stored objects). A stored package specification declares public routines (procedures and functions) of the package, but does not implement these routines.

A package whose specification was created by the `CREATE PACKAGE` statement, should later be implemented using the [CREATE PACKAGE BODY](create-package-body.md) statement.

## Function parameter quantifiers IN | OUT | INOUT | IN OUT

**MariaDB starting with** [**10.8.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.0)

{% tabs %}
{% tab title="Current" %}
The function parameter quantifiers for `IN`, `OUT`, `INOUT`, and `IN OUT` are supported anywhere.
{% endtab %}

{% tab title="< 10.8.0" %}
The function parameter quantifiers for `IN`, `OUT`, `INOUT`, and `IN OUT` are supported only in procedures.
{% endtab %}
{% endtabs %}

`OUT`, `INOUT` and its equivalent `IN OUT`, are only valid if called from `SET` and not `SELECT`. These quantifiers are especially useful for creating functions and procedures with more than one return value. This allows functions and procedures to be more complex and nested.

## Package-Wide Type Declarations

{% hint style="info" %}
This feature is available from MariaDB 13.1, in `sql_mode=ORACLE` only.
{% endhint %}

A package specification can declare data types with `TYPE`, alongside its public routines. Such a type is public: routines outside the package can declare variables of it, using the qualified name `package_name.type_name` or `schema_name.package_name.type_name`.

```sql
SET sql_mode=ORACLE;
DELIMITER $$
CREATE OR REPLACE PACKAGE pkg AS
  TYPE varchar_array IS TABLE OF VARCHAR(2000) INDEX BY INTEGER;
END;
$$
DELIMITER ;
```

Using the type requires the `EXECUTE` privilege on the package. For the contexts where a package type is accepted, name resolution, and the restrictions that apply, see [DECLARE TYPE](../../programmatic-compound-statements/declare-type.md).

## Examples

```sql
SET sql_mode=ORACLE; # unnecessary from MariaDB 11.4
DELIMITER $$
CREATE OR REPLACE PACKAGE employee_tools AS
  FUNCTION getSalary(eid INT) RETURN DECIMAL(10,2);
  PROCEDURE raiseSalary(eid INT, amount DECIMAL(10,2));
  PROCEDURE raiseSalaryStd(eid INT);
  PROCEDURE hire(ename TEXT, esalary DECIMAL(10,2));
END;
$$
DELIMITER ;
```

## See Also

* [CREATE PACKAGE BODY](create-package-body.md)
* [DECLARE TYPE](../../programmatic-compound-statements/declare-type.md)
* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [DROP PACKAGE](../drop/drop-package.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
