---
description: >-
  A marker event indicating a checkpoint in the binary log, used to ensure
  consistency and safe rotation of log files.
---

# BINLOG\_CHECKPOINT\_EVENT

Binlog Checkpoint Event, Event Type is 161 (0xa1). This event specifies a binlog file such that XA crash recovery can start from that file.

{% hint style="info" %}
There can be more than one event in a binlog file.
{% endhint %}

## Header

* Event type is 161 (0xa1).

## Fields

* [uint<4>](../protocol-data-types.md#fixed-length-integers) Log filename length.
* [string](../protocol-data-types.md#fixed-length-bytes) Log filename.

## Example Without CRC32

```
12 ad 26 5a a1 84 27 00  00 27 00 00 00 47 01 00  ..&Z..'..'...G..
00 00 00 10 00 00 00 6d  79 73 71 6c 2d 62 69 6e  .......mysql-bin
2e 30 30 30 30 36 32                              .000062
```

## Header, 19 Bytes

* Event Timestamp = 12 ad 26 5a.
* Event Type = a1 => 161.
* Server\_id = 84 27 00 00 => 00 00 27 84 = 10116.
* Event Size = 27 00 00 00 => 00 00 00 27 = 39.
* Next Pos = 47 01 00 00 => 00 00 01 47 = 327.
* Flags = 00 => 0.

## Content, Variable Size

* Filename length = 10 00 00 00 = >00 00 00 10 => 16.
* Filename = mysql-bin.000062.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
