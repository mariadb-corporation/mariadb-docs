---
description: >-
  IPv4 address data type. Stores IPv4 addresses as 4-byte binary strings for
  efficient storage and retrieval.
---

# INET4

{% hint style="info" %}
INET4 is available from MariaDB 10.10.
{% endhint %}

## Syntax

```sql
INET4
```

## Description

`INET4` is a data type to store IPv4 addresses, as 4-byte binary strings.

{% tabs %}
{% tab title="Current" %}
Casting from [INET4](inet4.md) data types to `INET6` is permitted, allowing for example comparisons between the two data types, and for `INET4` values to be inserted into `INET6` columns.
{% endtab %}

{% tab title="< 11.3" %}
Casting from [INET4](inet4.md) data types to `INET6` is **not** permitted.
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE OR REPLACE TABLE t1 (a INET4);

INSERT INTO t1 VALUES('0.0.0.0'), ('255.10.0.0'), ('255.255.255.255');

INSERT INTO t1 VALUES (0xa0000001);
INSERT INTO t1 VALUES (0xf0000000);
INSERT INTO t1 VALUES (0xff000001);

SELECT HEX(a), a FROM t1 ORDER BY a;
+----------+-----------------+
| HEX(a)   | a               |
+----------+-----------------+
| 00000000 | 0.0.0.0         |
| A0000001 | 160.0.0.1       |
| F0000000 | 240.0.0.0       |
| FF000001 | 255.0.0.1       |
| FF0A0000 | 255.10.0.0      |
| FFFFFFFF | 255.255.255.255 |
+----------+-----------------+
```

Casting from `INET4` to [INET6](inet6.md) is permitted, allowing direct inserts.

{% tabs %}
{% tab title="Current" %}
```sql
CREATE TABLE t1 (a INET6);

INSERT INTO t1 VALUES('0.0.0.0'), ('255.10.0.0'), ('255.255.255.255');
Query OK, 3 rows affected (0.027 sec)
```

Comparisons are also permitted:

```sql
CREATE OR REPLACE TABLE t1 (i4 INET4, i6 INET6); 
INSERT INTO t1 VALUES('10.10.10.10','::ffff:192.168.0.1');

SELECT LEAST(i4,i6) FROM t1;
+--------------------+
| LEAST(i4,i6)       |
+--------------------+
| ::ffff:10.10.10.10 |
+--------------------+
```
{% endtab %}

{% tab title="< 11.3" %}
```sql
CREATE TABLE t1 (a INET6);

INSERT INTO t1 VALUES('0.0.0.0'), ('255.10.0.0'), ('255.255.255.255');
ERROR 1292 (22007): Incorrect inet6 value: '0.0.0.0' for column `test`.`t1`.`a` at row 1
```
{% endtab %}
{% endtabs %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
