---
description: >-
  MariaDB Cloud AI Retrieval indexes your documents in a knowledge base and
  returns relevant passages or generated answers through a REST API.
icon: magnifying-glass
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Open items are marked TODO. -->

# AI Retrieval

AI Retrieval is a MariaDB Cloud service that indexes your content in a knowledge base. Your applications query the knowledge base through a REST API and receive either the most relevant passages or an answer that a large language model (LLM) generates from them.

{% hint style="info" %}
AI Retrieval is in Public Preview. Behavior and limits can change before general availability.
{% endhint %}

## Knowledge Base Types

| Type | Content | Status in this guide |
| --- | --- | --- |
| Document knowledge base | Files such as PDF, Word, PowerPoint, Markdown, and HTML documents | Covered |
| Database knowledge base | Tables of an existing MariaDB service, queried in natural language | Not covered yet |

<!-- TODO: write the database knowledge base page. Vijay confirmed on 2026-10-13 that it is in scope. Egor (2026-10-14): ask Ryan Killea for the source. -->

## How It Works

1. You create a knowledge base. MariaDB Cloud stores its vectors in a MariaDB Serverless service, which it can provision for you.
2. You add documents by uploading files or by connecting an Amazon S3 or Google Cloud Storage bucket.
3. AI Retrieval parses each document, splits the text into chunks, creates an embedding for each chunk, and stores both in the vector store.
4. Your application sends a question to the knowledge base endpoint.

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

* Knowledge bases run on AWS. <!-- TODO: confirm the AWS regions available at launch. The test environment offers only eu-central-1. -->
* The vector store must be a MariaDB service in the same cloud and region as the knowledge base, running MariaDB 11.8 or later. You can select an existing service that meets this requirement or let MariaDB Cloud provision a new MariaDB Serverless instance.
* Users with the Viewer role can view knowledge bases but cannot create or change them.
* You need an API key to call the REST API from an application. See [Connect Your Application](document-knowledge-bases.md#connect-your-application).

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

<!-- TODO: confirm with Vijay or Ryan that support can change these limits and whether the daily request quotas per organization still apply. Source: ai-retrieval-cloud packages/quotas catalog and cp_catalog_seed.json @ 5393bced; Egor, 2026-10-14: "Quotas as PRD but per user". -->

## Known Limitations

* If you restore the vector store service from a backup, or you change or delete its data directly, the knowledge base can fall out of step with the documents it lists. AI Retrieval does not detect this. Add the affected documents again to restore consistency.
* If you remove a file from a bucket, AI Retrieval does not remove its document from the knowledge base. Delete the document in the knowledge base.
* Deleting a knowledge base or a data source does not delete the chunks that it stored in the vector store service. Deleting a single document does delete its chunks.
* Ingesting many large documents can take hours. A file that times out is retried once at the end of the sync. Run the sync again to ingest the files that still failed.
* If you delete the MariaDB service that stores the vectors, the knowledge base still shows **Ready**, but requests to it fail.
* Ingesting many documents into a vector store on a small Serverless instance can be slow or stall.
* The document status in the portal can lag. A document can show **Queued** or **Retrying** while you can already retrieve its content. See [Troubleshooting](document-knowledge-bases.md#troubleshooting).

<!-- TODO: re-verify these limitations before the launch. Egor confirmed on 2026-10-14 that deleting a knowledge base or data source keeps its chunks. The deleted vector store service and small Serverless instance limitations come from Jira (MCDEV-5449, MCDEV-5426, MCDEV-5330) and Slack, not from code. -->

## Next Steps

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
