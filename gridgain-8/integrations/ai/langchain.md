---
description: >-
  Use GridGain 8 as a backend for LangChain components, including a key-value store, document loader, chat message history, LLM caches, and a vector store.
---

# LangChain Integration

GridGain provides support for a LangChain integration. In this extension, a set of storage adapters that allow LangChain components to efficiently use GridGain as a backend for various data storage needs is provided.

## Features

Support for the following five key LangChain interfaces are provided in this extension:

1. **GridGainStore**: A key-value store implementation.
2. **GridGainDocumentLoader**: A document loader for retrieving documents from GridGain caches.
3. **GridGainChatMessageHistory**: A chat message history store using GridGain.
4. **GridGainCache**: A caching mechanism for Language Models using GridGain.
5. **GridGainVectorStore**: A vector store implementation using GridGain for storing and querying embeddings.

## Prerequisites

The following is required to use LangChain integration:

- GridGain 8.9.17 or later with an appropriate license is required to use vector store.
- Python 3.11.7 or later is required to use the LangChain extension.

## Installation

The `langchain-gridgain` extension is available for installation via pip:

```bash
pip install langchain-gridgain
```

## GridGain Setup

In order to use [GridGain](https://www.gridgain.com/) as an online store, you need to have a running GridGain cluster.

The GridGain online store provides the capability to connect to local/remote GridGain  clusters.

### Connecting to GridGain

Before using any of the GridGain-based components, you need to establish a connection to your GridGain cluster. The connection method differs slightly depending on whether you're using Apache Ignite or GridGain.

Below is an example of configuring GridGain:

```python
from pygridgain import Client
from pygridgain.exceptions import AuthenticationError

def connect_to_gridgain(username: str, password: str, url: str, port: int) -> Client:
    try:
        # Create client configuration
        client = Client(username=username, password=password, use_ssl=True)

        # Connect to the cluster
        client.connect(url, port)
        print("Connected to GridGain successfully.")
        return client
    except AuthenticationError:
        print("Authentication failed. Please check your username and password.")
        raise
    except Exception as e:
        print(f"Failed to connect to GridGain: {e}")
        raise

# Example usage
try:
    client = connect_to_gridgain(
        username="your_username",
        password="your_password",
        url="gridgain.example.com",
        port=10800
    )
except Exception as e:
    print(f"Connection failed: {e}")
```

Make sure to replace `"your_username"`, `"your_password"`, `"gridgain.example.com"`, and `10800` with your actual GridGain cluster credentials and connection details.

The client object returned by this connection functions will be used when initializing GridGain-based components.

## Detailed Component Explanations

### 1. GridGainStore

GridGainStore is a key-value store implementation that uses GridGain as its backend. It provides a simple and efficient way to store and retrieve data using key-value pairs.

Usage example:

```python
from langchain_community.storage.ignite import GridGainStore

def initialize_keyvalue_store(client) -> GridGainStore:
    try:
        key_value_store = GridGainStore(
            cache_name="laptop_specs",
            client=client
        )
        print("GridGainStore initialized successfully.")
        return key_value_store
    except Exception as e:
        print(f"Failed to initialize GridGainStore: {e}")
        raise

# Usage
client = connect_to_ignite("localhost", 10800)
key_value_store = initialize_keyvalue_store(client)

# Store a value
key_value_store.mset([("laptop1", "16GB RAM, NVIDIA RTX 3060, Intel i7 11th Gen")])

# Retrieve a value
specs = key_value_store.mget(["laptop1"])[0]
```

### 2. GridGainDocumentLoader

GridGainDocumentLoader is designed to load documents from GridGain caches. It's particularly useful for scenarios where you need to retrieve and process large amounts of textual data stored in GridGain.

Usage example:

```python
from langchain_community.document_loaders.ignite import GridGainDocumentLoader

def initialize_doc_loader(client) -> GridGainDocumentLoader:
    try:
        doc_loader = GridGainDocumentLoader(
            cache_name="review_cache",
            client=client,
            create_cache_if_not_exists=True
        )
        print("GridGainDocumentLoader initialized successfully.")
        return doc_loader
    except Exception as e:
        print(f"Failed to initialize GridGainDocumentLoader: {e}")
        raise

# Usage
client = connect_to_ignite("localhost", 10800)
doc_loader = initialize_doc_loader(client)

# Populate the cache
reviews = {
    "laptop1": "Great performance for coding and video editing. The 16GB RAM and dedicated GPU make multitasking a breeze."
}
doc_loader.populate_cache(reviews)

# Load documents
documents = doc_loader.load()
```

### 3. GridGainChatMessageHistory

GridGainChatMessageHistory provides a way to store and retrieve chat message history using GridGain. This is crucial for maintaining context in conversational AI applications.

Usage example:

```python
from langchain_community.chat_message_histories.ignite import GridGainChatMessageHistory

def initialize_chathistory_store(client) -> GridGainChatMessageHistory:
    try:
        chat_history = GridGainChatMessageHistory(
            session_id="user_session",
            cache_name="chat_history",
            client=client
        )
        print("GridGainChatMessageHistory initialized successfully.")
        return chat_history
    except Exception as e:
        print(f"Failed to initialize GridGainChatMessageHistory: {e}")
        raise

# Usage
client = connect_to_ignite("localhost", 10800)
chat_history = initialize_chathistory_store(client)

# Add a message to the history
chat_history.add_user_message("Hello, I need help choosing a laptop.")

# Retrieve the conversation history
messages = chat_history.messages
```

### 4. GridGainCache

GridGainCache provides a caching mechanism for the responses received from LLMs using GridGain. This can significantly improve response times for repeated or similar queries by storing and retrieving pre-computed results.

Usage example:

```python
from langchain_community.llm_cache.ignite import GridGainCache
from utils import connect_to_ignite, initialize_llm_cache

# Connect to GridGain/Ignite
client = connect_to_ignite("localhost", 10800)

# Initialize GridGainCache
llm_cache = initialize_llm_cache(client)

# Set up your LLM (e.g., OpenAI)
from langchain_openai import OpenAI
llm = OpenAI()

# Set the cache for the LLM
llm.cache = llm_cache

# Use the LLM in your application
response = llm.predict("What are the key features to consider when buying a laptop for video editing?")
print(response)
```

### 5. GridGainSemanticCache

Usage example:

```python
from langchain_community.llm_cache.ignite import GridGainSemanticCache
from langchain_openai import OpenAIEmbeddings
from utils import connect_to_ignite, initialize_semantic_llm_cache, initialize_embeddings_model

# Connect to GridGain/Ignite
client = connect_to_ignite("localhost", 10800)

# Initialize embedding model
api_key = os.environ["OPENAI_API_KEY"]
embedding_model = initialize_embeddings_model(api_key)

# Initialize GridGainSemanticCache
api_endpoint = "http://localhost:8080"
semantic_cache = initialize_semantic_llm_cache(client, embedding_model, api_endpoint)

# Set up your LLM (e.g., OpenAI)
from langchain_openai import OpenAI
llm = OpenAI()

# Set the cache for the LLM
llm.cache = semantic_cache

# Use the LLM in your application
response = llm.predict("What are the key features to consider when buying a laptop for video editing?")
print(response)
```

### 6. GridGainVectorStore

GridGainVectorStore is a vector store implementation using GridGain for storing and querying embeddings. It allows efficient similarity search operations on high-dimensional vector data.

Usage example:

```python
from langchain_community.vectorstores import GridGainVectorStore
from utils import initialize_embeddings_model, initialize_vector_store

# Initialize embedding model
api_key = os.environ["OPENAI_API_KEY"]
embedding_model = initialize_embeddings_model(api_key)

# Initialize GridGainVectorStore
api_endpoint = "http://localhost:8080"
vector_store = initialize_vector_store(api_endpoint, embedding_model)

# Add texts to the vector store
texts = [
    "The latest MacBook Pro offers exceptional performance for video editing.",
    "Dell XPS 15 is a powerful Windows laptop suitable for creative professionals.",
    "ASUS ROG Zephyrus G14 provides a balance of portability and gaming performance."
]
metadatas = [{"id": "tech_review_1"}, {"id": "tech_review_2"}, {"id": "tech_review_3"}]

vector_store.add_texts(texts=texts, metadatas=metadatas)

# Perform similarity search
query = "What's a good laptop for video editing?"
results = vector_store.similarity_search(query, k=2)

for doc in results:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
    print("---")

# Clear the vector store
vector_store.clear()
```

The GridGainVectorStore allows you to store text data along with their vector embeddings, enabling efficient similarity searches based on the semantic meaning of the text. This is particularly useful for applications involving natural language processing, recommendation systems, and information retrieval.

## Langchain Tutorial

GridGain provides a comprehensive, real-world example of how to use this package. The tutorial includes a demonstration project that showcases the integration of GridGain with LangChain, using the custom `langchain-gridgain` package and provides examples of how to use GridGain as a backend for various LangChain components, focusing on a laptop recommendation system.

The tutorial is available in the [Retrieval-Augmented Generation with GridGain and LangChain](https://www.gridgain.com/docs/tutorials/vector/langchain) section.
