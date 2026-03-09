---
description: The CONNECT storage engine.
---

# CONNECT TBL Table Type: Table List

This type allows defining a table as a list of tables of any engine and type. This is more flexible than multiple tables that must be all of the same file type. This type does, but is more powerful than, what is done with the [MERGE](../../merge.md) engine.

The list of the columns of the TBL table may not necessarily include all the columns of the tables of the list. If the name of some columns is different in the sub-tables, the column to use can be specified by its position given by the`FLAG` option of the column. If the `ACCEPT` option is set to true (Y or 1) columns that do not exist in some of the sub-tables are accepted and their value are null or pseudo-null (this depends on the nullability of the column) for the tables not having this column. The column types can also be different and an automatic conversion are done if necessary.

**Note:** If not specified, the column definitions are retrieved from the first table of the table list.

The default database of the sub-tables is the current database or if not, can be specified in the DBNAME option. For the tables that are not in the default database, this can be specified in the table list. For instance, to create a table based on the French table _employe_ in the current database and on the English table _employee_ of the _db2_ database, the syntax of the create statement can be:

```sql
CREATE TABLE allemp (
  SERIALNO char(5) NOT NULL flag=1,
  NAME varchar(12) NOT NULL flag=2,
  SEX smallint(1),
  TITLE varchar(15) NOT NULL flag=3,
  MANAGER char(5) DEFAULT NULL flag=4,
  DEPARTMENT char(4) NOT NULL flag=5,
  SECRETARY char(5) DEFAULT NULL flag=6,
  SALARY double(8,2) NOT NULL flag=7)
ENGINE=CONNECT table_type=TBL
table_list='employe,db2.employee' option_list='Accept=1';
```

The search for columns in sub tables is done by name and, if they exist with a different name, by their position given by a not null `FLAG` option. Column _sex_ exists only in the English table (`FLAG` is `0`). Its values will null value for the French table.

For instance, the query:

```sql
SELECT name, sex, title, salary FROM allemp WHERE department = 318;
```

Can reply:

| NAME     | SEX  | TITLE         | SALARY   |
| -------- | ---- | ------------- | -------- |
| BARBOUD  | NULL | VENDEUR       | 9700.00  |
| MARCHANT | NULL | VENDEUR       | 8800.00  |
| MINIARD  | NULL | ADMINISTRATIF | 7500.00  |
| POUPIN   | NULL | INGENIEUR     | 7450.00  |
| ANTERPE  | NULL | INGENIEUR     | 6850.00  |
| LOULOUTE | NULL | SECRETAIRE    | 4900.00  |
| TARTINE  | NULL | OPERATRICE    | 2800.00  |
| WERTHER  | NULL | DIRECTEUR     | 14500.00 |
| VOITURIN | NULL | VENDEUR       | 10130.00 |
| BANCROFT | 2    | SALESMAN      | 9600.00  |
| MERCHANT | 1    | SALESMAN      | 8700.00  |
| SHRINKY  | 2    | ADMINISTRATOR | 7500.00  |
| WALTER   | 1    | ENGINEER      | 7400.00  |
| TONGHO   | 1    | ENGINEER      | 6800.00  |
| HONEY    | 2    | SECRETARY     | 4900.00  |
| PLUMHEAD | 2    | TYPIST        | 2800.00  |
| WERTHER  | 1    | DIRECTOR      | 14500.00 |
| WHEELFOR | 1    | SALESMAN      | 10030.00 |

The first 9 rows, coming from the French table, have a null for the _sex_ value. They would have 0 if the sex column had been created NOT NULL.

### Subtables of Non-CONNECT Engines

Sub-tables are accessed as [PROXY](connect-proxy-table-type.md) tables. For not CONNECT sub-tables that are accessed via the MySQL API, it is possible like with `PROXY` to change the MYSQL default options. Of course, this will apply to all not CONNECT tables of the list.

### Using the TABID Special Column

The TABID special column can be used to see from which table the rows come from and to restrict the access to only some of the sub-tables.

Let us see the following example where t1 and t2 are MyISAM tables similar to the ones given in the `MERGE` description:

```sql
CREATE TABLE xt1 (
  a INT(11) NOT NULL,
  message CHAR(20))
ENGINE=CONNECT table_type=MYSQL tabname='t1'
option_list='database=test,user=root';

CREATE TABLE xt2 (
  a INT(11) NOT NULL,
  message CHAR(20))
ENGINE=CONNECT table_type=MYSQL tabname='t2'
option_list='database=test,user=root';

CREATE TABLE toto (
  tabname CHAR(8) NOT NULL special='TABID',
  a INT(11) NOT NULL,
  message CHAR(20))
ENGINE=CONNECT table_type=TBL table_list='xt1,xt2';

SELECT * FROM total;
```

The result returned by the `SELECT` statement is:

| tabname | a | message |
| ------- | - | ------- |
| xt1     | 1 | Testing |
| xt1     | 2 | table   |
| xt1     | 3 | t1      |
| xt2     | 1 | Testing |
| xt2     | 2 | table   |
| xt2     | 3 | t2      |

Now if you send the query:

```sql
SELECT * FROM total WHERE tabname = 'xt2';
```

CONNECT will analyze the where clause and only read the _xt1_ table. This can save time if you want to retrieve only a few sub-tables from a TBL table containing many sub-tables.

### Parallel Execution

Parallel Execution is currently unavailable until some bugs are fixed.

When the sub-tables are located on different servers, it is possible to execute the remote queries simultaneously instead of sequentially. To enable this, set the thread option to yes.

Additional options available for this table type:

| Option | Description                                                                                  |
| ------ | -------------------------------------------------------------------------------------------- |
| Maxerr | The max number of missing tables in the table list before an error is raised. Defaults to 0. |
| Accept | If true, missing columns are accepted and return null values. Defaults to false.             |
| Thread | If true, enables parallel execution of remote sub-tables.                                    |

These options can be specified in the `OPTION_LIST`.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
