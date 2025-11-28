# SET GLOBAL SQL\_SLAVE\_SKIP\_COUNTER

## Syntax

```sql
SET GLOBAL sql_slave_skip_counter = N
```

## Description

This statement skips the next `N` events from the primary. This is useful for recovering from [replication](../../../../ha-and-performance/standard-replication/) stops caused by a statement.

If multi-source replication is used, this statement applies to the default connection. It could be necessary to change the value of the [default\_master\_connection](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable.

Note that, if the event is a [transaction](../../transactions/), the whole transaction will be skipped. With non-transactional engines, an event is always a single statement.

This statement is valid only when the replica threads are not running. Otherwise, it produces an error.

The statement does not automatically restart the replica threads.

## Example

```sql
SHOW SLAVE STATUS \G
...
SET GLOBAL sql_slave_skip_counter = 1;
START SLAVE;
```

Multi-source replication:

```sql
SET @@default_master_connection = 'master_01';
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
START SLAVE;
```

## Multiple Replication Domains

`sql_slave_skip_counter` can't be used to skip transactions on a replica if [GTID replication](../../../../ha-and-performance/standard-replication/gtid.md) is in use and if [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) contains multiple [gtid\_domain\_id](../../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id) values. In that case, you'll get an error like the following:

```
ERROR 1966 (HY000): When using parallel replication and GTID with multiple 
 replication domains, @@sql_slave_skip_counter can not be used. Instead, 
 setting @@gtid_slave_pos explicitly can be  used to skip to after a given GTID 
 position.
```

In order to skip transactions in cases like this, you will have to manually change [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos).

## See Also

* [Selectively Skipping Replication of Binlog Events](../../../../ha-and-performance/standard-replication/selectively-skipping-replication-of-binlog-events.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
