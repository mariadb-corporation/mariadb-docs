---
description: >-
  This table displays the configuration parameters used by the replica to
  connect to the primary server, such as host, port, and user credentials.
---

# Performance Schema replication\_applier\_configuration Table

{% hint style="info" %}
The `replication_applier_configuration` table is available from MariaDB 10.5.2.
{% endhint %}

The [Performance Schema](../) replication\_applier\_configuration table contains configuration settings affecting replica transactions.

It contains the following fields.

| Field          | Type     | Null | Description                                                           |
| -------------- | -------- | ---- | --------------------------------------------------------------------- |
| CHANNEL\_NAME  | char(64) | NO   | Replication channel name.                                             |
| DESIRED\_DELAY | int(11)  | NO   | Target number of seconds the replica should be delayed to the master. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
