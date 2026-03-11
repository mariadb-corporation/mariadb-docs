---
description: >-
  A high-level comparison of MariaDB's architecture, including its pluggable
  storage engines, transaction log handling, and buffer pool management versus
  other databases.
---

# Differences Between MariaDB and Other DBMSs

This page lists _general_ differences between MariaDB and other DBMSs (database management systems). For _specific_ differences (for instance, between MariaDB and PostgreSQL), refer to the respective pages in this section.

## Database vs. Schema

In MariaDB, the terms _schema_ and _database_ are synonymous and used interchangeable. The `CREATE SCHEMA` statement is a synonym for `CREATE DATABASE`, meaning they create the same object—a container for database objects like tables and views.

MariaDB does not support a distinction between schema and database as seen in other systems like SQL Server or PostgreSQL, where a schema is a logical container within a database. Instead, a database in MariaDB serves as both a namespace and a logical container to separate objects, and it has a default character set and collation that are inherited by its tables.
