---
description: >-
  Install and use the experimental GridGain 9 Python client to connect to a
  cluster, configure connections, and work with distributed maps.
---

# Python Client

{% hint style="warning" %}
This is an experimental API. It can change significantly in later releases.
{% endhint %}

## Getting Started

### Prerequisites

To run the Python client, the following is required:

- Python 3.10 or newer (3.10, 3.11, 3.12, 3.13 and 3.14 are tested)

### Installation

To install Python Client, download it using pip.

```bash
pip install pygridgain>=9
```

After this, you can import `pygridgain` into your project and use it.

```python
import pygridgain
```

## Limitations

Current release has the following limitations:

- Only Distributed Map API is currently available.
- The client only works with binary data.

## Connecting to Cluster

To connect to the cluster, use the `connect()` method:

```python
async def connect_simple():
    """Simple connection to a single GridGain node."""
    address = EndPoint('127.0.0.1', 10800)

    client = AsyncClient(address)
    await client.connect()
    print("Simple client connected")
    return client
```

You can also configure multiple endpoints for the failover and automatic load-balancing:

```python
async def connect_multiple_nodes():
    """Connection to multiple GridGain nodes for failover."""
    addresses = [
        EndPoint("127.0.0.1", 10800),
        EndPoint("127.0.0.1", 10801)
    ]

    client = AsyncClient(addresses)
    await client.connect()
    print("Client connected to multiple nodes")
    return client
```

## Client Configuration

### Connection Timeout

You can configure client connection timeout with optional `connection_timeout` parameter. The client will try to connect for the specified time and fail if no connection is established.

The timeout is specified in seconds. To specify smaller time units, use decimals. For example, `10.5` sets the timeout to `10500` milliseconds.

The example below shows how to set client timeout:

```python
async def connect_with_timeout():
    """Connection with custom timeout."""
    address = EndPoint('127.0.0.1', 10800)

    client = AsyncClient(address, connection_timeout=10.0)
    await client.connect()
    print("Client connected with timeout")
    return clientt
```

### Client Heartbeats

You can configure the client to periodically send messages to the server to keep the connection alive and avoid the idle timeout with an optional `heartbeat_interval` parameter.

By default, client heartbeat interval is set to 1/3 of [ignite.clientConnector.idleTimeoutMillis](overview.md#client-connector-configuration) configuration, or 0.5 seconds, whichever is larger. This configuration is sufficient to keep the client active in most scenarios.

The interval is specified in seconds. To specify smaller time units, use decimals. For example, `10.5` sets the heartbeat interval to `10500` milliseconds.

The example below shows how to set heartbeat interval:

```python
async def connect_with_heartbeat():
    """Connection with custom heartbeat interval."""
    address = EndPoint('127.0.0.1', 10800)

    client = AsyncClient(address, heartbeat_interval=10.0)
    await client.connect()
    print("Client connected with timeout")
    return clientt
```

### SSL Configuration

If the cluster uses [SSL](../../administrators-guide/security/ssl-tls.md) encryption, you should specify the ssl configuration to allow the client to connect to the cluster safely. The example below shows how you can provide SSL configuration:

```python
async def connect_with_ssl():
    """Secure connection with SSL configuration."""
    ssl_config = SSLConfig(
        protocol_version=ssl.PROTOCOL_TLS,
        cert_reqs=ssl.CERT_OPTIONAL,
        key_file="/path/to/client.key",
        cert_file="/path/to/client.crt",
        ca_file="/path/to/ca.crt"
    )

    address = EndPoint('127.0.0.1', 10800)

    client = AsyncClient(address, ssl_config=ssl_config)
    await client.connect()
    print("Secure client connected")
    return client
```

### Authentication

If the cluster has [authentication](../../administrators-guide/security/authentication.md) enabled, you should provide user credentials for your connection. The example below shows how you can configure authentication:

```python
async def connect_with_authentication():
    """Connection with username/password authentication."""
    auth = BasicAuthenticator("username", "password")
    address = EndPoint('127.0.0.1', 10800)

    client = AsyncClient(address, authenticator=auth)
    await client.connect()
    print("Authenticated client connected")
    return client
```

## Working With Distributed Maps

The Python client provides an API for working with [distributed maps](../data-structures/map-structure.md).

{% hint style="info" %}
Currently, Python client only works with binary data.
{% endhint %}

### Creating or Getting Map

You can use the `get_or_create_binary_map` method to get the distributed map. If a map with the specified name exists, the client will get it from the cluster. If not, a new map will be created.

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')
```

### Adding Data to Maps

There are 2 methods that can be used to add data to distributed maps:

- `put` method adds a single value.
- `put_all` method adds a batch of values at the same time. Using this method is functionally equivalent to adding values individually with `put` method, but it works much faster for bigger amount of records..

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')

    await binary_map.put(b'1', b'Hello World')
    value = await binary_map.get(b'1')
    print(f"Retrieved value: {value.decode()}")

    batch_data = {
        b"2": b"Great World",
        b"3": b"Goodbye World"
    }
    await binary_map.put_all(batch_data)
```

### Iterating Maps Entries

Instead of working with entries one by one, you can iterate through all of them:

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')

    print("\nAll entries:")
    async for key, value in binary_map:
        print(f"Key: {key.decode()}, Value: {value.decode()}")
```

### Getting Data From Maps

You can check if the specific key exists on the cluster and get it with the following methods:

- `contains` method only checks if the entry  exists. It does not retrieve the value.
- `get` method retrieves the value associated with the specified key.

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')

    value = await binary_map.get(b'1')
    print(f"Retrieved value: {value.decode()}")
```

### Deleting Data in Maps

You can delete data in distributed maps with the following methods:

- `pop` method deletes a specific entry and returns the value it used to contain.
- `clear` method fully removes all data from the distributed map.

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')

    popped_value = await binary_map.pop(b"1")
    print(f"Removed value: {popped_value.decode()}")

    await binary_map.clear()
    print("Map cleared")
```

### Checking Map Information

You can get additional information about distributed maps with the following methods:

- `count` method returns the number of entries in the distributed map.
- `empty` checks if the distributed map is empty. This command works much faster than `count() == 0` and should be used when you only care about the emptiness of the map.

```python
async with await connect_simple() as client:
    await client.connect()
    print("Client connected")

    # Get or create a binary map
    binary_map = await client.structures().get_or_create_binary_map('myMap')

    count = await binary_map.count()
    print(f"\nMap contains {count} entries")

    is_empty = await binary_map.empty()
    print(f"Map is empty: {is_empty}")
```
</content>
