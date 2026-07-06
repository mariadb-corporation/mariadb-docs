---
description: >-
  Learn to insert and load data into MariaDB Server. This section covers INSERT
  and LOAD DATA SQL statements, enabling you to efficiently add new records to
  your databases.
---

# Inserting & Loading Data

{% columns %}
{% column %}
{% content-ref url="concurrent-inserts.md" %}
[concurrent-inserts.md](concurrent-inserts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand concurrent inserts in MyISAM. This feature allows SELECT statements to run simultaneously with INSERT operations, reducing lock contention and improving performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ignore.md" %}
[ignore.md](ignore.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the IGNORE keyword. This modifier suppresses certain errors during statement execution, downgrading them to warnings to allow the operation to proceed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert.md" %}
[insert.md](insert.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to inserting data in MariaDB. Complete INSERT syntax for single rows, bulk operations, and ON DUPLICATE KEY handling for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-default-duplicate-values.md" %}
[insert-default-duplicate-values.md](insert-default-duplicate-values.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Handle default and duplicate values during insertion. Learn how MariaDB manages missing columns and how to resolve duplicate key conflicts using various strategies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-delayed.md" %}
[insert-delayed.md](insert-delayed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Queue inserts for later execution. This MyISAM-specific extension returns control immediately to the client while the server inserts rows when the table is free.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-ignore.md" %}
[insert-ignore.md](insert-ignore.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete INSERT IGNORE reference: ignore insert errors and warnings, duplicate key error handling, invalid value coercion, and SHOW WARNINGS compatibility.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-on-duplicate-key-update.md" %}
[insert-on-duplicate-key-update.md](insert-on-duplicate-key-update.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to inserting data in MariaDB. Complete INSERT syntax for single rows, bulk operations, and ON DUPLICATE KEY handling for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-select.md" %}
[insert-select.md](insert-select.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Copy data between tables. This statement inserts the result set of a SELECT query directly into a target table, enabling efficient bulk data transfer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insertreturning.md" %}
[insertreturning.md](insertreturning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert rows and immediately retrieve the results. This extension returns the inserted values, including auto-increments and defaults, in the same round trip.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load-data-into-tables-or-index/" %}
[load-data-into-tables-or-index](load-data-into-tables-or-index/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Bulk load data efficiently. This section covers commands like LOAD DATA INFILE and LOAD XML for high-speed data import from text or XML files.
{% endcolumn %}
{% endcolumns %}
