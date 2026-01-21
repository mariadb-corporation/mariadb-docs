---
description: >-
  The Information Schema WSREP_BF_ABORTS table provides statistics on Galera
  Cluster brute force aborts, detailing the victim and transaction IDs.
---

# Information Schema WSREP\_BF\_ABORTS

{% hint style="info" %}
This plugin is used in [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).
{% endhint %}

{% hint style="info" %}
This plugin is available as of MariaDB Enterprise Server 11.8.
{% endhint %}

This table contains execution state information for Galera threads. [The respective plugin](../../../plugins/mariadb-replication-cluster-plugins/wsrep_info-plugin.md) is not installed by default — you have to install it.

The table displays the history of BF[^1] aborts. It has these columns:

* TIME - Datetime when bf abort happened
* VICTIM\_TRX\_ID - Victim trx ID or NULL
* VICTIM\_THREAD\_ID - Victim thread
* THD ID VICTIM\_QUERY\_ID - Victim query id
* VICTIM\_SEQNO - Victim TO seqno associated with victim transaction
* VICTIM\_CLIENT\_STATE - Victim thread wsrep client state at the moment when BF abort attempt happened
* VICTIM\_CLIENT\_MODE - Victim thread wsrep client mode
* VICTIM\_TRX\_STATE - Victim thread wsrep transaction state at the moment when BF abort attempt happened
* VICTIM\_LOCK - Victim lock information
* BF\_TRX\_ID - BF thread transaction ID
* BF\_THREAD\_ID - BF thread THD ID
* BF\_QUERY\_ID - BF query id
* BF\_SEQNO - TO sequence number associated with BF transaction
* BF\_CLIENT\_STATE - BF thread wsrep client state
* BF\_CLIENT\_MODE - BF thread wsrep client mode
* BF\_TRX\_STATE - BF thread wsrep transaction state
* BF\_LOCK - Information about the lock which BF thread tried to acquire
* SPACE\_ID - Lock space\_id in case of record or table lock
* PAGE\_NO - Lock page\_no in case of record lock
* INDEX\_NAME - Record lock index name
* TABLE\_NAME - Lock table name

Example output:

```sql
SELECT * FROM INFORMATION_SCHEMA.WSREP_BF_ABORT_HISTORY LIMIT 100;   
+----------------------------+---------------+------------------+-----------------+--------------+---------------------+--------------------+------------------+----------------------------+-----------+--------------+-------------+----------+-----------------+----------------+--------------+----------------------------+----------+---------+------------+------------------+
| TIME                       | VICTIM_TRX_ID | VICTIM_THREAD_ID | VICTIM_QUERY_ID | VICTIM_SEQNO | VICTIM_CLIENT_STATE | VICTIM_CLIENT_MODE | VICTIM_TRX_STATE | VICTIM_LOCK                | BF_TRX_ID | BF_THREAD_ID | BF_QUERY_ID | BF_SEQNO | BF_CLIENT_STATE | BF_CLIENT_MODE | BF_TRX_STATE | BF_LOCK                    | SPACE_ID | PAGE_NO | INDEX_NAME | TABLE_NAME       |
+----------------------------+---------------+------------------+-----------------+--------------+---------------------+--------------------+------------------+----------------------------+-----------+--------------+-------------+----------+-----------------+----------------+--------------+----------------------------+----------+---------+------------+------------------+
| 2025-05-14 09:48:31.539207 |        378998 |               94 |         2365214 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379010 |            1 |     2365229 |   174271 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.597005 |        379044 |               81 |         2365344 |         NULL | exec                | local              | certifying       | REC|LOCK_X|NOT_GAP         |    379060 |            1 |     2365419 |   174284 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.609301 |        379055 |              104 |         2365412 |         NULL | exec                | local              | certifying       | REC|LOCK_X|NOT_GAP         |    379070 |            1 |     2365445 |   174289 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.725899 |        379134 |              101 |         2366437 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP         |    379164 |            1 |     2366536 |   174307 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |  147008 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789128 |        379094 |              131 |         2366355 |         NULL | exec                | local              | certifying       | REC|LOCK_X|NOT_GAP         |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789140 |        379101 |              124 |         2366103 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789145 |        379093 |               82 |         2366113 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789148 |        379110 |              117 |         2366193 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789152 |        379126 |              111 |         2366201 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789156 |        379100 |              134 |         2366318 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789159 |        379109 |               93 |         2366334 |         NULL | exec                | local              | executing        | REC|LOCK_X|NOT_GAP|WAITING |    379195 |            1 |     2366599 |   174323 | exec            | high priority  | executing    | REC|LOCK_X|NOT_GAP|WAITING |       12 |       4 | PRIMARY    | `test`.`sbtest1` |
| 2025-05-14 09:48:31.789163 |        379119 |               90 |         2366384 |         NULL | exec                | local              | executing       +----------------------------+---------------+------------------+-----------------+--------------+---------------------+--------------------+------------------+----------------------------+-----------+--------------+-------------+----------+-----------------+----------------+--------------+----------------------------+----------+---------+------------+------------------+
...
```

[^1]: Brute Force (BF) conflict resolution mechanism:

    * Transaction Conflicts: In a multi-master environment where multiple nodes can process transactions simultaneously, a conflict can occur if two transactions try to modify the same data at the same time.
    * Brute Force (BF) Abort: When a conflict is detected, one of the conflicting transactions (the "victim") may be "killed" or aborted to allow the other transaction (the "aggressor") to proceed and maintain data consistency across the cluster. This is referred to as a "Brute Force" approach to conflict resolution.
    * Information Schema Table: The "Information schema table displaying history of BF aborts" is a system table (like `wsrep_local_bf_aborts` in Galera Cluster) that tracks the count or history of these brute force transaction terminations. This is a crucial metric for monitoring cluster health and identifying problematic transactions or high-contention ar
