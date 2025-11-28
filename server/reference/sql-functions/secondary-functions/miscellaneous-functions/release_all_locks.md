---
description: >-
  Release all named locks held by the session. This function frees all
  user-level locks acquired with GET_LOCK() in the current connection.
---

# RELEASE\_ALL\_LOCKS

{% hint style="info" %}
`RELEASE_ALL_LOCKS` is available from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes).
{% endhint %}

## Syntax

```sql
RELEASE_ALL_LOCKS()
```

## Description

Releases all named locks held by the current session. Returns the number of locks released, or `0` if none were held.

Statements using the `RELEASE_ALL_LOCKS` function are [not safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
SELECT RELEASE_ALL_LOCKS();
+---------------------+
| RELEASE_ALL_LOCKS() | 
+---------------------+
|                   0 |
+---------------------+

SELECT GET_LOCK('lock1',10);
+----------------------+
| GET_LOCK('lock1',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT RELEASE_ALL_LOCKS();
+---------------------+
| RELEASE_ALL_LOCKS() | 
+---------------------+
|                   1 |
+---------------------+
```

## See Also

* [GET\_LOCK](get_lock.md)
* [IS\_FREE\_LOCK](is_free_lock.md)
* [IS\_USED\_LOCK](is_used_lock.md)
* [RELEASE\_LOCK](release_lock.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
