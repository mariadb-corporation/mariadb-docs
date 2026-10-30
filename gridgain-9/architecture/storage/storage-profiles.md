---
description: >-
  How GridGain 9 storage profiles bind a storage engine and its configuration to
  distribution zones and tables, including primary and secondary profiles.
---

# Storage Profiles

## What is a Storage Profile?

Storage profiles are GridGain node entities that define a Storage Engine and its configuration parameters. They create a bridge between tables and the underlying storage engines that store data.

A storage profile defines:

- What storage engine is used to store data
- Configuration values for a particular Storage Engine's configuration properties

Each node in a GridGain cluster can have multiple storage profiles defined, and a table can only have a single storage profile defined.

## Storage Profiles and Distribution Zones

A Distribution Zone must be configured to use a set of declared Storage Profiles, which can be used to parameterize tables created in this Zone with different Storage Engines. When creating a distribution zone, you specify which storage profiles it can use:

```sql
CREATE ZONE exampleZone (PARTITIONS 2, REPLICAS 3) STORAGE PROFILES ['profile1, profile3'];
```

In this case, the tables created in this distribution zone can only use `profile1` or `profile3`.

## Default Storage Profile

GridGain creates a `default` storage profile that uses the persistent Apache Ignite storage engine (`aipersist`) to store data. Unless otherwise specified, distribution zones will use this storage profile to store data.

To check the currently available profiles on the node, use the following command:

```bash
node config show ignite.storage.profiles
```

## Creating and Using Storage Profiles

By default, only the `default` storage profile is created, however a node can have any number of storage profiles on it. To create a new profile, pass the profile configuration to the `storage.profiles` parameter:

```bash
node config update "ignite.storage.profiles:{rocksProfile{engine:rocksdb,size:10000}}"
```

After the configuration is updated, make sure to restart the node. The created storage profile will be available for use by a distribution zone after the restart.

## Defining Tables With Storage Profiles

After you have defined your storage profiles and distribution zones, you can create tables in it by using SQL or from code. Both zone and storage profile cannot be changed after the table has been created.

For example, here is how you create a simple table:

```sql
CREATE TABLE exampleTable (key INT PRIMARY KEY, my_value VARCHAR) ZONE exampleZone STORAGE PROFILE 'profile1';
```

In this case, the `exampleTable` table will be using the storage engine with the parameters specified in the `profile1` storage profile. If the node does not have the `profile1`, the table will not be stored on it. Each node may have different configuration for `profile1`, and data will be stored according to local configuration.

## Secondary Storage Profiles

In some scenarios, it is preferable to have a separate storage for "cold" data, while the primary storage profile handles active users. Data in secondary storage profiles is always stored in columnar format optimized analytics workloads and can only be read. Updates to primary storage are automatically also applied to secondary storage.

You can create a secondary storage profile in a way similar to primary storage profiles:

```bash
node config update "ignite.storage.profiles:{columnar_storage{engine:columnar}}"
```

To define a secondary storage profile in your table, you need to make sure it is part of the distribution zone, and then specify it as a `SECONDARY STORAGE PROFILE`. This can only be done when the table is created, for example:

```sql
CREATE TABLE exampleTable (key INT PRIMARY KEY, my_value VARCHAR) PRIMARY ZONE exampleZone PRIMARY STORAGE PROFILE 'profile1' SECONDARY ZONE exampleZone SECONDARY STORAGE PROFILE 'columnar_storage';
```

{% hint style="info" %}
Data from secondary storage profiles can only be read by specifying the `use_secondary_storage` hint.
{% endhint %}

```sql
SELECT /*+ use_secondary_storage */ * FROM exampleTable;
```

You can also mix data from primary and secondary storage in a single query:

```sql
SELECT * FROM Person JOIN Company /*+ use_secondary_storage */ Companies 
ON Person.id = Companies.companyName;
```

You can also specify a separate distribution zone for the secondary storage, in which case secondary storage data will be placed according to the configuration for secondary zone:

```sql
CREATE TABLE exampleTable (key INT PRIMARY KEY, my_value VARCHAR) PRIMARY ZONE exampleZone PRIMARY STORAGE PROFILE 'profile1' SECONDARY ZONE columnarZone SECONDARY STORAGE PROFILE 'columnar_storage';
```
