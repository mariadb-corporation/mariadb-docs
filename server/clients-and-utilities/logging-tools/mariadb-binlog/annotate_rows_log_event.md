---
description: >-
  The ANNOTATE_ROWS_EVENT, which records the original SQL statement alongside
  row-based binary log events.
---

# Annotate\_rows\_log\_event

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

## Overview

`Annotate_rows` events accompany `row` events and describe the query which caused the row event.

In the [binary log](./), each `Annotate_rows` event precedes the corresponding Table map event or the first of the Table map events, if there are more than one (for instance, in a case of multi-delete or insert delayed).

## Example

```sql
master> DROP DATABASE IF EXISTS test;
master> CREATE DATABASE test;
master> USE test;
master> CREATE TABLE t1(a int);
master> INSERT INTO t1 VALUES (1), (2), (3);
master> CREATE TABLE t2(a int);
master> INSERT INTO t2 VALUES (1), (2), (3);
master> CREATE TABLE t3(a int);
master> INSERT DELAYED INTO t3 VALUES (1), (2), (3);
master> DELETE t1, t2 FROM t1 INNER JOIN t2 INNER JOIN t3
    ->        WHERE t1.a=t2.a AND t2.a=t3.a;  
    
master> SHOW BINLOG EVENTS IN 'master-bin.000001';  
+-------------------+------+---------------+-----------+-------------+---------------------------------------------------------------------------------+
| Log_name          | Pos  | Event_type    | Server_id | End_log_pos | Info                                                                            |
+-------------------+------+---------------+-----------+-------------+---------------------------------------------------------------------------------+
| master-bin.000001 |    4 | Format_desc   |       100 |         240 | Server ver: 5.5.20-MariaDB-mariadb1~oneiric-log, Binlog ver: 4                  |
| master-bin.000001 |  240 | Query         |       100 |         331 | DROP DATABASE IF EXISTS test                                                    |
| master-bin.000001 |  331 | Query         |       100 |         414 | CREATE DATABASE test                                                            |
| master-bin.000001 |  414 | Query         |       100 |         499 | use `test`; CREATE TABLE t1(a int)                                              |
| master-bin.000001 |  499 | Query         |       100 |         567 | BEGIN                                                                           |
| master-bin.000001 |  567 | Annotate_rows |       100 |         621 | INSERT INTO t1 VALUES (1), (2), (3)                                             |
| master-bin.000001 |  621 | Table_map     |       100 |         662 | table_id: 16 (test.t1)                                                          |
| master-bin.000001 |  662 | Write_rows    |       100 |         706 | table_id: 16 flags: STMT_END_F                                                  |
| master-bin.000001 |  706 | Query         |       100 |         775 | COMMIT                                                                          |
| master-bin.000001 |  775 | Query         |       100 |         860 | use `test`; CREATE TABLE t2(a int)                                              |
| master-bin.000001 |  860 | Query         |       100 |         928 | BEGIN                                                                           |
| master-bin.000001 |  928 | Annotate_rows |       100 |         982 | INSERT INTO t2 VALUES (1), (2), (3)                                             |
| master-bin.000001 |  982 | Table_map     |       100 |        1023 | table_id: 17 (test.t2)                                                          |
| master-bin.000001 | 1023 | Write_rows    |       100 |        1067 | table_id: 17 flags: STMT_END_F                                                  |
| master-bin.000001 | 1067 | Query         |       100 |        1136 | COMMIT                                                                          |
| master-bin.000001 | 1136 | Query         |       100 |        1221 | use `test`; CREATE TABLE t3(a int)                                              |
| master-bin.000001 | 1221 | Query         |       100 |        1289 | BEGIN                                                                           |
| master-bin.000001 | 1289 | Annotate_rows |       100 |        1351 | INSERT DELAYED INTO t3 VALUES (1), (2), (3)                                     |
| master-bin.000001 | 1351 | Table_map     |       100 |        1392 | table_id: 18 (test.t3)                                                          |
| master-bin.000001 | 1392 | Write_rows    |       100 |        1426 | table_id: 18 flags: STMT_END_F                                                  |
| master-bin.000001 | 1426 | Table_map     |       100 |        1467 | table_id: 18 (test.t3)                                                          |
| master-bin.000001 | 1467 | Write_rows    |       100 |        1506 | table_id: 18 flags: STMT_END_F                                                  |
| master-bin.000001 | 1506 | Query         |       100 |        1575 | COMMIT                                                                          |
| master-bin.000001 | 1575 | Query         |       100 |        1643 | BEGIN                                                                           |
| master-bin.000001 | 1643 | Annotate_rows |       100 |        1748 | DELETE t1, t2 FROM t1 INNER JOIN t2 INNER JOIN t3 WHERE t1.a=t2.a AND t2.a=t3.a |
| master-bin.000001 | 1748 | Table_map     |       100 |        1789 | table_id: 16 (test.t1)                                                          |
| master-bin.000001 | 1789 | Table_map     |       100 |        1830 | table_id: 17 (test.t2)                                                          |
| master-bin.000001 | 1830 | Delete_rows   |       100 |        1874 | table_id: 16                                                                    |
| master-bin.000001 | 1874 | Delete_rows   |       100 |        1918 | table_id: 17 flags: STMT_END_F                                                  |
| master-bin.000001 | 1918 | Query         |       100 |        1987 | COMMIT                                                                          |
+-------------------+------+---------------+-----------+-------------+---------------------------------------------------------------------------------+
```

## Options

The following options control the behavior of`Annotate_rows_log_event`.

### Master Option: `--binlog-annotate-row-events`

This option tells the master to write `Annotate_rows` events to the binary log. See [binlog\_annotate\_row\_events](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for a detailed description of the variable.

Session values allow to annotate only some selected statements:

```sql
...
SET SESSION binlog_annotate_row_events=ON;
... statements to be annotated ...
SET SESSION binlog_annotate_row_events=OFF;
... statements not to be annotated ...
```

### Replica Option: `--replicate-annotate-row-events`

This option tells the replica to reproduce `Annotate_row` events received from the master in its own binary log (sensible only when used in tandem with the `log-slave-updates` option).

See [replicate\_annotate\_row\_events](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for a detailed description of the variable.

### mariadb-binlog Option: `--skip-annotate-row-events`

This option tells [mariadb-binlog](using-mariadb-binlog.md) to skip all `Annotate_row` events in its output (by default, mariadb-binlog prints `Annotate_row` events, if the binary log contains them).

## Example of mariadb-binlog Output

```sql
...> mariadb-binlog.exe -vv -R --user=root --port=3306 --host=localhost master-bin.000001  

/*!40019 SET @@session.max_insert_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
# at 4
#100516 15:36:00 server id 100  end_log_pos 240         Start: binlog v 4, server v 5.1.44-debug-log created 100516
 15:36:00 at startup
ROLLBACK/*!*/;
BINLOG '
oNjvSw9kAAAA7AAAAPAAAAAAAAQANS4xLjQ0LWRlYnVnLWxvZwAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAACg2O9LEzgNAAgAEgAEBAQEEgAA2QAEGggAAAAICAgCAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAA=
'/*!*/;
# at 240
#100516 15:36:18 server id 100  end_log_pos 331         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
SET @@session.pseudo_thread_id=1/*!*/;
SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=1, @@session.unique_checks=1, @@session.autocommit=1
/*!*/;
SET @@session.sql_mode=0/*!*/;
SET @@session.auto_increment_increment=1, @@session.auto_increment_offset=1/*!*/;
/*!\C latin1 *//*!*/;
SET @@session.character_set_client=8,@@session.collation_connection=8,@@session.collation_server=8/*!*/;
SET @@session.lc_time_names=0/*!*/;
SET @@session.collation_database=DEFAULT/*!*/;
DROP DATABASE IF EXISTS test
/*!*/;
# at 331
#100516 15:36:18 server id 100  end_log_pos 414         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
CREATE DATABASE test
/*!*/;
# at 414
#100516 15:36:18 server id 100  end_log_pos 499         Query   thread_id=1     exec_time=0     error_code=0
use test/*!*/;
SET TIMESTAMP=1274009778/*!*/;
CREATE TABLE t1(a int)
/*!*/;
# at 499
#100516 15:36:18 server id 100  end_log_pos 567         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
BEGIN
/*!*/;
# at 567
# at 621
# at 662
#100516 15:36:18 server id 100  end_log_pos 621         Annotate_rows:
#Q> INSERT INTO t1 VALUES (1), (2), (3)  
#100516 15:36:18 server id 100  end_log_pos 662         Table_map: `test`.`t1` mapped to number 16
#100516 15:36:18 server id 100  end_log_pos 706         Write_rows: table id 16 flags: STMT_END_F

BINLOG '
stjvSxNkAAAAKQAAAJYCAAAAABAAAAAAAAAABHRlc3QAAnQxAAEDAAE=
stjvSxdkAAAALAAAAMICAAAQABAAAAAAAAEAAf/+AQAAAP4CAAAA/gMAAAA=
'/*!*/;
### INSERT INTO test.t1
### SET
###   @1=1 /* INT meta=0 nullable=1 is_null=0 */
### INSERT INTO test.t1
### SET
###   @1=2 /* INT meta=0 nullable=1 is_null=0 */
### INSERT INTO test.t1
### SET
###   @1=3 /* INT meta=0 nullable=1 is_null=0 */
# at 706
#100516 15:36:18 server id 100  end_log_pos 775         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
COMMIT
/*!*/;
# at 775
#100516 15:36:18 server id 100  end_log_pos 860         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
CREATE TABLE t2(a int)
/*!*/;
# at 860
#100516 15:36:18 server id 100  end_log_pos 928         Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
BEGIN
/*!*/;
# at 928
# at 982
# at 1023
#100516 15:36:18 server id 100  end_log_pos 982         Annotate_rows:
#Q> INSERT INTO t2 VALUES (1), (2), (3)  
#100516 15:36:18 server id 100  end_log_pos 1023        Table_map: `test`.`t2` mapped to number 17
#100516 15:36:18 server id 100  end_log_pos 1067        Write_rows: table id 17 flags: STMT_END_F

BINLOG '
stjvSxNkAAAAKQAAAP8DAAAAABEAAAAAAAAABHRlc3QAAnQyAAEDAAE=
stjvSxdkAAAALAAAACsEAAAQABEAAAAAAAEAAf/+AQAAAP4CAAAA/gMAAAA=
'/*!*/;
### INSERT INTO test.t2
### SET
###   @1=1 /* INT meta=0 nullable=1 is_null=0 */
### INSERT INTO test.t2
### SET
###   @1=2 /* INT meta=0 nullable=1 is_null=0 */
### INSERT INTO test.t2
### SET
###   @1=3 /* INT meta=0 nullable=1 is_null=0 */
# at 1067
#100516 15:36:18 server id 100  end_log_pos 1136        Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
COMMIT
/*!*/;
# at 1136
#100516 15:36:18 server id 100  end_log_pos 1221        Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
CREATE TABLE t3(a int)
/*!*/;
# at 1221
#100516 15:36:18 server id 100  end_log_pos 1289        Query   thread_id=2     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
BEGIN
/*!*/;
# at 1289
# at 1351
# at 1392
#100516 15:36:18 server id 100  end_log_pos 1351        Annotate_rows:
#Q> INSERT DELAYED INTO t3 VALUES (1), (2), (3)  
#100516 15:36:18 server id 100  end_log_pos 1392        Table_map: `test`.`t3` mapped to number 18
#100516 15:36:18 server id 100  end_log_pos 1426        Write_rows: table id 18 flags: STMT_END_F

BINLOG '
stjvSxNkAAAAKQAAAHAFAAAAABIAAAAAAAAABHRlc3QAAnQzAAEDAAE=
stjvSxdkAAAAIgAAAJIFAAAQABIAAAAAAAEAAf/+AQAAAA==
'/*!*/;
### INSERT INTO test.t3
### SET
###   @1=1 /* INT meta=0 nullable=1 is_null=0 */
# at 1426
# at 1467
#100516 15:36:18 server id 100  end_log_pos 1467        Table_map: `test`.`t3` mapped to number 18
#100516 15:36:18 server id 100  end_log_pos 1506        Write_rows: table id 18 flags: STMT_END_F

BINLOG '
stjvSxNkAAAAKQAAALsFAAAAABIAAAAAAAAABHRlc3QAAnQzAAEDAAE=
stjvSxdkAAAAJwAAAOIFAAAQABIAAAAAAAEAAf/+AgAAAP4DAAAA
'/*!*/;
### INSERT INTO test.t3
### SET
###   @1=2 /* INT meta=0 nullable=1 is_null=0 */
### INSERT INTO test.t3
### SET
###   @1=3 /* INT meta=0 nullable=1 is_null=0 */
# at 1506
#100516 15:36:18 server id 100  end_log_pos 1575        Query   thread_id=2     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
COMMIT
/*!*/;
# at 1575
#100516 15:36:18 server id 100  end_log_pos 1643        Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
BEGIN
/*!*/;
# at 1643
# at 1748
# at 1789
# at 1830
# at 1874
#100516 15:36:18 server id 100  end_log_pos 1748        Annotate_rows:
#Q> DELETE t1, t2 FROM t1 INNER JOIN t2 INNER JOIN t3
#Q>        WHERE t1.a=t2.a AND t2.a=t3.  
#100516 15:36:18 server id 100  end_log_pos 1789        Table_map: `test`.`t1` mapped to number 16
#100516 15:36:18 server id 100  end_log_pos 1830        Table_map: `test`.`t2` mapped to number 17
#100516 15:36:18 server id 100  end_log_pos 1874        Delete_rows: table id 16
#100516 15:36:18 server id 100  end_log_pos 1918        Delete_rows: table id 17 flags: STMT_END_F

BINLOG '
stjvSxNkAAAAKQAAAP0GAAAAABAAAAAAAAAABHRlc3QAAnQxAAEDAAE=
stjvSxNkAAAAKQAAACYHAAAAABEAAAAAAAAABHRlc3QAAnQyAAEDAAE=
stjvSxlkAAAALAAAAFIHAAAAABAAAAAAAAAAAf/+AQAAAP4CAAAA/gMAAAA=
### DELETE FROM test.t1
### WHERE
###   @1=1 /* INT meta=0 nullable=1 is_null=0 */
### DELETE FROM test.t1
### WHERE
###   @1=2 /* INT meta=0 nullable=1 is_null=0 */
### DELETE FROM test.t1
### WHERE
###   @1=3 /* INT meta=0 nullable=1 is_null=0 */
stjvSxlkAAAALAAAAH4HAAAQABEAAAAAAAEAAf/+AQAAAP4CAAAA/gMAAAA=
'/*!*/;
### DELETE FROM test.t2
### WHERE
###   @1=1 /* INT meta=0 nullable=1 is_null=0 */
### DELETE FROM test.t2
### WHERE
###   @1=2 /* INT meta=0 nullable=1 is_null=0 */
### DELETE FROM test.t2
### WHERE
###   @1=3 /* INT meta=0 nullable=1 is_null=0 */
# at 1918
#100516 15:36:18 server id 100  end_log_pos 1987        Query   thread_id=1     exec_time=0     error_code=0
SET TIMESTAMP=1274009778/*!*/;
COMMIT
/*!*/;
DELIMITER ;
# End of log file
ROLLBACK /* added by mariadb-binlog */;
/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;
```

## See Also

* [mariadb-binlog Options](mariadb-binlog-options.md)
* [Replication and Binary Log Server System Variables](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [Full List of MariaDB Options, System and Status Variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md)
* [mariadbd Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
