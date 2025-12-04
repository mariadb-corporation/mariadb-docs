# SPIDER\_DIRECT\_SQL

## Syntax

```
SPIDER_DIRECT_SQL('sql', 'tmp_table_list', 'parameters')
```

## Description

A [UDF](../../../../server-usage/user-defined-functions/) installed with the [Spider Storage Engine](../), this function is used to execute the SQL string `sql` on the remote server, as defined in `parameters`. If any resultsets are returned, they are stored in the `tmp_table_list`.

The function returns `1` if the SQL executes successfully, or `0` if it fails.

## Examples

```sql
SELECT SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"');
+----------------------------------------------------------------------+
| SPIDER_DIRECT_SQL('SELECT * FROM s', '', 'srv "node1", port "8607"') |
+----------------------------------------------------------------------+
|                                                                    1 |
+----------------------------------------------------------------------+
```

## See also

* [SPIDER\_BG\_DIRECT\_SQL](spider_bg_direct_sql.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
