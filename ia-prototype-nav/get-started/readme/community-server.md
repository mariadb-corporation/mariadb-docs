---
title: Server
description: >-
  MariaDB Community Server runs transactions, JSON, and vector search behind one SQL surface. Tour the open source core of MariaDB Enterprise Platform and MariaDB Cloud.
icon: database
---

# Server

The shop runs. The `shop.products` table answers queries from Python, and before you build orders, carts, and reports on top of it, you want to know the machine you're standing on. That machine is MariaDB Community Server, the open source database that also sits at the core of MariaDB Enterprise Platform and MariaDB Cloud. Everything you learn about it here carries over to both.

The tour has three stops. Open the `mariadb` command-line client against the server from the landing page and follow along.

## Look Around

Start by asking the server what it is and what it holds. The answers come back in a few lines, and they tell you more than a version number.

```sql
SELECT VERSION();
SHOW DATABASES;
SHOW ENGINES;
```

The `SHOW DATABASES` output lists `shop` next to system databases such as `mysql` and `information_schema`, where the server keeps its own bookkeeping. The `SHOW ENGINES` output is the interesting one. Each storage engine stores table data in its own way, and the `Support` column marks InnoDB as `DEFAULT`. That's why the `products` table became an InnoDB table without an `ENGINE` clause, and why it can handle checkout traffic with transactions and row-level locks. [A MariaDB Primer]({server}/mariadb-quickstart-guides/mariadb-usage-guide) walks through more of the client.

## Create an Application User

So far the Python script connects as `root`, which can drop every database on the server. The shop doesn't need that much power, so create a `shop_app` account that can read and change rows in the `shop` database and nothing else.

```sql
CREATE DATABASE IF NOT EXISTS shop;

CREATE USER 'shop_app'@'localhost' IDENTIFIED BY 'app-password';
GRANT SELECT, INSERT, UPDATE, DELETE ON shop.* TO 'shop_app'@'localhost';

SHOW GRANTS FOR 'shop_app'@'localhost';
```

An account in MariaDB is a user name plus a host, so `'shop_app'@'localhost'` only gets in from the server machine itself. When the app runs on another host or outside a Docker container, put that host's name or address after the `@` instead. Point the Python script at the new account, and a bug in the app can no longer drop a table. The [GRANT]({server}/reference/sql-statements/account-management-sql-statements/grant) reference lists every privilege you can give.

## Change a Server Setting

Server behavior lives in system variables, such as the `max_connections` variable, which caps how many clients can connect at once. Its default is 151, and a busy sale with several app workers can use that up. You could run `SET GLOBAL max_connections = 300;`, but the server forgets that value at the next restart, because it reads its startup settings from option files such as `/etc/my.cnf`. Add a `[mariadb]` section there instead.

```ini
[mariadb]
max_connections = 300
```

Restart the server so it reads the file again, then check the value from the `mariadb` client.

```bash
sudo systemctl restart mariadb
```

```sql
SHOW VARIABLES LIKE 'max_connections';
```

[Configuring MariaDB with Option Files]({server}/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) explains which files the server reads and in what order.

{% hint style="info" %}
Running the official Docker image? Put your `.cnf` file in a host directory and mount it at `/etc/mysql/conf.d` when you start the container. The [MariaDB Container Cheat Sheet]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-container-cheat-sheet) has the full command.
{% endhint %}

With the app on its own account and the connection limit in an option file, the server is ready for the next table the shop needs.

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install MariaDB Server</strong></td><td>Install from the MariaDB package repository on your platform and secure the fresh install.</td><td><a href="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>Allow Remote Connections</strong></td><td>Change <code>bind-address</code> and create accounts so the app can connect from another machine.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-remote-connection-guide">mariadb-remote-connection-guide</a></td></tr><tr><td><strong>SQL Basics</strong></td><td>Create databases and tables, then insert, update, and query rows.</td><td><a href="{server}/mariadb-quickstart-guides/basics-guide">basics-guide</a></td></tr><tr><td><strong>Joining Tables</strong></td><td>Combine products with orders using <code>INNER JOIN</code> and <code>LEFT JOIN</code>.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-join-guide">mariadb-join-guide</a></td></tr><tr><td><strong>Back Up a Server</strong></td><td>Dump the <code>shop</code> database to an SQL file with the <code>mariadb-dump</code> tool.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-backup-guide">mariadb-backup-guide</a></td></tr><tr><td><strong>Backup and Restore Overview</strong></td><td>Compare logical and physical backups and pick the tool that fits your data.</td><td><a href="{server}/server-usage/backup-and-restore">backup-and-restore</a></td></tr></tbody></table>
