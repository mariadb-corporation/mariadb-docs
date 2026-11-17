---
description: >-
  How to upgrade a GridGain 9.1.29 cluster and its applications to 9.2, with links to the step-by-step procedure, the planning page, and the reference pages for each change.
---

# Upgrading from GridGain 9.1 to 9.2

This guide describes how to upgrade a GridGain 9.1.29 cluster and its applications to GridGain 9.2. GridGain 9.2 raises the Java baseline to Java 21, removes the RocksDB storage engine and the legacy configuration key names, changes the SQL syntax and system views, and makes user and role names case-sensitive. For other supported starting releases, see [Supported Starting Versions](before-you-upgrade.md#supported-starting-versions).

{% columns %}
{% column %}
{% content-ref url="upgrade-procedure.md" %}
[Upgrading a Cluster from GridGain 9.1 to 9.2](upgrade-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step procedure for a full-cluster or rolling upgrade, with verification, troubleshooting, and a recovery path back to 9.1.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="before-you-upgrade.md" %}
[What to Know Before Upgrading](before-you-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Planning reference: supported starting versions, upgrade constraints, the choice between a full-cluster and a rolling upgrade, and a scope and effort table for every change.
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
The `CREATE ZONE` syntax, system view columns, and other syntax and behavior changes to check in your queries and DDL.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-changes.md" %}
[Security and Authorization Changes](security-changes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Case-sensitive user and role names, the role migration, and index privileges. Check your existing roles before you upgrade.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clients-and-apis.md" %}
[Client and API Changes](clients-and-apis.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java 21 for client libraries, removed Java APIs, and renamed fields in the data center replication REST API.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
