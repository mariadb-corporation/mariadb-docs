---
description: >-
  Connect to a cluster, execute SQL, and manage cluster state using the GridGain 9 command-line interface.
---

# How to Work With the GridGain CLI

## Prerequisites

- A running 3-node cluster ([How to Start a Cluster with Docker Compose](installation/start-cluster-docker-compose.md))
- The GridGain CLI installed on your machine. Install it as described in [Installing Using ZIP](installation/installing-using-zip.md) and add the `bin/` directory to your PATH. Alternatively, use the CLI bundled inside the server Docker image via `docker exec`.

## Overview

This guide walks you through the GridGain CLI from first connection to cluster inspection. You will:

- Connect to a running cluster from the REPL and in non-interactive mode.
- Run SQL interactively and from files.
- Check cluster health with management commands.
- Format output for scripts and measure query timing.
- Create and switch between CLI profiles.

By the end, you have a working command-line workflow for the tasks that come up every day during development: loading schemas, verifying data, and checking that your cluster is healthy.

## Learn the Two-port Model

Before you type a single command, internalize this. The CLI talks to your cluster over two different ports, and every "connection failed" error you encounter comes down to using the wrong one.

| Port | Protocol | CLI flag | What it does |
|------|----------|----------|--------------|
| 10300 | REST (HTTP) | `--url` | Cluster management: `connect`, `cluster status`, `node version`, configuration |
| 10800 | JDBC | `--jdbc-url` | SQL execution: queries, file loading, interactive sessions |

Port 10300 handles administration. Port 10800 handles data. The CLI uses REST internally for every management command and opens a JDBC connection when you run SQL.

The good news: after you `connect` to a node's REST port, the CLI discovers the JDBC port automatically by calling the node info REST endpoint. You only need to remember one URL.

## Connect to a Cluster

### Interactive Mode (REPL)

Start the CLI with no arguments:

```bash
gridgain9
```

The CLI shows a startup banner. If you have connected before, it offers to reconnect to the last node. Connect to the first node in your cluster:

```
[disconnected]> connect http://localhost:10300
Connected to http://localhost:10300
[node1]>
```

The prompt changes from red `[disconnected]>` to green `[node1]>`. That node name comes from the REST API: the CLI called `GET /management/v1/node/info`, retrieved the node name and JDBC port, and stored both for the session. If the connection drops later, the prompt turns yellow as a warning.

### Non-interactive Mode

Pass the command directly to run it and exit:

```bash
gridgain9 cluster status --url http://localhost:10300
```

```
[name: gridgain9-reference-cluster, nodes: 3, status: active, cmgNodes: [node1, node2, node3], msNodes: [node1, node2, node3]]
```

The process exits after the command completes and returns the exit code to the calling shell, which makes it suitable for scripts and CI/CD pipelines.

{% hint style="success" %}
**Checkpoint:** After connecting, the prompt shows `[node1]>` in green. If you see `Node unavailable`, verify your cluster is running and port 10300 is accessible.
{% endhint %}

## Execute SQL Interactively

Now that you are connected, enter the SQL sub-REPL:

```
[node1]> sql
sql-cli>
```

The prompt changes to `sql-cli>`. The `sql` command is only available after you `connect` to a node. If you see `Unmatched arguments`, you are either not connected or you tried to type a SQL statement directly at the `[node1]>` prompt without entering the SQL sub-REPL first.

This is a nested REPL inside the main one, dedicated to SQL. Type a query and terminate it with a semicolon:

```
sql-cli> SELECT 1 AS col1, 2 AS col2;
╔══════╤══════╗
║ COL1 │ COL2 ║
╠══════╪══════╣
║ 1    │ 2    ║
╚══════╧══════╝
```

Multiline statements work as you would expect. Lines without a trailing semicolon produce a `>` continuation prompt, and the CLI waits for the semicolon before executing:

```
sql-cli> SELECT
>   1 AS col1,
>   2 AS col2;
```

This means you can paste multi-line SQL directly from your editor. The CLI collects the full statement and executes it as a single block.

Exit the SQL REPL to return to the main prompt:

```
sql-cli> exit;
[node1]>
```

For quick one-off queries, skip the SQL sub-REPL entirely. Pass the query as an argument to `sql` from the main prompt:

```
[node1]> sql "SELECT 1 AS id, 'hello' AS greeting"
```

The result prints inline and you stay at the `[node1]>` prompt.

{% hint style="info" %}
The examples in this guide use built-in SQL expressions that work on any cluster. If you have loaded the Music Store dataset from [Start Your Local GridGain 9 Development Cluster](../gridgain9-tutorials/distributed-sql-foundations/start-local-cluster.md), you can also query those tables directly (e.g., `sql "SELECT COUNT(*) FROM Artist"`).
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The `sql-cli>` prompt appears after typing `sql`. Queries return results in Unicode box-drawing tables. `exit;` returns to `[node1]>`.
{% endhint %}

## Execute SQL From Files

Loading SQL from a file is how you set up schemas and seed data. From the main REPL:

```
[node1]> sql --file /path/to/schema.sql
```

Or non-interactively, which is the pattern most tutorials in the [GridGain 9 Tutorials](../gridgain9-tutorials/README.md) use:

```bash
gridgain9 sql --jdbc-url jdbc:ignite:thin://localhost:10800 --file /path/to/schema.sql
```

Each statement in the file produces its own output line. A file that creates a table, inserts two rows, and queries them produces:

```
Updated 0 rows.
Updated 1 rows.
Updated 1 rows.
╔════╤═══════╗
║ ID │ VAL   ║
╠════╪═══════╣
║ 1  │ hello ║
╟────┼───────╢
║ 2  │ world ║
╚════╧═══════╝
```

Three output patterns appear in the result:

- **`Updated 0 rows.`** appears for DDL statements like `CREATE TABLE` and `DROP TABLE`.
- **`Updated N rows.`** appears for `INSERT`, `UPDATE`, and `DELETE`, where `N` is the affected row count.
- **A Unicode box-drawing table** appears for `SELECT` statements.

Two things to know about file loading:

1. **Errors stop execution.** If statement 50 out of 200 fails, statements 51-200 never run. The error message includes a line and column number so you can find the problem in your file.
2. **No progress indicator.** The CLI reads the entire file into memory and passes it to the JDBC driver, which executes statements sequentially. A 15,000-line file takes about 10 seconds and the CLI is silent the entire time. This is normal.

{% hint style="warning" %}
`sql --file` only works from the main REPL (`[node1]>`). Inside the SQL sub-REPL (`sql-cli>`), the CLI interprets `sql --file path` as a SQL statement and returns a parse error.
{% endhint %}

## Inspect Cluster State

The CLI wraps the REST management API for common cluster operations. Every command below has a `curl` equivalent, shown so you can use either approach or automate with scripts.

### Cluster Status

```
[node1]> cluster status
[name: gridgain9-reference-cluster, nodes: 3, status: active, cmgNodes: [node1, node2, node3], msNodes: [node1, node2, node3]]
```

`cmgNodes` are the Cluster Management Group nodes that manage membership. `msNodes` are the Meta Storage nodes that hold cluster metadata. In a typical development cluster, both lists are the same.

```bash
curl -s http://localhost:10300/management/v1/cluster/state | python3 -m json.tool
```

### Cluster Topology

```
[node1]> cluster topology physical
╔═══════╤════════════╤══════╤═══════════════╤══════════════════════════════════════╗
║ name  │ host       │ port │ consistent id │ id                                   ║
╠═══════╪════════════╪══════╪═══════════════╪══════════════════════════════════════╣
║ node1 │ 172.18.0.2 │ 3344 │ node1         │ 2cf874d1-9c83-494b-9628-b3fbbe0ba262 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node2 │ 172.18.0.3 │ 3344 │ node2         │ 0aed0d12-4b60-4ad2-aa0f-5b9112688c30 ║
╟───────┼────────────┼──────┼───────────────┼──────────────────────────────────────╢
║ node3 │ 172.18.0.4 │ 3344 │ node3         │ 5351135e-cc1d-470a-ae55-efa70b627e43 ║
╚═══════╧════════════╧══════╧═══════════════╧══════════════════════════════════════╝
```

Port 3344 is the internal cluster communication port. The `host` column shows Docker-internal IPs; from outside the container you reach these nodes through the mapped ports (10300-10302).

`cluster topology logical` shows only nodes that have joined after initialization. In a healthy cluster, the physical and logical topologies are identical. A node that appears in physical but not logical has not yet joined or was removed.

```bash
curl -s http://localhost:10300/management/v1/cluster/topology/physical | python3 -m json.tool
```

### Node Status and Version

```
[node1]> node status
[name: node1, state: started]
```

```
[node1]> node version
GridGain version <latest GridGain 9 version>, revision <revision>
```

The node info REST endpoint reveals the JDBC port, which is how the CLI auto-derives the JDBC URL after `connect`:

```bash
curl -s http://localhost:10300/management/v1/node/info | python3 -m json.tool
```

```json
{
    "name": "node1",
    "jdbcPort": 10800
}
```

## Format Output for Scripting

The default Unicode box-drawing tables are readable in a terminal but awkward to parse in scripts. Two flags change the output format.

**`--plain`** switches to tab-separated values, which pipes cleanly into `awk`, `cut`, or spreadsheet tools:

```bash
gridgain9 sql --jdbc-url jdbc:ignite:thin://localhost:10800 --plain "SELECT 1 AS id, 'Alice' AS name"
```

```
ID	NAME
1	Alice
```

**`--timed`** appends client-side execution time, useful for measuring query performance during development:

```
Query executed in 27ms (client-side).
```

Both flags work in interactive and non-interactive modes. The line above is what a one-shot `sql` command prints. The interactive SQL shell prints its own timing line, for example `Query executed in 27 ms, 1 rows returned`. Combine them: `--plain --timed` gives you parseable output with timing.

## Configure CLI Profiles

If you work with more than one cluster, profiles let you switch connection settings without retyping URLs. The CLI stores configuration in two files: `~/.config/ignitecli/defaults` for connection settings and `~/.config/ignitecli/secrets` for SSL and credentials. Command history lives in `~/.local/state/ignitecli/`.

Create a profile for a staging cluster:

```
[node1]> cli config profile create staging --copy-from default
[node1]> cli config set ignite.cluster-endpoint-url=http://staging-node:10300
```

Switch to it:

```
[node1]> cli config profile activate staging
```

Profiles store six categories of settings:

- **Default cluster URL** used by `connect` and management commands.
- **JDBC URL** used for SQL execution.
- **Authentication credentials** for clusters with security enabled.
- **SSL configuration** for TLS-protected clusters.
- **Output and display preferences** such as truncation, maximum column width, pager, color scheme, and syntax highlighting. The `--plain` and `--timed` flags apply to a single command and cannot be stored in a profile.
- **SQL page size** controlling how many rows the CLI fetches per round trip.

Run `cli config show` to see all settings in the active profile.

{% hint style="info" %}
Configuration and history are stored on the local filesystem. When running the CLI inside Docker with `--rm`, these files are lost when the container exits. For persistent settings, run the CLI on the host or mount `~/.config/ignitecli` as a Docker volume.
{% endhint %}

## Troubleshooting

<details>
<summary>Unmatched arguments: 'select', '*', 'from', ...</summary>

You typed a SQL statement directly at the `[node1]>` prompt. The main REPL only understands CLI commands like `cluster status` and `node version`. To run SQL, either enter the SQL sub-REPL first with `sql`, then type your query at the `sql-cli>` prompt, or use the inline form: `sql "SELECT * FROM SYSTEM.TABLES"`.

</details>

<details>
<summary>Connection reset</summary>

You pointed a REST command (`--url`) at the JDBC port. Port 10800 speaks the JDBC protocol, not HTTP. Switch to port 10300:

```bash
gridgain9 cluster status --url http://localhost:10300
```

</details>

<details>
<summary>IGN-CLIENT-1: Handshake error [endpoint=localhost/&lt;unresolved&gt;:10300]</summary>

The opposite problem: you pointed a SQL command (`--jdbc-url`) at the REST port. Port 10300 speaks HTTP, not the JDBC thin client protocol. Switch to port 10800:

```bash
gridgain9 sql --jdbc-url jdbc:ignite:thin://localhost:10800 "SELECT 1"
```

</details>

<details>
<summary>Node unavailable. Could not connect to node with URL http://localhost:10300</summary>

The cluster is not running or the port is not reachable. Run `docker compose ps` to check that all three containers show "Up" status. Verify that port 10300 is mapped in your Docker Compose file and not blocked by a firewall.

</details>

<details>
<summary>IGN-SQL-3: Failed to parse query: Non-query expression encountered in illegal context</summary>

A SQL syntax error. The message includes the line and column number. Check for misspelled keywords, missing commas, or unquoted string values.

When this error comes from `sql --file`, execution stopped at that statement. Statements before the error may have committed; statements after it did not run. Fix the error and re-run the file. Use `IF NOT EXISTS` and `IF EXISTS` clauses in DDL to make re-runs safe.

</details>

<details>
<summary>IGN-SQL-4: Failed to validate query. Object 'TABLE_NAME' not found</summary>

The table does not exist in the catalog. Table names are case-insensitive in SQL but stored as uppercase internally. Verify with:

```sql
SELECT * FROM SYSTEM.TABLES;
```

</details>

<details>
<summary>IGN-SQL-4: Failed to validate query. Table with name 'PUBLIC.MY_TABLE' already exists</summary>

Use `CREATE TABLE IF NOT EXISTS` to skip creation when the table is already present, or drop it first with `DROP TABLE IF EXISTS my_table`.

</details>

<details>
<summary>File [/path/to/file.sql] not found</summary>

The file path does not exist or is not readable. If running the CLI inside Docker, the file must exist inside the container. Either `docker cp` the file in or mount it as a volume.

</details>

<details>
<summary>Initialization of node "node1" failed: Init CMG request denied, reason: CMG node names do not match</summary>

The cluster is already initialized with a different configuration. You cannot re-initialize an existing cluster. To start fresh, stop the cluster with `docker compose down -v` (this destroys all data), then bring it back up and initialize again.

</details>

## Related

- [How to Start a Cluster with Docker Compose](installation/start-cluster-docker-compose.md)
- [How to Manage Cluster Lifecycle With the REST API](manage-cluster-lifecycle-rest-api.md)
- [Using the CLI Tool](using-the-cli-tool.md)
- [GridGain CLI Tool Reference](../reference/cli-tool.md)
