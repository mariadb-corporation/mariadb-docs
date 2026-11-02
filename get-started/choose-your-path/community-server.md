---
title: Server
description: >-
  MariaDB Community Server runs transactions, JSON, and vector search behind one SQL surface. Tour the open source edition of MariaDB Server, from storage engines to option files.
icon: database
---

# Server

The shop runs. The `shop.products` table answers queries from Python, and before you build orders, carts, and reports on top of it, you want to know the machine you're standing on. That machine is MariaDB Community Server, the open source edition of MariaDB Server. MariaDB Enterprise Platform is built on MariaDB Enterprise Server instead, and MariaDB Cloud runs Community Server on its Foundation tier and Enterprise Server on its Power and PowerPlus tiers. The accounts, privileges, and option files on this page work the same way in both editions.

The tour has three stops. Open the `mariadb` command-line client against the server from the landing page and follow along.

## Look Around

Start by asking the server what it is and what it holds. The answers come back in a few lines, and they tell you more than a version number. In the `mariadb` command-line client, run:

```sql
SELECT VERSION();
SHOW DATABASES;
SHOW ENGINES;
```

The `SHOW DATABASES` output lists `shop` next to system databases such as `mysql` and `information_schema`, where the server keeps its own bookkeeping. The `SHOW ENGINES` output is the interesting one. Each storage engine stores table data in its own way, and the `Support` column marks InnoDB as `DEFAULT`. That's why the `products` table became an InnoDB table without an `ENGINE` clause, and why it can handle checkout traffic with transactions and row-level locks. [A MariaDB Primer](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-usage-guide) walks through more of the client.

## Create an Application User

So far the Python script connects as `root`, which can drop every database on the server. The shop doesn't need that much power, so create a `shop_app` account that can read and change rows in the `shop` database and nothing else.

```sql
CREATE DATABASE IF NOT EXISTS shop;

CREATE USER 'shop_app'@'%' IDENTIFIED BY 'app-password';
GRANT SELECT, INSERT, UPDATE, DELETE ON shop.* TO 'shop_app'@'%';

SHOW GRANTS FOR 'shop_app'@'%';
```

An account in MariaDB is a user name plus a host, and the `%` wildcard matches any host. The wildcard matters under Docker: the script's connection reaches the container through Docker's network, so the server sees it arrive from the network's gateway address, not from `localhost`. On a server you run yourself, narrow the host to the machine the app runs on, as the [Deployment](../deployment.md) page does.

This example uses Python. MariaDB has [connectors](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L) for Node.js, Java, C#, C++, and more, and each one signs in with the same account. Point the Python script at the new account by changing two lines:

```python
    user="shop_app",
    password="app-password",
```

The script prints the same two products, and a bug in the app can no longer drop a table. The [GRANT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) reference lists every privilege you can give.

## Change a Server Setting

Server behavior lives in system variables, such as the `max_connections` variable, which caps how many clients can connect at once. Its default is 151, and a busy sale with several app workers can use that up. You could run `SET GLOBAL max_connections = 300;`, but the server forgets that value at the next restart, because it reads its startup settings from option files. Put this `[mariadb]` section in an option file, then restart the server so it reads the file again.

```ini
[mariadb]
max_connections = 300
```

Where the file goes and how you restart depend on how you installed the server. Pick your tab.

{% tabs %}
{% tab title="Docker" %}
The image reads option files from `/etc/mysql/conf.d` inside the container. Save the section above as `shop.cnf` on your machine, copy it in, and restart the container:

```bash
docker cp shop.cnf mariadb:/etc/mysql/conf.d/shop.cnf
docker restart mariadb
```

The file lives in the container, so it's gone if you remove the container. For a long-lived setup, keep the file in a host directory and mount it at `/etc/mysql/conf.d`, as the [MariaDB Container Cheat Sheet](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-container-cheat-sheet) shows.
{% endtab %}

{% tab title="Linux" %}
On RHEL and its relatives, add the section to `/etc/my.cnf` or a file in `/etc/my.cnf.d/`. On Debian and Ubuntu, add it to a file in `/etc/mysql/mariadb.conf.d/`, such as `99-shop.cnf`. Then restart the server:

```bash
sudo systemctl restart mariadb
```
{% endtab %}

{% tab title="Windows" %}
The MSI installer creates a `my.ini` file in the `data` folder of the install directory. Add the section to that file, then restart the `MariaDB` service, the installer's default service name, from a command prompt that runs as Administrator:

```powershell
net stop MariaDB
net start MariaDB
```

You can also restart the service from the Services app.
{% endtab %}

{% tab title="macOS" %}
Homebrew's MariaDB reads `/opt/homebrew/etc/my.cnf` on Apple silicon and `/usr/local/etc/my.cnf` on Intel-based Macs. Add the section to that file, then restart the server:

```bash
brew services restart mariadb
```
{% endtab %}
{% endtabs %}

Check the value from the `mariadb` client:

```sql
SHOW VARIABLES LIKE 'max_connections';
```

[Configuring MariaDB with Option Files](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) explains which files the server reads and in what order.

With the app on its own account and the connection limit in an option file, the server is ready for the next table the shop needs.

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install MariaDB Server</strong></td><td>Install with your distribution's package manager on Linux or the <code>.msi</code> installer on Windows, then secure the fresh install.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>Allow Remote Connections</strong></td><td>Change <code>bind-address</code> and create accounts so the app can connect from another machine.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-remote-connection-guide">mariadb-remote-connection-guide</a></td></tr><tr><td><strong>SQL Basics</strong></td><td>Create databases and tables, then insert, update, and query rows.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/basics-guide">basics-guide</a></td></tr><tr><td><strong>Joining Tables</strong></td><td>Combine products with orders using <code>INNER JOIN</code> and <code>LEFT JOIN</code>.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-join-guide">mariadb-join-guide</a></td></tr><tr><td><strong>Back Up a Server</strong></td><td>Dump the <code>shop</code> database to an SQL file with the <code>mariadb-dump</code> tool.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-backup-guide">mariadb-backup-guide</a></td></tr><tr><td><strong>Backup and Restore Overview</strong></td><td>Compare logical and physical backups and pick the tool that fits your data.</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore">backup-and-restore</a></td></tr></tbody></table>
