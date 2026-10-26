---
description: >-
  Compare the MariaDB MCP servers by where they run and who they are for, and
  choose the one that fits your deployment.
icon: scale-balanced
---

# Choose an MCP Server

An MCP server lets an AI agent work with your databases through the Model Context Protocol. MariaDB has four. The right one depends on where your databases run and who uses the agent.

## MariaDB Enterprise MCP Server

MariaDB Enterprise MCP Server is a single, hardened endpoint between AI agents and your MariaDB data. Platform engineering and DBA teams deploy and manage it in their own environment. It is for organizations that put AI agents into production and need central control over how those agents reach the data. See [MariaDB Enterprise MCP Server]({tools}/enterprise/mariadb-enterprise-mcp-server).

## MariaDB Cloud MCP Server

MariaDB Cloud MCP Server lets AI tools such as Cursor, Claude Desktop, and Visual Studio Code Copilot launch MariaDB Cloud serverless databases and run SQL on them. You clone it from the [`skysqlinc/skysql-mcp`](https://github.com/skysqlinc/skysql-mcp) repository and run it with a MariaDB Cloud API key. It is for developers whose databases run in MariaDB Cloud. See [MariaDB Cloud MCP Server]({mariadb-cloud}/cloud-ai/mcp-server).

## MariaDB Shell MCP Server

MariaDB Shell includes an MCP server, and the MariaDB AI plugins start it for coding agents such as Claude Code, Codex, OpenCode, and Pi. A client starts it on your machine and talks to it over standard input and output, or it connects to a server that you run over HTTP. To share one server among several users, multi-tenant mode signs each user in with an API key or OAuth2, and it can run in a container. The MCP server is a preview feature. See [MCP Server]({tools}/community/mariadb-shell/mcp-server).

## Open-Source MariaDB MCP Server

The [`MariaDB/mcp`](https://github.com/MariaDB/mcp) project on GitHub is an open-source MCP server that you host yourself. Its repository has the source and the setup steps.
