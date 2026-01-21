---
description: >-
  The Information Schema WSREP_THD_STATE table displays the internal state of
  Galera threads, helping to monitor replication progress and locking.
---

# Information Schema WSREP\_THD\_STATE

{% hint style="info" %}
This table is used in [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).
{% endhint %}

{% hint style="info" %}
This table is available as of MariaDB Enterprise Server 11.8.
{% endhint %}

This table contains execution state information for Galera threads, and has these columns:

* ID - Thread ID
* OS\_THREAD\_ID - Os thread ID
* CLIENT\_MODE - Client mode (local, high priority, toi...)
* CLIENT\_STATE - Wsrep query state (idle, exec, result...)
* TRANSACTION\_STATE - Wsrep transaction state or "none" if no active transaction
* SEQNO - Commit order seqno if assigned, otherwise -1
* DEPENDS\_ON - Depends on seqno if assigned, otherwise -1\
  The table must have low overhead (populated only when queried) and must be enabled at all times (not plugin or plugin must be loaded by default).
* GTID - transaction GTID assigned during commit phase

Example output:

```sql
SELECT * FROM information_schema.wsrep_thd_info;
ID	OS_THREAD_ID	MODE	STATE	TRANSACTION_ID	TRANSACTION_STATE	SEQNO	DEPENDS_ON	GTID
14	128875466565312	local	exec	64	executing	NULL	NULL	NULL
13	128875466872512	local	exec	61	committing	9	3	0-1-7
12	128875467179712	local	idle	NULL	aborted	NULL	NULL	NULL
2	128875634570944	high priority	exec	NULL	executing	NULL	NULL	NULL
1	128875634878144	local	none	NULL	executing	NULL	NULL	NULL
```

There is also an `INFORMATION_SCHEMA.WSREP_THD_STATE_HISTORY` table that contains the history of execution state information for Galera threads.
