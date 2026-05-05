---
description: >-
  Set a MariaDB Enterprise ColumnStore node to maintenance mode in MaxScale
  using the maxctrl set server command, taking the node out of read-write
  rotation.
---

# Setting a Node to Maintenance Mode

To set a node to maintenance mode with Enterprise ColumnStore, perform the following procedure.

## Setting the Server State in MaxScale

The server object for the node can be set to maintenance mode in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client.
* Set the server object to maintenance mode using the `set server` command.
* As the first argument, provide the name for the server.
* As the second argument, provide `maintenance` as the state.

For example:

```bash
maxctrl set server \
   mcs3 \
   maintenance
```

If the specified server is a primary server, then MaxScale will allow open transactions to complete before closing any connections.

If you would like MaxScale to immediately close all connections, the `--force` option can be provided as a third argument:

```bash
maxctrl set server \
   mcs3 \
   maintenance \
   --force
```

## Confirming Maintenance Mode is Set with MaxScale

Confirm the state of the server object in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* List the servers using the `list servers` command, like this:

```bash
maxctrl list servers
```

If the node is properly in maintenance mode, then the `State` column will show `Maintenance` as one of the states.

## Performing Maintenance

Now that the server is in maintenance mode in MaxScale, you can perform your maintenance.

While the server is in maintenance mode:

* MaxScale doesn't route traffic to the node.
* MaxScale doesn't select the node to be primary during failover.
* The node can be rebooted.
* The node's services can be restarted.

## Clear the Server State in MaxScale

Maintenance mode for the server object for the node can be cleared in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client.
* Clear the server object's state using the `clear server` command.
* As the first argument, provide the name for the server.
* As the second argument, provide `maintenance` as the state.

For example:

```bash
maxctrl clear server \
   mcs3 \
   maintenance
```

## Confirming Maintenance Mode is Cleared with MaxScale

Confirm the state of the server object in MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* List the servers using the `list servers` command, like this:

```bash
maxctrl list servers
```

If the node is no longer in maintenance mode, the `State` column no longer shows `Maintenance` as one of the states.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
