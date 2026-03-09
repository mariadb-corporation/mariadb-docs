---
description: The CONNECT storage engine.
---

# Using CONNECT - Virtual and Special Columns

CONNECT supports MariaDB [virtual and persistent columns](../../../../reference/sql-statements/data-definition/create/generated-columns.md). It is also possible to declare a column as\
being a CONNECT special column. Let us see on an example how this can be done. The boys table we have seen previously can be recreated as:

```sql
CREATE TABLE boys (
  linenum INT(6) NOT NULL DEFAULT 0 special=ROWID,
  name CHAR(12) NOT NULL,
  city CHAR(12) NOT NULL,
  birth DATE NOT NULL date_format='DD/MM/YYYY',
  hired DATE NOT NULL date_format='DD/MM/YYYY' flag=36,
  agehired INT(3) AS (floor(datediff(hired,birth)/365.25))
  virtual,
  fn CHAR(100) NOT NULL DEFAULT '' special=FILEID)
ENGINE=CONNECT table_type=FIX file_name='boys.txt' mapped=YES lrecl=47;
```

We have defined two CONNECT special columns. You can give them any name; it is the field `SPECIAL` option that specifies the special column functional name.

**Note:** the default values specified for the special columns do not mean anything. They are specified just to prevent getting warning messages when inserting new rows.

For the definition of the _agehired_ virtual column, no CONNECT options can be specified as it has no offset or length, not being stored in the file.

The command:

```sql
SELECT * FROM boys WHERE city = 'boston';
```

will return:

| linenum | name  | city   | birth      | hired      | agehired | fn                           |
| ------- | ----- | ------ | ---------- | ---------- | -------- | ---------------------------- |
| 1       | John  | Boston | 1986-01-25 | 2010-06-02 | 24       | d:\mariadb\sql\data\boys.txt |
| 2       | Henry | Boston | 1987-06-07 | 2008-04-01 | 20       | d:\mariadb\sql\data\boys.txt |
| 6       | Bill  | Boston | 1986-09-11 | 2008-02-10 | 21       | d:\mariadb\sql\data\boys.txt |

Existing special columns are listed in the following table:

| Special Name                   | Type    | Description of the column value                                                                                                                                                                                        |
| ------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ROWID                          | Integer | The row ordinal number in the table. This is not quite equivalent to a virtual column with an auto increment of 1 because rows are renumbered when deleting rows.                                                      |
| ROWNUM                         | Integer | The row ordinal number in the file. This is different from ROWID for multiple tables, TBL/XCOL/OCCUR/PIVOT tables, XML tables with a multiple column, and for DBF tables where ROWNUM includes soft deleted rows.      |
| FILEID FDISK FPATH FNAME FTYPE | String  | FILEID returns the full name of the file this row belongs to. Useful in particular for multiple tables represented by several files. The other special columns can be used to retrieve only one part of the full name. |
| TABID                          | String  | The name of the table this row belongs to. Useful for TBL tables.                                                                                                                                                      |
| PARTID                         | String  | The name of the partition this row belongs to. Specific to partitioned tables.                                                                                                                                         |
| SERVID                         | String  | The name of the federated server or server host used by a MYSQL table. “ODBC” for an ODBC table, "JDBC" for a JDBC table and “Current” for all other tables.                                                           |

**Note:** CONNECT does not currently support auto incremented columns. However, a `ROWID` special column will do the job of a column auto incremented by 1.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
