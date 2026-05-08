---
description: >-
  Common questions about the MCP Server address installation, MariaDB
  connection setup, AI client integration, how LLM agents invoke tools, and
  the purpose of JSON protocol examples.
---

# Frequently Asked Questions

<details>

<summary><strong>Where do you get MCP Server from and what are the installation requirements?</strong></summary>

The MCP Server can be launched individually or as part of the RAG-in-a-box system. It is distributed as pre-compiled binaries that can run on various operating systems, including:

* Windows
* RHEL (Red Hat Enterprise Linux)
* Ubuntu

</details>

<details>

<summary><strong>Is MCP Server a command-line tool, or does it have a GUI?</strong></summary>

The MCP Server is a network service that runs as an HTTP server; it does not have a graphical user interface (GUI) or a direct command-line interface (CLI) for tools. It's designed to be a backend service that is:

* Accessed programmatically via the Model Context Protocol.
* Integrated into AI assistants and clients like Claude Desktop, Cursor, or Windsurf.

You interact with the server by configuring a client application to communicate with it. For example, here is how you might configure a client like Windsurf:

{% code overflow="wrap" %}
```json
{
  "mcpServers": {
    "rag-mcp": {
      "serverUrl": "http://localhost:8002/mcp",
      "headers": {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xyz.abc"
      }
    }
  }
}
```
{% endcode %}

</details>

<details>

<summary><strong>How do you configure the MCP Server and connect it to MariaDB?</strong></summary>

The MCP Server does not include its own database. It acts as a client and requires a connection to an external, pre-existing MariaDB server.

The system components are connected as follows:

```
MCP Server (Port 8002) ---------> MariaDB Server (Port 3306)
                         (connects via MySQL protocol)
```

Configuration is managed through environment files where you specify the connection details for your MariaDB instance.

</details>

<details>

<summary><strong>How are tools like <code>list_databases</code> executed?</strong></summary>

Tools are not typed into a command line. Instead, they are executed programmatically by a Large Language Model (LLM) in response to a user's query in natural language.

The process works like this:

1. A user asks a question in an integrated client (e.g., "Can you show me what databases are available?").
2. The LLM interprets the request and determines that the `list_databases` tool is needed.
3. The LLM calls the `list_databases` tool by sending a JSON-RPC request to the MCP Server.
4. The MCP Server executes the tool against the connected MariaDB database.
5. The results are sent back to the LLM, which formats them into a natural language response for the user.

</details>

<details>

<summary><strong>What are the JSON snippets in the documentation for?</strong></summary>

The JSON snippets shown in the documentation are examples of the "behind-the-scenes" communication between a client, the LLM, and the MCP Server. They are not meant to be copied and pasted into a CLI but serve to illustrate how the protocol functions.

</details>

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
