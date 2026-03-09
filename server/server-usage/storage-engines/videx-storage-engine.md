---
description: >-
  The VIDEX storage engine is an aggregated, extensible engine suitable for
  what-if analyses in MariaDB. The name is derived from [VI]rtual in[DEX].
---

# VIDEX Storage Engine

{% hint style="info" %}
This storage engine is available from MariaDB 12.3.
{% endhint %}

This document explains how to install and use **VIDEX** with MariaDB, including:

* Installing/enabling the **VIDEX plugin** in MariaDB.
* Running the **VIDEX-Server** (statistics service) as a container.
* Running a one-shot **videx-sync** workflow to build a VIDEX database.
* Comparing `EXPLAIN` between your original schema and the VIDEX schema.

The VIDEX server repository, with more examples and extension points, can be accessed [here](https://github.com/bytedance/videx/). It contains [an example dataset (TPC-H tiny)](https://github.com/bytedance/videx/blob/main/data/tpch_tiny/tpch_tiny.sql.tar.gz).&#x20;

## Prerequisites

* A running MariaDB server you can connect to (the _target_).
* A MariaDB build that includes the `VIDEX` engine plugin (the _MariaDB-VIDEX_).
  * For a quick start, the _target_ MariaDB and _MariaDB-VIDEX_ can be the same instance.
* Docker (to run `VIDEX-Server` and `videx-sync`).

## What is VIDEX

VIDEX is a **virtual/hypothetical index engine** for what-if analysis.

* **Goal**: Evaluate how potential indexes (and optimizer decisions such as join orders) would change query plans _without creating real indexes on production data_.
* **How it works**: VIDEX replays optimizer / handler calls using **statistics** (cardinality, NDV, histograms, etc.) instead of reading table data. Complex statistics computation is offloaded to an external service (**VIDEX-Server**) via HTTP.

In practice, you keep your existing MariaDB schema and data as the _target_, and create a second schema whose tables use `ENGINE=VIDEX`. You then run `EXPLAIN` on both schemas and compare plans.

{% hint style="info" %}
Research note (AI4DB)

Estimating **multi-column joint NDV (Number of Distinct Value)** and **cardinality** is a challenging research problem. You can extend VIDEX by implementing your own estimation models in **VIDEX-Server** to improve accuracy for your workload.
{% endhint %}

## Components and Roles

VIDEX typically involves the following roles:

* **Target MariaDB**: your original database instance and schema (contains real data).
* **MariaDB with VIDEX plugin** (_MariaDB-VIDEX_): a MariaDB instance that has the `VIDEX` storage engine plugin enabled.
  * It can be the _same_ instance as the _target MariaDB_ (common for a quick start).
  * Alternatively, it can be a separate MariaDB instance used only for what-if analysis.
* **VIDEX-Server**: a standalone HTTP service that stores metadata/statistics and answers estimation requests from the VIDEX plugin.

This document focuses on a **docker-based workflow** for `VIDEX-Server` and `videx-sync`, so users can complete the VIDEX end-to-end flow with a few `docker` commands, while the MariaDB server itself is managed by users.

## Prepare Sample Data

You can test VIDEX with the `TPC-H tiny` sample.

1. Download `tpch_tiny.sql.tar.gz` from [here](https://github.com/bytedance/videx/blob/main/data/tpch_tiny/tpch_tiny.sql.tar.gz).
2. Create a database, and import the data (replace `<TARGET_HOST>`, `<TARGET_PORT>`, etc. with your settings:

```bash
mariadb -h<TARGET_HOST> -P<TARGET_PORT> -u<TARGET_USER> -p<TARGET_PASS> \
  -e "CREATE DATABASE tpch_tiny;"

tar -zxf tpch_tiny.sql.tar.gz
mariadb -h<TARGET_HOST> -P<TARGET_PORT> -u<TARGET_USER> -p<TARGET_PASS> \
  -Dtpch_tiny < tpch_tiny.sql
```

## Install and Enable the VIDEX Plugin

Connect to your MariaDB instance and check whether the `VIDEX` engine is available:

```sql
SHOW ENGINES
```

If you see a row for `VIDEX` with `SUPPORT` as `YES` or `DEFAULT`, the engine is available.

## Install and Run VIDEX-Server in Docker

`VIDEX-Server` is a separate service providing statistics/estimation over HTTP, and _MariaDB-VIDEX_ calls it to get statistics information for generating query plans.

### Images

Public images are on Docker Hub: `kangrongme/videx-server:0.2.0`

### Start the Server

Expose container port `5001`:

```bash
docker run -d --name videx-server \
  -p 5001:5001 \
  kangrongme/videx-server:0.2.0
```

When done, the service is reachable under `http://<YOUR_HOST_IP>:5001` .

{% hint style="info" %}
Reachability note

Prefer using a **routable IP address** (your host/server IP) instead of `localhost/127.0.0.1`. This matters because both MariaDB-VIDEX (the plugin) and `videx-sync` need to reach `VIDEX-Server`. If any of them run inside a container, `localhost/127.0.0.1` refers to that container itself (not your host), so the service isn't reachable via `localhost`.
{% endhint %}

## Build the VIDEX Schema

The `VIDEX-Server` image supports two entry point modes:

* `server` (default): start `VIDEX-Server`
* `sync`: run a one-shot workflow to collect metadata from `--target`, then:
  * add metadata to `VIDEX-Server`
  * create virtual tables in `--videx`

### Command Template

```bash
docker run --rm --name videx-sync \
  kangrongme/videx-server:0.2.0 sync \
  --target <TARGET_HOST>:<TARGET_PORT>:<TARGET_DB>:<TARGET_USER>:<TARGET_PASS> \
  [--videx <VIDEX_HOST>:<VIDEX_PORT>:<VIDEX_DB>:<VIDEX_USER>:<VIDEX_PASS>] \
  [--videx_server <VIDEX_SERVER_HOST>:<VIDEX_SERVER_PORT>]
```

Notes:

1. If `--videx` is not specified, a default database `videx_{TARGET_DB}` is created in `--target`.
2. If you run a separate MariaDB-VIDEX instance, pass that instance as `--videx`.
3. If your `VIDEX-Server` is not `<TARGET_HOST>:5001`, pass `--videx_server` explicitly.

### Localhost Failures

Inside a container, `localhost/127.0.0.1` refers to the container itself.

On Linux Docker Engine, you can reach the host via `host.docker.internal` using `--add-host`:

```bash
docker run --rm --name videx-sync \
  --add-host=host.docker.internal:host-gateway \
  kangrongme/videx-server:0.2.0 sync \
  --target host.docker.internal:<PORT>:<DB>:<USER>:<PASS> \
  --videx host.docker.internal:<PORT>:<VIDEX_DB>:<VIDEX_USER>:<VIDEX_PASS> \
  --videx_server host.docker.internal:<VIDEX_SERVER_PORT>
```

However, if _MariaDB-VIDEX_ itself is also running in a container, reachability can become tricky. Using a routable IP is the most robust approach.

## Configure the Plugin

On MariaDB, the VIDEX plugin exposes **session** system variables.

```sql
SHOW VARIABLES LIKE '%videx_server_ip%';
```

Example output:

```
+-----------------+----------------+
| Variable_name   | Value          |
+-----------------+----------------+
| videx_server_ip | 127.0.0.1:5001 |
+-----------------+----------------+
```

* `videx_server_ip`: **critical**. This is the address (`host:port`) that _MariaDB-VIDEX_ uses to call `VIDEX-Server`.

Configure them for your current session before running `EXPLAIN` on `ENGINE=VIDEX` tables (replace `<VIDEX_SERVER_HOST>:<VIDEX_SERVER_PORT>` with your settings):

```sql
SET SESSION videx_server_ip = '<VIDEX_SERVER_HOST>:<VIDEX_SERVER_PORT>';
```

## Quickstart

This section assumes:

* Users already have **one MariaDB instance** running.
* Users want to create the VIDEX schema **in the same instance** (which means “MariaDB-VIDEX == Target MariaDB”).
* MariaDB is running and reachable.
* The routable IP is something like `203.0.113.42` (example only).
* MariaDB is reachable at, for instance, `203.0.113.42:15508` (example only).
* `VIDEX-Server` is reachable at, for instance, `203.0.113.42:5001` (example only).
* The default user/password credentials are: `videx` / `password`.

{% stepper %}
{% step %}
### Start VIDEX-Server

```bash
docker run -d --name videx-server \
  -p 5001:5001 \
  kangrongme/videx-server:0.2.0
```
{% endstep %}

{% step %}
### Build VIDEX schema via videx-sync

```bash
docker run --rm --name videx-sync \
  kangrongme/videx-server:0.2.0 sync \
  --target 203.0.113.42:15508:tpch_tiny:videx:password \
  --videx  203.0.113.42:15508:videx_tpch_tiny:videx:password \
  --videx_server 203.0.113.42:5001
```
{% endstep %}

{% step %}
### Run EXPLAIN on the original schema

Run [`EXPLAIN`](../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) on your original tables:

{% code overflow="wrap" %}
```sql
USE tpch_tiny;
SET SESSION use_stat_tables = NEVER;
EXPLAIN SELECT s_name, count(*) AS numwait FROM supplier, lineitem l1, orders, nation WHERE s_suppkey = l1.l_suppkey AND o_orderkey = l1.l_orderkey AND o_orderstatus = 'F' AND l1.l_receiptdate > l1.l_commitdate AND EXISTS (SELECT * FROM lineitem l2 WHERE l2.l_orderkey = l1.l_orderkey AND l2.l_suppkey <> l1.l_suppkey) AND NOT EXISTS (SELECT * FROM lineitem l3 WHERE l3.l_orderkey = l1.l_orderkey AND l3.l_suppkey <> l1.l_suppkey AND l3.l_receiptdate > l3.l_commitdate) AND s_nationkey = n_nationkey AND n_name = 'IRAQ' GROUP BY s_name ORDER BY numwait DESC, s_name; 
```
{% endcode %}

{% hint style="info" %}
Collecting histograms may change MariaDB’s cardinality estimates (for instance, histogram-based estimates rather than InnoDB index statistics). Since VIDEX aims to simulate InnoDB index engine behavior, users can set `SET SESSION use_stat_tables = NEVER;` to make `EXPLAIN` results more similar between InnoDB and the VIDEX engine.
{% endhint %}

The `EXPLAIN` output for the original schema is:

```sql
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------+-------+----------------------------------------------+
| id | select_type        | table    | type   | possible_keys                                         | key          | key_len | ref                            | rows  | Extra                                        |
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------+-------+----------------------------------------------+
| 1  | PRIMARY            | orders   | ALL    | PRIMARY                                               | <null>       | <null>  | <null>                         | 14944 | Using where; Using temporary; Using filesort |
| 1  | PRIMARY            | l1       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_FK1 | 4       | tpch_tiny.orders.O_ORDERKEY    | 1     | Using where                                  |
| 1  | PRIMARY            | supplier | eq_ref | PRIMARY,SUPPLIER_FK1,idx_S_NATIONKEY_S_SUPPKEY_S_NAME | PRIMARY      | 4       | tpch_tiny.l1.L_SUPPKEY         | 1     |                                              |
| 1  | PRIMARY            | nation   | eq_ref | PRIMARY                                               | PRIMARY      | 4       | tpch_tiny.supplier.S_NATIONKEY | 1     | Using where                                  |
| 1  | PRIMARY            | l2       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_FK1 | 4       | tpch_tiny.orders.O_ORDERKEY    | 1     | Using where; FirstMatch(nation)              |
| 3  | DEPENDENT SUBQUERY | l3       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_UK1 | 4       | tpch_tiny.l1.L_ORDERKEY        | 1     | Using where                                  |
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------+-------+----------------------------------------------+
```
{% endstep %}

{% step %}
### Run EXPLAIN on the VIDEX schema

Run `EXPLAIN` on the VIDEX schema (tables are `ENGINE=VIDEX`):

{% code overflow="wrap" %}
```sql
USE videx_tpch_tiny;
SET SESSION videx_server_ip = '203.0.113.42:5001';
EXPLAIN SELECT s_name, count(*) AS numwait FROM supplier, lineitem l1, orders, nation WHERE s_suppkey = l1.l_suppkey AND o_orderkey = l1.l_orderkey AND o_orderstatus = 'F' AND l1.l_receiptdate > l1.l_commitdate AND EXISTS (SELECT * FROM lineitem l2 WHERE l2.l_orderkey = l1.l_orderkey AND l2.l_suppkey <> l1.l_suppkey) AND NOT EXISTS (SELECT * FROM lineitem l3 WHERE l3.l_orderkey = l1.l_orderkey AND l3.l_suppkey <> l1.l_suppkey AND l3.l_receiptdate > l3.l_commitdate) AND s_nationkey = n_nationkey AND n_name = 'IRAQ' GROUP BY s_name ORDER BY numwait DESC, s_name; 
```
{% endcode %}

The `EXPLAIN` output for the VIDEX schema is:

```
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------------+-------+----------------------------------------------+
| id | select_type        | table    | type   | possible_keys                                         | key          | key_len | ref                                  | rows  | Extra                                        |
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------------+-------+----------------------------------------------+
| 1  | PRIMARY            | orders   | ALL    | PRIMARY                                               | <null>       | <null>  | <null>                               | 14883 | Using where; Using temporary; Using filesort |
| 1  | PRIMARY            | l1       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_FK1 | 4       | videx_tpch_tiny.orders.O_ORDERKEY    | 1     | Using where                                  |
| 1  | PRIMARY            | supplier | eq_ref | PRIMARY,SUPPLIER_FK1,idx_S_NATIONKEY_S_SUPPKEY_S_NAME | PRIMARY      | 4       | videx_tpch_tiny.l1.L_SUPPKEY         | 1     |                                              |
| 1  | PRIMARY            | nation   | eq_ref | PRIMARY                                               | PRIMARY      | 4       | videx_tpch_tiny.supplier.S_NATIONKEY | 1     | Using where                                  |
| 1  | PRIMARY            | l2       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_FK1 | 4       | videx_tpch_tiny.orders.O_ORDERKEY    | 1     | Using where; FirstMatch(nation)              |
| 3  | DEPENDENT SUBQUERY | l3       | ref    | LINEITEM_UK1,LINEITEM_FK1                             | LINEITEM_UK1 | 4       | videx_tpch_tiny.l1.L_ORDERKEY        | 1     | Using where                                  |
+----+--------------------+----------+--------+-------------------------------------------------------+--------------+---------+--------------------------------------+-------+----------------------------------------------+
```

Compare the output between Step 3 and Step 4.
{% endstep %}
{% endstepper %}

## Notes and Best Practices

1. `videx-sync` can be time-consuming on large schemas, because it needs to collect metadata/statistics. The metadata collection method is extensible; the VIDEX source repository also discusses lighter-weight sampling approaches.
2. Networking matters. Since `VIDEX-Server` is often in a container, `localhost/127.0.0.1` may not refer to what you expect. The routable IP is recommended for reachability, as it ensures that both _MariaDB-VIDEX_ and the container can reach it.
