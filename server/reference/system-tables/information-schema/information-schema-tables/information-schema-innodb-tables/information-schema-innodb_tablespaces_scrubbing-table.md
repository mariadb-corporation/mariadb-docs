---
description: >-
  The INNODB_TABLESPACES_SCRUBBING table contains statistics about background
  data scrubbing processes for InnoDB tablespaces.
---

# Information Schema INNODB\_TABLESPACES\_SCRUBBING Table

{% hint style="info" %}
This table was removed in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes) - see [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528).
{% endhint %}

The [Information Schema](../../) `INNODB_TABLESPACES_SCRUBBING` table contains [data scrubbing](../../../../../server-usage/storage-engines/innodb/innodb-data-scrubbing.md) information.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column                            | Description                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| SPACE                             | InnoDB table space id number.                                                                                                        |
| NAME                              | Path to the table space file, without the extension.                                                                                 |
| COMPRESSED                        | The compressed page size, or zero if uncompressed.                                                                                   |
| LAST\_SCRUB\_COMPLETED            | Date and time when the last scrub was completed, or NULL if never been performed.                                                    |
| CURRENT\_SCRUB\_STARTED           | Date and time when the current scrub started, or NULL if never been performed.                                                       |
| CURRENT\_SCRUB\_ACTIVE\_THREADS   | Number of threads currently scrubbing the tablespace.                                                                                |
| CURRENT\_SCRUB\_PAGE\_NUMBER      | Page that the scrubbing thread is currently scrubbing, or NULL if not enabled.                                                       |
| CURRENT\_SCRUB\_MAX\_PAGE\_NUMBER | When a scrubbing starts rotating a table space, the field contains its current size. NULL if not enabled.                            |
| ON\_SSD                           | The field contains 1 when MariaDB detects that the table space is on a SSD based storage. 0 if not SSD or it could not be determined |

## Example

```sql
SELECT * FROM information_schema.INNODB_TABLESPACES_SCRUBBING LIMIT 1\G
*************************** 1. row ***************************
                        SPACE: 1
                         NAME: mysql/innodb_table_stats
                   COMPRESSED: 0
         LAST_SCRUB_COMPLETED: NULL
        CURRENT_SCRUB_STARTED: NULL
    CURRENT_SCRUB_PAGE_NUMBER: NULL
CURRENT_SCRUB_MAX_PAGE_NUMBER: 0
         ROTATING_OR_FLUSHING: 0
1 rows in set (0.00 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
