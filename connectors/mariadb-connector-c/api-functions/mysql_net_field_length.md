# mysql\_net\_field\_length

## Syntax

```bnf
#include <mysql.h>

unsigned long mysql_net_field_length(unsigned char **packet)
```

## Parameter

| Parameter | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `packet`  | A pointer to a pointer to the current position in the packet buffer.  |

## Description

Returns the length of a length encoded field and increments the pointer to the beginning of the field.

## Return Value

Returns the length of the field.

{% hint style="info" %}
This function is part of the **low level protocol API** and can be used to retrieve data if a callback function was provided for fetching results from prepared statements.
{% endhint %}

## See Also

* [`mysql_net_read_packet()`](mysql_net_read_packet.md)
