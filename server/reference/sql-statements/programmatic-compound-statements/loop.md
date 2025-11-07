# LOOP

## Syntax

```sql
[begin_label:] LOOP
    statement_list
END LOOP [end_label]
```

## Description

`LOOP` implements a simple loop construct, enabling repeated execution of the statement list, which consists of one or more statements, each terminated by a semicolon (i.e., `;`) statement delimiter. The statements within the loop are repeated until the loop is exited; usually this is accomplished with a [LEAVE](leave.md) statement.

A `LOOP` statement can be [labeled](labels.md). `end_label` cannot be given unless`begin_label` also is present. If both are present, they must be the same.

See [Delimiters](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters) in the [mariadb](../../../clients-and-utilities/mariadb-client/) client for more on delimiter usage in the client.

## See Also

* [LOOP in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)
* [ITERATE](iterate.md)
* [LEAVE](leave.md)
* [FOR Loops](for.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
