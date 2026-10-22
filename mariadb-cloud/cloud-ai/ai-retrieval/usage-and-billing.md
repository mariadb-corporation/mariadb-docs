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

<!-- TODO: say how the MCUs of the operations appear on the invoice and in the portal billing page. Egor did not cover it. Also say whether a free tier applies (the product requirements say 100 MCUs per month; MCDEV-5410 enforces it). -->

## Document Knowledge Bases

| Operation | Unit | MCUs |
| --- | --- | --- |
| Parsing with the Base parser | 1,000 pages | 6 |
| Parsing with the Layout-aware parser | 1,000 pages | 48 |
| Embedding | 1 million input tokens | Depends on the embedding model. See the table below. |
| Retrieve chunks | 1,000 requests | 0 |
| Reranking | 1,000 requests | 6 |
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

<!-- TODO: the rows come from the AI Retrieval pricing sheet that Egor shared (tabs Pricing overview, Embedding, Generate), as MCU columns only. Do not copy any dollar column, margin, or competitor figure. Verify the numbers with Egor before unhiding. -->
<!-- TODO: the Generate tab also lists other models (Claude Fable 5.1, Kimi K2.5) and Google models. Add the rows for the models that the Generation Model list offers. Ask Egor which ones ship. -->
<!-- TODO: confirm that the Layout-aware figure of 48 MCUs per 1,000 pages is for digital documents and that scanned documents (80) are out of scope, because AI Retrieval does not parse scanned documents. Egor said on 2026-10-22 not to include scanned or image parsing. -->
<!-- TODO: confirm the unit of Retrieve chunks and Reranking (1,000 requests or 1,000 queries) and whether the query embedding is included. Egor said to enter 0 for Retrieve chunks. -->

## Database Knowledge Bases

| Operation | Unit | MCUs |
| --- | --- | --- |
| Creating or updating the semantic map | Operation | 16 |
| Retrieve rows | Request | 0.5 |
| Generating an answer from rows | 1 million tokens | The same rates as the generation of a document knowledge base, for the generation model that AI Retrieval uses. |

<!-- TODO: the sheet lists 0.5 MCU per request for Retrieve rows with its unit column saying per 1K queries in one place and per query in another; Egor said half an MCU per query. Confirm. Also confirm the rates for the generation model of a database knowledge base (GPT 5.6 Luna); the sheet shows the Claude Sonnet 5 rates in the Generate rows of the database section. -->

## Next Steps

{% content-ref url="supported-models-formats-and-regions.md" %}
[supported-models-formats-and-regions.md](supported-models-formats-and-regions.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
