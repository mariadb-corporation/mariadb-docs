---
description: >-
  This function quotes a given string with backticks to ensure it can be safely
  used as an identifier in SQL statements.
---

# quote\_identifier

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.quote_identifier(str)
```

## Description

`quote_identifier` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It quotes a string to produce a result that can be used as an identifier in an SQL statement. The string is returned enclosed by backticks ("`") and with each instance of backtick ("`") doubled. If the argument is `NULL`, the return value is the word "`NULL`" without enclosing backticks.

## Examples

```sql
SELECT sys.quote_identifier("Identifier with spaces");
+------------------------------------------------+
| sys.quote_identifier("Identifier with spaces") |
+------------------------------------------------+
| `Identifier with spaces`                       |
+------------------------------------------------+

SELECT sys.quote_identifier("Identifier` containing `backticks");
+-----------------------------------------------------------+
| sys.quote_identifier("Identifier` containing `backticks") |
+-----------------------------------------------------------+
| `Identifier`` containing ``backticks`                     |
+-----------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
