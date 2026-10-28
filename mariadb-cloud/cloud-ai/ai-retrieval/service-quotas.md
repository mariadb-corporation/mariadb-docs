---
description: >-
  The default service quotas of MariaDB Cloud AI Retrieval, what happens when
  you reach one, and how to request a higher quota.
icon: gauge
hidden: true
---

<!-- DRAFT for DOCS-6592. Hidden until the Public Preview launch. Values confirmed by Karan Siddhpura (DOCS-6592 comment 1144511; Slack DM 2026-10-28) against the quota catalog in skysql-microservices ai-service (migrations 21 and 23) and ai-retrieval-cloud packages/quotas. Egor (2026-10-26): do not publish the ranges; tell customers to contact support. Open items are marked TODO. -->

# Service Quotas

AI Retrieval applies service quotas to each organization. The quotas below are the defaults. To request a higher quota, contact [MariaDB support](../../reference/support.md).

## Request Rates

| Quota | Default | Scope |
| --- | --- | --- |
| Requests per second to `retrieve-chunks` | 2 | Each organization in a region |
| Requests per second to `retrieve-chunks-and-generate`, including streaming | 2 | Each organization in a region |
| Requests per second to list the chunks of a knowledge base | 2 | Each organization in a region |

All users and API keys of an organization share these limits.

When a request exceeds a rate quota, the API returns HTTP status 429 with the error `ERR_RATE_LIMITED`. The `Retry-After` header says how many seconds to wait, and the `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` headers show the state of the limit. The error message names the quota ID to quote when you ask support for a higher quota.

## Documents and Ingestion

| Quota | Default | Scope |
| --- | --- | --- |
| Document size | 50 MB | Each document |
| Files per upload session, in the API | 100 | Each upload session |
| Pending upload sessions | 5 | Each knowledge base |
| Concurrent ingestion jobs | 5 | Each organization in a region |
| Concurrent data source syncs | 5 | Each organization in a region |

The portal uploads at most 5 files at a time, each up to 50 MB.

A data source sync over the limit is not rejected. It waits and starts by itself when a sync slot is free.

<!-- TODO: Karan has not answered whether Egor's ingestion model (tasks of up to 20 documents and under 20 MB, documents processed in 10-page batches, 3 tasks per organization per region) replaces "5 concurrent ingestion jobs" as the customer-facing limit, nor what a customer sees when a size, concurrency, or count quota is reached (Slack DM 2026-10-27 questions 1 and 7). Update this table and add the error behavior when he does. -->

## Monthly MCU Limit

AI Retrieval also limits the MCUs that an organization can consume each month. See [Usage and Billing](usage-and-billing.md#monthly-mcu-limit).

<!-- Database knowledge base quotas (database knowledge bases per organization, indexed tables and columns, retrieve rows rates) exist in the catalog but are switched off and not checked anywhere (Karan, 2026-10-26). Do not document them until they are on. No daily request limits apply (Karan). -->

## Next Steps

{% content-ref url="usage-and-billing.md" %}
[usage-and-billing.md](usage-and-billing.md)
{% endcontent-ref %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
