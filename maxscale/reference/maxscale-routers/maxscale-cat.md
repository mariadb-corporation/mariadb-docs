# MaxScale Cat

## Cat

The `cat` router is a special router that concatenates result sets.

_Note:_ This module is experimental and must be built from source. The
module is deprecated in MaxScale 23.08 and might be removed in a future
release.

### Configuration

The router has no special parameters. To use it, define a service with`router=cat` and add the servers you want to use.

### Behavior

The order the servers are defined in is the order in which the servers are
queried. This means that the results are ordered based on the `servers`
parameter of the service. The result will only be completed once all servers
have executed this.

All commands executed via this router will be executed on all servers. This
means that an INSERT through the `cat` router will send it to all servers. In
the case of commands that do not return resultsets, the response of the last
server is sent to the client. This means that if one of the earlier servers
returns a different result, the client will not see it.

As the intended use-case of the router is to mainly reduce multiple result sets
into one, it has no mechanisms to prevent writes from being executed on slave
servers (which would cause data corruption or replication failure). Take great
care when performing administrative operations though this router.

If a connection to one of the servers is lost, the client connection will also
be closed.

### Example

Here is a simple example service definition that uses the servers from the [Configuring Servers](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-configuring-servers.md) tutorial and the
credentials from the [MaxScale Tutorial](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md).

```
[concat-service]
type=service
router=cat
servers=dbserv1,dbserv2,dbserv3
user=maxscale
password=maxscale_pw
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
