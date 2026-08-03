---
description: >-
  The mysql.global_priv table stores global privileges and account properties
  for all users, replacing the older mysql.user table structure.
---

# mysql.global\_priv Table

The `mysql.global_priv` table contains information about users that have permission to access the MariaDB server, and their global privileges.

Note that the MariaDB privileges occur at many levels. A user may not be granted `CREATE` privilege at the user level, but may still have `CREATE` permission on certain tables or databases, for example. See [privileges](../../sql-statements/account-management-sql-statements/grant.md) for a more complete view of the MariaDB privilege system.

The `mysql.global_priv` table contains the following fields:

| Field | Type     | Null | Key | Default | Description                                                                |
| ----- | -------- | ---- | --- | ------- | -------------------------------------------------------------------------- |
| Host  | char(60) | NO   | PRI |         | Host (together with User makes up the unique identifier for this account). |
| User  | char(80) | NO   | PRI |         | User (together with Host makes up the unique identifier for this account). |
| Priv  | longtext | NO   |     |         | Global privileges, granted to the account and other account properties     |

From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2), in order to help the server understand which version a privilege record was written by, the `priv` field contains a new JSON field, `version_id` ([MDEV-21704](https://jira.mariadb.org/browse/MDEV-21704)).

From [MariaDB 13.1](https://jira.mariadb.org/browse/MDEV-14443), the `Priv` field also holds a `denies` array, recording the negative privileges created with [DENY](../../sql-statements/account-management-sql-statements/deny.md). Denies are stored here for every privilege level, not in `mysql.db`, `mysql.tables_priv`, or `mysql.columns_priv`. See [The denies Field](mysql-global_priv-table.md#the-denies-field).

## Examples

```sql
SELECT * FROM mysql.global_priv;
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Host      | User        | Priv                                                                                                                                  |
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| localhost | root        | {"access": 18446744073709551615,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"} |
| 127.%     | msandbox    | {"access":1073740799,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}            |
| localhost | msandbox    | {"access":1073740799,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}            |
| localhost | msandbox_rw | {"access":487487,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | msandbox_rw | {"access":487487,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | msandbox_ro | {"access":262145,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| localhost | msandbox_ro | {"access":262145,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | rsandbox    | {"access":524288,"plugin":"mysql_native_password","authentication_string":"*B07EB15A2E7BD9620DAE47B194D5B9DBA14377AD"}                |
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
```

Readable format:

```sql
SELECT CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv)) FROM mysql.global_priv;

+--------------------------------------------------------------------------------------+
| CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv))                                 |
+--------------------------------------------------------------------------------------+
| root@localhost => {
    "access": 18446744073709551615,
    "plugin": "mysql_native_password",
    "authentication_string": "*6C387FC3893DBA1E3BA155E74754DA6682D04747"
} |
| msandbox@127.% => {
    "access": 1073740799,
    "plugin": "mysql_native_password",
    "authentication_string": "*6C387FC3893DBA1E3BA155E74754DA6682D04747"
}           |
+--------------------------------------------------------------------------------------+
```

A particular user:

```sql
SELECT CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv)) FROM mysql.global_priv 
  WHERE user='marijn';
+--------------------------------------------------------------------------------------+
| CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv))                                 |
+--------------------------------------------------------------------------------------+
| marijn@localhost => {
    "access": 0,
    "plugin": "mysql_native_password",
    "authentication_string": "",
    "account_locked": true,
    "password_last_changed": 1558017158
} |
+--------------------------------------------------------------------------------------+
```

From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2):

```sql
GRANT FILE ON *.* TO user1@localhost;
SELECT Host, User, JSON_DETAILED(Priv) FROM mysql.global_priv WHERE user='user1'\G

*************************** 1. row ***************************
               Host: localhost
               User: user1
JSON_DETAILED(Priv): {
    "access": 512,
    "plugin": "mysql_native_password",
    "authentication_string": "",
    "password_last_changed": 1581070979,
    "version_id": 100502
}
```

## Mapping the `access` Field Values to Grants

The `access` field contains the grants of the user which can be mapped to individual grants with the following table. The most up-to-date information can be found in the `sql/privilege.h` file in the source code.

| Grant                 | Bit          |
| --------------------- | ------------ |
| SELECT                | (1UL << 0)   |
| INSERT                | (1UL << 1)   |
| UPDATE                | (1UL << 2)   |
| DELETE                | (1UL << 3)   |
| CREATE                | (1UL << 4)   |
| DROP                  | (1UL << 5)   |
| RELOAD                | (1UL << 6)   |
| SHUTDOWN              | (1UL << 7)   |
| PROCESS               | (1UL << 8)   |
| FILE                  | (1UL << 9)   |
| GRANT                 | (1UL << 10)  |
| REFERENCES            | (1UL << 11)  |
| INDEX                 | (1UL << 12)  |
| ALTER                 | (1UL << 13)  |
| SHOW\_DB              | (1UL << 14)  |
| SUPER                 | (1UL << 15)  |
| CREATE\_TMP           | (1UL << 16)  |
| LOCK\_TABLES          | (1UL << 17)  |
| EXECUTE               | (1UL << 18)  |
| REPL\_SLAVE           | (1UL << 19)  |
| BINLOG\_MONITOR       | (1UL << 20)  |
| CREATE\_VIEW          | (1UL << 21)  |
| SHOW\_VIEW            | (1UL << 22)  |
| CREATE\_PROC          | (1UL << 23)  |
| ALTER\_PROC           | (1UL << 24)  |
| CREATE\_USER          | (1UL << 25)  |
| EVENT                 | (1UL << 26)  |
| TRIGGER               | (1UL << 27)  |
| CREATE\_TABLESPACE    | (1UL << 28)  |
| DELETE\_HISTORY       | (1UL << 29)  |
| SET\_USER             | (1UL << 30)  |
| FEDERATED\_ADMIN      | (1UL << 31)  |
| CONNECTION\_ADMIN     | (1ULL << 32) |
| READ\_ONLY\_ADMIN     | (1ULL << 33) |
| REPL\_SLAVE\_ADMIN    | (1ULL << 34) |
| REPL\_MASTER\_ADMIN   | (1ULL << 35) |
| BINLOG\_ADMIN         | (1ULL << 36) |
| BINLOG\_REPLAY        | (1ULL << 37) |
| SLAVE\_MONITOR        | (1ULL << 38) |
| SHOW\_CREATE\_ROUTINE | (1ULL << 39) |

## The `denies` Field

From [MariaDB 13.1](https://jira.mariadb.org/browse/MDEV-14443), the `denies` array records the privileges that [DENY](../../sql-statements/account-management-sql-statements/deny.md) blocks for an account or role. Each element describes one privilege level:

```sql
DENY SELECT ON hr.* TO user1@localhost;
DENY SELECT (salary) ON hr.staff TO user1@localhost;
SELECT JSON_PRETTY(JSON_EXTRACT(Priv, '$.denies')) FROM mysql.global_priv
  WHERE User='user1'\G

*************************** 1. row ***************************
JSON_PRETTY(JSON_EXTRACT(Priv, '$.denies')): [
    {
        "type": "db",
        "db": "hr",
        "bits": 1
    },
    {
        "type": "column",
        "db": "hr",
        "table": "staff",
        "column": "salary",
        "bits": 1
    }
]
```

The fields of an element are:

| Field | Description |
| ----- | ----------- |
| `type` | The privilege level: `global`, `db`, `table`, `column`, `function`, `procedure`, `package`, or `package body`. |
| `db` | Database name. Absent for `global`. |
| `table` | Table name, for `table` and `column` entries. |
| `column` | Column name, for `column` entries. |
| `function`, `procedure`, `package`, `package body` | Routine name, named after the entry's `type`. |
| `bits` | The denied privileges, using the same bit values as the `access` field. |

An account with no denies has either no `denies` key or an empty array.

{% hint style="warning" %}
Do not edit the `denies` array with `UPDATE`. A malformed entry is skipped when privileges are loaded, with a `Malformed DENY entry in mysql.global_priv` warning written to the [error log](../../../server-management/server-monitoring-logs/error-log.md), which leaves the privilege allowed. Use `DENY` and `REVOKE DENY` instead.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
