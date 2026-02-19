---
title: InnoDB-based binlog from 12.3
---

{% if  %}
{% hint style="info" %}
From MariaDB 12.3, InnoDB-based binary logs can be used. (This is configurable, and not the default.)

If configured, binary logs are stored in InnoDB tablespaces, rather than binary files. This removes the need of protecting binary logs separately, since they'll "inherit" the same protection as other MariaDB database tables. Also, any other information about log **files** doesn't apply – for example, you cannot specify a storage location for binary logs stored in an InnoDB tablespace.

InnoDB-based binary logs are enabled by setting `binlog_storage_engine=innodb` in the server configuration. See [InnoDB-Based Binary Log](../../ha-and-performance/standard-replication/innodb-based-binary-log.md) for more information.
{% endhint %}
{% endif %}
