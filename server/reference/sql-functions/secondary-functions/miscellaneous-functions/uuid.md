---
description: >-
  Generate a Universally Unique Identifier (v1). This function returns a
  standard 128-bit UUID as a 36-character string with hyphens.
---

# UUID

## Syntax

```sql
UUID()
```

## Description

Returns a Universally Unique Identifier (UUID) version 1. Functions to generate v4 and v7 UUIDs are available from [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117). See [UUIDv4](uuid_v4.md) and [UUIDv7](uuid_v7.md) respectively.

A UUID is designed as a number that is globally unique in space and time. Two calls to `UUID()` are expected to generate two different values, even if these calls are performed on two separate computers that are not connected to each other.

UUID() results are intended to be unique, but cannot always be relied upon to be unpredictable and unguessable.

A UUID is a 128-bit number represented by a utf8 string of five hexadecimal numbers in `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee` format:

* The first three numbers are generated from a timestamp.
* The fourth number preserves temporal uniqueness in case the timestamp value\
  loses monotonicity (for example, due to daylight saving time).
* The fifth number is an IEEE 802 node number that provides spatial uniqueness.\
  A random number is substituted if the latter is not available (for example,\
  because the host computer has no Ethernet card, or we do not know how to find\
  the hardware address of an interface on your operating system). In this case,\
  spatial uniqueness cannot be guaranteed. Nevertheless, a collision should\
  have very low probability.

Currently, the MAC address of an interface is taken into account only on FreeBSD and Linux. On other operating systems, MariaDB uses a randomly generated 48-bit number.

Statements using the UUID() function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

The function generates a UUIDv1 and the results are generated according to the "DCE 1.1:Remote Procedure Call" (Appendix A) CAE (Common Applications Environment) Specifications published by The Open Group in October 1997 ([Document Number C706](https://www.opengroup.org/public/pubs/catalog/c706.htm)).

## Examples

```sql
SELECT UUID();
+--------------------------------------+
| UUID()                               |
+--------------------------------------+
| cd41294a-afb0-11df-bc9b-00241dd75637 |
+--------------------------------------+
```

## See Also

* [UUIDv4](uuid_v4.md)
* [UUIDv7](uuid_v7.md)
* [UUID\_SHORT()](uuid_short.md) - Return short (64 bit) Universal Unique Identifier
* [SYS\_GUID](sys_guid.md) - UUID without the `-` character for Oracle compatibility
* [UUID data type](../../../data-types/string-data-types/uuid-data-type.md)
* [MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339) (Support UUID v4 generation)
* [MDEV-32637](https://jira.mariadb.org/browse/MDEV-32637) (Implement native UUID7 function)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
