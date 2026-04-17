---
description: >-
  LangChain integration for MariaDB, providing vector stores, chat message
  history, and natural language query capabilities.
icon: link
---

# LangChain MariaDB

The **langchain-mariadb** package provides seamless integration between [LangChain](https://python.langchain.com/) and MariaDB, enabling advanced AI and machine learning workflows with persistent storage.

## Features

- **Vector Store** - Store and search embeddings using MariaDB's vector capabilities
- **Chat Message History** - Persistent conversation storage for chatbots and AI assistants
- **Expression Filters** - Advanced metadata filtering for vector search
- **Natural Language Queries** - Translate natural language to SQL queries

## Installation

```bash
pip install langchain-mariadb
```

## Quick Start

### Vector Store Example

```python
from langchain_mariadb import MariaDBStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = MariaDBStore(
    embeddings=embeddings,
    datasource="mariadb://user:password@localhost/database",
    collection_name="my_documents"
)

# Add documents
vectorstore.add_texts(["Hello world", "LangChain with MariaDB"])

# Search
results = vectorstore.similarity_search("greeting", k=1)
```

### Chat Message History Example

```python
from langchain_mariadb import MariaDBChatMessageHistory

history = MariaDBChatMessageHistory(
    session_id="user_123",
    connection_string="mariadb://user:password@localhost/database"
)

history.add_user_message("Hello!")
history.add_ai_message("Hi! How can I help you?")
```

## Documentation

For complete documentation, guides, and tutorials, visit the official LangChain documentation:
- **[LangChain MariaDB Documentation](https://docs.langchain.com/oss/python/integrations/vectorstores/mariadb)**

This section contains only the API reference:
- **[API Reference](api-reference/README.md)** - Complete API documentation

## Resources

- [GitHub Repository](https://github.com/mariadb-corporation/langchain-mariadb)
- [PyPI Package](https://pypi.org/project/langchain-mariadb/)
- [LangChain Documentation](https://python.langchain.com/)

## Version

Current version: **v0.0.20**
