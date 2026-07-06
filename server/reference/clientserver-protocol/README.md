---
description: >-
  Understand the MariaDB client/server protocol. This section details how
  clients communicate with the server, including connection, authentication,
  query execution, and result set handling.
---

# Client/Server Protocol

## Client/Server Protocol Overview

{% columns %}
{% column %}
{% content-ref url="protocol-data-types.md" %}
[protocol-data-types.md](protocol-data-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page defines the fundamental data types used in the MariaDB client/server protocol, including integers, strings, and binary representations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-protocol-differences-with-mysql.md" %}
[mariadb-protocol-differences-with-mysql.md](mariadb-protocol-differences-with-mysql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the specific extensions and differences in the MariaDB protocol compared to MySQL, such as extended capability flags and metadata.
{% endcolumn %}
{% endcolumns %}

## Client/Server Protocol Documentation

{% columns %}
{% column %}
{% content-ref url="0-packet.md" %}
[0-packet.md](0-packet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the standard packet structure in the MariaDB protocol, including the packet header, length, sequence number, and payload handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="1-connecting/" %}
[1-connecting](1-connecting/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the connection phase in the client/server protocol. This section details how clients establish initial communication with the server, including handshaking and authentication processes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="2-text-protocol/" %}
[2-text-protocol](2-text-protocol/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the text protocol in the Server's client/server communication. This section details how SQL commands and results are exchanged as plain text, including command types and packet structures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="3-binary-protocol-prepared-statements/" %}
[3-binary-protocol-prepared-statements](3-binary-protocol-prepared-statements/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the binary protocol for prepared statements. This section details how prepared statements are exchanged efficiently between client and server, optimizing performance and security.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="4-server-response-packets/" %}
[4-server-response-packets](4-server-response-packets/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand server response packets in MariaDB's client/server protocol. This section details the various types of packets sent by the server, including OK, Error, and Result Set packets.
{% endcolumn %}
{% endcolumns %}

## Replication Protocol Documentation

{% columns %}
{% column %}
{% content-ref url="replication-protocol/" %}
[replication-protocol](replication-protocol/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the replication protocol. This section details how primary and replica servers communicate, exchanging binary log events to ensure data consistency and enable high availability.
{% endcolumn %}
{% endcolumns %}
