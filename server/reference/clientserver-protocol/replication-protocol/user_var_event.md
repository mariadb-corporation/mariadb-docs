---
description: >-
  The USER_VAR_EVENT logs the value of a user-defined variable, ensuring that
  statements using variables replicate consistently.
---

# USER\_VAR\_EVENT

A `USER_VAR_EVENT` is written every time a statement uses a user defined variable.

## Header

* Event Type is `14` (`0x0e`).

## Fields

* [uint<4>](../protocol-data-types.md#fixed-length-integers) The length of the user variable name.
* [string](../protocol-data-types.md#fixed-length-strings) The name of the user variable.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) `NULL` indicator.
* If (not null indicator):
  * [uint<1>](../protocol-data-types.md#fixed-length-integers) variable type.
  * [uint<4>](../protocol-data-types.md#fixed-length-integers) collation number.
  * [uint<4>](../protocol-data-types.md#fixed-length-integers) The length of value.
  * [string](../protocol-data-types.md#fixed-length-strings) value.
  * [uint<1>](../protocol-data-types.md#fixed-length-integers) flags.

## Variable type

| Value | Type            | Example              |
| ----- | --------------- | -------------------- |
| 0x00  | STRING\_RESULT  | set @a:="foo"        |
| 0x01  | REAL\_RESULT    | set @a:= @@timestamp |
| 0x02  | INT\_RESULT     | set @a:= 4           |
| 0x03  | ROW\_RESULT     | (not in use)         |
| 0x04  | DECIMAL\_RESULT | set @a:=1.2345       |

## Flag

|      |          |
| ---- | -------- |
| 0x01 | unsigned |

## Example for `SET @foo:="bar"` From mysqlbinlog Utility, CRC32

```
# at 511
#180610 10:26:43 server id 1  end_log_pos 554 CRC32 0x7dd93d6b 	User_var
SET @`foo`:=_utf8 X'626172' COLLATE `utf8_general_ci`/*!*/;
```

## Example Event as Written to the Binlog File

```
c3 e0 1c 5b 0e 01 00 00 00 2b 00       ...[.....+.
00 00 2a 02 00 00 00 00 03 00 00 00 66 6f 6f 00  ..*.........foo.
00 21 00 00 00 03 00 00 00 62 61 72 6b 3d d9 7d  .!.......bark=.}                                          ....
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
