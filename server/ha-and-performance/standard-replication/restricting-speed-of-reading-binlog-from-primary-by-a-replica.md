---
description: >-
  Configure throughput limits for replication traffic. Learn to throttle the
  binlog download speed to prevent replication from consuming all available
  network bandwidth.
---

# Restricting Speed of Reading Binlog from Primary by a Replica

When a replica starts after being stopped for some time, or a new replica starts\
that was created from a backup from some time back, a lot of old binlog events\
may need to be downloaded from the primary. If this happens from many replicas\
simultaneously, it can put a lot of load on the primary.

The **read\_binlog\_speed\_limit** option can be used to reduce such load, by\
limiting the speed at which events are downloaded. The limit is given as\
maximum kilobytes per second to download on one replica connection.

With this option set, the replication I/O thread will limit the rate of\
download. Since the I/O thread is often much faster to download events than\
the SQL thread is at applying them, an appropriate value for**read\_binlog\_speed\_limit** may reduce load spikes on the primary without\
much limit in the speed of the replica.

The option **read\_binlog\_speed\_limit** is available starting from [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3).

#### `read_binlog_speed_limit`

* Description: Maximum speed(KB/s) to read binlog from primary.
* Command line: `--read-binlog-speed-limit[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
