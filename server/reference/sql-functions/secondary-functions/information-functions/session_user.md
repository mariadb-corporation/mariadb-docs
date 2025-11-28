---
description: >-
  Return the current user name. This function returns the user name and host
  name as provided by the client when connecting.
---

# SESSION\_USER

## Syntax

```sql
SESSION_USER()
```

## Description

{% tabs %}
{% tab title="Current" %}
Shows the value of [CURRENT\_USER()](current_user.md) when the session was created, that is, it shows a `user@host` pair from the [mysql.global\_priv table](../../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md), like `CURRENT_USER()`, but unlike `CURRENT_USER()` it will not change inside stored routines and views. This is SQL Standard behavior for the `SESSION_USER` function.
{% endtab %}

{% tab title="< 11.7" %}
`SESSION_USER()` is a synonym for [USER()](user.md).
{% endtab %}
{% endtabs %}

Backward-compatible behavior can be restored by setting old mode to [SESSION\_USER\_IS\_USER](../../../../server-management/variables-and-modes/old_mode.md#session_user_is_user).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
