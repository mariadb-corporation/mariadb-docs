---
description: >-
  mysql_info returns a string with summary statistics about the last executed
  query, covering INSERT, UPDATE, ALTER TABLE, and LOAD DATA operations; returns
  NULL for SELECT.
---

# mysql\_info

## Syntax

```c
const char * mysql_info(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

The `mysql_info()` function returns a string providing information about the last query executed.

## Return Value

Possible `mysql_info` return values.  The nature of this string is provided below:

| Query type                                                                                                                                                                               | Example result string                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [INSERT INTO...SELECT...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data)                                              | Records: 100 Duplicates: 0 Warnings: 0       |
| [INSERT INTO...VALUES (...),(...),(...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data)                               | Records: 3 Duplicates: 0 Warnings: 0         |
| [LOAD DATA INFILE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) | Records: 1 Deleted: 0 Skipped: 0 Warnings: 0 |
| [ALTER TABLE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table)                                                             | Records: 3 Duplicates: 0 Warnings: 0         |
| [UPDATE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update)                                                    | Rows matched: 40 Changed: 40 Warnings: 0     |

{% hint style="info" %}
Queries which do not fall into one of the preceding formats are not supported (e.g. [SELECT ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select)). In these situations, `mysql_info()` will return `NULL`.
{% endhint %}

## See Also

* [mysql\_affected\_rows()](mysql_affected_rows.md)
* [mysql\_warning\_count()](mysql_warning_count.md)

{% @marketo/form formId="4316" %}
