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

The remaining products have their own sets: MaxScale, Galera Cluster, ColumnStore, Exa, the connectors, the Kubernetes Operator, Enterprise Manager, the MCP server, the AI RAG tooling, GridGain 8 and GridGain 9, MariaDB Cloud, and the package repository changelogs.

Component versions matter together as well as individually. In a MariaDB Enterprise Platform deployment the components are certified against specific versions of each other, so upgrading one means checking the notes for the others rather than treating it as an isolated change.

Find the product you run, then read every release between your current version and your target.

## Server Release Notes

{% content-ref url="per-product-release-sets/community-server.md" %}
[community-server.md](per-product-release-sets/community-server.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/enterprise-server.md" %}
[enterprise-server.md](per-product-release-sets/enterprise-server.md)
{% endcontent-ref %}

## Platform Components

{% content-ref url="per-product-release-sets/maxscale.md" %}
[maxscale.md](per-product-release-sets/maxscale.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/galera-cluster.md" %}
[galera-cluster.md](per-product-release-sets/galera-cluster.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/columnstore.md" %}
[columnstore.md](per-product-release-sets/columnstore.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/mariadb-exa.md" %}
[mariadb-exa.md](per-product-release-sets/mariadb-exa.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/gridgain-8.md" %}
[gridgain-8.md](per-product-release-sets/gridgain-8.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/gridgain-9.md" %}
[gridgain-9.md](per-product-release-sets/gridgain-9.md)
{% endcontent-ref %}

## Clients and Tools

{% content-ref url="per-product-release-sets/connectors.md" %}
[connectors.md](per-product-release-sets/connectors.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/kubernetes-operator.md" %}
[kubernetes-operator.md](per-product-release-sets/kubernetes-operator.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/enterprise-manager.md" %}
[enterprise-manager.md](per-product-release-sets/enterprise-manager.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/mcp-server.md" %}
[mcp-server.md](per-product-release-sets/mcp-server.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/ai-rag.md" %}
[ai-rag.md](per-product-release-sets/ai-rag.md)
{% endcontent-ref %}

## Cloud and Repositories

{% content-ref url="per-product-release-sets/mariadb-cloud.md" %}
[mariadb-cloud.md](per-product-release-sets/mariadb-cloud.md)
{% endcontent-ref %}

{% content-ref url="per-product-release-sets/package-repository-changelogs.md" %}
[package-repository-changelogs.md](per-product-release-sets/package-repository-changelogs.md)
{% endcontent-ref %}
