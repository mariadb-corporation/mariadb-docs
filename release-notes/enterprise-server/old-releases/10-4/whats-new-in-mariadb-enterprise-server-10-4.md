# What's New in MariaDB Enterprise Server 10.4?

MariaDB Enterprise Server 10.4 introduces the following new features:

## Enterprise Lifecycle

MariaDB Enterprise Server uses an [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle) that provides optimized builds, predictable release behavior, and vendor support.

## InnoDB Instant ALTER

[Instant ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm) enables reliable and predictable schema change behavior.

## Optimizer Trace

[Optimizer Trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans) collects trace data to aid query optimization and diagnosis of query execution issues.

## Temporal Data

[Temporal data table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables) support has been expanded from system-versioned tables to also include application-time period and bitemporal tables.

## Enterprise Audit Plugin

[MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit) provides support for auditing resource access to MariaDB Enterprise Server.

## Enterprise Backup

[MariaDB Enterprise Backup](../../10-4/broken-reference/) enables non-blocking backups of MariaDB Enterprise Server.

## Data-at-Rest Encryption

With [data-at-rest encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security), data is encrypted before writing to the disk and decrypted when read from disk. MariaDB Enterprise Server extends data-at-rest encryption support to include:

* Encryption of Spatial indexes
* Key rotation when encrypting the InnoDB Redo Log
* Encryption of MariaDB Enterprise Cluster's write-set cache (GCache)

## MariaDB Enterprise Cluster

MariaDB Enterprise Server includes support for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md), which incorporates Galera Cluster 4. New features include:

* Parallel replication and improved performance when blocks of grouped transactions can be committed without conflict.
* The [Streaming replication](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md), to eliminate transaction limitations by fragmenting huge transactions for replication.
* Rolling upgrades to permit a smooth transition of MariaDB Cluster deployments to Galera 4 functionality by operating as a Galera 3-compatible node until all nodes are Galera 4-compatible.

## Data Reliability and SQL Functionality

MariaDB Enterprise Server includes changes to improve data reliability and SQL functionality:

* System tables use the Aria storage engine, making them crash-safe.
* UNIQUE index support for the BLOB data type.
* [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) data type validation.
* Parentheses in UNION, INTERSECT, and EXCEPT operations to control order of execution.

## Enhanced Credential Management

MariaDB Enterprise Server features [security](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security) improvements, including:

* Ability to reload SSL certificates without server restart.
* SET PASSWORD option to specify authentication plugins.
* Improved support for authentication plugins, including the ability to set multiple authentication plugins on individual users. Also supported is fallback on internal methods, such as password authentication.
* ALTER USER option for account locking, to enable MariaDB Enterprise Server to reject all new connections for an account.
* Account blocking based on number of failed login attempts.
* Ability to set password expiration dates.
* Logging of access when passwords are ignored, e.g., for passwordless authentication by UNIX socket.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
