# COM\_INIT\_DB

`COM_INIT_DB` is used to specify the default schema for the connection.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x02` : `COM_INIT_DB` Header.
* [string<nul>](../protocol-data-types.md#null-terminated-strings) schema name.

## Response

[ERR\_Packet](../4-server-response-packets/err_packet.md) or [OK\_Packet](../4-server-response-packets/ok_packet.md).

## Example

```
06 00 00 00 02 74 65 73 74 63                    .....testc
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
