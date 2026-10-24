---
description: >-
  Duplicate query traffic to multiple targets. This filter sends a copy of
  incoming requests to a secondary service or server useful for testing and
  auditing.
---

# MaxScale Tee Filter

## Overview

The tee filter is a "plumbing" fitting in the MariaDB MaxScale filter toolkit. It can be used in a filter pipeline of a service to make copies of requests from the client and send the copies to another service within MariaDB MaxScale.

## Configuration

The configuration block for the TEE filter requires the minimal filter parameters in its section within the MaxScale configuration file. The service to send the duplicates to must be defined.

```
[DataMartFilter]
type=filter
module=tee
target=DataMart

[Data-Service]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=DataMartFilter
```

## Settings

The tee filter requires a mandatory parameter to define the service to replicate statements to and accepts a number of optional parameters.

### `target`

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none
* Description: Specifies the branch target, which is the service or server where queries will be replicated.

The target where the filter will duplicate all queries. The target can be either a service or a server. The duplicate connection that is created to this target will be referred to as the "branch target" in this document.

### `service`

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none
* Description: Specifies the service for which queries are replicated; deprecated in favor of the target parameter.

{% hint style="warning" %}
This parameter is deprecated and will be removed in a future release. This parameter can always be replaced with the `target` parameter.
{% endhint %}

The service where the filter will duplicate all queries. Both `target` and `service` cannot be defined.

### `match`

* Type: [regex](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern to include only queries that match it for processing or filtering.

What queries should be included.

```
match=/insert.*into.*order*/
```

### `exclude`

* Type: [regex](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern to exclude queries from processing or matching.

What queries should be excluded.

```
exclude=/select.*from.*t1/
```

### `options`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`
* Description: Does nothing and is deprecated, do not use.

This option does nothing and has been deprecated ([MXS-7684](https://jira.mariadb.org/browse/MXS-7684))

### `source`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits query replication to sessions that start from a specific client IP address.

The optional source parameter defines an address that is used to match against the address from which the client connection to MariaDB MaxScale originates. Only sessions that originate from this address will be replicated.

```
source=127.0.0.1
```

### `user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Restricts query replication to sessions initiated by a specific username.

The optional user parameter defines a user name that is used to match against the user from which the client connection to MariaDB MaxScale originates. Only sessions that are connected using this username are replicated.

```
user=john
```

### `sync`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Allows synchronous routing, ensuring queries are executed on both the main and branch targets before continuing; branch failures close the client connection.

Enable synchronous routing mode. When configured with `sync=true`, the filter will queue new queries until the response from both the main and the branch target has been received. This means that for `n` executed queries, `n - 1` queries are guaranteed to be synchronized. Adding one extra statement (e.g. `SELECT 1`) to a batch of statements guarantees that all previous SQL statements have been successfully executed on both targets.

In the synchronous routing mode, a failure of the branch target will cause the client session to be closed.

## Limitations

* All statements that are executed on the branch target are done in an asynchronous manner. This means that when the client receives the response there is no guarantee that the statement has completed on the branch target. The `sync` feature provides some synchronization guarantees that can be used to verify successful execution on both targets.

* Any errors on the branch target will cause the connection to it to be closed. If `target` is a service, it is up to the router to decide whether the connection is closed. For direct connections to servers, any network errors cause the connection to be closed. When the connection is closed, no new queries will be routed to the branch target.

* With `sync=true`, a failure of the branch target will cause the whole session to be closed.

* [MXS-7676](https://jira.mariadb.org/browse/MXS-7676): Even with `sync=false`, a slow branch target may cause MaxScale to throttle the amount of data read from the client to prevent an out-of-memory situation from happening.

## Module commands

Read [Module Commands](../maxscale-module-commands.md) documentation for details about module commands.

The tee filter supports the following module commands.

### `tee disable [FILTER]`

This command disables a tee filter instance. A disabled tee filter will not send any queries to the target service.

### `tee enable [FILTER]`

Enable a disabled tee filter. This resumes the sending of queries to the target service.

## Examples

### Example 1 - Replicate all inserts into the orders table

Assume an order processing system that has a table called orders. You also have another database server, the datamart server, that requires all inserts into orders to be replicated to it. Deletes and updates are not, however, required.

Set up a service in MariaDB MaxScale, called Orders, to communicate with the order processing system with the tee filter applied to it. Also set up a service to talk to the datamart server, using the DataMart service. The tee filter would have as its service entry the DataMart service, by adding a match parameter of "insert into orders" would then result in all requests being sent to the order processing system, and insert statements that include the orders table being additionally sent to the datamart server.

```
[Orders]
type=service
router=readconnroute
servers=server1, server2, server3, server4
user=massi
password=6628C50E07CCE1F0392EDEEB9D1203F3
filters=ReplicateOrders

[ReplicateOrders]
type=filter
module=tee
target=DataMart
match=insert[   ]*into[     ]*orders

[DataMart]
type=service
router=readconnroute
servers=datamartserver
user=massi
password=6628C50E07CCE1F0392EDEEB9D1203F3
filters=QLA-DataMart

[QLA-DataMart]
type=filter
module=qlafilter
options=/var/log/DataMart/InsertsLog

[Orders-Listener]
type=listener
target=Orders
port=4011

[DataMart-Listener]
type=listener
target=DataMart
port=4012
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
