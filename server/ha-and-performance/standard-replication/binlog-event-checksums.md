---
description: >-
  Configure checksums to detect data corruption in binary logs. Learn how to
  enable verification to ensure the integrity of replication events during
  transmission and storage.
---

# Binlog Event Checksums

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

MariaDB includes a feature to include a checksum in [binary log](../../server-management/server-monitoring-logs/binary-log/) events.

Checksums are enabled with the [binlog\_checksum option](replication-and-binary-log-system-variables.md), which is set to `CRC32` by default.

The variable can be changed dynamically without restarting the server. Setting the variable in any way (even to the existing value) forces a rotation of the [binary log](../../server-management/server-monitoring-logs/binary-log/) (the intention is to avoid having a single binlog where some events are checksummed and others are not).

When checksums are enabled, replicas will check events received over the network for checksum errors, and will stop with an error if a corrupt event is detected.

In addition, the server can be configured to verify checksums in two other places.

One is when reading events from the binlog on the primary, for example when sending events to a replica or for something like SHOW BINLOG EVENTS. This is controlled by the master\_verify\_checksum option, and is thus used to detect file system corruption of the binlog files.

The other is when the replica SQL thread reads events from the [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md). This is controlled by the slave\_sql\_verify\_checksum option, and is used to detect file system corruption of replica relay log files.

**MariaDB starting with** [**11.4**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

From [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114), binlog checksums are computed when writing events into the statement or transaction caches, where before this was done when the caches were copied to the real binlog file. This moves the checksum computation outside of holding LOCK\_log, improving scalability. See [MDEV-31273](https://jira.mariadb.org/browse/MDEV-31273).

`master_verify_checksum`

* Description: Verify binlog checksums when reading events from the binlog on the primary.
* Command line: `--master_verify_checksum=[0|1]`
* Scope: Global
* Access Type: Can be changed dynamically
* Data Type: `bool`
* Default Value: `OFF (0)`

`slave_sql_verify_checksum`

* Description: Verify binlog checksums when the replica SQL thread reads events from the relay log.
* Command line: `--slave_sql_verify_checksum=[0|1]`
* Scope: Global
* Access Type: Can be changed dynamically
* Data Type: `bool`
* Default Value: `ON (1)`

The [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) client program by default does not verify checksums when reading a binlog file, however it can be instructed to do so with the option `verify-binlog-checksum`:

* Variable Name: `verify-binlog-checksum`
* Data Type: `bool`
* Default Value: `OFF`

## See Also

* [Binlog Event Checksum Interoperability](binlog-event-checksum-interoperability.md)
* [What is MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
