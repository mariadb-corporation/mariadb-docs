---
description: >-
  IPv6 address data type. Stores IPv6 addresses as 16-byte binary strings, also
  supporting IPv4 addresses via mapping.
---

# INET6

{% hint style="info" %}
`INET6` is available from MariaDB 10.5.
{% endhint %}

## Syntax

```sql
INET6
```

## Description

The `INET6` data type is intended for storage of IPv6 addresses, as well as IPv4 addresses assuming conventional mapping of IPv4 addresses into IPv6 addresses.

Both short and long IPv6 notation are permitted, according to RFC-5952.

* Values are stored as a 16-byte fixed length binary string, with most significant byte first.
* Storage engines see `INET6` as `BINARY(16)`.
* Clients see `INET6` as `CHAR(39)` and get text representation on retrieval.

The IPv4-compatible notation is considered as deprecated. It is supported for compatibility with the [INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) function, which also understands this format. It's recommended to use the mapped format to store IPv4 addresses in `INET6`.

When an IPv4 mapped (or compatible) value is stored in `INET6`, it still occupies 16 bytes:

### Retrieval

On retrieval, in the client-server text protocol, `INET6` values are converted to the short text representation, according to RFC-5952, that is with all leading zeroes in each group removed and with consequent zero groups compressed.

Besides creating one's own [stored function](../../../server-usage/stored-routines/stored-functions/), there is no a way to retrieve an `INET6` value using long text representation.

### Casting

* [CAST](../../sql-functions/string-functions/cast.md) from a character string to `INET6` understands addresses in short or long text notation (including IPv4 mapped and compatible addresses). `NULL` is returned if the format is not understood.
* `CAST` from a binary string to `INET6` requires a 16-byte string as an argument. `NULL` is returned if the argument length is not equal to 16.
* `CAST` from other data types to `INET6` first converts data to a character string, then `CAST` from character string to `INET6` is applied.
* `CAST` from `INET6` to [CHAR](char.md) returns short text address notation.
* `CAST` from `INET6` to [BINARY](binary.md) returns its 16-byte binary string representation.
* `CAST` from `INET6` to data types other than [CHAR](char.md) (e.g. `SIGNED`, `UNSIGNED`, `TIME`, etc) returns an error.

### Comparisons

An `INET6` expression can be compared to:

* another `INET6` expression
* a character string expression with a text (short or long) address representation:
* a 16-byte binary string expression.

{% hint style="warning" %}
Attempting to compare `INET6` to an expression of any other data type returns an error.
{% endhint %}

### Mixing INET6 Values for Result

An `INET6` expression can be mixed for result (i.e. [UNION](../../sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md), [CASE..THEN](https://mariadb.com/kb/en/case), [COALESCE](../../sql-structure/operators/comparison-operators/coalesce.md) etc) with:

* another `INET6` expression. The resulting data type is `INET6`.
* a character string in text (short or long) address representation. The result data type is `INET6`. The character string counterpart is automatically converted to `INET6`. If the string format is not understood, it's converted with a warning to either `NULL` or to '::', depending on the `NULL`-ability of the result.
* a 16-byte binary string. The resulting data type is `INET6`. The binary string counterpart is automatically converted to `INET6`. If the length of the binary string is not equal to 16, it's converted with a warning to `NULL` or to '::' depending on the `NULL`-ability of the result.

Attempts to mix `INET6` for result with other data types will return an error.

Mixing `INET6` with other data types for [LEAST](../../sql-structure/operators/comparison-operators/least.md) and [GREATEST](../../sql-structure/operators/comparison-operators/greatest.md), when mixing for comparison and mixing for result are involved at the same time, uses the same rules with mixing for result, described in the previous paragraphs.

### Functions and Operators

* [HEX()](../../sql-functions/string-functions/hex.md) with an INET6 argument returns a hexadecimal representation of the underlying 16-byte binary string
* Arithmetic operators (+,-,\*,/,MOD,DIV) are not supported for INET6. This may change in the future.
* The [INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) function now understands INET6 values as an argument
* The prototypes of the [IS\_IPV4\_COMPAT](../../sql-functions/secondary-functions/miscellaneous-functions/is_ipv4_compat.md) and I [S\_IPV4\_MAPPED](../../sql-functions/secondary-functions/miscellaneous-functions/is_ipv4_mapped.md) functions have changed from `a BINARY(16)` to `a INET6`,

{% tabs %}
{% tab title="Current" %}
When the argument for the aforementioned two functions is not `INET6`, automatic implicit `CAST` to `INET6` is applied. As a consequence, both functions understand arguments in both text representation and binary(16) representation.
{% endtab %}

{% tab title="< 10.5" %}
When the argument for the aforementioned two functions is not `INET6`, automatic implicit `CAST` to `INET6` is **not** applied.
{% endtab %}
{% endtabs %}

### Prepared Statement Parameters

INET6 understands both [text](text.md) and [binary(16)](binary.md) address representation in [prepared statement](../../sql-statements/prepared-statements/) parameters ([PREPARE](../../sql-statements/prepared-statements/prepare-statement.md)..[EXECUTE](../../sql-statements/prepared-statements/execute-statement.md) and [EXECUTE IMMEDIATE](../../sql-statements/prepared-statements/execute-immediate.md) statements).

### Migration between BINARY(16) and INET6

{% tabs %}
{% tab title="Current" %}
You may have used [BINARY(16)](binary.md) as a storage for IPv6 internet addresses, in combination with [INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) and [INET6\_NTOA](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_ntoa.md) to respectively insert and retrieve data.

However, you can [ALTER](../../sql-statements/data-definition/alter/alter-table/) `BINARY(16)` columns storing IPv6 addresses to `INET6`. After such an alter, there is no a need to use `INET6_ATON()` and `INET6_NTOA()`. Addresses can be inserted and retrieved directly.
{% endtab %}

{% tab title="< 10.5" %}
You may use [BINARY(16)](binary.md) as a storage for IPv6 internet addresses, in combination with [INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) and [INET6\_NTOA](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_ntoa.md) to respectively insert and retrieve data.
{% endtab %}
{% endtabs %}

It is also possible to convert `INET6` columns to `BINARY(16)` and continue using the data in combination with `INET6_NTOA()` and `INET6_ATON()`.

## Examples

```sql
CREATE TABLE t1 (a INET6);
```

Inserting using short text address notation:

```sql
INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');
```

Long text address notation:

```sql
INSERT INTO t1 VALUES ('2001:0db8:0000:0000:0000:ff00:0042:8329');
```

16-byte binary string notation:

```sql
INSERT INTO t1 VALUES (0x20010DB8000000000000FF0000428329);
INSERT INTO t1 VALUES (UNHEX('20010DB8000000000000FF0000428329'));
```

IPv4 addresses, using IPv4-mapped and IPv4-compatible notations:

```sql
INSERT INTO t1 VALUES ('::ffff:192.0.2.128'); -- mapped
INSERT INTO t1 VALUES ('::192.0.2.128'); -- compatible
```

```sql
SELECT * FROM t1;
+------------------------+
| a                      |
+------------------------+
| 2001:db8::ff00:42:8329 |
| 2001:db8::ff00:42:8329 |
| 2001:db8::ff00:42:8329 |
| 2001:db8::ff00:42:8329 |
| ::ffff:192.0.2.128     |
| ::192.0.2.128          |
+------------------------+
```

IPv4 mapped (or compatible) values still occupy 16 bytes:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

INSERT INTO t1 VALUES ('::ffff:192.0.2.128');

SELECT * FROM t1;
+--------------------+
| a                  |
+--------------------+
| ::ffff:192.0.2.128 |
+--------------------+

SELECT HEX(a) FROM t1;
+----------------------------------+
| HEX(a)                           |
+----------------------------------+
| 00000000000000000000FFFFC0000280 |
+----------------------------------+
```

Casting from `INET6` to anything other than [CHAR](char.md) returns an error:

```sql
SELECT CAST(a AS DECIMAL) FROM t1;

ERROR 4079 (HY000): Illegal parameter data type inet6 for operation 'decimal_typecast'
```

### Comparison Examples

Comparison with another `INET6` expression:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);
    CREATE OR REPLACE TABLE t2 (a INET6);

    INSERT INTO t1 VALUES ('2001:db8::ff00:42:8328'),('2001:db8::ff00:42:8329');
    INSERT INTO t2 VALUES ('2001:db8::ff00:42:832a'),('2001:db8::ff00:42:8329');

    SELECT t1.* FROM t1,t2 WHERE t1.a=t2.a;
    +------------------------+
    | a                      |
    +------------------------+
    | 2001:db8::ff00:42:8329 |
    +------------------------+
```

With a character string expression with a text (short or long) address representation:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

    INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');

    SELECT * FROM t1 WHERE a='2001:db8::ff00:42:8329';
    +------------------------+
    | a                      |
    +------------------------+
    | 2001:db8::ff00:42:8329 |
    +------------------------+
```

With a 16-byte binary string expression:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

    INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');

    SELECT * FROM t1 WHERE a=X'20010DB8000000000000FF0000428329';
    +------------------------+
    | a                      |
    +------------------------+
    | 2001:db8::ff00:42:8329 |
    +------------------------+
```

With an expression of another data type:

```sql
SELECT * FROM t1 WHERE a=1;
ERROR 4078 (HY000): Illegal parameter data types inet6 and int for operation '='
```

### Mixing for Result Examples

Mixed with another `INET6` expression, returning an `INET6` data type:

```sql
CREATE OR REPLACE TABLE t1 (a INET6, b INET6);

    INSERT INTO t1 VALUES (NULL,'2001:db8::ff00:42:8329');

    SELECT a FROM t1 UNION SELECT b FROM t1;
    +------------------------+
    | a                      |
    +------------------------+
    | NULL                   |
    | 2001:db8::ff00:42:8329 |
    +------------------------+

    SELECT COALESCE(a, b) FROM t1;
    +------------------------+
    | COALESCE(a, b)         |
    +------------------------+
    | 2001:db8::ff00:42:8329 |
    +------------------------+
```

Mixed with a character string in text (short or long) address representation:

```sql
CREATE OR REPLACE TABLE t1 (a INET6, b VARCHAR(64));

    INSERT INTO t1 VALUES (NULL,'2001:db8::ff00:42:8328');

    INSERT INTO t1 VALUES (NULL,'2001:db8::ff00:42:832a garbage');

    SELECT COALESCE(a,b) FROM t1;
    +------------------------+
    | COALESCE(a,b)          |
    +------------------------+
    | 2001:db8::ff00:42:8328 |
    | NULL                   |
    +------------------------+
    2 rows in set, 1 warning (0.001 sec)

    SHOW WARNINGS;
    +---------+------+---------------------------------------------------------+
    | Level   | Code | Message                                                 |
    +---------+------+---------------------------------------------------------+
    | Warning | 1292 | Incorrect inet6 value: '2001:db8::ff00:42:832a garbage' |
    +---------+------+---------------------------------------------------------+
```

Mixed with a 16-byte binary string:

```sql
CREATE OR REPLACE TABLE t1 (a INET6, b VARBINARY(16));

    INSERT INTO t1 VALUES (NULL,CONCAT(0xFFFF,REPEAT(0x0000,6),0xFFFF));

    INSERT INTO t1 VALUES (NULL,0x00/*garbage*/);

    SELECT COALESCE(a,b) FROM t1;
    +---------------+
    | COALESCE(a,b) |
    +---------------+
    | ffff::ffff    |
    | NULL          |
    +---------------+
    2 rows in set, 1 warning (0.001 sec)

    SHOW WARNINGS;
    +---------+------+-------------------------------+
    | Level   | Code | Message                       |
    +---------+------+-------------------------------+
    | Warning | 1292 | Incorrect inet6 value: '\x00' |
    +---------+------+-------------------------------+
```

Mixing with other data types:

```sql
SELECT CAST('ffff::ffff' AS INET6) UNION SELECT 1;
ERROR 4078 (HY000): Illegal parameter data types inet6 and int for operation 'UNION'
```

### Functions and Operators Examples

[HEX](../../sql-functions/string-functions/hex.md) with an `INET6` argument returning a hexadecimal representation:

```sql
SELECT HEX(CAST('2001:db8::ff00:42:8329' AS INET6));
    +----------------------------------------------+
    | HEX(CAST('2001:db8::ff00:42:8329' AS INET6)) |
    +----------------------------------------------+
    | 20010DB8000000000000FF0000428329             |
    +----------------------------------------------+
```

[INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) now understands `INET6` values as an argument:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

    INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');

    SELECT a, HEX(INET6_ATON(a)) FROM t1;
    +------------------------+----------------------------------+
    | a                      | HEX(INET6_ATON(a))               |
    +------------------------+----------------------------------+
    | 2001:db8::ff00:42:8329 | 20010DB8000000000000FF0000428329 |
    +------------------------+----------------------------------+
```

[IS\_IPV4\_COMPAT](../../sql-functions/secondary-functions/miscellaneous-functions/is_ipv4_compat.md) and [IS\_IPV4\_MAPPED](../../sql-functions/secondary-functions/miscellaneous-functions/is_ipv4_mapped.md) prototype now `a BINARY(16))`:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

    INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');
    INSERT INTO t1 VALUES ('::ffff:192.168.0.1');
    INSERT INTO t1 VALUES ('::192.168.0.1');

    SELECT a, IS_IPV4_MAPPED(a), IS_IPV4_COMPAT(a) FROM t1;
    +------------------------+-------------------+-------------------+
    | a                      | IS_IPV4_MAPPED(a) | IS_IPV4_COMPAT(a) |
    +------------------------+-------------------+-------------------+
    | 2001:db8::ff00:42:8329 |                 0 |                 0 |
    | ::ffff:192.168.0.1     |                 1 |                 0 |
    | ::192.168.0.1          |                 0 |                 1 |
    +------------------------+-------------------+-------------------+
```

Automatic implicit `CAST` to `INET6`:

```sql
CREATE OR REPLACE TABLE t1 (
      a INET6,
      b VARCHAR(39) DEFAULT a
    );

    INSERT INTO t1 (a) VALUES ('ffff::ffff'),('::ffff:192.168.0.1');

    SELECT a, IS_IPV4_MAPPED(a), b, IS_IPV4_MAPPED(b) FROM t1;
    +--------------------+-------------------+--------------------+-------------------+
    | a                  | IS_IPV4_MAPPED(a) | b                  | IS_IPV4_MAPPED(b) |
    +--------------------+-------------------+--------------------+-------------------+
    | ffff::ffff         |                 0 | ffff::ffff         |                 0 |
    | ::ffff:192.168.0.1 |                 1 | ::ffff:192.168.0.1 |                 1 |
    +--------------------+-------------------+--------------------+-------------------+

    CREATE OR REPLACE TABLE t1 (
      a INET6,
      b BINARY(16) DEFAULT UNHEX(HEX(a))
    );

    INSERT INTO t1 (a) VALUES ('ffff::ffff'),('::ffff:192.168.0.1');

    SELECT a, IS_IPV4_MAPPED(a), HEX(b), IS_IPV4_MAPPED(b) FROM t1;
    +--------------------+-------------------+----------------------------------+-------------------+
    | a                  | IS_IPV4_MAPPED(a) | HEX(b)                           | IS_IPV4_MAPPED(b) |
    +--------------------+-------------------+----------------------------------+-------------------+
    | ffff::ffff         |                 0 | FFFF000000000000000000000000FFFF |                 0 |
    | ::ffff:192.168.0.1 |                 1 | 00000000000000000000FFFFC0A80001 |                 1 |
    +--------------------+-------------------+----------------------------------+-------------------+
```

### Prepared Statement Parameters Examples

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

EXECUTE IMMEDIATE 'INSERT INTO t1 VALUES (?)' USING 'ffff::fffe';
EXECUTE IMMEDIATE 'INSERT INTO t1 VALUES (?)' USING X'FFFF000000000000000000000000FFFF';

SELECT * FROM t1;
+------------+
| a          |
+------------+
| ffff::fffe |
| ffff::ffff |
+------------+

EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING 'ffff::fffe';
+------------+
| a          |
+------------+
| ffff::fffe |
+------------+

EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING X'FFFF000000000000000000000000FFFF';
+------------+
| a          |
+------------+
| ffff::ffff |
+------------+
```

### Migration between BINARY(16) and INET6 Examples

{% tabs %}
{% tab title="Current" %}
```sql
CREATE OR REPLACE TABLE t1 (a BINARY(16));

INSERT INTO t1 VALUES (INET6_ATON('ffff::ffff'));

SELECT INET6_NTOA(a) FROM t1;
+---------------+
| INET6_NTOA(a) |
+---------------+
| ffff::ffff    |
+---------------+
```

Migrating to `INET6`:

```sql
ALTER TABLE t1 MODIFY a INET6;

INSERT INTO t1 VALUES ('ffff::fffe');

SELECT * FROM t1;
+------------+
| a          |
+------------+
| ffff::ffff |
| ffff::fffe |
+------------+
```
{% endtab %}

{% tab title="< 10.5" %}
There's no conversion you can use:

```sql
CREATE OR REPLACE TABLE t1 (a BINARY(16));

INSERT INTO t1 VALUES (INET6_ATON('ffff::ffff'));

SELECT INET6_NTOA(a) FROM t1;
+---------------+
| INET6_NTOA(a) |
+---------------+
| ffff::ffff    |
+---------------+
```
{% endtab %}
{% endtabs %}

Migration from `INET6` to `BINARY(16)`:

```sql
CREATE OR REPLACE TABLE t1 (a INET6);

INSERT INTO t1 VALUES ('2001:db8::ff00:42:8329');
INSERT INTO t1 VALUES ('::ffff:192.168.0.1');
INSERT INTO t1 VALUES ('::192.168.0.1');

ALTER TABLE t1 MODIFY a BINARY(16);

SELECT INET6_NTOA(a) FROM t1;
+------------------------+
| INET6_NTOA(a)          |
+------------------------+
| 2001:db8::ff00:42:8329 |
| ::ffff:192.168.0.1     |
| ::192.168.0.1          |
+------------------------+
```

### Casting from INET4 to INET6

{% tabs %}
{% tab title="Current" %}
Casting from [INET4](inet4.md) data types to `INET6` is permitted, allowing `INET4` values to be inserted into `INET6` columns.

```sql
CREATE TABLE t1 (a INET6);

INSERT INTO t1 VALUES('0.0.0.0'), ('255.10.0.0'), ('255.255.255.255');
Query OK, 3 rows affected (0.027 sec)
```
{% endtab %}

{% tab title="< 11.3" %}
Casting from [INET4](inet4.md) data types to `INET6` is **not** permitted. You get an error if you try:

```
CREATE TABLE t1 (a INET6);

INSERT INTO t1 VALUES('0.0.0.0'), ('255.10.0.0'), ('255.255.255.255');
ERROR 1292 (22007): Incorrect inet6 value: '0.0.0.0' for column `test`.`t1`.`a` at row 1
```
{% endtab %}
{% endtabs %}

## See Also

* [IS\_IPV6](../../sql-functions/secondary-functions/miscellaneous-functions/is_ipv6.md)
* [INET6\_ATON](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md)
* [INET6\_NTOA](../../sql-functions/secondary-functions/miscellaneous-functions/inet6_ntoa.md)
* [Working with IPv6 in MariaDB - the INET6 datatype](https://www.youtube.com/watch?v=1zNOGGgUnlQ) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
