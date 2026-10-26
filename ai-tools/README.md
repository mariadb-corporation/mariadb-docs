---
title: AI Tools
description: >-
  Build with a coding agent that knows MariaDB, give production agents governed access over MCP, and run retrieval on the same database as your data.
icon: robot
---

# AI Tools

The shop's search box now finds the desk lamp when a customer asks for "something to light my desk", and a coding agent wrote most of the code behind it. That's the first of two jobs agents do with MariaDB. One helps you build, on your machine, against a sandbox server. The other acts on live data in production, such as a support bot that looks up an order, and it needs access you can control and audit. These pages cover the tools for both, plus the retrieval pipelines that sit between your data and a language model.

Vector search itself isn't on this list, because it's built into MariaDB Server. Its reference stays with the [server documentation]({server}/reference/sql-structure/vectors).

## Build With a Coding Agent

A coding agent writes better MariaDB code when it knows MariaDB and can try its SQL before you run it. The MariaDB AI plugins give it both. Skills are MariaDB reference material that the agent reads when a task needs it, such as how `ALTER TABLE` behaves or how vector indexes work. The `mariadb-shell` MCP server is a live connection the agent drives through tool calls, so it can start a sandbox server, create tables, and check its own queries.

<figure><picture><source srcset=".gitbook/assets/ai-tools-agent-setup-dark.svg" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/ai-tools-agent-setup-light.svg" alt="What the agent prompt sets up. You install the MariaDB AI plugins into Claude Code. The plugins add MariaDB skills and the mariadb-shell MCP server. The agent uses the sandbox tools to start a local MariaDB Server on port 3310 with no Docker, creates the shop database and products table with the db tools, and writes a Python script that queries it. The docs MCP server lets the agent read current MariaDB documentation."></picture><figcaption><p>Everything the agent builds runs against a sandbox server that you can delete afterward.</p></figcaption></figure>

Install the plugin for your agent:

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add mariadb/ai-plugins
claude plugin install dev@mariadb
```
{% endtab %}

{% tab title="Codex" %}
```bash
codex plugin marketplace add mariadb/ai-plugins
codex plugin add dev@mariadb
```
{% endtab %}

{% tab title="Pi" %}
```bash
pi install git:github.com/mariadb/ai-plugins
```

The package needs Pi 1.0 or later.
{% endtab %}

{% tab title="Hermes Agent" %}
```bash
hermes plugins install mariadb/ai-plugins#hermes/dev-plugin --enable
hermes plugins install mariadb/ai-plugins#hermes/guard-plugin --enable
```

The second package stops the agent from using the MariaDB command-line clients for work that the MCP tools do.
{% endtab %}
{% endtabs %}

The `mariadb-shell` MCP server starts out allowed to reach nothing. Before the agent works against your own databases, run `mariadb-shell -- mcp setup` once per machine to choose the connections and folders it may use. The plugin installs `mariadb-shell` in `~/.local/bin` the first time it starts the MCP server, so let the agent run once before you run the setup. Add the docs MCP server too, so the agent reads current MariaDB syntax instead of guessing from older training data:

```bash
claude mcp add --transport http mariadb-docs \
  https://mariadb.com/docs/~gitbook/mcp
```

[Plugin Variants]({tools}/community/mariadb-ai-plugins/plugin-variants) covers the three plugin variants and what each one installs, and [Installation]({tools}/community/mariadb-ai-plugins/installation) has setup steps for OpenCode.

## Give Agents Access to Live Data

A coding agent on your laptop can do almost anything to a sandbox. An agent that answers customers can't, so it reaches the database through an MCP server that decides what it may see and do. MariaDB has four, and the right one depends on where your databases run.

| MCP server | Where it runs | Use it for |
| --- | --- | --- |
| MariaDB Shell MCP server, a preview feature | On your machine, started by the MariaDB AI plugins, or over HTTP, with a multi-tenant mode for several users | Development with a coding agent, including sandbox servers, and one shared server for a team |
| Open-source MCP server | Wherever you host it, from the [`MariaDB/mcp`](https://github.com/MariaDB/mcp) project | SQL and vector search against your own MariaDB servers |
| MariaDB Enterprise MCP Server | Your infrastructure, as part of MariaDB Enterprise Platform | One governed endpoint for production agents, with authentication and access control |
| MariaDB Cloud MCP Server | Your machine, cloned from the [`skysqlinc/skysql-mcp`](https://github.com/skysqlinc/skysql-mcp) repository and run with a MariaDB Cloud API key | Launching and querying MariaDB Cloud databases from tools such as Cursor and Claude Desktop |

[Choose an MCP Server](choose-an-mcp-server.md) compares them in more detail.

## Retrieve and Generate

Retrieval-augmented generation (RAG) answers a question by first finding the right passages in your own data, then handing them to a language model. MariaDB AI RAG runs that pipeline on your infrastructure, from parsing and chunking documents to hybrid search. For the embeddings and the generated answer, it calls the embedding model and language model you configure: Gemini by default, or a provider such as OpenAI or Ollama. If your application already uses LangChain, LangChain MariaDB lets it keep its vectors and chat history in MariaDB instead of a separate store.

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB AI Plugins</strong></td><td>What the <code>dev</code>, <code>sql</code>, and <code>contributor</code> plugins install, and which agents they support.</td><td><a href="{tools}/community/mariadb-ai-plugins">mariadb-ai-plugins</a></td></tr><tr><td><strong>Choose an MCP Server</strong></td><td>Compare the four MariaDB MCP servers by where they run and who they are for.</td><td><a href="choose-an-mcp-server.md">choose-an-mcp-server.md</a></td></tr><tr><td><strong>MariaDB Enterprise MCP Server</strong></td><td>Give production agents one authenticated, governed endpoint to your databases.</td><td><a href="{tools}/enterprise/mariadb-enterprise-mcp-server">mariadb-enterprise-mcp-server</a></td></tr><tr><td><strong>MariaDB Cloud MCP Server</strong></td><td>Launch and query MariaDB Cloud databases from your AI tools.</td><td><a href="{mariadb-cloud}/cloud-ai/mcp-server">mcp-server</a></td></tr><tr><td><strong>MariaDB AI RAG</strong></td><td>Run document ingestion, embedding, hybrid search, and answer generation on your own infrastructure.</td><td><a href="{tools}/enterprise/mariadb-ai-rag">mariadb-ai-rag</a></td></tr><tr><td><strong>LangChain MariaDB</strong></td><td>Use MariaDB as the vector store and chat history store for a LangChain application.</td><td><a href="{connectors}/other/langchain-mariadb">langchain-mariadb</a></td></tr></tbody></table>
