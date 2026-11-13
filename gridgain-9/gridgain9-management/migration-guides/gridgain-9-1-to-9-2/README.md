---
description: >-
  How to upgrade a GridGain 9.1.29 cluster or application to GridGain 9.2, with links to the planning page, the step-by-step procedure, and the reference pages for each change.
---

# Upgrading from GridGain 9.1 to 9.2

This guide describes how to upgrade a GridGain 9.1.29 cluster and its applications to GridGain 9.2. GridGain 9.2 raises the Java baseline to Java 21, removes the RocksDB storage engine and the legacy configuration key names, changes the `CREATE ZONE` syntax and the system views, makes user and role names case-sensitive, and changes the SQL query protocol.

{% columns %}
{% column %}
{% content-ref url="upgrade-procedure.md" %}
[Upgrading a Cluster from GridGain 9.1 to 9.2](upgrade-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step procedure for upgrading a cluster with a rolling or a full-cluster upgrade, with verification, troubleshooting, and the recovery options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="before-you-upgrade.md" %}
[What to Know Before Upgrading](before-you-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Planning reference: the choice between a rolling and a full-cluster upgrade, upgrade constraints, and a scope and effort table for every change.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="platform-and-packaging.md" %}
[Platform and Packaging Changes](platform-and-packaging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java 21, the CLI launchers, the `JVM_GC` fallback, and the Windows installer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-and-storage.md" %}
[Configuration, Storage, and Metrics Changes](configuration-and-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Removed and renamed configuration keys, the removed RocksDB engine, page replacement, and renamed metrics.
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
