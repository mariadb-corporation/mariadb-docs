---
description: >-
  Use GridGain 8 as a backend for LangChain components, including key-value and byte stores, a document loader, chat message history, LLM caches, and a vector store.
---

# LangChain Integration

The `langchain-gridgain` package provides storage adapters that let LangChain components use GridGain as a backend for various data storage needs.

## Features

The package implements the following LangChain interfaces:

1. **GridGainStore**: A key-value store for string values.
2. **GridGainByteStore**: A key-value store for binary values, for example, to cache computed embeddings.
3. **GridGainDocumentLoader**: A document loader for retrieving documents from GridGain caches.
4. **GridGainChatMessageHistory**: A chat message history store.
5. **GridGainCache**: An exact-match cache for LLM responses.
6. **GridGainSemanticCache**: A semantic cache for LLM responses.
7. **GridGainVectorStore**: A vector store for storing and querying embeddings.

## Prerequisites

The following is required to use the LangChain integration:

- Python 3.10 or later.
- A running GridGain 8 cluster. The edition you need depends on the components that you use:
  - `GridGainStore`, `GridGainByteStore`, `GridGainDocumentLoader`, `GridGainChatMessageHistory`, and `GridGainCache` use only key-value operations and work with any edition.
  - `GridGainVectorStore` and `GridGainSemanticCache` require GridGain 8.9.17 or later with a license that provides access to vector search.
- To filter vector searches by metadata, GridGain 8.10.0 or later and `pygridgain` 1.7.0 or later, which requires Python 3.11 or later. See [Filtering by Metadata](#filtering-by-metadata).

## Installation

Install the `langchain-gridgain` package using pip:

```bash
pip install langchain-gridgain
```

Version 3.0.0 depends on `langchain-core` 1.4.7 or later (below 2.0) and the GridGain 8 Python thin client, `pygridgain` 1.6.0 or later (below 2.0). It does not depend on `langchain-community`.

## Connecting to GridGain

Before using any of the GridGain-based components, connect to your GridGain cluster with the [Python thin client](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/python-thin-client):

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
client = connect_to_gridgain(
    username="your_username",
    password="your_password",
    url="gridgain.example.com",
    port=10800
)
```

Replace `"your_username"`, `"your_password"`, `"gridgain.example.com"`, and `10800` with your actual GridGain cluster credentials and connection details.

The examples below use the `client` object returned by this function.

{% hint style="info" %}
All components that use the same client share one lock, so you can use one client from several components and threads without extra locking. Operations on one client run one at a time. If you need client-side parallelism, use several clients.
{% endhint %}

## Detailed Component Explanations

### 1. GridGainStore

`GridGainStore` is a key-value store that uses GridGain as its backend. It provides a simple way to store and retrieve data using key-value pairs.

Usage example:

```python
from langchain_gridgain import GridGainStore

key_value_store = GridGainStore(cache_name="laptop_specs", client=client)

# Store a value
key_value_store.mset([("laptop1", "16GB RAM, NVIDIA RTX 3060, Intel i7 11th Gen")])

# Retrieve a value
specs = key_value_store.mget(["laptop1"])[0]
```

### 2. GridGainByteStore

`GridGainByteStore` is a key-value store for binary values (`BaseStore[str, bytes]`). Its main use is caching computed embeddings with LangChain's `CacheBackedEmbeddings`, so each text is embedded only once.

`mget`, `mset`, and `mdelete` each send one request for the whole batch. `mget` returns the values in the order of the keys, with `None` for missing keys.

Usage example:

```python
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_gridgain import GridGainByteStore

byte_store = GridGainByteStore(cache_name="embedding_cache", client=client, ttl=3600)

cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
    embeddings, byte_store, namespace="my_embedding_model", key_encoder="sha256"
)

# The first call computes and caches the embeddings; repeated calls read them from GridGain.
vectors = cached_embeddings.embed_documents(["Hello world"])
```

This example requires the `langchain-classic` package, which `langchain-gridgain` does not install. Choose a `namespace` that identifies the embedding model and its configuration.

### 3. GridGainDocumentLoader

`GridGainDocumentLoader` loads documents from GridGain caches. It is useful when you need to retrieve and process large amounts of text stored in GridGain.

Usage example:

```python
from langchain_gridgain import GridGainDocumentLoader

doc_loader = GridGainDocumentLoader(
    cache_name="review_cache",
    client=client,
    create_cache_if_not_exists=True
)

# Populate the cache
reviews = {
    "laptop1": "Great performance for coding and video editing. The 16GB RAM and dedicated GPU make multitasking a breeze."
}
doc_loader.populate_cache(reviews)

# Load documents
documents = doc_loader.load()
```

### 4. GridGainChatMessageHistory

`GridGainChatMessageHistory` stores and retrieves chat message history in GridGain. This is crucial for maintaining context in conversational AI applications.

Usage example:

```python
from langchain_gridgain import GridGainChatMessageHistory

chat_history = GridGainChatMessageHistory(
    session_id="user_session",
    cache_name="chat_history",
    client=client
)

# Add a message to the history
chat_history.add_user_message("Hello, I need help choosing a laptop.")

# Retrieve the conversation history
messages = chat_history.messages
```

### 5. GridGainCache

`GridGainCache` caches LLM responses in GridGain. This improves response times for repeated, identical prompts.

The cache key includes both the prompt and the LLM, so the same prompt sent to different models is cached separately.

Usage example:

```python
from langchain_core.globals import set_llm_cache
from langchain_gridgain import GridGainCache

llm_cache = GridGainCache(cache_name="llm_cache", client=client)
set_llm_cache(llm_cache)
```

To remove all entries from the cache, call `llm_cache.clear()`.

### 6. GridGainSemanticCache

`GridGainSemanticCache` caches LLM responses for similar prompts. It finds a cached response by comparing the embedding of a new prompt with the embeddings of earlier prompts, and stores the responses in a `GridGainCache`.

Usage example:

```python
from langchain_core.globals import set_llm_cache
from langchain_gridgain import GridGainCache, GridGainSemanticCache

llm_cache = GridGainCache(cache_name="llm_cache", client=client)
semantic_cache = GridGainSemanticCache(
    llm_cache=llm_cache,
    cache_name="semantic_llm_cache",
    client=client,
    embedding=embeddings,
    similarity_threshold=0.85
)
set_llm_cache(semantic_cache)
```

If a lookup fails, the semantic cache logs the error and treats it as a cache miss. If an update fails, it logs the error and skips the write. `clear()` raises an exception on failure.

`semantic_cache.clear()` removes all entries from its own cache and from the whole `GridGainCache` that it uses.

### 7. GridGainVectorStore

`GridGainVectorStore` stores and queries embeddings in GridGain. It implements the standard LangChain `VectorStore` interface.

Usage example:

```python
from langchain_gridgain import GridGainVectorStore

vector_store = GridGainVectorStore(
    cache_name="tech_reviews",
    embedding=embeddings,
    client=client,
)

texts = [
    "The latest MacBook Pro offers exceptional performance for video editing.",
    "ASUS ROG Zephyrus G14 provides a balance of portability and gaming performance.",
]

# IDs are optional. If you do not pass them, the store generates them.
ids = vector_store.add_texts(
    texts,
    metadatas=[{"category": "laptop"}, {"category": "laptop"}],
    ids=["review-1", "review-2"],
)

# Similarity search, with or without scores
docs = vector_store.similarity_search("What's a good laptop for video editing?", k=2)
scored = vector_store.similarity_search_with_score("video editing", k=2)

# Maximal marginal relevance search: balance relevance and diversity
diverse = vector_store.max_marginal_relevance_search(
    "laptops", k=2, fetch_k=10, lambda_mult=0.5
)

# Get and delete documents by ID
vector_store.get_by_ids(["review-1"])
vector_store.delete(["review-1"])

# Delete all documents
vector_store.clear()
```

Note the following:

- Scores are cosine distances: a lower distance means a closer match. Relevance scores, as returned by `similarity_search_with_relevance_scores` and used by the `similarity_score_threshold` retriever, are calculated as `1 - distance`. They are not limited to the `[0, 1]` range: opposite vectors have a relevance below `0`.
- Deleting a document also removes it from the vector index.
- The asynchronous methods run the synchronous ones in a thread pool.

#### Filtering by Metadata

You can restrict a vector search to documents with given metadata values. GridGain applies the filter on the server before it selects the top `k` results, so a filtered search returns up to `k` matching documents.

Declare the metadata keys that you want to filter on in `filterable_metadata_fields` when you create the store. The store writes each declared key as a separate string field in a full-text index next to the vector index. The full metadata is still stored and returned unchanged.

```python
from langchain_gridgain import GridGainVectorStore

store = GridGainVectorStore(
    cache_name="docs_with_filters",
    client=client,
    embedding=embeddings,
    filterable_metadata_fields=["tenant", "category"],
)
store.add_texts(
    ["A laptop guide"],
    metadatas=[{"tenant": "alice", "category": "laptop"}],
    ids=["guide-1"],
)
docs = store.similarity_search("laptop", k=3, filter={"tenant": "alice"})
retriever = store.as_retriever(
    search_kwargs={"k": 3, "filter": {"tenant": "alice"}}
)
```

The filter is passed to similarity search, maximal marginal relevance search, and retrievers. It supports the following forms:

- Several keys, combined with AND: `{"tenant": "alice", "category": "laptop"}`.
- Explicit equality: `{"tenant": {"$eq": "alice"}}`.
- Explicit AND: `{"$and": [{"tenant": "alice"}, {"category": "laptop"}]}`.

Only `None` and `{}` mean no filter. The following raise `ValueError` instead of being ignored: other operators, such as ranges, `$or`, and `$in`; keys that are not declared in `filterable_metadata_fields`; a key tested for two different values; and filters that are not dictionaries.

Values are compared as text. Strings are compared as is, booleans as `"true"` or `"false"`, and numbers as their text form. As a result, the integer `1` matches the string `"1"`, but not the float `1.0`. Other values, such as `None`, lists, and dates, are not stored in the filter fields, so they never match, and a filter on them raises `ValueError`.

{% hint style="warning" %}
The filter fields are set when the cache is created. If you declare `filterable_metadata_fields` for an existing cache that was created without them, the store raises `ValueError`. Create the store with a new cache name and add the documents again. A store without `filterable_metadata_fields` opens existing caches as before.
{% endhint %}

If the installed `pygridgain` is older than 1.7.0, creating a store with `filterable_metadata_fields` raises `ImportError`. If the cluster does not support filtered vector queries, a filtered search raises `NotSupportedByClusterError`. The filter is never dropped silently.

## Entry Expiry (TTL)

`GridGainStore`, `GridGainByteStore`, `GridGainCache`, `GridGainSemanticCache`, and `GridGainVectorStore` accept an optional `ttl` argument: a number of seconds or a `datetime.timedelta`. Entries that the component writes expire that long after they are created or updated. Reading an entry does not extend its lifetime. A `ttl` below one millisecond raises `ValueError`.

The default, `None`, does not change the expiry policy of the cache.

`GridGainChatMessageHistory` and `GridGainDocumentLoader` do not accept `ttl`.

```python
from datetime import timedelta
from langchain_gridgain import GridGainCache, GridGainSemanticCache

llm_cache = GridGainCache(cache_name="llm_cache", client=client, ttl=timedelta(hours=1))

semantic_cache = GridGainSemanticCache(
    llm_cache=llm_cache,
    cache_name="semantic_llm_cache",
    client=client,
    embedding=embeddings,
    ttl=timedelta(hours=1),
)
```

For the semantic cache, `ttl` applies to its own entries. Set the same `ttl` on the `GridGainCache` that it uses, so that both expire together.

## Upgrading from Version 1.0.x

Version 2.0.0 changed the following:

- **Dependencies.** The package depends on `langchain-core` 1.4.7 or later instead of fixed versions of `langchain` and `langchain-community`, and requires `pygridgain` 1.6.0 or later.
- **Imports.** Import the components from `langchain_gridgain`, not from `langchain_community`.
- **LLM cache keys.** `GridGainCache` keys now include the LLM. Entries written by version 1.0.x cannot be found with the new keys and never expire. After the upgrade, clear each cache once:

  ```python
  llm_cache.clear()        # exact-match cache
  semantic_cache.clear()   # semantic cache and its exact-match cache
  ```

- **Embedding cache keys.** The `CacheBackedEmbeddings` example now uses `key_encoder="sha256"`. If you change the key encoder, the embeddings are computed again. `GridGainByteStore` has no `clear()` method. To remove the old entries, call `byte_store.mdelete(list(byte_store.yield_keys()))`.
- **Vector store.** `GridGainVectorStore` returns real cosine distances instead of a constant score of `1.0`, and supports deleting documents by ID.

## LangChain Tutorial

GridGain provides a comprehensive, real-world example of how to use this package. The tutorial includes a demonstration project that showcases the integration of GridGain with LangChain, using the `langchain-gridgain` package, and provides examples of how to use GridGain as a backend for various LangChain components, focusing on a laptop recommendation system.

The tutorial is available in the [Retrieval-Augmented Generation with GridGain and LangChain](https://www.gridgain.com/docs/tutorials/vector/langchain) section.
