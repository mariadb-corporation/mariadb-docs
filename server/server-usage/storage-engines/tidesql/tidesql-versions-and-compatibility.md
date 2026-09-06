---
description: >-
  How TideSQL major versions map to the TidesDB library, and which MariaDB
  Server versions each TideSQL release is built against and tested with.
---

# TideSQL Versions and Compatibility

TideSQL is a storage engine plugin built on the TidesDB library, and it is compiled against a specific MariaDB Server. Three version lines therefore matter when you deploy it: the TideSQL plugin version, the TidesDB library version it links, and the MariaDB Server version it is built for.

## TideSQL Versions and the TidesDB Library

A TideSQL major version pairs with a single TidesDB library major version. A minor or patch release within a major line links a newer library release of the same major and extends the same manual, so only a new TideSQL major opens a new manual and moves to a new library major.

| TideSQL version | TidesDB library | Status |
|-----------------|-----------------|--------|
| 5.x | v10.x | Current |
| 4.x and earlier | v9.x | Archived |

This manual documents the TideSQL 5.x line, which links TidesDB v10. The current pinned release is 5.0.0, whose version is encoded as the hex value `0x50000`, and it links TidesDB v10.0.0. For the exact rules that relate the plugin version to the library version, see [Versioning](https://github.com/tidesdb/tidesql/blob/5.0.0/VERSIONING.md) for the 5.0.0 release.

## MariaDB Server Compatibility

Because TideSQL tracks the server's storage-engine interface, a given TideSQL release targets specific MariaDB Server versions. The table below records the versions that have been tested and confirmed working. Full support means the engine has been tested against all known functionality on that server version.

| MariaDB version | Minimum TideSQL version | Full support |
|-----------------|-------------------------|:------------:|
| 10.x.x | – | No |
| 11.4.10 | 3.4.0 | Yes |
| 11.8.6 | 4.0.0 | Yes |
| 12.2.2 | 1.0.0 | Yes |
| 12.3.1 | 4.2.6 | Yes |
| 13.0.2 | 4.5.4 | Yes |

The table is updated as new server versions are tested and confirmed working. MariaDB 10.x is not supported.

{% hint style="info" %}
TideSQL 5.0.0 targets the MariaDB 13 line. When the `install.sh` builder is run without a `--mariadb-version`, it builds against the latest MariaDB release, falling back to `mariadb-13.0.1`.
{% endhint %}

## Installation

TideSQL is a shared-object plugin that must be built against a matching MariaDB Server and TidesDB library. The repository ships an `install.sh` builder that clones MariaDB, builds it with the plugin against a matching library, and writes a ready-to-run configuration file. See [Getting Started with TideSQL](getting-started-with-tidesql.md) for the builder, its options, and how to load the plugin.

## Clustering

Beyond standalone and replicated servers, TideSQL participates in Galera clustering through the server's wsrep interface, with engine-level write-set certification and cross-node conflict resolution. See [TideSQL Replication and High Availability](tidesql-replication-and-ha.md) for what the engine does in a cluster.

<sub>_This page is licensed: GPLv2_</sub>
