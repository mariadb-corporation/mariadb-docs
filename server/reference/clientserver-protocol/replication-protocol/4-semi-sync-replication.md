---
description: >-
  Explains the handshake and acknowledgement process for semi-synchronous
  replication, ensuring data is committed on at least one replica.
---

# 4-Semi-Sync Replication

[Regular MariaDB replication](../../../ha-and-performance/standard-replication/) is asynchronous. MariaDB also includes [semisynchronous replication](../../../ha-and-performance/standard-replication/semisynchronous-replication.md) semi-synchronous Binlog Event.

## Event Header Changes

If the user variable `@rpl_semi_sync_slave` is set, 2 extra bytes are added after the status byte of a [binlog network stream](3-binlog-network-stream.md) and before the normal binlog event header.

* [uint<1>](../protocol-data-types.md#fixed-length-integers) semi-sync indicator, always `0xef`.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) semi-sync flags, either `0x00` (no `ACK`) or `0x01` (`ACK`).

**Note** : The packet size, as in the network protocol header, is then: `event_size + 1 byte status + 2 bytes semi-sync replication`.

The MariaDB server sets the user variable whenever it is starting replication. For MariaDB Connector/C , the following query must be executed before the call to `mariadb_rpl_open()` is made to enable semi-sync replication.

```sql
SET @rpl_semi_sync_slave=1
```

If the semi-sync flag is set to `0x01`, the master waits for a Semi Sync `ACK` packet from the slave and when the Semi Sync `ACK` is seen, the master acknowledges the client which has issued the transaction with a standard `OK_Packet` or a `ERR_Packet`.

The master can then write the transaction to the binary log and send the next events to the replica.

**Note** : The master only requests Semi Sync ACKs if [rpl\_semi\_sync\_master\_enabled](../../../ha-and-performance/standard-replication/semisynchronous-replication.md#rpl_semi_sync_master_enabled) is enabled. If it is not enabled, the semi-sync flag will always be `0x00`.

## Semi Sync ACK Details

This event is sent by the replica **only if** the semi-sync flag is set to `0x01`.

* [uint<1>](../protocol-data-types.md#fixed-length-integers) semi-sync indicator, always 0xef;
* [uint<8>](../protocol-data-types.md#fixed-length-integers) the next position of received event;
* [string](../protocol-data-types.md#fixed-length-integers) binlog file name.

{% hint style="info" %}
This packet sent by the replica never includes the `CRC32`.
{% endhint %}

Sending an `ACK` when the semi-sync flag is set to `0x0` causes an error, and the connection is closed.

## Example of Heartbeat Event With Semi-Sync Protocol and CRC32

We can see:

* 2a 00 00 \[3 bytes] packet size.
* 06 \[1] sequence.
* 00 \[1] status byte = 00 => OK.
* ef 00 \[2] bytes => semi sync indicator (0xef) and semi-sync flag (00).
* The ef 00 2 bytes after the OK byte 00.

```
T 127.0.0.1:23240 -> 127.0.0.1:41054 [AP]
  2a 00 00 06 00 ef 00 00    00 00 00 1b d9 27 00 00    *............'..
  27 00 00 00 79 04 00 00    00 00 6d 79 73 71 6c 2d    '...y.....mysql-
  62 69 6e 2e 30 30 30 30    33 34 ed ef e1 f0          bin.000034....
```

## Example of XID\_EVENT, With CRC32

The master sets the Semi-Sync `ACK` request in the `XID_EVENT` event:

We see the 2 semi sync bytes: **ef** and **01**. The latter, being 1, means the replica server must send the Semi Sync `ACK` packet.

We also see in the binlog event header:

* Event Type \[1] = 10 `XID_EVENT`.
* Next Event pos \[4] = 4a 05 00 00 => 1354.

```
22 00 00 0c 00 ef 01 17  d0 37 5a 17 d0 37 5a 10  "............7Z.
d9 27 00 00 1f 00 00 00  4a 05 00 00 00 00 6f 00  .?......J.....o.
00 00 00 00 00 00 44 30  aa fc                    ......D0..
```

## Example of Semi-Sync ACK

This is sent by the replica server after the `XID_EVENT` receiving.

We see:

* The semi sync indicator \[1] = 0xef, sent before anything else.
* The Next Event position \[8] = 4a 05 00 00 00 00 00 00 => 1354\
  which is the next position of the XID\_EVENT above.
* The binlog filename = mysql-bin.000034.

Please note:

* There is no terminating `CRC32`.
* The packet sequence now start starts from 0.

```
19 00 00 00 ef 4a 05 00    00 00 00 00 00 6d 79 73    .....J.......mys
  71 6c 2d 62 69 6e 2e 30    30 30 30 33 34             ql-bin.000034
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
