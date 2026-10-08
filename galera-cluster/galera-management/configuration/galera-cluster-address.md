---
description: >-
  Galera Cluster address format for wsrep_cluster_address: gcomm or dummy
  schema, a comma-separated member list or multicast address, optional port,
  and inline provider options.
---

# Galera Cluster Address

URLs in [Galera](https://mariadb.com/docs/galera-cluster) take a particular format:

```uri
<schema>://<cluster_address>[?option1=value1[&option2=value2]]
```

## Schema

* `gcomm`⁣- This is the option to use for a working implementation.
* `dummy`⁣- Used for running tests and profiling, does not do any actual replication, and all following parameters are ignored.

## Cluster address

* The cluster address shouldn't be empty like `gcomm://`. This should never be hardcoded into any configuration files.
* To connect the node to an existing cluster, the cluster address should contain the address of any member of the cluster you want to join.
* The cluster address can also contain a comma-separated list of multiple members of the cluster. It is good practice to list all possible members of the cluster, for example. ⁣`gcomm:<node1 name or ip>,<node2 name or ip2>,<node3 name or ip>` Alternately, if multicast is used, put the multicast address instead of the list of nodes. Each member address or multicast address can specify `<node name or ip>:<port>`if a non-default port is used.

## Option list

* The [wsrep\_provider\_options](../../reference/galera-cluster-system-variables.md#wsrep_provider_options) variable is used to set a [list of options](../../reference/wsrep-variable-details/wsrep_provider_options.md). These parameters can also be provided (and overridden) as part of the URL. Unlike options provided in a configuration file, they will not endure and need to be resubmitted with each connection.

A useful option to set is `pc.wait_prim=no`to ensure the server will start running even if it can't determine a primary node. This is useful if all members go down at the same time.

## Port

By default, gcomm listens on all interfaces. The port is either provided in the cluster address or will default to 4567 if not set.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
