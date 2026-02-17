---
description: >-
  Learn how to migrate your existing databases to MariaDB Server. This section
  provides comprehensive guides and best practices for a smooth and successful
  data transfer.
---

# Migrating to MariaDB

{% columns %}
{% column %}
{% content-ref url="differences-between-mariadb-and-other-dbmss.md" %}
[differences-between-mariadb-and-other-dbmss.md](differences-between-mariadb-and-other-dbmss.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
A high-level comparison of MariaDB's architecture, including its pluggable storage engines, transaction log handling, and buffer pool management versus other databases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ddl-export.md" %}
[ddl-export.md](ddl-export.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Learn how to export SQL DDL[^1] to MariaDB from database management systems like Oracle Database, Microsoft SQL Server, MySQL, and IBM DB2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="moving-from-mysql/" %}
[moving-from-mysql](moving-from-mysql/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete MySQL to MariaDB migration: `mysqldump`/`mysql` import steps, SQL syntax compatibility, user/privilege migration, and replication configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migrating-to-mariadb-from-postgresql.md" %}
[migrating-to-mariadb-from-postgresql.md](migrating-to-mariadb-from-postgresql.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Strategies for moving data from PostgreSQL to MariaDB, using the CONNECT storage engine with ODBC/JDBC or foreign data wrappers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migrating-to-mariadb-from-oracle/" %}
[migrating-to-mariadb-from-oracle](migrating-to-mariadb-from-oracle/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Migrate from Oracle to MariaDB Server. This section provides detailed guidance, tools, and best practices for a smooth and efficient transition of your databases and applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migrating-to-mariadb-from-sql-server/" %}
[migrating-to-mariadb-from-sql-server](migrating-to-mariadb-from-sql-server/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Migrate from SQL Server to MariaDB. This section provides detailed guidance, tools, and best practices for a smooth and efficient transition of your databases and applications to MariaDB.
{% endcolumn %}
{% endcolumns %}

[^1]: DDL (Data Definition Language): The subset of SQL commands used to create, modify, or destroy the structure of database objects (like tables, indexes, and databases) rather than the data itself.
