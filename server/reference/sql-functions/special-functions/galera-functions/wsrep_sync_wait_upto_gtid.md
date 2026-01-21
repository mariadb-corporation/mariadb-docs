---
description: >-
  Wait for a specific GTID to be applied. This function blocks the client until
  the node has committed the transaction with the specified Global Transaction
  ID.
---

# WSREP\_SYNC\_WAIT\_UPTO\_GTID

## Syntax

```sql
WSREP_SYNC_WAIT_UPTO_GTID(gtid[,timeout])
```

## Description

Blocks the client until the transaction specified by the given [Global Transaction ID](../../../../ha-and-performance/standard-replication/gtid.md) is applied and committed by the node.

The optional _timeout_ argument can be used to specify a block timeout in seconds. If not provided, the timeout will be indefinite.

Returns the node that applied and committed the Global Transaction ID, `ER_LOCAL_WAIT_TIMEOUT` if the function is timed out before this, or `ER_WRONG_ARGUMENTS` if the function is given an invalid GTID.

The result from [WSREP\_LAST\_SEEN\_GTID](wsrep_last_seen_gtid.md) can be useful to determine the transaction to provide to `WSREP_SYNC_WAIT_UPTO_GTID` for waiting and unblocking purposes.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
