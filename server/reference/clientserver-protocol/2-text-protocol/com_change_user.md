# COM\_CHANGE\_USER

`COM_CHANGE_USER` resets the connection and re-authenticates with the given credentials. The packet is identical to the authentication packet in the connection handshake.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0x11` : `COM_CHANGE_USER` header.
* [string<nul>](../protocol-data-types.md#null-terminated-strings) username.
* If (`server_capabilities` & `CLIENT_SECURE_CONNECTION`):
  * [int<1>](../protocol-data-types.md#fixed-length-integers) length of authentication response.
  * string authentication response.
* Else:
  * [string<nul>](../protocol-data-types.md#null-terminated-strings) authentication response.
* [string<nul>](../protocol-data-types.md#null-terminated-strings) default schema name.
* [int<2>](../protocol-data-types.md#fixed-length-integers) client character collation.
* If (`server_capabilities` & `CLIENT_PLUGIN_AUTH`):
  * [string<nul>](../protocol-data-types.md#null-terminated-strings) authentication plugin name.
* If (`server_capabilities` & `CLIENT_CONNECT_ATTRS`):
  * [int](../protocol-data-types.md#length-encoded-integers) size of connection attributes.
  * Loop:
    * [string<len>](../protocol-data-types.md#length-encoded-strings) key.
    * [string<len>](../protocol-data-types.md#length-encoded-strings) value.

## Response

Server response is like [connection authentication](../1-connecting/connection.md) :

* An `OK` packet in case of success [OK\_Packet](../4-server-response-packets/ok_packet.md).
* An error packet in case of error [ERR\_Packet](../4-server-response-packets/err_packet.md).
* Authentication switch:
  * If the client or server doesn't have `PLUGIN_AUTH` capability:
    * Server sends `0xFE` byte.
    * Client sends `old_password`.
  * Else:
    * Server sends [Authentication switch request](com_change_user.md#authentication-switch-request).
    * Client may have many exchanges with the server according to the [Plugin](com_change_user.md#plugin-list).
  * Authentication switch ends with server sending either [OK\_Packet](../4-server-response-packets/ok_packet.md) or [ERR\_Packet](../4-server-response-packets/err_packet.md).

If the authentication fails more than three times, all future `COM_CHANGE_USER` commands on the connection will return the `#08S01 Unknown command` error. This is an anti-brute-force mechanism designed to prevent rapid guessing of passwords.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
