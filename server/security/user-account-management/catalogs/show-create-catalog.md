---
description: >-
  Reference for the SHOW CREATE CATALOG statement, which displays the SQL
  statement used to create a specific catalog.
---

# SHOW CREATE CATALOG

{% include "../../../.gitbook/includes/catalogs.md" %}

## Syntax

```bnf
SHOW CREATE CATALOG catalog_name
```

## Description

Shows the [CREATE CATALOG](create-catalog.md) statement that creates the given [catalog](./).

## Examples

```sql
SHOW CREATE CATALOG def;
+---------+-------------------------------------------------------------------------------------------------------+
| Catalog | Create Catalog                                                                                        |
+---------+-------------------------------------------------------------------------------------------------------+
| def     | CREATE CATALOG `def` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci COMMENT 'default catalog' |
+---------+-------------------------------------------------------------------------------------------------------+
```

## See Also

* [CREATE CATALOG](create-catalog.md)
* [Character Sets and Collations](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
