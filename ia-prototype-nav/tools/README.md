---
title: Tools
description: >-
  Clients, utilities, and management applications for MariaDB Server and
  MariaDB Enterprise Platform, including Enterprise Manager, the Kubernetes
  Operator, and the MCP server.
icon: screwdriver-wrench
---

# Tools

This space documents the clients, utilities, and management applications that surround a MariaDB deployment. They fall into a few groups, and which ones you need depends on how much you operate and how you deploy.

**Fleet management.** MariaDB Enterprise Manager is a management and observability console for a set of servers. It provides topology aware monitoring plus visual tools for query development and schema management, from one interface. It becomes worth deploying at the point where you run more servers than you can hold in your head.

**Kubernetes.** The MariaDB Enterprise Operator runs MariaDB Enterprise Server and MaxScale on Kubernetes, managing them as custom resources declared in your manifests and reconciled by the cluster. If your workloads already run on Kubernetes, this makes the database deploy the same way everything else does.

**AI and agent access.** The MariaDB MCP Server exposes a database over the Model Context Protocol, so an agent can inspect schemas and run read only SQL under access you control. The AI RAG tooling assembles a retrieval pipeline that pairs vector search in the database with a language model.

**Command line utilities.** The client and utility programs that ship with the server handle the everyday work: connecting, dumping and loading data, taking physical backups, and checking tables. These are documented alongside the server as well, and they are the tools most operational procedures are actually built from.

**Install and configure.** Each tool has its own installation and configuration path, and the guides here cover them individually along with securing the ones that hold credentials for your databases.

Start from the tool that matches the problem you have rather than reading the space end to end.

## Get Started

{% content-ref url="get-started/install-tools.md" %}
[install-tools.md](get-started/install-tools.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-tools.md" %}
[connect-to-tools.md](get-started/connect-to-tools.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/tools-tutorial.md" %}
[tools-tutorial.md](tutorials/tools-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-tools.md" %}
[configure-tools.md](how-to-guides/configure-tools.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-tools.md" %}
[secure-tools.md](how-to-guides/secure-tools.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-tools.md" %}
[what-is-tools.md](overview/what-is-tools.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-tools-works.md" %}
[how-tools-works.md](concepts/how-tools-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/tools-reference.md" %}
[tools-reference.md](reference/tools-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/tools-releases.md" %}
[tools-releases.md](release-notes/tools-releases.md)
{% endcontent-ref %}
