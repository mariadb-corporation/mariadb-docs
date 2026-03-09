---
description: >-
  Understand server response packets in MariaDB's client/server protocol. This
  section details the various types of packets sent by the server, including OK,
  Error, and Result Set packets.
---

# 4 - Server Response Packets

For most commands which the client sends to the server, the server returns the following response packets:

{% columns %}
{% column %}
{% content-ref url="eof_packet.md" %}
[eof\_packet.md](eof_packet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Marks the end of a result set and returns status and warnings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="err_packet.md" %}
[err\_packet.md](err_packet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Indicates that an error occured.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="packet_local_infile.md" %}
[packet\_local\_infile.md](packet_local_infile.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
If the client sends a `LOAD DATA LOCAL INFILE` statement via [com\_query](https://kb-archive.mariadb.net/kb/en/com_query/), the server responds with `LOCAL_INFILE_Packet` to tell the client to send a specified file to the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ok_packet.md" %}
[ok\_packet.md](ok_packet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Sent by the server to the client. Indicates a successful completion of a command sent by the client before.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="result-set-packets.md" %}
[result-set-packets.md](result-set-packets.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The server sends multiple packets as part of a result set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="resultset-row.md" %}
[resultset-row.md](resultset-row.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Data representing a database result set unit.
{% endcolumn %}
{% endcolumns %}

