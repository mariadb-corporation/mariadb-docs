# REPEAT LOOP

## Syntax

```sql
[begin_label:] REPEAT
    statement_list
UNTIL search_condition
END REPEAT [end_label]
```

The statement list within a `REPEAT` statement is repeated until the search\_condition is true. Thus, a `REPEAT` always enters the loop at least once. statement\_list consists of one or more statements, each\
terminated by a semicolon (i.e., `;`) statement delimiter.

A `REPEAT` statement can be [labeled](labels.md). end\_label cannot be given unless begin\_label is also present. If both are present, they must be the same.

See [Delimiters](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters) in the [mariadb](../../../clients-and-utilities/mariadb-client/) client for more on client delimiter usage.

```sql
DELIMITER //

CREATE PROCEDURE dorepeat(p1 INT)
  BEGIN
    SET @x = 0;
    REPEAT SET @x = @x + 1; UNTIL @x > p1 END REPEAT;
  END
//

CALL dorepeat(1000)//

SELECT @x//
+------+
| @x   |
+------+
| 1001 |
+------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
