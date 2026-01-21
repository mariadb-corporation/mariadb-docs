---
description: >-
  Check and correct a view's algorithm. This statement is primarily used by
  upgrade scripts to ensure view definitions are compatible.
---

# REPAIR VIEW

## Syntax

{% code overflow="wrap" %}
```sql
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] VIEW  view_name[, view_name] ... [FROM MYSQL]
```
{% endcode %}

## Description

The `REPAIR VIEW` statement checks whether the view algorithm is correct. It is run as part of [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md), and should not normally be required in regular use.

By default it corrects the checksum and if necessary adds the mariadb-version field. If the optional `FROM MYSQL` clause is used, and no mariadb-version field is present, the `MERGE` and `TEMPTABLE` algorithms are toggled.

By default, `REPAIR VIEW` statements are written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) and will be [replicated](../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.

## See Also

* [CHECK VIEW](check-view.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
