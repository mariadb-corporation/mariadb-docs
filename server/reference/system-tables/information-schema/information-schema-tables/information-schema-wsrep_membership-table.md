---
description: >-
  The Information Schema WSREP_MEMBERSHIP table lists the current members of the
  Galera Cluster, including their node UUIDs, names, and IP addresses.
---

# Information Schema WSREP\_MEMBERSHIP Table

The `WSREP_STATUS` table makes [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) node cluster membership information available through the [Information Schema](../). The same information can be returned using the [SHOW WSREP\_MEMBERSHIP](../../../sql-statements/administrative-sql-statements/show/show-wsrep_membership.md) statement. Only users with the [SUPER](../../../sql-statements/account-management-sql-statements/grant.md#super) can access information from this table.

The `WSREP_MEMBERSHIP` table is part of the [WSREP\_INFO plugin](../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md).

## Example

```sql
SELECT * FROM information_schema.WSREP_MEMBERSHIP;
+-------+--------------------------------------+-------+-----------------+
| INDEX | UUID                                 | NAME  | ADDRESS         |
+-------+--------------------------------------+-------+-----------------+
|     0 | 46da96e3-6e9e-11e4-95a2-f609aa5444b3 | node1 | 10.0.2.15:16000 |
|     1 | 5f6bc72a-6e9e-11e4-84ed-57ec6780a3d3 | node2 | 10.0.2.15:16001 |
|     2 | 7473fd75-6e9e-11e4-91de-0b541ad91bd0 | node3 | 10.0.2.15:16002 |
+-------+--------------------------------------+-------+-----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
