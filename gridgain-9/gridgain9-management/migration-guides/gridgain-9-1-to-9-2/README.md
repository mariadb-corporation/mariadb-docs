---
description: >-
  How to upgrade a GridGain 9.1 cluster and its applications to 9.2, and which changes to check first.
---

# Upgrading from GridGain 9.1 to 9.2

This guide explains how to upgrade a GridGain 9.1 cluster and its applications to GridGain 9.2. Start with the planning page to choose between a [full-cluster upgrade](../../upgrade/full-cluster-upgrade.md) and a [rolling upgrade](../../upgrade/rolling-upgrade.md), then follow the upgrade procedure. Use the other pages as a reference for the changes that affect you.

Key points:

* You can upgrade to 9.2 only from GridGain 9.1.29.
* You cannot downgrade from 9.2 to 9.1. Take a backup before you upgrade.
* 9.2 requires Java 21 or later.
* 9.2 removes the RocksDB storage engine and the legacy configuration key names.
* Each node migrates its Raft logs to a new log storage on first start.
* The `CREATE ZONE` syntax, the system views, and the SQL query protocol change.
* User and role names become case-sensitive.

{% columns %}
{% column %}
{% content-ref url="before-you-upgrade.md" %}
[What to Know Before Upgrading](before-you-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Upgrade constraints, how to choose between a full-cluster and a rolling upgrade, and the scope and effort of each change.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="upgrade-procedure.md" %}
[Upgrading a Cluster from GridGain 9.1 to 9.2](upgrade-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Steps for a full-cluster or rolling upgrade, how to verify the result, and what to do if something fails.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="platform-and-packaging.md" %}
[Platform and Packaging Changes](platform-and-packaging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java 21, the Windows installer, the CLI launchers, and the `JVM_GC` fallback.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-and-storage.md" %}
[Configuration, Storage, and Metrics Changes](configuration-and-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Removed and renamed configuration keys, the removed RocksDB engine, page replacement, renamed metrics, and the Raft log storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-changes.md" %}
[SQL and System View Changes](sql-changes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `CREATE ZONE` syntax, system view columns, the `__part` column, the `ADD` keyword, microsecond precision, and the query protocol.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-changes.md" %}
[Security and Authorization Changes](security-changes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Case-sensitive user and role names, the role migration, and index privileges.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clients-and-apis.md" %}
[Client and API Changes](clients-and-apis.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java 21 for client libraries, `PartitionManager`, `RecordSupportInternal`, and the data center replication REST API.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
