---
description: >-
  GridGain MCP Server lets AI assistants such as Claude Code, Cursor, and Visual Studio Code inspect a GridGain 8 cluster and run read-only SQL queries.
---

# MCP Server

{% hint style="warning" %}
MCP Server is available only with GridGain Ultimate Edition.
{% endhint %}

GridGain MCP Server lets an AI assistant work with the data in your GridGain cluster.
It implements the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).
It works with any assistant or IDE that supports MCP, such as Claude Code, Cursor, or Visual Studio Code.

The server connects to your cluster and gives the assistant a fixed set of tools. With them, the assistant can:

- Check that the cluster is reachable.
- List caches, tables, and system views, and describe their columns.
- Run read-only SQL queries and read the results.
- Show the execution plan of a query, so the assistant can check whether it uses an index.

The server also gives the assistant reference guides about the GridGain SQL dialect and query tuning.
With them, the assistant can write queries that the cluster answers correctly.
See [Tools and Resources](tools-and-resources.md) for the full list.

## Server Limits

- The server does not change data or the schema. It only reads. See [Security](security.md) for how this is enforced and where its limits are.
- The server does not give the password to the assistant. You set the cluster user name and password in the server's environment. The assistant can see the user name, but never the password.
- The server does not listen on a network port. The assistant starts the server on the same machine and talks to it directly.
- The server connects to one cluster, which you choose when you configure it.

## Requirements

- GridGain Ultimate Edition.
- A GridGain 8.10 cluster that the machine can reach over the thin client port.
- One of the following on the machine where the assistant runs:
  - Docker, to run the container image.
  - Java 17 or later, to run the JAR from the download package.

The server does not need a GridGain installation on its machine.
