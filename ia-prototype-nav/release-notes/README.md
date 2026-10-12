---
title: Release Notes
description: >-
  Release notes for every MariaDB product: what changed, what was fixed,
  and what to check before upgrading.
icon: file-lines
---

# Release Notes

Release notes record what changed in each release of each MariaDB product: new features, changed behavior, fixed bugs, security updates, and anything that needs attention during an upgrade. Each product releases on its own schedule, so the notes are organized per product rather than as one timeline.

Read them for two reasons. Before an upgrade, the notes for every version between your current one and your target tell you what behavior changes and what needs checking, and skipping intermediate versions does not skip their changes. After a problem, the notes tell you whether it is a known and fixed bug, which is faster than reproducing it.

Server release notes are split by edition, because the editions release differently. MariaDB Community Server follows the community release schedule. MariaDB Enterprise Server follows a maintenance schedule, where fixes are backported to supported versions, so an Enterprise release can carry a fix without carrying the feature changes of a later community version. Check the notes for the edition you actually run.

The remaining products have their own sets: MaxScale, ColumnStore, Galera Cluster, Advanced Cluster, the connectors, the Enterprise Kubernetes Operator, Enterprise Manager, the MCP server, the AI RAG tooling, MariaDB Cloud, and the tools.

Component versions matter together as well as individually. In a MariaDB Enterprise Platform deployment the components are certified against specific versions of each other, so upgrading one means checking the notes for the others rather than treating it as an isolated change.

Dates for releases that have not shipped yet live outside these notes. The Enterprise Server release schedule lists the next scheduled Enterprise releases, and Community Server dates are tracked in Jira.

Find the product you run, then read every release between your current version and your target.

{% content-ref url="latest-releases.md" %}
[Download Latest Releases](latest-releases.md)
{% endcontent-ref %}

{% content-ref url="enterprise-server/README.md" %}
[Enterprise Server Release Notes](enterprise-server/README.md)
{% endcontent-ref %}

{% content-ref url="community-server/README.md" %}
[Community Server Release Notes](community-server/README.md)
{% endcontent-ref %}

{% content-ref url="maxscale/README.md" %}
[MaxScale Release Notes](maxscale/README.md)
{% endcontent-ref %}

{% content-ref url="columnstore/README.md" %}
[ColumnStore Release Notes](columnstore/README.md)
{% endcontent-ref %}

{% content-ref url="galera-cluster/README.md" %}
[Galera Cluster Release Notes](galera-cluster/README.md)
{% endcontent-ref %}

{% content-ref url="advanced-cluster/README.md" %}
[Advanced Cluster Release Notes](advanced-cluster/README.md)
{% endcontent-ref %}

{% content-ref url="connectors/README.md" %}
[Connectors Release Notes](connectors/README.md)
{% endcontent-ref %}

{% content-ref url="enterprise-operator/README.md" %}
[Enterprise Kubernetes Operator Release Notes](enterprise-operator/README.md)
{% endcontent-ref %}

{% content-ref url="enterprise-manager/README.md" %}
[Enterprise Manager Release Notes](enterprise-manager/README.md)
{% endcontent-ref %}

{% content-ref url="ai-rag-release-notes/README.md" %}
[AI Rag Release Notes](ai-rag-release-notes/README.md)
{% endcontent-ref %}

{% content-ref url="mcp-server-release-notes/README.md" %}
[MCP Server Release Notes](mcp-server-release-notes/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-cloud-release-notes/README.md" %}
[MariaDB Cloud Release Notes](mariadb-cloud-release-notes/README.md)
{% endcontent-ref %}

{% content-ref url="control-center/README.md" %}
[Control Center Release Notes](control-center/README.md)
{% endcontent-ref %}

{% content-ref url="ignite-agent/README.md" %}
[Control Center Agent Release Notes](ignite-agent/README.md)
{% endcontent-ref %}

{% content-ref url="tools/README.md" %}
[Tools Release Notes](tools/README.md)
{% endcontent-ref %}

{% content-ref url="gridgain-9/README.md" %}
[GridGain 9 Release Notes](gridgain-9/README.md)
{% endcontent-ref %}

{% content-ref url="gridgain-8/README.md" %}
[GridGain 8 Release Notes](gridgain-8/README.md)
{% endcontent-ref %}
