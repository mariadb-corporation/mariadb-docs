---
description: >-
  Build a visual RAG application on Langflow, using GridGain 8 vector search with HNSW as the vector store and chat memory, no code required.
---

# How to Build a Low-Code RAG Application With GridGain and Langflow

## Prerequisites

- A running **GridGain 8** cluster with vector search enabled
- [**Langflow**](https://www.langflow.org/) installed and running
- An LLM provider account with an API key (for example, OpenAI)

## Overview

Langflow is a no-code platform that makes building AI applications visual and intuitive. It is like a visual programming tool for LangChain - you can drag, drop, and connect components to create AI workflows without writing code.

GridGain extends Langflow with two key components:

1. **Vector Store**
   - Implements the HNSW (Hierarchical Navigable Small World) algorithm for efficient similarity search
   - Sub-millisecond query latency for vector similarity searches
   - Real-time indexing of new vectors without blocking read operations
   - Horizontal scaling across multiple nodes
2. **Chat Memory**
   - Distributed session management with consistent hashing
   - In-memory storage with disk persistence for durability
   - Automatic failover and data replication
   - Session data partitioning for optimal performance
   - Built-in TTL (Time-To-Live) management for sessions

This guide walks through a practical example that uses these capabilities, then points you to a fully functional demo project you can run yourself.

## Real-Time Product Updates: A Practical Example

The [dynamic product information system](https://github.com/GridGain-Demos/langflow_example) uses GridGain's capabilities in Langflow. Here is the technical breakdown.

### The Challenge

Imagine an online store where prices, availability, and delivery times change constantly. You need to:

- Update product info instantly
- Help customers find similar products
- Remember customer preferences
- Give accurate, up-to-date answers

### How GridGain Helps

1. **Quick Updates**
   - New prices instantly reflected in search
   - Availability status always current
   - Delivery times automatically adjusted
2. **Smart Search**
   - Finds similar products even as data changes
   - Keeps recommendations fresh
3. **Personal Experience**
   - Remembers what each customer likes
   - Maintains conversation context
   - Gives consistent responses across sessions

### System Architecture

The system integrates three main components:

1. Real-time data ingestion pipeline
2. Vector search infrastructure
3. Conversational AI interface

### Technical Implementation

1. **Data Management**
   - Product embeddings generated using OpenAI's text-embedding-ada-002 model
   - Vectorized product data stored in GridGain's Vector Database
2. **Search Infrastructure**
   - Cosine similarity computations
   - Configurable number of nearest neighbors (k-NN search)
3. **Conversation Handling**
   - Session management through distributed key-value storage
   - Conversation context maintained using Langflow's Memory component
   - Automatic session cleanup through TTL mechanisms
   - Load balancing of chat requests across nodes

This implementation demonstrates how GridGain's distributed computing capabilities can be leveraged within Langflow to create a responsive, scalable product search system that handles real-time updates efficiently while maintaining high availability and consistent performance.

## Demonstration Project

A fully functional demo project is available on GitHub in the [Langflow demo](https://github.com/GridGain-Demos/langflow_example) repository. It includes functional sample code, as well as step-by-step instructions on setting up and running the project.

## Related

- [Langflow](https://www.langflow.org/) - The no-code platform used to build the visual AI workflow.
- [Langflow demo repository](https://github.com/GridGain-Demos/langflow_example) - The full sample project with setup instructions.
