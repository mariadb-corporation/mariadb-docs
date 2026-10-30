---
description: >-
  How MariaDB Cloud AI Retrieval authenticates requests, connects to your
  database, and handles the region of your data.
icon: shield-check
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Structure follows Egor Ustinov's call of 2026-10-20. Open items are marked TODO. -->

# Access and Security

This page explains who can use AI Retrieval, how your applications authenticate, how AI Retrieval connects to your MariaDB service, and where your data is processed. Document knowledge bases and database knowledge bases handle the database connection differently, so each has its own section.

## Roles and Permissions

Your MariaDB Cloud role decides what you can do with knowledge bases:

| Role | Access |
| --- | --- |
| Viewer | Can view knowledge bases. Cannot create or change them. |
| Member | Can create, change, and delete knowledge bases. |
| Administrator | Can create, change, and delete knowledge bases. |
| Billing | No access to knowledge bases. |

<!-- TODO: the role table comes from the product requirements (NFR-SEC-04) as summarized in Egor's layout document of 2026-10-20, not from code. The portal code in skysql-ui-client has no role check in the knowledge base pages that I found. Verify with Vijay or Ryan. The same source says that MariaDB staff roles that impersonate a user cannot call the data plane endpoints; that is not for customers. -->

## API Keys and Authentication

Applications call a knowledge base through a REST API and authenticate with an API key. Send the key as a bearer token in the `Authorization` header, or in the `X-API-Key` header. An API key belongs to your user account, not to a single knowledge base.

To create, revoke, or delete a key, see [Connect Your Application](document-knowledge-bases.md#connect-your-application).

<!-- TODO: confirm the scope of a key and the roles that can create one. Egor, 2026-10-20: keys authenticate the same way as any MariaDB Cloud endpoint. -->

## Document Knowledge Bases

A document knowledge base stores its chunks and embeddings in a MariaDB service that you select or let MariaDB Cloud provision. AI Retrieval does not read any other data in that service.

### Objects That AI Retrieval Creates

For each document knowledge base, AI Retrieval creates these objects in the vector store service:

| Object | Name | Purpose |
| --- | --- | --- |
| Schema | `ai_retrieval_cloud_` followed by the last 7 characters of the knowledge base ID | Holds the chunks and embeddings of the knowledge base. |
| Database user | `mdb_ai_rag_` followed by the same 7 characters | The account that AI Retrieval uses to connect. It has privileges on this schema only. |

AI Retrieval creates these objects with a service user that has permission to create users. You do not supply credentials for a document knowledge base, and the portal does not offer an option to choose the user name.

{% hint style="warning" %}
Do not delete or change these objects, and do not change the password of the database user. A knowledge base cannot ingest or retrieve documents without them.
{% endhint %}

<!-- Egor, 2026-10-22: the code is right. AI Retrieval still uses a service user that has permission to create users, and with it creates the dedicated user of each knowledge base. He asked to double-check with Vijay. Code: ai-retrieval-cloud packages/skysql-common dbprovision/user_provisioner.py, commit 5124e49a of 2026-09-15; customer_db.py ensures the user on first ingestion. -->

<!-- TODO: confirm that deleting the schema breaks the knowledge base and whether a service restored from a backup needs the objects recreated. See Known Limitations in the overview. -->

### Network Access

AI Retrieval connects to the vector store service over a private network inside MariaDB Cloud. You do not need to add AI Retrieval to the IP allowlist of the service.

<!-- Egor confirmed this on the 2026-10-20 call (the open allowlist requirement from MCDEV-2653 is fixed; MCDEV-2653 itself is still In Progress). Code check: ai-retrieval-cloud rewrites the public host of the service to a cluster-internal service and probes that endpoint (services/ingestion/infrastructure/customer_db.py, commit c72ab65c of 2026-10-20 @ a66a013d). -->

<!-- Conflict: the early Slack thread of 2026-10-02 (jeet, Vijay, Nachiket) still discusses subnets and firewall rules. Egor's later statement and the code win. -->

## Database Knowledge Bases

A database knowledge base reads from a MariaDB service that already holds your data. The create form pre-fills the default user of the service, and you can enter a different user name and password instead. AI Retrieval builds the semantic map of the database only from the tables and columns that this account can see.

To control what a database knowledge base can read, create a dedicated user:

1. Create a view that exposes only the data that the knowledge base should use.
2. Create a user that has privileges on the view only.
3. Enter that user when you create the knowledge base.

### Network Access for Database Knowledge Bases

A database knowledge base connects to your service from outside the network of the service. Add this address of AI Retrieval to the IP allowlist of the service, or the connection fails:

```
34.41.226.174/32
```

<!-- Egor gave this address on 2026-10-22 (Slack DM, 15:17 IST) as the production address for database knowledge bases. It is the address that the portal shows today in the AI Agents datasource dialog. The portal will show it in the knowledge base form later. Egor wants it in this guide. Keep the address out of research notes that are committed. -->

<!-- TODO: Database knowledge bases are not documented yet. The source is on the unmerged branch feature/MCDEV-3646-DBKB of skysql-gen-ai and in skysql-microservices ai-service. Confirm this section against the merged code and the final create form. -->

## Data Residency

Document knowledge bases run in the cloud and region that you select. The vector store service must be in the same cloud and region, so the chunks and embeddings are stored there. You access a document knowledge base through the regional endpoint that the **Connect** dialog shows.

The create form marks where each embedding model runs. Text that is sent to a model is processed as follows:

| Provider | Models | Processing |
| --- | --- | --- |
| AWS Bedrock, in the region of the knowledge base | Cohere Embed 3 English, Cohere Embed 3 Multilingual, Cohere Embed 4 | Traffic stays in the region. |
| Google | Gemini Embedding 2 | Processed outside your cloud. |

<!-- TODO: the model list is from the test environment on 2026-10-20 and the processing labels come from the create form. Confirm the final model list and the wording on data residency with Egor. Model names are not published elsewhere yet. -->

<!-- TODO: Egor said document knowledge bases must be accessed through the regional endpoints. Replace the placeholder host in the guide with the production host once it is known. -->

<!-- Egor said on 2026-10-20 not to cover encryption or audit logging. Left out on purpose. -->

## Next Steps

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
