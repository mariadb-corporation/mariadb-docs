# Connection Routing with MariaDB MaxScale

The goal of this tutorial is to configure a system that has two ports available, one for
write connections and another for read connections. The read connections are load-
balanced across replica servers.

### Setting up MariaDB MaxScale

This tutorial is a part of the [MariaDB MaxScale Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md).
Please read it and follow the instructions. Return here once basic setup is complete.

### Configuring services

We want two services and ports to which the client application can connect. One service
routes client connections to the primary server, the other load balances between replica
servers. To achieve this, we need to define two services in the configuration file.

Create the following two sections in your configuration file. The section names are the
names of the services and should be meaningful. For this tutorial, we use the name&#x73;_&#x57;rite-Service_ and _Read-Service_.

```ini
[Write-Service]
type=service
router=readconnroute
router_options=master
servers=dbserv1, dbserv2, dbserv3
user=maxscale
password=maxscale_pw

[Read-Service]
type=service
router=readconnroute
router_options=slave
servers=dbserv1, dbserv2, dbserv3
user=maxscale
password=maxscale_pw
```

_router_ defines the routing module used. Here we use _readconnroute_ for
connection-level routing.

A service needs a list of servers to route queries to. The server names must
match the names of server sections in the configuration file and not the hostnames or
addresses of the servers.

The _router\_options_-parameter tells the _readconnroute_-module which servers it should
route a client connection to. For the write service we use the `master`-type and for the
read service the `slave`-type.

The _user_ and _password_ parameters define the credentials the service uses to populate
user authentication data. These users were created at the start of the [MaxScale Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md).

For increased security, see [password encryption](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-encrypting-passwords.md).

### Configuring the Listener

To allow network connections to a service, a network ports must be associated with it.
This is done by creating a separate listener section in the configuration file. A service
may have multiple listeners but for this tutorial one per service is enough.

```ini
[Write-Listener]
type=listener
service=Write-Service
port=3306

[Read-Listener]
type=listener
service=Read-Service
port=3307
```

The _service_ parameter tells which service the listener connects to. For th&#x65;_&#x57;rite-Listener_ we set it to _Write-Service_ and for the _Read-Listener_ we set
it to _Read-Service_.

A listener must define the network port to listen on.

The optional _address_-parameter defines the local address the listener should bind to.
This may be required when the host machine has multiple network interfaces. The
default behavior is to listen on all network interfaces (the IPv6 address `::`).

### Starting MariaDB MaxScale

For the last steps, please return to [MaxScale Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-setting-up-mariadb-maxscale.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
