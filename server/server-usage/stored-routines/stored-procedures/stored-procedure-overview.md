---
description: >-
  Stored procedures are precompiled collections of SQL statements stored on the
  server, allowing for encapsulated logic, parameterized execution, and improved
  application performance.
---

# Stored Procedure Overview

A Stored Procedure is a routine invoked with a [CALL](../../../reference/sql-statements/stored-routine-statements/call.md) statement. It may have input parameters, output parameters and parameters that are both input parameters and output parameters.

## Creating a Stored Procedure

Here's a skeleton example to see a stored procedure in action:

```sql
DELIMITER //

CREATE PROCEDURE Reset_animal_count() 
 MODIFIES SQL DATA
 UPDATE animal_count SET animals = 0;
//

DELIMITER ;
```

First, the delimiter is changed, since the function definition will contain the regular semicolon delimiter. The procedure is named `Reset_animal_count`. `MODIFIES SQL DATA` indicates that the procedure will perform a write action of sorts, and modify data. It's for advisory purposes only. Finally, there's the actual SQL statement - an UPDATE.

```sql
SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|     101 |
+---------+

CALL Reset_animal_count();

SELECT * FROM animal_count;
+---------+
| animals |
+---------+
|       0 |
+---------+
```

A more complex example, with input parameters, from an actual procedure used by banks:

```sql
CREATE PROCEDURE
  Withdraw                             /* Routine name */
  (parameter_amount DECIMAL(6,2),     /* Parameter list */
  parameter_teller_id INTEGER,
  parameter_customer_id INTEGER)
  MODIFIES SQL DATA                   /* Data access clause */
  BEGIN                        /* Routine body */
    UPDATE Customers
        SET balance = balance - parameter_amount
        WHERE customer_id = parameter_customer_id;
    UPDATE Tellers
        SET cash_on_hand = cash_on_hand + parameter_amount
        WHERE teller_id = parameter_teller_id;
    INSERT INTO Transactions VALUES (
        parameter_customer_id,
        parameter_teller_id,
        parameter_amount);
  END;
```

See [CREATE PROCEDURE](create-procedure.md) for full syntax details.

## Why use Stored Procedures?

Security is a key reason. Banks commonly use stored procedures so that applications and users don't have direct access to the tables. Stored procedures are also useful in an environment where multiple languages and clients are all used to perform the same operations.

## Stored Procedure listings and definitions

To find which stored functions are running on the server, use [SHOW PROCEDURE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-procedure-status.md).

```sql
SHOW PROCEDURE STATUS\G
*************************** 1. row ***************************
                  Db: test
                Name: Reset_animal_count
                Type: PROCEDURE
             Definer: root@localhost
            Modified: 2013-06-03 08:55:03
             Created: 2013-06-03 08:55:03
       Security_type: DEFINER
             Comment: 
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

or query the [routines table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md) in the INFORMATION\_SCHEMA database directly:

```sql
SELECT ROUTINE_NAME FROM INFORMATION_SCHEMA.ROUTINES 
  WHERE ROUTINE_TYPE='PROCEDURE';
+--------------------+
| ROUTINE_NAME       |
+--------------------+
| Reset_animal_count |
+--------------------+
```

To find out what the stored procedure does, use [SHOW CREATE PROCEDURE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md).

```sql
SHOW CREATE PROCEDURE Reset_animal_count\G
*************************** 1. row ***************************
           Procedure: Reset_animal_count
            sql_mode: 
    Create Procedure: CREATE DEFINER=`root`@`localhost` PROCEDURE `Reset_animal_count`()
    MODIFIES SQL DATA
UPDATE animal_count SET animals = 0
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## Dropping and Updating a Stored Procedure

To drop a stored procedure, use the [DROP PROCEDURE](drop-procedure.md) statement.

```
DROP PROCEDURE Reset_animal_count();
```

To change the characteristics of a stored procedure, use [ALTER PROCEDURE](alter-procedure.md). However, you cannot change the parameters or body of a stored procedure using this statement; to make such changes, you must drop and re-create the procedure using [CREATE OR REPLACE PROCEDURE](create-procedure.md#or-replace) (which retains existing privileges), or DROP PROCEDURE followed CREATE PROCEDURE .

## Permissions in Stored Procedures

See the article [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
