---
description: >-
  Comprehensive MariaDB data types reference. Complete guide for numeric,
  string, date/time, spatial, and JSON types with storage specifications.
---

# Data Types

{% columns %}
{% column %}
{% content-ref url="data-type-storage-requirements.md" %}
[data-type-storage-requirements.md](data-type-storage-requirements.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for storage space usage. This page lists the disk space consumed by each data type, helping with capacity planning and schema optimization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="auto_increment.md" %}
[auto_increment.md](auto_increment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete AUTO_INCREMENT data type guide for MariaDB. Complete reference for syntax, valid values, storage requirements, and range limits for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="auto_increment-faq.md" %}
[auto_increment-faq.md](auto_increment-faq.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Answers to common questions about AUTO_INCREMENT. Learn about gaps in sequences, resetting values, and behavior in different storage engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="null-values.md" %}
[null-values.md](null-values.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the concept of NULL. This page explains how NULL represents missing or unknown data and how it interacts with comparison operators and functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="row-type-of.md" %}
[row-type-of.md](row-type-of.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Declare row-based variables. This PL/SQL compatibility feature allows declaring variables that match the structure of a table row or cursor.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="serial.md" %}
[serial.md](serial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Alias for BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE. This shorthand data type is often used to define primary keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="type-of.md" %}
[type-of.md](type-of.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Declare variables based on existing types. This feature allows defining variables or parameters that inherit the data type of a table column or another variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="numeric-data-types/" %}
[numeric-data-types](numeric-data-types/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete numeric types reference: INT/BIGINT ranges, DECIMAL(M,D) precision/scale, FLOAT/DOUBLE storage sizes, and numeric type selection guidelines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="date-and-time-data-types/" %}
[date-and-time-data-types](date-and-time-data-types/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Store temporal values. This section covers data types for dates, times, and timestamps, including DATE, DATETIME, TIMESTAMP, TIME, and YEAR.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="string-data-types/" %}
[string-data-types](string-data-types/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Store text and binary data. This section covers character types like CHAR, VARCHAR, and TEXT, as well as binary types like BLOB and BINARY.
{% endcolumn %}
{% endcolumns %}
