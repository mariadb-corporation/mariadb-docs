---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Data Loading

MariaDB Cloud enables you to import, synchronize, and load data into your database services using several tools and methods from various data formats and sources. Whether you are importing CSV and TSV files, restoring dumps, or using command-line utilities, these methods provide flexibility and instructions to prepare, import, and validate your data for different data loading use cases.

## Import CSV Data

Import datasets of different file sizes directly into MariaDB Cloud service using the [`LOAD DATA LOCAL INFILE`](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement, which can be executed by any client or connector after enabling local infile support.

{% content-ref url="import-csv-data.md" %}
[import-csv-data.md](import-csv-data.md)
{% endcontent-ref %}

## Install mariadb-dump

Install the `mariadb-dump` command-line utility to create logical backups of your MariaDB Cloud services on Linux and Windows platforms for export, migration, or backup scenarios.

{% content-ref url="install-mariadb-dump.md" %}
[install-mariadb-dump.md](install-mariadb-dump.md)
{% endcontent-ref %}

## Install mariadb-import

Install and use the `mariadb-import` command-line utility to efficiently bulk-load CSV or TSV data into your MariaDB Cloud database services from various platforms, such as Linux and Windows.

{% content-ref url="install-mariadb-import.md" %}
[install-mariadb-import.md](install-mariadb-import.md)
{% endcontent-ref %}

## Replicating Data from an External Database to MariaDB Cloud

Set up and run continuous, inbound replication from an external MySQL or MariaDB server to MariaDB Cloud using binary log position or [GTID-based](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) replication.

{% content-ref url="replicating-data-from-external-db.md" %}
[replicating-data-from-external-db.md](replicating-data-from-external-db.md)
{% endcontent-ref %}

