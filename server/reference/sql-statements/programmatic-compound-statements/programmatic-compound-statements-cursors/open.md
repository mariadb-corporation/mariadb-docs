# OPEN

## Syntax

{% tabs %}
{% tab title="Current" %}
```bnf
OPEN cursor_name [[USING variable[,...]] | [expression[,...]]];
```
{% endtab %}

{% tab title="Oracle Mode" %}
{% code title="-- From MariaDB 12.3" %}
```sql
OPEN cursor_variable FOR dynamic_sql_string;
```
{% endcode %}

{% code title="-- From MariaDB 13.1.1" %}
```sql
OPEN cursor_variable FOR PREPARE stmt_name;
OPEN cursor_variable FOR LOCAL spvar;
```
{% endcode %}
{% endtab %}

{% tab title="< 10.3" %}
```sql
OPEN cursor_name
```
{% endtab %}
{% endtabs %}

## Description

This statement opens a [cursor](./) which was previously declared with [DECLARE CURSOR](declare-cursor.md).

The query associated to the `DECLARE CURSOR` is executed when `OPEN` is executed. It is important to remember this if the query produces an error, or calls functions which have side effects.

This is necessary in order to [FETCH](fetch.md) rows from a cursor.

See [Cursor Overview](cursor-overview.md) for an example.

### Opening a Cursor Over a Prepared Statement

{% hint style="info" %}
`OPEN ... FOR PREPARE` and `OPEN ... FOR LOCAL` are available from MariaDB 13.1.1.
{% endhint %}

In Oracle mode, a `SYS_REFCURSOR` can be opened over an already-prepared statement:

* `OPEN cursor_variable FOR PREPARE stmt_name;` opens the cursor over the prepared statement named `stmt_name`.
* `OPEN cursor_variable FOR LOCAL spvar;` opens the cursor over the prepared statement whose name is the _value_ of the stored-procedure variable `spvar`.

`OPEN ... FOR LOCAL` is only valid inside a stored procedure, and like the other LOCAL forms is not permitted in stored functions or triggers.

Both forms require a weak cursor variable (`SYS_REFCURSOR`). Using them with a strongly-typed `REF CURSOR` (one declared with a `RETURN` clause) returns an error.

## See Also

* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [FETCH cursor\_name](fetch.md)
* [CLOSE cursor\_name](close.md)
* [Cursors in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
