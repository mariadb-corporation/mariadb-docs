---
description: >-
  Get started quickly with MariaDB Server using these quickstart guides. Follow
  step-by-step instructions to install, configure, and begin using MariaDB for
  your projects.
icon: rabbit-running
---

# Quickstart Guides

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide" %}
[installing-mariadb-server-guide.md]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Official MariaDB Server install guide: Linux apt/dnf/yum commands, mariadb-secure-installation setup, systemctl status/start checks, Windows .msi installer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-adding-and-changing-data-guide-1" %}
[mariadb-adding-and-changing-data-guide-1.md]({server}/mariadb-quickstart-guides/mariadb-adding-and-changing-data-guide-1)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide provides a walkthrough of the INSERT, UPDATE, and DELETE statements, demonstrating how to add, modify, and remove data in tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide" %}
[mariadb-advanced-sql-guide.md]({server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to perform essential SQL operations such as creating tables, inserting data, and using aggregate functions like MAX, MIN, and AVG.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/basics-guide" %}
[basics-guide.md]({server}/mariadb-quickstart-guides/basics-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB basics guide: connect with mariadb -u/-p/-h, CREATE DATABASE/USE, CREATE TABLE with AUTO_INCREMENT, INSERT/SELECT/UPDATE/DELETE commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-alter-table-guide-1" %}
[mariadb-alter-table-guide-1.md]({server}/mariadb-quickstart-guides/mariadb-alter-table-guide-1)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to modify existing table structures using the ALTER TABLE statement, including adding columns, changing types, and managing indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-connecting-guide" %}
[mariadb-connecting-guide.md]({server}/mariadb-quickstart-guides/mariadb-connecting-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide details how to connect to a MariaDB server using the command-line client, covering options for host, user, password, and protocol.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide" %}
[mariadb-connection-troubleshooting-guide.md]({server}/mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Diagnose and fix common MariaDB Server connection problems, such as "Can't connect to local server" and access-denied errors, with step-by-step troubleshooting.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-datetime-guide" %}
[mariadb-datetime-guide.md]({server}/mariadb-quickstart-guides/mariadb-datetime-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how to work with date and time values in MariaDB, including data types like DATETIME and TIMESTAMP, and useful temporal functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-importing-data-guide" %}
[mariadb-importing-data-guide.md]({server}/mariadb-quickstart-guides/mariadb-importing-data-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to efficiently import data into MariaDB tables from external files using the LOAD DATA INFILE statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/essentials-of-an-index-guide" %}
[essentials-of-an-index-guide.md]({server}/mariadb-quickstart-guides/essentials-of-an-index-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide provides a conceptual overview of database indexes, explaining their purpose, different types, and when to use them for optimization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-indexes-guide" %}
[mariadb-indexes-guide.md]({server}/mariadb-quickstart-guides/mariadb-indexes-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Definitive MariaDB indexes guide: PRIMARY KEY, UNIQUE INDEX, INDEX, FULLTEXT types, CREATE/ALTER TABLE syntax, CREATE INDEX, SHOW INDEX, and EXPLAIN.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-join-guide" %}
[mariadb-join-guide.md]({server}/mariadb-quickstart-guides/mariadb-join-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide introduces the different types of JOINs (INNER, LEFT, RIGHT, CROSS) and demonstrates how to combine data from multiple tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins" %}
[more-advanced-joins.md]({server}/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore complex join scenarios. This guide covers filtering joined data with WHERE clauses, handling dates, and aggregating results from multiple tables for deeper analysis.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-remote-connection-guide" %}
[mariadb-remote-connection-guide.md]({server}/mariadb-quickstart-guides/mariadb-remote-connection-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure MariaDB Server to accept remote connections by setting bind-address, granting privileges for remote users, and opening the right firewall rules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-selecting-data-guide" %}
[mariadb-selecting-data-guide.md]({server}/mariadb-quickstart-guides/mariadb-selecting-data-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide explains the SELECT statement in detail, covering how to retrieve, filter, limit, and sort data from your MariaDB database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-sql-cheat-cheat-guide" %}
[mariadb-sql-cheat-cheat-guide.md]({server}/mariadb-quickstart-guides/mariadb-sql-cheat-cheat-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A quick reference for core SQL statements including DDL (CREATE, DROP), DML (INSERT, UPDATE, DELETE), and TCL (COMMIT, ROLLBACK) commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-sql-debugging-guide" %}
[mariadb-sql-debugging-guide.md]({server}/mariadb-quickstart-guides/mariadb-sql-debugging-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide offers conventions and practical tips for designing SQL queries that are easier to read, understand, and debug.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-string-functions-guide" %}
[mariadb-string-functions-guide.md]({server}/mariadb-quickstart-guides/mariadb-string-functions-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide goes through several built-in string functions in MariaDB, grouping them by similar features, and providing examples of how they might be used.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-restore-guide" %}
[mariadb-restore-guide.md]({server}/mariadb-quickstart-guides/mariadb-restore-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restore MariaDB data from mariadb-dump backup files using the mariadb client, including how to selectively restore a single table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-time-guide" %}
[mariadb-time-guide.md]({server}/mariadb-quickstart-guides/mariadb-time-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide explores MariaDB functions for performing calculations and modifications on date and time values, like DATE_ADD and DATE_SUB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/system-and-status-variables-guide" %}
[system-and-status-variables-guide.md]({server}/mariadb-quickstart-guides/system-and-status-variables-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide indicates where the various system and status variables of MariaDB Server are found.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-backup-guide" %}
[mariadb-backup-guide.md]({server}/mariadb-quickstart-guides/mariadb-backup-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create logical backups of MariaDB databases with the mariadb-dump utility, covering how to back up all databases, specific databases, or individual tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-usage-guide" %}
[mariadb-usage-guide.md]({server}/mariadb-quickstart-guides/mariadb-usage-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A beginner-friendly primer on using the mariadb command-line client to log in, create databases, and execute basic SQL commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-views-guide" %}
[mariadb-views-guide.md]({server}/mariadb-quickstart-guides/mariadb-views-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover how to create and use views to simplify complex queries, restrict data access, and present a specific perspective of your data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/mariadb-quickstart-guides/database-applications" %}
[database-applications]({server}/mariadb-quickstart-guides/database-applications)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This section offers advice on writing and maintaining applications that use databases, covering schema design, code practices, and testing.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
