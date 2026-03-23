---
description: >-
  Complete MySQL to MariaDB migration: mysqldump/mysql import steps, SQL syntax
  compatibility, user/privilege migration, and replication configuration.
---

# Migrating to MariaDB from MySQL

MariaDB Server is designed to be a high-performance, drop-in replacement for MySQL. Whether you are moving from legacy versions (5.5, 5.6, 5.7) or modern releases (8.0, 8.4 LTS), this section provides the tools and workflows needed for a successful transition.

## Evaluate Compatibility

{% columns %}
{% column %}
{% content-ref url="mysql-to-mariadb-compatibility-matrix.md" %}
[mysql-to-mariadb-compatibility-matrix.md](mysql-to-mariadb-compatibility-matrix.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Before moving data, understand the technical differences between your current MySQL version and your target MariaDB version. Our Compatibility Matrix covers changes in authentication, SQL syntax, and system variables. It's a detailed reference for DBAs and developers.
{% endcolumn %}
{% endcolumns %}

## Choose Your Migration Path

{% columns %}
{% column %}
{% content-ref url="mysql-to-mariadb-migration-the-master-guide.md" %}
[mysql-to-mariadb-migration-the-master-guide.md](mysql-to-mariadb-migration-the-master-guide.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
The best method for migration depends on your downtime requirements and server architecture. We have consolidated these workflows into a single authoritative guide.

* [MySQL to MariaDB Migration: The Master Guide](mysql-to-mariadb-migration-the-master-guide.md) — Step-by-step instructions for:
  * In-Place Upgrades: Fast, same-server binary swaps.
  * Logical Migrations: Safe, cross-server dump and restore.
  * Cloud & RDS Migrations: Specialized paths for managed environments.
{% endcolumn %}
{% endcolumns %}

## Specialized Migration Scenarios

{% columns %}
{% column %}
{% content-ref url="migration-from-mysql-to-mariadb-cluster-using-replication.md" %}
[migration-from-mysql-to-mariadb-cluster-using-replication.md](migration-from-mysql-to-mariadb-cluster-using-replication.md)
{% endcontent-ref %}

{% content-ref url="migration-from-mysql-to-mariadb-cluster-node-by-node-in-place.md" %}
[migration-from-mysql-to-mariadb-cluster-node-by-node-in-place.md](migration-from-mysql-to-mariadb-cluster-node-by-node-in-place.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Guides for migrating MySQL Galera Cluster to MariaDB Galera Cluster.
{% endcolumn %}
{% endcolumns %}

