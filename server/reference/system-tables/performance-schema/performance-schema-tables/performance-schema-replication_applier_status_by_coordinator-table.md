---
description: >-
  This table shows the status of the coordinator thread when parallel
  replication is enabled, detailing the distribution of transactions to workers.
---

# Performance Schema replication\_applier\_status\_by\_coordinator Table

{% hint style="info" %}
The `replication_applier_status_by_coordinator` table is available from MariaDB 10.5.2.
{% endhint %}

The [Performance Schema](../) replication\_applier\_status\_by\_coordinator table displays the status of the coordinator thread used in multi-threaded replicas to manage multiple worker threads.

It contains the following fields.

| Column                    | Type                | Null | Description                                                                |
| ------------------------- | ------------------- | ---- | -------------------------------------------------------------------------- |
| CHANNEL\_NAME             | varchar(256)        | NO   | Replication channel name.                                                  |
| THREAD\_ID                | bigint(20) unsigned | YES  | The SQL/coordinator thread ID.                                             |
| SERVICE\_STATE            | enum('ON','OFF')    | NO   | ON (thread exists and is active or idle) or OFF (thread no longer exists). |
| LAST\_ERROR\_NUMBER       | int(11)             | NO   | Last error number that caused the SQL/coordinator thread to stop.          |
| LAST\_ERROR\_MESSAGE      | varchar(1024)       | NO   | Last error message that caused the SQL/coordinator thread to stop.         |
| LAST\_ERROR\_TIMESTAMP    | timestamp           | NO   | Timestamp that shows when the most recent SQL/coordinator error occured.   |
| LAST\_SEEN\_TRANSACTION   | char(57)            | NO   | The transaction the worker has last seen.                                  |
| LAST\_TRANS\_RETRY\_COUNT | int(11)             | NO   | Total number of retries attempted by last transaction.                     |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
