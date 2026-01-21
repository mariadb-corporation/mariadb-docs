---
description: >-
  Logged during binlog rotation or checkpoints, this event lists the GTIDs
  present in the binary log to help replicas determine their replication state.
---

# GTID\_LIST\_EVENT

Logged in every binlog to record the current [replication](../../../ha-and-performance/standard-replication/) state. Consists of the last [GTID](../../../ha-and-performance/standard-replication/gtid.md) seen for each replication domain.

The Global Transaction ID, [GTID](../../../ha-and-performance/standard-replication/gtid.md) for short, consists of three components:

* Replication domain ID;
* Master server ID;
* Sequence ID.

It's represented as three numbers separated with dashes (`-`); for example: `1-1222-1011` .

It's usually written after the [Format Description Event](format_description_event.md). If binary log encryption is enabled, it is written after the [Start Encryption Event](start_encryption_event.md).

{% hint style="info" %}
In case of encrypted binlog files ([encrypt\_binlog](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is set to `ON`), this event is written just after the [START\_ENCRYPTION\_EVENT](start_encryption_event.md).
{% endhint %}

## Header

* Event type is 163 (0xa3).

## Fields

* [uint<4>](../protocol-data-types.md#fixed-length-integers) Number of GTIDs.
* For (i=0; i < gtid\_count; i++):
  * [uint<4>](../protocol-data-types.md#fixed-length-integers) Replication Domain ID.
  * [uint<4>](../protocol-data-types.md#fixed-length-integers) Server\_ID.
  * [uint<8>](../protocol-data-types.md#fixed-length-integers) GTID sequence.

The minimum content size for one GTID is `4 + (4 + 4 + 8) * 1 = 20 bytes` .

## Example With 1 GTID, With CRC32

From the [mysqlbinlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) utility:

170824 9:52:04 server id 10124 end\_log\_pos 292 CRC32 **0xb6d8f0a8** Gtid list **\[0-10124-3584]**

```
a4 85 9e 59 a3 8c 27 00  00 2b 00 00 00 24 01 00  ...Y..'..+...$..
00 00 00 01 00 00 00 00  00 00 00 8c 27 00 00 00  ............'...
0e 00 00 00 00 00 00 a8  f0 d8 b6                 ..........
```

### Header, 19 Bytes

* Event Time = a4 85 9e 59 ===> 2017-08-24 9:52:04.
* Event Type = a3 => 163.
* Server\_id = 8c 27 00 00 => 00 00 27 8c => 10124.
* Event Size = 2b => 43 (header\[19] + 1 GTID(20 bytes) + CRC32\[4].
* Next Pos = 24 01 00 00 => 00 00 01 24 => 292.
* Flags = 00 => 0.

### Content, Variable Size, is (4 + (4 + 4 + 8 ) \* n\_GTIDs) Bytes

The content example with one GTID is 20 bytes + 4 bytes CRC32:

* Number of GTIDs\[4] = 01 00 00 00 => 1.
* GTID\[0] replication\_domain\[4] = 00 00 00 00 => 0.
* GTID\[0] Server\_id\[4] = 8c 27 00 00 => 00 00 27 8c => 10124.
* GTID\[0] Sequence\[8] = 00 0e 00 00 00 00 00 00 ===> 3584.
* crc32\[4] = a8 f0 d8 b6 => b6 d8 f0 a8 => 0xb6d8f0a8.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
