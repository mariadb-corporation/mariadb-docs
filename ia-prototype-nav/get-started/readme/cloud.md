---
title: Cloud
description: >-
  Launch a MariaDB Cloud service, connect to it over TLS, and run the same Python query you ran on your own server.
icon: cloud
---

# Cloud

MariaDB Cloud runs MariaDB for you, on AWS, Google Cloud, or Azure, and takes care of the hardware, patching, backups, and failover. A Serverless service is ready in seconds, and a Provisioned service gives a steady workload its own dedicated capacity. It's the same MariaDB Server you queried from Python on the landing page, so the `shop.products` table and the script move over with two changes: a cloud host and TLS.

## From Sign-Up to a Query Over TLS

{% stepper %}
{% step %}
### Launch a Serverless Service

Sign in at [cloud.mariadb.com](https://cloud.mariadb.com), click **+ Launch New Service**, and pick **MariaDB Serverless Single Node** with a cloud provider and region near you. Every service sits behind a firewall, so add your client's public IP address under **Manage**, then **Security Access**. If you don't know the address, look it up:

```bash
curl -sS checkip.amazonaws.com
```

When the service shows **Healthy**, click **Connect** and copy the host, port, user, and password. [Using the Portal]({mariadb-cloud}/quickstart/using-the-portal) walks through each screen, including Provisioned services.
{% endstep %}

{% step %}
### Connect With the `mariadb` Client

Use the values from the **Connect** dialog. The `--ssl-verify-server-cert` option tells the `mariadb` client to check the server's TLS certificate. With `-p`, the client prompts for the password.

```bash
mariadb --host <host> --port <port> \
  --user <user> -p --ssl-verify-server-cert
```

At the prompt, create the same `shop` database and `products` table as on the landing page:

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

[Connect using MariaDB Client]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-using-mariadb-cli) has install steps for the `mariadb` client on macOS, Linux, and Windows.
{% endstep %}

{% step %}
### Query It From Python

The script from the landing page needs the cloud host and port, plus `ssl_verify_cert=True`. MariaDB Connector/Python 1.1 leaves certificate checks off unless you turn them on:

```python
import mariadb

conn = mariadb.connect(
    host="<host>",
    port=3306,
    user="<user>",
    password="<password>",
    database="shop",
    ssl_verify_cert=True,
)
cur = conn.cursor()
cur.execute("SELECT name, price FROM products WHERE price < ?", (50,))

for name, price in cur:
    print(f"{name}: {price}")

conn.close()
```

Replace `3306` with the port from the **Connect** dialog if it differs. [Connect From Python App]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-python-app) adds error handling and connection failover across several hosts.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
A Provisioned service with replicas also has a read-only port, `3307`. Send reporting queries there and keep writes on the read-write port.
{% endhint %}

## Launch From Code

Use the API or Terraform when databases come from a pipeline instead of the portal.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Launch From the Portal</strong></td><td>Pick a Serverless or Provisioned service, a provider, and a region, then watch it come up on the Dashboard.</td><td><a href="{mariadb-cloud}/quickstart/using-the-portal">using-the-portal</a></td></tr><tr><td><strong>Launch From Python</strong></td><td>Create an API key, set the IP allowlist, and provision a service with one script against the MariaDB Cloud API.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-python">launch-db-using-python</a></td></tr><tr><td><strong>Launch With Terraform</strong></td><td>Define a service in <code>main.tf</code> and manage its lifecycle with <code>terraform apply</code>.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-the-terraform-provider">launch-db-using-the-terraform-provider</a></td></tr></tbody></table>

## Connect and Stay Up

The MariaDB connectors and common SQL clients connect to MariaDB Cloud, and a replicated topology keeps your application online through the loss of a node.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Connection Settings</strong></td><td>The firewall, the <strong>Connect</strong> dialog, and the connectors and GUI clients tested against MariaDB Cloud.</td><td><a href="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connection-overview">connection-overview</a></td></tr><tr><td><strong>Connect From Java</strong></td><td>Take the details from the portal, open a connection with MariaDB Connector/J, and run a query.</td><td><a href="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-java-app">connect-from-java-app</a></td></tr><tr><td><strong>High Availability</strong></td><td>Move to a replicated topology that keeps serving when a node goes down.</td><td><a href="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology">ha-and-replicated-topology</a></td></tr></tbody></table>

## Bring Your Data In

Load an existing database or a folder of CSV files into the service you launched.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Migrate Your Database</strong></td><td>Run a managed migration through the API, or do it yourself with a logical dump and replication.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr><tr><td><strong>From Amazon RDS</strong></td><td>Move an Amazon RDS for MariaDB instance to MariaDB Cloud.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud">migrating-from-mariadb-rds-to-mariadb-cloud</a></td></tr><tr><td><strong>Import CSV Data</strong></td><td>Turn on <code>local_infile</code> for the service, then load files with <code>LOAD DATA LOCAL INFILE</code> from the <code>mariadb</code> client.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading/import-csv-data">import-csv-data</a></td></tr></tbody></table>
