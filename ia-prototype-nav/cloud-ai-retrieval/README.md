---
title: Cloud AI Retrieval
description: >-
  Cloud AI Retrieval provides managed vector search and retrieval on
  MariaDB Cloud for AI and RAG applications.
icon: robot
---

# Cloud AI Retrieval

Cloud AI Retrieval is the managed retrieval capability of MariaDB Cloud. It stores embedding vectors alongside your relational data and serves similarity search over them, which is the retrieval half of a retrieval augmented generation application.

The reason to keep retrieval in the database is that most real queries are not purely semantic. A useful search is a similarity match constrained by things the relational data knows: this customer, this date range, this document type, this permission. When the vectors and the rows live in one system, that is a single SQL statement against consistent data. When they live in separate systems, it becomes two queries and a join you write and maintain yourself.

MariaDB Cloud runs the same `VECTOR` column type and vector indexing as the self managed server, so a schema you develop on MariaDB Server works here. What the service adds is the operation of it: provisioning, scaling, and index maintenance.

**Get started.** Provision a database, create a table with a `VECTOR` column and an index, and run a similarity query. Getting one query returning ranked rows is the checkpoint worth reaching before adding a framework.

**Connect your application.** Most applications generate embeddings in an AI framework rather than in SQL. The guides cover connecting the common frameworks so that embeddings your application produces are written here and queried with the same SQL.

**Understand how retrieval behaves.** The concepts pages cover distance functions, index behavior, and the accuracy and speed trade-off an approximate index makes, which is what determines whether your results are good enough.

Create a `VECTOR` column, load a sample of your own embeddings, and check whether the top results are the ones you expected.

## Get Started

{% content-ref url="get-started/install-cloud-ai-retrieval.md" %}
[install-cloud-ai-retrieval.md](get-started/install-cloud-ai-retrieval.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-cloud-ai-retrieval.md" %}
[connect-to-cloud-ai-retrieval.md](get-started/connect-to-cloud-ai-retrieval.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/cloud-ai-retrieval-tutorial.md" %}
[cloud-ai-retrieval-tutorial.md](tutorials/cloud-ai-retrieval-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-cloud-ai-retrieval.md" %}
[configure-cloud-ai-retrieval.md](how-to-guides/configure-cloud-ai-retrieval.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-cloud-ai-retrieval.md" %}
[secure-cloud-ai-retrieval.md](how-to-guides/secure-cloud-ai-retrieval.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-cloud-ai-retrieval.md" %}
[what-is-cloud-ai-retrieval.md](overview/what-is-cloud-ai-retrieval.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-cloud-ai-retrieval-works.md" %}
[how-cloud-ai-retrieval-works.md](concepts/how-cloud-ai-retrieval-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/cloud-ai-retrieval-reference.md" %}
[cloud-ai-retrieval-reference.md](reference/cloud-ai-retrieval-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/cloud-ai-retrieval-releases.md" %}
[cloud-ai-retrieval-releases.md](release-notes/cloud-ai-retrieval-releases.md)
{% endcontent-ref %}
