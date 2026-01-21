---
description: >-
  This command is used by a replica to register its details, such as server ID,
  hostname, and port, with the primary server.
---

# COM\_REGISTER\_SLAVE

This command is sent by the replica server to start MariaDB replication, and should be sent before requesting binlog events with [COM\_BINLOG\_DUMP](com_binlog_dump.md).

The payload is:

* [uint<1>](../protocol-data-types.md#fixed-length-bytes) command (`COM_REGISTER_SLAVE` = `0x15`).
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Replica server ID.
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Replica hostname length.
* [string](../protocol-data-types.md#fixed-length-bytes) Hostname.
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Replica username length.
* [string](../protocol-data-types.md#fixed-length-bytes) Username.
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Replica password length.
* [string](../protocol-data-types.md#fixed-length-bytes) Replica password.
* [uint<2>](../protocol-data-types.md#fixed-length-bytes) Replica connection port.
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Replication rank.
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Master server ID.

**Note**:

* Replica hostname, replica user, replica password, and replica port are usually not set.\
  Some replica [replication parameters](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) can be used for such settings (`report_host`, `report_port` etc).
* Replication rank is not set.
* Master server ID is not set either.

## Example of COM\_REGISTER\_SLA

The replica server is configured with:

* server-id=10101;
* report-host=slave\_n\_1;
* report-port=23241.

```
1b 00 00 00 15 75 27 00    00 09 73 6c 61 76 65 5f    .....u'...slave_
 6e 5f 31 00 00 c9 5a 00    00 00 00 00 00 00 00       n_1...Z.......
```

We can see from the example:

* server\_id \[4] = 75 27 00 00 => 10101.
* hostname\_len \[1] = 09.
* hostname\[n] = slave\_n\_1 (9 bytes).
* username len \[1] = 0 (not set).
* password len \[1] = 0 (not set).
* slave port \[2] = c9 5a => 23241.
* rank \[4] = 0.
* master server id = 0.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
