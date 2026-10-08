---
description: >-
  Delete a tablespace. This command removes the physical file container used for
  storing table data, applicable to engines like InnoDB or NDB.
---

# DROP TABLESPACE

{% hint style="info" %}
The `DROP TABLESPACE` statement is not supported by MariaDB. It was originally inherited from MySQL NDB Cluster. In MySQL 5.7 and later, the statement is also supported for InnoDB. However, MariaDB has chosen not to include that specific feature. See [MDEV-19294](https://jira.mariadb.org/browse/MDEV-19294) for more information.
{% endhint %}

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
