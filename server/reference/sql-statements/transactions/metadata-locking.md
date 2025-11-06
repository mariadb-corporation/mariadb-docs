# Metadata Locking

MariaDB supports metadata locking. This means that when a transaction (including [XA transactions](xa-transactions.md)) uses a table, it locks its metadata until the end of transaction. Non-transactional tables are also locked, as well as views and objects which are related to locked tables/views (stored functions, triggers, etc). When a connection tries to use a DDL statement (like an [ALTER TABLE](../data-definition/alter/alter-table/)) which modifies a table that is locked, that connection is queued, and has to wait until it's unlocked. Using savepoints and performing a partial rollback does not release metadata locks.

[LOCK TABLES ... WRITE](lock-tables.md) are also queued. Some wrong statements which produce an error may not need to wait for the lock to be freed.

The metadata lock's timeout is determined by the value of the [lock\_wait\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) server system variable (in seconds). However, note that its default value is 31536000 (1 year). If this timeout is exceeded, the following error is returned:

```sql
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

If the [metadata\_lock\_info](../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, the [Information Schema](../../system-tables/information-schema/) [metadata\_lock\_info](../../system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table stores information about existing metadata locks.

{% tabs %}
{% tab title="Current" %}
The [Performance Schema metadata\_locks](../../system-tables/performance-schema/performance-schema-tables/performance-schema-metadata_locks-table.md) table contains metadata lock information.

#### Example

Let's use the following MEMORY (non-transactional) table:

```sql
CREATE TABLE t (a INT) ENGINE = MEMORY;
```

Connection 1 starts a transaction, and INSERTs a row into t:

```sql
START TRANSACTION;

INSERT INTO t SET a=1;
```

`t`'s metadata is now locked by connection 1. Connection 2 tries to alter `t`, but has to wait:

```sql
ALTER TABLE t ADD COLUMN b INT;
```

Connection 2's prompt is blocked now.

Now connection 1 ends the transaction:

```sql
COMMIT;
```

...and connection 2 finally gets the output of its command:

```sql
Query OK, 1 row affected (35.23 sec)
Records: 1  Duplicates: 0  Warnings: 0
```
{% endtab %}

{% tab title="< 10.5.2" %}
The [Performance Schema metadata\_locks](../../system-tables/performance-schema/performance-schema-tables/performance-schema-metadata_locks-table.md) table does **not** contain metadata lock information.
{% endtab %}
{% endtabs %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
