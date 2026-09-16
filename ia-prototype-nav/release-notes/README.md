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

{% content-ref url="{release-notes}/latest-releases" %}
[Download Latest Releases]({release-notes}/latest-releases)
{% endcontent-ref %}

{% content-ref url="{release-notes}/enterprise-server" %}
[Enterprise Server Release Notes]({release-notes}/enterprise-server)
{% endcontent-ref %}

{% content-ref url="{release-notes}/community-server" %}
[Community Server Release Notes]({release-notes}/community-server)
{% endcontent-ref %}

{% content-ref url="{release-notes}/maxscale" %}
[MaxScale Release Notes]({release-notes}/maxscale)
{% endcontent-ref %}

{% content-ref url="{release-notes}/columnstore" %}
[ColumnStore Release Notes]({release-notes}/columnstore)
{% endcontent-ref %}

{% content-ref url="{release-notes}/galera-cluster" %}
[Galera Cluster Release Notes]({release-notes}/galera-cluster)
{% endcontent-ref %}

{% content-ref url="{release-notes}/advanced-cluster" %}
[Advanced Cluster Release Notes]({release-notes}/advanced-cluster)
{% endcontent-ref %}

{% content-ref url="{release-notes}/connectors" %}
[Connectors Release Notes]({release-notes}/connectors)
{% endcontent-ref %}

{% content-ref url="{release-notes}/enterprise-operator" %}
[Enterprise Kubernetes Operator Release Notes]({release-notes}/enterprise-operator)
{% endcontent-ref %}

{% content-ref url="{release-notes}/enterprise-manager" %}
[Enterprise Manager Release Notes]({release-notes}/enterprise-manager)
{% endcontent-ref %}

{% content-ref url="{release-notes}/ai-rag-release-notes" %}
[AI Rag Release Notes]({release-notes}/ai-rag-release-notes)
{% endcontent-ref %}

{% content-ref url="{release-notes}/mcp-server-release-notes" %}
[MCP Server Release Notes]({release-notes}/mcp-server-release-notes)
{% endcontent-ref %}

{% content-ref url="{release-notes}/mariadb-cloud-release-notes" %}
[MariaDB Cloud Release Notes]({release-notes}/mariadb-cloud-release-notes)
{% endcontent-ref %}

{% content-ref url="{release-notes}/tools" %}
[Tools Release Notes]({release-notes}/tools)
{% endcontent-ref %}

{% content-ref url="{release-notes}/test-page" %}
[Test Page]({release-notes}/test-page)
{% endcontent-ref %}
