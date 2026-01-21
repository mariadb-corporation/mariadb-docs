---
description: >-
  This table exposes user-defined variables set within active threads, allowing
  inspection of custom variables across all sessions.
---

# Performance Schema user\_variables\_by\_thread Table

{% hint style="info" %}
The `user_variables_by_thread` table is available from MariaDB 10.5.2.
{% endhint %}

The `user_variables_by_thread` table contains information about [user-defined variables](../../../sql-structure/sql-language-structure/user-defined-variables.md) and the threads that defined them.

[TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) cannot be performed on the table.

The table contains the following columns:

| Column          | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| THREAD\_ID      | The thread identifier of the session in which the variable is defined. |
| VARIABLE\_NAME  | The variable name, without the leading @ character.                    |
| VARIABLE\_VALUE | The variable value                                                     |

## Example

```sql
SET @var = 0;

SELECT * FROM user_variables_by_thread;
+-----------+---------------+----------------+
| THREAD_ID | VARIABLE_NAME | VARIABLE_VALUE |
+-----------+---------------+----------------+
|        11 | var           | 0              |
+-----------+---------------+----------------+
```

## See Also

* [User-defined variables](../../../sql-structure/sql-language-structure/user-defined-variables.md)
* [Information Schema USER\_VARIABLES Table](../../information-schema/information-schema-tables/information-schema-user_variables-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
