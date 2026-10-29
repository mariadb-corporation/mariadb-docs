---
description: >-
  Use GridGain 8 as a LangGraph persistence backend: a checkpointer for thread state and a store for long-term memory across threads.
---

# LangGraph Integration

The `langgraph-checkpoint-gridgain` package lets LangGraph applications keep their state in GridGain. It provides the following components:

- **GridGainCheckpointSaver** stores the state of a graph thread. It enables pausing and resuming graphs, human approval steps, and time travel.
- **GridGainMemoryStore** stores JSON memory that is shared across graph threads. It supports namespaces, structured filters, and expiry enforced by the server.

These components use only the SQL and key-value APIs, so they do not require a license for vector search.

## Prerequisites

- Python 3.10 or later.
- A running GridGain 8 cluster.

## Installation

Install the package using pip:

```bash
pip install langgraph-checkpoint-gridgain==3.0.0
```

The package depends on `langchain-gridgain` 3.0.0, `langgraph-checkpoint` 4.1.1 or later (below 5.0), `langchain-core` 1.4.7 or later (below 2.0), and `pygridgain` 1.6.0 or later (below 2.0). It installs the `langchain-gridgain` [LangChain components](langchain.md) as well. Install the `langgraph` package that runs your graphs separately.

Import the components from the `langgraph` namespace:

```python
from langgraph.checkpoint.gridgain import GridGainCheckpointSaver
from langgraph.store.gridgain import GridGainMemoryStore
```

## Connecting to GridGain

The components take a connected [Python thin client](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/python-thin-client). Your application creates and closes the clients:

```python
from pygridgain import Client

client = Client()
client.connect("127.0.0.1", 10800)
```

Each component accepts a synchronous `Client`, an asynchronous `AioClient`, or both. With an `AioClient`, the asynchronous methods use non-blocking I/O. Without it, they run the synchronous methods in a worker thread.

```python
from pygridgain import AioClient

aio_client = AioClient()
await aio_client.connect("127.0.0.1", 10800)

checkpointer = GridGainCheckpointSaver(client, aio_client=aio_client)
```

## GridGainCheckpointSaver

`GridGainCheckpointSaver` is a LangGraph checkpointer. It supports reading the latest and earlier checkpoints, listing checkpoints, writing checkpoints and intermediate writes, and deleting a thread with `delete_thread`.

The checkpointer stores data in three SQL caches: `lg_checkpoints`, `lg_checkpoint_blobs`, and `lg_checkpoint_writes`. It creates them automatically.

```python
from langgraph.checkpoint.gridgain import GridGainCheckpointSaver

checkpointer = GridGainCheckpointSaver(client)

graph = builder.compile(checkpointer=checkpointer)
config = {"configurable": {"thread_id": "conversation-1"}}
result = graph.invoke(inputs, config)

# Inspect the latest state of the thread
snapshot = graph.get_state(config)
```

A graph that uses the checkpointer can pause, resume later with a new checkpointer instance, and continue from an earlier checkpoint.

The checkpointer has no expiry (TTL) option. It does not support extended operations such as `copy_thread`, `prune`, or `delete_for_runs`.

## GridGainMemoryStore

`GridGainMemoryStore` is a LangGraph store for memory that outlives a single thread, such as user preferences or facts that an agent should recall across conversations. It stores JSON items in namespaces. By default, it uses the `lg_store` cache; to use another cache, set `cache_name`.

The store supports `get`, `put`, `delete`, `search`, `list_namespaces`, `batch`, and `abatch`.

```python
from langgraph.store.gridgain import GridGainMemoryStore

store = GridGainMemoryStore(client)

# Namespaced items
store.put(("users", "u1"), "prefs", {"theme": "dark", "score": 5})
item = store.get(("users", "u1"), "prefs")

# Search a namespace and everything nested under it
matches = store.search(("users",), filter={"theme": "dark"})
top = store.search(("users",), filter={"score": {"$gte": 5}}, limit=10)

# List namespaces
store.list_namespaces(prefix=("users",))

store.delete(("users", "u1"), "prefs")

graph = builder.compile(store=store)
```

Filters support exact matches and the `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, and `$lte` operators. They apply to the JSON value of the item.

{% hint style="info" %}
Semantic search is not supported. If you pass a non-empty `query` to `search`, the store logs a warning and runs a structured search instead.
{% endhint %}

### Item Expiry (TTL)

The cluster enforces item expiry. TTL values are in **minutes**. Set a TTL for an item with the `ttl` argument of `put`, or for the whole store with `ttl_config`. By default, reading an item resets its expiry. To read an item without resetting it, pass `refresh_ttl=False`.

```python
store = GridGainMemoryStore(
    client, ttl_config={"default_ttl": 60, "refresh_on_read": True}
)

store.put(("users", "u1"), "session", {"step": 3}, ttl=10)
item = store.get(("users", "u1"), "session", refresh_ttl=False)
```

## Using the Components Together

Given a connected `client` and a configured graph `builder`:

```python
saver = GridGainCheckpointSaver(client)
store = GridGainMemoryStore(
    client, ttl_config={"default_ttl": 60, "refresh_on_read": True}
)
graph = builder.compile(checkpointer=saver, store=store)
config = {"configurable": {"thread_id": "conversation-1"}}

store.put(("users", "u1"), "prefs", {"theme": "dark"}, ttl=10)
item = store.get(("users", "u1"), "prefs", refresh_ttl=False)
matches = store.search(("users",), filter={"theme": "dark"})
# Use config with graph.invoke(...) and graph.get_state(...).
```

## Upgrading from langchain-gridgain 2.x

In `langchain-gridgain` 2.x, the checkpointer and the memory store were part of the `langchain-gridgain` package. In version 3.0.0, they moved to `langgraph-checkpoint-gridgain`. Install the new package and update the imports:

```diff
-from langchain_gridgain import GridGainCheckpointSaver, GridGainMemoryStore
+from langgraph.checkpoint.gridgain import GridGainCheckpointSaver
+from langgraph.store.gridgain import GridGainMemoryStore
```

The classes, their behavior, and the stored data are unchanged. The `langchain_gridgain` package does not import them anymore, and there is no `langgraph_checkpoint_gridgain` module.
