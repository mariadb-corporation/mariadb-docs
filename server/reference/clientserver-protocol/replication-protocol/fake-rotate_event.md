---
description: >-
  An artificial event sent to the replica to indicate the name of the binary log
  file on the master, ensuring the replica knows which file is being read.
---

# Fake ROTATE\_EVENT

When a slave server connects to a MariaDB master server, the first binlog event sent is Fake `ROTATE_EVENT`. This event is similar to [ROTATE\_EVENT](rotate_event.md), but it's artificial and its purpose is to tell the replica server which the binlog file name of the master is.

This matters when the replica connects with the GTID option (no filename is given) or when using file and pos with empty file name (usually file='' and pos = 4).

The Event Type is `ROTATE_EVENT` (`0x4`).

{% hint style="info" %}
The fake `ROTATE_EVENT` event is not written in the binlog file. It's created by the master and sent to newly connected replica before [FORMAT\_DESCRIPTION\_EVENT](format_description_event.md)
{% endhint %}

## Header

* Timestamp set to `0`.
* Event Tye is `ROTATE_EVENT`.
* Next Pos is set to `0`.
* Flags are set to `LOG_ARTIFICIAL_F` (`0x20`).

## Content

The content is the same as [ROTATE\_EVENT](rotate_event.md).

* pos = the requested pos from slave, usually `4`.
* filename = the master binlog filename.

If it is the first fake rotate event, and the global server variable `@@binlog_checksum` is set to `CRC32`:

* crc32\_checksum (4 Bytes).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
