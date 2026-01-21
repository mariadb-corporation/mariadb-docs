---
description: >-
  Understand the extensions to the SHOW statement. Learn how to use WHERE and
  LIKE clauses to perform complex filtering on metadata results.
---

# Extended SHOW

The following [SHOW](./) statements can be extended using a `WHERE` clause and a `LIKE` clause to refine the results:

* [SHOW CHARACTER SET](show-character-set.md)
* [SHOW COLLATION](show-collation.md)
* [SHOW COLUMNS](show-columns.md)
* [SHOW DATABASES](show-databases.md)
* [SHOW FUNCTION STATUS](show-function-status.md)
* [SHOW INDEX](show-index.md)\`\`
* [SHOW OPEN TABLES](show-open-tables.md)
* [SHOW PACKAGE STATUS](show-package-status.md)
* [SHOW PACKAGE BODY STATUS](show-package-body-status.md)
* [SHOW INDEX](show-index.md)
* [SHOW PROCEDURE STATUS](show-procedure-status.md)
* [SHOW STATUS](show-status.md)
* [SHOW TABLE STATUS](show-table-status.md)
* [SHOW TABLES](show-tables.md)
* [SHOW TRIGGERS](show-triggers.md)
* [SHOW VARIABLES](show-variables.md)

As with a regular [SELECT](../../data-manipulation/selecting-data/select.md), the `WHERE` clause can be used for the specific columns returned, and the [LIKE](../../built-in-functions/string-functions/like.md) clause with the regular wildcards.

## Examples

This statement shows all tables:

```sql
SHOW TABLES;
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
| t1                   |
| view1                |
+----------------------+
```

This statement only shows tables starting with the letter 'a':

```sql
SHOW TABLES WHERE Tables_in_test LIKE 'a%';
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
+----------------------+
```

This statement shows variables whose names start with _aria_ and have a value greater than 8192:

```sql
SHOW VARIABLES WHERE Variable_name LIKE 'aria%' AND Value >8192;
+------------------------------+---------------------+
| Variable_name                | Value               |
+------------------------------+---------------------+
| aria_checkpoint_log_activity | 1048576             |
| aria_log_file_size           | 1073741824          |
| aria_max_sort_file_size      | 9223372036853727232 |
| aria_pagecache_buffer_size   | 134217728           |
| aria_sort_buffer_size        | 134217728           |
+------------------------------+---------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
