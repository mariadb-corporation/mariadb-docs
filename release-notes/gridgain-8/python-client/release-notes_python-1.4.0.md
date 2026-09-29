---
description: >-
  PyGridGain 1.4.0 adds Python 3.10 support, a handshake timeout, monitoring and
  event handling, transactions, and expiry policy configuration.
hidden: true
---

# PyGridGain 1.4.0 Release Notes

## New Features

PyGridGain 1.4.0 provides access to new features and improvements.

### Support for Python 3.10

You can now use Python 3.10 to work with GridGain. Pre-built packages for Python 3.10 were added into the package.

### Handshake Timeout

Handshake operation now has timeout argument. You can set it in the following way:

```python
client = Client(handshake_timeout=3.0)
```

### Monitoring and Event Handling

Monitoring and event handling were added. You can track events, or set up a query logger. Here is the example:

```python
class RecordingConnectionEventListener(ConnectionEventListener):
    def on_handshake_start(self, event):
        events.append(event)

    def on_handshake_success(self, event):
        events.append(event)

    def on_handshake_fail(self, event):
        events.append(event)

    def on_authentication_fail(self, event):
        events.append(event)

    def on_connection_closed(self, event):
        events.append(event)

    def on_connection_lost(self, event):
        events.append(event)

# Sync API:
    client = Client(event_listeners=[RecordingConnectionEventListener()])
#   ...

# Async API:
    client = AioClient(event_listeners=[RecordingConnectionEventListener()])"
#   ...
```

### Transactions

Transaction operations are now supported. Both synchronous and asynchronous APIs are supported:

{% tabs %}
{% tab title="Sync" %}
```python
with client.tx_start(isolation=iso_level, concurrency=concurrency) as tx:
    tx_cache.put(1, 1)
    tx.commit()

assert tx_cache.get(1) == 1
```
{% endtab %}

{% tab title="Async" %}
```python
async with async_client.tx_start(isolation=iso_level, concurrency=concurrency) as tx:
    await async_tx_cache.put(1, 1)
    await tx.commit()

assert await async_tx_cache.get(1) == 1"
```
{% endtab %}
{% endtabs %}

### Expiry Policy

Added support for configuring ExpiryPolicy for cache operations. Here is how you can set it up:

```python
cache_eternal = cache.with_expire_policy(create=ExpiryPolicy.ETERNAL)
cache_created = cache.with_expire_policy(create=0.6)
cache_updated = cache.with_expire_policy(update=0.6)
cache_accessed = cache.with_expire_policy(access=0.6)"
```

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-35197 | Added prebuilt biniary for Python 3.10 |
| GG-33939 | Added handshake timeout. |
| GG-33936 | Added monitoring and event handling. |
| GG-33923 | Added logging. |
| GG-33908 | Unified timeouts across the entire Python client API. |
| GG-33899 | Partition awareness is now enabled by default. |
| GG-33857 | Added support for transactions. |
| GG-33821 | Added ExpiryPolicy support. |
| GG-33820 | Fixed potential binary object serialization issues. |
| GG-33810 | Fixed implicit ByteArray to string conversion. |
| GG-33808 | Fixed a bug that sometimes caused random freezes when using sync client due to partial read from TCP socket. |
| GG-33663 | Fixed an issue with nested array deserialization. |

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
pip install pygridgain==1.4.0
```

## Previous Releases

- [PyGridGain 1.3.1](release-notes_python-1.3.1.md)
- [PyGridGain 1.2.0](release-notes_python-1.2.0.md)

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
