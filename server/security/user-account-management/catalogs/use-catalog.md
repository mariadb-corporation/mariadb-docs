---
description: >-
  Reference for the USE CATALOG statement, allowing a user to switch their
  current session's context to a different catalog.
---

# USE CATALOG

{% include "../../../.gitbook/includes/catalogs.md" %}

## Syntax

```bnf
USE CATALOG catalog_name
```

## Description

Changes to another [catalog](./).\
Can only be done by a super user in the 'def' catalog.\
Changing catalog will update catalog status and reset all session status.

A tenant (a user in any other catalog than 'def') cannot change to another catalog.\
However tenants can execute `USE CATALOG current_catalog`. This is to allow the\
user to import SQL scripts that use `USE CATALOG...`.

## See Also

* [USE database](../../../reference/sql-statements/administrative-sql-statements/use-database.md). Changing database.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
