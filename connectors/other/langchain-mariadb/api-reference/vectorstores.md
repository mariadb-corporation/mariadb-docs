# Vector Stores

> **Version:** langchain-mariadb v0.0.21

## DistanceStrategy

Distance strategies for vector similarity.

### Attributes

- **EUCLIDEAN**: 
- **COSINE**: 

---

## TableConfig

Configuration for database table names.

### Constructor

```python
__init__(embedding_table: Optional[str] = None, collection_table: Optional[str] = None) -> None
```

Initialize TableConfig with custom or default table names.

**Parameters:**

- **embedding_table** (`Optional[str]`): Name for embedding table (default: langchain_embedding)
- **collection_table** (`Optional[str]`): Name for collection table (default: langchain_collection)

### Methods

#### `default`

```python
default() -> 'TableConfig'
```

Create TableConfig with default values.

### Attributes

- **embedding_table** (`str`): 
- **collection_table** (`str`): 

---

## ColumnConfig

Configuration for database column names.

### Constructor

```python
__init__(
    embedding_id: Optional[str] = None,
    embedding: Optional[str] = None,
    content: Optional[str] = None,
    metadata: Optional[str] = None,
    collection_id: Optional[str] = None,
    collection_label: Optional[str] = None,
    collection_metadata: Optional[str] = None
) -> None
```

Initialize ColumnConfig with custom or default column names.

**Parameters:**

- **embedding_id** (`Optional[str]`): Name for embedding ID column (default: id)
- **embedding** (`Optional[str]`): Name for embedding vector column (default: embedding)
- **content** (`Optional[str]`): Name for content column (default: content)
- **metadata** (`Optional[str]`): Name for metadata column (default: metadata)
- **collection_id** (`Optional[str]`): Name for collection ID column (default: id)
- **collection_label** (`Optional[str]`): Name for collection label column (default: label)
- **collection_metadata** (`Optional[str]`): Name for collection metadata column (default: metadata)

### Methods

#### `default`

```python
default() -> 'ColumnConfig'
```

Create ColumnConfig with default values.

### Attributes

- **embedding_id** (`str`): 
- **embedding** (`str`): 
- **content** (`str`): 
- **metadata** (`str`): 
- **collection_id** (`str`): 
- **collection_label** (`str`): 
- **collection_metadata** (`str`): 

---

## MariaDBStoreSettings

Configuration for MariaDBStore.

### Constructor

```python
__init__(
    tables: Optional[TableConfig] = None,
    columns: Optional[ColumnConfig] = None,
    pre_delete_collection: bool = False,
    lazy_init: bool = False
) -> None
```

Initialize MariaDBStoreSettings with custom or default configurations.

**Parameters:**

- **tables** (`Optional[TableConfig]`): Table configuration
- **columns** (`Optional[ColumnConfig]`): Column configuration
- **pre_delete_collection** (`bool`): delete existing collection (default: False)

### Methods

#### `default`

```python
default() -> 'MariaDBStoreSettings'
```

Create MariaDBStoreSettings with default values.

### Attributes

- **tables** (`TableConfig`): 
- **columns** (`ColumnConfig`): 
- **pre_delete_collection** (`bool`): 
- **lazy_init** (`bool`): 

---

## MariaDBStore

MariaDB vector store integration for LangChain.

**Examples:**

```python
Basic usage::

    from langchain_mariadb import MariaDBStore
    from langchain_openai import OpenAIEmbeddings

    # Create connection
    url = "mariadb+mariadbconnector://user:pass@localhost/db"
    embeddings = OpenAIEmbeddings()

    # Create vector store
    store = MariaDBStore.from_texts(
        texts=["Hello, world!", "Another text"],
        embedding=embeddings,
        datasource=url,
        collection_name="my_collection"
    )

    # Search similar texts
    results = store.similarity_search("Hello", k=2)

Search with metadata filter::

    results = store.similarity_search(
        "Hello",
        filter={"category": "greeting"}
    )

Complex filter with operators::

    results = store.similarity_search(
        "Hello",
        filter={
            "$and": [
                {"category": "greeting"},
                {"language": {"$in": ["en", "es"]}}
            ]
        }
    )

Asynchronous usage::

    import asyncio

    async def search_docs():
        results = await store.amax_marginal_relevance_search(
            "Hello", k=2, fetch_k=10, lambda_mult=0.5
        )
        return results

    results = asyncio.run(search_docs())

Custom configuration::

    from langchain_mariadb import (
        MariaDBStore, MariaDBStoreSettings,
        TableConfig, ColumnConfig
    )

    config = MariaDBStoreSettings(
        tables=TableConfig(
            embedding_table="custom_embeddings",
            collection_table="custom_collections"
        ),
        columns=ColumnConfig(
            embedding_id="doc_id",
            content="text_content",
            metadata="doc_metadata"
        )
    )

    store = MariaDBStore.from_texts(
        texts=["Hello"],
        embedding=embeddings,
        datasource=url,
        config=config
    )

Working with documents::

    from langchain_core.documents import Document

    documents = [
        Document(
            page_content="Hello",
            metadata={"source": "greeting.txt"}
        ),
        Document(
            page_content="World",
            metadata={"source": "greeting.txt"}
        )
    ]

    store = MariaDBStore.from_documents(
        documents=documents,
        embedding=embeddings,
        datasource=url
    )

    # Add more documents
    store.add_documents(documents)
```

### Constructor

```python
__init__(
    embeddings: Embeddings,
    embedding_length: Optional[int] = None,
    datasource: Union[Engine | str],
    collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    collection_metadata: Optional[dict] = None,
    distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
    config: MariaDBStoreSettings = MariaDBStoreSettings(),
    logger: Optional[logging.Logger] = None,
    engine_args: Optional[dict[str, Any]] = None,
    relevance_score_fn: Optional[Callable[[float], float]] = None
) -> None
```

Initialize the MariaDB vector store.

**Parameters:**

- **embeddings** (`Embeddings`): Embeddings object for creating embeddings
- **embedding_length** (`Optional[int]`): Length of embedding vectors (default: 1536)
- **datasource** (`Union[Engine | str]`): datasource (connection string, sqlalchemy engine or
  MariaDB connection pool)
- **collection_name** (`str`): Name of the collection to store vectors
- **collection_metadata** (`Optional[dict]`): Optional metadata for the collection
- **distance_strategy** (`DistanceStrategy`): Strategy for distances (COSINE or EUCLIDEAN)
- **config** (`MariaDBStoreSettings`): Store configuration for tables and columns
- **logger** (`Optional[logging.Logger]`): Optional logger instance for debugging
- **relevance_score_fn** (`Optional[Callable[[float], float]]`): function to override relevance score calculation

### Methods

#### `create_tables_if_not_exists`

```python
create_tables_if_not_exists() -> None
```

Create the necessary database tables if they don't exist.

#### `drop_tables`

```python
drop_tables() -> None
```

Drop all tables used by the vector store.

#### `create_collection`

```python
create_collection() -> None
```

Create a new collection or retrieve existing one.

#### `delete_collection`

```python
delete_collection() -> None
```

Delete the current collection and its associated data.

#### `delete`

```python
delete(ids: Optional[List[str]] = None, kwargs: Any = {}) -> None
```

Delete vectors by their IDs.

**Parameters:**

- **ids** (`Optional[List[str]]`): List of IDs to delete
- ****kwargs** (`Any`): Additional arguments (not used)

#### `get_by_ids`

```python
get_by_ids(ids: Sequence[str]) -> List[Document]
```

Get documents by their IDs.

#### `add_embeddings`

```python
add_embeddings(
    texts: Sequence[str],
    embeddings: List[List[float]],
    metadatas: Optional[List[dict]] = None,
    ids: Optional[List[str]] = None,
    kwargs: Any = {}
) -> List[str]
```

Add embeddings to the vectorstore.

**Parameters:**

- **texts** (`Sequence[str]`): Sequence of strings to add
- **embeddings** (`List[List[float]]`): List of embedding vectors
- **metadatas** (`Optional[List[dict]]`): Optional list of metadata dicts for each text
- **ids** (`Optional[List[str]]`): Optional list of IDs for the documents
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[str]` - List of IDs for the added documents

**Raises:**

- **ValueError**: If any provided ID contains invalid characters

#### `add_texts`

```python
add_texts(
    texts: Iterable[str],
    metadatas: Optional[List[dict]] = None,
    ids: Optional[List[str]] = None,
    kwargs: Any = {}
) -> List[str]
```

Run more texts through the embeddings and add to the vectorstore.

**Parameters:**

- **texts** (`Iterable[str]`): Iterable of strings to add to the vectorstore.
- **metadatas** (`Optional[List[dict]]`): Optional list of metadatas associated with the texts.
- **ids** (`Optional[List[str]]`): Optional list of ids for the texts.
  If not provided, will generate a new id for each text.
- **kwargs** (`Any`): vectorstore specific parameters

**Returns:**

 `List[str]` - List of ids from adding the texts into the vectorstore.

#### `similarity_search`

```python
similarity_search(
    query: str,
    k: int = 4,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Run similarity search with MariaDB.

**Parameters:**

- **query** (`str`): Query text to search for
- **k** (`int`): Number of results to return (default: 4)
- **filter** (`Union[None, dict]`): Optional filter by metadata
- ****kwargs** (`Any`): Additional arguments passed to similarity_search_by_vector

**Returns:**

 `List[Document]` - List of Documents most similar to the query

#### `similarity_search_with_score`

```python
similarity_search_with_score(query: str, k: int = 4, filter: Union[None, dict] = None) -> List[Tuple[Document, float]]
```

Return docs most similar to query along with scores.

**Parameters:**

- **query** (`str`): Text to look up documents similar to
- **k** (`int`): Number of Documents to return (default: 4)
- **filter** (`Union[None, dict]`): Optional filter by metadata

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, similarity_score)

#### `similarity_search_with_score_by_vector`

```python
similarity_search_with_score_by_vector(embedding: List[float], k: int = 4, filter: Union[None, dict] = None) -> List[Tuple[Document, float]]
```

Return docs most similar to embedding vector along with scores.

**Parameters:**

- **embedding** (`List[float]`): Embedding vector to look up documents similar to
- **k** (`int`): Number of Documents to return (default: 4)
- **filter** (`Union[None, dict]`): Optional filter by metadata

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, similarity_score)

#### `similarity_search_by_vector`

```python
similarity_search_by_vector(
    embedding: List[float],
    k: int = 4,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Return docs most similar to embedding vector.

**Parameters:**

- **embedding** (`List[float]`): Embedding vector to look up documents similar to
- **k** (`int`): Number of Documents to return (default: 4)
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[Document]` - List of Documents most similar to the query vector

#### `max_marginal_relevance_search`

```python
max_marginal_relevance_search(
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Return docs selected using maximal marginal relevance.

**Parameters:**

- **query** (`str`): Text to look up documents similar to
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments passed to search_by_vector

**Returns:**

 `List[Document]` - List of Documents selected by maximal marginal relevance

#### `amax_marginal_relevance_search`

```python
amax_marginal_relevance_search(
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Return docs selected using maximal marginal relevance asynchronously.

**Parameters:**

- **query** (`str`): Text to look up documents similar to
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments passed to search_by_vector

**Returns:**

 `List[Document]` - List of Documents selected by maximal marginal relevance

#### `max_marginal_relevance_search_with_score`

```python
max_marginal_relevance_search_with_score(
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Tuple[Document, float]]
```

Return docs selected using maximal marginal relevance with scores.

**Parameters:**

- **query** (`str`): Text to look up documents similar to
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments passed to search_by_vector

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, score) selected by maximal marginal relevance

#### `amax_marginal_relevance_search_with_score`

```python
amax_marginal_relevance_search_with_score(
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Tuple[Document, float]]
```

Return docs selected using maximal marginal relevance with scores
asynchronously.

**Parameters:**

- **query** (`str`): Text to look up documents similar to
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments passed to search_by_vector

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, score) selected by maximal marginal relevance

#### `max_marginal_relevance_search_by_vector`

```python
max_marginal_relevance_search_by_vector(
    embedding: List[float],
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Return docs selected using maximal marginal relevance.

**Parameters:**

- **embedding** (`List[float]`): Query embedding vector
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[Document]` - List of Documents selected by maximal marginal relevance

#### `amax_marginal_relevance_search_by_vector`

```python
amax_marginal_relevance_search_by_vector(
    embedding: List[float],
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Document]
```

Return docs selected using maximal marginal relevance asynchronously.

**Parameters:**

- **embedding** (`List[float]`): Query embedding vector
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[Document]` - List of Documents selected by maximal marginal relevance

#### `max_marginal_relevance_search_with_score_by_vector`

```python
max_marginal_relevance_search_with_score_by_vector(
    embedding: List[float],
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Tuple[Document, float]]
```

Return docs selected using maximal marginal relevance with scores.

**Parameters:**

- **embedding** (`List[float]`): Query embedding vector
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, score) selected by maximal marginal relevance

#### `amax_marginal_relevance_search_with_score_by_vector`

```python
amax_marginal_relevance_search_with_score_by_vector(
    embedding: List[float],
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    filter: Union[None, dict] = None,
    kwargs: Any = {}
) -> List[Tuple[Document, float]]
```

Return docs selected using maximal marginal relevance with scores
asynchronously.

**Parameters:**

- **embedding** (`List[float]`): Query embedding vector
- **k** (`int`): Number of documents to return (default: 4)
- **fetch_k** (`int`): Number of documents to fetch before selecting top-k (default: 20)
- **lambda_mult** (`float`): Balance between relevance and diversity, 0-1 (default: 0.5)
  0 = maximize diversity, 1 = maximize relevance
- **filter** (`Union[None, dict]`): Optional metadata filter
- ****kwargs** (`Any`): Additional arguments (not used)

**Returns:**

 `List[Tuple[Document, float]]` - List of tuples of (Document, score) selected by maximal marginal relevance

#### `from_texts`

```python
from_texts(
    texts: List[str],
    embedding: Embeddings,
    metadatas: Optional[List[dict]] = None,
    ids: Optional[List[str]] = None,
    datasource: Optional[Union[Engine, str]] = None,
    collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
    embedding_length: Optional[int] = None,
    config: MariaDBStoreSettings = MariaDBStoreSettings(),
    logger: Optional[logging.Logger] = None,
    relevance_score_fn: Optional[Callable[[float], float]] = None,
    kwargs: Any = {}
) -> MariaDBStore
```

Create a MariaDBStore instance from texts.

**Parameters:**

- **texts** (`List[str]`): List of text strings to store
- **embedding** (`Embeddings`): Embeddings object for creating embeddings
- **metadatas** (`Optional[List[dict]]`): Optional list of metadata dicts for each text
- **ids** (`Optional[List[str]]`): Optional list of unique IDs for each text
- **datasource** (`Optional[Union[Engine, str]]`): Database connection (connection string or sqlalchemy engine)
- **collection_name** (`str`): Name of the collection to store vectors
- **distance_strategy** (`DistanceStrategy`): Strategy for distances (COSINE or EUCLIDEAN)
- **embedding_length** (`Optional[int]`): Length of embedding vectors (default: 1536)
- **config** (`MariaDBStoreSettings`): Store configuration for tables and columns
- **logger** (`Optional[logging.Logger]`): Optional logger instance for debugging
- **relevance_score_fn** (`Optional[Callable[[float], float]]`): Optional function to override relevance score calculation
- ****kwargs** (`Any`): Additional arguments passed to add_embeddings

**Returns:**

 `MariaDBStore` - MariaDBStore instance initialized with the provided texts

**Raises:**

- **ValueError**: If ``datasource`` is not provided.

#### `from_embeddings`

```python
from_embeddings(
    text_embeddings: List[Tuple[str, List[float]]],
    ids: Optional[List[str]] = None,
    metadatas: Optional[List[dict]] = None,
    embedding: Embeddings,
    distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
    relevance_score_fn: Optional[Callable[[float], float]] = None,
    config: MariaDBStoreSettings = MariaDBStoreSettings(),
    kwargs: Any = {}
) -> MariaDBStore
```

Create a MariaDBStore instance from text-embedding pairs.

**Parameters:**

- **text_embeddings** (`List[Tuple[str, List[float]]]`): List of (text, embedding) tuples
- **ids** (`Optional[List[str]]`): Optional list of IDs for the documents
- **metadatas** (`Optional[List[dict]]`): Optional list of metadata dicts
- **embedding** (`Embeddings`): Embeddings object for creating embeddings
- **distance_strategy** (`DistanceStrategy`): Strategy for computing distances
- **relevance_score_fn** (`Optional[Callable[[float], float]]`): Optional function to compute relevance scores
- **config** (`MariaDBStoreSettings`): Store configuration for tables and columns
- ****kwargs** (`Any`): Additional arguments including datasource, collection_name

**Returns:**

 `MariaDBStore` - MariaDBStore instance

#### `from_existing_index`

```python
from_existing_index(
    embedding: Embeddings,
    collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
    datasource: Union[Engine | str],
    config: MariaDBStoreSettings = MariaDBStoreSettings(),
    kwargs: Any = {}
) -> MariaDBStore
```

Create a MariaDBStore instance from an existing index.

**Parameters:**

- **embedding** (`Embeddings`): Embeddings object for creating embeddings
- **collection_name** (`str`): Name of collection (default: langchain)
- **distance_strategy** (`DistanceStrategy`): Strategy for computing distances
- **datasource** (`Union[Engine | str]`): datasource (connection string, sqlalchemy engine or MariaDB
  connection pool)
- ****kwargs** (`Any`): Additional arguments passed to constructor

**Returns:**

 `MariaDBStore` - MariaDBStore instance connected to existing index

#### `from_documents`

```python
from_documents(
    documents: List[Document],
    embedding: Embeddings,
    ids: Optional[List[str]] = None,
    datasource: Optional[Union[Engine, str]] = None,
    collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
    embedding_length: Optional[int] = None,
    config: MariaDBStoreSettings = MariaDBStoreSettings(),
    logger: Optional[logging.Logger] = None,
    relevance_score_fn: Optional[Callable[[float], float]] = None,
    kwargs: Any = {}
) -> MariaDBStore
```

Create a MariaDBStore instance from documents.

**Parameters:**

- **documents** (`List[Document]`): List of Document objects to store
- **embedding** (`Embeddings`): Embeddings object for creating embeddings
- **ids** (`Optional[List[str]]`): Optional list of IDs for the documents
- **datasource** (`Optional[Union[Engine, str]]`): Database connection (connection string or sqlalchemy engine)
- **collection_name** (`str`): Name of the collection to store vectors
- **distance_strategy** (`DistanceStrategy`): Strategy for distances (COSINE or EUCLIDEAN)
- **embedding_length** (`Optional[int]`): Length of embedding vectors (default: 1536)
- **config** (`MariaDBStoreSettings`): Store configuration for tables and columns
- **logger** (`Optional[logging.Logger]`): Optional logger instance for debugging
- **relevance_score_fn** (`Optional[Callable[[float], float]]`): Optional function to override relevance score calculation
- ****kwargs** (`Any`): Additional arguments passed to from_texts

**Returns:**

 `MariaDBStore` - MariaDBStore instance

#### `as_retriever`

```python
as_retriever(kwargs: Any = {}) -> VectorStoreRetriever
```

Return VectorStoreRetriever initialized from this VectorStore.

**Parameters:**

- ****kwargs** (`Any`): Keyword arguments to pass to the search function.
  Can include:
  
  - search_type: Defines the type of search that the Retriever should
  perform. Can be 'similarity' (default), 'mmr', or
  'similarity_score_threshold'.
  - search_kwargs: Keyword arguments to pass to the search function.
  Can include:
  
  - k: Amount of documents to return (Default: 4)
  - score_threshold: Minimum relevance threshold for
  similarity_score_threshold
  - fetch_k: Amount of documents to pass to MMR algorithm (Default: 20)
  - lambda_mult: Diversity of results returned by MMR; 1 for minimum
  diversity and 0 for maximum. (Default: 0.5)
  - filter: Filter by document metadata

**Returns:**

 `VectorStoreRetriever` - VectorStoreRetriever instance configured for this vector store.

**Examples:**

```python
Retrieve more documents with higher diversity::

    docsearch.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 6, "lambda_mult": 0.25}
    )

Fetch more documents for the MMR algorithm to consider::

    docsearch.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 50}
    )

Only retrieve documents above a relevance threshold::

    docsearch.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"score_threshold": 0.8}
    )

Get only the single most similar document::

    docsearch.as_retriever(search_kwargs={"k": 1})
```

### Attributes

- **embedding_function**: 
- **collection_name**: 
- **collection_metadata**: 
- **pre_delete_collection**: 
- **lazy_init**: 
- **logger**: 
- **override_relevance_score_fn**: 
- **embeddings** (`Embeddings`): 

---
