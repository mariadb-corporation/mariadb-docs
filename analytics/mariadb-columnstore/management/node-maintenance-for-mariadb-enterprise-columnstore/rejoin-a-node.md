---
description: >-
  Rejoin a node to a MariaDB Enterprise ColumnStore cluster through MaxScale's
  REST API, calling the mariadbmon module's rejoin command via MaxCtrl or
  another REST client.
---

# Rejoining a Node

To rejoin a node with Enterprise ColumnStore, perform the following procedure.

## Performing Rejoin in MaxScale

The node can be configured to rejoin in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client.
* Call a module command using the `call command` command.
* As the first argument, provide the name for the module, which is [mariadbmon](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/mariadb-monitor).
* As the second argument, provide the module command, which is `rejoin` .
* As the third argument, provide the name of the monitor.
* As the fourth argument, provide the name of the server.

For example:

```bash
maxctrl call command \
   mariadbmon \
   rejoin \
   mcs_monitor \
   mcs3
```

## Checking Replication Status with MaxScale

MaxScale is capable of checking the status of [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* List the servers using the `list servers` command, like this:

```bash
maxctrl list servers
```

If the node properly rejoined, the `State` column of the node shows `Slave, Running`.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
