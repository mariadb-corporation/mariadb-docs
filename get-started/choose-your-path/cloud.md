---
title: Cloud
description: >-
  Run MariaDB Server as a managed service. Launch MariaDB Cloud, connect over TLS, and keep your schema, SQL, and code.
icon: cloud
---

# Cloud

The shop runs on a MariaDB Community Server that you installed yourself, and lately the server takes more of your week than the shop does. A security release lands, so you patch. Somebody asks whether last night's backup restores, so you test it. The disk alert pages you on a Saturday. None of that work ships a feature.

MariaDB Cloud takes those jobs off your list. It runs MariaDB Server on AWS, Google Cloud, or Azure, handles the hardware and backups, and applies patches in a weekly maintenance window. A service launched with replicas also fails over to a replica on its own. [Deployment](../deployment.md) compares who runs what across all three ways to run MariaDB. A Serverless service is ready in seconds and needs no sizing. Because it's the same MariaDB Server, the `shop.products` table and the Python script come along. Only the connection changes: a new host, port, user, and password, and TLS.

## Connect to MariaDB Cloud

{% stepper %}
{% step %}
### Launch a Service

Sign in at [cloud.mariadb.com](https://cloud.mariadb.com), click **+ Launch New Service**, and pick **MariaDB Serverless Single Node** with a cloud provider and the Serverless region nearest your customers. Serverless runs in two regions on each provider, as [Region Choices]({mariadb-cloud}/reference/region-choices) lists. Every service starts behind a firewall that refuses all connections, so add your laptop's public IP address under **Manage**, then **Security Access**. If you don't know the address, ask for it:

```bash
curl -sS checkip.amazonaws.com
```

When the service shows **Healthy**, click **Connect** and copy the host, port, user, and password. [Using the Portal]({mariadb-cloud}/quickstart/using-the-portal) walks through each screen.
{% endstep %}

{% step %}
### Connect Over TLS

Connect with the `mariadb` client and the values from the **Connect** dialog. The `--ssl-verify-server-cert` option makes the client check the server's TLS certificate, so nobody between your laptop and the cloud can pose as your database. With `-p`, the client prompts for the password.

```bash
mariadb --host <host> --port <port> \
  --user <user> -p --ssl-verify-server-cert
```

At the prompt, create the same `shop` database and `products` table you made on your own server:

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

[Connect using MariaDB Client]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-using-mariadb-cli) has install steps for the `mariadb` client on macOS, Linux, and Windows.
{% endstep %}

{% step %}
### Connect From Python

The Python script changes in two ways. The `host`, `port`, `user`, and `password` values come from the **Connect** dialog, and `ssl_verify_cert=True` turns on the certificate check, because MariaDB Connector/Python 1.1 leaves it off until you ask for it.

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

Replace `3306` with the port from the **Connect** dialog if it differs. [Connect From Python App]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-python-app) adds error handling and failover across several hosts.
{% endstep %}
{% endstepper %}

The script prints the desk lamp and the notebook, the same two rows as before, and the backups, the patch schedule, and the Saturday disk alerts now belong to MariaDB Cloud.

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Launch From Python</strong></td><td>Create an API key and provision a service with one script against the MariaDB Cloud API.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-python">launch-db-using-python</a></td></tr><tr><td><strong>Launch With Terraform</strong></td><td>Define the service in <code>main.tf</code> so it comes from your pipeline instead of the portal.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-the-terraform-provider">launch-db-using-the-terraform-provider</a></td></tr><tr><td><strong>Connection Settings</strong></td><td>Read how the firewall and the <strong>Connect</strong> dialog work, and which connectors and GUI clients are tested.</td><td><a href="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connection-overview">connection-overview</a></td></tr><tr><td><strong>High Availability</strong></td><td>Move to a replicated topology that keeps the shop online when a node goes down.</td><td><a href="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology">ha-and-replicated-topology</a></td></tr><tr><td><strong>Migrate Your Database</strong></td><td>Bring the full shop database over with a managed migration or a logical dump.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr><tr><td><strong>Import CSV Data</strong></td><td>Turn on <code>local_infile</code> for the service and load a product catalog with <code>LOAD DATA LOCAL INFILE</code>.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading/import-csv-data">import-csv-data</a></td></tr></tbody></table>
