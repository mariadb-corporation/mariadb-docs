---
description: >-
  MariaDB Cloud AI Agents are built-in assistants for developers and DBAs: the
  Developer Agent, the Data Agent, and the DBA Agent.
hidden: true
---

<!-- DRAFT for DOCS-6592: the AI Agents page after the AI Retrieval launch, for Egor Ustinov's review. Hidden. On launch, this content replaces copilot-guide.md (URL stays /cloud-ai/copilot-guide) and this draft page is deleted. Custom (user-created) agents are removed: database knowledge bases replace them (call of 2026-10-26); the change is announced in the release notes, not on this page. Agent names and descriptions from skysql-ui-client src/composables/useAssistantChat.js @ 212a105a. -->

# AI Agents

{% hint style="info" %}
AI Agents are in Public Preview and free to use, with up to one million tokens of free usage per month per account. The free usage policy can change before general availability.
{% endhint %}

MariaDB Cloud includes built-in AI agents that help developers and DBAs get more out of MariaDB Cloud. You chat with them in the portal, in natural language.

| Agent | What it helps with |
| --- | --- |
| Developer Agent | Questions about MariaDB Cloud, MariaDB, and MySQL: connecting applications, configuring services, using the APIs, and writing SQL. |
| Data Agent | Querying and exploring the data of a connected service in natural language. |
| DBA Agent | Monitoring performance, diagnosing issues, and getting administration insights about a connected service. |

To ask questions about your own documents or database from an application, use [AI Retrieval](ai-retrieval/README.md). Your knowledge bases also appear in the agent list of the chat, so you can test them there.

<!-- TODO: confirm the free usage hint (1M tokens/month) still applies to the built-in agents after the launch. -->

## Developer Agent

The Developer Agent works like a coding assistant that knows MariaDB Cloud and MariaDB. Ask it how to do something instead of searching the documentation.

You can ask questions such as:

* "What is the default storage engine in MariaDB?"
* "Show me a program that connects to MariaDB Cloud from Java."
* "How can I change the configuration of my service in MariaDB Cloud?"

The agent can also write SQL queries across several tables, create schemas, write integration code, and help with tasks such as stored procedures or loading data.

## Data Agent

The Data Agent answers questions about the data in a connected service. It turns your question into an SQL query, runs it, and shows the result.

To try it without your own data, select the demo database as the data source. It is a MariaDB server with sample data.

<!-- TODO: confirm with Egor how the Data Agent relates to database knowledge bases after the launch (both turn questions into SQL). -->

## DBA Agent

The DBA Agent helps with system information, tuning, and diagnostics. It reads the system tables and metadata of the service to answer questions about its internal state.

When you ask a question, the agent splits it into steps. Each step usually becomes an SQL statement on system tables such as those in `information_schema`, `mysql`, or `performance_schema`. The agent runs the steps and uses the results to answer.

## Connect a Data Source

The Data Agent and the DBA Agent work on a data source: a MariaDB service in MariaDB Cloud, or another MariaDB or MySQL server.

* The default database user of a MariaDB Cloud service already has the privileges that the agents need.
* For another server, add a data source and test the connection. Use a development or test database first. Grant the database user of the data source these privileges, replacing `your_datasource_username` with that user:

```sql
GRANT SELECT, PROCESS, SHOW VIEW, SHOW DATABASES ON *.* TO `your_datasource_username`@`%`;
GRANT CREATE, DROP, CREATE VIEW ON `sky_sys_catalog`.* TO `your_datasource_username`@`%`;
```

The agents do not need write privileges on your schemas.

### Slow Query Analysis

To let the DBA Agent analyze slow queries, turn on slow query logging. The overhead of `slow_query_log` grows with the number of queries that it logs, so start with a high `long_query_time`, set `log_slow_rate_limit`, and turn logging off when you do not need it.

In MariaDB Cloud, open Config Manager. If the service uses the default configuration, select **Create New** and change these settings:

* Set `slow_query_log` to `ON`, and `log_output` to `TABLE`. The default is `FILE`.
* Adjust `long_query_time` if needed. The default is 10 seconds. A very low value can add a lot of load. Check the global status variable `slow_queries` to tune it.

### Performance Schema

It also helps to turn on the Performance Schema.

{% hint style="warning" %}
Turning on the Performance Schema restarts the service and adds some overhead. Test the setting before you use it in production.
{% endhint %}

## Use the Agents Through the API

You can also call the built-in agents through the Copilot REST API, for example to start a chat session and send questions. See the MariaDB Cloud API reference.

<!-- TODO: link the Copilot section of the public API reference. Egor (2026-10-26): the Copilot API keeps its name; only the custom-agent endpoints (/copilot/v1/agent create, import, generate, rebuild, and so on) are deprecated and removed at AI Retrieval GA; built-in agent endpoints such as chat and sessions stay. Decide whether ai-api-guide.md stays (Egor questioned it). -->

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
