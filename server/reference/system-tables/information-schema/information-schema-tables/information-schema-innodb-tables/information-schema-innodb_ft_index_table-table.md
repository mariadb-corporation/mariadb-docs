---
description: >-
  The INNODB_FT_INDEX_TABLE table provides information about the inverted index
  (tokens and positions) for an InnoDB FULLTEXT index currently in use.
---

# Information Schema INNODB\_FT\_INDEX\_TABLE Table

The [Information Schema](../../) `INNODB_FT_INDEX_TABLE` table contains information about InnoDB [fulltext indexes](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). To avoid re-organizing the fulltext index each time a change is made, which would be very expensive, new changes are stored separately and only integrated when an [OPTIMIZE TABLE](../../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) is run. See the [INNODB\_FT\_INDEX\_CACHE](information-schema-innodb_ft_index_cache-table.md) table.

The `SUPER` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table, and it also requires the [innodb\_ft\_aux\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_aux_table) system variable to be set.

It has the following columns:

| Column         | Description                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| WORD           | Word from the text of a column with a fulltext index. Words can appear multiple times in the table, once per DOC\_ID and POSITION combination. |
| FIRST\_DOC\_ID | First document ID where this word appears in the index.                                                                                        |
| LAST\_DOC\_ID  | Last document ID where this word appears in the index.                                                                                         |
| DOC\_COUNT     | Number of rows containing this word in the index.                                                                                              |
| DOC\_ID        | Document ID of the newly added row, either an appropriate ID column or an internal InnoDB value.                                               |
| POSITION       | Position of this word instance within the DOC\_ID, as an offset added to the previous POSITION instance.                                       |

Note that for `OPTIMIZE TABLE` to process InnoDB fulltext index data, the [innodb\_optimize\_fulltext\_only](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_optimize_fulltext_only) system variable needs to be set to `1`. When this is done, and an `OPTIMIZE TABLE` statement run, the [INNODB\_FT\_INDEX\_CACHE](information-schema-innodb_ft_index_cache-table.md) table will be emptied, and the `INNODB_FT_INDEX_TABLE` table will be updated.

## Examples

```sql
SELECT * FROM INNODB_FT_INDEX_TABLE;
Empty set (0.00 sec)

SET GLOBAL innodb_optimize_fulltext_only =1;

OPTIMIZE TABLE test.ft_innodb;
+----------------+----------+----------+----------+
| Table          | Op       | Msg_type | Msg_text |
+----------------+----------+----------+----------+
| test.ft_innodb | optimize | status   | OK       |
+----------------+----------+----------+----------+

SELECT * FROM INNODB_FT_INDEX_TABLE;
+------------+--------------+-------------+-----------+--------+----------+
| WORD       | FIRST_DOC_ID | LAST_DOC_ID | DOC_COUNT | DOC_ID | POSITION |
+------------+--------------+-------------+-----------+--------+----------+
| and        |            4 |           5 |         2 |      4 |        0 |
| and        |            4 |           5 |         2 |      5 |        0 |
| arrived    |            4 |           4 |         1 |      4 |       20 |
| ate        |            1 |           5 |         2 |      1 |        4 |
| ate        |            1 |           5 |         2 |      5 |        8 |
| everybody  |            1 |           1 |         1 |      1 |        8 |
| goldilocks |            4 |           4 |         1 |      4 |        9 |
| hungry     |            3 |           3 |         1 |      3 |        8 |
| pear       |            5 |           5 |         1 |      5 |       14 |
| she        |            5 |           5 |         1 |      5 |        4 |
| then       |            4 |           4 |         1 |      4 |        4 |
| wicked     |            2 |           2 |         1 |      2 |        4 |
| witch      |            2 |           2 |         1 |      2 |       11 |
+------------+--------------+-------------+-----------+--------+----------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
