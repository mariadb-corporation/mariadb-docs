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

{% content-ref url="{tools}/mariadb-enterprise-manager" %}
[MariaDB Enterprise Manager]({tools}/mariadb-enterprise-manager)
{% endcontent-ref %}

{% content-ref url="{tools}/mariadb-enterprise-operator" %}
[MariaDB Enterprise Kubernetes Operator]({tools}/mariadb-enterprise-operator)
{% endcontent-ref %}

{% content-ref url="{tools}/mariadb-enterprise-mcp-server" %}
[MariaDB Enterprise MCP Server]({tools}/mariadb-enterprise-mcp-server)
{% endcontent-ref %}

{% content-ref url="{tools}/mariadb-ai-rag" %}
[MariaDB AI RAG]({tools}/mariadb-ai-rag)
{% endcontent-ref %}
