---
description: >-
  The Information Schema INNODB_MUTEXES table displays statistics about InnoDB
  mutex and read-write lock waits, helping to identify internal contention.
---

# Information Schema INNODB\_MUTEXES Table

The `INNODB_MUTEXES` table monitors mutex and rw locks waits. It has the following columns:

| Column       | Description                                         |
| ------------ | --------------------------------------------------- |
| NAME         | Name of the lock, as it appears in the source code. |
| CREATE\_FILE | File name of the mutex implementation.              |
| CREATE\_LINE | Line number of the mutex implementation.            |
| OS\_WAITS    | How many times the mutex occurred.                  |

The `CREATE_FILE` and `CREATE_LINE` columns depend on the InnoDB/XtraDB version.

{% tabs %}
{% tab title="Current" %}
The table provides information about all columns listed in the previous table.
{% endtab %}

{% tab title="< 10.2.2" %}
The table provides information about `rw_lock_t`, not about any mutexes.
{% endtab %}
{% endtabs %}

The [SHOW ENGINE INNODB STATUS](../../../../sql-statements/administrative-sql-statements/show/show-engine.md#show-engine-innodb-mutex) statement provides similar information.

## Examples

```sql
SELECT * FROM INNODB_MUTEXES;
+------------------------------+---------------------+-------------+----------+
| NAME                         | CREATE_FILE         | CREATE_LINE | OS_WAITS |
+------------------------------+---------------------+-------------+----------+
| &dict_sys->mutex             | dict0dict.cc        |         989 |        2 |
| &buf_pool->flush_state_mutex | buf0buf.cc          |        1388 |        1 |
| &log_sys->checkpoint_lock    | log0log.cc          |        1014 |        2 |
| &block->lock                 | combined buf0buf.cc |        1120 |        1 |
+------------------------------+---------------------+-------------+----------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
