---
hidden: true
noIndex: true
---

# MariaDB AI RAG 1.1.0 Release Notes

## MariaDB AI RAG 1.1.0 Release Notes

MariaDB AI RAG 1.1.0 is the Beta release of our enterprise-grade Retrieval-Augmented Generation (RAG) solution. This version introduces major improvements across the ingestion and retrieval pipeline—especially for complex document layouts and large document libraries.

This release improves the system's precision and transparency by introducing layout-aware extraction, incremental S3 syncing, automated reranking, and citation-backed outputs within a single, repeatable containerized deployment.

### New Features and Improvements

* Layout-based text extraction: Includes built-in Docling (local) and LlamaParse (public endpoint) integration to improve ingestion quality for complex PDFs, tables, and multi-column documents.
* Incremental S3 Ingestion: Bulk document ingestion from S3-compatible storage with incremental sync to process only new or changed documents.
* Cross-encoder reranker: Integration with Cohere (public endpoint) and Flashrank (built-in/local) to select the most relevant context and reduce hallucinations.
* Answer Citations: Increases trustworthiness by showing which documents or chunks were used to generate specific parts of the output.
* Docker Deployment: Ability to spin up all pipeline components, including the parsing engine and MCP Server, in a single step.

### Packaging

* Docker: MariaDB AI RAG 1.1.0 is provided exclusively as a containerized stack.

{% hint style="warning" %}
**Deprecation Note**

Packager-based deployments (RPM, DEB, and MSI) provided in version 1.0.0 are no longer available.
{% endhint %}

### Installation

* Deploy MariaDB AI RAG as a containerized stack using Docker to spin up all RAG pipeline components.
* For quick evaluation, you can optionally run a MariaDB 11.8 vector store in a container alongside the AI RAG stack to get an end-to-end setup in minutes.
* This release is available for evaluation through a trial license.
