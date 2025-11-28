---
description: >-
  View Galera Cluster status variables. This statement displays internal status
  metrics for the wsrep provider.
---

# SHOW WSREP\_STATUS

`SHOW WSREP_STATUS` is part of the [WSREP\_INFO](../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) plugin.

## Syntax

```sql
SHOW WSREP_STATUS
```

## Description

The `SHOW WSREP_STATUS` statement returns [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) node and cluster status information. It returns the same information as found in the [information\_schema.WSREP\_STATUS](../../../system-tables/information-schema/information-schema-tables/information-schema-wsrep_status-table.md) table. Only users with the [SUPER](../../account-management-sql-statements/grant.md#super) privilege can access this information.

## Examples

```sql
SHOW WSREP_STATUS;
+------------+-------------+----------------+--------------+
| Node_Index | Node_Status | Cluster_Status | Cluster_Size |
+------------+-------------+----------------+--------------+
|          0 | Synced      | Primary        |            3 |
+------------+-------------+----------------+--------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
