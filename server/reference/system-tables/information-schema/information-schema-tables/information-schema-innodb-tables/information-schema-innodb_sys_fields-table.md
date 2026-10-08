---
description: >-
  The INNODB_SYS_FIELDS table lists the fields that comprise InnoDB indexes,
  detailing their position within the index structure.
---

# Information Schema INNODB\_SYS\_FIELDS Table

The [Information Schema](../../) `INNODB_SYS_FIELDS` table contains information about fields that are part of an InnoDB index.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column    | Description                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------- |
| INDEX\_ID | Index identifier, matching the value from [INNODB\_SYS\_INDEXES.INDEX\_ID](information-schema-innodb_sys_indexes-table.md). |
| NAME      | Field name, matching the value from [INNODB\_SYS\_COLUMNS.NAME](information-schema-innodb_sys_columns-table.md).            |
| POS       | Ordinal position of the field within the index, starting from 0. This is adjusted as columns are removed.                   |

## Example

```sql
SELECT * FROM information_schema.INNODB_SYS_FIELDS LIMIT 3\G
*************************** 1. row ***************************
INDEX_ID: 11
    NAME: ID
     POS: 0
*************************** 2. row ***************************
INDEX_ID: 12
    NAME: FOR_NAME 
     POS: 0
*************************** 3. row ***************************
INDEX_ID: 13
    NAME: REF_NAME 
     POS: 0
3 rows in set (0.00 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
