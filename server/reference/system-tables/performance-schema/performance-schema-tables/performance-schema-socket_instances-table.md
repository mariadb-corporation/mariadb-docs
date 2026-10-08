---
description: >-
  The socket_instances table lists active network socket connections, providing
  details such as the IP address, port, and state of each socket.
---

# Performance Schema socket\_instances Table

The `socket_instances` table lists active server connections, with each record being a Unix socket file or TCP/IP connection.

The `socket_instances` table contains the following columns:

| Column                  | Description                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| EVENT\_NAME             | NAME from the setup\_instruments table, and the name of the wait/io/socket/\* instrument that produced the event.                   |
| OBJECT\_INSTANCE\_BEGIN | Memory address of the object.                                                                                                       |
| THREAD\_ID              | Thread identifier that the server assigns to each socket.                                                                           |
| SOCKET\_ID              | The socket's internal file handle.                                                                                                  |
| IP                      | Client IP address. Blank for Unix socket file, otherwise an IPv4 or IPv6 address. Together with the PORT identifies the connection. |
| PORT                    | TCP/IP port number, from 0 to 65535. Together with the IP identifies the connection.                                                |
| STATE                   | Socket status, either IDLE if waiting to receive a request from a client, or ACTIVE                                                 |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
