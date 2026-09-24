---
description: >-
  How to configure a GridGain 9 cluster to receive the components of a
  GridGain 8 cluster, either from the GridGain 8 configuration or from scratch.
---

# Configuration Migration

This section describes how to configure a GridGain 9 cluster into which you will migrate all the components of your GridGain 8 cluster.

## Configure the Cluster

You need to configure the cluster you have created to match the GridGain 8 cluster you are migrating from.

While cluster configuration files for GridGain 8 are XML beans, GridGain 9 uses the HOCON format. Moreover, many configuration structures in version 9 are different from those used in version 8.

In GridGain 9, the configuration file has a single root called `ignite`. All configuration sections are children, grandchildren, etc., of that root.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

For example:

```json
{
    "ignite" : {
        "network" : {
            "nodeFinder" : {
                "netClusterNodes" : ["localhost:3344"]
            },
            "port" : 3344
        },
        "storage" : {
            "profiles" : [
                {
                    "name" : "persistent",
                    "engine" : "aipersist"
                }
            ]
        },
        "userAttributes" : {
            "region" : "US",
            "storage" : "SSD"
        }
    }
}
```

There are two options for creating the required GridGain 9 configuration:

- [Based on GridGain 8 Configuration](#based-on-gridgain-8-configuration)
- [From Scratch](#from-scratch)

## Based on GridGain 8 Configuration

To create a GridGain 9 cluster and node configuration HOCON files based on the GridGain 8 configuration XML file, you can use the migration tools:

### Download and Install Migration Tools

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

### Update Configuration

For simpler configurations, this tool will be sufficient. All [Supported Properties](#supported-properties) will be converted to GridGain 9 format, and you will receive warnings for all configuration parameters that were not converted.

Advanced cluster configurations should be remade in GridGain 9 [From Scratch](#from-scratch) to avoid possible issues.

#### Supported Properties

The migration tool supports the following configuration properties:

- `clientConnectorConfiguration`
- `communicationSpi`
- `dataStorageConfiguration`
- `discoverySpi`
- `sslContextFactory`

Other properties present in the configuration will be ignored.

### Convert Configuration

To convert the configuration:

```bash
bin/migration-tools configuration-converter sourceFile targetNodeConfig targetClusterConfig
```

Where:

- `sourceFile` is the GridGain 8 configuration file.
- `targetNodeConfig` is the node configuration file. This configuration will be applied only to individual nodes.
- `targetClusterConfig` is the cluster configuration file. This configuration will be applied to the entire cluster.

For example:

```bash
bin/migration-tools configuration-converter source.xml target-node.conf target-cluster.conf
```

Migration tool will store logs in the `USER_HOME/.ignite-migration-tools/logs` folder by default.
Alternatively, the logs folder can be configured using the `IGNITE_MIGRATION_TOOLS_LOGS_DIR` environment variable.

### Apply Configuration

#### Node Configuration

You can apply the converted node configuration to the node on startup by replacing the contents of the `etc/gridgain-config.conf` file. Only modified configurations are applied, other required parameters will be applied at default values. The default configuration file contains only default values.

#### Cluster Configuration

The newly generated configuration can be applied to the cluster by using the CLI tool.

- Start GridGain 9 nodes as described in the [Quick Start](../../gridgain9-get-started/quick-start.md);
- When initializing the cluster, provide the :

  ```bash
  cluster init --name=sampleCluster --license=/license.conf --config-files=target-cluster.conf
  ```

## From Scratch

GridGain 9 configuration is split between Cluster, Node and distribution zone configurations.

### Node Configuration

Node configuration stores information about the locally running node.

#### Storage Configuration

GridGain 9 storage is configured in a completely different manner from GridGain 8:

- First, you configure **storage engine** properties, which may include properties like page size or checkpoint frequency.
- Then, you create a **storage profile**, which defines a specific storage that will be used.
- Then, you create a **distribution zone** using the storage profile, which can be further used to fine-tune the storage by defining where and how to store data across the cluster.
- Finally, each **table** can be assigned  to the distribution zone, or directly to a storage profile.

Fore more information about the storage profiles, see [Storage Profiles and Engines](../../architecture/storage/README.md) and [Distribution Zones](../../architecture/storage/distribution-zones.md).

Note:

- Only tables and distribution zones can be configured from code. Storage profiles and engines must be configured by updating node configuration and restarting node.
- Custom affinity functions are replaced by distribution zones.
- External storage is supported via cache storage that must be configured by using SQL.

#### Client Configuration

All clients in GridGain 9 are "thin", and use a similar `clientConnector` configuration. See [GridGain Clients](../developers-guide/clients/overview.md) section for more information on configuring client connector.

#### Eviction Policies

Data eviction is performed on volatile storage based on [storage engine](../../architecture/storage/README.md) configuration.

#### Expiry Policies

Expiry policies are now configured on a per-table basis by creating a column with `timestamp` data type and specifying it with a `EXPIRE AT` command. See the [SQL DDL](../../reference/sql/ddl.md) reference.

#### Network Configuration

Node network configuration is now performed in  the `network` section of the [node configuration](../../reference/configuration/node-configuration-parameters.md).

#### REST API Configuration

REST API is a significant part of GridGain 9. It can be used for multiple purposes, including cluster and node configuration and running SQL requests.

You can configure REST properties in [node configuration](../../reference/configuration/node-configuration-parameters.md). For more information about REST API, see the [REST API](../../reference/rest-api/overview.md) documentation and the provided [OpenAPI](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html) specification.

### Cluster Configuration

Cluster configuration applies to all nodes in the cluster. It is automatically propagated across the cluster from the node you apply in at.

#### Data Encryption

Transparent data encryption is configured for the whole cluster at once, instead of being done on a per-cache basis. For information on configuring TDE, see [Transparent Data Encryption](../../security/transparent-data-encryption.md) section.

#### Handling Events

Events configuration is simplified in GridGain 9. It is separated in 2 configurations:

- Event **channels** define what is collected.
- Event **sinks** define where the data is sent.

In the current release, only `log` sink are supported. You can configure events as described in the [Events](../../gridgain9-usage/events/working-with-events.md) section.

#### Metrics Collection

GridGain 9 has metrics disabled by default.

All metrics are grouped according to their metric sources, and are enabled in cluster configuration per metric source.

Then, these metrics will be available in GridGain JMX beans.

For instructions on configuring metrics, see [Metrics Configuration](../monitoring/configuring-metrics.md).

#### Cluster Security and Authorization

Cluster security and authorization was completely rewritten from the ground up and is not directly comparable with GridGain 8. In GridGain 9:

- If security is enabled, users need a password to log in to the cluster.
- Each user has one or more roles.
- Each role specifies a list of permissions that users with this role can perform.

All security configuration is part of cluster configuration and is shared across all nodes. For more information on configuring security, see [Authentication](../../security/authentication.md) documentation.
