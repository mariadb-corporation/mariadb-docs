---
description: >-
  This page defines the fundamental data types used in the MariaDB client/server
  protocol, including integers, strings, and binary representations.
---

# Protocol Data Types

## List of Possible Types

Unknown type:

|                                                               |                          |
| ------------------------------------------------------------- | ------------------------ |
| [byte<1>](protocol-data-types.md#fixed-length-bytes)          | Fixed-length bytes       |
| [byte\<lenenc>](protocol-data-types.md#length-encoded-bytes)  | Length-encoded bytes     |
| [byte\<EOF>](protocol-data-types.md#end-of-file-length-bytes) | End-of-file length bytes |

Integer type:

|                                                                |                         |
| -------------------------------------------------------------- | ----------------------- |
| [int<1>](protocol-data-types.md#fixed-length-integers)         | Fixed-length integers   |
| [int\<lenenc>](protocol-data-types.md#length-encoded-integers) | Length-encoded integers |

String type:

|                                                                   |                            |
| ----------------------------------------------------------------- | -------------------------- |
| [string\<fix>](protocol-data-types.md#fixed-length-strings)       | Fixed-length strings       |
| [string\<NUL>](protocol-data-types.md#null-terminated-strings)    | Null-terminated strings    |
| [string\<lenenc>](protocol-data-types.md#length-encoded-strings)  | Length-encoded strings     |
| [string\<EOF>](protocol-data-types.md#end-of-file-length-strings) | End-of-file length strings |

### Fixed-Length Bytes

The notation is `byte`_`<n>`_, where _`<n>`_ is a positive integer. A fixed-length byte stores the value in a series of `n` bytes.

### Length-Encoded Bytes

The notation is `byte<lenenc>`. Length-encoded bytes are prefixed by a length-encoded integer which describes the length of the byte value, followed by the bytes value.

### End of File Length Bytes

The notation is `byte<EOF>`. Bytes whose length is calculated by the packet remaining length.

### Fixed-Length Integers

Notation is `int`_`<n>`_, where _`<n>`_ is a positive integer. A fixed-length integer stores the value in a series of `n` bytes. The least significant byte is always the first byte (little-endian format).

#### Example

An `int<4>` with value of `2` is stored as `02 00 00 00` .

### Length-Encoded Integers

The notation is `int<lenenc>`. An integer which depending on its value is represented by `n` bytes.

The first byte represents the size of the integer, depending on the value of the first byte:

* < `0xFB` - Integer value is this a 1-byte integer
* `0xFB` - `NULL` value
* `0xFC` - Integer value is encoded in the next 2 bytes (3 bytes total)
* `0xFD` - Integer value is encoded in the next 3 bytes (4 bytes total)
* `0xFE` - Integer value is encoded in the next 8 bytes (9 bytes total)

### Fixed-Length Strings

The notation is `string<fix>`. Fixed-length strings have a known hardcoded length.

### Null-Terminated Strings

The notation is `string<NUL>`. Null-terminated strings have a variable size and are terminated by a `0x00` character.

### Length-Encoded Strings

The notation is `string<lenenc>`. Length-encoded strings are prefixed by a length-encoded integer which describes the length of the string, followed by the string value.

#### Example

An string of 512 "a" is encoded in 515 bytes:

{% code overflow="wrap" %}
```
fc 00 02 97 97 97 97 97 97 97 97 97 97 97 97 97	² .. a a a a a a a a a a a a a
```
{% endcode %}

The `NULL` value is encoded using null (`0xfb`) length.

An empty value is encoded with a 0 (`0x00`) length.

### End of File Length Strings

The notation is `string<EOF>`.

Strings whose length is calculated by the packet remaining length. For an example, see the [COM\_STMT\_PREPARE](3-binary-protocol-prepared-statements/com_stmt_prepare.md) packet.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
