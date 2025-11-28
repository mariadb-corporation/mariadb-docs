---
description: >-
  Details the initialization phase where a replica connects to the primary,
  authenticates, sends capabilities, and registers for updates.
---

# 5-Replica Registration

## Overview

The replica server, when properly configured with `CHANGE MASTER TO ...` , can start MariaDB replication with the [START REPLICA](../../sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement.

After authentication, some [COM\_QUERY](../2-text-protocol/com_query.md) packets are exchanged before sending [COM\_REGISTER\_SLAVE](com_register_slave.md) and [COM\_BINLOG\_DUMP](com_binlog_dump.md).

The following `COM_QUERY` packets come from MariaDB 10.X replicas using [GTID](../../../ha-and-performance/standard-replication/gtid.md):

* `SELECT UNIX_TIMESTAMP()`;
* `SHOW VARIABLES LIKE 'SERVER_ID'`;
* `SET @master_heartbeat_period`= 30000001024;
* `SET @master_binlog_checksum`= `@@global.binlog_checksum`;
* `SELECT @master_binlog_checksum`;
* `SET @mariadb_slave_capability`=4;
* `SELECT @@GLOBAL.gtid_domain_id GTID` registration: domain ID;
* `SET @slave_connect_state`='0-10201-9868' GTID registration: the requested GTID;
* `SET @slave_gtid_strict_mode`=0 GTID registration: strict\_mode;
* `SET @slave_gtid_ignore_duplicates`=0 GTID registration: ignore\_duplicates.

Then `COM_REGISTER_SLAVE` completes the registration.

The `COM_BINLOG_DUMP` marks the request of binlog events stream.

{% hint style="info" %}
If semi-sync is in use, the request for the network protocol change is sent between `COM_REGISTER_SLAVE` and `COM_BINLOG_DUMP`.
{% endhint %}

## Example Using 'ngrep'

[COM\_REGISTER\_SLAVE](com_register_slave.md), [Semi-Sync](4-semi-sync-replication.md) and [COM\_BINLOG\_DUMP](com_binlog_dump.md):

```
T 127.0.0.1:42158 -> 127.0.0.1:23240 [AP]
  1a 00 00 00 15 75 27 00    00 08 53 42 73 6c 61 76    .....u'...SBslav
  65 31 00 00 c9 5a 00 00    00 00 00 00 00 00          e1...Z........  

T 127.0.0.1:23240 -> 127.0.0.1:42158 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42158 -> 127.0.0.1:23240 [AP]
  33 00 00 00 03 53 48 4f    57 20 56 41 52 49 41 42    3....SHOW VARIAB
  4c 45 53 20 4c 49 4b 45    20 27 72 70 6c 5f 73 65    LES LIKE 'rpl_se
  6d 69 5f 73 79 6e 63 5f    6d 61 73 74 65 72 5f 65    mi_sync_master_e
  6e 61 62 6c 65 64 27                                  nabled'         

T 127.0.0.1:23240 -> 127.0.0.1:42158 [AP]
  01 00 00 01 02 64 00 00    02 03 64 65 66 12 69 6e    .....d....def.in
  66 6f 72 6d 61 74 69 6f    6e 5f 73 63 68 65 6d 61    formation_schema
  11 53 45 53 53 49 4f 4e    5f 56 41 52 49 41 42 4c    .SESSION_VARIABL
  45 53 11 53 45 53 53 49    4f 4e 5f 56 41 52 49 41    ES.SESSION_VARIA
  42 4c 45 53 0d 56 61 72    69 61 62 6c 65 5f 6e 61    BLES.Variable_na
  6d 65 0d 56 41 52 49 41    42 4c 45 5f 4e 41 4d 45    me.VARIABLE_NAME
  0c 08 00 40 00 00 00 fd    01 00 00 00 00 5d 00 00    ...@.........]..
  03 03 64 65 66 12 69 6e    66 6f 72 6d 61 74 69 6f    ..def.informatio
  6e 5f 73 63 68 65 6d 61    11 53 45 53 53 49 4f 4e    n_schema.SESSION
  5f 56 41 52 49 41 42 4c    45 53 11 53 45 53 53 49    _VARIABLES.SESSI
  4f 4e 5f 56 41 52 49 41    42 4c 45 53 05 56 61 6c    ON_VARIABLES.Val
  75 65 0e 56 41 52 49 41    42 4c 45 5f 56 41 4c 55    ue.VARIABLE_VALU
  45 0c 08 00 00 08 00 00    fd 01 00 00 00 00 05 00    E...............
  00 04 fe 00 00 22 00 20    00 00 05 1c 72 70 6c 5f    .....". ....rpl_
  73 65 6d 69 5f 73 79 6e    63 5f 6d 61 73 74 65 72    semi_sync_master
  5f 65 6e 61 62 6c 65 64    02 4f 4e 05 00 00 06 fe    _enabled.ON.....
  00 00 22 00                                           ..". 

T 127.0.0.1:42158 -> 127.0.0.1:23240 [AP]
  1c 00 00 00 03 53 45 54    20 40 72 70 6c 5f 73 65    .....SET @rpl_se
  6d 69 5f 73 79 6e 63 5f    73 6c 61 76 65 3d 20 31    mi_sync_slave= 1

T 127.0.0.1:23240 -> 127.0.0.1:42158 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42158 -> 127.0.0.1:23240 [AP]
  1b 00 00 00 12 34 06 00    00 02 00 75 27 00 00 6d    .....4.....u'..m
  79 73 71 6c 2d 62 69 6e    2e 30 30 30 30 33 34       ysql-bin.000034
```

In the example, we see that these two `COM_QUERY` commands are sent just after `COM_REGISTER_SLAVE` and before `COM_BINLOG_DUMP`:

* `SHOW VARIABLES LIKE` 'rpl\_semi\_sync\_master\_enabled';
* `SET @rpl_semi_sync_slave`= 1.

## Complete Example with GTID Registration

The example shows output up to `COM_BINLOG_DUMP` request, No Semi-Sync:

```
T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  5d 00 00 00 0a 35 2e 35    2e 35 2d 31 30 2e 32 2e    ]....5.5.5-10.2.
  31 30 2d 4d 61 72 69 61    44 42 2d 6c 6f 67 00 22    10-MariaDB-log."
  00 00 00 7d 2e 6a 4f 2c    2c 36 6a 00 fe f7 08 02    ...}.jO,,6j.....
  00 bf 81 15 00 00 00 00    00 00 07 00 00 00 38 74    ..............8t
  60 64 54 59 44 28 38 24    48 7c 00 6d 79 73 71 6c    `dTYD(8$H|.mysql
  5f 6e 61 74 69 76 65 5f    70 61 73 73 77 6f 72 64    _native_password
  00                                                    .               

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  a9 00 00 01 05 a2 38 80    70 03 00 40 08 00 00 00    ......8.p..@....
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 6d 73 61 6e    64 62 6f 78 00 14 52 42    ....msandbox..RB
  0b e8 ae 56 ec ff ef 1f    1f 14 51 1d 4a 47 f4 32    ...V......Q.JG.2
  56 74 6d 79 73 71 6c 5f    6e 61 74 69 76 65 5f 70    Vtmysql_native_p
  61 73 73 77 6f 72 64 00    54 03 5f 6f 73 05 4c 69    assword.T._os.Li
  6e 75 78 0c 5f 63 6c 69    65 6e 74 5f 6e 61 6d 65    nux._client_name
  08 6c 69 62 6d 79 73 71    6c 04 5f 70 69 64 05 33    .libmysql._pid.3
  30 30 31 33 0f 5f 63 6c    69 65 6e 74 5f 76 65 72    0013._client_ver
  73 69 6f 6e 07 31 30 2e    32 2e 31 30 09 5f 70 6c    sion.10.2.10._pl
  61 74 66 6f 72 6d 06 78    38 36 5f 36 34             atform.x86_64   

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 02 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  18 00 00 00 03 53 45 4c    45 43 54 20 55 4e 49 58    .....SELECT UNIX
  5f 54 49 4d 45 53 54 41    4d 50 28 29                _TIMESTAMP()    

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  01 00 00 01 01 26 00 00    02 03 64 65 66 00 00 00    .....&....def...
  10 55 4e 49 58 5f 54 49    4d 45 53 54 41 4d 50 28    .UNIX_TIMESTAMP(
  29 00 0c 3f 00 11 00 00    00 08 80 00 00 00 00 05    )..?............
  00 00 03 fe 00 00 02 00    0b 00 00 04 0a 31 35 31    .............151
  33 36 38 34 33 38 36 05    00 00 05 fe 00 00 02 00    3684386.........

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  20 00 00 00 03 53 48 4f    57 20 56 41 52 49 41 42     ....SHOW VARIAB
  4c 45 53 20 4c 49 4b 45    20 27 53 45 52 56 45 52    LES LIKE 'SERVER
  5f 49 44 27                                           _ID'            

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  01 00 00 01 02 64 00 00    02 03 64 65 66 12 69 6e    .....d....def.in
  66 6f 72 6d 61 74 69 6f    6e 5f 73 63 68 65 6d 61    formation_schema
  11 53 45 53 53 49 4f 4e    5f 56 41 52 49 41 42 4c    .SESSION_VARIABL
  45 53 11 53 45 53 53 49    4f 4e 5f 56 41 52 49 41    ES.SESSION_VARIA
  42 4c 45 53 0d 56 61 72    69 61 62 6c 65 5f 6e 61    BLES.Variable_na
  6d 65 0d 56 41 52 49 41    42 4c 45 5f 4e 41 4d 45    me.VARIABLE_NAME
  0c 08 00 40 00 00 00 fd    01 00 00 00 00 5d 00 00    ...@.........]..
  03 03 64 65 66 12 69 6e    66 6f 72 6d 61 74 69 6f    ..def.informatio
  6e 5f 73 63 68 65 6d 61    11 53 45 53 53 49 4f 4e    n_schema.SESSION
  5f 56 41 52 49 41 42 4c    45 53 11 53 45 53 53 49    _VARIABLES.SESSI
  4f 4e 5f 56 41 52 49 41    42 4c 45 53 05 56 61 6c    ON_VARIABLES.Val
  75 65 0e 56 41 52 49 41    42 4c 45 5f 56 41 4c 55    ue.VARIABLE_VALU
  45 0c 08 00 00 08 00 00    fd 01 00 00 00 00 05 00    E...............
  00 04 fe 00 00 22 00 10    00 00 05 09 73 65 72 76    ....."......serv
  65 72 5f 69 64 05 31 30    32 30 31 05 00 00 06 fe    er_id.10201.....
  00 00 22 00                                           ..".            

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  2a 00 00 00 03 53 45 54    20 40 6d 61 73 74 65 72    *....SET @master
  5f 68 65 61 72 74 62 65    61 74 5f 70 65 72 69 6f    _heartbeat_perio
  64 3d 20 33 30 30 30 30    30 30 31 30 32 34          d= 30000001024  

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  36 00 00 00 03 53 45 54    20 40 6d 61 73 74 65 72    6....SET @master
  5f 62 69 6e 6c 6f 67 5f    63 68 65 63 6b 73 75 6d    _binlog_checksum
  3d 20 40 40 67 6c 6f 62    61 6c 2e 62 69 6e 6c 6f    = @@global.binlo
  67 5f 63 68 65 63 6b 73    75 6d                      g_checksum      

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  1f 00 00 00 03 53 45 4c    45 43 54 20 40 6d 61 73    .....SELECT @mas
  74 65 72 5f 62 69 6e 6c    6f 67 5f 63 68 65 63 6b    ter_binlog_check
  73 75 6d                                              sum             

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  01 00 00 01 01 2d 00 00    02 03 64 65 66 00 00 00    .....-....def...
  17 40 6d 61 73 74 65 72    5f 62 69 6e 6c 6f 67 5f    .@master_binlog_
  63 68 65 63 6b 73 75 6d    00 0c 08 00 ff ff ff 00    checksum........
  fa 00 00 27 00 00 05 00    00 03 fe 00 00 02 00 06    ...'............
  00 00 04 05 43 52 43 33    32 05 00 00 05 fe 00 00    ....CRC32.......
  02 00                                                 ..              

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  20 00 00 00 03 53 45 54    20 40 6d 61 72 69 61 64     ....SET @mariad
  62 5f 73 6c 61 76 65 5f    63 61 70 61 62 69 6c 69    b_slave_capabili
  74 79 3d 34                                           ty=4            

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  1f 00 00 00 03 53 45 4c    45 43 54 20 40 40 47 4c    .....SELECT @@GL
  4f 42 41 4c 2e 67 74 69    64 5f 64 6f 6d 61 69 6e    OBAL.gtid_domain
  5f 69 64                                              _id             

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  01 00 00 01 01 2d 00 00    02 03 64 65 66 00 00 00    .....-....def...
  17 40 40 47 4c 4f 42 41    4c 2e 67 74 69 64 5f 64    .@@GLOBAL.gtid_d
  6f 6d 61 69 6e 5f 69 64    00 0c 3f 00 15 00 00 00    omain_id..?.....
  08 a0 00 00 00 00 05 00    00 03 fe 00 00 02 00 02    ................
  00 00 04 01 30 05 00 00    05 fe 00 00 02 00          ....0.........  

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  28 00 00 00 03 53 45 54    20 40 73 6c 61 76 65 5f    (....SET @slave_
  63 6f 6e 6e 65 63 74 5f    73 74 61 74 65 3d 27 30    connect_state='0
  2d 31 30 32 30 31 2d 39    38 36 38 27                -10201-9868'    

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  1e 00 00 00 03 53 45 54    20 40 73 6c 61 76 65 5f    .....SET @slave_
  67 74 69 64 5f 73 74 72    69 63 74 5f 6d 6f 64 65    gtid_strict_mode
  3d 30                                                 =0              

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  24 00 00 00 03 53 45 54    20 40 73 6c 61 76 65 5f    $....SET @slave_
  67 74 69 64 5f 69 67 6e    6f 72 65 5f 64 75 70 6c    gtid_ignore_dupl
  69 63 61 74 65 73 3d 30                               icates=0        

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  1b 00 00 00 15 75 27 00    00 09 73 6c 61 76 65 5f    .....u'...slave_
  6e 5f 31 00 00 c9 5a 00    00 00 00 00 00 00 00       n_1...Z........ 

T 127.0.0.1:23240 -> 127.0.0.1:42367 [AP]
  07 00 00 01 00 00 00 02    00 00 00                   ...........     

T 127.0.0.1:42367 -> 127.0.0.1:23240 [AP]
  1b 00 00 00 12 34 06 00    00 02 00 75 27 00 00 6d    .....4.....u'..m
  79 73 71 6c 2d 62 69 6e    2e 30 30 30 30 33 34       ysql-bin.000034
```

## Events Transmission After COM\_BINLOG\_DUMP

The MariaDB master always sends this, after the `COM_BINLOG_DUMP`:

* [FAKE\_ROTATE\_EVENT](fake-rotate_event.md);
* [FORMAT\_DESCRIPTION\_EVENT](format_description_event.md): Next Pos in the header is set to 0 if not requesting binlog file from the beginning, and the GTID is not in use; otherwise, Next Pos is related to next event after FDE.
* [FAKE\_GTID\_LIST\_EVENT](fake-gtid_list-event.md) with latest GTID information.

After those first events, the master sends events related to changes in database to the connected replica binlog. The replica is just waiting for new events from master.

## Complete Example of Event Transmission With CRC32

```
T 127.0.0.1:23240 -> 127.0.0.1:42219 [AP]
  30 00 00 01 00 00 00 00    00 04 d9 27 00 00 2f 00    0..........'../.
  00 00 00 00 00 00 20 00    04 00 00 00 00 00 00 00    ...... .........
  6d 79 73 71 6c 2d 62 69    6e 2e 30 30 30 30 33 34    mysql-bin.000034
  d5 3f ea d7 fd 00 00 02    00 fb cc 37 5a 0f d9 27    .?.........7Z..'
  00 00 fc 00 00 00 00 01    00 00 00 00 04 00 31 30    ..............10
  2e 32 2e 31 30 2d 4d 61    72 69 61 44 42 2d 6c 6f    .2.10-MariaDB-lo
  67 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    g...............
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 13 38 0d 00    08 00 12 00 04 04 04 04    .....8..........
  12 00 00 e4 00 04 1a 08    00 00 00 08 08 08 02 00    ................
  00 00 0a 0a 0a 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 00 00 00    00 00 00 00 00 00 00 00    ................
  00 00 00 00 00 04 13 04    00 0d 08 08 08 0a 0a 0a    ................
  01 17 0b 12 63 3c 00 00    03 00 fb cc 37 5a a3 d9    ....c<......7Z..
  27 00 00 3b 00 00 00 3b    01 00 00 00 00 02 00 00    '..;...;........
  00 00 00 00 00 01 00 00    00 1e 00 00 00 00 00 00    ................
  00 00 00 00 00 d9 27 00    00 86 26 00 00 00 00 00    ......'...&.....
  00 b6 33 8a 22 2c 00 00    04 00 fb cc 37 5a a1 d9    ..3.",......7Z..
  27 00 00 2b 00 00 00 66    01 00 00 00 00 10 00 00    '..+...f........
  00 6d 79 73 71 6c 2d 62    69 6e 2e 30 30 30 30 33    .mysql-bin.00003
  34 16 1f fe 3f 2c 00 00    05 00 00 00 00 00 a3 d9    4...?,..........
  27 00 00 2b 00 00 00 34    06 00 00 20 00 01 00 00    '..+...4... ....
  00 00 00 00 00 d9 27 00    00 8c 26 00 00 00 00 00    ......'...&.....
  00 4a 01 94 22 2b 00 00    06 00 94 fd 38 5a a2 d9    .J.."+......8Z..
  27 00 00 2a 00 00 00 5e    06 00 00 08 00 8d 26 00    '..*...^......&.
  00 00 00 00 00 00 00 00    00 29 00 00 00 00 00 00    .........)......
  22 87 c0 61 4c 00 00 07    00 94 fd 38 5a 02 d9 27    "..aL......8Z..'
  00 00 4b 00 00 00 a9 06    00 00 00 00 21 00 00 00    ..K.........!...
  00 00 00 00 00 00 00 1a    00 00 00 00 00 00 01 00    ................
  00 20 54 00 00 00 00 06    03 73 74 64 04 08 00 08    . T......std....
  00 08 00 00 66 6c 75 73    68 20 74 61 62 6c 65 73    ....flush tables
  6e c8 89 60                                           n..`
```

We can see:

1. `FAKE_ROTATE_EVENT` packet: 30 00 00 01 ... d5 3f ea d7
2. `FORMAT_DESCRIPTION_EVENT` packet: fd 00 00 02 00 ... 17 0b 12 63\
   FDE size is fc 00 00 00 (252)\
   Next Pos in FDE is 00 01 00 00 = >256 = 4 + FDE size (252)
3. `FAKE_GTID_LIST_EVENT` packet : 3c 00 00 03 00 ... b6 33 8a 22
4. `BINLOG_CHECKPOINT` EVENT packet: 2c 00 00 04 ... 16 1f fe 3f
5. `GTID_LIST_EVENT` packet: 2c 00 00 05 ... 4a 01 94 22
6. `GTID_EVENT` packet: 2b 00 00 06 ... 22 87 c0 61
7. `QUERY_EVENT` packet: 4c 00 00 07 ... 6e c8 89 60

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
