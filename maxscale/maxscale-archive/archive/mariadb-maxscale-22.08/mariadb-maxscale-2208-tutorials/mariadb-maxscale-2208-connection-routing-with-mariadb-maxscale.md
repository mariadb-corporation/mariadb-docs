# MaxScale 22.08 Connection Routing with MariaDB MaxScale

## Connection Routing with MariaDB MaxScale

## Connection Routing with MariaDB MaxScale

The goal of this tutorial is to configure a system that has two ports available, one for\
write connections and another for read connections. The read connections are load-\
balanced across slave servers.

### Setting up MariaDB MaxScale

This tutorial is a part of the [MariaDB MaxScale Tutorial](mariadb-maxscale-2208-setting-up-mariadb-maxscale.md).\
Please read it and follow the instructions. Return here once basic setup is complete.

### Configuring services

We want two services and ports to which the client application can connect. One service\
routes client connections to the master server, the other load balances between slave\
servers. To achieve this, we need to define two services in the configuration file.

Create the following two sections in your configuration file. The section names are the\
names of the services and should be meaningful. For this tutorial, we use the names_Write-Service_ and _Read-Service_.

```
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

_router_ defines the routing module used. Here we use _readconnroute_ for\
connection-level routing.

A service needs a list of servers to route queries to. The server names must\
match the names of server sections in the configuration file and not the hostnames or\
addresses of the servers.

The _router\_options_-parameter tells the _readconnroute_-module which servers it should\
route a client connection to. For the write service we use the _master_-type and for the\
read service the _slave_-type.

The _user_ and _password_ parameters define the credentials the service uses to populate\
user authentication data. These users were created at the start of the [MaxScale Tutorial](mariadb-maxscale-2208-setting-up-mariadb-maxscale.md).

For increased security, see [password encryption](mariadb-maxscale-2208-encrypting-passwords.md).

### Configuring the Listener

To allow network connections to a service, a network ports must be associated with it.\
This is done by creating a separate listener section in the configuration file. A service\
may have multiple listeners but for this tutorial one per service is enough.

```
[Write-Listener]
type=listener
service=Write-Service
port=3306

[Read-Listener]
type=listener
service=Read-Service
port=3307
```

The _service_ parameter tells which service the listener connects to. For the_Write-Listener_ we set it to _Write-Service_ and for the _Read-Listener_ we set\
it to _Read-Service_.

A listener must define the network port to listen on.

The optional _address_-parameter defines the local address the listener should bind to.\
This may be required when the host machine has multiple network interfaces. The\
default behavior is to listen on all network interfaces (the IPv6 address `::`).

### Starting MariaDB MaxScale

For the last steps, please return to [MaxScale Tutorial](mariadb-maxscale-2208-setting-up-mariadb-maxscale.md).

CC BY-SA / Gnu FDL
