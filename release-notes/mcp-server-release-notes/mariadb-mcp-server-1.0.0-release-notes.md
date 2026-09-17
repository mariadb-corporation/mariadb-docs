# MariaDB MCP Server 1.0.0 Release Notes

The MariaDB MCP (Model Context Protocol) Server is a secure, enterprise-grade application designed to act as the primary interface between AI assistants and MariaDB data ecosystems. It provides a standardized way for AI systems to interact with databases, vector stores, and RAG workflows through the Model Context Protocol.

The MCP Server is an extension of the existing community MCP Server with authentication as well as new RAG functionality, providing a single endpoint for AI-driven data interactions with MariaDB.

We plan to do multiple releases of this tech preview to continue to improve the system and incorporate feedback from users.

## Key Features

* MCP Server tools for database operations (list databases, tables, schemas, execute SQL)
* Vector store management (create, list, delete vector stores)
* Semantic search with MariaDB vector indexes
* RAG workflow orchestration (ingestion and generation pipelines)
* JWT authentication for secure operations
* MCP standard compliance for AI assistant integration (Cursor, Windsurf, VSCode)
* Support for multiple embedding providers (OpenAI, Google Gemini, Hugging Face)
* Configurable read-only mode for enhanced security

## Packaging

* RPM, DEB, and MSI installers for RHEL, Ubuntu, and Windows are provided

## Installation

* Using the platform's installer file (.msi, .rpm, or .deb) run the installer
* Then follow the installation instructions in the MCP Server documentation

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
