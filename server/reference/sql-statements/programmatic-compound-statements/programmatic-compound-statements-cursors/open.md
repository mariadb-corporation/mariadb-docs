# OPEN

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
OPEN cursor_name [[USING variable[,...]] | [expression[,...]]];
```
{% endtab %}

{% tab title="Oracle Mode" %}
{% code title="-- From MariaDB 12.3" %}
```sql
OPEN cursor_variable FOR dynamic_sql_string;
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

## See Also

* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [FETCH cursor\_name](fetch.md)
* [CLOSE cursor\_name](close.md)
* [Cursors in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
