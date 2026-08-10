# MariaDB AI RAG 1.0.0 Release Notes

The MariaDB AI RAG API is a tech preview of an enterprise-grade Retrieval-Augmented Generation (RAG) solution that provides a simple, configurable REST API for ingesting documents and retrieving information from them. It is designed to be used as a building block for larger AI RAG systems.

As a REST API with controls around visibility of documents and chunks, with options for full pipeline orchestration, it simplifies the process of implementing a RAG system compared to approaches that require users to learn and implement the ingestion, chunking, and retrieval programmatically for each application separately.

We plan to do multiple releases of this tech preview to continue to improve the system and incorporate feedback from users.

## Key Features

* RAG API endpoints for document ingestion and chunking
* User and document management endpoints
* JWT authentication for API access
* Support for multiple document formats (PDF, DOCX, TXT, CSV, XLSX)
* MariaDB vector index integration for efficient document search
* Retrieval options include semantic search, hybrid search, and fulltext search
* Support for multiple retrieval and generation models (e.g. OpenAI, Cohere, etc.)
* Support for key vaults to make configuration of sensitive information easier

## Packaging

* RPM, DEB, and MSI installers for RHEL, Ubuntu, and Windows are provided

## Installation

* Using the platform's installer file (.msi, .rpm, or .deb) run the installer
* Then follow the installation instructions in the AI RAG API documentation

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
