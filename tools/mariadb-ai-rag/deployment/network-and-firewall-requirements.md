# Network and Firewall Requirements

{% hint style="info" %}
It is recommended to run MariaDB AI RAG on an internal, secured network. Direct public exposure of application or database ports is not recommended.
{% endhint %}

Before deploying MariaDB AI RAG, ensure that your firewall and network rules allow traffic on all required ports. Proper connectivity between the Docker containers, local services, and external AI providers is essential for the system to function correctly.

The following table details the necessary ports and their purposes, following the standard MariaDB deployment format.

<table><thead><tr><th>Service/Component</th><th width="79">Port</th><th width="79">Protocol</th><th width="94">Traffic Direction</th><th width="142.5">Purpose</th></tr></thead><tbody><tr><td>RAG API</td><td><code>8000</code></td><td>TCP</td><td>Inbound</td><td>API Access: Main REST API endpoint and Swagger UI documentation.</td></tr><tr><td>MCP Server</td><td><code>8002</code></td><td>TCP</td><td>Inbound</td><td>AI Gateway: Model Context Protocol endpoint for AI agent and IDE interactions.</td></tr><tr><td>MariaDB Server</td><td><code>3306</code></td><td>TCP</td><td>Outbound</td><td>Database Access: Native port for relational and vector data storage.</td></tr><tr><td>Ollama</td><td><code>11434</code></td><td>TCP</td><td>Outbound</td><td>Local LLM: API endpoint for local language models (active only with the Ollama profile).</td></tr><tr><td>External API Providers</td><td><code>443</code></td><td>HTTPS</td><td>Outbound</td><td>AI Services: Requests to configured providers (OpenAI, Gemini, Voyage, Cohere).</td></tr><tr><td>MariaDB Licensing</td><td><code>443</code></td><td>HTTPS</td><td>Outbound</td><td>License Validation: Required at startup to fetch public keys for license verification.</td></tr></tbody></table>

{% hint style="info" %}
All inbound ports listed are TCP. Ensure your firewall rules explicitly allow TCP traffic for the specified ports within the Docker network (`rag-network`) or from authorized external hosts.
{% endhint %}

### Summary of Required Firewall Rules

For a standard AI RAG 1.1 deployment, ensure the following rules are in place:

* Inbound Access: Allow traffic from user workstations or applications to the RAG API on port `8000` and the MCP Server on port `8002`.
* Outbound Access: The host must be able to reach `https://*.mariadb.com` and your configured AI provider endpoints (e.g., `https://generativelanguage.googleapis.com`) on port `443`.
* Internal Connectivity: If your MariaDB vector database is hosted on a separate machine, ensure the RAG host can communicate with it on port `3306`.
