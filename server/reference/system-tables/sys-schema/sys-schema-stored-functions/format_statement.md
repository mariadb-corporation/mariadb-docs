---
description: >-
  This function formats and truncates an SQL statement string to a specified
  length, making it suitable for display in summary views.
---

# format\_statement

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.format_statement(statement)
```

## Description

Returns a reduced length string. The length is specified by the [statement\_truncate\_len configuration option](../sys-schema-sys_config-table.md) (default 64), and the removed part of the string (if any) is replaced with an ellipsis (three dots).

The function is intended for use in formatting lengthy SQL statements to a fixed length.

## Examples

Default truncation length 64:

```sql
SELECT sys.format_statement(
  'SELECT field1, field2, field3, field4, field5, field6 FROM table1'
  ) AS formatted_statement;
+-------------------------------------------------------------------+
| formatted_statement                                               |
+-------------------------------------------------------------------+
| SELECT field1, field2, field3, ... d4, field5, field6 FROM table1 |
+-------------------------------------------------------------------+
```

Reducing the truncation length to 48:

```sql
SET @sys.statement_truncate_len = 48;

SELECT sys.format_statement( 
  'SELECT field1, field2, field3, field4, field5, field6 FROM table1'
  ) AS formatted_statement;
+---------------------------------------------------+
| formatted_statement                               |
+---------------------------------------------------+
| SELECT field1, field2, ... d5, field6 FROM table1 |
+---------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
