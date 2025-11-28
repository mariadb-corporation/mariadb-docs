---
description: >-
  The GTID_EVENT marks the start of a new transaction event group, associating
  it with a Global Transaction ID (GTID) and providing commit flags.
---

# GTID\_EVENT

For [global transaction ID](../../../ha-and-performance/standard-replication/gtid.md), used to start a new transaction event group, instead of the old `BEGIN` query event, and also to mark stand-alone (DDL).

`GTID_EVENT` event type is `162` (`0xa2`).

## Event Header

* Type\[1] = `0xa2`.
* Flags\[2] = 08 00 => `LOG_EVENT_SUPPRESS_USE_F`.

## Fields

* [uint<8>](../protocol-data-types.md#fixed-length-integers) GTID sequence.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Replication Domain ID.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) Flags.

If flag & `FL_GROUP_COMMIT_ID`:

* [uint<8>](../protocol-data-types.md#fixed-length-integers) commit\_id.

Else if flag & (`FL_PREPARED_XA` or `FL_COMPLETED_XA`):

* [uint<4>](../protocol-data-types.md#fixed-length-integers) format\_id.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) gtid\_length.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) bqual\_length.
* [byte](../protocol-data-types.md#fixed-length-bytes) xid, where n is sum of gtrid and bqual lengths.

Else:

* [uint<6>](../protocol-data-types.md#fixed-length-integers) 0.

## Flags

| Flag                  | Value | Details                                                                                                                      |
| --------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| FL\_STANDALONE        | 1     | Set when there is no terminating `COMMIT` event.                                                                             |
| FL\_GROUP\_COMMIT\_ID | 2     | Set when event group is part of a group commit on the master. Groups with same commit\_id are part of the same group commit. |
| FL\_TRANSACTIONAL     | 4     | Set for an event group that can be safely rolled back (no MyISAM, for instance).                                             |
| FL\_ALLOW\_PARALLEL   | 8     | Reflects the (negation of the) value of `@@SESSION.skip_parallel_replication` at the time of commit.                         |
| FL\_WAITED            | 16    | Set if a row lock wait (or other wait) is detected during the execution of the transaction.                                  |
| FL\_DDL               | 32    | Set for event group containing DDL.                                                                                          |
| FL\_PREPARED\_XA      | 64    | Set for XA transaction.                                                                                                      |
| FL\_COMPLETED\_XA     | 128   | XA transaction completed (committed or rolled back).                                                                         |

### Transaction Example From mysqlbinlog Utility

```sql
BEGIN
#171205 18:22:52 server id 10124  end_log_pos 652 CRC32 0x23c8d337 	GTID 0-10124-9884 trans
TBALE_MAP
#171205 18:22:52 server id 10124  end_log_pos 752 CRC32 0x52601513 	Table_map: `test`.`t4` mapped to number 92
WRITE
#171205 18:22:52 server id 10124  end_log_pos 790 CRC32 0x8869c123 	Write_rows: table id 92 flags: STMT_END_F
COMMIT
#171205 18:22:52 server id 10124  end_log_pos 821 CRC32 0x15517636 	Xid = 42004
```

### Standalone Event DDL (FLUSH TABLES) From mysqlbinlog Utility

```
#171205 17:44:27 server id 10124  end_log_pos 535 CRC32 0x309a668e 	GTID 0-10124-9883 ddl
#171205 17:44:27 server id 10124  end_log_pos 610 CRC32 0xda151470 	Query	thread_id=819	...
```

### Example GTID\_EVENT with DDL and CRC32

```
eb cc 26 5a a2 8c 27 00  00 2a 00 00 00 17 02 00  ...&Z..'..*.....
00 08 00 9b 26 00 00 00  00 00 00 00 00 00 00 29  ...&..........).
00 00 00 00 00 00 8e 66  9a 30                    ......f.0.
```

#### **Content**

* GTID seq\[8] = 9b 26 00 00 00 00 00 00 => 9883.
* domain id\[4] = 00 00 00 00 00 => 0.
* flags\[1] = 29 => 41 (`FL_DDL` =32 + `FL_ALLOW_PARALLEL`=8 + `FL_STANDALONE`=1).
* commit\_id\[6] = 00 00 00 00 00 00 = 0.
* CRC32\[4] = 8e 66 9a 30.

### Example GTID\_EVENT With a Transaction and CRC32

```
ec d5 26 5a a2 8c 27 00  00 2a 00 00 00 8c 02 00 ..&Z..'..*......
00 08 00 9c 26 00 00 00  00 00 00 00 00 00 00 0c ....&...........
00 00 00 00 00 00 37 d3  c8 23                   ......7..#
```

#### **Content**

* GTID seq\[8] = 9c 26 00 00 00 00 00 00 => 9884.
* domain id\[4] = 00 00 00 00 00 => 0.
* flags\[1] = 0c => 12 (`FL_ALLOW_PARALLEL`=8 + `FL_TRANSACTIONAL`=4).
* commit\_id\[6] = 00 00 00 00 00 00 = 0.
* CRC32\[4] = 37 d3 c8 23.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
