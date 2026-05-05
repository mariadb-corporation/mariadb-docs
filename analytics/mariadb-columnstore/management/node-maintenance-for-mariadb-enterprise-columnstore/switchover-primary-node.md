---
description: >-
  Switch the primary node in a MariaDB Enterprise ColumnStore cluster by
  calling the mariadbmon switchover command in MaxScale via maxctrl or another
  REST client.
---

# Switchover of the Primary Node

To switchover to a new primary node with Enterprise ColumnStore, perform the following procedure.

## Performing Switchover in MaxScale

The primary node can be switched in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client.
* Call a module command using the `call command` command.
* As the first argument, provide the name for the module, which is [mariadbmon](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/mariadb-monitor).
* As the second argument, provide the module command, which is `switchover` .
* As the third argument, provide the name of the monitor.

For example:

```bash
maxctrl call command \
   mariadbmon \
   switchover \
   mcs_monitor
```

With the above syntax, MaxScale will choose the most up-to-date replica to be the new primary.

If you want to manually select a new primary, provide the server name of the new primary as the fourth argument:

```bash
maxctrl call command \
   mariadbmon \
   switchover \
   mcs_monitor \
   mcs2
```

## Checking the Replication Status with MaxScale

MaxScale is capable of checking the status of [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* List the servers using the `list servers` command, like this:

```bash
maxctrl list servers
```

If switchover was properly performed, the `State` column of the new primary shows `Master, Running`.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
