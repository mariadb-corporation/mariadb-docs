---
description: >-
  How MariaDB Cloud AI Retrieval measures usage in MariaDB Compute Units (MCUs)
  for document knowledge bases and database knowledge bases.
icon: receipt
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Built from the call of 2026-10-22: MCU consumption only, no prices, separate tables for document and database knowledge bases. Open items are marked TODO. -->

# Usage and Billing

AI Retrieval measures usage in MariaDB Compute Units (MCUs), the same unit that MariaDB Cloud uses for Serverless services. This page shows how many MCUs each operation consumes. The price of an MCU depends on your plan, the cloud, and the region. See [Pricing](../../reference/pricing.md).

<!-- TODO: add the AI Retrieval section to the Pricing page, as Egor suggested, or link this page from it. Egor left the choice to the writer. -->

## What You Pay For

* **The vector store.** A document knowledge base stores its chunks in a MariaDB service. You pay for that service as for any other service, including its compute and storage.
* **AI Retrieval operations.** Parsing, embedding, reranking, generating answers, and the other operations in the tables below consume MCUs.

<!-- TODO: say how the MCUs of the operations appear on the invoice and in the portal billing page. Egor did not cover it. -->

## Monthly MCU Limit

Each organization has a monthly limit on the MCUs that AI Retrieval operations consume. The default limit is 100 MCUs per month. When the organization reaches its limit, AI Retrieval rejects new uploads, data source syncs, and retrieval and generation requests with HTTP status 403 and the error `ERR_MCU_LIMIT_REACHED` until the next month starts. Files of a sync that are over the limit are not ingested. To raise the limit, contact MariaDB support.

<!-- Source: ai-retrieval-cloud packages/metering limits.py and config.py @ f9bd8c0e (MCDEV-5410, MCDEV-5494, MCDEV-5507: default 100, per-org override, 403 ERR_MCU_LIMIT_REACHED; enforced on upload, data source sync, retrieval, and generation). TODO: the limit is off by default in the code (metering_limit_enabled); confirm it is on at launch, whether the 100 MCUs are a free tier that applies to every organization or a spend cap for card-billed organizations (Naman, 2026-09-02; Egor's layout document mentions a 4,000 MCU cap), whether customers can see their usage (GET /usage/mcu, MCDEV-5507), and who can raise the limit. -->

## Document Knowledge Bases

| Operation | Unit | MCUs |
| --- | --- | --- |
| Parsing with the Base parser | 1,000 pages | 6 |
| Parsing with the Layout-aware parser | 1,000 pages | 48 |
| Embedding | 1 million input tokens | Depends on the embedding model. See the table below. |
| Retrieve chunks | 1,000 queries | 0 |
| Reranking | 1,000 queries | 6 |
| Generating an answer, input | 1 million input tokens | Depends on the generation model. See the table below. |
| Generating an answer, output | 1 million output tokens | Depends on the generation model. See the table below. |

Embedding consumption per 1 million input tokens:

| Embedding model | MCUs |
| --- | --- |
| Cohere Embed 3 English | 1.33 |
| Cohere Embed 3 Multilingual | 1.33 |
| Cohere Embed 4 | 1.60 |
| Gemini Embedding 2 | 2.67 |

Generation consumption per 1 million tokens:

| Generation model | MCUs per 1 million input tokens | MCUs per 1 million output tokens |
| --- | --- | --- |
| Claude Sonnet 5 | 26.67 | 133.33 |
| Claude Opus 5 | 66.67 | 333.33 |
| Claude Fable 5.1 | 133.33 | 666.67 |
| Gemini 3.8 Flash | 20.00 | 100.00 |

<!-- TODO: the rows come from the AI Retrieval pricing sheet that Egor shared (tabs Pricing overview, Embedding, Generate), as MCU columns only. Do not copy any dollar column, margin, or competitor figure. Verify the numbers with Egor before unhiding. -->
<!-- Egor, 2026-10-26: add Claude Fable 5.1 (pricing sheet Generate tab: 133.33 / 666.67 MCUs per 1M input / output tokens). Kimi K2.5 has no MCU rate in the sheet and is not listed. -->
<!-- TODO: confirm that the Layout-aware figure of 48 MCUs per 1,000 pages is for digital documents and that scanned documents (80) are out of scope, because AI Retrieval does not parse scanned documents. Egor said on 2026-10-22 not to include scanned or image parsing. -->
<!-- The units match the Price per component slide of the October release deck, which Egor showed on 2026-10-22: embedding and generation per 1M tokens (marked as varying with the model), parsing per 1K pages, reranking per 1K queries, semantic map per operation, Retrieve rows per query. Egor said to enter 0 for Retrieve chunks. Whether the query embedding is included is not stated. -->

## Database Knowledge Bases

| Operation | Unit | MCUs |
| --- | --- | --- |
| Creating or updating the semantic map | Operation | 16 |
| Retrieve rows | Query | 0.5 |
| Generating an answer from rows | 1 million tokens | The same rates as the generation of a document knowledge base, for the generation model that AI Retrieval uses. |

<!-- TODO: confirm the rates for the generation model of a database knowledge base (GPT 5.6 Luna). The pricing sheet and the slide show the generation rates of the document knowledge base models, as "Generate (Unstructured and Structured RAG)". -->

## Next Steps

{% content-ref url="supported-models-formats-and-regions.md" %}
[supported-models-formats-and-regions.md](supported-models-formats-and-regions.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
