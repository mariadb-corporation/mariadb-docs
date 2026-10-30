---
description: >-
  The embedding and generation models, the file formats, and the regions that
  MariaDB Cloud AI Retrieval supports, and how it keeps traffic in a region.
icon: globe
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Follows Egor Ustinov's calls of 2026-10-22 and 2026-10-26: list the models without explaining design choices, say where the traffic goes, keep quota limits on the quotas page, separate document and database knowledge bases. Open items are marked TODO. -->

# Supported Models, Formats, and Regions

This page lists the models, file formats, and regions that AI Retrieval supports.

## Models for Document Knowledge Bases

A document knowledge base uses an embedding model, which turns each chunk and each question into an embedding, and a generation model, which writes an answer from the retrieved chunks. You select both when you create a knowledge base. You can change the generation model for a single request, but you cannot change the embedding model after you create the knowledge base.

### Embedding Models

| Provider | Model | Where the model runs |
| --- | --- | --- |
| Amazon Bedrock | Cohere Embed 3 English | In the region of the knowledge base |
| Amazon Bedrock | Cohere Embed 3 Multilingual | In the region of the knowledge base |
| Amazon Bedrock | Cohere Embed 4 | In `us-east-1` only |
| Google | Gemini Embedding 2 | Outside your cloud. Traffic goes to the public Google endpoint over the internet. |

The create form lists the embedding models that are available in the region that you select. For the regions of the Cohere models, see [Cohere models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html#model-regions-cohere) in the Amazon Bedrock documentation.

### Generation Models

| Provider | Model | Where the model runs |
| --- | --- | --- |
| Amazon Bedrock | Claude Fable 5.1 | In the geography of the knowledge base, such as the United States or Europe, or globally where no geographic endpoint exists |
| Amazon Bedrock | Claude Opus 5 | The same as Claude Fable 5.1 |
| Amazon Bedrock | Claude Sonnet 5 | The same as Claude Fable 5.1 |
| Google | Gemini 3.8 Flash | Outside your cloud. Traffic goes to the public Google endpoint over the internet. |

For the regions of the Claude models, see [Anthropic models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html#model-regions-anthropic) in the Amazon Bedrock documentation.

<!-- TODO: confirm the model lists in the create form of each region before unhiding. Sources: test environment create form (2026-10-20, eu-central-1); Egor's calls of 2026-10-22 (in-region embedding, Embed 4 only in us-east-1, Claude through geographic or global endpoints, Gemini over the public endpoint) and 2026-10-26 (add Claude Fable 5.1 and Gemini 3.8 Flash; list the models, do not explain design choices); pricing sheet Generate tab. -->

## Models for Database Knowledge Bases

A database knowledge base has no model selector. To generate an answer from the rows, it uses GPT 5.6 Luna.

<!-- Egor, Slack DM 2026-10-22 15:11 IST: GPT 5.6 Luna for RetrieveRowsAndGenerate. On 2026-10-26 he asked to drop the note about undisclosed models. -->

## Supported File Formats for Document Knowledge Bases

| Format | Extension |
| --- | --- |
| Text | `.txt` |
| Markdown | `.md` |
| Web page | `.html` |
| JSON | `.json` |
| Microsoft Word | `.docx` |
| PDF | `.pdf` |
| Microsoft PowerPoint | `.pptx` |

Documents must be in English.

{% hint style="warning" %}
Scanned documents, which are PDFs that contain only images of pages, and password-protected PDFs are not supported yet.
{% endhint %}

For the maximum document size and the other limits, see [Service Quotas](service-quotas.md).

<!-- Egor, 2026-10-26: keep the upload limits of the portal (5 files at a time, 50 MB per file) off this page; quotas go on their own page. Present scanned documents as a current limitation, not a design choice. TODO: point to the Service Quotas page once it exists. -->

## Supported Regions

### Document Knowledge Bases

A document knowledge base processes your data in the region that you select: its vector store, its ingestion, and its retrieval all run in that region. Document knowledge bases run on AWS in these regions:

| Region | Location |
| --- | --- |
| `us-east-1` | N. Virginia |
| `eu-west-2` | London |
| `eu-central-1` | Frankfurt |
| `ap-southeast-1` | Singapore |

Google Cloud and Azure are not available yet. The create form shows both and offers to register your interest.

### Database Knowledge Bases

Database knowledge bases are available globally, in every region.

<!-- TODO: Egor said on 2026-10-22 that four regions are planned, as in the product requirements (NFR-CLO-01), for document knowledge bases only. On 2026-10-26 he asked to say "in-region data processing" for document knowledge bases and "available globally in every region" for database knowledge bases, without mentioning the control plane. Confirm which regions are live on the release date. The test environment offers only eu-central-1. -->

## Next Steps

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
