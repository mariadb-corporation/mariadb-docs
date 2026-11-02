---
description: >-
  MariaDB Cloud AI Retrieval indexes your documents or your database in a
  knowledge base and returns relevant passages, rows, or generated answers
  through a REST API.
hidden: true
icon: magnifying-glass
---

# AI Retrieval

AI Retrieval is a managed retrieval-augmented generation (RAG) service that grounds AI and agentic applications in documents or data in MariaDB databases.

MariaDB Cloud AI Retrieval works over two kinds of data. For documents, it handles parsing, chunking, embeddings, managed vector storage, and reranking, and returns results through retrieval REST API. For data in a MariaDB database, it turns a natural-language question into SQL, runs it against the database, and returns the results also via retrieval REST API — with multi-turn follow-up requests.

{% hint style="info" %}
AI Retrieval is in Public Preview. Behavior and limits can change before general availability.
{% endhint %}

## Knowledge Base Types

| Type                    | Content                                                           | How you query it                                                                                      |
| ----------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Document knowledge base | Files such as PDF, Word, PowerPoint, Markdown, and HTML documents | You ask a question in natural language and receive the most relevant passages, or a generated answer. |
| Database knowledge base | Tables of an existing MariaDB service                             | You ask a question in natural language and receive the rows that answer it, or a generated answer.    |

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

## Key Concepts

| Concept          | Meaning                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Knowledge base   | The searchable collection that you create and query. It has a type, a cloud region, and settings such as the models and the reranker.                                                            |
| Vector store     | The MariaDB service that stores the chunks and embeddings of a document knowledge base.                                                                                                          |
| Document         | A file in a document knowledge base.                                                                                                                                                             |
| Data source      | <p>An Amazon S3 or Google Cloud Storage bucket that is connected to a document knowledge base. </p><p></p><p>And MariaDB database connected as a source to database knowledge base.</p>          |
| Chunk            | A passage of a document. A retrieval request returns chunks.                                                                                                                                     |
| Embedding        | A list of numbers that represents the meaning of a chunk. AI Retrieval compares the embedding of a question with the embeddings of the chunks to find related text.                              |
| Sync             | The action that ingests the new and changed files of a data source, or builds the semantic map of a database. AI Retrieval does not sync by itself.                                              |
| Semantic map     | The metadata layer built automatically over the source database: schema metadata (including indexes and column relations), generated table and column descriptions, and a column literals index. |
| Reranker         | A model that re-scores the retrieved chunks.                                                                                                                                                     |
| Generation model | The LLM that writes an answer from the retrieved content.                                                                                                                                        |
| API key          | The credential that your application uses to call a knowledge base.                                                                                                                              |

## Retrieval Modes

Both knowledge base types offer two modes:

| Mode                | Document knowledge base                                                                                 | Database knowledge base                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Retrieve            | The most relevant chunks for the question                                                               | The SQL query that answers the question, and its rows            |
| Retrieve & Generate | An answer that the generation model writes from the retrieved chunks, with citations to the chunks used | An answer in plain language, written from the query and its rows |

A document knowledge base searches its chunks with one of three methods.

| Method           | How it searches                        |
| ---------------- | -------------------------------------- |
| Hybrid (default) | Combines semantic and full-text search |
| Semantic         | Matches the meaning of the question    |
| Full text        | Matches the keywords in the question   |

For a document knowledge base, Retrieve & Generate can stream the answer as it is generated. A database knowledge base can keep the context of a session, so that a follow-up question builds on the earlier ones. See [Database Knowledge Bases](database-knowledge-bases.md#ask-follow-up-questions).

## Requirements and Availability

* Document knowledge bases run on AWS, in the region that you select. Database knowledge bases are available in every region. See [Supported Models, Formats, and Regions](supported-models-formats-and-regions.md#supported-regions).
* For a document knowledge base, the vector store must be a MariaDB service, Provisioned or Serverless, in the same cloud and region as the knowledge base, running MariaDB 11.8 or later. You can select an existing service or let MariaDB Cloud provision a new Serverless service.
* For a database knowledge base, you need a MariaDB service with your data, a database user that can read it, and the AI Retrieval IP address in the IP allowlist of the service. See [Access and Security](access-and-security.md#database-knowledge-bases).
* Your role decides what you can do with knowledge bases. See [Access and Security](access-and-security.md#roles-and-permissions).
* You need an API key to call the REST API from an application. See [Access and Security](access-and-security.md#api-keys-and-authentication).

## Supported Files and Limits

This applies to document knowledge bases. A document knowledge base accepts TXT, Markdown, HTML, JSON, Word (DOCX), PDF, and PowerPoint (PPTX) files. See [Supported Models, Formats, and Regions](supported-models-formats-and-regions.md#supported-file-formats-for-document-knowledge-bases).

Scanned documents, which are PDFs that contain only images of pages, and password-protected files are not supported yet. Images inside documents are skipped. Documents must be in English.

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
