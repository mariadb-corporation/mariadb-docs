---
title: Server
description: >-
  Get to know MariaDB Community Server, the open source database at the core of MariaDB Enterprise Platform and MariaDB Cloud.
icon: database
---

# Server

MariaDB Community Server is the open source relational database behind the `shop.products` query you ran from Python on the landing page. It speaks standard SQL and the MySQL wire protocol, so existing MySQL clients and drivers connect as they are. It stores tables through pluggable storage engines, with InnoDB as the default, and it handles JSON and native `VECTOR` columns in the same SQL as everything else. The same server is the core of MariaDB Enterprise Platform and MariaDB Cloud, so what you learn here carries over to both.

## Get to Know Your Server

These three steps show you how the server is put together. Run them against the server you started on the landing page.

{% stepper %}
{% step %}
### Look Around

Connect with the `mariadb` command-line client and ask the server what it is, which databases it holds, and which storage engines it can use:

```sql
SELECT VERSION();
SHOW DATABASES;
SHOW ENGINES;
```

The `Support` column of the `SHOW ENGINES` output marks InnoDB as `DEFAULT`, which means every `CREATE TABLE` without an `ENGINE` clause gets an InnoDB table. [A MariaDB Primer]({server}/mariadb-quickstart-guides/mariadb-usage-guide) walks through more of the client.
{% endstep %}

{% step %}
### Give Your Application Its Own User

Your application doesn't need the `root` account. Create a user that can read and change rows in the `shop` database and do nothing else:

```sql
CREATE DATABASE IF NOT EXISTS shop;

CREATE USER 'shop_app'@'localhost' IDENTIFIED BY 'app-password';
GRANT SELECT, INSERT, UPDATE, DELETE ON shop.* TO 'shop_app'@'localhost';

SHOW GRANTS FOR 'shop_app'@'localhost';
```

The `'localhost'` part limits where the user can connect from. If your application reaches the server over the network or from outside a Docker container, use the client's host name or address instead. The [GRANT]({server}/reference/sql-statements/account-management-sql-statements/grant) reference lists every privilege you can give.
{% endstep %}

{% step %}
### Change a Setting That Survives a Restart

Server behavior lives in system variables, and the server reads their startup values from option files such as `/etc/my.cnf`. Add a `[mariadb]` section to raise the connection limit from its default of 151:

```ini
[mariadb]
max_connections = 300
```

Restart the server, then check the value from the `mariadb` client:

```bash
sudo systemctl restart mariadb
```

```sql
SHOW VARIABLES LIKE 'max_connections';
```

A `SET GLOBAL max_connections = 300;` statement changes the value right away, but the server forgets it at the next restart. [Configuring MariaDB with Option Files]({server}/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) explains which files the server reads and in what order.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Running the official Docker image? Put your `.cnf` file in a host directory and mount it at `/etc/mysql/conf.d` when you start the container. The [MariaDB Container Cheat Sheet]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-container-cheat-sheet) has the full command.
{% endhint %}

## Install and Connect

Put the server where it will live, then let clients reach it from other hosts.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install MariaDB Server</strong></td><td>Install from the MariaDB package repository on your platform and secure the fresh install.</td><td><a href="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>Connect With the Client</strong></td><td>Learn the connection options of the <code>mariadb</code> client, from host and port to sockets.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-connecting-guide">mariadb-connecting-guide</a></td></tr><tr><td><strong>Allow Remote Connections</strong></td><td>Change <code>bind-address</code> and create accounts so clients on other machines can connect.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-remote-connection-guide">mariadb-remote-connection-guide</a></td></tr></tbody></table>

## Learn the SQL

Go from single-table statements to the queries applications run every day.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>SQL Basics</strong></td><td>Create databases and tables, then insert, update, and query rows.</td><td><a href="{server}/mariadb-quickstart-guides/basics-guide">basics-guide</a></td></tr><tr><td><strong>Joining Tables</strong></td><td>Combine rows from several tables with <code>INNER JOIN</code>, <code>LEFT JOIN</code>, and <code>CROSS JOIN</code>.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-join-guide">mariadb-join-guide</a></td></tr><tr><td><strong>Essential Queries</strong></td><td>Grouping, maximums per group, and other patterns that come up in most applications.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide">mariadb-advanced-sql-guide</a></td></tr></tbody></table>

## Protect Your Data

Take a backup and restore it once by hand, before the database holds anything you care about.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Back Up a Server</strong></td><td>Dump databases to SQL files with the <code>mariadb-dump</code> tool.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-backup-guide">mariadb-backup-guide</a></td></tr><tr><td><strong>Restore a Server</strong></td><td>Load a dump file back into the server and check the result.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-restore-guide">mariadb-restore-guide</a></td></tr><tr><td><strong>Backup and Restore Overview</strong></td><td>Compare logical and physical backups and pick the tool that fits your data.</td><td><a href="{server}/server-usage/backup-and-restore">backup-and-restore</a></td></tr></tbody></table>
