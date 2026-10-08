---
description: >-
  The mysql.help_category table stores category information for the server-side
  help system, organizing help topics into a hierarchy.
---

# mysql.help\_category Table

`mysql.help_category` is one of the four tables used by the [HELP command](../../sql-statements/administrative-sql-statements/help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help\_relation](mysql-help_relation-table.md), [help\_topic](mysql-help_topic-table.md) and [help\_keyword](mysql-help_keyword-table.md).

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.help_category` table contains the following fields:

| Field                | Type                 | Null | Key | Default | Description |
| -------------------- | -------------------- | ---- | --- | ------- | ----------- |
| help\_category\_id   | smallint(5) unsigned | NO   | PRI | NULL    |             |
| name                 | char(64)             | NO   | UNI | NULL    |             |
| parent\_category\_id | smallint(5) unsigned | YES  |     | NULL    |             |
| url                  | char(128)            | NO   |     | NULL    |             |

## Example

```sql
SELECT * FROM help_category;
+------------------+-----------------------------------------------+--------------------+-----+
| help_category_id | name                                          | parent_category_id | url |
+------------------+-----------------------------------------------+--------------------+-----+
|                1 | Geographic                                    |                  0 |     |
|                2 | Polygon properties                            |                 34 |     |
|                3 | WKT                                           |                 34 |     |
|                4 | Numeric Functions                             |                 38 |     |
|                5 | Plugins                                       |                 35 |     |
|                6 | MBR                                           |                 34 |     |
|                7 | Control flow functions                        |                 38 |     |
|                8 | Transactions                                  |                 35 |     |
|                9 | Help Metadata                                 |                 35 |     |
|               10 | Account Management                            |                 35 |     |
|               11 | Point properties                              |                 34 |     |
|               12 | Encryption Functions                          |                 38 |     |
|               13 | LineString properties                         |                 34 |     |
|               14 | Miscellaneous Functions                       |                 38 |     |
|               15 | Logical operators                             |                 38 |     |
|               16 | Functions and Modifiers for Use with GROUP BY |                 35 |     |
|               17 | Information Functions                         |                 38 |     |
|               18 | Comparison operators                          |                 38 |     |
|               19 | Bit Functions                                 |                 38 |     |
|               20 | Table Maintenance                             |                 35 |     |
|               21 | User-Defined Functions                        |                 35 |     |
|               22 | Data Types                                    |                 35 |     |
|               23 | Compound Statements                           |                 35 |     |
|               24 | Geometry constructors                         |                 34 |     |
|               25 | GeometryCollection properties                 |                  1 |     |
|               26 | Administration                                |                 35 |     |
|               27 | Data Manipulation                             |                 35 |     |
|               28 | Utility                                       |                 35 |     |
|               29 | Language Structure                            |                 35 |     |
|               30 | Geometry relations                            |                 34 |     |
|               31 | Date and Time Functions                       |                 38 |     |
|               32 | WKB                                           |                 34 |     |
|               33 | Procedures                                    |                 35 |     |
|               34 | Geographic Features                           |                 35 |     |
|               35 | Contents                                      |                  0 |     |
|               36 | Geometry properties                           |                 34 |     |
|               37 | String Functions                              |                 38 |     |
|               38 | Functions                                     |                 35 |     |
|               39 | Data Definition                               |                 35 |     |
+------------------+-----------------------------------------------+--------------------+-----+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
