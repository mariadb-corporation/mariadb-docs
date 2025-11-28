# Read-Write Splitting

The goal of this tutorial is to configure a system that appears to the client as a single
database. MariaDB MaxScale will split the statements such that write statements are sent
to the primary server and read statements are balanced across the replica servers.

### Setting up MariaDB MaxScale

This tutorial is a part of [MariaDB MaxScale Tutorial](setting-up-mariadb-maxscale.md).
Please read it and follow the instructions. Return here once basic setup is complete.

### Configuring the service

After configuring the servers and the monitor, we create a read-write-splitter service configuration. Create the following section in your configuration file. The section name is also the name of the service and should be meaningful. For this tutorial, we use the name _Splitter-Service_.

```ini
[Splitter-Service]
type=service
router=readwritesplit
servers=dbserv1, dbserv2, dbserv3
user=maxscale
password=maxscale_pw
```

_router_ defines the routing module used. Here we use _readwritesplit_ for query-level read-write-splitting.

A service needs a list of servers where queries will be routed to. The server names must
match the names of server sections in the configuration file and not the hostnames or
addresses of the servers.

The _user_ and _password_ parameters define the credentials the service uses to populate
user authentication data. These users were created at the start of the [MaxScale Tutorial](setting-up-mariadb-maxscale.md).

For increased security, see [password encryption](encrypting-passwords.md).

### Configuring the Listener

To allow network connections to a service, a network ports must be associated with it. This is done by creating a separate listener section in the configuration file. A service may have multiple listeners but for this tutorial one is enough.

```ini
[Splitter-Listener]
type=listener
service=Splitter-Service
port=3306
```

The _service_ parameter tells which service the listener connects to. For the_Splitter-Listener_ we set it to _Splitter-Service_.

A listener must define the network port to listen on.

The optional _address_-parameter defines the local address the listener should bind to. This may be required when the host machine has multiple network interfaces. The default behavior is to listen on all network interfaces (the IPv6 address `::`).

### Starting MariaDB MaxScale

For the last steps, please return to [MaxScale Tutorial](setting-up-mariadb-maxscale.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
