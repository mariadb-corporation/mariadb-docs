---
description: >-
  Return the GTID of the most recent write transaction. This function helps
  determine the transaction ID to use for synchronization waiting.
---

# WSREP\_LAST\_SEEN\_GTID

## Syntax

```sql
WSREP_LAST_SEEN_GTID()
```

## Description

Returns the [Global Transaction ID](../../../../ha-and-performance/standard-replication/gtid.md) of the most recent write transaction observed by the client.

The result can be useful to determine the transaction to provide to [WSREP\_SYNC\_WAIT\_UPTO\_GTID](wsrep_sync_wait_upto_gtid.md) for waiting and unblocking purposes.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
