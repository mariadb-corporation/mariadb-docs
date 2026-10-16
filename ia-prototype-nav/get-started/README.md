---
title: Get Started
description: >-
  Run MariaDB Server with your coding agent, Docker, a Linux package, MariaDB
  Cloud, or Kubernetes, then go from install to your first query from Python.
icon: rocket
layout:
  width: wide
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
  metadata:
    visible: false
---

# MariaDB Documentation

{% columns %}
{% column %}
MariaDB gives your applications, and the agents you build on them, one durable place for their data. You get a single source of truth that scales with your workload and runs wherever you need it, from a laptop to Kubernetes to MariaDB Cloud. It's all built on curated open source.

**MariaDB Server is the database.** These docs cover both MariaDB Community Server and MariaDB Enterprise Server. When a feature is Enterprise-only, its page tells you.

**MariaDB Platform builds on the server.** MaxScale, Galera Cluster, ColumnStore, Exa, and GridGain add query routing, clustering, analytics, and in-memory caching when your application needs them.

Pick a tab to get a server running. The agent prompt has your coding agent do the setup. The other tabs show you how to do it yourself.
{% endcolumn %}

{% column %}
{% tabs %}
{% tab title="Agent prompt" %}
Add the MariaDB plugin to Claude Code:

```bash
claude plugin marketplace add mariadb/ai-plugins
claude plugin install dev@mariadb
```

Then start Claude Code in your project and paste this:

```
Set up MariaDB for this project.

1. Use the MariaDB sandbox tools to deploy a MariaDB 11.8
   sandbox on port 3310.
2. Create a database called shop with a products table
   (id, name, price) and add ten rows.
3. Write a Python script that connects with MariaDB
   Connector/Python and prints every product under 50.
4. Show me how to connect to the sandbox with the
   mariadb client.
```

The sandbox runs a native MariaDB server binary, so you don't need Docker. Using Codex, Pi, Hermes Agent, or OpenCode? The [MariaDB AI plugins README](https://github.com/mariadb/ai-plugins) has the install steps for each.
{% endtab %}

{% tab title="Docker" %}
```bash
docker run -d --name mariadb -p 3306:3306 \
  -e MARIADB_ROOT_PASSWORD=changeme \
  mariadb:lts

docker exec -it mariadb mariadb -uroot -pchangeme
```

This runs the [official MariaDB image](https://hub.docker.com/_/mariadb) from Docker Hub. For volumes, configuration, and the other environment variables, see [Installing and Using MariaDB via Docker]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker).
{% endtab %}

{% tab title="Linux" %}
```bash
# Debian and Ubuntu
sudo apt install mariadb-server

# RHEL, Rocky Linux, AlmaLinux, Fedora
sudo dnf install mariadb-server
sudo systemctl enable --now mariadb

sudo mariadb
```

Your distribution's package might be a few releases behind. To get the current release, [add the MariaDB package repository]({server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage) first.
{% endtab %}

{% tab title="Cloud" %}
1. Sign in at [cloud.mariadb.com](https://cloud.mariadb.com) and launch a **Serverless** service. It's ready in seconds.
2. Click **Connect** on the service and copy the host, port, user, and password.
3. Connect:

```bash
mariadb --host <host> --port <port> \
  --user <user> -p --ssl-verify-server-cert
```

The [MariaDB Cloud quickstart]({mariadb-cloud}/quickstart/using-the-portal) walks through each screen.
{% endtab %}

{% tab title="Kubernetes" %}
```bash
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator-crds \
  mariadb-enterprise-operator/mariadb-enterprise-operator-crds
helm install mariadb-enterprise-operator \
  mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

The MariaDB Enterprise Kubernetes Operator is part of MariaDB Enterprise Platform. It pulls images with your customer credentials, which go in `values.yaml`. See [Install the operator with Helm]({tools}/mariadb-enterprise-operator/installation/helm).
{% endtab %}
{% endtabs %}
{% endcolumn %}
{% endcolumns %}

## From Install to Your First Query

Three steps take you from a running server to rows coming back in Python.

{% stepper %}
{% step %}
### Run MariaDB Server

Use any tab above. Each one gives you MariaDB Server on a port you can reach. Not sure which one fits? [Choose how to run MariaDB](choose-how-to-run-mariadb.md).
{% endstep %}

{% step %}
### Create Some Data

Open the `mariadb` client and run:

```sql
CREATE DATABASE shop;

CREATE TABLE shop.products (
  id    INT PRIMARY KEY AUTO_INCREMENT,
  name  VARCHAR(100) NOT NULL,
  price DECIMAL(8,2) NOT NULL
);

INSERT INTO shop.products (name, price) VALUES
  ('Desk lamp', 39.00),
  ('Standing desk', 249.00),
  ('Notebook', 4.50);
```

[The MariaDB basics guide]({server}/mariadb-quickstart-guides/basics-guide) covers databases, tables, and your first statements in more depth.
{% endstep %}

{% step %}
### Query It From Python

Install MariaDB Connector/Python:

```bash
pip install mariadb
```

Version 1.1 builds against MariaDB Connector/C 3.3.1 or later, so install Connector/C first if your system doesn't have it. Then run:

```python
import mariadb

conn = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="changeme",
    database="shop",
)
cur = conn.cursor()
cur.execute("SELECT name, price FROM products WHERE price < ?", (50,))

for name, price in cur:
    print(f"{name}: {price}")

conn.close()
```

On the sandbox, the port is `3310`. The [Python connector quickstart]({connectors}/connectors-quickstart-guides/connector-python-guide) picks up from here with transactions, connection pools, and error handling.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Already running MariaDB?** Go to [Server]({server}) for administration and the SQL reference, or to [MariaDB Platform]({platform}) for MaxScale, clustering, and analytics.
{% endhint %}

## Build With MariaDB

Jump to a feature, find the connector for your language, or clone a sample app and run it.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>AI and Vector Search</strong></td><td>Store embeddings in a native <code>VECTOR</code> column and run similarity search in SQL, next to the rest of your data.</td><td><a href="ai.md">ai.md</a></td></tr><tr><td><strong>JSON</strong></td><td>Keep flexible documents in the same tables as relational data, and query both with one statement.</td><td><a href="{server}/reference/sql-functions/special-functions/json-functions">json-functions</a></td></tr><tr><td><strong>Temporal Tables</strong></td><td>Let the database keep every version of a row, then query your data as it was at any point in time.</td><td><a href="{server}/reference/sql-structure/temporal-tables/system-versioned-tables">system-versioned-tables</a></td></tr><tr><td><strong>Modern SQL</strong></td><td>Recursive and non-recursive common table expressions, window functions, and sequences, for queries that go past a basic <code>SELECT</code>.</td><td><a href="{server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions">common-table-expressions</a></td></tr><tr><td><strong>Analytics and HTAP</strong></td><td>Run columnar analytics on live operational data with ColumnStore and Exa.</td><td><a href="analytics.md">analytics.md</a></td></tr><tr><td><strong>Sample Apps</strong></td><td>Open source apps on GitHub, from to-do lists to RAG, in Python, Node.js, Java, .NET, and C++.</td><td><a href="https://github.com/mariadb-developers">mariadb-developers</a></td></tr></tbody></table>

### Connect From Your Language

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python</strong></td><td>MariaDB Connector/Python</td><td><a href="{connectors}/connectors-quickstart-guides/connector-python-guide">connector-python-guide</a></td></tr><tr><td><strong>Node.js</strong></td><td>MariaDB Connector/Node.js</td><td><a href="{connectors}/connectors-quickstart-guides/connector-node.js-guide">connector-node.js-guide</a></td></tr><tr><td><strong>Java</strong></td><td>MariaDB Connector/J</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide">mariadb-connector-j-guide</a></td></tr><tr><td><strong>PHP</strong></td><td>PDO and mysqli</td><td><a href="{connectors}/other/mariadb-php-connectors-guide">mariadb-php-connectors-guide</a></td></tr><tr><td><strong>C# and .NET</strong></td><td>MariaDB Connector/NET</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-net-guide">mariadb-connector-net-guide</a></td></tr><tr><td><strong>C++</strong></td><td>MariaDB Connector/C++</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-c++-guide">mariadb-connector-c++-guide</a></td></tr></tbody></table>

## Pick a Path

Each path is a page that walks through one job in order and links to the docs you need along the way.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Build an AI Application</strong></td><td>Store and search vectors, connect your AI framework, and give an agent access to the database.</td><td><a href="ai.md">ai.md</a></td></tr><tr><td><strong>Develop an Application</strong></td><td>Connect from your language, write the SQL, and build the schema out from there.</td><td><a href="development.md">development.md</a></td></tr><tr><td><strong>Move to MariaDB</strong></td><td>See what's different, then bring your schema and data over from MySQL, PostgreSQL, or Amazon RDS.</td><td><a href="migration.md">migration.md</a></td></tr><tr><td><strong>Run MariaDB in Production</strong></td><td>Install from packages, deploy on Kubernetes, back up, and keep it available. For instructor-built courses and certification, see <a href="https://learn.mariadb.com">MariaDB University</a>.</td><td><a href="deployment.md">deployment.md</a></td></tr></tbody></table>

## Keep Your Agent in the Docs

{% columns %}
{% column %}
This documentation is also an MCP server. Add it once, and your coding agent can search and read current MariaDB docs while it works with you, so it stops guessing at syntax.
{% endcolumn %}

{% column %}
```bash
claude mcp add --transport http mariadb-docs \
  https://mariadb.com/docs/~gitbook/mcp
```
{% endcolumn %}
{% endcolumns %}

## Get Help

* **Community:** [mariadb.org](https://mariadb.org) and the [MariaDB Zulip](https://mariadb.zulipchat.com) chat.
* **Bugs and feature requests:** [MariaDB Jira](https://jira.mariadb.org).
* **Support:** [MariaDB Cloud and Enterprise support](https://mariadb.com/support/).
* **What's new:** [Release notes]({release-notes}).
