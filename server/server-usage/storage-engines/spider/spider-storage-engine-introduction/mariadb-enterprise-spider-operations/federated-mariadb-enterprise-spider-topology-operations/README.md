---
description: >-
  This section covers operational guides for managing a Federated Spider
  topology, including migrating tables and performing backup and restore.
---

# Federated MariaDB Enterprise Spider Topology Operations

{% columns %}
{% column %}
{% content-ref url="spider-federated-overview.md" %}
[spider-federated-overview.md](spider-federated-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of the federated topology for Spider, where a single Spider node aggregates data from multiple remote data nodes, acting as a unified access point.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="federated-mariadb-enterprise-spider-topology-backup-and-restore.md" %}
[federated-mariadb-enterprise-spider-topology-backup-and-restore.md](federated-mariadb-enterprise-spider-topology-backup-and-restore.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Procedures for performing consistent backups and restores in a federated Spider topology using MariaDB Backup and MariaDB Dump, ensuring data synchronization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="federated-mariadb-enterprise-spider-topology-migrate-tables.md" %}
[federated-mariadb-enterprise-spider-topology-migrate-tables.md](federated-mariadb-enterprise-spider-topology-migrate-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide on how to migrate tables from a standard MariaDB deployment to a Federated Spider topology, distributing data across multiple backend nodes.
{% endcolumn %}
{% endcolumns %}
