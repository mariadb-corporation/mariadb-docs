---
description: >-
  Use GTID replication domains with multi-source replication and multi-primary rings, set up redundant replication paths, and delete unused domains.
---

# GTID with Multi-Source and Multi-Primary Replication

MariaDB global transaction ID supports having multiple primaries active at the same time. Typically this happens with either multi-source replication or multi-master ring setups.

In such setups, each active primary must be configured with its own distinct replication domain ID, [gtid\_domain\_id](gtid-system-variables.md#gtid_domain_id). The binlog will then in effect consists of multiple independent streams, one per active primary. Within one replication domain, binlog order is always the same on every server. But two different streams can be interleaved differently in different server binlogs.

The GTID position of a given replica is then not a single GTID. Rather, it becomes the GTID of the last event group applied for each value of domain ID, in effect the position reached in each binlog stream. When the replica connects to a primary, it can continue from one stream in a different binlog position than another stream. Since order within one stream is consistent across all servers, this is sufficient to always be able to continue replication at the correct point in any new primary server(s).

Domain IDs are assigned by the DBA, according to the need of the application. The default value of `@@GLOBAL.gtid_domain_id` is `0`. This is appropriate for most replication setups, where only a single primary is active at a time. The MariaDB server never by itself introduces new `domain_id` values to the binlog.

When using multi-source replication, where a single replica connects to multiple primaries at the same time, each such primary should be configured with its own distinct domain ID.

Similarly, in a multi-master ring topology, where all primary in the ring are updated by the application concurrently (with some mechanism to avoid conflicts), a distinct domain ID should be configured for each server (In a multi-master ring where the application is careful to only do updates on one primary at a time, a single domain ID is sufficient).

Normally, a replica server should not receive direct updates (as this creates binlog differences compared to the primary). Thus it does not matter what value of `gtid_domain_id` is set on a replica, though it may make sense to make it the same as the primary (if not using multi-master) to make it easy to promote the replica as a new primary. Of course, if a replica is itself an active primary, as in a multi-master ring topology, the domain ID should be set according to the server's role as active primary.

Note that domain ID and server ID are distinct concepts. It is possible to use a different domain ID on each server, but this is normally not desirable. It makes the current GTID position (`@@global.gtid_slave_pos`) more complicated to understand and work with, and loses the concept of a single ordered binlog stream across all servers. It is recommended only to configure as many domain IDs as there are primary servers actively being updated by the application at the same time.

It is not an error in itself to configure domain IDs incorrectly (for example, not configuring them at all). The ring continues to work as before even though everything is configured to use the default domain ID `0`. It is even possible to use GTID for replication between the servers. However, care must be taken when switching a replica to a different primary. If the binlog order between the old and the new primary differs, then a single GTID position to start replication from in the new primary's binlog may not be sufficient.

## Multiple Redundant Replication Paths

Using GTID with multi-source replication, it is possible to set up multiple redundant replication paths. For example:

```
M1 <-> M2
  M1 -> S1
  M1 -> S2
  M2 -> S1
  M2 -> S2
```

Here, M1 and M2 are setup in a master-master ring. S1 and S2 both replicate from each of M1 and M2. Each event generated on M1 will now arrive twice at S1, through the paths M1->S1 and M1->M2->S1. This way, if the network connection between M1 and S1 is broken, the replication can continue uninterrupted through the alternate path through M2. Note that this is an advanced setup, and good familiarity with MariaDB replication is recommended to successfully operate it.

The option [--gtid-ignore-duplicates](gtid-system-variables.md#gtid_ignore_duplicates) must be enabled to use multiple redundant replication paths. This is necessary to avoid each event being applied twice on the replica as it arrives through each path. The GTID of every event will be compared against the sequence number of the current GTID replica position (within each domain), and will be skipped if less than or equal. Thus it is required that sequence numbers are strictly increasing within each domain for [--gtid-ignore-duplicates](gtid-system-variables.md#gtid_ignore_duplicates) to function correctly, and setting [--gtid-strict-mode=1](gtid-system-variables.md#gtid_strict_mode) to help enforce this is recommended.

The --gtid-ignore-duplicates options also relaxes the requirement for connection to the primary. In the above example, when S1 connects to M2, it may connect at a GTID position from M1 that has not yet been applied on M2.

When --gtid-ignore-duplicates is enabled, the connection will be allowed, and S1 will start receiving events from M2 once the GTID has been replicated from M1 to M2. This can also be used to use replication filters in parts of a replication topology, to allow a replica to connect to a GTID position which was filtered on a primary. When --gtid-ignore-duplicates is enabled, the connecting replica will start receiving events from the primary at the first GTID sequence number that is larger than the connect-position.

## Deleting Unused Domains

[FLUSH BINARY LOGS DELETE\_DOMAIN\_ID=(list-of-domains)](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) can be used to discard obsolete GTID domains from the server's binary log state. In order for this to be successful, no event group from the listed GTID domains can be present in existing binary log files. If some still exist, then they must be purged prior to executing this command.

If the command completes successfully, then it also rotates the binary log.

The old domains will still appear in [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos). To get rid of these, you can stop the replica and execute `SET GLOBAL` on the replica, specifying only the list of active domains to be retained:

```sql
SET GLOBAL gtid_slave_pos="<position with the old or unused domains removed>";
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
