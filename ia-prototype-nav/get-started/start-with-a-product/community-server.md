---
title: Server
description: >-
  Get started with MariaDB Server, the open source relational database you run
  yourself. Install it, connect a client, and learn the SQL you need to build.
icon: database
---

# Server

MariaDB Server is the open source relational database at the center of the product line. You download it, run it on your own hardware or cloud instances, and manage it yourself, with no contract required. The same server is also the database component inside MariaDB Enterprise Platform under the name MariaDB Enterprise Server, so what you learn here carries over if you later adopt the platform or the managed service.

This page is the first path into Server. It takes you from an empty machine to a running database with data in it, and then points you at the guides you use every day after that. The order below is the order to follow the first time. Later, you can come straight back to any step.

The first step is to install the server and open a client session against it. The installation guide covers the supported operating systems and the package repository that installs come from, so you know your build is genuine and can be upgraded from a known source. Once the server runs, the connection guide shows you how to reach it with the `mariadb` command line client, supply credentials, and confirm the server is answering. That same connection information is what an application driver later uses, so it is worth getting right early.

With a session open, the next step is to learn how the database is used. The basics guide walks you through creating a database, defining tables, and running your first statements. The usage guide builds on that with the everyday operations an application relies on, and the advanced SQL guide moves into joins, subqueries, and the query patterns that real workloads use. You do not need all of this before you write code, but it is the material you return to as your schema grows.

The last step before you trust the database with anything is to learn how to get your data back. The backup guide takes a logical backup, and the restore guide brings it back. Run both once by hand, so the routine is familiar before you need it under pressure. Every production habit you build later rests on this pair.

## Install and connect

{% content-ref url="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide" %}
[Install MariaDB Server]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-connecting-guide" %}
[Connect to MariaDB Server]({server}/mariadb-quickstart-guides/mariadb-connecting-guide)
{% endcontent-ref %}

## Learn the basics

{% content-ref url="{server}/mariadb-quickstart-guides/basics-guide" %}
[MariaDB Basics]({server}/mariadb-quickstart-guides/basics-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-usage-guide" %}
[Using MariaDB Server]({server}/mariadb-quickstart-guides/mariadb-usage-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide" %}
[Advanced SQL]({server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide)
{% endcontent-ref %}

## Protect your data

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-backup-guide" %}
[Back Up a Database]({server}/mariadb-quickstart-guides/mariadb-backup-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-restore-guide" %}
[Restore a Database]({server}/mariadb-quickstart-guides/mariadb-restore-guide)
{% endcontent-ref %}
