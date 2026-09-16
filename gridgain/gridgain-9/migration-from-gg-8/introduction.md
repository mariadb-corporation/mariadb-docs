---
description: >-
  What can and cannot be migrated when moving a cluster from GridGain 8 to
  GridGain 9, and where to start.
---

# Migration From GridGain 8

This section guides you through the process of migrating a cluster from GridGain 8 to 9.

## Migration Limitations

Not everything from GridGain 8 can be directly migrated to GridGain 9. As a general guideline, basic features of GridGain 8 can be migrated directly, while anything written by you or using advanced features will need to be manually recreated in GridGain 9.

The migration tools will be continuously improved, removing some of these limitations in later GridGain 9 releases.

The following can be migrated:

- Basic cluster and node configuration;
- Persistent data stored on GridGain 8 cluster;
- Simple clients that use cache and transaction interfaces;
- Distributed computing code.

The following will need to be recreated on a GridGain 9 cluster:

- Advanced cluster and node configuration;
- Complicated code that uses features without direct equivalents in GridGain 9;
- Data stored in memory;
- SQL queries.

The following pages help you with migrating your cluster to GridGain 9:

- [Configuration Migration](config.md)
- [Migrate persistent data](persistent-migration.md)
- [Data Center Replication Between GridGain 8 and GridGain 9](dcr-from-gg8.md)
- [Migrate codebase](codebase-migration.md)
