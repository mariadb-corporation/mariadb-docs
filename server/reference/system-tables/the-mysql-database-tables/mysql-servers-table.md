---
description: >-
  The mysql.servers table stores connection information for remote servers, used
  by the FEDERATED and Spider storage engines.
---

# mysql.servers Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.servers` table contains information about servers as used by the [Spider](../../../server-usage/storage-engines/spider/), [FEDERATED](../../../server-usage/storage-engines/legacy-storage-engines/federated-storage-engine.md) or [FederatedX](../../../server-usage/storage-engines/federatedx-storage-engine/), [Connect](../../../server-usage/storage-engines/connect/) storage engines.

The contents are modified by the [CREATE SERVER](../../sql-statements/data-definition/create/create-server.md), [ALTER SERVER](../../sql-statements/data-definition/alter/alter-server.md) and [DROP SERVER](../../sql-statements/data-definition/drop/drop-server.md) statements.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.servers` table contains the following fields:

| Field        | Type     | Null | Key | Default | Description      |
| ------------ | -------- | ---- | --- | ------- | ---------------- |
| Server\_name | char(64) | NO   | PRI |         |                  |
| Host         | char(64) | NO   |     |         |                  |
| Db           | char(64) | NO   |     |         |                  |
| Username     | char(80) | NO   |     |         |                  |
| Password     | char(64) | NO   |     |         |                  |
| Port         | int(4)   | NO   |     | 0       |                  |
| Socket       | char(64) | NO   |     |         |                  |
| Wrapper      | char(64) | NO   |     |         | mysql or mariadb |
| Owner        | char(64) | NO   |     |         |                  |

## Example

```sql
SELECT * FROM mysql.servers\G
*************************** 1. row ***************************
Server_name: s
       Host: 192.168.1.106
         Db: test
   Username: Remote
   Password: 
       Port: 0
     Socket: 
    Wrapper: mariadb
      Owner:
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
