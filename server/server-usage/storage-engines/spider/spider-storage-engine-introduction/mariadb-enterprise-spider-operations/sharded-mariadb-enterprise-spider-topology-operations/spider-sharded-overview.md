# Spider Sharded Overview

## Overview

Choose an operation for the Sharded MariaDB Enterprise Spider topology:

| Operation                                                                                            | Description                                                      |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [Add a Shard](sharded-mariadb-enterprise-spider-topology-add-a-shard.md)                             | How to add a new shard to a Spider Table.                        |
| [Backup and Restore](sharded-mariadb-enterprise-spider-topology-backup-and-restore.md)               | How to create a new backup or restore an existing backup.        |
| [Update Character Set or Collation](spider-sharded-overview.md#update-character-sets-and-collations) | How to update the character set or collation for a Spider Table. |
| [Update Connection Options](spider-sharded-overview.md#update-connection-options)                    | How to update the connection options for a Data Node.            |

## Update Character Sets and Collations

The character set or collation for the Spider Table can be updated or modified using the [ALTER TABLE](../../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

On the Spider Node, alter the Spider Table's character set and collation:

```sql
ALTER TABLE spider_sharded_sales.invoices
   DEFAULT CHARACTER SET 'utf8mb4'
   DEFAULT COLLATE 'utf8mb4_general_ci';
```

If the new character set and collation are not compatible with the character set and collation used by the Data Table, you must also alter the character set and collation for the Data Table on the Data Node.

## Update Connection Options

In a Sharded MariaDB Enterprise Spider topology, the connection options for a Data Node can be updated using the [ALTER TABLE](../../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

On the Spider Node, alter the partition's connection details:

```sql
ALTER TABLE spider_sharded_sales.invoices
   REORGANIZE PARTITION hq_partition INTO (
      PARTITION hq_partition VALUES IN (1) COMMENT = 'server "new_hq_server", table "invoices"'
   );
```

{% @marketo/form formId="4316" %}
