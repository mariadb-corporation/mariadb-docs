---
description: >-
  The INNODB_FT_DEFAULT_STOPWORD table lists the default stop words used by
  InnoDB FULLTEXT indexes when no custom stopword list is defined.
---

# Information Schema INNODB\_FT\_DEFAULT\_STOPWORD Table

The [Information Schema](../../) `INNODB_FT_DEFAULT_STOPWORD` table contains a list of default [stopwords](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) used when creating an InnoDB [fulltext index](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).

The [PROCESS](../../../../sql-statements/account-management-sql-statements/grant.md#process) privilege is required to view the table.

It has the following column:

| Column | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VALUE  | Default [stopword](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) for an InnoDB [fulltext index](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). Setting either the [innodb\_ft\_server\_stopword\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) or the [innodb\_ft\_user\_stopword\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) system variable will override this. |

## Example

```sql
SELECT * FROM information_schema.INNODB_FT_DEFAULT_STOPWORD\G
*************************** 1. row ***************************
value: a
*************************** 2. row ***************************
value: about
*************************** 3. row ***************************
value: an
*************************** 4. row ***************************
value: are
...
*************************** 36. row ***************************
value: www
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
