---
description: >-
  The XID_EVENT signifies the commit of a transaction, containing the
  transaction ID (XID) to ensure atomicity across replication.
---

# XID\_EVENT

An XID event is generated for a `COMMIT` of a transaction that modifies one or more tables of an XA-capable storage engine.

## Header

* Event Type is `XID_EVENT` (`0x10`).

## Fields

[uint<8>](../protocol-data-types.md#fixed-length-integers) The XID transaction number.

## Complete Example With CRC32

```
ee b7 15 5a 10 01 00 00  00 1f 00 00 00 f2 0b 00  ...Z............
00 00 00 66 00 00 00 00  00 00 00 09 30 45 a8     ...f.........0E.
```

## Header, 19 Bytes

Event size is: header\[19] + XID\[8] + CRC32\[4] of (header + xid).

* Event Time ee b7 15 5a => 5a 15 b7 ee => 1511372782 \[2017-11-22 18:46:22].
* Event Type = 10.
* Server\_id 01 00 00 00 => 1.
* Event Size 1f 00 00 00 => 31.
* Next Pos f2 0b 00 00 => 00 00 0b f2 => 3058.
* Flags 00 00 = 0.

## Content, 8 Bytes

* XID 66 00 00 00 00 00 00 00 => 102.

## CRC32, 4 Bytes

* 09 30 45 a8 => a8 45 30 09 => 2823106569.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
