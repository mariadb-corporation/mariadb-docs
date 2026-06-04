# FETCH

## Syntax

```bnf
FETCH cursor_name INTO var_name [, var_name] ...
```

## Description

This statement fetches the next row (if a row exists) using the specified [open](open.md) [cursor](./), and advances the cursor pointer.

`var_name` can be a [local variable](../declare-variable.md), but _not_ a [user-defined variable](../../../sql-structure/sql-language-structure/user-defined-variables.md).

If no more rows are available, a No Data condition occurs with`SQLSTATE` value `02000`. To detect this condition, you can set up a handler for it (or for a `NOT FOUND` condition).

See [Cursor Overview](cursor-overview.md) for an example.

## See Also

* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [OPEN cursor\_name](open.md)
* [CLOSE cursor\_name](close.md)
* [Cursors in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
