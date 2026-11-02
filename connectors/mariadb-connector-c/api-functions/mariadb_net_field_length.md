# mariadb\_net\_field\_length

## Syntax

```bnf
#include <mysql.h>

int mariadb_net_field_length(unsigned char **packet,
                             const unsigned char *end,
                             int flags,
                             unsigned long *length)
```

## Parameter

| Parameter | Description                                                                      |
| --------- | -------------------------------------------------------------------------------- |
| `packet`  | Pointer to the read position in the packet buffer. On success, it is advanced past the length-encoded integer. (verify: its state after MARIADB_LENENC_NULL and MARIADB_LENENC_ERROR.) |
| `end`     | Pointer to the first byte after the end of the buffer. Used for bounds checking. |
| `flags`   | Bitmask of behavior flags. Use 0 for default behavior. See Flags.                |
| `length`  | Pointer to a variable that receives the decoded value                            |

### Flags

| Flag                        | Value | Description                                          |
|-----------------------------|-------|------------------------------------------------------|
| MARIADB_LENCENC_FORBID_NULL | 1     | Treat the NULL marker (0xFB) as an error             |

## Description

Decodes a length-encoded integer from a network packet buffer. Length-encoded integers are used in the client/server protocol to prefix variable-length fields, such as column values in a text protocol result set row.

The function reads the encoded value at *packet, stores the decoded value in *length, and on success advances *packet past the bytes consumed. It never reads at or beyond end, so truncated or malformed packets are reported as errors rather than causing out-of-bounds reads.

### Length Encoding

| First byte | Meaning                                                 |
| ---------- | --------------------------------------------------------|
| 0x00–0xFA  | The value is the first byte itself (1 byte total)       |
| 0xFB       | NULL (no length; see MARIADB_LENENC_FORBID_NULL)        |
| 0xFC       | The value is stored in the next 2 bytes (3 bytes total) |
| 0xFD       | The value is stored in the next 3 bytes (4 bytes total) |
| 0xFE       | The value is stored in the next 8 bytes (9 bytes total) |
| 0xFF       | Invalid; returns MARIADB_LENENC_ERROR                   |

## Return Values

| Value	| Constant             | Meaning                                                                                        |
|-------|----------------------|------------------------------------------------------------------------------------------------|
| 0     | MARIADB_LENENC_OK    | A length was decoded successfully. *length holds the value and *packet has been advanced.      |
| 1     | MARIADB_LENENC_NULL  | The field is NULL (marker byte 0xFB). Only returned if MARIADB_LENENC_FORBID_NULL was not set. |
| 2     | MARIADB_LENENC_ERROR | The data could not be decoded. This happens when the buffer is truncated (the encoded integer would extend past end), the first byte is the invalid marker 0xFF, a NULL marker was found while MARIADB_LENENC_FORBID_NULL was set, or the value does not fit in unsigned long (verify for 8-byte values on platforms where unsigned long is 32 bits**)**. |

{% hint style="info" %}
* This function is part of the **low level protocol API** and can be used to retrieve data if a callback function was provided for fetching results from prepared statements.
* Always check the return value before using *length. A MARIADB_LENENC_NULL result means the field has no value, which is different from a value of length 0.
* The decoded length is not validated against the remaining buffer size. Callers must still check that *packet + *length <= end before reading the field contents.
{% endhint %}

## Example

The following example decodes the fields of a text protocol row, checking each length against the end of the buffer before using it.

```c
unsigned char *pos = row_data;
const unsigned char *end = row_data + row_len;
unsigned long len;
unsigned int i;

for (i = 0; i < field_count; i++)
{
  switch (mariadb_net_field_length(&pos, end, 0, &len))
  {
  case MARIADB_LENENC_OK:
    /* The length itself is not validated against the buffer */
    if (len > (unsigned long)(end - pos))
      return 1;                  /* field exceeds packet */
    process_field(pos, len);
    pos += len;
    break;
  case MARIADB_LENENC_NULL:
    process_null_field();
    break;
  case MARIADB_LENENC_ERROR:
    return 1;                    /* malformed packet */
  }
}
```

## History
mariadb_net_field_length() was added in MariaDB Connector/C 3.3.22 and 3.4.12

## See Also

* [`mysql_net_field_length()`](mysql_net_field_length.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
