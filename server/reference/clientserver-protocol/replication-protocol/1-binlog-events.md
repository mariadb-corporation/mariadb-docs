---
description: >-
  This section provides an overview of the various events recorded in the binary
  log, which are the core units of replication data transmission.
---

# 1-Binlog Events

Binary log events, or binlog events, are information about data modification made to a MariaDB server instance stored in the [binary log](../../../server-management/server-monitoring-logs/binary-log/) files.

## Log File Structure

Each log file contains:

* A 4-byte magic number, followed by a series of events describing data modifications:\
  The magic number bytes are `0xfe` `0x62` `0x69` `0x6e` = `0xfe 'b''i''n'` (this is the `BINLOG_MAGIC` constant).
* A series of binlog events.

## Event Content

Each event contains the 'header' followed by 'data bytes':

The header bytes provide information about:

* The event type;
* The creation time;
* Which server created the event;
* Flags and so forth.

The data bytes provide information specific to the type of event.

{% hint style="info" %}
The first event, [FORMAT\_DESCRIPTION\_EVENT](format_description_event.md) at 'position' 4, is a descriptor event that describes the format used to write events in the file.
{% endhint %}

The remaining events are interpreted according to the version.

The final event is usually a log-rotation event [ROTATE\_EVENT](rotate_event.md) that specifies the next binary log filename or a [STOP\_EVENT](stop_event.md) written during server shutdown.

**Note**: in case of a server crash there is no terminating event (no `ROTATE` nor `STOP`).

## Example Binlog File (Hexdump -C $file\_name)

```
fe 62 69 6e a4 85 9e 59  0f 8c 27 00 00 f5 00 00  |.bin...Y..'.....|
00 f9 00 00 00 00 00 04  00 31 30 2e 31 2e 32 34  |.........10.1.24|
2d 4d 61 72 69 61 44 42  00 6c 6f 67 00 00 00 00  |-MariaDB.log....|
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00 00 00 00 00 00 00 00  00 00 00 a4 85 9e 59 13  |..............Y.|
38 0d 00 08 00 12 00 04  04 04 04 12 00 00 dd 00  |8...............|
04 1a 08 00 00 00 08 08  08 02 00 00 00 0a 0a 0a  |................|
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
04 13 04 00 01 ab 5b a2  e0 a4 85 9e 59 a3 8c 27  |......[.....Y..'|
00 00 2b 00 00 00 24 01  00 00 00 00 01 00 00 00  |..+...$.........|
00 00 00 00 8c 27 00 00  00 0e 00 00 00 00 00 00  |.....'..........|
...
...
```

## Example From [mysqlbinlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/)

```sql
DELIMITER /*!*/;
# at 4
#170824  9:52:04 server id 10124  end_log_pos 249 CRC32 0xe0a25bab 	Start: binlog v 4, server v 10.1.24-MariaDB created 170824  9:52:04 at startup
ROLLBACK/*!*/;
BINLOG '
pIWeWQ+MJwAA9QAAAPkAAAAAAAQAMTAuMS4yNC1NYXJpYURCAGxvZwAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAACkhZ5ZEzgNAAgAEgAEBAQEEgAA3QAEGggAAAAICAgCAAAACgoKAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAEEwQAAatbouA=
'/*!*/;
# at 249
#170824  9:52:04 server id 10124  end_log_pos 292 CRC32 0xb6d8f0a8 	Gtid list [0-10124-3584]
# at 292
#170824  9:52:04 server id 10124  end_log_pos 334 CRC32 0xf2dc685f 	Binlog checkpoint log-bin.000011
# at 334
#170824  9:52:13 server id 10124  end_log_pos 376 CRC32 0xe958a0ae 	GTID 0-10124-3585 trans
...
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
