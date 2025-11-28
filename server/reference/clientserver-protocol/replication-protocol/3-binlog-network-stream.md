---
description: >-
  Describes the continuous packet stream format used to transmit binary log
  events from the primary server to the replica over the network.
---

# 3-Binlog Network Stream

The binary log events stored in a binary log file can be sent over the network in order to replicate data changes from the master server (where data changes are written in binary logs) to replica servers which apply data changes to their own databases.

The MariaDB replica replication protocol consists of:

* A registration phase to master;
* Events receiving (the master sending data when changes are available).

{% hint style="info" %}
This section is related to **events sending only**.
{% endhint %}

Binlog Network streams are requested with `COM_BINLOG_DUMP` , and each Binlog Event is prepended with a status byte. The data sent over network is then MariaDB network protocol (4 bytes) + 1 byte status flag + event data.

MariaDB [network protocol](../0-packet.md) 4 bytes are:

* [uint<3>](../protocol-data-types.md#fixed-length-integers) packet length (the sent binlog event can be up to 2^24 - 1 - 1 data bytes).
* [uint<1>](../protocol-data-types.md#fixed-length-integers) packet sequence byte<1>(0 to 255).

Replication protocol status byte:

* [uint<1>](../protocol-data-types.md#fixed-length-integers) OK (0) or ERR (ff) or End of File, EOF, (fe).

{% hint style="warning" %}
Due to the 1 byte status flag, the effective data payload is event\_size + 1. This means than an event of exactly 16M bytes (2 ^ 24 - 1) cannot be sent in one transmission: it requires 2 packets instead.
{% endhint %}

```
packet #n:   3 bytes length + sequence + status + [event_header + (event data - 1)]
packet #n+1: 3 bytes length + sequence + last byte of the event data.
```

{% hint style="info" %}
The remaining bytes of a large event transmission are always sent **without** a status flag and binlog event header, but rather just as network packet header + data.
{% endhint %}

## Example of an Event Transmission HEARTBEAT\_LOG\_EVENT

```
T 127.0.0.1:8808 -> 127.0.0.1:57157 [AP]
  23 00 00 04 00 00 00 00    00 1b 67 2b 00 00 22 00    '.........g+..&.
  00 00 ed 01 00 00 20 00    66 6f 6f 2d 62 69 6e 2e    ...... .log-bin.
  31 30 30 30 31 33 39                                  1000139
```

### Network Replication Protocol, 5 Bytes

* packet size \[3] = 23 00 00 => 00 00 23 => 35 (ok byte + event size).
* pkt sequence \[1] = 04.
* `OK` indicator \[1] = 0 (`OK`).

### [Heartbeat event](heartbeat_log_event.md)

* Header, 19 bytes.
* Content, string.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
