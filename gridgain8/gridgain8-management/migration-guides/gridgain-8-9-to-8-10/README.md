---
description: >-
  How to upgrade a GridGain 8.9.x cluster or application to 8.10, with links to the planning page, the step-by-step procedure, and the reference pages for each change.
---

# Upgrading from GridGain 8.9 to 8.10

This guide describes how to upgrade a GridGain 8.9.x cluster and its applications to GridGain 8.10. GridGain 8.10 raises the Java baseline to Java 17, removes several modules and integrations, moves key dependencies to current versions, and changes a small number of defaults.

If you are migrating from Apache Ignite 2.x, see [Migrating from Apache Ignite 2](../apache-ignite-2x/README.md) instead.

{% columns %}
{% column %}
{% content-ref url="upgrade-procedure.md" %}
[Upgrade Procedure](upgrade-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step procedure for upgrading a cluster with Rolling Upgrades or offline, with verification, troubleshooting, and a recovery path back to 8.9.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="before-you-upgrade.md" %}
[What to Know Before Upgrading](before-you-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Planning reference: the choice between a rolling and an offline upgrade, upgrade constraints, and a scope and effort table for every change.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="platform-and-modules.md" %}
[Platform, Modules, and Packaging](platform-and-modules.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java 17, removed modules and integrations, upgraded dependencies (Spring, Hibernate, Lucene, Jetty, Cassandra), and distribution changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-and-defaults.md" %}
[Configuration and Default Value Changes](configuration-and-defaults.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Changed defaults, new limits, system properties, startup messages, and JMX metric types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-and-licensing.md" %}
[Security, Permission, and Licensing Changes](security-and-licensing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Server-side SQL `COPY`, REST scan queries, thin client permission checks, and per-feature license checks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clients-and-drivers.md" %}
[Client and Driver Changes](clients-and-drivers.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Java thin client timeouts, DNS resolution and transactions, and .NET and C++ client changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="other-changes.md" %}
[Deprecations, Other Changes, and New Features](other-changes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deprecated APIs, changes that need no action, and the new features of 8.10.
{% endcolumn %}
{% endcolumns %}
