---
description: >-
  MariaDB Cloud 2026.11.03 is a Public Preview release, released on
  2026-11-03. It adds AI Retrieval, a managed retrieval service that answers
  questions from your documents or your MariaDB databases.
icon: rocket-launch
---

<!-- DOCS-6592. Released 2026-11-03 (AI Service production rollout, Jeet in #sky-operations). Important Notes from Egor Ustinov, Slack DM 2026-10-29 17:04 India time. Scanned-document and multi-turn limitations reworded per his DM of 2026-11-03 18:33 India time. -->

# MariaDB Cloud 2026.11.03 Release Notes: AI Retrieval

**Release Date:** 3 November 2026

Release 2026.11.03 is a Public Preview release.

## Important Notes

* **Custom agents are replaced by database knowledge bases.** To query a MariaDB Cloud database in natural language, create a database knowledge base in AI Retrieval. It turns questions into SQL (Text-to-SQL).
* **Deprecated: the Copilot API endpoints for custom agents.** They are removed when AI Retrieval becomes generally available, planned for early 2027. Migrate to database knowledge bases. The other Copilot API endpoints, such as those for the built-in agents, are not affected.

## New Features

### AI Retrieval (Public Preview)

{% hint style="info" %}
AI Retrieval is in **Public Preview**. Features, behavior, and limits may change before general availability.
{% endhint %}

AI Retrieval is a managed retrieval-augmented generation (RAG) service. You put your content in a knowledge base and query it through a REST API, or test it in the Cloud Portal. There are two types of knowledge base:

* **Document knowledge bases:** upload files, or connect an Amazon S3 or Google Cloud Storage bucket. AI Retrieval parses, chunks, and embeds the documents, and stores the chunks and embeddings in a MariaDB Provisioned or Serverless service that you select or let MariaDB Cloud provision. A request returns the most relevant chunks, or an answer generated from them, with semantic, full-text, or hybrid search and optional reranking.
* **Database knowledge bases:** connect a schema of a MariaDB service. AI Retrieval builds a semantic map of the database automatically, turns a question into a read-only SQL query, runs it, and returns the rows or an answer generated from them. A follow-up question in the same session can build on the earlier ones.

During Public Preview, each organization can use up to 100 MCUs per month for AI Retrieval at no charge. This is separate from the monthly MCU allowance of Serverless services.

For details, see [AI Retrieval](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-ai/ai-retrieval).

## Availability

* Document knowledge bases run on AWS, in a limited set of regions. Database knowledge bases are available in every region. See [Supported Models, Formats, and Regions](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-ai/ai-retrieval/supported-models-formats-and-regions).
* Not available for Bring Your Own Cloud (BYOC) organizations.
* Usage above the free tier is not available during Public Preview. When an organization reaches it, requests fail until the next month.

## Limitations

* Document knowledge bases accept TXT, Markdown, HTML, JSON, Word (DOCX), PDF, and PowerPoint (PPTX) files of up to 50 MB.
* Scanned documents and image documents are not supported yet.
* Documents must be in English.
* Bucket syncs are manual. AI Retrieval does not sync a bucket on a schedule.
* You cannot change the embedding model of a document knowledge base after you create it.
* Multi-turn queries are not supported for document knowledge bases.
* The semantic map of a database knowledge base covers up to 100 tables in each database schema and up to 1,000 columns in each table. The rest are skipped.
* Request rates, upload sessions, and concurrent ingestion are limited for each organization. See [Service Quotas](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-ai/ai-retrieval/service-quotas).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
