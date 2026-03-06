# MariaDB AI RAG 1.1.0 Release Notes

The MariaDB AI RAG API 1.1.0 is a beta release of our enterprise-grade Retrieval-Augmented Generation (RAG) solution. This version introduces major improvements across the ingestion and retrieval pipeline—especially for complex document layouts and large document libraries.

By deploying as a containerized stack, it simplifies the process of implementing a RAG system by providing layout-aware extraction, incremental S3 syncing, and automated reranking within a single, repeatable deployment. This release builds upon the REST API foundation of the tech preview to offer higher precision and more transparent, citation-backed outputs.

### Key Features

* Layout-based text extraction: Built-in Docling and LlamaParse integration improves ingestion quality for complex PDFs, tables, and multi-column documents.
* Incremental S3 Ingestion: Bulk document ingestion from S3-compatible storage with incremental sync to process only new or changed documents.
* Cross-encoder reranker: Integration with Cohere (managed) and Flashrank (built-in/local) to select the most relevant context and reduce hallucinations.
* Answer Citations: Increases trustworthiness by showing which documents or chunks were used to generate specific parts of the output.
* Docker Deployment: Ability to spin up all pipeline components, including the parsing engine and MCP Server, in a single step.
* MariaDB Vector Integration: Efficient document search using MariaDB 10.8 or later with vector index integration for semantic, hybrid, and full-text retrieval.

### Packaging

* Docker: MariaDB AI RAG 1.1.0 is provided as a containerized stack.

### Installation

* Deploy MariaDB AI RAG as a containerized stack using Docker to spin up all RAG pipeline components.
* For quick evaluation, you can optionally run a MariaDB 10.8 vector store in a container alongside the AI RAG stack to get an end-to-end setup in minutes.
* This release is available for evaluation through a trial license.
