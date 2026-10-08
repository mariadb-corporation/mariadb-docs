---
description: >-
  The STOP_EVENT is written to the binary log when the server shuts down,
  serving as a marker for a clean stop.
---

# STOP\_EVENT

The master server writes the event to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) when it shuts down, or when resuming after a mariadbd process crash.

A new binary log file is always created, but there is no `ROTATE_EVENT`.

`STOP_EVENT` is the last written event after a clean shutdown, or when resuming after a crash.

{% hint style="warning" %}
This event is never sent to replica servers.
{% endhint %}

## Header

* Event header with EventType set to `STOP_EVENT` (`0x03`).
* Event header NextPos set to `EOF` .
* No special flags added.

## Fields

* The event has no data.

## Example With CRC32 (Last 4 Bytes)

Event size = header\[19] + 0 bytes data + 4 CRC32 = 23.

```
3a b8 15 5a 03 01 00 00  00 17 00 00 00 09 0c 00  ..Z............
00 00 00 4e 99 ee 2c                              ...N..,
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
