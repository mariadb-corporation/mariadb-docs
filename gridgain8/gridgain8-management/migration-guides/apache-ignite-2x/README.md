---
description: >-
  How to migrate from Apache Ignite 2.18 to the GridGain 8.10 Ultimate release,
  with links to the step-by-step procedure and planning reference material.
---

# Migration from Apache Ignite 2

This guide describes how to migrate from Apache Ignite 2.18 to the GridGain 8.10 Ultimate release.

{% columns %}
{% column %}
{% content-ref url="migration-procedure.md" %}
[Migrating from Apache Ignite 2](migration-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Step-by-step procedure for migrating a cluster, its data, clients, and tooling from Apache Ignite 2.18 to GridGain 8.10, with cutover, verification, and rollback.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="before-you-migrate.md" %}
[What to Know Before Migrating](before-you-migrate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Planning reference for migrating from Apache Ignite 2.18 to GridGain 8: prerequisites, migration constraints, a compatibility summary, and effort estimates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="features-to-replace.md" %}
[Features to Replace](features-to-replace.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Apache Ignite 2 features that work differently or have no equivalent in GridGain 8, with what to do and how to verify each replacement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration.md" %}
[Configuration and Validation Changes](configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuration changes when migrating from Apache Ignite 2 to GridGain 8: changed defaults, removed and unsupported properties, and binary field ordering.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="apis-and-clients.md" %}
[APIs, Clients, and Extensions](apis-and-clients.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL engine, per-language client, and plugin/SPI changes to account for when migrating applications from Apache Ignite 2 to GridGain 8.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="artifacts-and-modules.md" %}
[Artifacts and Deployment](artifacts-and-modules.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain distribution formats, per-language build coordinate changes, Docker differences, and module and extension availability when migrating from Apache Ignite 2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="operations.md" %}
[Monitoring and CLI Changes](operations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitoring and command-line changes when migrating from Apache Ignite 2 to GridGain 8, covering logs, metrics, system views, events, and the CLI tools.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-authorization.md" %}
[Security Authorization Changes](security-authorization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to migrate authorization from a secured Apache Ignite 2.x cluster to GridGain 8: retired permissions, coarser admin grants, and user management.
{% endcolumn %}
{% endcolumns %}
