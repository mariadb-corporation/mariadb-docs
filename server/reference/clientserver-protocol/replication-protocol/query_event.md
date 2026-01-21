---
description: >-
  The QUERY_EVENT records text-based SQL statements for statement-based
  replication, capturing the query string and execution context like the default
  database.
---

# QUERY\_EVENT

This event is written into the binary log file for:

* Statement-based replication (updating statements).
* DDLs.
* COMMIT related to nontransactional engines (like [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) or [BLACKHOLE](../../../server-usage/storage-engines/blackhole.md)).

## Header

* Event Type = 0x02.

## Fields

Fixed data part:

* [uint<4>](../protocol-data-types.md#fixed-length-integers) The ID of the thread that issued this statement on the master.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) The time in seconds that the statement took to execute.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) The length of the name of the database which was the default database when the statement was executed. This name appears later, in the variable data part. It is necessary for statements such as `INSERT INTO t VALUES(1)` that don't specify the database and rely on the default database previously selected by `USE`.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The error code resulting from execution of the statement on the master.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) The length of the status variable block.

Variable data part:

* [byte](../protocol-data-types.md#fixed-length-bytes) Zero or more status variables. Each status variable consists of one byte code identifying the variable stored, followed by the value of the variable. The format of the value is variable-specific.\
  The number of bytes 'n' is the length of the status variable block (read in fixed data part).
* [string](../protocol-data-types.md#fixed-length-bytes) The default database name (null-terminated).
* [string](../protocol-data-types.md#fixed-length-bytes) The SQL statement. By subtraction the size of the statement can be known.

## Status variables

### Q\_FLAGS2\_CODE (0x00)

* [uint<4>](../protocol-data-types.md#fixed-length-integers) bitmask.

| Value      | Option                           |
| ---------- | -------------------------------- |
| 0x00004000 | OPTION\_AUTO\_IS\_NULL           |
| 0x00080000 | OPTION\_NOT\_AUTOCOMMIT          |
| 0x04000000 | OPTION\_NO\_FOREIGN\_KEY\_CHECKS |
| 0x08000000 | OPTION\_RELAXED\_UNIQUE\_CHECKS  |

### Q\_SQL\_MODE\_CODE (0x01)

* [uint<8>](../protocol-data-types.md#fixed-length-integers) 8-byte bitmask.

| Value      | Option                               |
| ---------- | ------------------------------------ |
| 0x00000001 | MODE\_REAL\_AS\_FLOAT                |
| 0x00000002 | MODE\_PIPES\_AS\_CONCAT              |
| 0x00000004 | MODE\_ANSI\_QUOTES                   |
| 0x00000008 | MODE\_IGNORE\_SPACE                  |
| 0x00000010 | MODE\_NOT\_USED                      |
| 0x00000020 | MODE\_ONLY\_FULL\_GROUP\_BY          |
| 0x00000040 | MODE\_NO\_UNSIGNED\_SUBTRACTION      |
| 0x00000080 | MODE\_NO\_DIR\_IN\_CREATE            |
| 0x00000100 | MODE\_POSTGRESQL                     |
| 0x00000200 | MODE\_ORACLE                         |
| 0x00000400 | MODE\_MSSQL                          |
| 0x00000800 | MODE\_DB2                            |
| 0x00001000 | MODE\_MAXDB                          |
| 0x00002000 | MODE\_NO\_KEY\_OPTIONS               |
| 0x00004000 | MODE\_NO\_TABLE\_OPTIONS             |
| 0x00008000 | MODE\_NO\_FIELD\_OPTIONS             |
| 0x00010000 | MODE\_MYSQL323                       |
| 0x00020000 | MODE\_MYSQL40                        |
| 0x00040000 | MODE\_ANSI                           |
| 0x00080000 | MODE\_NO\_AUTO\_VALUE\_ON\_ZERO      |
| 0x00100000 | MODE\_NO\_BACKSLASH\_ESCAPES         |
| 0x00200000 | MODE\_STRICT\_TRANS\_TABLES          |
| 0x00400000 | MODE\_STRICT\_ALL\_TABLES            |
| 0x00800000 | MODE\_NO\_ZERO\_IN\_DATE             |
| 0x01000000 | MODE\_NO\_ZERO\_DATE                 |
| 0x02000000 | MODE\_INVALID\_DATES                 |
| 0x04000000 | MODE\_ERROR\_FOR\_DIVISION\_BY\_ZERO |
| 0x08000000 | MODE\_TRADITIONAL                    |
| 0x10000000 | MODE\_NO\_AUTO\_CREATE\_USER         |
| 0x20000000 | MODE\_HIGH\_NOT\_PRECEDENCE          |
| 0x40000000 | MODE\_NO\_ENGINE\_SUBSTITUTION       |
| 0x80000000 | MODE\_PAD\_CHAR\_TO\_FULL\_LENGTH    |

### **Q\_CATALOG\_NZ\_CODE** (0x02)

* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string\<length +1>](../protocol-data-types.md#fixed-length-bytes) catalog name + '\0'

### **Q\_AUTO\_INCREMENT** (0x03)

* [uint<2>](../protocol-data-types.md#fixed-length-integers) auto\_increment increment
* [uint<2>](../protocol-data-types.md#fixed-length-integers) auto\_increment offset

### **Q\_CHARSET\_CODE** (0x04)

* [uint<2>](../protocol-data-types.md#fixed-length-integers) client character set
* [uint<2>](../protocol-data-types.md#fixed-length-integers) collation\_connection
* [uint<2>](../protocol-data-types.md#fixed-length-integers) collation\_server

### **Q\_TIMEZONE\_CODE** (0x05)

* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string](../protocol-data-types.md#fixed-length-bytes) time zone

### **Q\_CATALOG\_NZ\_CODE** (0x06)

* [uint<1>](../protocol-data-types.md#fixed-length-integers) length
* [string](../protocol-data-types.md#fixed-length-bytes) catalog

### **Q\_LC\_TIME\_NAMES\_CODE** (0x07)

* [uint<2>](../protocol-data-types.md#fixed-length-integers) code\
  The mapping between code and names are defined in sql\_locale.cc.

### **Q\_CHARSET\_DATABASE\_CODE** (0x08)

* [uint<2>](../protocol-data-types.md#fixed-length-integers) database collation

### **Q\_TABLE\_MAP\_FOR\_UPDATE\_CODE** (0x09)

* [uint<8>](../protocol-data-types.md#fixed-length-integers) table bittmask\
  Every bit of this variable represents a table, and is set to 1 if the corresponding table is to be updated by this statement.

### **Q\_MASTER\_DATA\_WRITTEN\_CODE** (0x0A)

* Not in use any more
* [uint<4>](../protocol-data-types.md#fixed-length-integers) original event length

### **Q\_INVOKER** (0x0B|)

* [uint<1>](../protocol-data-types.md#fixed-length-integers) user name length
* [string](../protocol-data-types.md#fixed-length-bytes) user name
* [uint<1>](../protocol-data-types.md#fixed-length-integers) host name length
* [string](../protocol-data-types.md#fixed-length-bytes) host name

### **Q\_UPDATED\_DB\_NAMES** (0x0C)

* MySQL only
* [uint<1>](../protocol-data-types.md#fixed-length-integers) count
* for (i=0;i < count; i++)
  * [string](../protocol-data-types.md#fixed-length-bytes) Null terminated database name

### **Q\_MICROSECONDS** (0x0D)

* MySQL only
* [uint<3>](../protocol-data-types.md#fixed-length-integers) microsecond part

### **Q\_HRNOW** (0x80)

* MariaDB only
* [uint<3>](../protocol-data-types.md#fixed-length-integers) microsecond part

### **Q\_XID** (0x81)

* MariaDB only
* [uint<8>](../protocol-data-types.md#fixed-length-integers) xid

## Example With CRC32

```sql
71 17 28 5a 02 8c 27 00  00 55 00 00 00 01 09 00  q.(Z..'..U......
00 00 00 66 01 00 00 00  00 00 00 00 00 00 1a 00  ...f............
00 00 00 00 00 01 00 00  00 50 00 00 00 00 06 03  .........P......
73 74 64 04 08 00 08 00  08 00 00 54 52 55 4e 43  std........TRUNC
41 54 45 20 54 41 42 4c  45 20 74 65 73 74 2e 74  ATE TABLE test.t
34 4a 69 9e ed                                    4Ji..
```

## Header, 19 Bytes

* Event Time\[4] = 71 17 28 5a ===> 1512576881.
* Event Type\[1] = 2.
* Server\_id\[4] = 8c 27 00 00 ===> 10124.
* Event Size = 55 00 00 00 ===> 85.
* Next Pos = 01 09 00 00 ===> 2305.
* Flags = 00 00 => 0.

## Content, Variable Data

* Thread ID\[4] = 66 01 00 00 ===> 358.
* Execution Time\[4] = 00 00 00 00 => 0 seconds.
* Statement default database name len\[1] = 00 => 0 (no default database).
* Error code\[2] = 00 00 => 0 (no errors).
* Status variable block len\[2] = 1a 00 => 26.
* Status variables\[n] = 00 ... 08 00.
* The default database\[string] = 00 = 0 (no default database).
* The SQL statement\[string] = `TRUNCATE TABLE` test.t4.

## CRC32, 4 Bytes

* 4a 69 9e ed.

## Example With Default Database and CRC32

```
MariaDB []> use test;
Database changed
MariaDB [test]> TRUNCATE TABLE t4;
...

ce 22 28 5a 02 8c 27 00  00 54 00 00 00 87 0c 00  ."(Z..'..T......
00 00 00 66 01 00 00 01  00 00 00 04 00 00 1a 00  ...f............
00 00 00 00 00 01 00 00  00 50 00 00 00 00 06 03  .........P......
73 74 64 04 08 00 08 00  08 00 74 65 73 74 00 54  std.......test.T
52 55 4e 43 41 54 45 20  54 41 42 4c 45 20 74 34  RUNCATE TABLE t4
08 f1 09 16                                       ....
```

## Content, Variable Data

* Thread ID\[4] = 66 01 00 00 ===> 358.
* Execution Time\[4] = 10 00 00 00 => 1 second.
* Statement default database name len\[1] = 04 => 4 (default database is "test").
* Error code\[2] = 00 00 => 0 (no errors).
* Status variable block len\[2] = 1a 00 => 26.
* Status variables\[n] = 00 ... 08 00.
* The default database\[string] = 74 65 73 74 00 ⇒ test.
* The SQL statement\[string] = `TRUNCATE TABLE` test.t4.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
