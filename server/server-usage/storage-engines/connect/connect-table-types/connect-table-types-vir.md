---
description: The CONNECT storage engine.
---

# CONNECT Table Types - VIR

## VIR Type

A VIR table is a virtual table having only Special or Virtual columns. Its only property is its “size”, or cardinality, meaning the number of virtual rows it contains. It is created using the syntax:

```sql
CREATE TABLE name [coldef] ENGINE=CONNECT TABLE_TYPE=VIR
[BLOCK_SIZE=n];
```

The optional `BLOCK_SIZE` option gives the size of the table, defaulting to 1 if not specified. When its columns are not specified, it is almost equivalent to a [SEQUENCE](../../sequence-storage-engine.md) table “seq\_1\_to\_Size”.

### Displaying constants or expressions

Many DBMS use a no-column one-line table to do this, often call “dual”. MySQL and MariaDB use\
syntax where no table is specified. With CONNECT, you can achieve the same purpose with a virtual\
table, with the noticeable advantage of being able to display several lines:

```sql
CREATE TABLE virt ENGINE=CONNECT table_type=VIR block_size=10;
SELECT concat('The square root of ', n, ' is') what,
round(sqrt(n),16) value FROM virt;
```

This will return:

| what                     | value              |
| ------------------------ | ------------------ |
| The square root of 1 is  | 1.0000000000000000 |
| The square root of 2 is  | 1.4142135623730951 |
| The square root of 3 is  | 1.7320508075688772 |
| The square root of 4 is  | 2.0000000000000000 |
| The square root of 5 is  | 2.2360679774997898 |
| The square root of 6 is  | 2.4494897427831779 |
| The square root of 7 is  | 2.6457513110645907 |
| The square root of 8 is  | 2.8284271247461903 |
| The square root of 9 is  | 3.0000000000000000 |
| The square root of 10 is | 3.1622776601683795 |

What happened here? First of all, unlike Oracle “dual” tableS that have no columns, a MariaDB table must have at least one column. By default, CONNECT creates VIR tables with one special column. This can be seen with the SHOW CREATE TABLE statement:

```
CREATE TABLE `virt` (
`n` INT(11) NOT NULL `SPECIAL`=ROWID,
PRIMARY KEY (`n`)
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='VIR'
`BLOCK_SIZE`=10
```

This special column is called “n” and its value is the row number starting from 1. It is purely a virtual\
table and no data file exists corresponding to it and to its index.\
It is possible to specify the columns of a VIR table but they must be CONNECT special columns or\
virtual columns. For instance:

```
CREATE TABLE virt2 (
n INT KEY NOT NULL special=ROWID,
sig1 BIGINT AS ((n*(n+1))/2) virtual,
sig2 BIGINT AS(((2*n+1)*(n+1)*n)/6) virtual)
ENGINE=CONNECT table_type=VIR block_size=10000000;
SELECT * FROM virt2 LIMIT 995, 5;
```

This table shows the sum and the sum of the square of the n first integers:

| n    | sig1   | sig2      |
| ---- | ------ | --------- |
| 996  | 496506 | 329845486 |
| 997  | 497503 | 330839495 |
| 998  | 498501 | 331835499 |
| 999  | 499500 | 332833500 |
| 1000 | 500500 | 333833500 |

Note that the size of the table can be made very big as there no physical data. However, the result\
should be limited in the queries. For instance:

```
SELECT * FROM virt2 WHERE n = 1664510;
```

Such a query could last very long if the rowid column were not indexed. Note that by default,\
CONNECT declares the “n” column as a primary key. Actually, VIR tables can be indexed but only on\
the ROWID (or ROWNUM) columns of the table. This is a virtual index for which no data is stored.

### Generating a Table filled with constant values

An interesting use of virtual tables, which often cannot be achieved with a table of any other type, is to\
generate a table containing constant values.\
This is easily done with a virtual table. Let us define the table FILLER as:

```
CREATE TABLE filler ENGINE=CONNECT table_type=VIR block_size=5000000;
```

Here we choose a size larger than the biggest table we want to generate. Later if we need a table pre-\
filled with default and/or null values, we can do for example:

```
CREATE TABLE tp (
id INT(6) KEY NOT NULL,
name CHAR(16) NOT NULL,
salary FLOAT(8,2));
INSERT INTO tp SELECT n, 'unknown', NULL FROM filler WHERE n <= 10000;
```

This will generate a table having 10000 rows that can be updated later when needed. Note that a [SEQUENCE](../../sequence-storage-engine.md) table could have been used here instead of FILLING .

### VIR tables vs. SEQUENCE tables

With just its default column, a VIR table is almost equivalent to a [SEQUENCE](../../sequence-storage-engine.md) table. The syntax used is the main difference, for instance:

```
SELECT * FROM seq_100_to_150_step_10;
```

can be obtained with a VIR table (of size >= 15) by:

```
SELECT n*10 FROM vir WHERE n BETWEEN 10 AND 15;
```

Therefore, the main difference is to be able to define the columns of VIR tables. Unfortunately, there are currently many limitations to virtual columns that hopefully should be removed in the future.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
