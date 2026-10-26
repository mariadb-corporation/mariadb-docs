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

The pages in this section describe the document knowledge base in detail.

<!-- TODO: write the database knowledge base page. Vijay confirmed on 2026-10-13 that it is in scope. Egor (2026-10-14): ask Ryan Killea for the source. -->

## How It Works

### Document Knowledge Bases

1. You create a knowledge base. MariaDB Cloud stores its vectors in a MariaDB Serverless service, which it can provision for you.
2. You add documents by uploading files or by connecting an Amazon S3 or Google Cloud Storage bucket.
3. AI Retrieval parses each document, splits the text into chunks, creates an embedding for each chunk, and stores both in the vector store.
4. Your application sends a question to the knowledge base endpoint.
5. AI Retrieval searches the chunks, ranks them, and returns the best matches. For a generated answer, it passes the best chunks to a generation model, which writes the answer and cites the chunks that it used.

### Database Knowledge Bases

1. You create a knowledge base from a schema of a MariaDB service.
2. You synchronize the knowledge base. AI Retrieval reads the tables and columns that the database user can see, and builds a description of them, called the semantic map.
3. Your application sends a question to the knowledge base endpoint.
4. AI Retrieval uses the semantic map to turn the question into an SQL query, checks that the query only reads data, runs it, and returns the rows. For a generated answer, it writes the answer from the rows.

<!-- TODO: the database knowledge base steps come from the product requirements and Egor's layout document, not from code. The code is on the unmerged branch feature/MCDEV-3646-DBKB of skysql-gen-ai. Verify the steps, the read-only check, and the limits (100 tables, 1,000 columns, a row limit, and a query timeout) against the merged code. -->

## Key Concepts

| Concept | Meaning |
| --- | --- |
| Knowledge base | The searchable collection that you create and query. It has a type, a cloud region, and settings such as the models and the reranker. |
| Vector store | The MariaDB service that stores the chunks and embeddings of a document knowledge base. |
| Document | A file in a document knowledge base. |
| Data source | An Amazon S3 or Google Cloud Storage bucket that is connected to a document knowledge base. |
| Chunk | A passage of a document. A retrieval request returns chunks. |
| Embedding | A list of numbers that represents the meaning of a chunk. AI Retrieval compares the embedding of a question with the embeddings of the chunks to find related text. |
| Sync | The action that ingests the new and changed files of a data source, or builds the semantic map of a database. AI Retrieval does not sync by itself. |
| Semantic map | The description of the tables and columns of a database that AI Retrieval builds for a database knowledge base. |
| Reranker | A model that re-scores the retrieved chunks. |
| Generation model | The LLM that writes an answer from the retrieved content. |
| API key | The credential that your application uses to call a knowledge base. |

## Retrieval Modes

| Mode | Result |
| --- | --- |
| Retrieve | The most relevant chunks for the question, without a generated answer |
| Retrieve & Generate | An answer that the knowledge base's generation model creates from the retrieved chunks, with citations to the chunks used |

Both modes search with one of three methods.

| Method | How it searches |
| --- | --- |
| Hybrid (default) | Combines semantic and full-text search |
| Semantic | Matches the meaning of the question |
| Full text | Matches the keywords in the question |

Retrieve & Generate can stream the answer as it is generated.

## Requirements and Availability

* Knowledge bases run on AWS.
* The vector store must be a MariaDB service in the same cloud and region as the knowledge base, running MariaDB 11.8 or later. You can select an existing service that meets this requirement or let MariaDB Cloud provision a new MariaDB Serverless instance.
* Your role decides what you can do with knowledge bases. See [Access and Security](access-and-security.md#roles-and-permissions).
* You need an API key to call the REST API from an application. See [Connect Your Application](document-knowledge-bases.md#connect-your-application).

<!-- TODO: confirm the AWS regions available at launch. The test environment offers only eu-central-1. Egor said the regions follow the product requirements page (us-east-1, eu-west-2, eu-central-1, ap-southeast-1 in NFR-CLO-01). Google Cloud and Azure open a Register Interest dialog. -->

## Supported Files and Limits

The portal accepts these file types:

| Format | Extension |
| --- | --- |
| Text | `.txt` |
| Markdown | `.md` |
| Web page | `.html` |
| JSON | `.json` |
| Microsoft Word | `.docx` |
| PDF | `.pdf` |
| Microsoft PowerPoint | `.pptx` |

When you upload files from your computer, you can select up to 5 files at a time, and each file can be up to 50 MB.

AI Retrieval cannot parse scanned documents, which are PDFs that contain only images of pages. It uses OCR only to detect the layout of a document, not to read scanned pages. Password-protected PDFs are not supported. Documents must be in English.

<!-- TODO: English only and no password-protected PDFs come from Egor (2026-10-14, MCDEV-5201) and Slack, not from code. -->

## Quotas

AI Retrieval applies these default quotas.

| Quota | Default | Scope |
| --- | --- | --- |
| Requests per second to `retrieve-chunks` | 2 | Each user |
| Requests per second to `retrieve-chunks-and-generate`, including streaming | 2 | Each user |
| Document size | 50 MB | Each document |
| Concurrent ingestion jobs | 5 | Each organization in a region |
| Concurrent data source syncs | 5 | Each organization in a region |

When you exceed a request limit, the API returns HTTP status 429.

<!-- TODO: confirm with Vijay or Ryan that support can change these limits and whether the daily request quotas per organization still apply. Source: ai-retrieval-cloud packages/quotas catalog and cp_catalog_seed.json @ 5393bced; Egor, 2026-10-14: "Quotas as PRD but per user". Egor's layout document also lists 5 database knowledge bases per organization; verify. -->

## Known Limitations

* Syncs are manual. AI Retrieval does not ingest the documents of a data source automatically, so run a sync whenever you add files to the bucket.
* If you restore the vector store service from a backup, or you change or delete its data directly, the knowledge base can fall out of step with the documents it lists. AI Retrieval does not detect this. Add the affected documents again to restore consistency.
* If you remove a file from a bucket, AI Retrieval does not remove its document from the knowledge base. Delete the document in the knowledge base.
* Deleting a knowledge base or a data source does not delete the chunks that it stored in the vector store service. Deleting a single document does delete its chunks.
* Ingesting many large documents can take hours. A file that times out is retried once at the end of the sync. Run the sync again to ingest the files that still failed.
* If you delete the MariaDB service that stores the vectors, the knowledge base still shows **Ready**, but requests to it fail.
* Ingesting many documents into a vector store on a small Serverless instance can be slow or stall.
* The document status in the portal can lag. A document can show **Queued** or **Retrying** while you can already retrieve its content. See [Troubleshooting](document-knowledge-bases.md#troubleshooting).

<!-- TODO: re-verify these limitations before the launch. Egor confirmed on 2026-10-14 that deleting a knowledge base or data source keeps its chunks. The deleted vector store service and small Serverless instance limitations come from Jira (MCDEV-5449, MCDEV-5426, MCDEV-5330) and Slack, not from code. -->

<!-- TODO: Egor's layout document says that agentic retrieval, bring your own model, PrivateLink, scheduled syncs, and external databases are roadmap items that belong only on this list. Add the ones that Egor confirms. Also settle whether multi-turn conversations are in the preview (Vijay said single-turn on 2026-10-01; MCDEV-3429 says otherwise). -->

## Next Steps

{% content-ref url="quickstart.md" %}
[quickstart.md](quickstart.md)
{% endcontent-ref %}

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

{% content-ref url="parsing-and-chunking.md" %}
[parsing-and-chunking.md](parsing-and-chunking.md)
{% endcontent-ref %}

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
