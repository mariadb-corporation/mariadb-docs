---
description: >-
  Learn how to resolve inconsistencies between the InnoDB internal data
  dictionary and the file system, such as orphan .frm or .ibd files.
---

# InnoDB Data Dictionary Troubleshooting

## Can't Open File

If InnoDB returns something like the following error:

```
ERROR 1016: Can't open file: 'x.ibd'. (errno: 1)
```

it may be that an orphan `.frm` file exists. Something like the following may also appear in the [error log](../../../../server-management/server-monitoring-logs/error-log.md):

```
InnoDB: Cannot find table test/x from the internal data dictionary
InnoDB: of InnoDB though the .frm file for the table exists. Maybe you
InnoDB: have deleted and recreated InnoDB data files but have forgotten
InnoDB: to delete the corresponding .frm files of InnoDB tables?
```

If this is the case, as the text describes, delete the orphan `.frm` file on the filesystem.

## Could not find a valid tablespace file

In this case the table definition, the `.frm` file, is missing and the InnoDB dictionary expects it to be there. To remove the InnoDB dictionary entry, the existence of the file needs to faked and then dropped. The existence of the file is faked by creating the `tablename.frm` and potential the database directory if it is missing. Then a `DROP TABLE` or `DROP DATABASE` can be executed which will remove the InnoDB dictionary entry.

Use the query to identify potentially other tablespaces that are known but missing with:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE NAME LIKE 'dbname/%';
```

## Removing Orphan Intermediate Tables

An orphan intermediate table may prevent you from dropping the tablespace even if it is otherwise empty, and generally takes up unnecessary space.

It may come about if MariaDB exits in the middle of an [ALTER TABLE ... ALGORITHM=INPLACE](../../../../reference/sql-statements/data-definition/alter/alter-table/#algorithm) operation. They are listed in the [INFORMATION\_SCHEMA.INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table, and always start with an `#sql-ib` prefix. The accompanying `.frm` file also begins with `#sql-`, but has a different name.

To identify orphan tables, run:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE NAME LIKE '%#sql%';
```

When [innodb\_file\_per\_table](../innodb-system-variables.md) is set, the `#sql-*.ibd` file will also be visible in the database directory.

To remove an orphan intermediate table:

* Rename the `#sql-*.frm` file (in the database directory) to match the base name of the orphan intermediate table, for example:

```
mv #sql-36ab_2.frm #sql-ib87-856498050.frm
```

* Drop the table, for example:

```sql
DROP TABLE `#mysql50##sql-ib87-856498050`;
```

## See Also

* [InnoDB Troubleshooting Overview](innodb-troubleshooting-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
