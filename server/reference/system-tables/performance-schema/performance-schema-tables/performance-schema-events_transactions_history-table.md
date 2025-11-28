---
description: >-
  This table records the ten most recent completed stage events per thread,
  useful for analyzing recent thread activity.
---

# Performance Schema events\_transactions\_history Table

{% hint style="info" %}
The `events_transactions_history` table is available from MariaDB 10.5.2.
{% endhint %}

The `events_transactions_history` table contains the most recent completed transaction events for each thread.

The number of records stored per thread in the table is determined by the [performance\_schema\_events\_transactions\_history\_size](../performance-schema-system-variables.md#performance_schema_events_transactions_history_size) system variable, which is autosized on startup.

If adding a completed transaction event would cause the table to exceed this limit, the oldest thread row is discarded.

All of a thread's rows are discarded when the thread ends.

The table contains the following columns:

| Column                              | Type                                              | Description                                                                                                                                                                               |
| ----------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| THREAD\_ID                          | bigint(20) unsigned                               | The thread associated with the event.                                                                                                                                                     |
| EVENT\_ID                           | bigint(20) unsigned                               | The event id associated with the event.                                                                                                                                                   |
| END\_EVENT\_ID                      | bigint(20) unsigned                               | This column is set to NULL when the event starts and updated to the thread current event number when the event ends.                                                                      |
| EVENT\_NAME                         | varchar(128)                                      | The name of the instrument from which the event was collected. This is a NAME value from the setup\_instruments table.                                                                    |
| STATE                               | enum('ACTIVE', 'COMMITTED',' ROLLED BACK')        | The current transaction state. The value is ACTIVE (after START TRANSACTION or BEGIN), COMMITTED (after COMMIT), or ROLLED BACK (after ROLLBACK).                                         |
| TRX\_ID                             | bigint(20) unsigned                               | Unused.                                                                                                                                                                                   |
| GTID                                | varchar(64)                                       | Transaction [GTID](../../../../ha-and-performance/standard-replication/gtid.md), using the format DOMAIN-SERVER\_ID-SEQUENCE\_NO.                                                         |
| XID\_FORMAT\_ID                     | int(11)                                           | XA transaction format ID for GTRID and BQUAL values.                                                                                                                                      |
| XID\_GTRID                          | varchar(130)                                      | XA global transaction ID.                                                                                                                                                                 |
| XID\_BQUAL                          | varchar(130)                                      | XA transaction branch qualifier.                                                                                                                                                          |
| XA\_STATE                           | varchar(64)                                       | The state of the XA transaction. The value is ACTIVE (after XA START), IDLE (after XA END), PREPARED (after XA PREPARE), ROLLED BACK (after XA ROLLBACK), or COMMITTED (after XA COMMIT). |
| SOURCE                              | varchar(64)                                       | The name of the source file containing the instrumented code that produced the event and the line number in the file at which the instrumentation occurs.                                 |
| TIMER\_START                        | bigint(20) unsigned                               | The unit is picoseconds. When event timing started. NULL if event has no timing information.                                                                                              |
| TIMER\_END                          | bigint(20) unsigned                               | The unit is picoseconds. When event timing ended. NULL if event has no timing information.                                                                                                |
| TIMER\_WAIT                         | bigint(20) unsigned                               | The unit is picoseconds. Event duration. NULL if event has not timing information.                                                                                                        |
| ACCESS\_MODE                        | enum('READ ONLY', 'READ WRITE')                   | Transaction access mode.                                                                                                                                                                  |
| ISOLATION\_LEVEL                    | varchar(64)                                       | Transaction isolation level. One of: REPEATABLE READ, READ COMMITTED, READ UNCOMMITTED, or SERIALIZABLE.                                                                                  |
| AUTOCOMMIT                          | enum('YES', 'NO')                                 | NO                                                                                                                                                                                        |
| NUMBER\_OF\_SAVEPOINTS              | bigint(20) unsigned                               | The number of SAVEPOINT statements issued during the transaction.                                                                                                                         |
| NUMBER\_OF\_ROLLBACK\_TO\_SAVEPOINT | bigint(20) unsigned                               | The number of ROLLBACK\_TO\_SAVEPOINT statements issued during the transaction.                                                                                                           |
| NUMBER\_OF\_RELEASE\_SAVEPOINT      | bigint(20) unsigned                               | The number of RELEASE\_SAVEPOINT statements issued during the transaction.                                                                                                                |
| OBJECT\_INSTANCE\_BEGIN             | bigint(20) unsigned                               | Unused.                                                                                                                                                                                   |
| NESTING\_EVENT\_ID                  | bigint(20) unsigned                               | The EVENT\_ID value of the event within which this event is nested.                                                                                                                       |
| NESTING\_EVENT\_TYPE                | enum('TRANSACTION',' STATEMENT', 'STAGE', 'WAIT') | The nesting event type.                                                                                                                                                                   |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
