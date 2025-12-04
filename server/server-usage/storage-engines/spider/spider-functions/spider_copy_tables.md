# SPIDER\_COPY\_TABLES

## Syntax

```
SPIDER_COPY_TABLES(spider_table_name, 
  source_link_id, destination_link_id_list [,parameters])
```

## Description

A [UDF](../../../../server-usage/user-defined-functions/) installed with the [Spider Storage Engine](../), this function copies table data from `source_link_id` to `destination_link_id_list`. The service does not need to be stopped in order to copy.

If the Spider table is partitioned, the name must be of the format `table_name#P#partition_name`. The partition name can be viewed in the `mysql.spider_tables` table, for example:

```sql
SELECT table_name FROM mysql.spider_tables;
+-------------+
| table_name  |
+-------------+
| spt_a#P#pt1 |
| spt_a#P#pt2 |
| spt_a#P#pt3 |
+-------------+
```

Returns `1` if the data was copied successfully, or `0` if copying the data failed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
