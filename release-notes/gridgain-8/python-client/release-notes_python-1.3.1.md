---
description: >-
  PyGridGain 1.3.1 adds support for the with statement, asynchronous I/O through
  asyncio, and a new API for retrieving and changing the cluster state.
hidden: true
---

# PyGridGain 1.3.1 Release Notes

## New Features

PyGridGain 1.3.1 provides access to new features and improvements.

### Connection Support "with" Statement

Connection method of Client class now supports "with" statement semantics.

```python
client = Client()
with client.connect('127.0.0.1', 10800):
    do_something()
	# When the block ends connection is closed automatically
```

### Asynchronous I/O Support

Pygridgain now supports asyncio to provide asynchronous API. See https://docs.python.org/3/library/asyncio.html for details.

See https://github.com/gridgain/python-thin-client/blob/master/examples/async_key_value.py and https://github.com/gridgain/python-thin-client/blob/master/examples/async_sql.py for detailed usage examples.

```python
client = AioClient()
    async with client.connect('127.0.0.1', 10800):
        # Create cache
        cache = await client.get_or_create_cache('my_async_cache')

		# Load data concurrently.
        await asyncio.gather(
            *[cache.put(f'key_{i}', f'value_{i}') for i in range(0, 20)]
        )

        # Key-value queries.
        print(await cache.get('key_10'))
        print(await cache.get_all([f'key_{i}' for i in range(0, 10)]))
        # value_10
        # {'key_3': 'value_3', 'key_2': 'value_2', 'key_1': 'value_1','....}
```

### Ability to Retrieve and Change Cluster State

In this release, we added a new API that can be used to get and change the cluster state.

```python
    client = Client()
    with client.connect("127.0.0.1", 10801):
        cluster = client.get_cluster()
        print(f'Changing state from {cluster.get_state()} to ClusterState.ACTIVE_READ_ONLY')

        cluster.set_state(ClusterState.ACTIVE_READ_ONLY)
```

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-32946 | Connection method of Client class now supports "with" semantics and can be used like this: with client.connect('my_address'): |
| GG-32914 | Pygridgain now supports asyncio to provide asynchronous API. See https://docs.python.org/3/library/asyncio.html for details. |
| GG-32909 | Added C module that significantly increases performance during hash calculation, which is especially visible during the operations with big objects. Package is shipped with pre-built extension for pythons 3.6-3.9, x86, x86_64 and Linux and Windows OSs. |
| GG-31859 | Added new API that can be used to get and change the cluster state. |

## Installation and Upgrade Information

To upgrade an existing package, use the following command:

```shell
pip install --upgrade pygridgain
```

To install the latest version of a package:

```shell
pip install pygridgain
```

To install a specific version:

```shell
pip install pygridgain==1.3.1
```

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
