---
description: >-
  Learn about the IGNORE keyword. This modifier suppresses certain errors during
  statement execution, downgrading them to warnings to allow the operation to
  proceed.
---

# IGNORE

The `IGNORE` option tells the server to ignore some common errors.

`IGNORE` can be used with the following statements:

* [DELETE](../changing-deleting-data/delete.md)
* [INSERT](insert.md) (see also [INSERT IGNORE](insert-ignore.md))
* [LOAD DATA INFILE](load-data-into-tables-or-index/load-data-infile.md)
* [UPDATE](../changing-deleting-data/update.md)
* [ALTER TABLE](../../data-definition/alter/alter-table/)
* [CREATE TABLE ... SELECT](../../data-definition/create/create-table.md#create-select)
* [INSERT ... SELECT](insert-select.md)

The logic used:

* Variables out of ranges are replaced with the maximum/minimum value.
* [SQL\_MODEs](../../../../server-management/variables-and-modes/sql_mode.md) `STRICT_TRANS_TABLES`, `STRICT_ALL_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE` are ignored.
* Inserting `NULL` in a `NOT NULL` field will insert 0 ( in a numerical field), 0000-00-00 ( in a date field) or an empty string ( in a character field).
* Rows that cause a duplicate key error or break a foreign key constraint are not inserted, updated, or deleted.

The following errors are ignored:

| Error number | Symbolic error name                              | Description                                                           |
| ------------ | ------------------------------------------------ | --------------------------------------------------------------------- |
| 1022         | ER\_DUP\_KEY                                     | Can't write; duplicate key in table '%s'                              |
| 1048         | ER\_BAD\_NULL\_ERROR                             | Column '%s' cannot be null                                            |
| 1062         | ER\_DUP\_ENTRY                                   | Duplicate entry '%s' for key %d                                       |
| 1242         | ER\_SUBQUERY\_NO\_1\_ROW                         | Subquery returns more than 1 row                                      |
| 1264         | ER\_WARN\_DATA\_OUT\_OF\_RANGE                   | Out of range value for column '%s' at row %ld                         |
| 1265         | WARN\_DATA\_TRUNCATED                            | Data truncated for column '%s' at row %ld                             |
| 1292         | ER\_TRUNCATED\_WRONG\_VALUE                      | Truncated incorrect %s value: '%s'                                    |
| 1366         | ER\_TRUNCATED\_WRONG\_VALUE\_FOR\_FIELD          | Incorrect integer value                                               |
| 1369         | ER\_VIEW\_CHECK\_FAILED                          | CHECK OPTION failed '%s.%s'                                           |
| 1451         | ER\_ROW\_IS\_REFERENCED\_2                       | Cannot delete or update a parent row                                  |
| 1452         | ER\_NO\_REFERENCED\_ROW\_2                       | Cannot add or update a child row: a foreign key constraint fails (%s) |
| 1526         | ER\_NO\_PARTITION\_FOR\_GIVEN\_VALUE             | Table has no partition for value %s                                   |
| 1586         | ER\_DUP\_ENTRY\_WITH\_KEY\_NAME                  | Duplicate entry '%s' for key '%s'                                     |
| 1591         | ER\_NO\_PARTITION\_FOR\_GIVEN\_VALUE\_SILENT     | Table has no partition for some existing values                       |
| 1748         | ER\_ROW\_DOES\_NOT\_MATCH\_GIVEN\_PARTITION\_SET | Found a row not matching the given partition set                      |

Ignored errors normally generate a warning.

A property of the `IGNORE` clause consists in causing transactional engines and non-transactional engines (like InnoDB and Aria) to behave the same way. For example, normally a multi-row insert which tries to violate a `UNIQUE` contraint is completely rolled back on InnoDB, but might be partially executed on Aria. With the `IGNORE` clause, the statement will be partially executed in both engines.

Duplicate key errors also generate warnings. The [OLD\_MODE](../../../../server-management/variables-and-modes/old_mode.md) server variable can be used to prevent this.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
