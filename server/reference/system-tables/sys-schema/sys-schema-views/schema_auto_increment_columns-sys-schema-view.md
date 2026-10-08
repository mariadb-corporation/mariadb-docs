---
description: >-
  The schema_auto_increment_columns view lists tables with AUTO_INCREMENT
  columns, showing the current value and the maximum allowed value for the
  column type.
---

# schema\_auto\_increment\_columns Sys Schema View

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

Information about [AUTO\_INCREMENT](../../../data-types/auto_increment.md) columns, sorted by descending usage ratio and maximum column value. Does not include columns in the `mysql`, `sys`, `information_schema` and `performance_schema` schemas.

Contains the following columns:

| Column                 | Description                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| table\_schema          | Schema name containing the table with the auto\_increment attribute.                                                                       |
| table\_name            | Table containing the auto\_increment attribute.                                                                                            |
| column\_name           | Name of the column containing the auto\_increment attribute.                                                                               |
| data\_type             | [Data type](../../../data-types/) of the auto\_increment column, for example [tinyint](../../../data-types/numeric-data-types/tinyint.md). |
| column\_type           | [Data type](../../../data-types/) of the auto\_increment column, plus additional information for example tinyint(3) unsigned.              |
| is\_signed             | 1 if the column is [signed](../../../data-types/numeric-data-types/numeric-data-type-overview.md#signed-unsigned-and-zerofill),0 if not.   |
| is\_unsigned           | 1 if the column is unsigned,0 if it is.                                                                                                    |
| max\_value             | Maximum possible value for the column, for example 255 for an unsigned tinyint.                                                            |
| auto\_increment        | Current auto\_increment value for the column.                                                                                              |
| auto\_increment\_ratio | Ratio of used to maximum value for the auto\_increment column.                                                                             |

## Example

```sql
CREATE OR REPLACE TABLE animals (
    id TINYINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

 INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('fox'),('whale'),('ostrich');

SELECT * FROM sys.schema_auto_increment_columns\G
*************************** 1. row ***************************
        table_schema: test
          table_name: animals
         column_name: id
           data_type: tinyint
         column_type: tinyint(4)
           is_signed: 1
         is_unsigned: 0
           max_value: 127
      auto_increment: 7
auto_increment_ratio: 0.0551
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
