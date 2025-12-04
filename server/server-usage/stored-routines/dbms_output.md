---
description: >-
  The DBMS_OUTPUT plugin provides Oracle-compatible output buffering functions
  (like PUT_LINE), allowing stored procedures to send messages to the client.
---

# DBMS\_OUTPUT

{% hint style="info" %}
This feature is available from MariaDB Enterprise Server 11.8.
{% endhint %}

## Overview

Oracle documentation describing `DBMS_OUTPUT` can be found here:\
[https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS\_OUTPUT.html](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_OUTPUT.html)

The main idea of `DBMS_OUTPUT` is:

* Messages submitted by `DBMS_OUTPUT.PUT_LINE()` are not sent to the client until the sending subprogram (or trigger) completes. There is no a way to flush output during the execution of a procedure.
* Therefore, lines are collected into a server side buffer, which, at the end of the current user statement, can be fetched to the client side using another SQL statement. Then, they can be read using a regular MariaDB Connector-C API. No changes in the client-protocol are needed.
* Oracle's SQLPlus uses the procedure `DBMS_PACKAGE.GET_LINES()` to fetch the output to the client side as an array of strings.
* For JDBC, using `GET_LINES()` is preferable, because it's more efficient than individual `GET_LINE()` calls.

## Package Routines <a href="#packageroutines" id="packageroutines"></a>

### Package Overview

MariaDB implements all routines supported by Oracle, except `GET_LINES()`:

* Procedure `ENABLE()` - enable the routines.
* Procedure `DISABLE()` - disable the routines. If the package is disabled, all calls to subprograms, such as `PUT()` and `PUT_LINE()`, are ignored (or exit immediately without doing anything).
* Procedure `PUT_LINE()` - submit a line into the internal buffer.
* Procedure `PUT()` - submit a partial line into the buffer.
* Procedure `NEW_LINE()` - terminate a line submitted by `PUT()`.
* Procedure `GET_LINE()` - read one line (the earliest) from the buffer. When a line is read by `GET_LINE()`, it's automatically removed from the buffer.
* Procedure `GET_LINES()` - read all lines (as an array of strings) from the buffer - this procedure isn't implemented.

The package starts in disabled mode, so an explicit enabling is needed:

```sql
CALL DBMS_OUTPUT.ENABLE;
```

### Details <a href="#details" id="details"></a>

If a call for `GET_LINE` or `GET_LINES` did not retrieve all lines, then a subsequent call for `PUT`, `PUT_LINE`, or `NEW_LINE` discards the remaining lines (to avoid confusing with the next message). This script demonstrates the principle:

```sql
DROP TABLE t1;
CREATE TABLE t1 (line VARCHAR2(400), status INTEGER);
DECLARE
  line   VARCHAR2(400);
  status INTEGER;
BEGIN
  DBMS_OUTPUT.PUT_LINE('line1');
  DBMS_OUTPUT.PUT_LINE('line2');
  DBMS_OUTPUT.GET_LINE(line, status);
  INSERT INTO t1 VALUES (line, status);
  DBMS_OUTPUT.PUT_LINE('line3'); -- This cleares the buffer (removes line2) before putting line3
  LOOP
    DBMS_OUTPUT.GET_LINE(line, status);
    INSERT INTO t1 VALUES (line, status);
    EXIT WHEN status <> 0;
  END LOOP;
END;
/
SELECT * FROM t1;
```

| LINE  | STATUS |
| ----- | ------ |
| line1 | 0      |
| line3 | 0      |
| -     | 1      |

## Data Type for the Buffer <a href="#datatypeforthebuffer" id="datatypeforthebuffer"></a>

Oracle uses this data type as a storage for the buffer:

```sql
TYPE CHARARR IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER;
```

Like Oracle, MariaDB uses an associative array as a storage for the buffer.

## Data Type Used for GET\_LINES() <a href="#datatypeusedforgetlines-28-29notimplementedyet" id="datatypeusedforgetlines-28-29notimplementedyet"></a>

{% hint style="warning" %}
This functionality is not implemented.
{% endhint %}

In Oracle, the function `GET_LINES()` returns an array of strings of this data type:

```sql
TYPE DBMSOUTPUT_LINESARRAY IS VARRAY(2147483647) OF VARCHAR2(32767);
```

MariaDB does not have array data types in the C and C++ connectors, so they can't take advantage of `GET_LINES()` in a client program.

## Fetching all Lines in a PL/SQL Program <a href="#fetchingalllinesinapl-2fsqlprogram" id="fetchingalllinesinapl-2fsqlprogram"></a>

Fetching all lines in a PL/SQL program is implemented using a loop of `sys.DBMS_OUTPUT.GET_LINE()` calls:

```sql
SET sql_mode=ORACLE;
DELIMITER /
DECLARE
  all_lines MEDIUMTEXT CHARACTER SET utf8mb4 :='';
  line MEDIUMTEXT CHARACTER SET utf8mb4;
  status INT;
BEGIN
  sys.DBMS_OUTPUT.PUT_LINE('line1');
  sys.DBMS_OUTPUT.PUT_LINE('line2');
  sys.DBMS_OUTPUT.PUT_LINE('line3');
  LOOP
    sys.DBMS_OUTPUT.GET_LINE(line, status);
    EXIT WHEN status > 0;
    all_lines:= all_lines || line || '\n';
  END LOOP;
  SELECT all_lines;
END;
/
DELIMITER ;
```

## Fetching all Lines on the Client Side <a href="#fetchingalllinesontheclientside" id="fetchingalllinesontheclientside"></a>

Fetching all lines on the client side (for instance, in a C program using Connector/C) is done by using a loop of `sys.DBMS_OUTPUT.GET_LINE()` queries.

## Limits <a href="#limits-3a" id="limits-3a"></a>

Oracle has the following limits:

* The maximum individual line length (sent to `DBMS_OUTPUT`) is 32767 bytes.
* The default buffer size is 20000 bytes. The minimum size is 2000 bytes. The maximum is unlimited.

MariaDB also implements some limits, either using the total size of all rows or using the row count.

## Installation <a href="#installationandprivileges" id="installationandprivileges"></a>

Like other bootstrap scripts, the script creating `DBMS_OUTPUT`:

* Is put into a new separate `/scripts/dbms_ouput.sql` file in the source directory;
* Is installed into `/share/dbms_ouput.sql` of the installation directory.

\\
