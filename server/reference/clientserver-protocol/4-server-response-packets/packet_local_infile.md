---
description: >-
  The LOCAL_INFILE_Packet is sent by the server to request a file from the
  client during the execution of a LOAD DATA LOCAL INFILE statement.
---

# LOCAL\_INFILE\_Packet

If the client sends a `LOAD DATA LOCAL INFILE` statement via [com\_query](../2-text-protocol/com_query.md), the server responds with `LOCAL_INFILE_Packet` to tell the client to send a specified file to the server.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) `0xFB` : `LOCAL_INFILE` header.
* [string](../protocol-data-types.md#end-of-file-length-strings) filename.

## Client Response

The client sends the file as the packet body. If the file is large, the contents are sent in multiple separate packets. After the file is sent, the client must send an empty packet to indicate that no more data will follow.

Once the client has finished sending the file, the server will respond with an [OK\_packet](ok_packet.md) or an [ERR\_packet](err_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
