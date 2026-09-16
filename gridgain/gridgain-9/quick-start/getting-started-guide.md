---
description: >-
  Download, install, and start GridGain 9, then run SQL queries against the
  cluster using the CLI tool.
---

# Getting Started With GridGain 9

This guide shows you how to start working with GridGain. In it, we will download GridGain from the website, install it, start the database and perform some simple SQL queries by using the provided CLI tool.

We will be using the [zip archive](../installation/installing-using-zip.md) to demonstrate how to use GridGain. When using [deb or rpm packages](../installation/deb-rpm.md), or when running GridGain in Docker, some steps may be different.

If you are more comfortable with running the database from Java code, you can try [starting GridGain from code](embedded-mode.md).

## Install GridGain

1. [Download](https://www.gridgain.com/tryfree) GridGain from the website. This archive contains everything related to the GridGain database itself.
2. On the same page, [get a free trial license](https://www.gridgain.com/tryfree).
3. Also from the same page, download the [GridGain command line interface](../ignite-cli-tool.md). This tool is the main way of interacting with GridGain database and will be used in the tutorial
4. Unpack the downloaded archives:

{% tabs %}
{% tab title="Unix" %}
```bash
unzip gridgain9-db-9.1.zip
unzip gridgain9-cli-9.1.zip
```
{% endtab %}

{% tab title="Windows (PowerShell)" %}
```bash
Expand-Archive gridgain9-db-9.1.zip -DestinationPath .
Expand-Archive gridgain9-cli-9.1.zip -DestinationPath .
```
{% endtab %}

{% tab title="Windows (CMD)" %}
```bash
unzip -xf gridgain9-db-9.1.zip
unzip -xf gridgain9-cli-9.1.zip
```
{% endtab %}
{% endtabs %}

Now you should have the `gridgain9-db-9.1` and `gridgain9-cli-9.1` directories that we will be using in this tutorial, and the license file provided via e-mail.

## Start GridGain Node

GridGain is a distributed database, that runs on a collection of *nodes* - GridGain database instances that contain data. When running GridGain, you would typically run multiple nodes - a *cluster*, that shares information and evenly distributes data across its nodes. In this part of the tutorial, we will only run one node, but a later part shows how you can start multiple.

To start a locally running node:

1. Navigate to the `gridgain9-db-9.1` directory.
2. Run the `gridgain9db` script:

{% tabs %}
{% tab title="Linux" %}
```bash
bin/gridgain9db
```
{% endtab %}

{% tab title="Windows" %}
{% hint style="info" %}
You need to install Java in the Bash environment to run GridGain on Windows.
{% endhint %}

```bash
bash bin\gridgain9db
```
{% endtab %}
{% endtabs %}

## Start the GridGain CLI

The primary means of interacting with your nodes and cluster is the [GridGain CLI](../ignite-cli-tool.md). It can connect to a node running on a local or remote machine, and is the main tool that is used to manually configure and manage the database. In this example, we will be connecting to a local node.

To start the GridGain CLI:

1. Navigate to the `gridgain9-cli-9.1` directory.
2. Run the following command:

{% tabs %}
{% tab title="Linux" %}
```bash
bin/gridgain9
```
{% endtab %}

{% tab title="Windows" %}
{% hint style="info" %}
You need to install Java in the Bash environment to run GridGain on Windows.
{% endhint %}

```bash
bash bin\gridgain9
```
{% endtab %}
{% endtabs %}

3. Confirm the connection the CLI tool attempts to establish with the node running on the default URI.
4. If your node is running at a different address, use the `connect` command to connect to the node. For example:

{% tabs %}
{% tab title="Command" %}
```
connect http://127.0.0.1:10300
```
{% endtab %}

{% tab title="Output" %}
```
Connected to http://127.0.0.1:10300
```
{% endtab %}
{% endtabs %}

## Initialize Your Cluster

GridGain database functions as a cluster. Even if you are currently only running a single node, theoretically you could start another node and have it join the already running cluster. When the nodes are started for the first time, they find each other, form the _physical topology_ and wait for the user to start the cluster.

The process of starting a cluster is called _initialization_. When the cluster is initialized, GridGain creates 2 RAFT groups, the cluster management group (nodes responsible for managing cluster operation) and the metastorage group (nodes storing authoritative copy of the cluster's metadata). Once these groups are formed, they validate other nodes in the cluster, which establishes _logical topology_. Once the initialization process is complete, the cluster is ready.

{% hint style="info" %}
[Obtain a license](https://www.gridgain.com/tryfree) to initialize your cluster.
{% endhint %}

To initialize the cluster with the node you have started (see [Start GridGain Node](#start-gridgain-node)), run the following command. Replace `$PATH_TO_LICENSE` with the actual path to the directory where your configuration file is located:

{% tabs %}
{% tab title="Command" %}
```
cluster init --name=sampleCluster --license=$PATH_TO_LICENSE/license.conf
```
{% endtab %}

{% tab title="Output" %}
```
Cluster was initialized successfully
```
{% endtab %}
{% endtabs %}

- The `--license` parameter specifies the path to the license file.
- The `--name` parameter sets the cluster name. It can be changed later with the [`cluster rename`](../ignite-cli-tool.md#cluster-rename) CLI command or the [`cluster/rename`](../developers-guide/rest/rest-api.md#using-http-tools) REST endpoint.

## Run SQL Statements Against the Cluster

Once your cluster has been initialized, you can start working with it. In this tutorial, we will be using the CLI tool to create a table, insert some rows and retrieve data. In most real scenarios you would have a [client](../developers-guide/clients/overview.md) writing data to a cluster and retrieving it, but the CLI tool can still be used for debugging or minor adjustments.

To work with the SQL in CLI:

1. Enter the SQL REPL mode. In this mode, you will have access to SQL hints and command completion:

{% tabs %}
{% tab title="Command" %}
```
sql
```
{% endtab %}

{% tab title="Output" %}
```
sql-cli>
```
{% endtab %}
{% endtabs %}

2. Use the `CREATE TABLE` statement to create a new table:

{% tabs %}
{% tab title="Command" %}
```sql
CREATE TABLE IF NOT EXISTS Person (id int primary key,  city varchar,  name varchar,  age int,  company varchar);
```
{% endtab %}

{% tab title="Output" %}
```
Updated 0 rows.
```
{% endtab %}
{% endtabs %}

3. Fill the table with data using the `INSERT` statement:

{% tabs %}
{% tab title="Command" %}
```sql
INSERT INTO Person (id, city, name, age, company) VALUES (1, 'London', 'John Doe', 42, 'Apache');
INSERT INTO Person (id, city, name, age, company) VALUES (2, 'New York', 'Jane Doe', 36, 'Apache');
```
{% endtab %}

{% tab title="Output" %}
```
Updated 1 rows.
```
{% endtab %}
{% endtabs %}

4. Get all the data you inserted in the previous step:

{% tabs %}
{% tab title="Command" %}
```sql
SELECT * FROM Person;
```
{% endtab %}

{% tab title="Output" %}
```
╔════╤══════════╤══════════╤═════╤═════════╗
║ ID │ CITY     │ NAME     │ AGE │ COMPANY ║
╠════╪══════════╪══════════╪═════╪═════════╣
║ 2  │ New York │ Jane Doe │ 36  │ Apache  ║
╟────┼──────────┼──────────┼─────┼─────────╢
║ 1  │ London   │ John Doe │ 42  │ Apache  ║
╚════╧══════════╧══════════╧═════╧═════════╝
```
{% endtab %}
{% endtabs %}

5. If needed, exit the REPL mode with the `exit` command.

{% hint style="info" %}
For more information about available SQL statements, see the [SQL Reference](../sql-reference/ddl.md) section.
{% endhint %}

## Stop the Node

After you are done working with your cluster, you need to stop the node by stopping the `gridgain9db` process:

- Unix: `Control + C`
- Windows: `Ctrl+C`

You can also exit the CLI tool with the `exit` command.

The cluster will remain initialized, and ready once again when you restart the node.

## Extended Cluster Startup Tutorial

GridGain 9 is designed to work in a cluster of 3 or more nodes at once. While a single node can be used in some scenarios and can be used for the tutorial, having multiple nodes in a cluster is the most common use case. The steps below provide optional alternatives to starting your cluster, in case you want to run the tutorial on multiple nodes in a cluster that is closer to what would be encountered in real scenarios.

### Optional: Starting Multiple GridGain Nodes in Docker

{% hint style="info" %}
Docker installation does not persist data by default, and all data will be lost when the container is deleted. To learn how to persist data, see [Getting Started with GridGain 9 Persistent Storage](../get-started/persist-data.md).
{% endhint %}

To run multiple instances of GridGain, you would normally install it on multiple machines before starting a cluster. If you want to run a GridGain cluster on local VMs for this tutorial, we recommend using a Docker image:

1. Download the [docker-compose](../../.gitbook/assets/gg9-quick-start-docker-compose.yml) file.

   {% hint style="info" %}
   Docker compose version 2.23.1 or later is required to use the provided compose file.
   {% endhint %}
2. Download the Docker image:

{% tabs %}
{% tab title="Command" %}
```bash
docker pull gridgain/gridgain9:9.1
```
{% endtab %}

{% tab title="Output" %}
```
9.1.6: Pulling from gridgain/gridgain9
3713021b0277: Pull complete
fea31cb87980: Pull complete
07f7cfe80ff6: Pull complete
ab1fd3f4849e: Pull complete
34896af28f87: Pull complete
Digest: sha256:43ab9cfb8f58b66e4a5027d4ed529216963d0bcab3fa3fc6d5e2042fa3dd5a74
Status: Downloaded newer image for gridgain/gridgain9:9.1.21
docker.io/gridgain/gridgain9:9.1.21
```
{% endtab %}
{% endtabs %}

3. Run the Docker compose command, providing the previously downloaded compose file:

{% tabs %}
{% tab title="Command" %}
```bash
docker compose -f docker-compose.yml up -d
```
{% endtab %}

{% tab title="Output" %}
```
[+] Running 4/4
 ✔ Network gridgain9_default    Created                                                                            0.8s
 ✔ Container gridgain9-node1-1  Started                                                                            3.2s
 ✔ Container gridgain9-node2-1  Started                                                                            1.7s
 ✔ Container gridgain9-node3-1  Started                                                                            3.4s
```
{% endtab %}
{% endtabs %}

3 nodes start in Docker and become available through the CLI tool that can be run locally.

4. Initialize your cluster before attempting to work with it. Replace `$PATH_TO_LICENSE` with the actual path to the directory where your configuration file is located:

{% tabs %}
{% tab title="Command" %}
```
cluster init --name=sampleCluster --license=PATH_TO_LICENSE/license.conf
```
{% endtab %}

{% tab title="Output" %}
```
Cluster was initialized successfully
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
This tutorial assumes that you are running the CLI tool locally. If you are running it from Docker, make sure to mount a volume for the license.
{% endhint %}

### Optional: Start Multiple GridGain Nodes on Different Hosts

In the examples above, we were running a single node, or a small cluster that used predefined configuration. Creating a GridGain cluster on several hosts involves adjustments to its configuration.

#### List all Nodes in NodeFinder

When nodes are running, they use the node finder configuration. When the node starts, it loads the configuration file from `/etc/gridgain-config.conf`. Add the addresses to the `network.nodeFinder` configuration, for example for the 3-node cluster:

```json
{
  "ignite" : {
    "nodeFinder" : {
      "netClusterNodes" : [
        "localhost:3344",
        "otherhost:3344",
        "thirdhost:3344"
      ]
    }
  }
}
```

Now, when the node starts, it automatically tries to find nodes at the listed addresses. You can see the current configuration of a running node at any point by running the following command from the CLI tool:

{% tabs %}
{% tab title="Command" %}
```
node config show ignite.network.nodeFinder
```
{% endtab %}

{% tab title="Output" %}
```
{
  "netClusterNodes" : [ "localhost:3344", "otherhost:3344", "thirdhost:3344" ],
  "type" : "STATIC"
}
```
{% endtab %}
{% endtabs %}

If the node is already running, you can also use the CLI tool to change node configuration, for example:

```
node config update ignite.network.nodeFinder.netClusterNodes=["localhost:3344", "otherHost:3344"]
```

This change requires the node restart to take effect.

#### Change Node Names

You need to make sure that all nodes in the cluster have different names. Node name is defined in the `/etc/vars.env` file. Change the `NODE_NAME` variable to have unique name for each node in cluster, otherwise it will be impossible for the nodes with conflicting names to enter the same cluster.

#### Start all Nodes

Start each node as described in [Start GridGain Node](#start-gridgain-node).

#### Initialize Your Cluster

Before initializing the cluster, it is important to check that all nodes found each other and can connect into a cluster. Nodes visible to each other, but not necessarily connected into a cluster form [physical topology](../administrators-guide/lifecycle.md). You can check it by connecting to any node using the CLI tool and executing the following command:

{% tabs %}
{% tab title="Command" %}
```bash
cluster topology physical
```
{% endtab %}

{% tab title="Output" %}
```
╔═══════╤════════════╤══════╤═══════════════╤══════════════════════════════════════╗
║ name  │ host       │ port │ consistent id │ id                                   ║
╠═══════╪════════════╪══════╪═══════════════╪══════════════════════════════════════╣
║ node1 │ 172.19.0.4 │ 3344 │ node1         │ 0c61dad3-bc4c-4c60-8772-1a903632dcb4 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node2 │ 172.19.0.2 │ 3344 │ node2         │ 21f516bd-0774-4c53-bbfb-ad21bc21c500 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node3 │ 172.19.0.3 │ 3344 │ node3         │ b2bbfbff-eb08-4252-b154-681c49164708 ║
╚═══════╧════════════╧══════╧═══════════════╧══════════════════════════════════════╝
```
{% endtab %}
{% endtabs %}

The command lists the nodes visible to the node you are connecting to, their addresses, names, and IDs. Once you are certain all nodes are running and visible, initialize your cluster. Replace `$PATH_TO_LICENSE` with the actual path to the directory where your configuration file is located:

{% tabs %}
{% tab title="Command" %}
```bash
cluster init --name=sampleCluster --license=$PATH_TO_LICENSE/license.conf
```
{% endtab %}

{% tab title="Output" %}
```
Cluster was initialized successfully
```
{% endtab %}
{% endtabs %}

Once the cluster starts, the nodes in it will form the _logical topology_. You can check if all nodes have entered the cluster by using the following command:

{% tabs %}
{% tab title="Command" %}
```bash
cluster topology logical
```
{% endtab %}

{% tab title="Output" %}
```
╔═══════╤════════════╤══════╤═══════════════╤══════════════════════════════════════╗
║ name  │ host       │ port │ consistent id │ id                                   ║
╠═══════╪════════════╪══════╪═══════════════╪══════════════════════════════════════╣
║ node1 │ 172.19.0.4 │ 3344 │ node1         │ 0c61dad3-bc4c-4c60-8772-1a903632dcb4 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node2 │ 172.19.0.2 │ 3344 │ node2         │ 21f516bd-0774-4c53-bbfb-ad21bc21c500 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node3 │ 172.19.0.3 │ 3344 │ node3         │ b2bbfbff-eb08-4252-b154-681c49164708 ║
╚═══════╧════════════╧══════╧═══════════════╧══════════════════════════════════════╝
```
{% endtab %}
{% endtabs %}

If all nodes are in the command output, the cluster is now started and can be worked with.

## Next Steps

From here, you may want to:

- Check out the [GridGain CLI Tool](../ignite-cli-tool.md) page for more detail on supported commands
- Try out our [examples](https://github.com/apache/ignite-3/tree/main/examples)
