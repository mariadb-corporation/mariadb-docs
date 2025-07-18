# CREATE SEQUENCE

## Syntax

```sql
CREATE [OR REPLACE] [TEMPORARY] SEQUENCE [IF NOT EXISTS] sequence_name
[AS { TINYINT | SMALLINT | |MEDIUMINT | INT | INTEGER | BIGINT } [SIGNED | UNSIGNED]]
[ INCREMENT [ BY | = ] number ]
[ MINVALUE [=] number | NO MINVALUE | NOMINVALUE ]
[ MAXVALUE [=] number | NO MAXVALUE | NOMAXVALUE ]
[ START [ WITH | = ] number ] 
[ CACHE [=] number | NOCACHE ] [ CYCLE | NOCYCLE] 
[table_options](../sql-statements/data-definition/create/create-table.md#table-options)
```

The options for `CREATE SEQUENCE` can be given in any order, optionally followed by `table_options`.

_`table_options`_ can be any of the normal table options in [CREATE TABLE](../../sql-statements/data-definition/create/create-table.md) — the most used ones are `ENGINE=...` and `COMMENT=`.

`NOMAXVALUE` and `NOMINVALUE` are there to allow one to create `SEQUENCE`s using the Oracle syntax.

## Description

`CREATE SEQUENCE` creates a sequence that generates new values when called with `NEXT VALUE FOR sequence_name`. It's an alternative to [AUTO INCREMENT](../../data-types/auto_increment.md) if you want to have more control of how the numbers are generated. As the `SEQUENCE` caches values (up to `CACHE`), it can in some cases be much faster than [AUTO INCREMENT](../../data-types/auto_increment.md). Another benefit is that you can access the last value generated by all used sequences, which solves one of the limitations with [LAST\_INSERT\_ID()](../../sql-functions/secondary-functions/information-functions/last_insert_id.md).

`CREATE SEQUENCE` requires the [CREATE privilege](../../sql-statements/account-management-sql-statements/grant.md).

[DROP SEQUENCE](drop-sequence.md) can be used to drop a sequence, and [ALTER SEQUENCE](alter-sequence.md) to change it.

### CREATE Options

#### AS

{% tabs %}
{% tab title="Current" %}
`INT` type, that is, one of [TINYINT](../../data-types/numeric-data-types/tinyint.md), [SMALLINT](../../data-types/numeric-data-types/smallint.md), [MEDIUMINT](../../data-types/numeric-data-types/mediumint.md), [INT](../../data-types/numeric-data-types/int.md), [INTEGER](../../data-types/numeric-data-types/integer.md), [BIGINT](../../data-types/numeric-data-types/bigint.md). Can be signed or unsigned. Maximum value is based on the data type. The use of `BIGINT UNSIGNED` with this option extends the possible maximum value from `9223372036854775806` to `18446744073709551614`. Default  is `BIGINT`.
{% endtab %}

{% tab title="< 11.5" %}
The `AS` option is not available.
{% endtab %}
{% endtabs %}

#### INCREMENT

Increment to use for values. May be negative. Setting an increment of `0` causes the sequence to use the value of the [auto\_increment\_increment](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable at the time of creation, which is always a positive number. (see [MDEV-16035](https://jira.mariadb.org/browse/MDEV-16035)). Default `1`.

#### MINVALUE

Minimum value for the sequence. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the parser permits much smaller numbers, such as `-9999999999999999999999999999`, but converts to the minimum permitted for the `INT` type, with a note. Default `1` if `INCREMENT` > `0` , and `-9223372036854775807` (or based on int type) if `INCREMENT` < `0`.

#### MAXVALUE

Maximum value for sequence. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the parser permits much larger numbers, such as `9999999999999999999999999999` used in Oracle examples, but converts to the maximum permitted for the `INT` type, with a note. Default `9223372036854775806` (or based on int type) if `INCREMENT` > `0` , and `-1` if `INCREMENT` < `0`.

#### START

First value the sequence will generate. Default `MINVALUE` if `INCREMENT` > `0`, and `MAX_VALUE` if `INCREMENT`< `0`.

#### CACHE / NOCACHE

Number of values that should be cached. `0` if no `CACHE`. The underlying table will be updated first time a new sequence number is generated and each time the cache runs out. Default `1000`. [FLUSH TABLES](../../sql-statements/administrative-sql-statements/flush-commands/flush.md), shutting down the server, etc. will discard the cached values, and the next sequence number generated will be according to what's stored in the Sequence object. In effect, this will discard the cached values.&#x20;

{% hint style="warning" %}
Note that setting the cache to `1` from `1000` can make inserts to tables using sequences for default values 2x slower and increase the binary log sizes up to 7x.
{% endhint %}

#### CYCLE / NOCYCLE

If `CYCLE` is used, then the sequence should start again from `MINVALUE` after it has run out of values. Default value is `NOCYCLE`.

### Constraints on Create Arguments

To be able to create a legal sequence, the following must hold:

* `MAXVALUE` >= start
* `MAXVALUE` > `MINVALUE`
* `START` >= `MINVALUE`
* `MAXVALUE` <= `9223372036854775806` (`LONGLONG_MAX`-1). From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the parser accepts values beyond this, and converts based on the int type.
* `MINVALUE` >= `-9223372036854775807` (`LONGLONG_MIN`+1). From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the parser accepts values beyond this, and converts based on the int type.

{% hint style="warning" %}
Note that sequences can't generate the maximum/minimum 64 bit number because of the constraint of`MINVALUE` and `MAXVALUE`.
{% endhint %}

### Atomic DDL

{% tabs %}
{% tab title="Current" %}
MariaDB supports [Atomic DDL](../../sql-statements/data-definition/atomic-ddl.md) and `CREATE SEQUENCE` is atomic.
{% endtab %}

{% tab title="< 10.6.1" %}
MariaDB does **not** support [Atomic DDL](../../sql-statements/data-definition/atomic-ddl.md) and `CREATE SEQUENCE` is atomic.
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;

CREATE SEQUENCE s2 START WITH -100 INCREMENT BY -10;
```

The following statement fails, as the increment conflicts with the defaults:

```sql
CREATE SEQUENCE s3 START WITH -100 INCREMENT BY 10;
ERROR 4082 (HY000): Sequence 'test.s3' values are conflicting
```

The sequence can be created by specifying workable minimum and maximum values:

```sql
CREATE SEQUENCE s3 START WITH -100 INCREMENT BY 10 MINVALUE=-100 MAXVALUE=1000;
```

From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115):

```sql
CREATE SEQUENCE s3 AS BIGINT UNSIGNED START WITH 10;
```

Parser accepting larger or smaller values:

```sql
CREATE OR REPLACE SEQUENCE s AS TINYINT SIGNED
  MINVALUE=-999999999999999999999999999999999
  MAXVALUE=999999999999999999999999999999999 
  START WITH 100 INCREMENT BY 10;
Query OK, 0 rows affected, 2 warnings (0.037 sec)

SHOW WARNINGS;
+-------+------+-----------------------------------------------+
| Level | Code | Message                                       |
+-------+------+-----------------------------------------------+
| Note  | 1292 | Truncated incorrect INTEGER value: 'MINVALUE' |
| Note  | 1292 | Truncated incorrect INTEGER value: 'MAXVALUE' |
+-------+------+-----------------------------------------------+

SELECT * FROM INFORMATION_SCHEMA.SEQUENCES\G
*************************** 1. row ***************************
       SEQUENCE_CATALOG: def
        SEQUENCE_SCHEMA: test
          SEQUENCE_NAME: s
              DATA_TYPE: tinyint
      NUMERIC_PRECISION: 8
NUMERIC_PRECISION_RADIX: 2
          NUMERIC_SCALE: 0
            START_VALUE: 100
          MINIMUM_VALUE: -127
          MAXIMUM_VALUE: 126
              INCREMENT: 10
           CYCLE_OPTION: 0
```

### Cache

Flushing the cache:

```sql
CREATE OR REPLACE SEQUENCE s START WITH 1 INCREMENT BY 1 MAXVALUE=10 CACHE=5;

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          1 |
+------------+

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          2 |
+------------+

FLUSH TABLES s;

SELECT NEXTVAL(s);
+------------+
| NEXTVAL(s) |
+------------+
|          6 |
+------------+

FLUSH TABLES s;

SELECT NEXTVAL(s);
ERROR 4084 (HY000): Sequence 'test.s' has run out
```

### Create table with a sequence as a default value

You can use sequences instead of `AUTO_INCREMENT` to generate values for a table:

```sql
CREATE SEQUENCE s1;
CREATE TABLE t1 (a INT PRIMARY KEY DEFAULT nextval(s1), b INT);
INSERT INTO t1 (b) VALUES(1);
SELINT * FROM t1;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
+---+------+
```

## See Also

* [Sequence Overview](sequence-overview.md)
* [ALTER SEQUENCE](alter-sequence.md)
* [DROP SEQUENCE](drop-sequence.md)
* [NEXT VALUE FOR](sequence-functions/next-value-for-sequence_name.md)
* [PREVIOUS VALUE FOR](sequence-functions/previous-value-for-sequence_name.md)
* [SETVAL()](sequence-functions/setval.md). Set next value for the sequence.
* [AUTO INCREMENT](../../data-types/auto_increment.md)
* [SHOW CREATE SEQUENCE](../../sql-statements/administrative-sql-statements/show/show-create-sequence.md)
* [Information Schema SEQUENCES Table](../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
