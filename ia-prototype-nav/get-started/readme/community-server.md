---
title: Server
description: >-
  Get started with MariaDB Server, the open source database at the center of everything else in these docs. Install it, connect, write SQL, and protect your data.
icon: database
---

# Server

MariaDB Server is the open source relational database at the center of everything else in these docs. It runs on Linux, Windows, and macOS, speaks standard SQL and the MySQL wire protocol, and comes with transactions, replication, JSON, and native vector search built in. Existing MySQL clients, drivers, and admin tools connect to it as they are.

It's also the server inside MariaDB Enterprise Platform and MariaDB Cloud, so nothing you learn here goes to waste if you move to either one later.

## Install and Connect

Get a server running and prove that a client can reach it. The same host, port, user, and password then go into your application.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install MariaDB Server</strong></td><td>Install from the MariaDB repository on your platform and secure the fresh install.</td><td><a href="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>Run in Docker</strong></td><td>Start the official MariaDB image for local development.</td><td><a href="{server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker">installing-and-using-mariadb-via-docker</a></td></tr><tr><td><strong>Connect With the Client</strong></td><td>Open a session with the <code>mariadb</code> command-line client.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-connecting-guide">mariadb-connecting-guide</a></td></tr></tbody></table>

## Learn the Basics

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>SQL Basics</strong></td><td>Create a database and a table, then insert and query rows.</td><td><a href="{server}/mariadb-quickstart-guides/basics-guide">basics-guide</a></td></tr><tr><td><strong>A MariaDB Primer</strong></td><td>Log in, look around, and work with databases from the command line.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-usage-guide">mariadb-usage-guide</a></td></tr><tr><td><strong>Essential Queries</strong></td><td>Joins, grouping, and the query patterns applications depend on.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide">mariadb-advanced-sql-guide</a></td></tr></tbody></table>

## Protect Your Data

Take a backup and restore it once by hand, before the database holds anything you care about.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Back Up a Server</strong></td><td>Take your first backup with the quickstart.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-backup-guide">mariadb-backup-guide</a></td></tr><tr><td><strong>Restore a Server</strong></td><td>Bring a backup back and check the result.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-restore-guide">mariadb-restore-guide</a></td></tr><tr><td><strong>Backup and Restore Overview</strong></td><td>Compare logical and physical backups and pick the tool that fits.</td><td><a href="{server}/server-usage/backup-and-restore">backup-and-restore</a></td></tr></tbody></table>
