---
description: >-
  Convert GridGain 8 caches to GridGain 9 tables, either by replicating caches
  or by migrating persistent storage files directly with the migration tool.
---

# Persistent Data Migration

GridGain 9 persistent data storage is not directly compatible with GridGain 8. You need to convert your GridGain 8 caches to GridGain 9 tables. GridGain migration tool can be used to convert most GG8 caches.

There are two options for creating the required GridGain 9 configuration:

- [Replicating Caches to GridGain 9](#replicating-caches-to-gridgain-9)
- [Migrating Persistent Data](#migrating-persistent-data)

Regardless of the approach you choose, you need to download the migration tools first:

1. Download the migration tools from the [website](https://www.gridgain.com/tryfree).
2. Unpack the downloaded archive to your machine.
3. To explore the available commands in help, run the following command from the migration tools directory:

   ```bash
   bin/migration-tools --help
   ```

   or

   ```bash
   bin/migration-tools {command} --help
   ```

   Substitute `{command}` with the actual command name.

## Replicating Caches to GridGain 9

The GridGain migration tool can analyze GridGain 8 configuration (including XML configuration) and create DDL requests required to reproduce the caches. These caches will be empty, and you can then use the [data center replication between GridGain 8 and GridGain 9](dcr-from-gridgain-8.md) to transfer data between your clusters.

This approach allows migrating data and load to GridGain 9 cluster without downtime, as GridGain 9 cluster will receive data from your cluster and can seamlessly take on the load afterwards.

### Export DDL Script

To create the DDL script, use the following command:

```bash
bin/migration-tools sql-ddl-generator [-o={file}] [--allow-extra-fields] [--stop-on-error] [--extra-lib={jar}] gridgain-config.xml
```

Where:

- `-o` - saves the script to a file (e.g., `-o=gg9-script.sql`). By default, the script is printed to the console.
- `--allow-extra-fields` - if specified, any columns or fields of unsupported types will be saved to an `__EXTRA__` column as JSON data.
- `--stop-on-error` - if specified, the command stops when it encounters an error when attempting to produce the DDL for a cache. By default,, the command logs errors and continues.
- `--extra-lib` - if specified, adds the classes from the provided JAR file to CLI tool classpath. These classes, which that may be referenced in any cache configuration, can be used to ensure optimal results and avoid errors and warning messages. Use this parameter for each JAR you want to add. You can specify this parameter multiple times to provide multiple JARs.

### Create GridGain 9 Tables

Then, execute the script from the [GridGain 9 CLI tool](../../reference/cli-tool.md):

```bash
sql --file=gg9-script.sql
```

When executed, the script will create all required schemas and tables with the same configuration specified in GridGain 8.

## Migrating Persistent Data

An alternative to configuring the tables and migrating data from GridGain 8 via SQL script is to migrate data directly from the persistent storage files. When done this way, all data stored on the node will be converted to GridGain 9 tables and will be accessible once the cluster is started. As this approach converts stored data directly, schemas will be preserved from GridGain 8.

This approach requires downtime, but does not involve using data center replication.

To convert your persistent storage to GridGain 9:

- Safely stop the GridGain 8 node you intend to migrate data from.

  {% hint style="info" %}
  Let the node complete a checkpoint after stopping the clients to make sure that all the data is properly saved in persistent storage.
  {% endhint %}
- Start the GridGain 9 cluster.
- Run the command to list available caches on the node:

  ```bash
  bin/migration-tools persistent-data work-dir consistent-id config-file list-caches [--mode] [--rate-limiter] [--client.basicAuthenticator.username]
  ```

  Where:

  - `work-dir` - the GridGain 8 node's work directory. By default, it is the `{GRIDGAIN_HOME}/work` folder.
  - `consistent-id` - the GridGain 8 node's unique node identifier.
  - `config-file` - GridGain 8 configuration file. This file will be used to determine table parameters in GridGain 9.
  - `cacheName` - the name of the specific cache to migrate.
  - `gg9urls` - the list of URLs that the migration tool will use to connect to the GridGain 9 cluster.
  - `--mode` - the migration mode, which defines what to do in case of an irreconcilable mismatch between the object stored in the cache and the GridGain 9 table:
    - `ABORT` (default) - abort the migration.
    - `IGNORE_COLUMN` - ignore (not migrate to the table) those columns/fields in the cache record that are defined in GridGain 8 but not defined in GridGain 9.
    - `SKIP_RECORD` - ignore (not migrate to the table) the entire cache record.
    - `PACK_EXTRA` - serialize to JSON and store in the `__EXTRA__` column all additional columns/fields in the cache record. The tool adds this column to the table (it is not native to GridGain 9) and makes this column [accessible to the Java client](codebase-migration.md).
  - `--rate-limiter` - limits the number of records migrated per second (allows to save resources). The default is "-1", which means "no limit".
  - `--client.basicAuthenticator.username` - the name of the user to authenticate to GridGain 9 cluster with. User password must be specified in the `IGNITE_CLIENT_SECRET` environment variable.
- Run the persistent data migration command in the migration tool:

  ```bash
  bin/migration-tools persistent-data work-dir consistent-id config-file migrate-cache cacheName gg9urls [--mode] [--rate-limiter]  [--client.basicAuthenticator.username]
  ```

  Where:

  - `work-dir` - the GridGain 8 node's work directory. By default, it is the `{GRIDGAIN_HOME}/work` folder.
  - `consistent-id` - the GridGain 8 node's unique node identifier.
  - `config-file` - GridGain 8 configuration file. This file will be used to determine table parameters in GridGain 9.
  - `cacheName` - the name of the specific cache to migrate.
  - `gg9urls` - the list of URLs that the migration tool will use to connect to the GridGain 9 cluster.
  - `--mode` - the migration mode, which defines what to do in case of an irreconcilable mismatch between the object stored in the cache and the GridGain 9 table:
    - `ABORT` (default) - abort the migration.
    - `IGNORE_COLUMN` - ignore (not migrate to the table) those columns/fields in the cache record that are defined in GridGain 8 but not defined in GridGain 9.
    - `SKIP_RECORD` - ignore (not migrate to the table) the entire cache record.
    - `PACK_EXTRA` - serialize to JSON and store in the `__EXTRA__` column all additional columns/fields in the cache record. The tool adds this column to the table (it is not native to GridGain 9) and makes this column [accessible to the Java client](codebase-migration.md).
  - `--rate-limiter` - limits the number of records migrated per second (allows to save resources). The default is "-1", which means "no limit".
  - `--client.basicAuthenticator.username` - the name of the user to authenticate to GridGain 9 cluster with. User password must be specified in the `IGNITE_CLIENT_SECRET` environment variable.

The migration tool analyzes the specified cache and writes it to the GridGain 9 cluster.

Here is what your commands may look like:

```bash
bin/migration-tools persistent-data ./nodeWorkDir ad26bff6-5ff5-49f1-9a61-425a827953ed ./config-file.xml list-caches
bin/migration-tools persistent-data ./nodeWorkDir ad26bff6-5ff5-49f1-9a61-425a827953ed ./config-file.xml migrate-cache cacheName localhost:10800 --mode IGNORE_COLUMN --rate-limiter 1000
```

In this case, the migration tools will first display what caches are available, and then migrate the `cacheName` cache.

Migration tool will store logs in the `USER_HOME/.ignite-migration-tools/logs` folder.
Alternatively, the logs folder can be configured by using the `IGNITE_MIGRATION_TOOLS_LOGS_DIR` environment variable.
