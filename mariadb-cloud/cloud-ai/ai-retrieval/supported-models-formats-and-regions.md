---
description: >-
  The embedding and generation models, the file formats, and the regions that
  MariaDB Cloud AI Retrieval supports, and how it keeps traffic in a region.
icon: globe
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Structure follows Egor Ustinov's call of 2026-10-22: explain the approach, do not maintain a model table, and point to the Amazon Bedrock documentation. Open items are marked TODO. -->

# Supported Models, Formats, and Regions

This page lists what AI Retrieval supports and explains how it chooses the endpoint for each model.

## Models for Document Knowledge Bases

A document knowledge base uses two kinds of models. An embedding model turns each chunk and each question into an embedding. A generation model writes an answer from the retrieved chunks. You select both when you create a knowledge base. You can change the generation model for a single request, but you cannot change the embedding model after you create the knowledge base.

### Embedding Models

The create form lists the embedding models that are available in the region that you select.

| Provider | Models | Where the model runs |
| --- | --- | --- |
| Amazon Bedrock | Cohere Embed 3 English, Cohere Embed 3 Multilingual, Cohere Embed 4 | In the region of the knowledge base. Traffic does not leave the region. |
| Google | Gemini Embedding 2 | Outside your cloud. AI Retrieval calls the public Google endpoint over the internet. |

AI Retrieval calls Amazon Bedrock embedding models only through endpoints in the region of the knowledge base, and the form shows only the models that have one. Cohere Embed 3 English and Cohere Embed 3 Multilingual have regional endpoints in every region that AI Retrieval supports. Cohere Embed 4 has a regional endpoint only in `us-east-1`, so it is available only there.

<!-- TODO: confirm the model list in the create form of each region. Egor's statements are from the call of 2026-10-22; the list is from the test environment of 2026-10-20 in eu-central-1. -->

### Generation Models

Anthropic Claude models on Amazon Bedrock do not have endpoints in a single region. AI Retrieval calls them through a geographic endpoint of the area of the knowledge base, such as the United States or Europe, and through a global endpoint where no geographic endpoint is available. A generation request can therefore be processed in another region of the same geography, or outside it.

For the models and areas that Amazon Bedrock offers, see [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) and [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geo-cross-region-inference.html) in the Amazon Bedrock documentation.

<!-- TODO: list the generation models of the Generation Model list (the test environment shows Claude Sonnet 5; Egor's layout document also names Claude Opus 5 and Gemini 3.8 Flash) and say which endpoint type each one uses. Egor does not want a table of regions per model. -->

## Models for Database Knowledge Bases

A database knowledge base has no model selector. AI Retrieval does not publish the models that it uses to turn a question into an SQL query or to create embeddings of the database description.

When you use the `retrieve-rows-and-generate` endpoint to generate an answer from the rows, AI Retrieval uses GPT 5.6 Luna.

<!-- TODO: Egor gave the model name in a Slack DM on 2026-10-22 (15:11 IST) for RetrieveRowsAndGenerate on a database knowledge base. Confirm the exact name, and the endpoint name and path after the API paths are final (MCDEV-1488). -->

## Supported File Formats

A document knowledge base accepts these file types.

| Format | Extension |
| --- | --- |
| Text | `.txt` |
| Markdown | `.md` |
| Web page | `.html` |
| JSON | `.json` |
| Microsoft Word | `.docx` |
| PDF | `.pdf` |
| Microsoft PowerPoint | `.pptx` |

You can upload up to 5 files at a time, and each file can be up to 50 MB. Documents must be in English.

AI Retrieval cannot parse scanned documents, which are PDFs that contain only images of pages. It uses OCR only to detect the layout of a document, not to read scanned pages. Password-protected PDFs are not supported.

A database knowledge base reads the tables of a MariaDB service, so it has no file formats.

## Supported Regions

Document knowledge bases run on AWS, in the region that you select. The vector store service must be in the same region. These are the regions at launch:

| Region | Location |
| --- | --- |
| `us-east-1` | N. Virginia |
| `eu-west-2` | London |
| `eu-central-1` | Frankfurt |
| `ap-southeast-1` | Singapore |

Google Cloud and Azure are not available. The create form shows both and offers to register your interest.

<!-- TODO: Egor said on 2026-10-22 that four regions are planned, as in the product requirements (NFR-CLO-01), and only for document knowledge bases. Confirm which regions are live on the release date and that the names are right. The test environment offers only eu-central-1. -->

<!-- TODO: say where a database knowledge base runs and which regions it supports. -->

## Next Steps

{% content-ref url="access-and-security.md" %}
[access-and-security.md](access-and-security.md)
{% endcontent-ref %}

{% content-ref url="document-knowledge-bases.md" %}
[document-knowledge-bases.md](document-knowledge-bases.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
