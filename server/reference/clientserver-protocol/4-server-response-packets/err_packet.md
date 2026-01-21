---
description: >-
  The ERR_Packet is sent by the server to report an error, containing a numeric
  error code, SQL state marker, and a human-readable error message.
---

# ERR\_Packet

`ERR_Packet` indicates that an error occurred.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `ERR_Packet` header = `0xFF`.
* [int<2>](../protocol-data-types.md#fixed-length-integers) error code. see [error list](../../error-codes/mariadb-error-code-reference.md).
* If (error code == `0xFFFF`) /\* progress reporting \*/:
  * [int<1>](../protocol-data-types.md#fixed-length-integers) stage.
  * [int<1>](../protocol-data-types.md#fixed-length-integers) max\_stage.
  * [int<3>](../protocol-data-types.md#fixed-length-integers) progress.
  * [string](../protocol-data-types.md#length-encoded-strings) progress\_info.
* Else:
  * If (next byte = '#'):
    * [string<1>](../protocol-data-types.md#fixed-length-strings) sql state marker '#'.
    * [string<5>](../protocol-data-types.md#fixed-length-strings) sql state.
    * [string](../protocol-data-types.md#fixed-length-strings) human-readable error message.
  * Else:
    * [string](../protocol-data-types.md#fixed-length-strings) human-readable error message.

{% hint style="warning" %}
Note that the `ERR_Packet` is supposed to send a server error to the client. In particular, all error codes in the range 2000 to 2999 and 5000 to 5999 (inclusive) are reserved for client errors and an ERR packet with such an error code will be considered malformed.
{% endhint %}

## See also

["Progress reporting"](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/KgSCnuNXCMSK6rHfTpO5)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
