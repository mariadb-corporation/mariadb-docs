---
description: >-
  The mysql.help_topic table stores the detailed content of help topics,
  including descriptions and examples displayed by the HELP command.
---

# mysql.help\_topic Table

`mysql.help_topic` is one of the four tables used by the [HELP command](../../sql-statements/administrative-sql-statements/help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help\_relation](mysql-help_relation-table.md), [help\_category](mysql-help_category-table.md) and [help\_keyword](mysql-help_keyword-table.md).

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.help_topic` table contains the following fields:

| Field              | Type                 | Null | Key | Default | Description |
| ------------------ | -------------------- | ---- | --- | ------- | ----------- |
| help\_topic\_id    | int(10) unsigned     | NO   | PRI | NULL    |             |
| name               | char(64)             | NO   | UNI | NULL    |             |
| help\_category\_id | smallint(5) unsigned | NO   |     | NULL    |             |
| description        | text                 | NO   |     | NULL    |             |
| example            | text                 | NO   |     | NULL    |             |
| url                | char(128)            | NO   |     | NULL    |             |

## Example

```sql
SELECT * FROM help_topic\G;
...
*************************** 704. row ***************************
   help_topic_id: 692
            name: JSON_DEPTH
help_category_id: 41
     description: JSON functions were added in MariaDB 10.2.3.
 
Syntax
------ 
JSON_DEPTH(json_doc)
 
Description
----------- 
Returns the maximum depth of the given JSON document, or
NULL if the argument is null. An error will occur if the
argument is an invalid JSON document.
Scalar values or empty arrays or objects have a depth of 1.
Arrays or objects that are not empty but contain only
elements or member values of depth 1 will have a depth of 2.
In other cases, the depth will be greater than 2.
 
Examples
-------- 
SELECT JSON_DEPTH('[]'), JSON_DEPTH('true'),
JSON_DEPTH('{}');
+------------------+--------------------+------------------+
| JSON_DEPTH('[]') | JSON_DEPTH('true') |
JSON_DEPTH('{}') |
+------------------+--------------------+------------------+
| 1 | 1 | 1 |
+------------------+--------------------+------------------+
 
SELECT JSON_DEPTH('[1, 2, 3]'), JSON_DEPTH('[[], {},
[]]');
+-------------------------+----------------------------+
| JSON_DEPTH('[1, 2, 3]') | JSON_DEPTH('[[], {}, []]') |
+-------------------------+----------------------------+
| 2 | 2 |
+-------------------------+----------------------------+
 
SELECT JSON_DEPTH('[1, 2, [3, 4, 5, 6], 7]');
+---------------------------------------+
| JSON_DEPTH('[1, 2, [3, 4, 5, 6], 7]') |
+---------------------------------------+
| 3 |
+---------------------------------------+

URL: https://mariadb.com/kb/en/json_depth/
         example: 
             url: https://mariadb.com/kb/en/json_depth/
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
