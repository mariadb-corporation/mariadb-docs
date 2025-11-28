---
description: >-
  This event marks the beginning of encrypted data in the binary log, defining
  the encryption scheme and key version for subsequent events.
---

# START\_ENCRYPTION\_EVENT

The `START_ENCRYPTION` event is written to every [binary log](../../../server-management/server-monitoring-logs/binary-log/) file if [encrypt\_binlog](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is set to `ON`.

This event is written just once, after the Format Description event (which is the first event of a binlog file at pos 4).

The event has the 19 bytes event header with EventType set to value `164` (`0xa4`) + 17 bytes data.

## Header

* Event type is `164` (`0xa4`).

## Fields

* [uint<1>](../protocol-data-types.md#fixed-length-integers) The Encryption scheme, always set to 1 for system files.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) The Encryption key version.
* [byte<12>](../protocol-data-types.md#fixed-length-bytes) Nonce (12 random bytes) of current binlog file.

## Decryption of Following Events

All data of following events in the binlog file are encrypted, except for the `event_length` field.

The 16 byte encryption IV is generated from the 12 byte nonce ([uint<12>](../protocol-data-types.md#fixed-length-integers)) in the binlog plus the current position of the event being encrypted ([uint<4>](../protocol-data-types.md#fixed-length-integers)). This means the last four bytes of the IV change for every event and the first 12 bytes change for every binlog file.

Since the `event_length` is always unencrypted, the encrypted data block has to be modified before it can be decrypted:

* Store event\_length.
* Copy the first four bytes (encrypted timestamp) to event\_length position (offset=9).
* Decrypt starting from offset 4 and store result at offset 4 of decrypted buffer.

The unencrypted block now also needs to be modified:

* Move unencrypted timestamp value from offset 9 to the beginning (offset=0).
* Store event\_length at position 9.

## Complete example with CRC32 from a binary log.

```
b8 5f 5a 59 a4 5d 00 00  00 28 00 00 00 21 01 00 ._ZY.]...(...!..
00 00 00 01 01 00 00 00  65 57 50 26 63 59 37 46 ........eWP&cY7F
2f 3b 33 23 06 bb da 62                          /;3#...b
```

### Header, 19 Bytes

* timestamp \[4] = b8 5f 5a 59 => 59 5a 5f b8 => 1499094968 \[2017-07-03 17:16:08].
* type \[1} = a4 => 164.
* server\_id \[4} = 5d 00 00 00 => 00 00 00 5d => 93.
* event\_size \[4] = 28 00 00 00 => 00 00 00 28 => 40 \[header + content + crc32(header + content)].
* next\_pos \[4] = 21 01 00 00 => 00 00 01 21 => 289.
* flags \[2] = 00 00 => 0.

### Content, 17 Bytes

* Enc scheme \[1] = 01 => 1.
* Enc key ver \[4] = 01 00 00 00 => 00 00 00 01 => 1.
* Nonce \[12] = eWP\&cY7F/;3#.

### CRC32, 4 bytes, of the Whole Event (Header\[19] + Content\[17])

* 06 bb da 62 => 62 da bb 06 => 1658501894.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
