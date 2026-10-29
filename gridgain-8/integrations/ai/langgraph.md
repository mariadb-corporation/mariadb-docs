---
description: >-
  Use GridGain 8 as a LangGraph persistence backend: a checkpointer for thread state, a store for long-term memory across threads, and a node cache.
---

# LangGraph Integration

The `langgraph-checkpoint-gridgain` package lets LangGraph applications keep their state in GridGain. It provides the following components:

- **GridGainCheckpointSaver** stores the state of a graph thread. It enables pausing and resuming graphs, human approval steps, and time travel.
- **GridGainMemoryStore** stores JSON memory that is shared across graph threads. It supports namespaces, structured filters, and expiry enforced by the server.
- **GridGainNodeCache** stores the outputs of graph nodes, so a repeated input can reuse the result.

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
from langgraph.cache.gridgain import GridGainNodeCache
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

## GridGainNodeCache

`GridGainNodeCache` is a LangGraph node cache. It caches the results of graph nodes. It is not related to the LangChain `GridGainCache`, which caches model responses and uses a different interface.

To use the node cache, add a `CachePolicy` to each node whose output should be cached, and pass the cache to `compile`. Finish the edges of the graph before you compile it.

Given a connected `client`, a graph `builder`, and a node function `expensive`:

```python
from langgraph.cache.gridgain import GridGainNodeCache
from langgraph.types import CachePolicy

node_cache = GridGainNodeCache(client, cache_name="my_app_node_cache")
builder.add_node("expensive", expensive, cache_policy=CachePolicy(ttl=300))
graph = builder.compile(cache=node_cache)
```

In this example, a repeated input reuses the cached output of the node for 300 seconds. The results are stored in GridGain, so a new graph or cache instance can read them after a restart.

- TTL values are in **seconds**. Reading an entry does not extend its lifetime. If the TTL is `None`, the entry does not expire.
- The default cache name is `lg_node_cache`, and the cache is shared across the cluster. The node cache does not add an application identifier to the keys, so applications that must not share entries need different `cache_name` values.
- `node_cache.clear()` removes all entries from the whole cache. To remove only some namespaces, pass them to `clear()`. `graph.clear_cache()` removes the entries of the nodes of that graph.
- With an `AioClient`, the asynchronous methods use non-blocking I/O.

{% hint style="info" %}
The default cache key does not guarantee a cache hit for every equivalent chat input. For nodes that take chat messages, set an explicit `key_func` in the `CachePolicy` that covers all fields that affect the output of the node:

```python
def messages_key(state):
    return "|".join(f"{m.type}:{m.content}" for m in state["messages"])

builder.add_node(
    "call_model", call_model, cache_policy=CachePolicy(key_func=messages_key)
)
```
{% endhint %}

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

The memory store TTL values above are in minutes. The node cache TTL is in seconds.

## Upgrading From langchain-gridgain 2.x

In `langchain-gridgain` 2.x, the checkpointer and the memory store were part of the `langchain-gridgain` package. In version 3.0.0, they moved to `langgraph-checkpoint-gridgain`. Install the new package and update the imports:

```diff
-from langchain_gridgain import GridGainCheckpointSaver, GridGainMemoryStore
+from langgraph.checkpoint.gridgain import GridGainCheckpointSaver
+from langgraph.store.gridgain import GridGainMemoryStore
```

The classes, their behavior, and the stored data are unchanged. `GridGainNodeCache` was never released in `langchain-gridgain`. It is available starting with `langgraph-checkpoint-gridgain` 3.0.0. The `langchain_gridgain` package does not import them anymore, and there is no `langgraph_checkpoint_gridgain` module.
