# XMLTYPE

## Introduced

MariaDB 12.3

## Syntax

```
XMLTYPE
```

* No parameters accepted
* Length specification for `XMLTYPE` (e.g., `XMLTYPE(100)`) results in an error

## Description

`XMLTYPE` is a data type introduced in MariaDB 12.3 for storing XML data. It is designed to:

* Provide convenient storage of XML data
* Ensure compatibility with Oracle databases
* Support future XML validation and processing capabilities

In its initial implementatio&#x6E;_,_ `XMLTYPE` provides basic XML storage capabilities onl&#x79;_,_ without validation or specialized XML-specific functionalit&#x79;_._ When using string functions, the data type is effectively converted to strings and is maintained in temporary tables.

## Characteristics

* Maximum storage capacity: 4GB (same as `LONGBLOB`)
* Compatibilit&#x79;**:** Designed to be compatible with Oracle’s `XMLTYPE`
* Validatio&#x6E;**:** XML validation or schema enforcement is not supported
* Length restrictio&#x6E;**:** Length cannot be specified.

**Example (invalid usage):**

```
CREATE TABLE t1 (a XMLTYPE(6));
```

`XMLTYPE` does not accept length parameters, unlike data types such as `VARCHAR(255)` or `DECIMAL(10,2)`_._

## Related Functions

With MariaDB 12.3, the following functions return the `XMLTYPE` data type:

* `UPDATEXML`&#x20;
* `CAST`&#x20;

## **Examples**

### Basic Tables Creation

```
CREATE TABLE t1(id INT, x xmltype);
SHOW CREATE TABLE t1;
```

**Output**

```
Table	Create Table
t1	CREATE TABLE `t1` (
  `id` int(11) DEFAULT NULL,
  `x` xmltype DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci
```

### Character Set Specification

```
CREATE TABLE t1(id INT, x xmltype  CHARACTER SET utf8mb3) CHARACTER SET utf8mb4;
SHOW CREATE TABLE t1;
```

**Output**

```
Table	Create Table
t1	CREATE TABLE `t1` (
  `id` int(11) DEFAULT NULL,
  `x` xmltype CHARACTER SET utf8mb3 COLLATE utf8mb3_uca1400_ai_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci
```

### Binary Attribute

```
CREATE TABLE t1 (a xmltype binary) CHARACTER SET utf8mb4;
SHOW CREATE TABLE t1;
```

**Output**

```
Table	Create Table
t1	CREATE TABLE `t1` (
  `a` xmltype CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci
```

### Basic Data Insertion and Selection

```
CREATE TABLE t1(id INT, x xmltype);
INSERT INTO t1 VALUES (1, 'one'), (2, 'two'), (3, 'three');
SELECT * FROM t1;
```

**Output**

```
id	x
1	 one
2	 two
3	 three
```

### Restrictions and Error Cases

#### Length Specification Not Permitted

If a length parameter is provided for `XMLTYPE`_,_ the system returns an error:

```
CREATE TABLE t1 (a XMLTYPE(6));
```

**Output**

```
ERROR HY000: Data type 'XMLTYPE' doesn't support LENGTH attribute.
```

#### REF\_SYSTEM\_ID Attribute Not Supported

```
CREATE TABLE t1 (a XMLTYPE REF_SYSTEM_ID=4);
```

**Output**

```
ERROR HY000: Data type 'XMLTYPE' doesn't support REF_SYSTEM_ID attribute.

```

#### Length Parameters in Complex Column Definitions

```
CREATE TABLE t1(id INT, x xmltype(10, 2));
```

**Output**

```
ERROR HY000: Data type 'xmltype' doesn't support LENGTH attribute.
```

## See Also

* [CAST](../../sql-functions/string-functions/cast.md)
* [Data Types](../)
* [String Functions](../../../server-usage/basics/mariadb-string-functions-guide-1.md)
* [LONGBLOB](longblob.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
