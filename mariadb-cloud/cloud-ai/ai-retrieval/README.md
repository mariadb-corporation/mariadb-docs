---
description: >-
  MariaDB Cloud AI Retrieval indexes your documents or your database in a
  knowledge base and returns relevant passages, rows, or generated answers
  through a REST API.
icon: magnifying-glass
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Restructured on 2026-10-22 to cover concepts first, as Egor Ustinov asked on the call of 2026-10-20. Open items are marked TODO. -->

# AI Retrieval

AI Retrieval is a MariaDB Cloud service that makes your own content available to AI applications. You create a knowledge base from your documents or from a MariaDB database. Your applications then query the knowledge base through a REST API and receive the most relevant content, or an answer that a large language model (LLM) generates from it.

AI Retrieval is a retrieval layer. It finds the right content and returns it, but it does not run an agent. You use it with your own application, or with an agent framework that calls a REST API.

<!-- TODO: the retrieval layer wording comes from the product requirements (Business Context) as summarized in Egor's layout document. Confirm it with Egor. -->

{% hint style="info" %}
AI Retrieval is in Public Preview. Behavior and limits can change before general availability.
{% endhint %}

## Knowledge Base Types

| Type | Content | How you query it |
| --- | --- | --- |
| Document knowledge base | Files such as PDF, Word, PowerPoint, Markdown, and HTML documents | You ask a question in natural language and receive the most relevant passages, or a generated answer. |
| Database knowledge base | Tables of an existing MariaDB service | You ask a question in natural language and receive the rows that answer it, or a generated answer. |

For the details, see [Document Knowledge Bases](document-knowledge-bases.md) and [Database Knowledge Bases](database-knowledge-bases.md).


## How It Works

### Document Knowledge Bases

1. You create a knowledge base. AI Retrieval stores its chunks and embeddings in a MariaDB service, the vector store. You can use an existing Provisioned or Serverless service, or let MariaDB Cloud provision a Serverless service for you.
2. You add documents by uploading files or by connecting an Amazon S3 or Google Cloud Storage bucket.
3. AI Retrieval parses each document, splits the text into chunks, creates an embedding for each chunk, and stores both in the vector store.
4. Your application sends a question to the knowledge base endpoint.
5. AI Retrieval searches the chunks, ranks them, and returns the best matches. For a generated answer, it passes the best chunks to a generation model, which writes the answer and cites the chunks that it used.

### Database Knowledge Bases

1. You create a knowledge base from a schema of a MariaDB service.
2. AI Retrieval connects to the database, reads the tables and columns that the database user can see, and builds the semantic map: a model of your database that AI Retrieval builds automatically: the tables and columns, the relationships between tables, the indexes, and descriptions of the data. You do not need to do anything for this step. You can refine the semantic map later.
3. Your application sends a question to the knowledge base endpoint.
4. AI Retrieval uses the semantic map to turn the question into an SQL query, checks that the query only reads data, runs it, and returns the rows. For a generated answer, it writes the answer from the rows. A follow-up question in the same session can build on the earlier ones.
<!-- TODO: replace the semantic map wording with the description that Egor will send (call of 2026-10-29: it is more than descriptions; it holds relationships, indexes, and more). -->


<!-- TODO: the database knowledge base steps come from the product requirements and Egor's layout document, not from code. The code is on the unmerged branch feature/MCDEV-3646-DBKB of skysql-gen-ai. Verify the steps, the read-only check, and the limits (100 tables, 1,000 columns, a row limit, and a query timeout) against the merged code. -->

## Key Concepts

| Concept | Meaning |
| --- | --- |
| Knowledge base | The searchable collection that you create and query. It has a type, a cloud region, and settings such as the models and the reranker. |
| Vector store | The MariaDB service, Provisioned or Serverless, that stores the chunks and embeddings of a document knowledge base. |
| Document | A file in a document knowledge base. |
| Data source | Where a knowledge base gets its content. For a document knowledge base, an Amazon S3 or Google Cloud Storage bucket, or files that you upload. For a database knowledge base, the MariaDB database that it queries. |
| Chunk | A passage of a document. A retrieval request returns chunks. |
| Embedding | A list of numbers that represents the meaning of a chunk. AI Retrieval compares the embedding of a question with the embeddings of the chunks to find related text. |
| Sync | For a document knowledge base, the action that ingests the new and changed files of a bucket. For a database knowledge base, the action that rebuilds the semantic map after the database changes. |
| Semantic map | For a database knowledge base, a model of your database that AI Retrieval builds automatically: the tables and columns, the relationships between tables, the indexes, and descriptions of the data. AI Retrieval uses it to turn a question into an SQL query. |
| Reranker | For a document knowledge base, a model that re-scores the retrieved chunks. |
| Generation model | The LLM that writes an answer from the retrieved content. |
| API key | The credential that your application uses to call a knowledge base. |

## Retrieval Modes

Both knowledge base types offer two modes:

| Mode | Document knowledge base | Database knowledge base |
| --- | --- | --- |
| Retrieve | The most relevant chunks for the question | The SQL query that answers the question, and its rows |
| Retrieve & Generate | An answer that the generation model writes from the retrieved chunks, with citations to the chunks used | An answer in plain language, written from the query and its rows |

A document knowledge base searches its chunks with one of three methods.

| Method | How it searches |
| --- | --- |
| Hybrid (default) | Combines semantic and full-text search |
| Semantic | Matches the meaning of the question |
| Full text | Matches the keywords in the question |

For a document knowledge base, Retrieve & Generate can stream the answer as it is generated. A database knowledge base can keep the context of a session, so that a follow-up question builds on the earlier ones. See [Database Knowledge Bases](database-knowledge-bases.md#ask-follow-up-questions).

## Requirements and Availability

* Document knowledge bases run on AWS, in the region that you select. Database knowledge bases are available in every region. See [Supported Models, Formats, and Regions](supported-models-formats-and-regions.md#supported-regions).
* For a document knowledge base, the vector store must be a MariaDB service, Provisioned or Serverless, in the same cloud and region as the knowledge base, running MariaDB 11.8 or later. You can select an existing service or let MariaDB Cloud provision a new Serverless service.
* For a database knowledge base, you need a MariaDB service with your data, a database user that can read it, and the AI Retrieval IP address in the IP allowlist of the service. See [Access and Security](access-and-security.md#database-knowledge-bases).
* Your role decides what you can do with knowledge bases. See [Access and Security](access-and-security.md#roles-and-permissions).
* You need an API key to call the REST API from an application. See [Access and Security](access-and-security.md#api-keys-and-authentication).

<!-- TODO: confirm the AWS regions available at launch. The test environment offers only eu-central-1. Egor said the regions follow the product requirements page (us-east-1, eu-west-2, eu-central-1, ap-southeast-1 in NFR-CLO-01). Google Cloud and Azure open a Register Interest dialog. -->

## Supported Files and Limits

This applies to document knowledge bases. A document knowledge base accepts TXT, Markdown, HTML, JSON, Word (DOCX), PDF, and PowerPoint (PPTX) files. See [Supported Models, Formats, and Regions](supported-models-formats-and-regions.md#supported-file-formats-for-document-knowledge-bases).

Scanned documents, which are PDFs that contain only images of pages, and password-protected files are not supported yet. Images inside documents are skipped. Documents must be in English.

<!-- TODO: English only and no password-protected PDFs come from Egor (2026-10-14, MCDEV-5201) and Slack, not from code. -->

## Quotas

AI Retrieval limits request rates, document sizes, and concurrent ingestion for each organization, and the MCUs that an organization can consume each month. See [Service Quotas](service-quotas.md).

## Known Limitations

### All Knowledge Bases

* AI Retrieval is not available for Bring Your Own Cloud (BYOC) organizations.

### Document Knowledge Bases

* Syncs are manual. AI Retrieval does not sync a bucket on a schedule, so run a sync whenever you add files to the bucket.
* You cannot change the embedding model after you create the knowledge base.
* Follow-up questions in a session are not supported. Each request is answered on its own.
* Scanned documents and images inside documents are not read. A scanned PDF is ingested with 0 chunks and no error.
* If you restore the vector store service from a backup, or you change or delete its data directly, the knowledge base can fall out of step with the documents it lists. AI Retrieval does not detect this. Add the affected documents again to restore consistency.
* If you remove a file from a bucket, AI Retrieval does not remove its document from the knowledge base. Delete the document in the knowledge base.
* Deleting a knowledge base or a data source does not delete the chunks that it stored in the vector store service. Deleting a single document does delete its chunks.
* Ingesting many large documents can take hours. A file that times out is retried once at the end of the sync. Run the sync again to ingest the files that still failed.
* If you delete the MariaDB service that stores the vectors, the knowledge base still shows **Ready**, but requests to it fail.
* Ingesting many documents into a vector store on a small Serverless instance can be slow or stall.
* The document status in the portal can lag. A document can show **Queued** or **Retrying** while you can already retrieve its content. See [Troubleshooting](document-knowledge-bases.md#troubleshooting).

<!-- Limitations list for Support from Vijay and Karan, launch channel 2026-10-30 (Zhanna's thread p1793334510708199): BYOC not supported; no sync scheduler; embedding model fixed; multi-turn not supported for document KBs; scanned docs return empty chunks without an error; images dropped; password-protected files not handled; English only. -->

<!-- TODO: re-verify these limitations before the launch. Egor confirmed on 2026-10-14 that deleting a knowledge base or data source keeps its chunks. The deleted vector store service and small Serverless instance limitations come from Jira (MCDEV-5449, MCDEV-5426, MCDEV-5330) and Slack, not from code. -->

<!-- TODO: Egor's layout document says that agentic retrieval, bring your own model, PrivateLink, scheduled syncs, and external databases are roadmap items that belong only on this list. Add the ones that Egor confirms. Also settle whether multi-turn conversations are in the preview (Vijay said single-turn on 2026-10-01; MCDEV-3429 says otherwise). -->

## Next Steps

{% content-ref url="quickstart.md" %}
[quickstart.md](quickstart.md)
{% endcontent-ref %}

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

{% content-ref url="database-knowledge-bases.md" %}
[database-knowledge-bases.md](database-knowledge-bases.md)
{% endcontent-ref %}

{% content-ref url="parsing-and-chunking.md" %}
[parsing-and-chunking.md](parsing-and-chunking.md)
{% endcontent-ref %}

{% content-ref url="supported-models-formats-and-regions.md" %}
[supported-models-formats-and-regions.md](supported-models-formats-and-regions.md)
{% endcontent-ref %}

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

{% content-ref url="service-quotas.md" %}
[service-quotas.md](service-quotas.md)
{% endcontent-ref %}

{% content-ref url="usage-and-billing.md" %}
[usage-and-billing.md](usage-and-billing.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
