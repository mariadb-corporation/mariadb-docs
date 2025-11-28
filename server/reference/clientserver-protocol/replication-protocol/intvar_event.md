---
description: >-
  This event records integer values for auto-increment columns or the
  LAST_INSERT_ID function, ensuring that these values are replicated
  deterministically.
---

# INTVAR\_EVENT

An `INTVAR_EVENT` is written every time a statement uses an auto increment column or the `LAST_INSERT_ID()` function.

## Header

* Event Type is `5` (`0x05`).

## Fields

* [uint<1>](../protocol-data-types.md#fixed-length-integers) Type.
* [uint<8>](../protocol-data-types.md#fixed-length-integers) Value.

## Type

|      |                              |
| ---- | ---------------------------- |
| 0x00 | Invalid value.               |
| 0x01 | LAST\_INSERT\_ID.            |
| 0x02 | Insert id (auto\_increment). |

## Example From mysqlbinlog Utility, CRC32

```sql
# at 738
#180610 11:20:56 server id 1  end_log_pos 770 CRC32 0xf5a23f2d 	Intvar
SET LAST_INSERT_ID=1/*!*/;
```

## Example Event As It's Written In The Binlog File

```
78 ed 1c 5b 05 01 00 00 00 20 00       x..[..... .
00 00 02 03 00 00 00 00 01 01 00 00 00 00 00 00  ................
00 2d 3f a2 f5                                   .-?..
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
