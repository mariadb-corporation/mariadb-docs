---
description: >-
  How TideSQL participates in MariaDB replication and in a Galera cluster,
  including write-set certification and cross-node conflict resolution.
---

# TideSQL Replication and High Availability

TideSQL stores data on one node. Replication and clustering come from the layers above the engine, and within those layers TideSQL is a first-class participant rather than a generic pass-through. It carries the binlog capabilities MariaDB replication needs, it commits through the two-phase protocol that keeps a replica crash-safe, and it participates directly in Galera certification, including the cross-node conflict resolution that keeps a multi-master cluster from diverging.

## MariaDB Replication

A TideSQL table replicates like any other. The engine is both row and statement binlog capable, so `binlog_format` of `ROW`, `STATEMENT`, or `MIXED` all work, with row-based replication the natural fit for an optimistic engine because it ships the resulting row images rather than re-running a statement whose outcome depends on commit ordering.

Commits go through the binlog two-phase protocol. The engine prepares durably before the binlog writes, and it commits in binlog order through the group-commit hook, so a crash between the binlog and the engine recovers to a consistent point and a replica built from that binlog is consistent with the primary. The prepare phase runs the same conflict checks as a commit, so with the binlog enabled, a write-write conflict is reported when the transaction prepares. Commit behavior is covered in [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

Nothing engine-specific has to be enabled. A table created with `ENGINE=TIDESDB` on the primary replicates to a replica running the same engine through the standard replication configuration.

## Galera Cluster

TideSQL advertises the Galera replication capability, so a table created with `ENGINE=TIDESDB` in a wsrep-enabled server is replicated to every node in the cluster and certified in the global order the provider assigns. The engine does three things for the cluster.

It appends a certification key for every row a transaction changes, built from the primary key and from each unique index, so a write to the same row or the same unique value on another node is caught as a conflict rather than silently diverging the replicas. A key with a `NULL` part constrains nothing and is skipped. A table with no unique key certifies each of its ordinary indexes instead, and a table with no certifiable key at all appends a table-level exclusive key, which serializes its writes across the cluster. When an update changes a key, the keys of both the before and the after image are appended, so the row's old identity stays covered. Inserts, updates, and deletes append their keys as exclusive keys.

It resolves a cross-node write-write conflict the way InnoDB does, without a pessimistic lock. When an applier replays a cluster write that collides with a local uncommitted transaction, the engine brute-force aborts that local transaction through the server before it certifies, so the losing side rolls back cleanly instead of committing a write the other nodes cannot apply. A lock-free store parks no row lock for the applier to block on, so the engine keeps a small write-intent record for each uncommitted write, keyed by the row's primary key and by each non-`NULL` unique value it writes, and uses it to find and abort the local loser. An aborted transaction fails its next operation, its commit included, and the application on the losing side sees a deadlock error and retries, the same outcome InnoDB produces for the same race.

It persists the cluster position in a dedicated internal column family, `__tidesdb_wsrep_meta`, so a node that restarts or rejoins knows where it left off and the provider can bring it back through state transfer.

## What an Application Sees Under Conflict

On a single node, an optimistic write-write conflict surfaces at `COMMIT` as error 1180 wrapping handler error 149 (deadlock), or mid-statement as a deadlock (1213), and the application retries, described in [TideSQL Limitations](tidesql-limitations.md). Across a cluster the losing transaction of a cross-node conflict is aborted and reaches the client as a deadlock, which an application should handle by retrying the transaction. Autocommit statements are retried by the server automatically, up to `wsrep_retry_autocommit` times. The winner's row stands identically on every node, so the replicas stay converged.

<sub>_This page is licensed: GPLv2_</sub>
