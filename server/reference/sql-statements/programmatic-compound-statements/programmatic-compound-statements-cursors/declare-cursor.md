# DECLARE CURSOR

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR {select_statement | prepared_statement_name}

cursor_formal_parameter:
    [IN] name type [collate clause]
```
{% endtab %}

{% tab title="< 10.8" %}
```sql
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR select_statement

cursor_formal_parameter:
    name type [collate clause]
```
{% endtab %}
{% endtabs %}

## Description

This statement declares a [cursor](./). Multiple cursors may be declared in a [stored program](../../../../server-usage/stored-routines/), but each cursor in a given block must have a unique name.

`select_statement` is not executed until the [OPEN](open.md) statement is executed. It is important to remember this if the query produces an error, or calls functions which have side effects.

A `SELECT` associated to a cursor can use variables, but the query itself cannot be a variable, and cannot be dynamically composed. The `SELECT` statement cannot have an `INTO` clause.

{% hint style="info" %}
Starting with MariaDB 12.3, the query can also be a prepared statement name, which allows the query to be dynamically composed. The `SELECT` statement cannot have an `INTO` clause.
{% endhint %}

Cursors must be declared before [HANDLERs](../declare-handler.md), but after local variables and [CONDITIONs](../declare-condition.md).

### **Dynamic Cursors**

Starting with MariaDB 12.3, a cursor can be declared for a prepared statement. This allows the use of Dynamic SQL within stored routines. The cursor is bound to a prepared statement name, which must be defined using the `PREPARE` statement before the cursor is opened.

```sql
CREATE OR REPLACE PROCEDURE p1(tab VARCHAR(64), min_id INTEGER)
BEGIN
  DECLARE v_id INT;
  DECLARE v_c1 VARCHAR(100);
  DECLARE no_data BOOL DEFAULT FALSE;
  
  -- 1. Declare cursor for the statement name 's1'
  DECLARE c1 CURSOR FOR s1;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET no_data = TRUE;

  -- 2. Prepare the statement dynamically
  PREPARE s1 FROM CONCAT('SELECT id, c1 FROM ', tab, ' WHERE id >= ?');
  
  -- 3. Open cursor and bind parameters
  OPEN c1 USING min_id;
  
  fetch_loop: LOOP
    FETCH c1 INTO v_id, v_c1;
    IF no_data THEN
      LEAVE fetch_loop;
    END IF;
    SELECT v_id, v_c1;
  END LOOP;
  
  CLOSE c1;
  DEALLOCATE PREPARE s1;
END;
$$

DELIMITER ;
```

### Parameters

Cursors can have parameters. This is a non-standard SQL extension. Cursor parameters can appear in any part of the `DECLARE CURSOR` `select_statement` where a stored procedure variable is allowed (select list, `WHERE`, `HAVING`, `LIMIT` , and so forth).

### IN

{% tabs %}
{% tab title="Current" %}
The `IN` qualifier is supported in the `cursor_formal_parameter` part of the syntax.
{% endtab %}

{% tab title="< 10.8" %}
The `IN` qualifier is **not** supported in the `cursor_formal_parameter` part of the syntax.
{% endtab %}
{% endtabs %}

See [Cursor Overview](cursor-overview.md) for an example.

## See Also

* [Cursor Overview](cursor-overview.md)
* [OPEN cursor\_name](open.md)
* [FETCH cursor\_name](fetch.md)
* [CLOSE cursor\_name](close.md)
* [Cursors in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
