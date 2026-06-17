---
title: InnoDB-based binlog from 12.3
---

{% if  %}
{% hint style="info" %}
From MariaDB 12.3, InnoDB-based binary logs can be used. (This is configurable, and not the default.)

If configured, binary logs are stored in InnoDB page-based tablespaces, rather than flat files. This removes the need for expensive two-phase commit between InnoDB transactions and the binary log.

InnoDB-based binary logs are enabled by setting `binlog_storage_engine=innodb` in the server configuration. See [InnoDB-Based Binary Log](../../ha-and-performance/standard-replication/innodb-based-binary-log.md) for more information.
{% endhint %}
{% endif %}
