---
description: >-
  Learn about sequences in MariaDB Server. This section details how to create
  and manage sequences for generating unique numbers, often used for primary
  keys and other auto-incrementing values.
---

# Sequences

{% columns %}
{% column %}
{% content-ref url="sequence-overview.md" %}
[sequence-overview.md](sequence-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of sequence objects, which generate a sequence of numeric values as defined by CREATE SEQUENCE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-sequence.md" %}
[create-sequence.md](create-sequence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a sequence generator. This statement initializes a sequence object that produces a series of unique numeric values on demand.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../sql-statements/administrative-sql-statements/show/show-create-sequence.md" %}
[show-create-sequence.md](../../sql-statements/administrative-sql-statements/show/show-create-sequence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
View the SQL used to create a sequence. This statement displays the CREATE SEQUENCE statement with current parameter values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-sequence.md" %}
[alter-sequence.md](alter-sequence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
ALTER SEQUENCE changes the properties of an existing sequence object.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-sequence.md" %}
[drop-sequence.md](drop-sequence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
DROP SEQUENCE removes one or more sequence objects.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sequence-functions/" %}
[sequence-functions](sequence-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about sequence functions in MariaDB Server. This section details SQL functions for retrieving the next or current value from a sequence, crucial for generating unique identifiers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md" %}
[information-schema-sequences-table.md](../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Information Schema SEQUENCES table provides metadata about sequence objects, including their minimum, maximum, and current values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../sql-statements/administrative-sql-statements/show/show-tables.md" %}
[show-tables.md](../../sql-statements/administrative-sql-statements/show/show-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to listing tables in MariaDB. Complete SHOW TABLES syntax reference with LIKE patterns, WHERE conditions, and filtering options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../error-codes/mariadb-error-codes-4000-to-4099/e4084.md" %}
[e4084.md](../../error-codes/mariadb-error-codes-4000-to-4099/e4084.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Error 4084: raised when a sequence without CYCLE reaches its MAXVALUE and can generate no more values.
{% endcolumn %}
{% endcolumns %}
