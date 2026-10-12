---
title: Enterprise Tools
description: >-
  Clients, utilities, and management applications for MariaDB Server and
  MariaDB Enterprise Platform, including Enterprise Manager and the Kubernetes
  Operator.
icon: screwdriver-wrench
---

# Enterprise Tools

This space documents the clients, utilities, and management applications that surround a MariaDB deployment. They fall into a few groups, and which ones you need depends on how much you operate and how you deploy.

**Fleet management.** MariaDB Enterprise Manager is a management and observability console for a set of servers. It provides topology aware monitoring plus visual tools for query development and schema management, from one interface. It becomes worth deploying at the point where you run more servers than you can hold in your head.

**Kubernetes.** The MariaDB Enterprise Operator runs MariaDB Enterprise Server and MaxScale on Kubernetes, managing them as custom resources declared in your manifests and reconciled by the cluster. If your workloads already run on Kubernetes, this makes the database deploy the same way everything else does.

**AI and agent access.** The MariaDB Enterprise MCP Server and MariaDB AI RAG are documented in the AI Tools section, together with the other tools that connect AI applications and agents to MariaDB.

**Command line utilities.** The client and utility programs that ship with the server handle the everyday work: connecting, dumping and loading data, taking physical backups, and checking tables. These are documented alongside the server as well, and they are the tools most operational procedures are actually built from.

**Install and configure.** Each tool has its own installation and configuration path, and the guides here cover them individually along with securing the ones that hold credentials for your databases.

Start from the tool that matches the problem you have rather than reading the space end to end.

{% content-ref url="mariadb-enterprise-manager/README.md" %}
[MariaDB Enterprise Manager](mariadb-enterprise-manager/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-enterprise-operator/README.md" %}
[MariaDB Enterprise Kubernetes Operator](mariadb-enterprise-operator/README.md)
{% endcontent-ref %}
