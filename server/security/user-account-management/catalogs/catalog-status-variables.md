---
description: >-
  Covers status variables related to catalog operations and performance, useful
  for monitoring multi-tenant environments.
---

# Catalog Status Variables

{% include "../../../.gitbook/includes/catalogs.md" %}

When using a MariaDB Server with [catalogs](./) support, all status information is collected for the whole server, per catalog and per session.

```sql
SHOW SERVER STATUS;
```

shows the status for the whole server. Note that only the super user in the 'def' catalog has privileges for the above statement.

```sql
SHOW GLOBAL STATUS;
SHOW CATALOG STATUS;
```

Both commands show the status for the current catalog.\
The reason that `GLOBAL` shows catalog status is that because catalogs are 'multi-tenant', a\
catalog user should not be able to see the status from other users (for most things).

```sql
SHOW [SESSION] STATUS;
```

Shows the status for the current connection.

The main "new thing" is that catalogs enable SAS providers to see the status for a single tenant (catalog user).\
This makes it much easier to find 'bad neighbors' (tenants that cause problems for other tenants) so that they can be moved to other servers.

When the MariaDB server is not configured for catalogs, the following commands are equivalent:

```sql
SHOW GLOBAL STATUS
SHOW SERVER STATUS 
SHOW CATALOG STATUS
```

## See Also

* [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
