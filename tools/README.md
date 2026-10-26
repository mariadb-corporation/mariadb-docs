---
description: >-
  This space includes documentation for clients, utilities, and applications,
  including AI-focused ones, designed to help you manage, monitor, back up, and
  interact with your MariaDB Server deployment.
---

# Tools

{% hint style="info" %}
📄 Read offline: [mariadb-tools.pdf](https://github.com/mariadb-corporation/mariadb-docs/releases/latest/download/mariadb-tools.pdf) (~610 pages, 23 MB). The PDF is a point-in-time snapshot; this site is always current.
{% endhint %}

## Enterprise Tools

[Enterprise Tools](enterprise/README.md) are made available and supported under a MariaDB Enterprise Support subscription.

### MariaDB Enterprise Manager

{% columns %}
{% column %}
<figure><img src=".gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
MariaDB Enterprise Manager is a comprehensive observability and management solution designed for your entire database fleet. It provides advanced, topology-aware monitoring and a powerful suite of visual tools for query development and schema management, all from a single, centralized interface.
{% endcolumn %}
{% endcolumns %}

{% content-ref url="enterprise/mariadb-enterprise-manager/" %}
[mariadb-enterprise-manager](enterprise/mariadb-enterprise-manager/)
{% endcontent-ref %}

### MariaDB Enterprise Operator

MariaDB Enterprise Operator provides a seamless way to run and operate containerized versions of MariaDB Enterprise Server and MaxScale on Kubernetes, allowing you to leverage Kubernetes orchestration and automation capabilities. This document outlines the features and advantages of using Kubernetes and the MariaDB Enterprise Operator to streamline the deployment and management of MariaDB and MaxScale instances.

{% content-ref url="enterprise/mariadb-enterprise-operator/" %}
[mariadb-enterprise-operator](enterprise/mariadb-enterprise-operator/)
{% endcontent-ref %}

### MariaDB Enterprise MCP Server

MariaDB Enterprise MCP (Model Context Protocol) Server is a secure, enterprise-grade application designed to act as the primary interface between AI assistants and MariaDB data ecosystems. This product solves a key challenge: how to allow powerful AI agents to safely and efficiently leverage an organization's most valuable asset—its data.

{% content-ref url="enterprise/mariadb-enterprise-mcp-server/" %}
[mariadb-enterprise-mcp-server](enterprise/mariadb-enterprise-mcp-server/)
{% endcontent-ref %}

### MariaDB AI RAG

MariaDB AI RAG is an enterprise-grade Retrieval-Augmented Generation (RAG) solution that integrates with MariaDB to provide AI-powered document processing, semantic search, and natural language generation capabilities.

{% content-ref url="enterprise/mariadb-ai-rag/" %}
[mariadb-ai-rag](enterprise/mariadb-ai-rag/)
{% endcontent-ref %}

### Control Center

Control Center is the management and monitoring interface for GridGain clusters, providing cluster visibility, metrics, and administrative tooling from a single place.

{% content-ref url="enterprise/control-center/" %}
[control-center](enterprise/control-center/)
{% endcontent-ref %}

## Community Tools

[Community Tools](community/README.md) don't require a MariaDB Enterprise Support subscription.

### MySQL to MariaDB Migrator

The MySQL to MariaDB Migrator automates end-to-end migrations from MySQL to MariaDB: schema, data, users, and validation, in four selectable modes.

{% content-ref url="community/mariadb-migrator/" %}
[mariadb-migrator](community/mariadb-migrator/)
{% endcontent-ref %}

### MariaDB AI Plugins

MariaDB AI Plugins extend AI coding agents such as Claude Code, Codex, OpenCode, Pi, and Hermes Agent with knowledge about MariaDB and with access to MariaDB databases. A plugin contains agent skills with MariaDB-specific guidance on SQL, client tools, and connectors, and it connects the agent to MariaDB Server through the `mariadb-shell` MCP server.

{% content-ref url="community/mariadb-ai-plugins/" %}
[mariadb-ai-plugins](community/mariadb-ai-plugins/)
{% endcontent-ref %}

### MariaDB Shell

MariaDB Shell is an interactive client for MariaDB Server with SQL and Python modes. It adds parallel dump, load, and copy utilities, SSH tunnels written as `mariadb+ssh://` URIs, local sandbox servers, and a Python API for scripting and extending the shell.

{% content-ref url="community/mariadb-shell/" %}
[mariadb-shell](community/mariadb-shell/)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
