---
description: >-
  Install the GridGain 9 database and CLI tool from the distributed ZIP
  archives, then start a node.
---

# Installing Using ZIP Archive

## Prerequisites

### Recommended Operating System

{% include "../../.gitbook/includes/prereqs-os.md" %}

### Recommended Java Version

{% include "../../.gitbook/includes/prereqs-java.md" %}

## Version Lifecycle

The information about versioning and lifecycle of GridGain 9 is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## GridGain Package Structure

The GridGain provides 2 archives for the distribution:

- `gridgain9-db-9.1` - this archive contains everything related to the GridGain database, and when unpacked,  the folder where data will be stored by default. You start GridGain nodes from this folder.
- `gridgain9-cli-9.1` - this archive contains the [GridGain CLI tool](../../reference/cli-tool.md). This tool is the main way of interacting with GridGain clusters and nodes.

## Installing GridGain Database

To install the GridGain database, [download](https://www.gridgain.com/tryfree) the database archive from the website and then:

1. Unpack the archive:

{% tabs %}
{% tab title="Unix" %}
```bash
unzip gridgain9-db-9.1.zip && cd gridgain9-db-9.1
```
{% endtab %}

{% tab title="Windows (PowerShell)" %}
```bash
Expand-Archive gridgain9-9.1.zip -DestinationPath . ; cd gridgain9-db-9.1
```
{% endtab %}

{% tab title="Windows (CMD)" %}
```bash
unzip -xf gridgain9-db-9.1.zip & cd gridgain9-db-9.1
```
{% endtab %}
{% endtabs %}

2. Create the `GRIDGAIN_HOME` environment variable with the path to the `gridgain9-db-9.1` folder.

## Starting the Node

Once you have unpacked the archive, you can start the GridGain node:

```bash
bin/gridgain9db
```

By default, the node loads the `etc/gridgain-config.conf` configuration file on startup. You can update it to customize the node configuration, or change the configuration folder in the `etc/vars.env` file.

When the node is started, it will enter the cluster if it is already configured and initialized, or will wait for cluster initialization.

## Installing GridGain CLI Tool

The CLI tool is the primary means of working with the GridGain database. It is not necessary to install on every machine that is running GridGain, as you can connect to the node via REST interface.

To install the GridGain CLI, [download](https://www.gridgain.com/tryfree) the database archive from the website and then unpack it:

{% tabs %}
{% tab title="Unix" %}
```bash
unzip gridgain9-cli-9.1.zip && cd gridgain9-cli-9.1
```
{% endtab %}

{% tab title="Windows (PowerShell)" %}
```bash
Expand-Archive gridgain9-cli-9.1.zip -DestinationPath . ; cd gridgain9-cli-9.1
```
{% endtab %}

{% tab title="Windows (CMD)" %}
```bash
unzip -xf gridgain9-cli-9.1.zip & cd gridgain9-cli-9.1
```
{% endtab %}
{% endtabs %}

## Software Identification

The ZIP archive includes a SWID tag in the `swidtag/` directory inside the unpacked archive.

See [Software Identification](software-identification.md) for details.

## Next Steps

With the GridGain installed, you can proceed with the [Getting Started](../../gridgain9-get-started/quick-start.md) or [use the available APIs](../../gridgain9-usage/table-api.md) immediately.
