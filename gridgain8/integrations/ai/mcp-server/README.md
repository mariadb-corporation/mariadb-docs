---
description: >-
  GridGain MCP Server lets AI assistants such as Claude Code, Cursor, and Visual Studio Code inspect a GridGain 8 cluster and run read-only SQL queries.
---

# MCP Server

GridGain MCP Server lets an AI assistant work with the data in your GridGain cluster.
It implements the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).
It works with any assistant or IDE that supports MCP, such as Claude Code, Cursor, or Visual Studio Code.

The server connects to your cluster and gives the assistant a fixed set of tools. With them, the assistant can:

- Check that the cluster is reachable.
- List caches, tables, and system views, and describe their columns.
- Run read-only SQL queries and read the results.
- Show the execution plan of a query, so the assistant can check whether it uses an index.

The server also hands the assistant reference guides about the GridGain SQL dialect and query tuning, so it can write queries that the cluster answers correctly.
See [Tools and Resources](tools-and-resources.md) for the full list.

## Limits of the Server

- The server only reads. It does not change data or the schema. See [Security](security.md) for how this is enforced and where its limits are.
- The server does not give credentials to the assistant. You set the cluster user name and password in the environment of the server, and the assistant never sees them.
- The server does not listen on a network port. The assistant starts the server on the same machine and talks to it directly.
- The server connects to one cluster, which you choose when you configure it.

## Requirements

- A GridGain 8.10 cluster that the machine can reach over the thin client port (10800 by default).
- One of the following on the machine where the assistant runs:
  - Docker, to run the container image.
  - Java 17 or later, to run the JAR from the download package.

The server does not need a GridGain installation on its machine.

## Get Started

1. [Install the server](installation.md) from the download package or as a container image.
2. [Connect your assistant](agent-hosts.md) to the server.
3. Create a [dedicated read-only account](security.md#preparing-a-cluster-account) on the cluster for the server.
4. Run the [connection check](operations.md#checking-the-connection) to confirm that the setup works.
