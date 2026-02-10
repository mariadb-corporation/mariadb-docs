---
description: >-
  Learn about table-related SQL statements in MariaDB Server. This section
  covers commands for creating, altering, dropping, and manipulating tables,
  essential for managing your database schema.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Table Statements

{% columns %}
{% column %}
{% content-ref url="../data-definition/alter/" %}
[alter](../data-definition/alter/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Access the reference for `ALTER` statements. This section lists commands to modify existing database objects, including tables, databases, users, and servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-definition/alter/alter-table/" %}
[alter-table](../data-definition/alter/alter-table/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `ALTER TABLE` guide for MariaDB. Complete syntax for modifying columns, indexes, constraints, and table properties with comprehensive examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="analyze-table.md" %}
[analyze-table.md](analyze-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Analyze and store key distribution. This statement updates index statistics used by the optimizer to choose the best execution plan.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="check-table.md" %}
[check-table.md](check-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Check tables or views for errors. This statement verifies the integrity of table structure and data for supported storage engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="check-view.md" %}
[check-view.md](check-view.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Verify the validity of a view's algorithm. This statement checks if the view definition is correct and references existing tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="checksum-table.md" %}
[checksum-table.md](checksum-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Report a checksum for table contents. This statement calculates a value to compare tables, useful for verifying replication consistency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-definition/create/create-table.md" %}
[create-table.md](../data-definition/create/create-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete guide to creating tables in MariaDB. Complete `CREATE TABLE` syntax for data types, constraints, indexes, and storage engines for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-manipulation/changing-deleting-data/delete.md" %}
[delete.md](../data-manipulation/changing-deleting-data/delete.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete guide to deleting data in MariaDB. Complete `DELETE` syntax with `WHERE` filtering, `JOIN` operations, and safety considerations for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-definition/drop/drop-table.md" %}
[drop-table.md](../data-definition/drop/drop-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `DROP TABLE` syntax: `TEMPORARY`, `IF EXISTS`, `WAIT`/`NOWAIT`, `RESTRICT`/`CASCADE` options, metadata locks, atomic `DROP`, and replication behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-manipulation/inserting-loading-data/insert.md" %}
[insert.md](../data-manipulation/inserting-loading-data/insert.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete guide to inserting data in MariaDB. Complete `INSERT` syntax for single rows, bulk operations, and `ON DUPLICATE KEY` handling for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md" %}
[optimize-table.md](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete MariaDB performance optimization guide. Complete reference for query tuning, indexing strategies, and configuration improvements for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-definition/rename-table.md" %}
[rename-table.md](../data-definition/rename-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Change the name of one or more tables atomically. This command moves tables within or between databases while preserving their data and structure.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repair-table.md" %}
[repair-table.md](repair-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Repair corrupted tables. This statement fixes errors in tables for supported storage engines like MyISAM, Aria, and Archive.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repair-view.md" %}
[repair-view.md](repair-view.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Check and correct a view's algorithm. This statement is primarily used by upgrade scripts to ensure view definitions are compatible.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-manipulation/changing-deleting-data/replace.md" %}
[replace.md](../data-manipulation/changing-deleting-data/replace.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Insert or replace rows based on unique keys. This statement acts like `INSERT`, but if a duplicate key exists, it deletes the old row and inserts the new one.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../administrative-sql-statements/show/show-columns.md" %}
[show-columns.md](../administrative-sql-statements/show/show-columns.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete guide to displaying table columns in MariaDB. Complete `SHOW COLUMNS` syntax with field types, keys, and filtering options for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../administrative-sql-statements/show/show-create-table.md" %}
[show-create-table.md](../administrative-sql-statements/show/show-create-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Get the SQL statement to recreate a table. This statement shows the complete `CREATE TABLE` syntax, including column definitions and indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../administrative-sql-statements/show/show-index.md" %}
[show-index.md](../administrative-sql-statements/show/show-index.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `SHOW INDEX` reference: `SHOW INDEX FROM`` `_`tbl_name`_ syntax, output fields, and `WHERE`/`LIKE` filters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="truncate-table.md" %}
[truncate-table.md](truncate-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `TRUNCATE TABLE` reference with `[WAIT n|NOWAIT]` syntax, InnoDB `FOREIGN KEY` constraints, implicit commit, and `AUTO_INCREMENT` reset.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-manipulation/changing-deleting-data/update.md" %}
[update.md](../data-manipulation/changing-deleting-data/update.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `UPDATE` statement guide for MariaDB. Complete syntax reference with `WHERE` conditions, `JOIN` operations, and multi-table updates for production use.
{% endcolumn %}
{% endcolumns %}
