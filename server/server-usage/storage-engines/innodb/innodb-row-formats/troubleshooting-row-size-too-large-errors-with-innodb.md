---
description: >-
  Diagnose and fix 'Row size too large' errors in InnoDB, usually caused by
  exceeding the maximum row size, by changing row formats to DYNAMIC or
  adjusting column data types.
---

# Troubleshooting Row Size Too Large Errors with InnoDB

With InnoDB, users can see the following message as an error or warning:

```
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored 
inline.
```

And they can also see the following message as an error or warning in the [error log](../../../../server-management/server-monitoring-logs/error-log.md):

```
[Warning] InnoDB: Cannot add field col in table db1.tab because after adding it, 
the row size is 8478 which is greater than maximum allowed size (8126) for a 
record on index leaf page.
```

These messages indicate that the table's definition allows rows that the table's InnoDB row format can't actually store.

These messages are raised in the following cases:

* If [InnoDB strict mode](../innodb-strict-mode.md) is enabled and if a [DDL](../../../../reference/sql-statements/data-definition/) statement is executed that touches the table, such as [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/), then InnoDB will raise an error with this message
* If [InnoDB strict mode](../innodb-strict-mode.md) is disabled and if a [DDL](../../../../reference/sql-statements/data-definition/) statement is executed that touches the table, such as [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/), then InnoDB will raise a warning with this message.
* Regardless of whether [InnoDB strict mode](../innodb-strict-mode.md) is enabled, if a [DML](../../../../reference/sql-statements/data-manipulation/) statement is executed that attempts to write a row that the table's InnoDB row format can't store, then InnoDB will raise an error with this message.

## Example of the Problem

Here is an example of the problem:

```sql
SET GLOBAL innodb_default_row_format='dynamic';

SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   col1 VARCHAR(40) NOT NULL,
   col2 VARCHAR(40) NOT NULL,
   col3 VARCHAR(40) NOT NULL,
   col4 VARCHAR(40) NOT NULL,
   col5 VARCHAR(40) NOT NULL,
   col6 VARCHAR(40) NOT NULL,
   col7 VARCHAR(40) NOT NULL,
   col8 VARCHAR(40) NOT NULL,
   col9 VARCHAR(40) NOT NULL,
   col10 VARCHAR(40) NOT NULL,
   col11 VARCHAR(40) NOT NULL,
   col12 VARCHAR(40) NOT NULL,
   col13 VARCHAR(40) NOT NULL,
   col14 VARCHAR(40) NOT NULL,
   col15 VARCHAR(40) NOT NULL,
   col16 VARCHAR(40) NOT NULL,
   col17 VARCHAR(40) NOT NULL,
   col18 VARCHAR(40) NOT NULL,
   col19 VARCHAR(40) NOT NULL,
   col20 VARCHAR(40) NOT NULL,
   col21 VARCHAR(40) NOT NULL,
   col22 VARCHAR(40) NOT NULL,
   col23 VARCHAR(40) NOT NULL,
   col24 VARCHAR(40) NOT NULL,
   col25 VARCHAR(40) NOT NULL,
   col26 VARCHAR(40) NOT NULL,
   col27 VARCHAR(40) NOT NULL,
   col28 VARCHAR(40) NOT NULL,
   col29 VARCHAR(40) NOT NULL,
   col30 VARCHAR(40) NOT NULL,
   col31 VARCHAR(40) NOT NULL,
   col32 VARCHAR(40) NOT NULL,
   col33 VARCHAR(40) NOT NULL,
   col34 VARCHAR(40) NOT NULL,
   col35 VARCHAR(40) NOT NULL,
   col36 VARCHAR(40) NOT NULL,
   col37 VARCHAR(40) NOT NULL,
   col38 VARCHAR(40) NOT NULL,
   col39 VARCHAR(40) NOT NULL,
   col40 VARCHAR(40) NOT NULL,
   col41 VARCHAR(40) NOT NULL,
   col42 VARCHAR(40) NOT NULL,
   col43 VARCHAR(40) NOT NULL,
   col44 VARCHAR(40) NOT NULL,
   col45 VARCHAR(40) NOT NULL,
   col46 VARCHAR(40) NOT NULL,
   col47 VARCHAR(40) NOT NULL,
   col48 VARCHAR(40) NOT NULL,
   col49 VARCHAR(40) NOT NULL,
   col50 VARCHAR(40) NOT NULL,
   col51 VARCHAR(40) NOT NULL,
   col52 VARCHAR(40) NOT NULL,
   col53 VARCHAR(40) NOT NULL,
   col54 VARCHAR(40) NOT NULL,
   col55 VARCHAR(40) NOT NULL,
   col56 VARCHAR(40) NOT NULL,
   col57 VARCHAR(40) NOT NULL,
   col58 VARCHAR(40) NOT NULL,
   col59 VARCHAR(40) NOT NULL,
   col60 VARCHAR(40) NOT NULL,
   col61 VARCHAR(40) NOT NULL,
   col62 VARCHAR(40) NOT NULL,
   col63 VARCHAR(40) NOT NULL,
   col64 VARCHAR(40) NOT NULL,
   col65 VARCHAR(40) NOT NULL,
   col66 VARCHAR(40) NOT NULL,
   col67 VARCHAR(40) NOT NULL,
   col68 VARCHAR(40) NOT NULL,
   col69 VARCHAR(40) NOT NULL,
   col70 VARCHAR(40) NOT NULL,
   col71 VARCHAR(40) NOT NULL,
   col72 VARCHAR(40) NOT NULL,
   col73 VARCHAR(40) NOT NULL,
   col74 VARCHAR(40) NOT NULL,
   col75 VARCHAR(40) NOT NULL,
   col76 VARCHAR(40) NOT NULL,
   col77 VARCHAR(40) NOT NULL,
   col78 VARCHAR(40) NOT NULL,
   col79 VARCHAR(40) NOT NULL,
   col80 VARCHAR(40) NOT NULL,
   col81 VARCHAR(40) NOT NULL,
   col82 VARCHAR(40) NOT NULL,
   col83 VARCHAR(40) NOT NULL,
   col84 VARCHAR(40) NOT NULL,
   col85 VARCHAR(40) NOT NULL,
   col86 VARCHAR(40) NOT NULL,
   col87 VARCHAR(40) NOT NULL,
   col88 VARCHAR(40) NOT NULL,
   col89 VARCHAR(40) NOT NULL,
   col90 VARCHAR(40) NOT NULL,
   col91 VARCHAR(40) NOT NULL,
   col92 VARCHAR(40) NOT NULL,
   col93 VARCHAR(40) NOT NULL,
   col94 VARCHAR(40) NOT NULL,
   col95 VARCHAR(40) NOT NULL,
   col96 VARCHAR(40) NOT NULL,
   col97 VARCHAR(40) NOT NULL,
   col98 VARCHAR(40) NOT NULL,
   col99 VARCHAR(40) NOT NULL,
   col100 VARCHAR(40) NOT NULL,
   col101 VARCHAR(40) NOT NULL,
   col102 VARCHAR(40) NOT NULL,
   col103 VARCHAR(40) NOT NULL,
   col104 VARCHAR(40) NOT NULL,
   col105 VARCHAR(40) NOT NULL,
   col106 VARCHAR(40) NOT NULL,
   col107 VARCHAR(40) NOT NULL,
   col108 VARCHAR(40) NOT NULL,
   col109 VARCHAR(40) NOT NULL,
   col110 VARCHAR(40) NOT NULL,
   col111 VARCHAR(40) NOT NULL,
   col112 VARCHAR(40) NOT NULL,
   col113 VARCHAR(40) NOT NULL,
   col114 VARCHAR(40) NOT NULL,
   col115 VARCHAR(40) NOT NULL,
   col116 VARCHAR(40) NOT NULL,
   col117 VARCHAR(40) NOT NULL,
   col118 VARCHAR(40) NOT NULL,
   col119 VARCHAR(40) NOT NULL,
   col120 VARCHAR(40) NOT NULL,
   col121 VARCHAR(40) NOT NULL,
   col122 VARCHAR(40) NOT NULL,
   col123 VARCHAR(40) NOT NULL,
   col124 VARCHAR(40) NOT NULL,
   col125 VARCHAR(40) NOT NULL,
   col126 VARCHAR(40) NOT NULL,
   col127 VARCHAR(40) NOT NULL,
   col128 VARCHAR(40) NOT NULL,
   col129 VARCHAR(40) NOT NULL,
   col130 VARCHAR(40) NOT NULL,
   col131 VARCHAR(40) NOT NULL,
   col132 VARCHAR(40) NOT NULL,
   col133 VARCHAR(40) NOT NULL,
   col134 VARCHAR(40) NOT NULL,
   col135 VARCHAR(40) NOT NULL,
   col136 VARCHAR(40) NOT NULL,
   col137 VARCHAR(40) NOT NULL,
   col138 VARCHAR(40) NOT NULL,
   col139 VARCHAR(40) NOT NULL,
   col140 VARCHAR(40) NOT NULL,
   col141 VARCHAR(40) NOT NULL,
   col142 VARCHAR(40) NOT NULL,
   col143 VARCHAR(40) NOT NULL,
   col144 VARCHAR(40) NOT NULL,
   col145 VARCHAR(40) NOT NULL,
   col146 VARCHAR(40) NOT NULL,
   col147 VARCHAR(40) NOT NULL,
   col148 VARCHAR(40) NOT NULL,
   col149 VARCHAR(40) NOT NULL,
   col150 VARCHAR(40) NOT NULL,
   col151 VARCHAR(40) NOT NULL,
   col152 VARCHAR(40) NOT NULL,
   col153 VARCHAR(40) NOT NULL,
   col154 VARCHAR(40) NOT NULL,
   col155 VARCHAR(40) NOT NULL,
   col156 VARCHAR(40) NOT NULL,
   col157 VARCHAR(40) NOT NULL,
   col158 VARCHAR(40) NOT NULL,
   col159 VARCHAR(40) NOT NULL,
   col160 VARCHAR(40) NOT NULL,
   col161 VARCHAR(40) NOT NULL,
   col162 VARCHAR(40) NOT NULL,
   col163 VARCHAR(40) NOT NULL,
   col164 VARCHAR(40) NOT NULL,
   col165 VARCHAR(40) NOT NULL,
   col166 VARCHAR(40) NOT NULL,
   col167 VARCHAR(40) NOT NULL,
   col168 VARCHAR(40) NOT NULL,
   col169 VARCHAR(40) NOT NULL,
   col170 VARCHAR(40) NOT NULL,
   col171 VARCHAR(40) NOT NULL,
   col172 VARCHAR(40) NOT NULL,
   col173 VARCHAR(40) NOT NULL,
   col174 VARCHAR(40) NOT NULL,
   col175 VARCHAR(40) NOT NULL,
   col176 VARCHAR(40) NOT NULL,
   col177 VARCHAR(40) NOT NULL,
   col178 VARCHAR(40) NOT NULL,
   col179 VARCHAR(40) NOT NULL,
   col180 VARCHAR(40) NOT NULL,
   col181 VARCHAR(40) NOT NULL,
   col182 VARCHAR(40) NOT NULL,
   col183 VARCHAR(40) NOT NULL,
   col184 VARCHAR(40) NOT NULL,
   col185 VARCHAR(40) NOT NULL,
   col186 VARCHAR(40) NOT NULL,
   col187 VARCHAR(40) NOT NULL,
   col188 VARCHAR(40) NOT NULL,
   col189 VARCHAR(40) NOT NULL,
   col190 VARCHAR(40) NOT NULL,
   col191 VARCHAR(40) NOT NULL,
   col192 VARCHAR(40) NOT NULL,
   col193 VARCHAR(40) NOT NULL,
   col194 VARCHAR(40) NOT NULL,
   col195 VARCHAR(40) NOT NULL,
   col196 VARCHAR(40) NOT NULL,
   col197 VARCHAR(40) NOT NULL,
   col198 VARCHAR(40) NOT NULL,
   PRIMARY KEY (col1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline.
```

## Root Cause of the Problem

The root cause is that InnoDB has a maximum row size that is roughly equivalent to half of the value of the [innodb\_page\_size](../innodb-system-variables.md) system variable. See [InnoDB Row Formats Overview: Maximum Row Size](innodb-row-formats-overview.md#maximum-row-size) for more information.

InnoDB's row formats work around this limit by storing certain kinds of variable-length columns on overflow pages. However, different row formats can store different types of data on overflow pages. Some row formats can store more data in overflow pages than others. For example, the [DYNAMIC](innodb-dynamic-row-format.md) and [COMPRESSED](innodb-compressed-row-format.md) row formats can store the most data in overflow pages. To learn how the various InnoDB row formats use overflow pages, see the following pages:

* [InnoDB REDUNDANT Row Format: Overflow Pages with the REDUNDANT Row Format](innodb-redundant-row-format.md#overflow-pages-with-the-redundant-row-format)
* [InnoDB COMPACT Row Format: Overflow Pages with the COMPACT Row Format](innodb-compact-row-format.md#overflow-pages-with-the-compact-row-format)
* [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format)
* [InnoDB COMPRESSED Row Format: Overflow Pages with the COMPRESSED Row Format](innodb-compressed-row-format.md#overflow-pages-with-the-compressed-row-format)

## Checking Existing Tables for the Problem

InnoDB does not currently have an easy way to check all existing tables to determine which tables have this problem. See [MDEV-20400](https://jira.mariadb.org/browse/MDEV-20400) for more information.

One method to check a single existing table for this problem is to enable [InnoDB strict mode](../innodb-strict-mode.md), and then try to create a duplicate of the table with [CREATE TABLE ... LIKE](../../../../reference/sql-statements/data-definition/create/create-table.md#create-table-like). If the table has this problem, then the operation will fail:

```sql
SET SESSION innodb_strict_mode=ON;

CREATE TABLE tab_dup LIKE tab;
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline.
```

## Finding All Tables That Currently Have the Problem

The following shell script will read through a MariaDB server to identify every table that has a row size definition that is too large for its row format and the server's page size. It runs on most common distributions of Linux.

To run the script, copy the code below to a shell-script named `rowsize.sh`, make it executable with the command `chmod 755 ./rowsize.sh`, and invoke it with the following parameters:

```
./rowsize.sh host user password
```

When the script runs, it displays the name of the temporary database it creates, so that if the script is interrupted before cleaning up, the database can be easily identified and removed manually.

As the script runs it will output one line reporting the database and tablename for each table it finds that has the oversize row problem. If it finds none, it will print the following message: "No tables with rows size too big found."

In either case, the script prints one final line to announce when it's done: `./rowsize.sh done.`

```bash
#!/bin/bash

[ -z "$3" ] && echo "Usage: $0 host user password" >&2 && exit 1

dt="tmp_$RANDOM$RANDOM"

mysql -h $1 -u $2 -p$3 -ABNe "create database $dt;"
[ $? -ne 0 ] && echo "Error: $0 terminating" >&2 exit 1

echo
echo "Created temporary database ${dt} on host $1"
echo

c=0
for d in $(mysql -h $1 -u $2 -p$3 -ABNe "show databases;" | egrep -iv "information_schema|mysql|performance_schema|$dt")
do
	for t in $(mysql -h $1 -u $2 -p$3 -ABNe "show tables;" $d)
	do
		tc=$(mysql -h $1 -u $2 -p$3 -ABNe "show create table $t\\G" $d | egrep -iv "^\*|^$t")
		
		echo $tc | grep -iq "ROW_FORMAT"
		if [ $? -ne 0 ]
		then
			tf=$(mysql -h $1 -u $2 -p$3 -ABNe "select row_format from information_schema.innodb_sys_tables where name = '${d}/${t}';")
			tc="$tc ROW_FORMAT=$tf"
		fi
		
		ef="/tmp/e$RANDOM$RANDOM"
		mysql -h $1 -u $2 -p$3 -ABNe "set innodb_strict_mode=1; set foreign_key_checks=0; ${tc};" $dt >/dev/null  2>$ef
		[ $? -ne 0 ] && cat $ef | grep -q "Row size too large" && echo "${d}.${t}" && let c++ || mysql -h $1 -u $2 -p$3 -ABNe "drop table if exists ${t};" $dt
		rm -f $ef
	done
done
mysql -h $1 -u $2 -p$3 -ABNe "set innodb_strict_mode=1; drop database $dt;"
[ $c -eq 0 ] && echo "No tables with rows size too large found." || echo && echo "$c tables found with row size too large."
echo
echo "$0 done."
```

## Solving the Problem

There are several potential solutions available to solve this problem.

### Converting the Table to the DYNAMIC Row Format

If the table is using either the [REDUNDANT](innodb-redundant-row-format.md) or the [COMPACT](innodb-compact-row-format.md) row format, then one potential solution to this problem is to convert the table to use the [DYNAMIC](innodb-dynamic-row-format.md) row format instead.

If your tables were originally created on an older version of MariaDB or MySQL, then your table may be using one of InnoDB's older row formats:

* In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and before, and in MySQL 5.6 and before, the [COMPACT](innodb-compact-row-format.md) row format was the default row format.
* In MySQL 4.1 and before, the [REDUNDANT](innodb-redundant-row-format.md) row format was the default row format.

The [DYNAMIC](innodb-dynamic-row-format.md) row format can store more data on overflow pages than these older row formats, so this row format may actually be able to store the table's data safely. See [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format) for more information.

Therefore, a potential solution to the _Row size too large_ error is to convert the table to use the [DYNAMIC](innodb-dynamic-row-format.md) row format:

```
ALTER TABLE tab ROW_FORMAT=DYNAMIC;
```

You can use the [INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table in the [information\_schema](../../../../reference/system-tables/information-schema/information-schema-tables/) database to find all tables that use the [REDUNDANT](innodb-redundant-row-format.md) or the [COMPACT](innodb-compact-row-format.md) row formats. This is helpful if you would like to convert all of your tables that you still use the older row formats to the [DYNAMIC](innodb-dynamic-row-format.md) row format. For example, the following query can find those tables, while excluding [InnoDB's internal system tables](../innodb-tablespaces/innodb-system-tablespaces.md#system-tables-within-the-innodb-system-tablespace):

```sql
SELECT NAME, ROW_FORMAT
FROM information_schema.INNODB_SYS_TABLES
WHERE ROW_FORMAT IN('Redundant', 'Compact')
AND NAME NOT IN('SYS_DATAFILES', 'SYS_FOREIGN', 'SYS_FOREIGN_COLS', 'SYS_TABLESPACES', 'SYS_VIRTUAL', 'SYS_ZIP_DICT', 'SYS_ZIP_DICT_COLS');
```

In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and later, the [DYNAMIC](innodb-dynamic-row-format.md) row format is the default row format. If your tables were originally created on one of these newer versions, then they may already be using this row format. In that case, you may need to try the next solution.

### Fitting More Columns on Overflow Pages

If the table is already using the [DYNAMIC](innodb-dynamic-row-format.md) row format, then another potential solution to this problem is to change the table schema, so that the row format can store more columns on overflow pages.

In order for InnoDB to store some variable-length columns on overflow pages, the length of those columns may need to be increased.

Therefore, a counter-intuitive solution to the _Row size too large_ error in a lot of cases is actually to **increase** the length of some variable-length columns, so that InnoDB's row format can store them on overflow pages.

Some possible ways to change the table schema are listed below.

#### Converting Some Columns to `BLOB` or `TEXT`

For [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns, the [DYNAMIC](innodb-dynamic-row-format.md) row format can store these columns on overflow pages. See [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format) for more information.

Therefore, a potential solution to the _Row size too large_ error is to convert some columns to the [BLOB](../../../../reference/data-types/string-data-types/blob.md) or [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.

#### Increasing the Length of `VARBINARY` Columns

For [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) columns, the [DYNAMIC](innodb-dynamic-row-format.md) row format can only store these columns on overflow pages if the maximum length of the column is 256 bytes or longer. See [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format) for more information.

Therefore, a potential solution to the _Row size too large_ error is to ensure that all [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) columns are at least as long as `varbinary(256)`.

#### Increasing the Length of `VARCHAR` Columns

For [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) columns, the [DYNAMIC](innodb-dynamic-row-format.md) row format can only store these columns on overflow pages if the maximum length of the column is 256 bytes or longer. See [InnoDB DYNAMIC Row Format: Overflow Pages with the DYNAMIC Row Format](innodb-dynamic-row-format.md#overflow-pages-with-the-dynamic-row-format) for more information.

The original table schema shown earlier on this page causes the _Row size too large_ error, because all of the table's [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) columns are smaller than 256 bytes, which means that they have to be stored on the row's main data page.

Therefore, a potential solution to the _Row size too large_ error is to ensure that all [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) columns are at least as long as 256 bytes. The number of characters required to reach the 256 byte limit depends on the [character set](../../../../reference/data-types/string-data-types/character-sets/) used by the column.

For example, when using InnoDB's [DYNAMIC](innodb-dynamic-row-format.md) row format and a default character set of [latin1](../../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) (which requires up to 1 byte per character), the 256 byte limit means that a [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) column will only be stored on overflow pages if it is at least as large as a `varchar(256)`:

```sql
SET GLOBAL innodb_default_row_format='dynamic';
SET SESSION innodb_strict_mode=ON;
CREATE OR REPLACE TABLE tab (
   col1 VARCHAR(256) NOT NULL,
   col2 VARCHAR(256) NOT NULL,
   col3 VARCHAR(256) NOT NULL,
   col4 VARCHAR(256) NOT NULL,
   col5 VARCHAR(256) NOT NULL,
   col6 VARCHAR(256) NOT NULL,
   col7 VARCHAR(256) NOT NULL,
   col8 VARCHAR(256) NOT NULL,
   col9 VARCHAR(256) NOT NULL,
   col10 VARCHAR(256) NOT NULL,
   col11 VARCHAR(256) NOT NULL,
   col12 VARCHAR(256) NOT NULL,
   col13 VARCHAR(256) NOT NULL,
   col14 VARCHAR(256) NOT NULL,
   col15 VARCHAR(256) NOT NULL,
   col16 VARCHAR(256) NOT NULL,
   col17 VARCHAR(256) NOT NULL,
   col18 VARCHAR(256) NOT NULL,
   col19 VARCHAR(256) NOT NULL,
   col20 VARCHAR(256) NOT NULL,
   col21 VARCHAR(256) NOT NULL,
   col22 VARCHAR(256) NOT NULL,
   col23 VARCHAR(256) NOT NULL,
   col24 VARCHAR(256) NOT NULL,
   col25 VARCHAR(256) NOT NULL,
   col26 VARCHAR(256) NOT NULL,
   col27 VARCHAR(256) NOT NULL,
   col28 VARCHAR(256) NOT NULL,
   col29 VARCHAR(256) NOT NULL,
   col30 VARCHAR(256) NOT NULL,
   col31 VARCHAR(256) NOT NULL,
   col32 VARCHAR(256) NOT NULL,
   col33 VARCHAR(256) NOT NULL,
   col34 VARCHAR(256) NOT NULL,
   col35 VARCHAR(256) NOT NULL,
   col36 VARCHAR(256) NOT NULL,
   col37 VARCHAR(256) NOT NULL,
   col38 VARCHAR(256) NOT NULL,
   col39 VARCHAR(256) NOT NULL,
   col40 VARCHAR(256) NOT NULL,
   col41 VARCHAR(256) NOT NULL,
   col42 VARCHAR(256) NOT NULL,
   col43 VARCHAR(256) NOT NULL,
   col44 VARCHAR(256) NOT NULL,
   col45 VARCHAR(256) NOT NULL,
   col46 VARCHAR(256) NOT NULL,
   col47 VARCHAR(256) NOT NULL,
   col48 VARCHAR(256) NOT NULL,
   col49 VARCHAR(256) NOT NULL,
   col50 VARCHAR(256) NOT NULL,
   col51 VARCHAR(256) NOT NULL,
   col52 VARCHAR(256) NOT NULL,
   col53 VARCHAR(256) NOT NULL,
   col54 VARCHAR(256) NOT NULL,
   col55 VARCHAR(256) NOT NULL,
   col56 VARCHAR(256) NOT NULL,
   col57 VARCHAR(256) NOT NULL,
   col58 VARCHAR(256) NOT NULL,
   col59 VARCHAR(256) NOT NULL,
   col60 VARCHAR(256) NOT NULL,
   col61 VARCHAR(256) NOT NULL,
   col62 VARCHAR(256) NOT NULL,
   col63 VARCHAR(256) NOT NULL,
   col64 VARCHAR(256) NOT NULL,
   col65 VARCHAR(256) NOT NULL,
   col66 VARCHAR(256) NOT NULL,
   col67 VARCHAR(256) NOT NULL,
   col68 VARCHAR(256) NOT NULL,
   col69 VARCHAR(256) NOT NULL,
   col70 VARCHAR(256) NOT NULL,
   col71 VARCHAR(256) NOT NULL,
   col72 VARCHAR(256) NOT NULL,
   col73 VARCHAR(256) NOT NULL,
   col74 VARCHAR(256) NOT NULL,
   col75 VARCHAR(256) NOT NULL,
   col76 VARCHAR(256) NOT NULL,
   col77 VARCHAR(256) NOT NULL,
   col78 VARCHAR(256) NOT NULL,
   col79 VARCHAR(256) NOT NULL,
   col80 VARCHAR(256) NOT NULL,
   col81 VARCHAR(256) NOT NULL,
   col82 VARCHAR(256) NOT NULL,
   col83 VARCHAR(256) NOT NULL,
   col84 VARCHAR(256) NOT NULL,
   col85 VARCHAR(256) NOT NULL,
   col86 VARCHAR(256) NOT NULL,
   col87 VARCHAR(256) NOT NULL,
   col88 VARCHAR(256) NOT NULL,
   col89 VARCHAR(256) NOT NULL,
   col90 VARCHAR(256) NOT NULL,
   col91 VARCHAR(256) NOT NULL,
   col92 VARCHAR(256) NOT NULL,
   col93 VARCHAR(256) NOT NULL,
   col94 VARCHAR(256) NOT NULL,
   col95 VARCHAR(256) NOT NULL,
   col96 VARCHAR(256) NOT NULL,
   col97 VARCHAR(256) NOT NULL,
   col98 VARCHAR(256) NOT NULL,
   col99 VARCHAR(256) NOT NULL,
   col100 VARCHAR(256) NOT NULL,
   col101 VARCHAR(256) NOT NULL,
   col102 VARCHAR(256) NOT NULL,
   col103 VARCHAR(256) NOT NULL,
   col104 VARCHAR(256) NOT NULL,
   col105 VARCHAR(256) NOT NULL,
   col106 VARCHAR(256) NOT NULL,
   col107 VARCHAR(256) NOT NULL,
   col108 VARCHAR(256) NOT NULL,
   col109 VARCHAR(256) NOT NULL,
   col110 VARCHAR(256) NOT NULL,
   col111 VARCHAR(256) NOT NULL,
   col112 VARCHAR(256) NOT NULL,
   col113 VARCHAR(256) NOT NULL,
   col114 VARCHAR(256) NOT NULL,
   col115 VARCHAR(256) NOT NULL,
   col116 VARCHAR(256) NOT NULL,
   col117 VARCHAR(256) NOT NULL,
   col118 VARCHAR(256) NOT NULL,
   col119 VARCHAR(256) NOT NULL,
   col120 VARCHAR(256) NOT NULL,
   col121 VARCHAR(256) NOT NULL,
   col122 VARCHAR(256) NOT NULL,
   col123 VARCHAR(256) NOT NULL,
   col124 VARCHAR(256) NOT NULL,
   col125 VARCHAR(256) NOT NULL,
   col126 VARCHAR(256) NOT NULL,
   col127 VARCHAR(256) NOT NULL,
   col128 VARCHAR(256) NOT NULL,
   col129 VARCHAR(256) NOT NULL,
   col130 VARCHAR(256) NOT NULL,
   col131 VARCHAR(256) NOT NULL,
   col132 VARCHAR(256) NOT NULL,
   col133 VARCHAR(256) NOT NULL,
   col134 VARCHAR(256) NOT NULL,
   col135 VARCHAR(256) NOT NULL,
   col136 VARCHAR(256) NOT NULL,
   col137 VARCHAR(256) NOT NULL,
   col138 VARCHAR(256) NOT NULL,
   col139 VARCHAR(256) NOT NULL,
   col140 VARCHAR(256) NOT NULL,
   col141 VARCHAR(256) NOT NULL,
   col142 VARCHAR(256) NOT NULL,
   col143 VARCHAR(256) NOT NULL,
   col144 VARCHAR(256) NOT NULL,
   col145 VARCHAR(256) NOT NULL,
   col146 VARCHAR(256) NOT NULL,
   col147 VARCHAR(256) NOT NULL,
   col148 VARCHAR(256) NOT NULL,
   col149 VARCHAR(256) NOT NULL,
   col150 VARCHAR(256) NOT NULL,
   col151 VARCHAR(256) NOT NULL,
   col152 VARCHAR(256) NOT NULL,
   col153 VARCHAR(256) NOT NULL,
   col154 VARCHAR(256) NOT NULL,
   col155 VARCHAR(256) NOT NULL,
   col156 VARCHAR(256) NOT NULL,
   col157 VARCHAR(256) NOT NULL,
   col158 VARCHAR(256) NOT NULL,
   col159 VARCHAR(256) NOT NULL,
   col160 VARCHAR(256) NOT NULL,
   col161 VARCHAR(256) NOT NULL,
   col162 VARCHAR(256) NOT NULL,
   col163 VARCHAR(256) NOT NULL,
   col164 VARCHAR(256) NOT NULL,
   col165 VARCHAR(256) NOT NULL,
   col166 VARCHAR(256) NOT NULL,
   col167 VARCHAR(256) NOT NULL,
   col168 VARCHAR(256) NOT NULL,
   col169 VARCHAR(256) NOT NULL,
   col170 VARCHAR(256) NOT NULL,
   col171 VARCHAR(256) NOT NULL,
   col172 VARCHAR(256) NOT NULL,
   col173 VARCHAR(256) NOT NULL,
   col174 VARCHAR(256) NOT NULL,
   col175 VARCHAR(256) NOT NULL,
   col176 VARCHAR(256) NOT NULL,
   col177 VARCHAR(256) NOT NULL,
   col178 VARCHAR(256) NOT NULL,
   col179 VARCHAR(256) NOT NULL,
   col180 VARCHAR(256) NOT NULL,
   col181 VARCHAR(256) NOT NULL,
   col182 VARCHAR(256) NOT NULL,
   col183 VARCHAR(256) NOT NULL,
   col184 VARCHAR(256) NOT NULL,
   col185 VARCHAR(256) NOT NULL,
   col186 VARCHAR(256) NOT NULL,
   col187 VARCHAR(256) NOT NULL,
   col188 VARCHAR(256) NOT NULL,
   col189 VARCHAR(256) NOT NULL,
   col190 VARCHAR(256) NOT NULL,
   col191 VARCHAR(256) NOT NULL,
   col192 VARCHAR(256) NOT NULL,
   col193 VARCHAR(256) NOT NULL,
   col194 VARCHAR(256) NOT NULL,
   col195 VARCHAR(256) NOT NULL,
   col196 VARCHAR(256) NOT NULL,
   col197 VARCHAR(256) NOT NULL,
   col198 VARCHAR(256) NOT NULL,
   PRIMARY KEY (col1)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

And when using InnoDB's [DYNAMIC](innodb-dynamic-row-format.md) row format and a default character set of [utf8](../../../../reference/data-types/string-data-types/character-sets/unicode.md) (which requires up to 3 bytes per character), the 256 byte limit means that a [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) column will only be stored on overflow pages if it is at least as large as a `varchar(86)`:

```sql
SET GLOBAL innodb_default_row_format='dynamic';
SET SESSION innodb_strict_mode=ON;
CREATE OR REPLACE TABLE tab (
   col1 VARCHAR(86) NOT NULL,
   col2 VARCHAR(86) NOT NULL,
   col3 VARCHAR(86) NOT NULL,
   col4 VARCHAR(86) NOT NULL,
   col5 VARCHAR(86) NOT NULL,
   col6 VARCHAR(86) NOT NULL,
   col7 VARCHAR(86) NOT NULL,
   col8 VARCHAR(86) NOT NULL,
   col9 VARCHAR(86) NOT NULL,
   col10 VARCHAR(86) NOT NULL,
   col11 VARCHAR(86) NOT NULL,
   col12 VARCHAR(86) NOT NULL,
   col13 VARCHAR(86) NOT NULL,
   col14 VARCHAR(86) NOT NULL,
   col15 VARCHAR(86) NOT NULL,
   col16 VARCHAR(86) NOT NULL,
   col17 VARCHAR(86) NOT NULL,
   col18 VARCHAR(86) NOT NULL,
   col19 VARCHAR(86) NOT NULL,
   col20 VARCHAR(86) NOT NULL,
   col21 VARCHAR(86) NOT NULL,
   col22 VARCHAR(86) NOT NULL,
   col23 VARCHAR(86) NOT NULL,
   col24 VARCHAR(86) NOT NULL,
   col25 VARCHAR(86) NOT NULL,
   col26 VARCHAR(86) NOT NULL,
   col27 VARCHAR(86) NOT NULL,
   col28 VARCHAR(86) NOT NULL,
   col29 VARCHAR(86) NOT NULL,
   col30 VARCHAR(86) NOT NULL,
   col31 VARCHAR(86) NOT NULL,
   col32 VARCHAR(86) NOT NULL,
   col33 VARCHAR(86) NOT NULL,
   col34 VARCHAR(86) NOT NULL,
   col35 VARCHAR(86) NOT NULL,
   col36 VARCHAR(86) NOT NULL,
   col37 VARCHAR(86) NOT NULL,
   col38 VARCHAR(86) NOT NULL,
   col39 VARCHAR(86) NOT NULL,
   col40 VARCHAR(86) NOT NULL,
   col41 VARCHAR(86) NOT NULL,
   col42 VARCHAR(86) NOT NULL,
   col43 VARCHAR(86) NOT NULL,
   col44 VARCHAR(86) NOT NULL,
   col45 VARCHAR(86) NOT NULL,
   col46 VARCHAR(86) NOT NULL,
   col47 VARCHAR(86) NOT NULL,
   col48 VARCHAR(86) NOT NULL,
   col49 VARCHAR(86) NOT NULL,
   col50 VARCHAR(86) NOT NULL,
   col51 VARCHAR(86) NOT NULL,
   col52 VARCHAR(86) NOT NULL,
   col53 VARCHAR(86) NOT NULL,
   col54 VARCHAR(86) NOT NULL,
   col55 VARCHAR(86) NOT NULL,
   col56 VARCHAR(86) NOT NULL,
   col57 VARCHAR(86) NOT NULL,
   col58 VARCHAR(86) NOT NULL,
   col59 VARCHAR(86) NOT NULL,
   col60 VARCHAR(86) NOT NULL,
   col61 VARCHAR(86) NOT NULL,
   col62 VARCHAR(86) NOT NULL,
   col63 VARCHAR(86) NOT NULL,
   col64 VARCHAR(86) NOT NULL,
   col65 VARCHAR(86) NOT NULL,
   col66 VARCHAR(86) NOT NULL,
   col67 VARCHAR(86) NOT NULL,
   col68 VARCHAR(86) NOT NULL,
   col69 VARCHAR(86) NOT NULL,
   col70 VARCHAR(86) NOT NULL,
   col71 VARCHAR(86) NOT NULL,
   col72 VARCHAR(86) NOT NULL,
   col73 VARCHAR(86) NOT NULL,
   col74 VARCHAR(86) NOT NULL,
   col75 VARCHAR(86) NOT NULL,
   col76 VARCHAR(86) NOT NULL,
   col77 VARCHAR(86) NOT NULL,
   col78 VARCHAR(86) NOT NULL,
   col79 VARCHAR(86) NOT NULL,
   col80 VARCHAR(86) NOT NULL,
   col81 VARCHAR(86) NOT NULL,
   col82 VARCHAR(86) NOT NULL,
   col83 VARCHAR(86) NOT NULL,
   col84 VARCHAR(86) NOT NULL,
   col85 VARCHAR(86) NOT NULL,
   col86 VARCHAR(86) NOT NULL,
   col87 VARCHAR(86) NOT NULL,
   col88 VARCHAR(86) NOT NULL,
   col89 VARCHAR(86) NOT NULL,
   col90 VARCHAR(86) NOT NULL,
   col91 VARCHAR(86) NOT NULL,
   col92 VARCHAR(86) NOT NULL,
   col93 VARCHAR(86) NOT NULL,
   col94 VARCHAR(86) NOT NULL,
   col95 VARCHAR(86) NOT NULL,
   col96 VARCHAR(86) NOT NULL,
   col97 VARCHAR(86) NOT NULL,
   col98 VARCHAR(86) NOT NULL,
   col99 VARCHAR(86) NOT NULL,
   col100 VARCHAR(86) NOT NULL,
   col101 VARCHAR(86) NOT NULL,
   col102 VARCHAR(86) NOT NULL,
   col103 VARCHAR(86) NOT NULL,
   col104 VARCHAR(86) NOT NULL,
   col105 VARCHAR(86) NOT NULL,
   col106 VARCHAR(86) NOT NULL,
   col107 VARCHAR(86) NOT NULL,
   col108 VARCHAR(86) NOT NULL,
   col109 VARCHAR(86) NOT NULL,
   col110 VARCHAR(86) NOT NULL,
   col111 VARCHAR(86) NOT NULL,
   col112 VARCHAR(86) NOT NULL,
   col113 VARCHAR(86) NOT NULL,
   col114 VARCHAR(86) NOT NULL,
   col115 VARCHAR(86) NOT NULL,
   col116 VARCHAR(86) NOT NULL,
   col117 VARCHAR(86) NOT NULL,
   col118 VARCHAR(86) NOT NULL,
   col119 VARCHAR(86) NOT NULL,
   col120 VARCHAR(86) NOT NULL,
   col121 VARCHAR(86) NOT NULL,
   col122 VARCHAR(86) NOT NULL,
   col123 VARCHAR(86) NOT NULL,
   col124 VARCHAR(86) NOT NULL,
   col125 VARCHAR(86) NOT NULL,
   col126 VARCHAR(86) NOT NULL,
   col127 VARCHAR(86) NOT NULL,
   col128 VARCHAR(86) NOT NULL,
   col129 VARCHAR(86) NOT NULL,
   col130 VARCHAR(86) NOT NULL,
   col131 VARCHAR(86) NOT NULL,
   col132 VARCHAR(86) NOT NULL,
   col133 VARCHAR(86) NOT NULL,
   col134 VARCHAR(86) NOT NULL,
   col135 VARCHAR(86) NOT NULL,
   col136 VARCHAR(86) NOT NULL,
   col137 VARCHAR(86) NOT NULL,
   col138 VARCHAR(86) NOT NULL,
   col139 VARCHAR(86) NOT NULL,
   col140 VARCHAR(86) NOT NULL,
   col141 VARCHAR(86) NOT NULL,
   col142 VARCHAR(86) NOT NULL,
   col143 VARCHAR(86) NOT NULL,
   col144 VARCHAR(86) NOT NULL,
   col145 VARCHAR(86) NOT NULL,
   col146 VARCHAR(86) NOT NULL,
   col147 VARCHAR(86) NOT NULL,
   col148 VARCHAR(86) NOT NULL,
   col149 VARCHAR(86) NOT NULL,
   col150 VARCHAR(86) NOT NULL,
   col151 VARCHAR(86) NOT NULL,
   col152 VARCHAR(86) NOT NULL,
   col153 VARCHAR(86) NOT NULL,
   col154 VARCHAR(86) NOT NULL,
   col155 VARCHAR(86) NOT NULL,
   col156 VARCHAR(86) NOT NULL,
   col157 VARCHAR(86) NOT NULL,
   col158 VARCHAR(86) NOT NULL,
   col159 VARCHAR(86) NOT NULL,
   col160 VARCHAR(86) NOT NULL,
   col161 VARCHAR(86) NOT NULL,
   col162 VARCHAR(86) NOT NULL,
   col163 VARCHAR(86) NOT NULL,
   col164 VARCHAR(86) NOT NULL,
   col165 VARCHAR(86) NOT NULL,
   col166 VARCHAR(86) NOT NULL,
   col167 VARCHAR(86) NOT NULL,
   col168 VARCHAR(86) NOT NULL,
   col169 VARCHAR(86) NOT NULL,
   col170 VARCHAR(86) NOT NULL,
   col171 VARCHAR(86) NOT NULL,
   col172 VARCHAR(86) NOT NULL,
   col173 VARCHAR(86) NOT NULL,
   col174 VARCHAR(86) NOT NULL,
   col175 VARCHAR(86) NOT NULL,
   col176 VARCHAR(86) NOT NULL,
   col177 VARCHAR(86) NOT NULL,
   col178 VARCHAR(86) NOT NULL,
   col179 VARCHAR(86) NOT NULL,
   col180 VARCHAR(86) NOT NULL,
   col181 VARCHAR(86) NOT NULL,
   col182 VARCHAR(86) NOT NULL,
   col183 VARCHAR(86) NOT NULL,
   col184 VARCHAR(86) NOT NULL,
   col185 VARCHAR(86) NOT NULL,
   col186 VARCHAR(86) NOT NULL,
   col187 VARCHAR(86) NOT NULL,
   col188 VARCHAR(86) NOT NULL,
   col189 VARCHAR(86) NOT NULL,
   col190 VARCHAR(86) NOT NULL,
   col191 VARCHAR(86) NOT NULL,
   col192 VARCHAR(86) NOT NULL,
   col193 VARCHAR(86) NOT NULL,
   col194 VARCHAR(86) NOT NULL,
   col195 VARCHAR(86) NOT NULL,
   col196 VARCHAR(86) NOT NULL,
   col197 VARCHAR(86) NOT NULL,
   col198 VARCHAR(86) NOT NULL,
   PRIMARY KEY (col1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

And when using InnoDB's [DYNAMIC](innodb-dynamic-row-format.md) row format and a default character set of [utf8mb4](../../../../reference/data-types/string-data-types/character-sets/unicode.md) (which requires up to 4 bytes per character), the 256 byte limit means that a [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) column will only be stored on overflow pages if it is at least as large as a `varchar(64)`:

```sql
SET GLOBAL innodb_default_row_format='dynamic';
SET SESSION innodb_strict_mode=ON;
CREATE OR REPLACE TABLE tab (
   col1 VARCHAR(64) NOT NULL,
   col2 VARCHAR(64) NOT NULL,
   col3 VARCHAR(64) NOT NULL,
   col4 VARCHAR(64) NOT NULL,
   col5 VARCHAR(64) NOT NULL,
   col6 VARCHAR(64) NOT NULL,
   col7 VARCHAR(64) NOT NULL,
   col8 VARCHAR(64) NOT NULL,
   col9 VARCHAR(64) NOT NULL,
   col10 VARCHAR(64) NOT NULL,
   col11 VARCHAR(64) NOT NULL,
   col12 VARCHAR(64) NOT NULL,
   col13 VARCHAR(64) NOT NULL,
   col14 VARCHAR(64) NOT NULL,
   col15 VARCHAR(64) NOT NULL,
   col16 VARCHAR(64) NOT NULL,
   col17 VARCHAR(64) NOT NULL,
   col18 VARCHAR(64) NOT NULL,
   col19 VARCHAR(64) NOT NULL,
   col20 VARCHAR(64) NOT NULL,
   col21 VARCHAR(64) NOT NULL,
   col22 VARCHAR(64) NOT NULL,
   col23 VARCHAR(64) NOT NULL,
   col24 VARCHAR(64) NOT NULL,
   col25 VARCHAR(64) NOT NULL,
   col26 VARCHAR(64) NOT NULL,
   col27 VARCHAR(64) NOT NULL,
   col28 VARCHAR(64) NOT NULL,
   col29 VARCHAR(64) NOT NULL,
   col30 VARCHAR(64) NOT NULL,
   col31 VARCHAR(64) NOT NULL,
   col32 VARCHAR(64) NOT NULL,
   col33 VARCHAR(64) NOT NULL,
   col34 VARCHAR(64) NOT NULL,
   col35 VARCHAR(64) NOT NULL,
   col36 VARCHAR(64) NOT NULL,
   col37 VARCHAR(64) NOT NULL,
   col38 VARCHAR(64) NOT NULL,
   col39 VARCHAR(64) NOT NULL,
   col40 VARCHAR(64) NOT NULL,
   col41 VARCHAR(64) NOT NULL,
   col42 VARCHAR(64) NOT NULL,
   col43 VARCHAR(64) NOT NULL,
   col44 VARCHAR(64) NOT NULL,
   col45 VARCHAR(64) NOT NULL,
   col46 VARCHAR(64) NOT NULL,
   col47 VARCHAR(64) NOT NULL,
   col48 VARCHAR(64) NOT NULL,
   col49 VARCHAR(64) NOT NULL,
   col50 VARCHAR(64) NOT NULL,
   col51 VARCHAR(64) NOT NULL,
   col52 VARCHAR(64) NOT NULL,
   col53 VARCHAR(64) NOT NULL,
   col54 VARCHAR(64) NOT NULL,
   col55 VARCHAR(64) NOT NULL,
   col56 VARCHAR(64) NOT NULL,
   col57 VARCHAR(64) NOT NULL,
   col58 VARCHAR(64) NOT NULL,
   col59 VARCHAR(64) NOT NULL,
   col60 VARCHAR(64) NOT NULL,
   col61 VARCHAR(64) NOT NULL,
   col62 VARCHAR(64) NOT NULL,
   col63 VARCHAR(64) NOT NULL,
   col64 VARCHAR(64) NOT NULL,
   col65 VARCHAR(64) NOT NULL,
   col66 VARCHAR(64) NOT NULL,
   col67 VARCHAR(64) NOT NULL,
   col68 VARCHAR(64) NOT NULL,
   col69 VARCHAR(64) NOT NULL,
   col70 VARCHAR(64) NOT NULL,
   col71 VARCHAR(64) NOT NULL,
   col72 VARCHAR(64) NOT NULL,
   col73 VARCHAR(64) NOT NULL,
   col74 VARCHAR(64) NOT NULL,
   col75 VARCHAR(64) NOT NULL,
   col76 VARCHAR(64) NOT NULL,
   col77 VARCHAR(64) NOT NULL,
   col78 VARCHAR(64) NOT NULL,
   col79 VARCHAR(64) NOT NULL,
   col80 VARCHAR(64) NOT NULL,
   col81 VARCHAR(64) NOT NULL,
   col82 VARCHAR(64) NOT NULL,
   col83 VARCHAR(64) NOT NULL,
   col84 VARCHAR(64) NOT NULL,
   col85 VARCHAR(64) NOT NULL,
   col86 VARCHAR(64) NOT NULL,
   col87 VARCHAR(64) NOT NULL,
   col88 VARCHAR(64) NOT NULL,
   col89 VARCHAR(64) NOT NULL,
   col90 VARCHAR(64) NOT NULL,
   col91 VARCHAR(64) NOT NULL,
   col92 VARCHAR(64) NOT NULL,
   col93 VARCHAR(64) NOT NULL,
   col94 VARCHAR(64) NOT NULL,
   col95 VARCHAR(64) NOT NULL,
   col96 VARCHAR(64) NOT NULL,
   col97 VARCHAR(64) NOT NULL,
   col98 VARCHAR(64) NOT NULL,
   col99 VARCHAR(64) NOT NULL,
   col100 VARCHAR(64) NOT NULL,
   col101 VARCHAR(64) NOT NULL,
   col102 VARCHAR(64) NOT NULL,
   col103 VARCHAR(64) NOT NULL,
   col104 VARCHAR(64) NOT NULL,
   col105 VARCHAR(64) NOT NULL,
   col106 VARCHAR(64) NOT NULL,
   col107 VARCHAR(64) NOT NULL,
   col108 VARCHAR(64) NOT NULL,
   col109 VARCHAR(64) NOT NULL,
   col110 VARCHAR(64) NOT NULL,
   col111 VARCHAR(64) NOT NULL,
   col112 VARCHAR(64) NOT NULL,
   col113 VARCHAR(64) NOT NULL,
   col114 VARCHAR(64) NOT NULL,
   col115 VARCHAR(64) NOT NULL,
   col116 VARCHAR(64) NOT NULL,
   col117 VARCHAR(64) NOT NULL,
   col118 VARCHAR(64) NOT NULL,
   col119 VARCHAR(64) NOT NULL,
   col120 VARCHAR(64) NOT NULL,
   col121 VARCHAR(64) NOT NULL,
   col122 VARCHAR(64) NOT NULL,
   col123 VARCHAR(64) NOT NULL,
   col124 VARCHAR(64) NOT NULL,
   col125 VARCHAR(64) NOT NULL,
   col126 VARCHAR(64) NOT NULL,
   col127 VARCHAR(64) NOT NULL,
   col128 VARCHAR(64) NOT NULL,
   col129 VARCHAR(64) NOT NULL,
   col130 VARCHAR(64) NOT NULL,
   col131 VARCHAR(64) NOT NULL,
   col132 VARCHAR(64) NOT NULL,
   col133 VARCHAR(64) NOT NULL,
   col134 VARCHAR(64) NOT NULL,
   col135 VARCHAR(64) NOT NULL,
   col136 VARCHAR(64) NOT NULL,
   col137 VARCHAR(64) NOT NULL,
   col138 VARCHAR(64) NOT NULL,
   col139 VARCHAR(64) NOT NULL,
   col140 VARCHAR(64) NOT NULL,
   col141 VARCHAR(64) NOT NULL,
   col142 VARCHAR(64) NOT NULL,
   col143 VARCHAR(64) NOT NULL,
   col144 VARCHAR(64) NOT NULL,
   col145 VARCHAR(64) NOT NULL,
   col146 VARCHAR(64) NOT NULL,
   col147 VARCHAR(64) NOT NULL,
   col148 VARCHAR(64) NOT NULL,
   col149 VARCHAR(64) NOT NULL,
   col150 VARCHAR(64) NOT NULL,
   col151 VARCHAR(64) NOT NULL,
   col152 VARCHAR(64) NOT NULL,
   col153 VARCHAR(64) NOT NULL,
   col154 VARCHAR(64) NOT NULL,
   col155 VARCHAR(64) NOT NULL,
   col156 VARCHAR(64) NOT NULL,
   col157 VARCHAR(64) NOT NULL,
   col158 VARCHAR(64) NOT NULL,
   col159 VARCHAR(64) NOT NULL,
   col160 VARCHAR(64) NOT NULL,
   col161 VARCHAR(64) NOT NULL,
   col162 VARCHAR(64) NOT NULL,
   col163 VARCHAR(64) NOT NULL,
   col164 VARCHAR(64) NOT NULL,
   col165 VARCHAR(64) NOT NULL,
   col166 VARCHAR(64) NOT NULL,
   col167 VARCHAR(64) NOT NULL,
   col168 VARCHAR(64) NOT NULL,
   col169 VARCHAR(64) NOT NULL,
   col170 VARCHAR(64) NOT NULL,
   col171 VARCHAR(64) NOT NULL,
   col172 VARCHAR(64) NOT NULL,
   col173 VARCHAR(64) NOT NULL,
   col174 VARCHAR(64) NOT NULL,
   col175 VARCHAR(64) NOT NULL,
   col176 VARCHAR(64) NOT NULL,
   col177 VARCHAR(64) NOT NULL,
   col178 VARCHAR(64) NOT NULL,
   col179 VARCHAR(64) NOT NULL,
   col180 VARCHAR(64) NOT NULL,
   col181 VARCHAR(64) NOT NULL,
   col182 VARCHAR(64) NOT NULL,
   col183 VARCHAR(64) NOT NULL,
   col184 VARCHAR(64) NOT NULL,
   col185 VARCHAR(64) NOT NULL,
   col186 VARCHAR(64) NOT NULL,
   col187 VARCHAR(64) NOT NULL,
   col188 VARCHAR(64) NOT NULL,
   col189 VARCHAR(64) NOT NULL,
   col190 VARCHAR(64) NOT NULL,
   col191 VARCHAR(64) NOT NULL,
   col192 VARCHAR(64) NOT NULL,
   col193 VARCHAR(64) NOT NULL,
   col194 VARCHAR(64) NOT NULL,
   col195 VARCHAR(64) NOT NULL,
   col196 VARCHAR(64) NOT NULL,
   col197 VARCHAR(64) NOT NULL,
   col198 VARCHAR(64) NOT NULL,
   PRIMARY KEY (col1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## Working Around the Problem

There are a few ways to work around this problem.

If you would like a solution for the problem instead of just working around it, then see the solutions mentioned in the previous section.

### Refactoring the Table into Multiple Tables

A _safe_ workaround is to refactor the single wide table, so that its columns are spread among multiple tables.

This workaround can even work if your table is so wide that the previous solutions have failed to solve them problem for your table.

### Refactoring Some Columns into JSON

A _safe_ workaround is to refactor some of the columns into a JSON document.

The JSON document can be queried and manipulated using MariaDB's [JSON functions](../../../../reference/sql-functions/special-functions/json-functions/).

The JSON document can be stored in a column that uses one of the following data types:

* [TEXT](../../../../reference/data-types/string-data-types/text.md): The maximum size of a [TEXT](../../../../reference/data-types/string-data-types/text.md) column is 64 KB.
* [MEDIUMTEXT](../../../../reference/data-types/string-data-types/mediumtext.md): The maximum size of a [MEDIUMTEXT](../../../../reference/data-types/string-data-types/mediumtext.md) column is 16 MB.
* [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md): The maximum size of a [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md) column is 4 GB.
* [JSON](../../../../reference/data-types/string-data-types/json.md): This is just an alias for the [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md) data type.

This workaround can even work if your table is so wide that the previous solutions have failed to solve them problem for your table.

### Disabling InnoDB Strict Mode

An _unsafe_ workaround is to disable [InnoDB strict mode](../innodb-strict-mode.md). [InnoDB strict mode](../innodb-strict-mode.md) can be disabled by setting the [innodb\_strict\_mode](../innodb-system-variables.md) system variable to `OFF`.

For example, even though the following table schema is too large for most InnoDB row formats to store, it can still be created when [InnoDB strict mode](../innodb-strict-mode.md) is disabled:

```sql
SET GLOBAL innodb_default_row_format='dynamic';
SET SESSION innodb_strict_mode=OFF;
CREATE OR REPLACE TABLE tab (
   col1 VARCHAR(40) NOT NULL,
   col2 VARCHAR(40) NOT NULL,
   col3 VARCHAR(40) NOT NULL,
   col4 VARCHAR(40) NOT NULL,
   col5 VARCHAR(40) NOT NULL,
   col6 VARCHAR(40) NOT NULL,
   col7 VARCHAR(40) NOT NULL,
   col8 VARCHAR(40) NOT NULL,
   col9 VARCHAR(40) NOT NULL,
   col10 VARCHAR(40) NOT NULL,
   col11 VARCHAR(40) NOT NULL,
   col12 VARCHAR(40) NOT NULL,
   col13 VARCHAR(40) NOT NULL,
   col14 VARCHAR(40) NOT NULL,
   col15 VARCHAR(40) NOT NULL,
   col16 VARCHAR(40) NOT NULL,
   col17 VARCHAR(40) NOT NULL,
   col18 VARCHAR(40) NOT NULL,
   col19 VARCHAR(40) NOT NULL,
   col20 VARCHAR(40) NOT NULL,
   col21 VARCHAR(40) NOT NULL,
   col22 VARCHAR(40) NOT NULL,
   col23 VARCHAR(40) NOT NULL,
   col24 VARCHAR(40) NOT NULL,
   col25 VARCHAR(40) NOT NULL,
   col26 VARCHAR(40) NOT NULL,
   col27 VARCHAR(40) NOT NULL,
   col28 VARCHAR(40) NOT NULL,
   col29 VARCHAR(40) NOT NULL,
   col30 VARCHAR(40) NOT NULL,
   col31 VARCHAR(40) NOT NULL,
   col32 VARCHAR(40) NOT NULL,
   col33 VARCHAR(40) NOT NULL,
   col34 VARCHAR(40) NOT NULL,
   col35 VARCHAR(40) NOT NULL,
   col36 VARCHAR(40) NOT NULL,
   col37 VARCHAR(40) NOT NULL,
   col38 VARCHAR(40) NOT NULL,
   col39 VARCHAR(40) NOT NULL,
   col40 VARCHAR(40) NOT NULL,
   col41 VARCHAR(40) NOT NULL,
   col42 VARCHAR(40) NOT NULL,
   col43 VARCHAR(40) NOT NULL,
   col44 VARCHAR(40) NOT NULL,
   col45 VARCHAR(40) NOT NULL,
   col46 VARCHAR(40) NOT NULL,
   col47 VARCHAR(40) NOT NULL,
   col48 VARCHAR(40) NOT NULL,
   col49 VARCHAR(40) NOT NULL,
   col50 VARCHAR(40) NOT NULL,
   col51 VARCHAR(40) NOT NULL,
   col52 VARCHAR(40) NOT NULL,
   col53 VARCHAR(40) NOT NULL,
   col54 VARCHAR(40) NOT NULL,
   col55 VARCHAR(40) NOT NULL,
   col56 VARCHAR(40) NOT NULL,
   col57 VARCHAR(40) NOT NULL,
   col58 VARCHAR(40) NOT NULL,
   col59 VARCHAR(40) NOT NULL,
   col60 VARCHAR(40) NOT NULL,
   col61 VARCHAR(40) NOT NULL,
   col62 VARCHAR(40) NOT NULL,
   col63 VARCHAR(40) NOT NULL,
   col64 VARCHAR(40) NOT NULL,
   col65 VARCHAR(40) NOT NULL,
   col66 VARCHAR(40) NOT NULL,
   col67 VARCHAR(40) NOT NULL,
   col68 VARCHAR(40) NOT NULL,
   col69 VARCHAR(40) NOT NULL,
   col70 VARCHAR(40) NOT NULL,
   col71 VARCHAR(40) NOT NULL,
   col72 VARCHAR(40) NOT NULL,
   col73 VARCHAR(40) NOT NULL,
   col74 VARCHAR(40) NOT NULL,
   col75 VARCHAR(40) NOT NULL,
   col76 VARCHAR(40) NOT NULL,
   col77 VARCHAR(40) NOT NULL,
   col78 VARCHAR(40) NOT NULL,
   col79 VARCHAR(40) NOT NULL,
   col80 VARCHAR(40) NOT NULL,
   col81 VARCHAR(40) NOT NULL,
   col82 VARCHAR(40) NOT NULL,
   col83 VARCHAR(40) NOT NULL,
   col84 VARCHAR(40) NOT NULL,
   col85 VARCHAR(40) NOT NULL,
   col86 VARCHAR(40) NOT NULL,
   col87 VARCHAR(40) NOT NULL,
   col88 VARCHAR(40) NOT NULL,
   col89 VARCHAR(40) NOT NULL,
   col90 VARCHAR(40) NOT NULL,
   col91 VARCHAR(40) NOT NULL,
   col92 VARCHAR(40) NOT NULL,
   col93 VARCHAR(40) NOT NULL,
   col94 VARCHAR(40) NOT NULL,
   col95 VARCHAR(40) NOT NULL,
   col96 VARCHAR(40) NOT NULL,
   col97 VARCHAR(40) NOT NULL,
   col98 VARCHAR(40) NOT NULL,
   col99 VARCHAR(40) NOT NULL,
   col100 VARCHAR(40) NOT NULL,
   col101 VARCHAR(40) NOT NULL,
   col102 VARCHAR(40) NOT NULL,
   col103 VARCHAR(40) NOT NULL,
   col104 VARCHAR(40) NOT NULL,
   col105 VARCHAR(40) NOT NULL,
   col106 VARCHAR(40) NOT NULL,
   col107 VARCHAR(40) NOT NULL,
   col108 VARCHAR(40) NOT NULL,
   col109 VARCHAR(40) NOT NULL,
   col110 VARCHAR(40) NOT NULL,
   col111 VARCHAR(40) NOT NULL,
   col112 VARCHAR(40) NOT NULL,
   col113 VARCHAR(40) NOT NULL,
   col114 VARCHAR(40) NOT NULL,
   col115 VARCHAR(40) NOT NULL,
   col116 VARCHAR(40) NOT NULL,
   col117 VARCHAR(40) NOT NULL,
   col118 VARCHAR(40) NOT NULL,
   col119 VARCHAR(40) NOT NULL,
   col120 VARCHAR(40) NOT NULL,
   col121 VARCHAR(40) NOT NULL,
   col122 VARCHAR(40) NOT NULL,
   col123 VARCHAR(40) NOT NULL,
   col124 VARCHAR(40) NOT NULL,
   col125 VARCHAR(40) NOT NULL,
   col126 VARCHAR(40) NOT NULL,
   col127 VARCHAR(40) NOT NULL,
   col128 VARCHAR(40) NOT NULL,
   col129 VARCHAR(40) NOT NULL,
   col130 VARCHAR(40) NOT NULL,
   col131 VARCHAR(40) NOT NULL,
   col132 VARCHAR(40) NOT NULL,
   col133 VARCHAR(40) NOT NULL,
   col134 VARCHAR(40) NOT NULL,
   col135 VARCHAR(40) NOT NULL,
   col136 VARCHAR(40) NOT NULL,
   col137 VARCHAR(40) NOT NULL,
   col138 VARCHAR(40) NOT NULL,
   col139 VARCHAR(40) NOT NULL,
   col140 VARCHAR(40) NOT NULL,
   col141 VARCHAR(40) NOT NULL,
   col142 VARCHAR(40) NOT NULL,
   col143 VARCHAR(40) NOT NULL,
   col144 VARCHAR(40) NOT NULL,
   col145 VARCHAR(40) NOT NULL,
   col146 VARCHAR(40) NOT NULL,
   col147 VARCHAR(40) NOT NULL,
   col148 VARCHAR(40) NOT NULL,
   col149 VARCHAR(40) NOT NULL,
   col150 VARCHAR(40) NOT NULL,
   col151 VARCHAR(40) NOT NULL,
   col152 VARCHAR(40) NOT NULL,
   col153 VARCHAR(40) NOT NULL,
   col154 VARCHAR(40) NOT NULL,
   col155 VARCHAR(40) NOT NULL,
   col156 VARCHAR(40) NOT NULL,
   col157 VARCHAR(40) NOT NULL,
   col158 VARCHAR(40) NOT NULL,
   col159 VARCHAR(40) NOT NULL,
   col160 VARCHAR(40) NOT NULL,
   col161 VARCHAR(40) NOT NULL,
   col162 VARCHAR(40) NOT NULL,
   col163 VARCHAR(40) NOT NULL,
   col164 VARCHAR(40) NOT NULL,
   col165 VARCHAR(40) NOT NULL,
   col166 VARCHAR(40) NOT NULL,
   col167 VARCHAR(40) NOT NULL,
   col168 VARCHAR(40) NOT NULL,
   col169 VARCHAR(40) NOT NULL,
   col170 VARCHAR(40) NOT NULL,
   col171 VARCHAR(40) NOT NULL,
   col172 VARCHAR(40) NOT NULL,
   col173 VARCHAR(40) NOT NULL,
   col174 VARCHAR(40) NOT NULL,
   col175 VARCHAR(40) NOT NULL,
   col176 VARCHAR(40) NOT NULL,
   col177 VARCHAR(40) NOT NULL,
   col178 VARCHAR(40) NOT NULL,
   col179 VARCHAR(40) NOT NULL,
   col180 VARCHAR(40) NOT NULL,
   col181 VARCHAR(40) NOT NULL,
   col182 VARCHAR(40) NOT NULL,
   col183 VARCHAR(40) NOT NULL,
   col184 VARCHAR(40) NOT NULL,
   col185 VARCHAR(40) NOT NULL,
   col186 VARCHAR(40) NOT NULL,
   col187 VARCHAR(40) NOT NULL,
   col188 VARCHAR(40) NOT NULL,
   col189 VARCHAR(40) NOT NULL,
   col190 VARCHAR(40) NOT NULL,
   col191 VARCHAR(40) NOT NULL,
   col192 VARCHAR(40) NOT NULL,
   col193 VARCHAR(40) NOT NULL,
   col194 VARCHAR(40) NOT NULL,
   col195 VARCHAR(40) NOT NULL,
   col196 VARCHAR(40) NOT NULL,
   col197 VARCHAR(40) NOT NULL,
   col198 VARCHAR(40) NOT NULL,
   PRIMARY KEY (col1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

But as mentioned above, if [InnoDB strict mode](../innodb-strict-mode.md) is **disabled** and if a [DDL](../../../../reference/sql-statements/data-definition/) statement is executed, then InnoDB will still raise a **warning** with this message. The [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) statement can be used to view the warning:

```sql
SHOW WARNINGS;
+---------+------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Level | Code | Message |
+---------+------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Warning | 139 | Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In current row format, BLOB prefix of 0 bytes is stored inline. |
+---------+------+----------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.000 sec)
```

As mentioned above, even though InnoDB is allowing the table to be created, there is still an opportunity for errors. Regardless of whether [InnoDB strict mode](../innodb-strict-mode.md) is enabled, if a [DML](../../../../reference/sql-statements/data-manipulation/) statement is executed that attempts to write a row that the table's InnoDB row format can't store, then InnoDB will raise an **error** with this message. This creates a somewhat _unsafe_ situation, because it means that the application has the chance to encounter an additional error while executing [DML](../../../../reference/sql-statements/data-manipulation/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
