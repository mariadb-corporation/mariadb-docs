---
description: >-
  Run the GridGain 9 CLI in interactive or non-interactive mode, and configure its files, JVM properties, and default parameter values.
---

# Using the CLI Tool

The GridGain CLI communicates with the cluster via the REST API, allowing you to configure the entire cluster or apply node-specific settings. You can run the CLI either in the interactive mode or execute commands without entering it.

## Interactive CLI Mode

To use the CLI in the interactive mode, first [run](../gridgain9-get-started/quick-start.md#start-the-gridgain-cli) it, then configure the [cluster](../reference/configuration/cluster-configuration-parameters.md) or [node](../reference/configuration/node-configuration-parameters.md) using the `update` command.

For example, to add a new user to the cluster:

```bash
cluster config update ignite.security.authentication.providers.default.users=[{username=newuser,displayName=newuser,password="newpassword",passwordEncoding=PLAIN,roles=[system]}]
```

## Non-Interactive CLI Mode

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

## Verbose Output

All CLI commands can provide additional output that can be helpful in debugging. You can specify the `-v` option multiple times to increase output verbosity. Single option shows REST request and response, second option (-vv) shows request headers, third one (-vvv) shows request body.

## CLI Tool Files

CLI tool stores additional files required for its operation on your local machine. These files are required for its normal operation and include defaults, history, logs and secrets. By default, these files are stored in the following locations:

- `~/.local/state/ignitecli/logs` directory contains CLI tool logs;
- `~/.local/state/ignitecli/history` file contains the history of CLI tool commands;
- `~/.config/ignitecli/defaults` file contains the default values to be used for CLI tool configuration for each profile;
- `~/.config/ignitecli/secrets` file contains potentially sensitive information such as passwords and other authorization information.

{% hint style="info" %}
Windows systems the `%USERPROFILE%` address instead of `~` for user home directory.
{% endhint %}

### Configuration

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

## Overriding JVM Properties

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

## Default Parameter Values

Some parameters are optional because the CLI can resolve their values automatically from the profile configuration or the current session state. The `--url` parameter for all `cluster` and `node` commands works this way. This is the only parameter with this resolution behavior.

The resolution order depends on whether the CLI is running in interactive (REPL) or non-interactive mode.

### Non-Interactive Mode

The value for `--url` is resolved in the following order:

1. Explicitly provided value: `--url=<clusterUrl>`.
2. If `--profile=<profileName>` is specified, the `ignite.cluster-endpoint-url` property from the specified CLI profile is used.
3. If neither is provided, or if the specified CLI profile does not define `ignite.cluster-endpoint-url`, the value is taken from the currently active profile.

### Interactive (REPL) Mode

The value for `--url` is resolved in the following order:

1. Explicitly provided value: `--url=<clusterUrl>`.
2. If `--profile=<profileName>` is specified, the `ignite.cluster-endpoint-url` property from the specified CLI profile is used.
3. If no URL was resolved from the previous steps and the CLI is currently connected to a node, the URL of the connected node is used.
4. If no URL was resolved from the previous steps and the CLI is not connected to a node, the value is taken from the currently active profile.
