---
description: >-
  The Information Schema USERS_VARIABLES table lists user accounts, including
  whether they are global or local, and details about their password expiration.
---

# Information Schema USER\_VARIABLES Table

## Description

The `USER_VARIABLES` table is created when the [user\_variables](../../../plugins/other-plugins/user-variables-plugin.md) plugin is enabled, and contains information about [user-defined variables](../../../sql-structure/sql-language-structure/user-defined-variables.md).

The table contains the following columns:

| Column               | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| VARIABLE\_NAME       | Variable name.                                                          |
| VARIABLE\_VALUE      | Variable value.                                                         |
| VARIABLE\_TYPE       | Variable [type](../../../data-types/).                                  |
| CHARACTER\_SET\_NAME | [Character set](../../../data-types/string-data-types/character-sets/). |

User variables are reset and the table emptied with the [FLUSH USER\_VARIABLES](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md) statement. `SHOW USER_VARIABLES` displays a subset of the data.

## Example

```sql
SET @v1 = 0;
SET @v2 = 'abc';
SET @v3 = CAST(123 AS CHAR(5));

SELECT * FROM information_schema.USER_VARIABLES ORDER BY VARIABLE_NAME;
+---------------+----------------+---------------+--------------------+
| VARIABLE_NAME | VARIABLE_VALUE | VARIABLE_TYPE | CHARACTER_SET_NAME |
+---------------+----------------+---------------+--------------------+
| v1            | 0              | INT           | latin1             |
| v2            | abc            | VARCHAR       | utf8               |
| v3            | 123            | VARCHAR       | utf8               |
+---------------+----------------+---------------+--------------------+

SHOW USER_VARIABLES;
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| v3            | 123   |
| v2            | abc   |
| v1            | 0     |
+---------------+-------+
```

## See Also

* [User-defined variables](../../../sql-structure/sql-language-structure/user-defined-variables.md)
* [Performance Schema user\_variables\_by\_thread Table](../../performance-schema/performance-schema-tables/performance-schema-user_variables_by_thread-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
