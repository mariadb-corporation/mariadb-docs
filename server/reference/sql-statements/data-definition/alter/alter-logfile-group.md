---
description: >-
  Understand the support status of this statement. Originally designed for NDB
  Cluster, it is not currently supported in MariaDB Server.
---

# ALTER LOGFILE GROUP

{% hint style="info" %}
The `ALTER LOGFILE GROUP` statement is not supported by MariaDB. It was originally inherited from MySQL NDB Cluster. See [MDEV-19295](https://jira.mariadb.org/browse/MDEV-19295) for more information.
{% endhint %}

## Syntax

```sql
ALTER LOGFILE GROUP logfile_group
    ADD UNDOFILE 'file_name'
    [INITIAL_SIZE [=] size]
    [WAIT]
    ENGINE [=] engine_name
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
