---
description: >-
  Generate a short 64-bit UUID. This function returns a unique, monotonically
  increasing integer suitable for use as a compact identifier.
---

# UUID\_SHORT

## Syntax

```sql
UUID_SHORT()
```

## Description

Returns a "short" universally unique identifier as a 64-bit unsigned integer (rather than a string-form 128-bit identifier as returned by the [UUID()](uuid.md) function).

The value of `UUID_SHORT()` is guaranteed to be unique if the following conditions hold:

* The server\_id of the current host is unique among your set of master and replica servers.
* `server_id` is between 0 and 255.
* You don't set back your system time for your server between mariadbd restarts.
* You do not invoke `UUID_SHORT()` on average more than 16 million times per second between mariadbd restarts

The `UUID_SHORT()` return value is constructed this way:

```sql
(server_id & 255) << 56
+ (server_startup_time_in_seconds << 24)
+ incremented_variable++;
```

Statements using the UUID\_SHORT() function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
SELECT UUID_SHORT();
+-------------------+
| UUID_SHORT()      |
+-------------------+
| 21517162376069120 |
+-------------------+
```

```sql
CREATE TABLE t1 (a BIGINT UNSIGNED DEFAULT(uuid_short()) PRIMARY KEY);
INSERT INTO t1 VALUES(),();
SELECT * FROM t1;
+-------------------+
| a                 |
+-------------------+
| 98113699159474176 |
| 98113699159474177 |
+-------------------+
```

## See Also

* [UUID()](uuid.md) ; Return full (128 bit) Universally Unique Identifier
* [AUTO\_INCREMENT](../../../data-types/auto_increment.md)
* [Sequences](../../../sql-structure/sequences/) - an alternative to auto\_increment available from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)
* [SYS\_GUID](sys_guid.md) - UUID without the `-` character for Oracle compatibility
* [UUID data type](../../../data-types/string-data-types/uuid-data-type.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
