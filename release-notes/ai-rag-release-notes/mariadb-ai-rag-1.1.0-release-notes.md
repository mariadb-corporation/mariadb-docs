---
hidden: true
noIndex: true
---

# MariaDB AI RAG 1.1.0 Release Notes

**Release Date:** 31 Mar 2026

Release 1.1.0 is a Beta release.

MariaDB AI RAG 1.1.0 introduces major improvements across the ingestion and retrieval pipeline—especially for complex document layouts and large document libraries.&#x20;

MariaDB AI RAG is currently in beta and can be evaluated with a trial license. This release adds layout-aware text extraction, incremental S3 ingestion, cross-encoder reranking, Docker-based deployment, and answer citations.

### New Features and Improvements

#### Layout-based text extraction (Built-in Docling + LlamaParse integration)

Improve ingestion quality for complex PDFs and other layout-heavy documents (tables, multi-column pages, headers/footers) using layout-aware extraction via Docling and LlamaParse. Cleaner extraction leads to better chunk boundaries and embeddings, and ultimately more accurate retrieval—especially when plain text extraction loses reading order or structure.

#### Bulk documents Ingestion from S3 storage with incremental sync

Ingest large document collections directly from S3-compatible object storage (bucket/prefix) and keep them up to date with incremental sync—processing only new or changed documents instead of re-ingesting everything. This turns S3 Storage into a scalable source of truth for your knowledge base while keeping indexing cost under control.

#### Cross-encoder reranker (Built-in Flashrank + Cohere integration)&#x20;

Improve answer quality by reranking retrieved passages with a cross-encoder, so the system selects the most relevant context before generating a response. MariaDB AI RAG 1.1.0 supports Cohere reranking for managed, high-quality ranking and includes Flashrank as a built-in option for lightweight, local reranking—helping reduce hallucinations and boosting precision on ambiguous queries.

#### Docker deployment

Deploy MariaDB AI RAG as a containerized stack using Docker, so you can spin up all RAG pipeline components—including Docling for document parsing and the MCP Server—with a single, repeatable step. For quick evaluation, you can also use a MariaDB vector store deployed in a container alongside the AI RAG stack to get an end-to-end setup in minutes.

#### Citation of generated answer

Make responses more trustworthy by having citations alongside the generated answer—so users and applications can see which documents/chunks were used to generate each paragraph in the generated output.

### Packaging

* MariaDB AI RAG 1.1.0 is delivered as a suite of Docker containers managed by Docker Compose.

{% hint style="warning" %}
**Deprecation Note**

Packager-based deployments (RPM, DEB, and MSI) provided in version 1.0.0 are no longer available.
{% endhint %}

### Installation

* Follow the [Deployment Guide](https://app.gitbook.com/s/kuTXWg0NDbRx6XUeYpGD/mariadb-ai-rag/deployment/overview) in the [MariaDB AI RAG documentation](https://app.gitbook.com/s/kuTXWg0NDbRx6XUeYpGD/mariadb-ai-rag) for installation and initial setup.

