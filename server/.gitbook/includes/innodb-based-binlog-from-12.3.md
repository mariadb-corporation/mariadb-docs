---
title: InnoDB-based binlog from 12.3
---

{% if  %}
{% hint style="info" %}
From MariaDB 12.3, InnoDB-based binary logs can be used. (This is configurable, and not the default.)

If configured, binary logs are written to InnoDB-managed, page-structured files (with the `.ibb` extension) that are integrated with InnoDB's redo log and crash recovery, rather than the traditional flat binary log files. This removes the need to protect the binary log separately, since it "inherits" the same crash safety as other InnoDB data, and it removes the need for expensive two-phase commit between InnoDB transactions and the binary log. Some options that apply to traditional binary log files behave differently or no longer apply – for example, `sync_binlog` is effectively ignored.

InnoDB-based binary logs are enabled by setting `binlog_storage_engine=innodb` in the server configuration. See [InnoDB-Based Binary Log](../../ha-and-performance/standard-replication/innodb-based-binary-log.md) for more information.
{% endhint %}
{% endif %}
