---
description: >-
  A heartbeat event sent over the network by the master when there are no binlog
  events, ensuring the replica knows the connection is still active.
---

# HEARTBEAT\_LOG\_EVENT

This event does not appear in the [binary log](../../../server-management/server-monitoring-logs/binary-log/). It's only sent over the network by a master to a replica server to let it know that the master is still alive, and is only sent when the master has no binlog events to send to replica servers.

{% hint style="info" %}
This event is never written to the binary log file.
{% endhint %}

## Header

* Timestamp is set to `0`.
* Next position is set to last position.
* Type is set to `HEARTBEAT_EVENT` (`0x1b`).

## Fields

* [string](../protocol-data-types.md#fixed-length-bytes) The current master binary log name.

## Example of Transmission (Without CRC32)

```
T 127.0.0.1:8808 -> 127.0.0.1:57157 [AP]
  23 00 00 04 00 00 00 00    00 1b 67 2b 00 00 22 00    '.........g+..&.
  00 00 ed 01 00 00 20 00    66 6f 6f 2d 62 69 6e 2e    ...... .log-bin.
  31 30 30 30 31 33 39                                  1000139
```

## Network Replication protocol, 5 bytes

* packet size \[3] = 23 00 00 => 00 00 23 => 35 (ok byte + event size).
* pkt sequence \[1] = 04.
* `OK` indicator \[1] = 0 (`OK`).

## Heartbeat Event

### **Header**

* Timestamp \[4] = 00 00 00 00 => 0.
* Event Type \[1] = 1b => 27.
* Server\_id \[4] = 67 2b 00 00 => 00 00 2b 67 => 111111.
* Event Size \[4] = 22 00 00 00 => 00 00 00 26 => 34 (header + data).
* Next\_pos \[4] = ed 01 00 00 => 00 00 01 ed => 493.
* Flags \[2] == 20 00 => 00 20 = > 32.

### **Content, String**

* log-bin.1000139.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
