---
title: AI Tools
description: >-
  MCP servers, coding-agent plugins, retrieval tools, and framework
  integrations that connect AI applications and agents to MariaDB.
icon: robot
---

# AI Tools

This section collects the tools that connect AI applications and agents to MariaDB. Each tool is installed or deployed separately from the database. Vector search is different: it is built into MariaDB Server, so its reference stays with the server documentation.

**MCP servers.** A Model Context Protocol (MCP) server gives an AI agent controlled access to a database. MariaDB offers more than one, and they differ in where they run and what they expose. Start with the comparison page to choose one.

**Coding agents.** The MariaDB AI plugins add MariaDB skills and a local MCP server to coding agents such as Claude Code and Codex. The skills correct the MariaDB-specific details that agents often get wrong.

**Retrieval and RAG.** MariaDB AI RAG runs a retrieval-augmented generation pipeline on your own infrastructure. AI Retrieval provides the same kind of retrieval as a managed MariaDB Cloud feature.

**Cloud AI agents.** MariaDB Cloud includes AI agents that work with your Cloud databases in natural language. These pages are part of the MariaDB Cloud documentation.

**Framework integrations.** LangChain MariaDB lets a LangChain application use MariaDB as its vector store and chat history store.

{% content-ref url="choose-an-mcp-server.md" %}
[Choose an MCP Server](choose-an-mcp-server.md)
{% endcontent-ref %}

{% content-ref url="mariadb-enterprise-mcp-server/README.md" %}
[MariaDB Enterprise MCP Server](mariadb-enterprise-mcp-server/README.md)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-ai/mcp-server" %}
[MariaDB Cloud MCP Server]({mariadb-cloud}/cloud-ai/mcp-server)
{% endcontent-ref %}

{% content-ref url="open-source-mcp-server.md" %}
[Open-Source MCP Server](open-source-mcp-server.md)
{% endcontent-ref %}

{% content-ref url="ai-plugins-and-skills.md" %}
[AI Plugins and Skills](ai-plugins-and-skills.md)
{% endcontent-ref %}

{% content-ref url="mariadb-ai-rag/README.md" %}
[MariaDB AI RAG](mariadb-ai-rag/README.md)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-ai/ai-retrieval" %}
[AI Retrieval]({mariadb-cloud}/cloud-ai/ai-retrieval)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-ai" %}
[Cloud AI Agents]({mariadb-cloud}/cloud-ai)
{% endcontent-ref %}

{% content-ref url="langchain-mariadb/README.md" %}
[LangChain MariaDB](langchain-mariadb/README.md)
{% endcontent-ref %}

{% content-ref url="{server}/reference/sql-structure/vectors" %}
[Vectors in MariaDB Server]({server}/reference/sql-structure/vectors)
{% endcontent-ref %}
