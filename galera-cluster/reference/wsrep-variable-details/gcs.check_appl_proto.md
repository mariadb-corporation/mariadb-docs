# gcs.check\_appl\_proto

Controls whether the node performs application-level protocol version checks when joining a cluster.

The `wsrep_provider_options` system variable applies to MariaDB Enterprise Cluster, powered by Galera and to Galera Cluster available with MariaDB Community Server. This page relates specifically to the `gcs.check_appl_proto` `wsrep_provider_options`.

## Details

Galera Cluster automatically uses the highest protocol version supported by all nodes. This prevents older nodes, which lack support for newer features, from joining or disrupting the cluster until an upgrade solution is available.

However, MySQL and MariaDB have evolved differently, and their internal protocol versions are incomparable. This incompatibility prevents a mixed-node cluster (MySQL nodes and MariaDB nodes) from forming, which blocks rolling migrations.

Migration Usage: When [migrating from a MySQL-based Galera cluster](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migration-from-mysql-to-mariadb-cluster-node-by-node-in-place) (e.g., Percona XtraDB Cluster) to MariaDB Galera Cluster, this parameter must be set to `FALSE` (OFF) on all nodes to disable the protocol check. Once the cluster is fully migrated to MariaDB, it should be set back to `TRUE`.

{% hint style="warning" %}
Known reporting issue in early versions

The variable may appear as `OFF` in plugins even though the default behavior is `TRUE`. Explicitly configure it to ensure the desired state during migration.
{% endhint %}

| Option Name   | gcs.check\_appl\_proto |
| ------------- | ---------------------- |
| Default Value | `TRUE`                 |
| Dynamic       | `NO`                   |
| Debug         | `NO`                   |

## Examples

### Display Current Value

`wsrep_provider_options` define optional settings the node passes to the wsrep provider.

To display current `wsrep_provider_options` values:

```sql
SHOW GLOBAL VARIABLES LIKE 'wsrep_provider_options';
```

The expected output will display the option and the value. Options with no default value will not be displayed in the output.

### Set in Configuration File

When changing a setting for a wsrep\_provider\_options in the config file, you must list EVERY option that is to have a value other than the default value. Options that are not explicitly listed are reset to the default value.

Options are set in the `my.cnf` configuration file. Use the `;` delimiter to set multiple options.

The configuration file must be updated on each node. A restart to each node is needed for changes to take effect.

Use a quoted string that includes every option where you want to override the default value. Options that are not in the list will reset to their default value.

To set the option in the configuration file (example for migration):

{% code overflow="wrap" %}
```ini
wsrep_provider_options='gcs.check_appl_proto=FALSE;gcache.size=512M;gcs.fc_limit=32'
```
{% endcode %}

### Set Dynamically

The `gcs.check_appl_proto` option cannot be set dynamically. It can only be set in the configuration file.

Trying to change a non-dynamic option with `SET` results in an error:

```
ERROR 1210 (HY000): Incorrect arguments to SET
```
