---
description: >-
  The online_alter_log plugin provides logging capabilities for online ALTER
  TABLE operations, helping administrators monitor and debug schema changes.
---

# online\_alter\_log

{% hint style="info" %}
This plugin is for internal use only.
{% endhint %}

This plugin represents the online alter log in a transaction. It is used to commit transactions for tables while an online `ALTER TABLE` query is running.

It is built in the server, and is always enabled.

See the [Online Schema Change](../../sql-statements/data-definition/alter/alter-table/online-schema-change.md) page for functionality details.

For plugin version and maturity level, see [this page](../information-on-plugins/list-of-plugins.md).
