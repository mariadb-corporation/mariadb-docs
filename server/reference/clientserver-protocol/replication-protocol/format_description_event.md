---
description: >-
  This descriptor event appears at the start of every binary log file, defining
  the server version, binlog version, and header lengths for all event types.
---

# FORMAT\_DESCRIPTION\_EVENT

This is a descriptor event that is written to the beginning of a [binary log](../../../server-management/server-monitoring-logs/binary-log/) file, at position 4 (after the 4 magic number bytes). The whole event written to disk is [byte<19>](../protocol-data-types.md#fixed-length-bytes) event header + data fields.

## Header

* The Event Type is 15 (0x0f).

## Fields

* [uint<2>](../protocol-data-types.md#fixed-length-integers) The binary log format version. This is `4` .
* [string<50>](../protocol-data-types.md#fixed-length-bytes) The MariaDB server version (example: 10.8.1-debug-log), padded with 0x00 bytes on the right.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Timestamp in seconds when this event was created (this is the moment when the binary log was created). This value is redundant; the same value occurs in the timestamp header field.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) The header length. This length `-19` gives the size of the extra headers field at the end of the header for other events.
* [byte](../protocol-data-types.md#fixed-length-bytes) Variable-sized. An array that indicates the post-header lengths for all event types.\
  There is one byte per event type that the server knows about. The value 'n' comes from the following formula:

```
n = event_size - header length - offset (2 + 50 + 4 + 1) - checksum_algo - checksum
```

* [uint<1>](../protocol-data-types.md#fixed-length-integers) Checksum Algorithm Type
* [uint<4>](../protocol-data-types.md#fixed-length-integers) CRC32 4 bytes (value matters only if checksum algo is CRC32)

## Example FDE of MariaDB With CRC32

```
4d af 15 5a 0f 01 00 00  00 fc 00 00 00 00 01 00  M..Z............
00 00 00 04 00 31 30 2e  32 2e 31 30 2d 4d 61 72  .....10.2.10-Mar
69 61 44 42 2d 6c 6f 67  00 00 00 00 00 00 00 00  iaDB-log.......
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00 00 00 00 00 00 00 00  00 00 00 4d af 15 5a 13  ...........M..Z.
00 12 00 04 04 04 04 12  00 00 e4 00 04 1a 08 00  ................
00 00 08 08 08 02 00 00  00 0a 0a 0a 00 00 00 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
0d 08 08 08 0a 0a 0a 01  d6 ce 13 e2              ............
```

### Header, 19 Bytes

* timestamp => 4d af 15 5a.
* type = 0f => 15.
* server\_id = 1.
* Event Size = fc => 252.
* Next Pos = 00 01 00 00 => 00 00 01 00 => 256.
* Flags = 00 => 0.

### Content, Variable Size Depending on MariaDB Versions

* format version = 04 00 => 4.
* server's version = 10.2.10-MariaDB-log .... \[50 bytes].
* create time = 4d af 15 5a.
* header\_length = 13 => 19.
* event\_types array\[252 - 19 - (2 + 50 + 4 +1) - 1 - 4] = 171 supported events.
* checksum\_algo = 01 => 1 (CRC32).
* CRC32 bytes = d6 ce 13 e2.

## Example FDE of MariaDB With CRC32

```
12 ad 26 5a 0f 84 27 00  00 f5 00 00 00 f9 00 00  ..&Z..'.........
00 01 00 04 00 31 30 2e  31 2e 31 36 2d 4d 61 72  .....10.1.16-Mar
69 61 44 42 00 6c 6f 67  00 00 00 00 00 00 00 00  iaDB.log........
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00 00 00 00 00 00 00 12  ad 26 5a 13 38 0d 00 08  .........&Z.8...
00 12 00 04 04 04 04 12  00 00 dd 00 04 1a 08 00  ................
00 00 08 08 08 02 00 00  00 0a 0a 0a 00 00 00 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00 00 00 00 00 00 00 00  00 00 00 00 04 13 04 00  ................
00 2b 91 c2 91
```

### Header, 19 Bytes

* timestamp => 12 ad 26 5aa.
* type = 0f => 15.
* server\_id = 84 27 00 00 => 00 00 27 84 => 10116.
* Event Size = fc => 245.
* Next Pos = f9 00 00 00 => 00 00 00 f9 => 249.
* Flags = 00 => 0.

### Content, Variable Size Depending on MariaDB Versions

* format version = 04 00 => 4.
* server's version = 10.1.16-MariaDB.log .... \[50 bytes].
* create time = 12 ad 26 5a.
* header\_length = 13 => 19.
* event\_types array\[245 - 19 - (2 + 50 + 4 +1) - 1 - 4] = 164 supported events.
* checksum\_algo = 0 => 0 (NONE).
* CRC32 bytes = 2b 91 c2 91 (useless).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
