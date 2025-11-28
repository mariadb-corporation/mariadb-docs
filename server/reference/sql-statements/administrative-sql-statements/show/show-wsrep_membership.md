---
description: >-
  View Galera Cluster membership. This statement displays the UUID, name, and
  address of nodes in the cluster.
---

# SHOW WSREP\_MEMBERSHIP

`SHOW WSREP_MEMBERSHIP` is part of the [WSREP\_INFO](../../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) plugin.

## Syntax

```sql
SHOW WSREP_MEMBERSHIP
```

## Description

The `SHOW WSREP_MEMBERSHIP` statement returns [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) node cluster membership information. It returns the same information as found in the [information\_schema.WSREP\_MEMBERSHIP](../../../system-tables/information-schema/information-schema-tables/information-schema-wsrep_membership-table.md) table. Only users with the [SUPER](../../account-management-sql-commands/grant.md) privilege can access this information.

## Examples

```sql
SHOW WSREP_MEMBERSHIP;
+-------+--------------------------------------+----------+-----------------+
| Index | Uuid                                 | Name     | Address         |
+-------+--------------------------------------+----------+-----------------+
|     0 | 19058073-8940-11e4-8570-16af7bf8fced | my_node1 | 10.0.2.15:16001 |
|     1 | 19f2b0e0-8942-11e4-9cb8-b39e8ee0b5dd | my_node3 | 10.0.2.15:16003 |
|     2 | d85e62db-8941-11e4-b1ef-4bc9980e476d | my_node2 | 10.0.2.15:16002 |
+-------+--------------------------------------+----------+-----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
