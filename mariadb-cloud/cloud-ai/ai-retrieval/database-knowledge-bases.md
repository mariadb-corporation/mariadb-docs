---
description: >-
  Create a MariaDB Cloud AI Retrieval database knowledge base, build its
  semantic map, describe your tables, and query your data in natural language.
icon: database
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Built from merged code on 2026-10-26: skysql-ui-client 4.13.37 (d9c5b422, src/locales/en.json, src/helpers/databaseKb.ts), skysql-gen-ai main (5dc0520, copilot/lib/database.py, agent/base.py), and skysql-microservices ai-service (ca4d8483d). Ryan Killea has not reviewed it yet. Screenshots wait for the production flip. Open items are marked TODO. -->

# Database Knowledge Bases

A database knowledge base answers questions about the data in a MariaDB service. You ask a question in natural language. AI Retrieval turns it into an SQL query, checks that the query only reads data, runs it, and returns the rows. It can also write an answer from the rows.

For a quick first run with the Northwind demo database, see [Quickstart](quickstart.md#create-a-database-knowledge-base).

## Before You Begin

* You need a MariaDB service that holds the data, and a database user that can read it. AI Retrieval sees only the tables and columns that this user can see. To limit what a knowledge base can read, see [Access and Security](access-and-security.md#database-knowledge-bases).
* Add the AI Retrieval IP address to the IP allowlist of the service. See [Network Access for Database Knowledge Bases](access-and-security.md#network-access-for-database-knowledge-bases).

## Create a Database Knowledge Base

1. In the portal, select **AI Retrieval** in the navigation, and then **Create Knowledge Base**.
2. For **Type**, select **Database Knowledge Base**.
3. Enter a **Name**, and optionally a **Description**.
4. Under **Datasource**, choose one:
   * **Existing service**: select your service. The hostname, the port, and the credentials of the service are filled in. You can change them, for example to use a user with fewer privileges.
   * **Demo**: AI Retrieval uses the Northwind demo schema. It is useful to try the features without your own data.
5. For an existing service, select **Fetch schemas**, and select the **Schema** whose tables the knowledge base can query. If the list cannot be loaded, enter the schema name.
6. Optionally, expand **Advanced Options** and set these options:
   * **Default max rows**, under **SQL Limits**: the most rows that a question returns, unless the question sets its own limit. The default is 20, and the value can be from 1 to 10,000.
   * **Golden Queries**: pairs of a question and its SQL query. AI Retrieval uses them as examples when it writes queries, so that it learns the terms and patterns of your data. Select **Add Example** to add a pair.
7. Select **Create Knowledge Base**.

AI Retrieval connects to the database and synchronizes its schema. This usually takes a few minutes. If no database is connected within 15 minutes, the setup is marked as failed. When the knowledge base is ready, use **Test** to ask a question, or **Connect** to call it from your application.

<!-- TODO: Ryan Killea to confirm the steps, the defaults, and whether Golden Queries ship in the preview (Egor asked on 2026-10-21 whether golden query add/edit is exposed in the API; the skysql-gen-ai branch feat/dbkb-literals-golden-creds is not merged). Document the Advanced Options field for the description that the model receives (agentDescription in databaseKb.ts) once its portal label is known. -->

## Build the Semantic Map

The semantic map is the description of your tables and columns that AI Retrieval uses to turn a question into a query. AI Retrieval builds it when it synchronizes the schema.

Synchronize the schema again after you change the tables of the database. Some changes in the portal also apply only after the next sync. In that case, the knowledge base page shows **Some schema changes apply only after the next sync**. Select **Sync Now**.

## Describe Your Tables and Columns

Descriptions help AI Retrieval pick the right tables and columns when it writes a query.

1. Open the knowledge base. The **Schema Annotations** section lists the tables of the semantic map.
2. Select **Edit Annotations**.
3. Select a table, and enter a **Table description** and a description for each column.
4. Select **Save**.

Descriptions apply right away. In the same editor, you can also control the columns:

| Setting | What it does | When it applies |
| --- | --- | --- |
| **Included** | Only included columns are mapped and shown to the model. | At the next sync |
| **Literals Index** | Indexes the distinct values of a column, so that a question can match them. Use it for text columns with a limited set of values, such as categories or statuses. It is available for text columns only. | At the next sync |

If a column was dropped from the database, the editor marks it as **No longer in the database**.

## Test a Database Knowledge Base

1. Open the knowledge base and select **Test**.
2. Enter a question about your data, and select **Test Query**.

The results show the **Generated SQL** and the rows that it returned. If more rows are available than the results show, the drawer says so. These options change the test:

| Option | Effect |
| --- | --- |
| **SQL Results** | Includes the result rows in the response, next to the generated answer. When it is off, the SQL is generated but not run. |
| **SQL Limit** | The maximum number of rows that the generated query returns. |

<!-- TODO: confirm the tab names of the Test drawer for a database knowledge base and add a screenshot after the production flip. -->

## Query a Database Knowledge Base with the API

Select **Connect** on the knowledge base to see its endpoints and examples. A database knowledge base has two endpoints:

| Endpoint | Result |
| --- | --- |
| Retrieve rows | Turns the question into SQL, runs it against the connected database, and returns the rows. |
| Retrieve rows and generate | Does the same, and also answers in plain language from the SQL and the returned rows. |

Authenticate with an API key, in the same way as for a document knowledge base. See [Connect Your Application](document-knowledge-bases.md#connect-your-application).

<!-- TODO: add the endpoint paths and the request and response fields once the API paths are final (MCDEV-1488 moves them to /ai/v1/knowledge-bases/). Vijay said on 2026-10-13 that database knowledge bases route through the API gateway, not the regional data plane. -->

## Safeguards

AI Retrieval protects your data when it runs a generated query:

* **Read-only statements.** AI Retrieval runs only statements that read data: `SELECT`, `WITH`, `SHOW`, `DESCRIBE`, and `EXPLAIN`. It rejects any other statement, such as `INSERT`, `UPDATE`, `DELETE`, or a DDL statement.
* **Row limit.** A query returns at most the number of rows that the question or the knowledge base sets, and never more than 10,000.
* **Timeout.** A query that runs for more than 30 seconds is stopped.

The database user is the main control over what a knowledge base can read. Use a user that has read privileges on the data that the knowledge base needs, and nothing more.

<!-- Source: skysql-gen-ai copilot/lib/database.py check_sql (allowed first keywords WITH, SELECT, SHOW, DESCRIBE, DESC, EXPLAIN, ANALYZE, USE) and max_statement_time=30 / max_execution_time=30000; agent/base.py SQL_ROW_LIMIT_CEILING 10000; validation on by default since 67180d4. The check looks only at the first keyword of the statement, so the read-only user is the real protection. TODO: Ryan to confirm the wording. -->

## Troubleshooting

| Message | What to do |
| --- | --- |
| Couldn't list the schemas for this login. | Enter the schema name manually. |
| Connected, but this login can't see any tables outside the system schemas. | Enter the schema name manually, or grant the user privileges on the tables. |
| The knowledge base was created, but connecting the database failed. | Connect the database from the knowledge base page. |
| The knowledge base shows an error after a sync. | Synchronize the schema again, or delete the database connection and connect a new one. |

<!-- TODO: add the failure that a missing IP allowlist entry causes once its message is known. -->

## Next Steps

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

{% content-ref url="usage-and-billing.md" %}
[usage-and-billing.md](usage-and-billing.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
