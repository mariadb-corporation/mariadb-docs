# Error 1305: does not exist

| Error Code | SQLSTATE | Error                    | Description          |
| ---------- | -------- | ------------------------ | -------------------- |
| 1305       | 42000    | ER\_SP\_DOES\_NOT\_EXIST | %s %s does not exist |

## Possible Causes and Solutions

This error is returned when what is being called does not exist. For example:

```
CALL Reset_animal_count();
ERROR 1305 (42000): PROCEDURE test.Reset_animal_count does not exist

SELECT Reset_animal_count();
ERROR 1305 (42000): FUNCTION test.Reset_animal_count does not exist
```

There are a number of possible causes:

* The [stored procedure](../../../server-usage/stored-routines/stored-procedures/) or [stored function](../../../server-usage/stored-routines/stored-functions/) has not yet been created. See [CREATE PROCEDURE](../../../server-usage/stored-routines/stored-procedures/create-procedure.md) or [CREATE FUNCTION](../../sql-statements/data-definition/create/create-function.md). For example:

```
DELIMITER //
CREATE PROCEDURE Reset_animal_count()                      
    MODIFIES SQL DATA
    UPDATE animal_count SET animals = 0;
 //
Query OK, 0 rows affected (0.032 sec)

DELIMITER ;

CALL Reset_animal_count();
Query OK, 0 rows affected (0.001 sec)
```

* There was a typo in the name. Check also that the case is correct. See [Identifier Case-sensitivity](../../sql-structure/sql-language-structure/identifier-case-sensitivity.md). For example:

```
CALL reset_animal_count();
ERROR 1305 (42000): PROCEDURE test.Reset_animal_count does not exist

CALL Reset_animal_count();
Query OK, 0 rows affected (0.001 sec)
```

* The database specified is not the same as the database containing the stored procedure or function. For example:

```
use test2
CALL Reset_animal_count();
ERROR 1305 (42000): PROCEDURE test2.Reset_animal_count does not exist
```

Either change the default (current) database with the [USE statement](../../sql-statements/administrative-sql-statements/use-database.md), or specify the database in the call, for example:

```
CALL test.Reset_animal_count(); 
Query OK, 0 rows affected (0.001 sec)
```

or

```
use test
CALL Reset_animal_count();
Query OK, 0 rows affected (0.001 sec)
```

* One is trying to access a stored procedure instead of a stored function, or vice-versa. For example:

```
SELECT Reset_animal_count();
ERROR 1305 (42000): FUNCTION test.Reset_animal_count does not exist

CALL Reset_animal_count();  
Query OK, 0 rows affected (0.001 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
