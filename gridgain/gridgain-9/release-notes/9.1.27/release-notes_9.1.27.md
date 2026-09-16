---
description: >-
  GridGain 9.1.27 restricts server-side file access for the SQL COPY command,
  adds SQL execution over the management REST API, changes the default
  transaction deadlock prevention policy, and hardens role and credential
  handling.
---

# GridGain 9.1.27 Release Notes

## Overview

GridGain 9.1.27 restricts server-side file access for the SQL `COPY` command, adds SQL execution over the management REST API, changes the default transaction deadlock prevention policy, and hardens role and credential handling.

## Major Changes

### Server-Side File Access for COPY Disabled by Default

The `COPY` command previously authorized only the table side of a statement. A filesystem path or object-store URI named as a `COPY` source or target required no privilege of its own, so any user who could write to one table could read or write arbitrary files on the server.

Server-side file and object-store access is now disabled entirely by default. To re-enable it:

- Set `importExport.fileAccessEnabled` to `true` in the [node configuration](../../administrators-guide/config/node-config.md).
- List the directories `COPY` command may read from and write to in `importExport.importRoots`. An empty list allows no local file access.
- Grant `COPY_FROM_FILE` privilege to read a server-side location, or `COPY_TO_FILE` to write one.

Object-store and Iceberg locations are governed by their own allow-lists, all of which default to empty and therefore deny access: `importExport.allowedS3Buckets`, `importExport.allowedS3Endpoints`, `importExport.allowedIcebergClasses`, and `importExport.allowedCatalogUris`.

{% hint style="warning" %}
An existing `COPY` job that names a filesystem path or object-store URI fails after the upgrade until you complete the steps above. A `COPY` between tables is unaffected. The failure message names what is missing: `Server-side file/object-store COPY is disabled on this node. Set importExport.fileAccessEnabled=true and configure importExport.importRoots, then grant COPY_FROM_FILE / COPY_TO_FILE.`
{% endhint %}

### Wound-Wait Deadlock Prevention by Default

Read-write transactions now use the wound-wait deadlock prevention algorithm instead of wait-die.

Under wait-die, a transaction that requested a lock held by an older transaction was cancelled and retried. Under wound-wait the priority runs the other way: an older transaction that needs a lock held by a younger one aborts the younger transaction and proceeds, while a younger transaction that meets an older holder waits for the lock to be released.

No configuration change is required. Applications that relied on the previous behavior may see different abort patterns under contention. See [Deadlock Prevention](../../developers-guide/transactions.md#deadlock-prevention).

### Built-In Roles Can No Longer Be Assigned, Revoked, or Dropped

The built-in `system` super role is now protected. Assigning it to a user, revoking it from a user, and dropping it are now blocked.

### Deprecations

The following features are deprecated:

| Deprecated | Replacement |
|---|---|
| `RANDOM_LRU` and `SEGMENTED_LRU` page replacement modes | Use `CLOCK`, which is already the default for `profiles.aipersist.replacementMode`. |
| The doubly-nested `ignite.nodeAttributes.nodeAttributes` configuration section | Use the flat `ignite.userAttributes` section. Values in the deprecated section are still read and are moved to the new location on every configuration change, so the deprecated section disappears from the stored configuration after the next write. If the same attribute name is set in both, the value in `ignite.userAttributes` is kept. |

## New Features

### SQL Execution Over the Management REST API

You can now run SQL statements over the management REST API. `POST /management/v1/sql/execute` runs a single statement and returns the first page of results, `POST /management/v1/sql/script` runs a semicolon-separated script, and `GET` and `DELETE` on `/management/v1/sql/cursors/{cursorId}` page through and close a result.

One response shape covers every kind of statement, reporting a row set, an affected-row count, or whether a conditional statement was applied. Values whose full range a JSON number cannot carry — `DECIMAL`, `INT64`, temporal types, `UUID`, and `BYTE_ARRAY` — travel as strings, and column metadata accompanies every page so a client can restore each value exactly.

A `cursorId` is valid only on the node that issued it, so paging requests must go to that same node.

See [Running SQL](../../developers-guide/rest/rest-api.md#running-sql).

### Connect Timeout for the C++ Client

The C++ client can now limit how long it waits for the handshake that follows a new connection to a server node. Set it with `set_connect_timeout`; a connection whose handshake does not complete in time is closed, so the client can re-connect instead of holding a socket that never becomes usable. There is no timeout by default. See [Connect Timeout](../../developers-guide/clients/cpp.md#connect-timeout).

### Low Watermark Progress Metrics

A new `low.watermark` metric source reports whether the low watermark is still advancing and what is holding it back: `Current`, `SinceLastUpdateMillis`, `BlockingLockCount`, and `BlockingLockLagMillis`. See [Available Metrics](../../administrators-guide/metrics/metrics-list.md).

### Table Schema Version in SYSTEM.TABLES

The `SYSTEM.TABLES` system view now has a `TABLE_SCHEMA_VERSION` column reporting the table's latest schema version, which increases every time the table's schema changes.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-51219 | Cluster Storage Engine | RANDOM_LRU and SEGMENTED_LRU page replacement policies are now deprecated. |
| GG-51103 | Cluster Storage Engine | Increased the page memory segment count and bounded segment size over-allocation. |
| GG-51034 | Cluster Storage Engine | The resource vacuum and the finished read-only broadcast now keep running after a failure. |
| GG-50978 | Cluster SQL Engine | Fix exception in MERGE INTO query with dynamic parameters when assertions enabled |
| GG-50916 | Cluster Data Replication | The DR connector `start.sh` now inherits `EXTRA_JVM_ARGS` from the environment, so JVM arguments no longer require editing the script after each upgrade. |
| GG-50904 | Cluster Data Snapshots and Recovery | Primary replicas are now awaited in assignments before point-in-time recovery. |
| GG-50893 | General | Added the node's build commit to `GET /management/v1/node/version` and to the CLI `node version` output. |
| GG-50739 | Cluster Security | A configuration update that sets an LDAP `bindDn` while leaving `bindCredentials` empty is now rejected, because a simple bind with an empty password leaves the search connection anonymous. |
| GG-50731 | CLI Tool | Fixed CLI options ignoring double quotes around a zone or table name. |
| GG-50690 | Cluster SQL Engine | Added the `TABLE_SCHEMA_VERSION` column to the `SYSTEM.TABLES` system view. |
| GG-50602 | Platforms & Clients | BigDecimal set to TRUNCATE on Java clients |
| GG-50600 | Cluster Storage Engine | Fixed an update command applied after a primary replica change killing all partition replicas or silently losing a committed write. |
| GG-50592 | General | Added `POST /management/v1/sql/script` to run a SQL script over the management REST API. |
| GG-50591 | General | Added cursor paging for SQL results over the management REST API. |
| GG-50590 | General | Added `POST /management/v1/sql/execute` to run a SQL statement over the management REST API. |
| GG-50589 | General | Defined the value encoding contract for SQL over the management REST API. |
| GG-50575 | Platforms & Clients | C++: Fixed correctness issues in `ignite::big_decimal`. |
| GG-50548 | Migration Tools | The migration tools adapter now implements `destroyCaches` and `destroyCachesAsync`. |
| GG-50523 | General | Fixed too early cleanup of transaction state during write intent resolution. In rare failover cases this could lead to data loss for a committed transaction. |
| GG-50522 | General | Wait Die deadlock policy is now changed to Wound Wait by default |
| GG-50512 | Platforms & Clients | Fix bug in security handlers for JDBC metadata |
| GG-50511 | Cluster Security | RLS policy DDL (CREATE/ALTER/DROP POLICY) now requires MANAGE_RLS on the table the policy protects, not on a table matching the policy name. Grants made against policy names must be re-issued on the protected tables after upgrade. |
| GG-50509 | Cluster Security | Dropping the built-in `system` super role is refused in any letter case. |
| GG-50493 | General | Fixed a permanent PrimaryReplicaMissException on writes after a Metastorage leadership failover, caused by an outdated lease being published over a newer one. |
| GG-50485 | Cluster Continuous Queries | .NET: Continuous Query: fixed event loss on table drop. |
| GG-50388 | Platforms & Clients | Fixed: A malformed client message could use up all of a node's memory. |
| GG-50379 | Cluster Security | Built-in roles (system, gridgain-system-bypass) can no longer be granted or revoked via SQL, REST or the Java API, in any letter case. Appointing or removing a cluster administrator now requires a security configuration update. |
| GG-50378 | Cluster Security | `CREATE USER` and `ALTER USER` password literals are now masked in the `SYSTEM.SQL_QUERIES` view and in query event records. The event error field is suppressed for such statements so it cannot republish the password. |
| GG-50361 | General | ignite.nodeAttributes.nodeAttributes.<name> is deprecated in favor of the new flat ignite.userAttributes.<name>, with existing configs migrated automatically. |
| GG-50359 | Cluster Storage Engine | Fixed calculation of partition state health |
| GG-50245 | Cluster Data Snapshots and Recovery | Primary replicas are now awaited in assignments during snapshot restore. |
| GG-50158 | Cluster Security | Hardened machine learning marshaller deserialization with a strict object input filter. |
| GG-50012 | General | Now under high partition operation pressure all cleanup related tasks with lock release included will be handled in parallel without interfering |
| GG-50009 | General | Now table estimated size won't be waiting for aborted transactions' cleanup finish |
| GG-49877 | Platforms & Clients | .NET: Fixed SchemaVersionMismatch handling in data streamer with retried batches. |
| GG-49876 | Platforms & Clients | .NET: Fixed DataStreamer missing in-flight FailedItems on error. |
| GG-49875 | Platforms & Clients | .NET: Fixed race condition in data streamer on auto flush. |
| GG-49727 | Cluster Security | An empty or blank LDAP username is now rejected. |
| GG-49677 | Cluster Storage Engine | Per-partition storage creation is now parallelized on table creation instead of running sequentially on one thread. |
| GG-49648 | Cluster Data Replication | Discard in-flight batches when connection with sender is closed |
| GG-49625 | Cluster Security | Data center replication request secrets are now masked. |
| GG-49607 | Cluster Security | Server-side file and object-store locations used by `COPY` now require the new `COPY_FROM_FILE` or `COPY_TO_FILE` action and must fall within a configured allow-list. File access is disabled by default. |
| GG-49590 | Platforms & Clients | C++: Added client connect timeout. |
| GG-49350 | Cluster SQL Engine | Added a dedicated termination program that also closes the cursor. |
| GG-49138 | General | Lock acquisition failures on already-finished transactions are now retriable: the new public TransactionFinishedException carries the RetriableTransactionException marker |
| GG-48984 | General | Introduced metrics for LWM progress |
| GG-48884 | General | The final transaction state is now respected on the disconnect path. |
| GG-48626 | Cluster SQL Engine | Fixed an AssertionError thrown when planning a comparison of a CHAR value with a VARCHAR column. |
| GG-47861 | Cluster SQL Engine | Improve constant predicates push-down for outer joins |
| GG-47643 | Cluster Storage Engine | Fixed partition modification increments on transaction commit. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`, `9.1.25`, `9.1.26`

When updating from older versions, we recommend updating to version `9.1.21` first, before performing an update to current version.

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
