---
description: >-
  Reference for the GridGain 9 command line interface: interactive and
  non-interactive modes and the full command set for managing SQL, clusters,
  nodes, snapshots, recovery, security, replication, and change data capture.
---

# GridGain CLI Tool

## CLI Mode

The GridGain CLI communicates with the cluster via the REST API, allowing you to configure the entire cluster or apply node-specific settings. You can run the CLI either in the interactive mode or execute commands without entering it.

### Interactive CLI Mode

To use the CLI in the interactive mode, first [run](quick-start/getting-started-guide.md#start-the-gridgain-cli) it, then configure the [cluster](administrators-guide/config/cluster-config.md) or [node](administrators-guide/config/node-config.md) using the `update` command.

For example, to add a new user to the cluster:

```bash
cluster config update ignite.security.authentication.providers.default.users=[{username=newuser,displayName=newuser,password="newpassword",passwordEncoding=PLAIN,roles=[system]}]
```

### Non-Interactive CLI Mode

Non-interactive mode is useful for quick updates or when running commands in scripts.

When running commands non-interactively, enclose arguments in quotation marks to ensure that special POSIX characters (such as `{` and `}`) are interpreted correctly:

{% tabs %}
{% tab title="Linux" %}
```bash
bin/gridgain9 cluster config update "ignite.schemaSync={delayDurationMillis=500,maxClockSkewMillis=500}"
```
{% endtab %}

{% tab title="Windows" %}
```bash
bin/gridgain9.bat cluster config update "ignite.schemaSync={delayDurationMillis=500,maxClockSkewMillis=500}"
```
{% endtab %}
{% endtabs %}

Alternatively, you can use the backslash (`\`) to escape all special characters in your command. For example:

{% tabs %}
{% tab title="Linux" %}
```bash
bin/gridgain9 cluster config update ignite.security.authentication.providers.default.users=\[\{username\=newuser,displayName\=newuser,password\=\"newpassword\",passwordEncoding\=PLAIN,roles\=\[system\]\}\]
```
{% endtab %}

{% tab title="Windows" %}
```bash
bin/gridgain9.bat cluster config update ignite.security.authentication.providers.default.users=\[\{username\=newuser,displayName\=newuser,password\=\"newpassword\",passwordEncoding\=PLAIN,roles\=\[system\]\}\]
```
{% endtab %}
{% endtabs %}

Non-interactive mode is also useful in automation scripts. For example, you can set configuration items in a Bash script as follows:

```bash
#!/bin/bash

...

bin/gridgain9 cluster config update "ignite.schemaSync={delayDurationMillis=500,maxClockSkewMillis=500}"

bin/gridgain9 cluster config update "ignite.security.authentication.providers.default.users=[{username=newuser,displayName=newuser,password=\"newpassword\",passwordEncoding=PLAIN,roles=[system]}]"
```

### Verbose Output

All CLI commands can provide additional output that can be helpful in debugging. You can specify the `-v` option multiple times to increase output verbosity. Single option shows REST request and response, second option (-vv) shows request headers, third one (-vvv) shows request body.

### CLI Tool Files

CLI tool stores additional files required for its operation on your local machine. These files are required for its normal operation and include defaults, history, logs and secrets. By default, these files are stored in the following locations:

- `~/.local/state/ignitecli/logs` directory contains CLI tool logs;
- `~/.local/state/ignitecli/history` file contains the history of CLI tool commands;
- `~/.config/ignitecli/defaults` file contains the default values to be used for CLI tool configuration for each profile;
- `~/.config/ignitecli/secrets` file contains potentially sensitive information such as passwords and other authorization information.

{% hint style="info" %}
Windows systems the `%USERPROFILE%` address instead of `~` for user home directory.
{% endhint %}

#### Configuration

You can configure the directories with the following methods:

1. Individually configure the location of the files with the following environment variables:
   - `IGNITE_CLI_LOGS_DIR` - configures the location of the logs directory;
   - `IGNITE_CLI_CONFIG_FILE` - configures the location of the `defaults` file;
   - `IGNITE_CLI_SECRET_CONFIG_FILE` - configures the location of the `secrets` file.
2. Configure home environment variables:

   {% hint style="info" %}
   These configuration variables follow the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) and do not override the parameters from the previous step.
   {% endhint %}
   - `$XDG_STATE_HOME` - sets the CLI tool home directory that will be used for storing logs and history;
   - `$XDG_CONFIG_HOME` - sets the CLI tool configuration home directory that will be used to store configuration files.
3. Set the user directory in the `user.home` JVM property.

### Overriding JVM Properties

You can override the default CLI tool JVM properties by specifying them in the `GRIDGAIN9_OPTS` environment variable before running the start script.

{% hint style="info" %}
We recommend explicitly limiting the CLI's memory footprint by setting `-Xms` and `-Xmx` to lower values before launching the tool.
{% endhint %}

{% tabs %}
{% tab title="Linux" %}
```bash
export GRIDGAIN9_OPTS="-Xms128m -Xmx512m"
```
{% endtab %}

{% tab title="Windows" %}
```bash
$env:GRIDGAIN9_OPTS = "-Xms128m -Xmx512m"
```
{% endtab %}
{% endtabs %}

### Default Parameter Values

Some parameters are optional because the CLI can resolve their values automatically from the profile configuration or the current session state. The `--url` parameter for all `cluster` and `node` commands works this way. Currently, this is the only parameter with this resolution behavior.

The resolution order depends on whether the CLI is running in interactive (REPL) or non-interactive mode.

#### Non-Interactive Mode

The value for `--url` is resolved in the following order:

1. Explicitly provided value: `--url=<clusterUrl>`.
2. If `--profile=<profileName>` is specified, the `ignite.cluster-endpoint-url` property from the specified CLI profile is used.
3. If neither is provided, or if the specified CLI profile does not define `ignite.cluster-endpoint-url`, the value is taken from the currently active profile.

#### Interactive (REPL) Mode

The value for `--url` is resolved in the following order:

1. Explicitly provided value: `--url=<clusterUrl>`.
2. If `--profile=<profileName>` is specified, the `ignite.cluster-endpoint-url` property from the specified CLI profile is used.
3. If no URL was resolved from the previous steps and the CLI is currently connected to a node, the URL of the connected node is used.
4. If no URL was resolved from the previous steps and the CLI is not connected to a node, the value is taken from the currently active profile.

## SQL Commands

These commands help you execute SQL queries against the cluster.

### sql

Executes SQL query or enters the interactive SQL editor mode if no SQL query is specified.

**Syntax**

```
sql [--jdbc-url=<jdbc>] [--plain] [--timed] [--query-timeout=<seconds>] [--file=<file>] [--profile=<profileName>] [--verbose] <command>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑jdbc‑url` | Option | No | JDBC url to GridGain cluster (e.g., 'jdbc:ignite:thin://127.0.0.1:10800'). |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑timed` | Flag | No | Display query execution time, as measured on the client, after the command output. In interactive mode the time will be displayed after each command. |
| `‑‑query‑timeout` | Option | No | Number of seconds a query can run before it is aborted. `0`, the default, means no limit. In interactive mode, the timeout applies to every query in the session. |
| `‑‑file` | Option | No | Path to file with SQL commands to execute. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<command>` | Argument | Yes | SQL query to execute. |

**Example**

```bash
sql "SELECT * FROM PUBLIC.PERSON"
```

{% code title="Output" %}
```
╔════╤═══════╗
║ ID │ VAL   ║
╠════╪═══════╣
║ 1  │ hello ║
╚════╧═══════╝
```
{% endcode %}

---

### sql planner invalidate-cache

Invalidates SQL planner cache.

**Syntax**

```
sql planner invalidate-cache [--tables=<tables>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑tables` | Option | No | Comma-separated list of tables. |
| `‑‑url` | Option | No | URL of cluster endpoint. It can be any node URL. If not set, the default URL from the profile settings will be used. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
sql planner invalidate-cache --tables=PUBLIC.PERSON,PUBLIC.ORDERS
```

{% code title="Output" %}
```
Successfully cleared SQL query plan cache.
```
{% endcode %}

---

## CLI Configuration Commands

These commands help you configure GridGain CLI tool profiles and settings.

### cli config profile create

Creates a profile with the given name.

**Syntax**

```
cli config profile create [--activate] [--copy-from=<copyFrom>] [--verbose] <profileName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑activate` | Flag | No | Activate new profile as current. |
| `‑‑copy-from` | Option | No | Profile whose content will be copied to new one. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls.. |
| `<profileName>` | Argument | Yes | Name of new profile. |

**Example**

```
cli config profile create --activate --copy-from=default myprofile
```

{% code title="Output" %}
```
Profile myprofile was created successfully.
```
{% endcode %}

---

### cli config profile activate

Activates the profile identified by name.

**Syntax**

```
cli config profile activate [--verbose] <profileName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<profileName>` | Argument | Yes | Name of profile to activate. |

**Example**

```bash
cli config profile activate myprofile
```

{% code title="Output" %}
```
Profile myprofile was activated successfully.
```
{% endcode %}

---

### cli config profile list

Lists configuration profiles.

**Syntax**

```
cli config profile list [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cli config profile list
```

{% code title="Output" %}
```
* default
  test
```
{% endcode %}

{% hint style="info" %}
When the output goes to a terminal, the active profile is marked with an asterisk. When the output is redirected or piped, only the profile names are printed.
{% endhint %}

---

### cli config profile show

Gets the name of the current profile.

**Syntax**

```
cli config profile show [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cli config profile show
```

{% code title="Output" %}
```
Current profile: default
```
{% endcode %}

---

### cli config get

Gets the value for the specified configuration key.

**Syntax**

```
cli config get [--profile=<profileName>] [--verbose] <key>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<key>` | Argument | Yes | Property name. |

**Example**

```bash
cli config get ignite.jdbc-url
```

{% code title="Output" %}
```
jdbc:ignite:thin://127.0.0.1:10800
```
{% endcode %}

---

### cli config set

Sets configuration parameters. Pass one or more `key=value` pairs, separated by spaces.

**Syntax**

```
cli config set [--profile=<profileName>] [--verbose] <String=String>...
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<String=String>...` | Arguments | Yes | CLI configuration parameters. |

**Example**

```bash
cli config set ignite.jdbc-url=jdbc:ignite:thin://127.0.0.1:10800 ignite.cli.pager.enabled=false
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### cli config show

Shows the currently active configuration.

**Syntax**

```
cli config show [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cli config show
```

{% code title="Output" %}
```
[default]
ignite.cluster-endpoint-url=http://localhost:10301
ignite.auth.basic.username=ignite
ignite.jdbc-url=jdbc:ignite:thin://127.0.0.1:10801
ignite.auth.basic.password=ignite
```
{% endcode %}

---

### cli config remove

Removes the specified configuration key.

**Syntax**

```
cli config remove [--profile=<profileName>] [--verbose] <key>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<key>` | Argument | Yes | Property name. |

**Example**

```bash
cli config remove ignite.jdbc-url
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

## Cluster Commands

These commands help you manage your cluster.

### cluster config show

Shows configuration of the cluster indicated by the endpoint URL and, optionally, by a configuration path selector.

**Syntax**

```
cluster config show [--url=<clusterUrl>] [--format=<format>] [--profile=<profileName>] [--verbose] [<selector>]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑format` | Option | No | Output format. Valid values: JSON, HOCON (Default: HOCON). |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<selector>` | Argument | No | Configuration path selector. |

**Example**

```bash
cluster config show
```

{% code title="Output" %}
```
ignite {
    gc {
        batchSize=5
        lowWatermark {
            dataAvailabilityTimeMillis=600000
            updateIntervalMillis=300000
        }
        threads=10
    }
    replication {
        idleSafeTimePropagationDurationMillis=1000
        leaseExpirationIntervalMillis=5000
        rpcTimeoutMillis=60000
    }
    security {
        enabled=true
    }
    sql {
        planner {
            estimatedNumberOfQueries=1024
            maxPlanningTimeMillis=15000
        }
    }
    ...
}
```
{% endcode %}

---

### cluster config update

Updates configuration of the cluster indicated by the endpoint URL with the provided argument values.

**Syntax**

```
cluster config update [--url=<clusterUrl>] [--file=<configFile>] [--profile=<profileName>] [--verbose] [<args>...]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑file` | Option | No | Path to file with config update commands to execute. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<args>...` | Arguments | No | Configuration arguments and values to update. |

**Example**

```bash
cluster config update ignite.system.idleSafeTimeSyncIntervalMillis=250
```

{% code title="Output" %}
```
Cluster configuration was updated successfully
```
{% endcode %}

---

### cluster init

Initializes the cluster.

**Syntax**

```
cluster init --name=<clusterName> --license=<license> [--metastorage-group=<nodeNames>] [--cluster-management-group=<nodeNames>] [--config=<config>] [--config-files=<filePaths>] [--if-needed] [--if-nodes=<nodeCount>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Human-readable name of the cluster. Can be changed after initialization with [cluster rename](#cluster-rename). |
| `‑‑license` | Option | Yes | License file. |
| `‑‑metastorage-group` | Option | No | Metastorage group nodes (comma-separated list). |
| `‑‑cluster-management-group` | Option | No | Names of nodes that will host the Cluster Management Group (comma-separated list). |
| `‑‑config` | Option | No | Cluster configuration that will be applied during initialization. |
| `‑‑config-files` | Option | No | Path to cluster configuration files (comma-separated list). |
| `‑‑if-needed` | Flag | No | Skips initialization and exits with code 0 if the cluster is already initialized, instead of failing. The check is not atomic with initialization, so concurrent `cluster init` calls may still fail with a server-side error. |
| `‑‑if-nodes` | Option | No | Skips initialization and exits with code 0 if fewer than `<nodeCount>` nodes are visible in the physical topology. Must be a positive integer and requires `‑‑if-needed`. If the physical topology cannot be retrieved, the command fails. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster init --name=myCluster --license=/path/to/license
```

To make initialization idempotent, use `--if-needed` argument. To also defer initialization until enough nodes have joined, add `--if-nodes` argument with the required number of nodes:

```bash
cluster init --name=myCluster --license=/path/to/license --if-needed --if-nodes=3
```

{% code title="Output" %}
```
Cluster was initialized successfully.
```
{% endcode %}

---

### cluster rename

Renames an already-initialized cluster. The cluster keeps its identity (cluster ID, metastorage state, data); only the human-readable name is updated.

{% hint style="info" %}
This command requires the `RENAME_CLUSTER` privilege. See [User Permissions and Roles](administrators-guide/security/permissions.md).
{% endhint %}

**Syntax**

```
cluster rename --name=<newClusterName> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | New human-readable name of the cluster. Must not be empty. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster rename --name=newClusterName --url=http://localhost:10300
```

{% code title="Output" %}
```
Cluster was renamed successfully
```
{% endcode %}

---

### cluster status

Prints status of the cluster.

**Syntax**

```
cluster status [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster status --url http://localhost:10300
```

{% code title="Output" %}
```
[name: dc1, nodes: 3, status: active, cmgNodes: [node1], msNodes: [node1]]
```
{% endcode %}

---

### cluster topology physical

Shows physical topology of the specified cluster.

**Syntax**

```
cluster topology physical [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster topology physical --url http://localhost:10300
```

{% code title="Output" %}
```
╔═══════╤═══════════╤══════╤═══════════════╤══════════════════════════════════════╗
║ name  │ host      │ port │ consistent id │ id                                   ║
╠═══════╪═══════════╪══════╪═══════════════╪══════════════════════════════════════╣
║ node1 │ 127.0.0.1 │ 3301 │ node1         │ 6e20876f-384c-4785-8e22-f134ded0ed63 ║
╟───────┼───────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node2 │ 127.0.0.1 │ 3302 │ node2         │ 90af68df-1626-4933-b60b-74c95fd46c6a ║
╟───────┼───────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node3 │ 127.0.0.1 │ 3303 │ node3         │ e21b1452-aa34-4250-a193-790758f92a50 ║
╚═══════╧═══════════╧══════╧═══════════════╧══════════════════════════════════════╝
```
{% endcode %}

---

### cluster topology logical

Shows logical topology of the specified cluster.

**Syntax**

```
cluster topology logical [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster topology logical --url http://localhost:10300
```

{% code title="Output" %}
```
╔═══════╤═══════════╤══════╤═══════════════╤══════════════════════════════════════╗
║ name  │ host      │ port │ consistent id │ id                                   ║
╠═══════╪═══════════╪══════╪═══════════════╪══════════════════════════════════════╣
║ node1 │ 127.0.0.1 │ 3301 │ node1         │ 6e20876f-384c-4785-8e22-f134ded0ed63 ║
╟───────┼───────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node2 │ 127.0.0.1 │ 3302 │ node2         │ 90af68df-1626-4933-b60b-74c95fd46c6a ║
╟───────┼───────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node3 │ 127.0.0.1 │ 3303 │ node3         │ e21b1452-aa34-4250-a193-790758f92a50 ║
╚═══════╧═══════════╧══════╧═══════════════╧══════════════════════════════════════╝
```
{% endcode %}

---

### cluster unit deploy

Deploys a unit from a file:

**Syntax**

```
cluster unit deploy --version=<version> --path=<path> [--nodes=<nodes>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <id>
```

Or a directory recursively:

**Syntax**

```
cluster unit deploy --recursive --version=<version> --path=<path> [--nodes=<nodes>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <id>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | Yes | Unit version (x.y.z). |
| `‑‑path` | Option | Yes | Path to deployment unit file or directory. |
| `‑‑nodes` | Option | No | Initial set of nodes where the unit will be deployed (comma-separated). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<id>` | Argument | Yes | Deployment unit identifier. |
| `<recursive>` | Option | No | Deploys a folder with subdirectories. |

**Example**

```bash
cluster unit deploy --version=1.0.0 --path=/path/to/unit.jar
```

{% code title="Output" %}
```
Done
```
{% endcode %}

---

### cluster unit undeploy

Undeploys a unit.

**Syntax**

```
cluster unit undeploy --version=<version> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <id>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | Yes | Unit version (x.y.z). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<id>` | Argument | Yes | Unit id. |

**Example**

```bash
cluster unit undeploy --version=1.0.0 --url http://localhost:10300 myunit
```

{% code title="Output" %}
```
Done
```
{% endcode %}

---

### cluster unit list

Shows a list of deployed units for specified deployment unit.

**Syntax**

```
cluster unit list [--version=<version>] [--status=<statuses>] [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <unitId>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | No | Filters out deployment unit by version (exact match assumed). |
| `‑‑status` | Option | No | Filters out deployment unit by status (comma-separated). |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<unitId>` | Argument | Yes | Deployment unit id. |

**Example**

```bash
cluster unit list --status=DEPLOYED,STARTING myunit
```

{% code title="Output" %}
```
╔════════╤═════════╤══════════╗
║ id     │ version │ status   ║
╠════════╪═════════╪══════════╣
║ myunit │ *1.0.0  │ DEPLOYED ║
╚════════╧═════════╧══════════╝
```
{% endcode %}

---

### cluster metric source enable

Enables cluster metric source.

**Syntax**

```
cluster metric source enable [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <srcName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<srcName>` | Argument | Yes | Metric source name. |

**Example**

```bash
cluster metric source enable jvm
```

{% code title="Output" %}
```
Metric source was enabled successfully
```
{% endcode %}

---

### cluster metric source disable

Disables cluster metric source.

**Syntax**

```
cluster metric source disable [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <srcName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<srcName>` | Argument | Yes | Metric source name. |

**Example**

```bash
cluster metric source disable jvm
```

{% code title="Output" %}
```
Metric source was disabled successfully
```
{% endcode %}

---

### cluster metric source list

Lists cluster metric sources.

**Syntax**

```
cluster metric source list [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster metric source list
```

{% code title="Output" %}
```
╔═══════╤═══════════════════════════════════════════════════════════╤══════════════╗
║ Node  │ Source name                                               │ Availability ║
╠═══════╪═══════════════════════════════════════════════════════════╪══════════════╣
║ node1 │                                                           │              ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
║       │ client.handler                                            │ enabled      ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
║       │ clock.service                                             │ enabled      ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
║       │ jvm                                                       │ enabled      ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
║       │ metastorage                                               │ enabled      ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
║       │ os                                                        │ enabled      ║
╟───────┼───────────────────────────────────────────────────────────┼──────────────╢
...
╚═══════╧═══════════════════════════════════════════════════════════╧══════════════╝
```
{% endcode %}

---

## Snapshot Commands

These commands help you manage GridGain snapshots.

### cluster snapshot create

Creates a new snapshot.

**Syntax**

```
cluster snapshot create --type=<snapshotType> (--all | --tables=<tableNames> [--structures=<structureNames>] | --structures=<structureNames>) [--timestamp=<timestampValue>] [--destination=<destination>] [--encryption-provider=<encryptionProvider>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑type` | Option | Yes | Type of the snapshot to create. Possible values: 'full', 'incremental'. |
| `‑‑all` | Flag | No | Create snapshot of all tables. Incompatible with --tables. |
| `‑‑tables` | Option | No | Comma-separated fully-qualified table names that will be parts of the snapshot. Incompatible with --all. |
| `‑‑structures` | Option | No | Comma-separated fully-qualified structure names that will be parts of the snapshot. Incompatible with --all. |
| `‑‑timestamp` | Option | No | Timestamp to create snapshot at in the ISO-8601 format (e.g., 1970-01-01T00:00:00Z). |
| `‑‑destination` | Option | No | Name of the snapshot URI in configuration. |
| `‑‑encryption‑provider` | Option | No | Name of the encryption provider. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster snapshot create --type=full --all
```

{% code title="Output" %}
```
Snapshot has been started with ID cc57dc34-abaf-436c-9c25-fdf8add42c52
```
{% endcode %}

---

### cluster snapshot delete

Deletes a snapshot.

**Syntax**

```
cluster snapshot delete --id=<snapshotId> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑id` | Option | Yes | ID of the snapshot. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster snapshot delete --id=15225e58-a045-4d7b-8ebe-b965f99d560c
```

{% code title="Output" %}
```
Snapshot deletion has been started, operation ID 8472c6f3-16d5-489e-8dc2-6f2e3ff0f255
```
{% endcode %}

---

### cluster snapshot list

Returns a list of snapshots from configured snapshot paths. Works with both `LOCAL` and `REMOTE` paths.

**Syntax**

```
cluster snapshot list [--plain] [--show-nodes] [--show-tables] [--show-source-uri] [--source=<snapshotUriName>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑show‑nodes` | Flag | No | Display node names instead of just their count in the output. |
| `‑‑show‑tables` | Flag | No | Display table names instead of just their count in the output. |
| `‑‑show‑source‑uri` | Flag | No | Display the snapshot path URI in the output. |
| `‑‑source` | Option | No | Name of the snapshot path from configuration to list snapshots from. Accepts both `LOCAL` and `REMOTE` paths. If not specified, lists snapshots from all configured paths. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster snapshot list --show-nodes --show-tables
```

{% code title="Output" %}
```
╔══════════════════════════════════════╤════════════════════╤══════╤══════════════════════════╤═════════╤═══════════╤════════════════════════╤════════════════════════╤════════════════════╗
║ Snapshot ID                          │ Parent Snapshot ID │ Type │ Creation Time            │ Source  │ Path type │ Number of target nodes │ Number of actual nodes │ Number of tables   ║
╠══════════════════════════════════════╪════════════════════╪══════╪══════════════════════════╪═════════╪═══════════╪════════════════════════╪════════════════════════╪════════════════════╣
║ 211e3cf7-dc99-414d-b205-ef1ab5e307ac │                    │ FULL │ 2026-03-10T10:24:23.285Z │ remote1 │ REMOTE    │ 3                      │ 3                      │ 2                  ║
╚══════════════════════════════════════╧════════════════════╧══════╧══════════════════════════╧═════════╧═══════════╧════════════════════════╧════════════════════════╧════════════════════╝
```
{% endcode %}

---

### cluster snapshot restore

Restores a snapshot.

**Syntax**

```
cluster snapshot restore --id=<snapshotId> [--tables=<tableNames>] [--structures=<structureNames>] [--force] [--source=<source>] [--decryption-provider=<decryptionProvider>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑id` | Option | Yes | ID of the snapshot. |
| `‑‑tables` | Option | No | Comma-separated fully-qualified table names to restore from the snapshot. |
| `‑‑structures` | Option | No | Comma-separated fully-qualified structure names that will be recovered. |
| `‑‑force` | Flag | No | Overwrite structures that already exist on the cluster; without this flag, restoration fails instead. Overwriting can cause duplicate values generated using sequences. |
| `‑‑source` | Option | No | Name of the snapshot URI in configuration. |
| `‑‑decryption‑provider` | Option | No | Name of the decryption provider. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster snapshot restore --id=15225e58-a045-4d7b-8ebe-b965f99d560c --tables=PUBLIC.PERSON,PUBLIC.ORDERS
```

{% code title="Output" %}
```
Snapshot restoration has been started, operation ID 47b83cb2-3b09-44c3-97ed-81d6c67ac141
```
{% endcode %}

---

### cluster snapshot status

Returns snapshot operations.

**Syntax**

```
cluster snapshot status [--plain] [--id=<operationId>] [--all-nodes] [--show-tables] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑id` | Option | No | ID of the operation. |
| `‑‑all-nodes` | Flag | No | Optional flag that modifies the output to contain every status of all nodes that participate in the snapshot operation. |
| `‑‑show-tables` | Flag | No | Optional flag that modifies the output to contain table names that participate in snapshot creation or restoration. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cluster snapshot status --id=15225e58-a045-4d7b-8ebe-b965f99d560c --all-nodes --show-tables
```

{% code title="Output" %}
```
╔══════════════════════════════════════╤══════════════════════════╤══════════════════════════╤═══════════╤═══════════╤══════════════════════════════════════╤════════════════════╤═════════════╤═══════════════════════════╤═══════════╤═══════╗
║ Operation ID                         │ Start time               │ Timestamp                │ Operation │ Status    │ Target Snapshot ID                   │ Parent Snapshot ID │ Description │ URI                       │ Path type │ Force ║
╠══════════════════════════════════════╪══════════════════════════╪══════════════════════════╪═══════════╪═══════════╪══════════════════════════════════════╪════════════════════╪═════════════╪═══════════════════════════╪═══════════╪═══════╣
║ cc57dc34-abaf-436c-9c25-fdf8add42c52 │ 2026-03-10T10:19:51.542Z │ 2026-03-10T10:19:51.542Z │ CREATE    │ COMPLETED │ 211e3cf7-dc99-414d-b205-ef1ab5e307ac │                    │             │ file:///tmp/gg9-snapshots │ LOCAL     │ false ║
╚══════════════════════════════════════╧══════════════════════════╧══════════════════════════╧═══════════╧═══════════╧══════════════════════════════════════╧════════════════════╧═════════════╧═══════════════════════════╧═══════════╧═══════╝
```
{% endcode %}

---

## Node Commands

These commands help you manage individual nodes.

### node config show

Shows node configuration.

**Syntax**

```
node config show [--url=<nodeUrl>] [--format=<format>] [--profile=<profileName>] [--verbose] [<selector>]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑format` | Option | No | Output format. Valid values: JSON, HOCON (Default: HOCON). |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<selector>` | Argument | No | Configuration path selector. |

**Example**

```bash
node config show ignite.clientConnector
```

{% code title="Output" %}
```
ignite {
    clientConnector {
        connectTimeoutMillis=5000
        idleTimeoutMillis=0
        metricsEnabled=true
        port=10801
        ssl {
            enabled=false
        }
    }
    network {
        nodeFinder {
            netClusterNodes=[
                "localhost:3301",
                "localhost:3302",
                "localhost:3303"
            ]
            type=STATIC
        }
        port=3301
    }
    rest {
        port=10301
    }
    ...
}
```
{% endcode %}

---

### node config update

Updates node configuration.

**Syntax**

```
node config update [--url=<nodeUrl>] [--file=<configFile>] [--profile=<profileName>] [--verbose] [<args>...]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑file` | Option | No | Path to file with config update commands to execute. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<args>...` | Arguments | No | Configuration arguments and values to update. |

**Example**

```bash
node config update --url http://localhost:10300 ignite.clientConnector.connectTimeoutMillis=5000
```

{% code title="Output" %}
```
Node configuration updated. Restart the node to apply changes.
```
{% endcode %}

---

### node status

Prints status of the node.

**Syntax**

```
node status [--url=<nodeUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
node status
```

{% code title="Output" %}
```
[name: node1, state: started]
```
{% endcode %}

---

### node version

Prints the node build version and, when the build was stamped with one, the git commit it was built from.

**Syntax**

```
node version [--url=<nodeUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
node version
```

{% code title="Output" %}
```
GridGain version 9.1, revision 2eaf1d093f
```
{% endcode %}

---

### node metric list

Lists node metrics.

**Syntax**

```
node metric list [--url=<nodeUrl>] [--plain] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
node metric list
```

{% code title="Output" %}
```
╔═══════════════════════════════════╤══════════════════════════╤═════════════════════════════════════╗
║ Set name                          │ Metric name              │ Description                         ║
╠═══════════════════════════════════╪══════════════════════════╪═════════════════════════════════════╣
║ client.handler                    │                          │                                     ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ BytesReceived            │ Total bytes received                ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ BytesSent                │ Total bytes sent                    ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ ConnectionsInitiated     │ Total initiated connections         ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ RequestsActive           │ Requests in progress                ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ RequestsFailed           │ Total failed requests               ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ RequestsProcessed        │ Total processed requests            ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
║                                   │ SessionsAccepted         │ Total accepted sessions             ║
╟───────────────────────────────────┼──────────────────────────┼─────────────────────────────────────╢
...
╚═══════════════════════════════════╧══════════════════════════╧═════════════════════════════════════╝
```
{% endcode %}

---

### node metric source enable

Enables node metric source.

**Syntax**

```
node metric source enable [--url=<nodeUrl>] [--profile=<profileName>] [--verbose] <srcName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<srcName>` | Argument | Yes | Metric source name. |

**Example**

```bash
node metric source enable jvm
```

{% code title="Output" %}
```
Metric source was enabled successfully
```
{% endcode %}

---

### node metric source disable

Disables node metric source.

**Syntax**

```
node metric source disable [--url=<nodeUrl>] [--profile=<profileName>] [--verbose] <srcName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<srcName>` | Argument | Yes | Metric source name. |

**Example**

```bash
node metric source disable jvm
```

{% code title="Output" %}
```
Metric source was disabled successfully
```
{% endcode %}

---

### node metric source list

Lists node metric sources.

**Syntax**

```
node metric source list [--url=<nodeUrl>] [--plain] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
node metric source list --plain
```

{% code title="Output" %}
```
╔═══════════════════════════════════════════════════════════╤══════════╗
║ Source name                                               │ Enabled  ║
╠═══════════════════════════════════════════════════════════╪══════════╣
║ client.handler                                            │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ clock.service                                             │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ expiration                                                │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ index.builder                                             │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ jvm                                                       │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ metastorage                                               │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
║ os                                                        │ enabled  ║
╟───────────────────────────────────────────────────────────┼──────────╢
...
╚═══════════════════════════════════════════════════════════╧══════════╝
```
{% endcode %}

---

### node unit list

Shows a list of deployed units.

**Syntax**

```
node unit list [--version=<version>] [--status=<statuses>] [--url=<nodeUrl>] [--plain] [--profile=<profileName>] [--verbose] <unitId>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | No | Filters out deployment unit by version (exact match assumed). |
| `‑‑status` | Option | No | Filters out deployment unit by status (comma-separated). |
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<unitId>` | Argument | Yes | Deployment unit id. |

**Example**

```bash
node unit list --status=DEPLOYED myunit
```

{% code title="Output" %}
```
╔════════╤═════════╤══════════╗
║ id     │ version │ status   ║
╠════════╪═════════╪══════════╣
║ myunit │ *1.0.0  │ DEPLOYED ║
╚════════╧═════════╧══════════╝
```
{% endcode %}

---

### node unit inspect

Inspects the structure of a deployed unit, allowing you to view the contents and file structure of a specific deployment unit version.

**Syntax**

```
node unit inspect [--version=<version>] [--node=<nodeName>] [--url=<nodeUrl>] [--plain] [--profile=<profileName>] [--verbose] <unitId>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | Yes | Unit version in x.y.z format. |
| `‑‑node` | Option | No | The name of the node to perform the operation on. Node names can be seen in the output of the 'cluster topology' command. Alias: `-n`. |
| `‑‑url` | Option | No | URL of a node that will be used as a communication endpoint. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<unitId>` | Argument | Yes | Deployment unit id. |

**Example**

```bash
node unit inspect --version=1.0.0 myunit
```

{% code title="Output" %}
```
myunit-1.0.0
\-- ignite-examples-9.1.127-snapshot.jar (96.3 KiB)
```
{% endcode %}

---

## Disaster Recovery Commands

These commands let you recover data partitions in disaster scenarios and recover system RAFT groups.

### recovery partitions restart

Restarts the corresponding replica service and Raft group for each specified partitions. If no partition IDs are provided, all partitions in the specified zone are restarted. If no node names are specified, the operation applies to all nodes.

**Syntax**

```
recovery partitions restart --zone=<zoneName> --table=<tableName> [--partitions=<partitionIds>] [--nodes=<nodeNames>] [--with-cleanup] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑zone` | Option | Yes | Name of the zone to reset partitions of. Case-sensitive, without quotes. |
| `‑‑table` | Option | Yes | Fully-qualified name of the table to reset partitions of. Case-sensitive, without quotes. |
| `‑‑partitions` | Option | No | IDs of partitions to get states. All partitions if not set (comma-separated). |
| `‑‑nodes` | Option | No | Names specifying nodes to get partition states from. Case-sensitive, without quotes, all nodes if not set (comma-separated). |
| `‑‑with-cleanup` | Flag | No | Restarts partitions, preceded by a storage cleanup. This will remove all data from the partition storages before restart. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery partitions restart --zone=default --table=PUBLIC.PERSON --with-cleanup
```

{% code title="Output" %}
```
Successfully restarted partitions.
```
{% endcode %}

---

### recovery partitions reset

Forces recovery of partitions that have lost Raft majority by performing a forced rebalance. This rebalance resets the Raft peers and allows a new leader to be elected. If no partition IDs are provided, all partitions in the specified zone are reset.

**Syntax**

```
recovery partitions reset --zone=<zoneName> [--table=<tableName>] [--partitions=<partitionIds>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑zone` | Option | Yes | Name of the zone to reset partitions of. Case-sensitive, without quotes. |
| `‑‑table` | Option | No | Fully-qualified name of the table to reset partitions of. Case-sensitive, without quotes. |
| `‑‑partitions` | Option | No | IDs of partitions to get states. All partitions if not set (comma-separated). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery partitions reset --zone=default --table=PUBLIC.PERSON
```

{% code title="Output" %}
```
Successfully reset partitions.
```
{% endcode %}

---

### recovery partitions states

Returns partition states.

**Syntax**

```
recovery partitions states (--global | --local) [--nodes=<nodeNames>] [--partitions=<partitionIds>] [--zones=<zoneNames>] [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑global` | Flag | Yes | Gets global partition states. One of global or local is required. |
| `‑‑local` | Flag | Yes | Gets local partition states. One of global or local is required. |
| `‑‑nodes` | Option | No | Names specifying nodes to get partition states from. Case-sensitive, without quotes, all nodes if not set (comma-separated). |
| `‑‑partitions` | Option | No | IDs of partitions to get states. All partitions if not set (comma-separated). |
| `‑‑zones` | Option | No | Names specifying zones to get partition states from. Case-sensitive, without quotes, all zones if not set (comma-separated). |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery partitions states --local --zones=default
```

{% code title="Output" %}
```
╔═══════════╤═════════════════╤══════════════╤═══════════╗
║ Node name │ Zone name       │ Partition ID │ State     ║
╠═══════════╪═════════════════╪══════════════╪═══════════╣
║ node1     │ MYZONE          │ 0            │ AVAILABLE ║
╟───────────┼─────────────────┼──────────────┼───────────╢
║ node1     │ CDC_SYSTEM_ZONE │ 0            │ READ_ONLY ║
╟───────────┼─────────────────┼──────────────┼───────────╢
║ node1     │ MYZONE          │ 1            │ AVAILABLE ║
╟───────────┼─────────────────┼──────────────┼───────────╢
║ node1     │ CDC_SYSTEM_ZONE │ 1            │ READ_ONLY ║
╟───────────┼─────────────────┼──────────────┼───────────╢
║ node1     │ MYZONE          │ 2            │ AVAILABLE ║
╟───────────┼─────────────────┼──────────────┼───────────╢
║ node1     │ CDC_SYSTEM_ZONE │ 2            │ READ_ONLY ║
╟───────────┼─────────────────┼──────────────┼───────────╢
...
╚═══════════╧═════════════════╧══════════════╧═══════════╝
```
{% endcode %}

---

### recovery cluster reset

Initiates recovery of the CMG and/or Metastorage group. This command can be used to recover from a permanent loss of the majority of the corresponding group(s). See the [disaster recovery](administrators-guide/system-groups-recovery.md) documentation for details.

**Syntax**

```
recovery cluster reset [--cluster-management-group=<cmgNodeNames>] [--metastorage-replication-factor=<metastorageReplicationFactor>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑cluster-management-group` | Option | No | Names of nodes that will host the Cluster Management Group (comma-separated) |
| `‑‑metastorage‑replication‑factor` | Option | No | Number of nodes in the voting member set of the Metastorage RAFT group. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery cluster reset
```

{% code title="Output" %}
```
Successfully initiated cluster repair.
```
{% endcode %}

---

### recovery cluster migrate

Migrates nodes missed during repair to repaired cluster.

**Syntax**

```
recovery cluster migrate --old-cluster-url=<oldClusterUrl> --new-cluster-url=<newClusterUrl> [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑old‑cluster‑url` | Option | Yes | URL of old cluster endpoint (nodes of this cluster will be migrated to a new cluster). |
| `‑‑new‑cluster‑url` | Option | Yes | URL of new cluster endpoint (nodes of old cluster will be migrated to this cluster). |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery cluster migrate --old-cluster-url=http://old-cluster:10300 --new-cluster-url=http://new-cluster:10300
```

{% code title="Output" %}
```
Successfully initiated migration.
```
{% endcode %}

---

### recovery tables start

Starts a table point-in-time recovery.

**Syntax**

```
recovery tables start --tables=<tableNames> --timestamp=<timestamp> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑tables` | Option | Yes | Comma-separated fully-qualified table names that will be recovered. |
| `‑‑timestamp` | Option | Yes | Timestamp to create snapshot at in the ISO-8601 format (e.g., 1970-01-01T00:00:00Z). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery tables start --tables=PUBLIC.PERSON,PUBLIC.ORDERS --timestamp=2024-01-01T00:00:00Z
```

{% code title="Output" %}
```
Point-in-time recovery has been started with ID a8675ed4-5171-4245-8c35-a48ffbc5444e
```
{% endcode %}

---

### recovery tables state

View state of a table point-in-time recovery.

**Syntax**

```
recovery tables state --id=<operationId> [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑id` | Option | Yes | ID of the recovery operation. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery tables state --id=15225e58-a045-4d7b-8ebe-b965f99d560c --plain
```

{% code title="Output" %}
```
╔════════╤═══════════════════╤════════╗
║ table  │ recovery progress │ status ║
╠════════╪═══════════════════╪════════╣
║ MYTEST │ 0 rows            │ FAILED ║
╚════════╧═══════════════════╧════════╝
```
{% endcode %}

---

### recovery low-watermark drop-locks

Removes low watermark locks on all cluster nodes that are older than the specified number of milliseconds, so that a stalled low watermark can advance again. By default, the command fails if a read-only transaction older than the cutoff is still active or a secondary storage full state transfer is in progress; use `--force` to remove the locks unconditionally. See the [Recovering a Stalled Low Watermark](administrators-guide/storage/low-watermark.md#recovering-a-stalled-low-watermark) section for details.

**Syntax**

```
recovery low-watermark drop-locks <olderThanMillis> [--force] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `<olderThanMillis>` | Argument | Yes | Remove locks older than this many milliseconds, counting back from now. |
| `‑‑force` | Flag | No | Remove locks even if they are held by active read-only transactions or a secondary storage full state transfer. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
recovery low-watermark drop-locks 3600000
```

{% code title="Output" %}
```
Removed 5 low watermark lock(s) across the cluster.
```
{% endcode %}

---

## User and Role Commands

These commands help you manage access to the system by defining users and roles.

### role create

Creates a new role if it does not exist.

**Syntax**

```
role create [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <roleName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<roleName>` | Argument | Yes | Role name. |

**Example**

```bash
role create myrole
```

{% code title="Output" %}
```
Role myrole created
```
{% endcode %}

---

### role delete

Deletes a role if it exists.

**Syntax**

```
role delete [--with-revoke] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <roleName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑with‑revoke` | Flag | No | Revoke connected roles and users. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<roleName>` | Argument | Yes | Role name. |

**Example**

```bash
role delete --with-revoke myrole
```

{% code title="Output" %}
```
Role myrole deleted
```
{% endcode %}

---

### role list

Lists roles.

**Syntax**

```
role list [--user=<user>] [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑user` | Option | No | Filter by user name. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
role list --user=admin
```

{% code title="Output" %}
```
╔═════════╗
║ role    ║
╠═════════╣
║ system  ║
╟─────────╢
║ analyst ║
╚═════════╝
```
{% endcode %}

---

### role show

Shows role information.

**Syntax**

```
role show [--with-users] [--with-privileges] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <roleName>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑with‑users` | Flag | No | Show role with assigned users. |
| `‑‑with‑privileges` | Flag | No | Show role with granted privileges. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<roleName>` | Argument | Yes | Role name. |

**Example**

```bash
role show --with-users --with-privileges myrole
```

{% code title="Output" %}
```
[role: myrole, users: [myuser], privileges: [CREATE_TABLE]]
```
{% endcode %}

---

### role privilege grant

Grants a privilege to a role.

**Syntax**

```
role privilege grant --to=<roleName> --action=<action> [--on=<object>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑to` | Option | Yes | To role name (comma-separated). |
| `‑‑action` | Option | Yes | Action (comma-separated). |
| `‑‑on` | Option | No | Object. If target object name has no dot(`STATICDATA`), its interpreted as a **schema** name. If it has one dot (`STATICDATA.Customer`), its interpreted as `"SCHEMA"."TABLE"`. Wildcards are not supported, only canonical SQL identifiers are accepted. Use **double quotes** for mixed-case or non-standard identifiers (`"StaticData"."Customer"`). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
role privilege grant --to=myrole --action=CREATE_TABLE
```

{% code title="Output" %}
```
Action CREATE_TABLE granted to role myrole
```
{% endcode %}

---

### role privilege revoke

Revokes a privilege from a role.

**Syntax**

```
role privilege revoke --from=<roleName> --action=<action> [--on=<object>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑from` | Option | Yes | From role (comma-separated). |
| `‑‑action` | Option | Yes | Action (comma-separated). |
| `‑‑on` | Option | No | Object. If target object name has no dot(`STATICDATA`), its interpreted as a **schema** name. If it has one dot (`STATICDATA.Customer`), its interpreted as `"SCHEMA"."TABLE"`. Wildcards are not supported, only canonical SQL identifiers are accepted. Use **double quotes** for mixed-case or non-standard identifiers (`"StaticData"."Customer"`). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
role privilege revoke --from=myrole --action=CREATE_TABLE
```

{% code title="Output" %}
```
Action CREATE_TABLE revoked from role myrole
```
{% endcode %}

---

### user create

Creates a new user if it does not exist.

**Syntax**

```
user create [--password=<password>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <username>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑password` | Option | No | Password. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<username>` | Argument | Yes | Username. |

**Example**

```bash
user create myuser
```

{% code title="Output" %}
```
User myuser created
```
{% endcode %}

---

### user delete

Deletes a user if it exists.

**Syntax**

```
user delete [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <username>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<username>` | Argument | Yes | Username. |

**Example**

```bash
user delete myuser
```

{% code title="Output" %}
```
User myuser deleted
```
{% endcode %}

---

### user edit

Edits a user if it exists.

**Syntax**

```
user edit [--password=<password>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <username>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑password` | Option | No | Password. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<username>` | Argument | Yes | Username. |

**Example**

```bash
user edit --password=newpassword myuser
```

{% code title="Output" %}
```
User myuser edited
```
{% endcode %}

---

### user list

Lists users.

**Syntax**

```
user list [--role=<role>] [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑role` | Option | No | Filter by role name. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
user list
```

{% code title="Output" %}
```
╔══════════╗
║ username ║
╠══════════╣
║ ignite   ║
╟──────────╢
║ alice    ║
╚══════════╝
```
{% endcode %}

---

### user show

Shows user information.

**Syntax**

```
user show [--with-roles] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <username>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑with‑roles` | Flag | No | Show user with assigned roles. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<username>` | Argument | Yes | Username. |

**Example**

```bash
user show myuser
```

{% code title="Output" %}
```
[username: myuser]
```
{% endcode %}

---

### user role assign

Assigns a role to a user.

**Syntax**

```
user role assign --to=<username> --role=<roleName> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑to` | Option | Yes | To username (comma-separated). |
| `‑‑role` | Option | Yes | Role name (comma-separated). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
user role assign --to=myuser --role=myrole
```

{% code title="Output" %}
```
Role myrole assigned to user myuser
```
{% endcode %}

---

### user role revoke

Revokes a role from a user.

**Syntax**

```
user role revoke --from=<username> --role=<roleName> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑from` | Option | Yes | From username (comma-separated). |
| `‑‑role` | Option | Yes | Role name (comma-separated). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
user role revoke --from=myuser --role=myrole
```

{% code title="Output" %}
```
Role myrole revoked from user myuser
```
{% endcode %}

---

## Data Center Replication Commands

These commands help you manage data center replication.

### dcr create

Creates data center replication.

**Syntax**

```
dcr create [--plain] --name=<name> --source-cluster-address=<sourceClusterAddresses> [--replication-nodes=<replicationNodes>] --username=<username> --password=<password> [--keyStorePath=<keyStorePath>] [--keyStorePassword=<keyStorePassword>] [--trustStorePath=<trustStorePath>] [--trustStorePassword=<trustStorePassword>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑name` | Option | Yes | The unique name of the replication. Should be without whitespaces. |
| `‑‑source‑cluster‑address` | Option | Yes | Comma-separated list of client addresses of the cluster that is a source cluster for the replication. |
| `‑‑replication‑nodes` | Option | No | Comma-separated replication nodes names, worker node will be chosen from the list of replication nodes. |
| `‑‑username` | Option | Yes | Username. |
| `‑‑password` | Option | Yes | Password |
| `‑‑keyStorePath` | Option | No | Key store path for SSL/TLS. |
| `‑‑keyStorePassword` | Option | No | Key store password for SSL/TLS. |
| `‑‑trustStorePath` | Option | No | Trust store path for SSL/TLS. |
| `‑‑trustStorePassword` | Option | No | Trust store password for SSL/TLS. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr create --name=myreplication --source-cluster-address=localhost:10300 --username=admin --password=password
```

{% code title="Output" %}
```
 name:        myreplication
 status:      STOPPED
 from:        dc1
 to:          gg9-2
 schema:      null
 tables:      []
 worker node: defaultNode
 fst progress:0%
 errors:      []
```
{% endcode %}

---

### dcr delete

Deletes data center replication.

**Syntax**

```
dcr delete --name=<nameOption> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Replication name. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr delete --name=myreplication
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### dcr flush

Sets replication flush point with provided timestamp.

**Syntax**

```
dcr flush --name=<nameOption> --flush-point=<flushPoint> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Replication name. |
| `‑‑flush‑point` | Option | Yes | The flush point is a timestamp in the ISO-8601 format (e.g., 1970-01-01T00:00:00Z). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr flush --name=myreplication --flush-point=2024-01-01T00:00:00Z
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### dcr list

Lists all replications in the cluster.

**Syntax**

```
dcr list [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr list
```

{% code title="Output" %}
```
╔═══════════════╤══════╤═══════╤═════════╗
║ name          │ from │ to    │ status  ║
╠═══════════════╪══════╪═══════╪═════════╣
║ myreplication │ dc1  │ gg9-2 │ STOPPED ║
╚═══════════════╧══════╧═══════╧═════════╝
```
{% endcode %}

---

### dcr start

Starts data center replication.

**Syntax**

```
dcr start --name=<nameOption> [--schema=<schema>] (--all | --tables=<tableNames>) [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Replication name. |
| `‑‑schema` | Option | No | When used with `--all`, replicates all tables from the specified schema. When used with `--tables`, acts as the default schema for unqualified table names. If omitted when used with `--tables`, unqualified table names default to the `PUBLIC` schema. |
| `‑‑all` | Flag | No | Replicate all tables from all user schemas. When combined with `--schema`, replicates only tables from that schema. Incompatible with `--tables`. One of `--tables` or `--all` is required. |
| `‑‑tables` | Option | No | Comma-separated table names to replicate. Accepts unqualified names (e.g., `ORDERS`) or fully qualified names (e.g., `SCHEMA.TABLE`). Unqualified names use `--schema` as the default schema, or `PUBLIC` if `--schema` is not specified. You can mix qualified and unqualified names in the same list. Incompatible with `--all`. One of `--tables` or `--all` is required. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

Replicate all tables from all schemas:

```bash
dcr start --name=myreplication --all
```

Replicate all tables from a specific schema:

```bash
dcr start --name=myreplication --schema=CUSTOMER1 --all
```

Replicate specific tables from a single schema:

```bash
dcr start --name=myreplication --schema=CUSTOMER1 --tables=ORDERS,PRODUCTS,INVENTORY
```

Replicate specific tables from the `PUBLIC` schema (default when `--schema` is omitted):

```bash
dcr start --name=myreplication --tables=ORDERS,PRODUCTS,INVENTORY
```

Replicate tables from multiple schemas using fully-qualified names, with unqualified names defaulting to `PUBLIC`:

```bash
dcr start --name=myreplication --tables=CUSTOMER1.ORDERS,CUSTOMER2.ORDERS,CONFIG
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### dcr stop

Stops data center replication.

**Syntax**

```
dcr stop --name=<nameOption> [--schema=<schema>] (--all | --tables=<tableNames>) [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Replication name. |
| `‑‑schema` | Option | No | When used with `--all`, stops replication for all tables from the specified schema. When used with `--tables`, acts as the default schema for unqualified table names. |
| `‑‑all` | Flag | No | Stop replication for all tables. When combined with `--schema`, stops only tables from that schema. Incompatible with `--tables`. One of `--tables` or `--all` is required. |
| `‑‑tables` | Option | No | Comma-separated table names to stop replicating. Supports unqualified names (e.g., `ORDERS`) when `--schema` is specified, or fully qualified names (e.g., `SCHEMA.TABLE`) to stop tables from multiple schemas. Incompatible with `--all`. One of `--tables` or `--all` is required. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr stop --name=myreplication --all
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### dcr status

Shows data center replication status.

**Syntax**

```
dcr status --name=<nameOption> [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Replication name. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
dcr status --name=myreplication
```

{% code title="Output" %}
```
 name:        myreplication
 status:      STOPPED
 from:        dc1
 to:          gg9-2
 schema:      null
 tables:      []
 worker node: defaultNode
 fst progress:0%
 errors:      []
```
{% endcode %}

---

## Distribution Commands

These commands help you manage table partition distribution.

### distribution reset

Resets distribution of partitions.

**Syntax**

```
distribution reset --zones=<zoneNames> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑zones` | Option | Yes | Names specifying zones to reset the distribution state in (comma-separated). |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
distribution reset --zones=default
```

{% code title="Output" %}
```
Successfully reset partitions distribution.
```
{% endcode %}

---

### distribution balance-leases

Balances leases across cluster nodes so that each node holds approximately the same number of leases.

The operation is asynchronous: the command initiates lease balancing and returns immediately. Leases are gradually redistributed to alive nodes as they expire and are reassigned, respecting partition assignment constraints.

**Syntax**

```
distribution balance-leases [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
distribution balance-leases
```

{% code title="Output" %}
```
Successfully initiated lease balancing.
```
{% endcode %}

---

### zone datanodes reset

Resets data nodes for distribution zones.

**Syntax**

```
zone datanodes reset [--zone-names=<zoneName>[,<zoneName>...]] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑zone‑names` | Option | No | Comma-separated list of zone names to reset data nodes for. If not specified, resets for all zones. |
| `‑‑url` | Option | No | URL of cluster endpoint. It can be any node URL. If not set, then the default URL from the profile settings will be used. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. This flag is useful for debugging. Specify multiple options to increase verbosity for REST calls. Single option shows request and response, second option (-vv) shows headers, third one (-vvv) shows body. |

**Example**

```bash
zone datanodes reset --zone-names=zone1,zone2
```

{% code title="Output" %}
```
Done
```
{% endcode %}

---

## License Commands

These commands help you manage the license on a running cluster.

### license update

Updates license.

**Syntax**

```
license update [--url=<clusterUrl>] [--profile=<profileName>] [--verbose] <licenseFile>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<licenseFile>` | Argument | Yes | License file. |

**Example**

```bash
license update /path/to/license
```

{% code title="Output" %}
```
License was updated successfully
```
{% endcode %}

---

### license show

Shows license.

**Syntax**

```
license show [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
license show
```

{% code title="Output" %}
```
{"features":["BASIC_AUTH","COLUMNAR_STORAGE","COMPRESSION","COMPUTE","CONTINUOUS_QUERIES","DATA_CENTER_REPLICATION","EVICTION","EXPIRY","EXPLICIT_TRANSACTIONS","EXTENDED_SECONDARY_STORAGE","ICEBERG_CDC","JWT_AUTH","ML_INFERENCE","PERSISTENT_PAGE_MEMORY","POINT_IN_TIME_RECOVERY","RACK_AWARENESS","RBAC","ROCKSDB","ROLLING_UPGRADES","SECONDARY_STORAGE","SNAPSHOTS","SQL","SQL_COPY","VECTOR","VOLATILE_PAGE_MEMORY"],"id":"1c856c46-84b8-4eee-b804-bd7b20ca626f","infos":{"companyName":"GridGain Systems","companyWebsite":"gridgain.com","contractEndDate":"2026-11-11","contractStartDate":"2025-11-10"},"limits":{"expireDate":"2026-11-11","maxNodes":0,"startDate":"2025-11-10"}}
```
{% endcode %}

---

## Rolling Update Commands

These commands help you manage rolling updates for cluster upgrades.

### upgrade start

Starts rolling upgrade process.

**Syntax**

```
upgrade start --version=<version> [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑version` | Option | Yes | New version. For example, 9.1.1. |
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
upgrade start --version=9.1.8
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### upgrade commit

Commits rolling upgrade process.

**Syntax**

```
upgrade commit [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
upgrade commit
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### upgrade cancel

Cancels rolling upgrade process.

**Syntax**

```
upgrade cancel [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
upgrade cancel
```

{% hint style="info" %}
This command produces no output on success.
{% endhint %}

---

### upgrade state

Shows rolling upgrade state.

**Syntax**

```
upgrade state [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
upgrade state
```

{% hint style="info" %}
This command shows the state of a rolling upgrade in progress. It requires a rolling upgrade to be underway.
{% endhint %}

---

## Change Data Capture Commands

These commands help you manage Change Data Capture (CDC) sources, sinks, and replications.

### cdc source create

Creates a CDC source.

**Syntax**

```
cdc source create --name=<name> --type=<type> --tables=<tables> [--parameters=<String=Object>] [--experimental] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC source. |
| `‑‑type` | Option | Yes | Type of the CDC source. |
| `‑‑tables` | Option | Yes | Comma-separated fully-qualified table names that will be parts of the source. |
| `‑‑parameters` | Option | No | Comma-separated key-value pairs of parameters for the source. For example: 'param1=value1, param2=value2'. If not set, then default parameters will be used. |
| `‑‑experimental` | Flag | No | Enables experimental source types, such as `mssql`. Required to create or update a source that uses an experimental type. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc source create --name=mysource --type=jdbc --tables=PUBLIC.PERSON,PUBLIC.ORDERS
```

{% code title="Output" %}
```
Source mysource created.
```
{% endcode %}

---

### cdc source update

Updates a CDC source.

**Syntax**

```
cdc source update --name=<name> --type=<type> --tables=<tables> [--parameters=<String=Object>] [--experimental] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC source. |
| `‑‑type` | Option | Yes | Type of the CDC source. |
| `‑‑tables` | Option | Yes | Comma-separated fully-qualified table names that will be parts of the source. |
| `‑‑parameters` | Option | No | Comma-separated key-value pairs of parameters for the source. For example: 'param1=value1, param2=value2'. If not set, then default parameters will be used. |
| `‑‑experimental` | Flag | No | Enables experimental source types, such as `mssql`. Required to create or update a source that uses an experimental type. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc source update --name=mysource --type=jdbc --tables=PUBLIC.USERS,PUBLIC.ORDERS --url http://localhost:10300
```

{% code title="Output" %}
```
Source mysource updated.
```
{% endcode %}

---

### cdc source delete

Deletes a CDC source.

**Syntax**

```
cdc source delete --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC source. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc source delete --name=mysource
```

{% code title="Output" %}
```
Source mysource deleted.
```
{% endcode %}

---

### cdc source status

Shows CDC source status.

**Syntax**

```
cdc source status --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC source. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc source status --name=mysource
```

{% code title="Output" %}
```
Name:   mysource
Type:   GRIDGAIN
Tables: PUBLIC.PERSON
```
{% endcode %}

---

### cdc source list

Lists CDC sources.

**Syntax**

```
cdc source list [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc source list
```

{% code title="Output" %}
```
Name:   mysource
Type:   GRIDGAIN
Tables: PUBLIC.PERSON
```
{% endcode %}

---

### cdc sink create

Creates a CDC sink.

**Syntax**

```
cdc sink create --name=<name> --type=<type> [--parameters=<String=Object>] [--experimental] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC sink. |
| `‑‑type` | Option | Yes | Type of the CDC sink. |
| `‑‑parameters` | Option | No | Comma-separated key-value pairs of parameters for the sink. For example: 'param1=value1, param2=value2'. If not set, then default parameters will be used. |
| `‑‑experimental` | Flag | No | Enables experimental sink types, such as `gridgain_9`. Required to create or update a sink that uses an experimental type. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc sink create --name=mysink --type=Iceberg
```

{% code title="Output" %}
```
Sink mysink created.
```
{% endcode %}

---

### cdc sink update

Updates a CDC sink.

**Syntax**

```
cdc sink update --name=<name> --type=<type> [--parameters=<String=Object>] [--experimental] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC sink. |
| `‑‑type` | Option | Yes | Type of the CDC sink. |
| `‑‑parameters` | Option | No | Comma-separated key-value pairs of parameters for the sink. For example: 'param1=value1, param2=value2'. If not set, then default parameters will be used. |
| `‑‑experimental` | Flag | No | Enables experimental sink types, such as `gridgain_9`. Required to create or update a sink that uses an experimental type. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc sink update --name=mysink --type=Iceberg
```

{% code title="Output" %}
```
Sink mysink updated.
```
{% endcode %}

---

### cdc sink delete

Deletes a CDC sink.

**Syntax**

```
cdc sink delete --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC sink. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc sink delete --name=mysink
```

{% code title="Output" %}
```
Sink mysink deleted.
```
{% endcode %}

---

### cdc sink status

Shows CDC sink status.

**Syntax**

```
cdc sink status --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC sink. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc sink status --name=mysink
```

{% code title="Output" %}
```
Name: mysink
Type: ICEBERG
```
{% endcode %}

---

### cdc replication create

Creates a CDC replication.

**Syntax**

```
cdc replication create --name=<name> --sink=<sinkName> --source=<sourceName> [--mode=<mode>] [--execution-nodes=<executionNodes>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC replication. |
| `‑‑sink` | Option | Yes | Name of the CDC sink to use for replication. If not set, then the first sink will be used. |
| `‑‑source` | Option | Yes | Name of the CDC source to use for replication. If not set, then the first source will be used. |
| `‑‑mode` | Option | No | Replication mode. Possible values: 'ALL', 'NEW_DATA'. If not set, then 'ALL' mode will be used. |
| `‑‑execution‑nodes` | Option | No | Names of nodes (comma-separated list) that will host the CDC replication. If not set, then a random node will be used. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication create --name=myreplication --sink=mysink --source=mysource --mode=ALL
```

{% code title="Output" %}
```
Replication myreplication created.
```
{% endcode %}

---

### cdc replication delete

Deletes a CDC replication.

**Syntax**

```
cdc replication delete --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC replication. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication delete --name=myreplication
```

{% code title="Output" %}
```
Replication myreplication deleted.
```
{% endcode %}

---

### cdc replication status

Shows CDC replication status.

**Syntax**

```
cdc replication status --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC replication. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication status --name=myreplication
```

{% code title="Output" %}
```
Status ok.
```
{% endcode %}

---

### cdc replication stop

Stops a CDC replication.

**Syntax**

```
cdc replication stop --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC replication. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication stop --name=myreplication
```

{% code title="Output" %}
```
Replication myreplication stopped.
```
{% endcode %}

---

### cdc replication start

Starts a CDC replication.

**Syntax**

```
cdc replication start --name=<name> [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑name` | Option | Yes | Name of the CDC replication. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication start --name=myreplication
```

{% code title="Output" %}
```
Replication myreplication started.
```
{% endcode %}

---

### cdc replication list

Lists CDC replications.

**Syntax**

```
cdc replication list [--plain] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑plain` | Flag | No | Display output with plain formatting. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cdc replication list
```

{% code title="Output" %}
```
Name:   myreplication
Sink:   mysink
Source: mysource
Mode:   NEW_DATA
Status: RUNNING
```
{% endcode %}

---

## JWT Management Commands

These commands help you manage JWT tokens.

### token revoke

Revokes a token.

**Syntax**

```
token revoke [--token=<token>] [--username=<username>] [--url=<clusterUrl>] [--profile=<profileName>] [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑token` | Option | No | Specific token to revoke. |
| `‑‑username` | Option | No | Username to revoke all tokens for. |
| `‑‑url` | Option | No | URL of cluster endpoint. |
| `‑‑profile` | Option | No | Local CLI profile name. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
token revoke --username=admin
```

{% code title="Output" %}
```
All tokens for user admin has been revoked.
```
{% endcode %}

---

## Miscellaneous Commands

These are general-purpose commands.

### connect

Connects to a GridGain 9 node.

**Syntax**

```
connect --username=<username> --password=<password> [--verbose] <nodeUrl>
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑username` | Option | Yes | Username to connect to cluster. |
| `‑‑password` | Option | Yes | Password to connect to cluster. |
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |
| `<nodeUrl>` | Argument | Yes | URL of a node that will be used as a communication endpoint. |

**Example**

```bash
connect --username=admin --password=password http://localhost:10300
```

{% code title="Output" %}
```
Connected to http://localhost:10300
```
{% endcode %}

---

### disconnect

Disconnects from a GridGain 9 node.

**Syntax**

```
disconnect [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
disconnect
```

{% code title="Output" %}
```
Disconnected from http://localhost:10300
```
{% endcode %}

---

### clear

Clears the screen.

**Syntax**

```
clear
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| _None_ |  |  | This command takes no parameters. |

**Example**

```bash
clear
```

{% hint style="info" %}
This command produces no output.
{% endhint %}

---

### cls

Clears the screen.

**Syntax**

```
cls [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
cls
```

{% hint style="info" %}
This command produces no output.
{% endhint %}

---

### exit

Exits the CLI.

**Syntax**

```
exit [--verbose]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `‑‑verbose` | Flag | No | Show additional information: logs, REST calls. |

**Example**

```bash
exit
```

{% hint style="info" %}
This command produces no output.
{% endhint %}

---

### help

Display help information about the specified command.

**Syntax**

```
help [COMMAND]
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `[COMMAND]` | Argument | No | The COMMAND to display the usage help message for. |

**Example**

```bash
help cluster config show
```

{% code title="Output" %}
```
USAGE
ignite cluster config show [OPTIONS] [<selector>]

DESCRIPTION
Shows cluster configuration.

PARAMETERS
      [<selector>]         Configuration selector (dot-separated path).

OPTIONS * - required option
      --url=<clusterUrl>   URL of cluster endpoint.
      --format=<format>    Output format: HOCON or YAML.
      --profile=<profileName>
                           Local CLI profile name.
  -h, --help               Show help for the specified command
  -v, --verbose            Show additional information: logs, REST calls.
```
{% endcode %}

---

### version

Displays the current CLI tool version.

**Syntax**

```
version
```

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| _None_ |  |  | This command takes no parameters. |

**Example**

```bash
version
```

{% code title="Output" %}
```
GridGain CLI version 9.1.127-SNAPSHOT
```
{% endcode %}
