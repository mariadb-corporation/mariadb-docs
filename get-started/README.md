---
title: Get Started
description: >-
  The unified open database for the agentic enterprise. Start MariaDB with your coding agent, Docker, Linux, MariaDB Cloud, or Kubernetes, then query it from Python.
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

MariaDB gives your applications and agents one durable place for their data: a single source of truth that scales with your workload, runs anywhere, and is built on curated open source. These docs cover MariaDB Server, both Community and Enterprise, plus the MariaDB Platform components that extend it.

<figure><picture><source srcset=".gitbook/assets/get-started-orientation-dark.svg" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/get-started-orientation-light.svg" alt="Run it anywhere. Your code stays the same. Your application connects through a MariaDB connector, and your coding agent connects through the MariaDB MCP server. Both reach MariaDB Server, Community or Enterprise. MariaDB Server runs on any of four environments. You run it with Docker on your laptop, with Linux on your servers and VMs, or with the operator on your Kubernetes cluster, and MariaDB Enterprise Platform adds MaxScale, Galera Cluster, ColumnStore, Exa, and GridGain to any of these. Or MariaDB runs it for you in MariaDB Cloud. Moving between them changes only the connection settings: host, user, password, and TLS."></picture><figcaption><p>Your code and your agent talk to the same server, wherever it runs.</p></figcaption></figure>

The Get Started pages follow one small online shop. It starts as a single `products` table that an application queries, and it grows into an application account, backups, a replica, and a weekly sales report. The pages are written for the developer who builds that shop, so each step is SQL or code that you run yourself. The people who keep the shop online and the people who report on its sales use the same server, and their part of the story has pages of its own.

{% hint style="info" %}
**Run databases for a team?** As a database administrator, start with [Deployment](deployment.md) to choose where the server runs, then go to [Operations](operations.md) to back it up, restore it, and add a replica. **Report on the data?** As an analyst, go to [Analytics](analytics-overview.md), which moves the shop's sales history into a columnar table and joins it to the live tables in one query.
{% endhint %}

Pick a tab to get a server running, either with your coding agent or by hand. The Get Started pages follow the Docker tab, and each other tab says what changes for you. On Windows or macOS without Docker, install MariaDB Server with the [Windows MSI package]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows) or with [Homebrew on macOS]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-on-macos-using-homebrew), then continue at step 2.

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

1. Use the MariaDB sandbox tools to deploy the latest
   MariaDB version they offer, on port 3310, with root
   password "sandbox". If the port is busy, pick the next
   free port and tell me.
2. Create a database called shop with a products table
   (id, name, price) and add ten rows.
3. In a Python virtual environment, install MariaDB
   Connector/Python with `pip install --pre mariadb`, then
   write a script that prints every product under 50.
   Run it.
4. Show me how to connect to the sandbox with the mariadb
   client. The sandbox has no TLS, so include --skip-ssl.
```

The first run downloads the `mariadb-shell` client and a MariaDB server binary, about 75 to 105 MB in total depending on your platform, and the sandbox runs natively, so you don't need Docker. The `--pre` flag installs the MariaDB Connector/Python 2.0 release candidate, which needs no C library, so it suits a sandbox. Step 3 below uses the GA release for application code. The sandbox doesn't include the `mariadb` command-line client, so install it from the Linux tab or your package manager. Using Codex, Pi, Hermes Agent, or OpenCode? The [MariaDB AI plugins README](https://github.com/mariadb/ai-plugins) has the install steps for each.

The prompt creates the `shop` database with ten products of its own, so skip step 2 below, and use port `3310` and the password `sandbox` in step 3.
{% endtab %}

{% tab title="Docker" %}
```bash
docker run -d --name mariadb -p 3306:3306 \
  -e MARIADB_ROOT_PASSWORD=changeme \
  mariadb:lts

until docker exec mariadb healthcheck.sh --connect >/dev/null 2>&1; do
  sleep 2
done

docker exec -it mariadb mariadb -uroot -pchangeme
```

This runs the [official MariaDB image](https://hub.docker.com/_/mariadb) from Docker Hub. On first start, the container spends a few seconds creating its data directory, so the `until` loop waits for the image's `healthcheck.sh` script to report that the server accepts connections. For volumes, configuration, and the other environment variables, see [Installing and Using MariaDB via Docker]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker).
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

A package install gives `root` no password. The `root` account signs in through Unix socket authentication, so open the client with `sudo mariadb`, and run the step 3 script after the [Server](choose-your-path/community-server.md) page creates the `shop_app` account.
{% endtab %}

{% tab title="Cloud" %}
1. Sign in at [cloud.mariadb.com](https://cloud.mariadb.com) and launch a **Serverless** service. It's ready in seconds.
2. Click **Manage** on the service, choose **Manage allowlist**, and add your IP address. A new service blocks all external traffic until you do.
3. Click **Connect** on the service and copy the host, port, user, and password.
4. Connect:

```bash
mariadb --host <host> --port <port> \
  --user <user> -p --ssl-verify-server-cert
```

The [MariaDB Cloud quickstart]({mariadb-cloud}/quickstart/using-the-portal) walks through each screen, and [Configuring Firewall]({mariadb-cloud}/security/configuring-firewall) covers the allowlist.

In steps 2 and 3, use the host, port, user, and password from the **Connect** dialog, and turn on TLS in the script with `ssl_verify_cert=True`. The [Cloud](choose-your-path/cloud.md) page shows the full script.
{% endtab %}

{% tab title="Kubernetes" %}
```bash
kubectl create secret docker-registry mariadb-enterprise \
  --docker-server=docker.mariadb.com \
  --docker-username=<email> \
  --docker-password=<customer-download-token>

helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator-crds \
  mariadb-enterprise-operator/mariadb-enterprise-operator-crds
helm install mariadb-enterprise-operator \
  mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

The MariaDB Enterprise Kubernetes Operator is part of MariaDB Enterprise Platform. It pulls images from `docker.mariadb.com` with your Customer Download Token, which the `mariadb-enterprise` secret holds. The `values.yaml` file names that secret under `imagePullSecrets`. See [Install the operator with Helm]({tools}/enterprise/mariadb-enterprise-operator/installation/helm).

The operator alone runs no database yet. Before step 2, create a `MariaDB` resource as the Kubernetes tab on the [Deployment](deployment.md) page shows.
{% endtab %}
{% endtabs %}

## From Install to Your First Query

Three steps take you from a running server to rows coming back in Python.

{% stepper %}
{% step %}
### Run MariaDB Server

Use the Docker tab above to follow along page by page, or another tab with the change it notes. Deciding where to run it in production? [Deployment](deployment.md) walks through the options.
{% endstep %}

{% step %}
### Create Some Data

Open the `mariadb` client and run:

```sql
CREATE DATABASE IF NOT EXISTS shop;

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

This example uses Python. MariaDB has connectors for Node.js, Java, C#, C++, and more, listed under [Connect From Your Language](#connect-from-your-language).

Install MariaDB Connector/Python:

```bash
pip install mariadb
```

The current GA release, MariaDB Connector/Python 1.1, builds against MariaDB Connector/C 3.3.1 or later, so install Connector/C first if your system doesn't have it. Then run:

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

On the sandbox, use port `3310` and the password `sandbox`. The [Python connector quickstart]({connectors}/connectors-quickstart-guides/connector-python-guide) picks up from here with transactions, connection pools, and error handling.
{% endstep %}
{% endstepper %}

## Keep Your Agent in the Docs

{% columns %}
{% column %}
This documentation is also a Model Context Protocol (MCP) server, which is how coding agents reach tools and data outside the editor. Add it once, and your agent can search and read current MariaDB docs while it works with you, so it stops guessing at syntax.
{% endcolumn %}

{% column %}
```bash
claude mcp add --transport http mariadb-docs \
  https://mariadb.com/docs/~gitbook/mcp
```
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
**Already running MariaDB?** The [Server]({server}) docs cover administration and the full SQL reference. For MaxScale, clustering, and analytics, head to [MariaDB Platform]({platform}).
{% endhint %}

## Build With MariaDB

Jump to a feature, find the connector for your language, or clone a sample app and run it.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>AI and Vector Search</strong></td><td>Store embeddings in a native <code>VECTOR</code> column and run similarity search in SQL, next to the rest of your data.</td><td><a href="{server}/reference/sql-structure/vectors/vector-overview">vector-overview</a></td></tr><tr><td><strong>JSON</strong></td><td>Keep flexible documents in the same tables as relational data, and query both with one statement.</td><td><a href="{server}/reference/sql-functions/special-functions/json-functions">json-functions</a></td></tr><tr><td><strong>Temporal Tables</strong></td><td>Let the database keep every version of a row, then query your data as it was at any point in time.</td><td><a href="{server}/reference/sql-structure/temporal-tables/system-versioned-tables">system-versioned-tables</a></td></tr><tr><td><strong>Modern SQL</strong></td><td>Recursive and non-recursive common table expressions, window functions, and sequences, for queries that go past a basic <code>SELECT</code>.</td><td><a href="{server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions">common-table-expressions</a></td></tr><tr><td><strong>Columnar Analytics</strong></td><td>Load operational data into ColumnStore tables in the same database, and run analytical queries there instead of in a separate warehouse.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide">mariadb-columnstore-guide</a></td></tr><tr><td><strong>Sample Apps</strong></td><td>Open source apps on GitHub, from to-do lists to RAG, in Python, Node.js, Java, .NET, and C++.</td><td><a href="https://github.com/mariadb-developers">mariadb-developers</a></td></tr></tbody></table>

### Connect From Your Language

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python</strong></td><td>MariaDB Connector/Python</td><td><a href="{connectors}/connectors-quickstart-guides/connector-python-guide">connector-python-guide</a></td></tr><tr><td><strong>Node.js</strong></td><td>MariaDB Connector/Node.js</td><td><a href="{connectors}/connectors-quickstart-guides/connector-node.js-guide">connector-node.js-guide</a></td></tr><tr><td><strong>Java</strong></td><td>MariaDB Connector/J</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide">mariadb-connector-j-guide</a></td></tr><tr><td><strong>PHP</strong></td><td>PHP's MySQL extensions</td><td><a href="{connectors}/other/mariadb-php-connectors-guide">mariadb-php-connectors-guide</a></td></tr><tr><td><strong>C# and .NET</strong></td><td>MariaDB Connector/NET</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-net-guide">mariadb-connector-net-guide</a></td></tr><tr><td><strong>C++</strong></td><td>MariaDB Connector/C++</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-c++-guide">mariadb-connector-c++-guide</a></td></tr></tbody></table>

## Pick a Path

Each path is a page that walks through one job in order and links to the docs you need along the way.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Build an AI Application</strong></td><td>Store and search vectors, connect your AI framework, and give an agent access to the database.</td><td><a href="ai.md">ai.md</a></td></tr><tr><td><strong>Develop an Application</strong></td><td>Connect from your language, write the SQL, and build the schema out from there.</td><td><a href="development.md">development.md</a></td></tr><tr><td><strong>Analyze Your Data</strong></td><td>Run analytics at scale with ColumnStore and Exa, and pick the right storage engine for each reporting table.</td><td><a href="analytics-overview.md">analytics-overview.md</a></td></tr><tr><td><strong>Move to MariaDB</strong></td><td>See what's different, then bring your schema and data over from MySQL, PostgreSQL, or Amazon RDS.</td><td><a href="migration.md">migration.md</a></td></tr><tr><td><strong>Deploy MariaDB</strong></td><td>Install from packages, run on Kubernetes with the operator, or launch a managed service on MariaDB Cloud.</td><td><a href="deployment.md">deployment.md</a></td></tr><tr><td><strong>Run It in Production</strong></td><td>Back up and restore, run clustered and routed topologies, and tune performance. For courses and certification, see <a href="https://learn.mariadb.com">MariaDB University</a>.</td><td><a href="operations.md">operations.md</a></td></tr></tbody></table>

## Get Help

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Community</strong></td><td>Ask questions and meet the people who build MariaDB on mariadb.org and the <a href="https://mariadb.zulipchat.com">MariaDB Zulip</a> chat.</td><td><a href="https://mariadb.org">mariadb.org</a></td></tr><tr><td><strong>Report a Bug</strong></td><td>File bugs and feature requests for MariaDB Server, the connectors, and MaxScale in MariaDB Jira.</td><td><a href="https://jira.mariadb.org">jira.mariadb.org</a></td></tr><tr><td><strong>Get Support</strong></td><td>Support for MariaDB Cloud and MariaDB Enterprise Platform customers.</td><td><a href="https://mariadb.com/services/">mariadb.com/services</a></td></tr></tbody></table>
