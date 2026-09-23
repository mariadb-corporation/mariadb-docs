---
description: >-
  GridGain 9.1.6 adds a Python client and extended bootstrap configuration support, along with various SQL, storage, and client fixes.
---

# GridGain 9.1.6 Release Notes

## Overview

GridGain 9.1.6 is a release with multiple minor improvements, including better backward compatibility support for bootstrap configuration, a new Python 3 client, extended distributed map configuration options, and various bug fixes across SQL, storage, and platform clients.

## Major Changes

### Extended Bootstrap Support

This release features extended backwards compatibility support for bootstrap configuration. You can now configure your compose files in the same way as you did in GridGain 9.1.4 and earlier with a minor update. Bootstrap configuration from 9.1.5 is also temporarily supported to allow for fluid migration to later versions.

To migrate from your earlier docker compose configurations, add a `BOOTSTRAP_NODE_CONFIG` environment variable to your configuration like that points to where the configuration file is stored in the container.

The example below shows how to do this:

```yaml
x-gridgain-def: &gridgain-def
  image: gridgain/gridgain9:9.1.6
  environment:
    BOOTSTRAP_NODE_CONFIG: /opt/gridgain/etc/gridgain-config.conf # Uses the configuration file to start GridGain 9.
  configs:
    - source: node_config
      target: /opt/gridgain/etc/gridgain-config.conf # Stores the configuration file defined elsewhere in node_config element in the compose file.
      mode: 0644
```

In the example above, `BOOTSTRAP_NODE_CONFIG` environment variable is set up to use the configuration file defined in the compose file.

## New Features

### Python Client

This release brings the first version of the Python client. The client API is experimental and may change in subsequent releases. Currently, the Python client is exclusively dedicated to working with distributed maps.

You can install the python client from pip by installing `pygridgain` of version 9 or later:

```bash
pip install pygridgain>=9
```

The following example demonstrates how you can use the client to create a map, add a value to it, and get it back:

```python
async with AsyncClient(address) as client:
    await client.connect()
    print("client connected")
    binary_map = await client.structures().get_or_create_binary_map('myMap')
    await binary_map.put(b'1', b'Hello World')
    value_exists = await binary_map.contains(b'1')
    print(f"Does 1 exist on the cluster: {value_exists}")
    print(await binary_map.get(b'1'))
```

For more information about Python client, see [client documentation](../../developers-guide/clients/python-client.md).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28521 | Cluster Storage Engine | Node configuration file is no longer updated on node start. |
| IGN-28375 | General | The changes in ignite.gc.lowWatermark.updateIntervalMillis configuration are now applied immediately. |
| IGN-28366 | General | Fixed a possible deadlock during data rebalancing when a node leaves under heavy load and returns to the cluster after a long time. |
| IGN-28346 | Cluster SQL Engine | Fixed an ArrayIndexOutOfBounds exception that happened when merge operation included JOINs. |
| IGN-28270 | General | Nodes now export some metrics to the log by default. |
| IGN-28113 | Cluster SQL Engine | Fixed an issue that caused time values to be incorrectly trimmed when converted to string via getString method of JDBC ResultSet. |
| IGN-28044 | SQL | TIME and TIMESTAMP data types conversion now correctly accounts for required precision. |
| IGN-27950 | General | Nodes now reliably destroy dropped tables after restart. |
| IGN-27917 | SQL | Added CURRENT_USER SQL function. |
| IGN-27821 | Platforms and Clients | C++ client: Added support for configuring transaction timeouts. |
| IGN-26455 | Distributed Computing | Added new compute task events. |
| GG-44621 | Cluster Storage Engine | Fixed data inconsistency issues when using columnar storage in Docker. |
| GG-44404 | General | Fixed NullPointerException when logging address binding error for data center replication. |
| GG-44379 | Builds and Deliveries | Added -XX:+PerfDisableSharedMem JVM parameter to bootstrap configuration to improve performance in certain scenarios. |
| GG-44340 | Cluster Storage Engine | Fixed a rare scenario where select with projection could fail. |
| GG-44188 | Cluster Continuous Queries | .NET client can now handle CQ events coming after table dropped. |
| GG-44170 | Distributed Data Structures | You can now specify the non-standard storage engine for distributed maps. |
| GG-44169 | Distributed Data Structures | You can now specify the distribution zone the distributed map will be stored at. |
| GG-43851 | Platforms & Clients | Added Python 3 client. |
| GG-42333 | Builds and Deliveries | Added Linux ARM64 support for Columnar store. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`, `9.1.3`, `9.1.4`, `9.1.5`

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
