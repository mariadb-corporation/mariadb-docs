# Spider Federated Overview

## Overview

Choose an operation for the Sharded MariaDB Enterprise Spider topology:

| Operation                                                                                              | Description                                               |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| [Backup and Restore](federated-mariadb-enterprise-spider-topology-backup-and-restore.md)               | How to create a new backup or restore an existing backup. |
| [Migrate Tables](federated-mariadb-enterprise-spider-topology-migrate-tables.md)                       | How to update the character set or collation.             |
| [Update Character Set or Collation](spider-federated-overview.md#update-character-sets-and-collations) | How to update the character set or collation.             |
| [Update Connection Options](spider-federated-overview.md#update-connection-options)                    | How to update the connection options for a Data Node.     |

## Update Character Sets and Collations

The character set or collation for the Spider Table can be updated or modified using the [ALTER TABLE](../../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

On the Spider Node, alter the Spider Table's character set and collation:

```sql
ALTER TABLE spider_hq_sales.invoices
   DEFAULT CHARACTER SET 'utf8mb4'
   DEFAULT COLLATE 'utf8mb4_general_ci';
```

If the new character set and collation are not compatible with the character set and collation used by the Data Table, you must also alter the character set and collation for the Data Table on the Data Node.

## Update Connection Options

In a Federated MariaDB Enterprise Spider topology, the connection options for a Data Node can be updated using the [ALTER TABLE](../../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

* On the Spider Node\*, alter the table's connection details:

```sql
ALTER TABLE spider_hq_sales.invoices
   COMMENT = 'server "new_hq_server", table "invoices"'
```

{% include "../../../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
