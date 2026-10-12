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

<!-- TODO: confirm the public name of the release stage. Jira and Slack say "Tech Preview"; the portal shows "Public Preview". -->

{% hint style="info" %}
AI Retrieval is in Public Preview. Behavior and limits can change before general availability.
{% endhint %}

## Knowledge Base Types

| Type | Content | Status in this guide |
| --- | --- | --- |
| Document knowledge base | Files such as PDF, Word, PowerPoint, Markdown, and HTML documents | Covered |
| Database knowledge base | Tables of an existing MariaDB service, queried in natural language | Not covered yet |

<!-- TODO: confirm that database knowledge bases are available in the preview and document them separately. -->

## How It Works

1. You create a knowledge base. MariaDB Cloud stores its vectors in a MariaDB Serverless service, which it can provision for you.
2. You add documents by uploading files or by connecting an Amazon S3 or Google Cloud Storage bucket.
3. AI Retrieval parses each document, splits the text into chunks, creates an embedding for each chunk, and stores both in the vector store.
4. Your application sends a question to the knowledge base endpoint.

## Retrieval Modes

| Mode | Result |
| --- | --- |
| Retrieve | The most relevant chunks for the question, without a generated answer |
| Retrieve & Generate | An answer that the knowledge base's LLM generates from the retrieved chunks, with citations to the chunks used |

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
* You need an API key to call the REST API from an application. See [Connect Your Application](document-knowledge-bases.md#connect-your-application).

## Supported Files and Limits

The portal accepts these file types:

| Format | Extensions |
| --- | --- |
| Text and Markdown | `.txt`, `.md` |
| Web pages | `.html` |
| Microsoft Word | `.doc`, `.docx` |
| PDF | `.pdf` |
| Microsoft PowerPoint | `.ppt`, `.pptx` |
| Spreadsheets and CSV | `.xlsx`, `.csv` |

<!-- TODO: confirm CSV and XLSX. The portal accepts them, but the product team moved both formats out of the preview scope on 2026-10-05. -->

When you upload files from your computer, you can select up to 5 files at a time, and each file can be up to 50 MB.

AI Retrieval cannot parse scanned documents, which are PDFs that contain only images of pages.

## Known Limitations

* If you restore the vector store service from a backup, or you change or delete its data directly, the knowledge base can fall out of step with the documents it lists. AI Retrieval does not detect this. Add the affected documents again to restore consistency.
* The document status in the portal can lag. A document can show **Queued** or **Retrying** while you can already retrieve its content. See [Troubleshooting](document-knowledge-bases.md#troubleshooting).

<!-- TODO: re-verify both limitations before the launch. Source: Slack #ai-retrieval-launch-tp-mcdev-2634 (2026-09-15) and the ingestion service retry code. -->

## Next Steps

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
