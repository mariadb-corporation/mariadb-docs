# mysql\_net\_read\_packet

## Syntax

```bnf
#include <mysql.h>

ulong mysql_net_read_packet(MYSQL *mysql)
```

## Parameter

| Parameter | Description                                                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `mysql`   | A connection handle previously allocated by [mysql\_init()](mysql_init.md) and connected by [mysql\_real\_connect()](mysql_real_connect.md).  |

## Description

`mysql_net_read_packet` reads the next protocol packet from the server into the connection's internal network buffer.

## Return Value

Returns the length of the received packet.

{% hint style="info" %}
This function is part of the low level protocol API.
{% endhint %}

## See also

* [`mysql_net_field_length()`](mysql_net_field_length.md)
