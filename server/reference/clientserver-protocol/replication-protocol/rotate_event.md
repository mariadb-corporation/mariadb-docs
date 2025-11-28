---
description: >-
  The ROTATE_EVENT indicates a log rotation, specifying the name of the next
  binary log file and the position where writing will continue.
---

# ROTATE\_EVENT

When a [binary log](../../../server-management/server-monitoring-logs/binary-log/) file exceeds the configured size limit, a `ROTATE_EVENT` is written at the end of the file, pointing to the next file in the sequence.

`ROTATE_EVENT` is generated locally and written to the binary log on the master. It is also written when a [FLUSH LOGS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) statement occurs on the master server.

The `ROTATE_EVENT` is sent to the connected replica servers.

## Header

* The Event Type is `ROTATE_EVENT` (`0x4`).

## Fields

* [uint<8>](../protocol-data-types.md#fixed-length-bytes) The position of the first event in the next log file. It always contains the number `4` (meaning the next event starts at position 4 in the next binary log).
* [string](../protocol-data-types.md#fixed-length-bytes) The next binary log name. The filename is not null-terminated.

## Example of Transmission With CRC32 (The Last 4 Bytes)

```
T 127.0.0.1:8808 -> 127.0.0.1:57157 [AP]
  30 00 00 4d 00 bc 4e 21    5a 04 d9 27 00 00 2f 00    0..M..N!Z..'../.
  00 00 c0 01 00 00 00 00    04 00 00 00 00 00 00 00    ................
  6d 79 73 71 6c 2d 62 69    6e 2e 30 30 30 30 31 39    mysql-bin.000019
  b2 bc db bf                                           ....
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
