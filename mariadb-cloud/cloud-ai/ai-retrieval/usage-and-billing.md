---
description: >-
  How MariaDB Cloud AI Retrieval measures usage in MariaDB Compute Units (MCUs)
  for document knowledge bases and database knowledge bases.
hidden: true
icon: receipt
---

# Usage and Billing

AI Retrieval measures usage in MariaDB Compute Units (MCUs), the same unit that MariaDB Cloud uses for Serverless services. This page shows how many MCUs each operation consumes. The price of an MCU depends on your plan, the cloud, and the region. See [Pricing](../../reference/pricing.md).

## What You Pay For

* **The vector store.** A document knowledge base stores its chunks in a MariaDB service. You pay for that service as for any other service, including its compute and storage.
* **AI Retrieval operations.** Parsing, embedding, reranking, generating answers, and the other operations in the tables below consume MCUs.

Each organization has a monthly allowance of MCUs for AI Retrieval operations. The default allowance is 100 MCUs per month. It is separate from the MCU allowance of Serverless services.

The allowance applies to the whole organization, across all regions. Usage in one region can take up to about 30 minutes to count in the other regions.

Each organization has a monthly limit on the MCUs that AI Retrieval operations consume. The default limit is 100 MCUs per month. When the organization reaches its limit, AI Retrieval rejects new uploads, data source syncs, and retrieval and generation requests with HTTP status 403 and the error `ERR_MCU_LIMIT_REACHED` until the next month starts. Files of a sync that are over the limit are not ingested. To raise the limit, contact MariaDB support.

## Free Tier

Each organization can use up to 100 MCUs per month for AI Retrieval operations at no charge. The free tier is available during Public Preview and may change when AI Retrieval moves to General Availability.

> **Note (Public Preview):** Usage above the free tier isn't available. When the organization reaches 100 MCUs in a month, AI Retrieval rejects new uploads, data source syncs, and retrieval and generation requests with HTTP status 403 and the error `ERR_MCU_LIMIT_REACHED` until the next month starts. Files of a sync that are over the free tier are not ingested. To raise the limit, contact MariaDB support.

## Document Knowledge Bases

| Operation                            | Unit                    | MCUs                                                  |
| ------------------------------------ | ----------------------- | ----------------------------------------------------- |
| Parsing with the Base parser         | 1,000 pages             | 6                                                     |
| Parsing with the Layout-aware parser | 1,000 pages             | 48                                                    |
| Embedding                            | 1 million input tokens  | Depends on the embedding model. See the table below.  |
| Retrieve chunks                      | 1,000 queries           | 0                                                     |
| Reranking                            | 1,000 queries           | 6                                                     |
| Generating an answer, input          | 1 million input tokens  | Depends on the generation model. See the table below. |
| Generating an answer, output         | 1 million output tokens | Depends on the generation model. See the table below. |

Embedding consumption per 1 million input tokens:

| Embedding model             | MCUs |
| --------------------------- | ---- |
| Cohere Embed 3 English      | 1.33 |
| Cohere Embed 3 Multilingual | 1.33 |
| Cohere Embed 4              | 1.60 |
| Gemini Embedding 2          | 2.67 |

Generation consumption per 1 million tokens:

| Generation model | MCUs per 1 million input tokens | MCUs per 1 million output tokens |
| ---------------- | ------------------------------- | -------------------------------- |
| Claude Sonnet 5  | 26.67                           | 133.33                           |
| Claude Opus 5    | 66.67                           | 333.33                           |
| Claude Fable 5.1 | 133.33                          | 666.67                           |
| Gemini 3.8 Flash | 20.00                           | 100.00                           |
| GPT-5.6 Luna     | 2.67                            | 16.00                            |

## Database Knowledge Bases

| Operation                             | Unit             | MCUs                                                                                                            |
| ------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------- |
| Creating or updating the semantic map | Operation        | 16                                                                                                              |
| Retrieve rows                         | Query            | 0.5                                                                                                             |
| Generating an answer from rows        | 1 million tokens | The same rates as the generation of a document knowledge base, for the generation model that AI Retrieval uses. |

## Next Steps

{% content-ref url="supported-models-formats-and-regions.md" %}
[supported-models-formats-and-regions.md](supported-models-formats-and-regions.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
