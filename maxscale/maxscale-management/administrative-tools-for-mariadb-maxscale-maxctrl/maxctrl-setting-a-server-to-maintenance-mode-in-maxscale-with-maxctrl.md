# Setting a Server to Maintenance Mode in MaxScale with MaxCtrl

## Overview

When using MaxScale, it is often necessary to temporarily remove a server from the load balancing pool without actually shutting down the server. This is usually needed to perform maintenance on the server, such as when upgrading the server's software or when performing schema upgrades.

MaxScale allows users to set servers to "maintenance mode", which prevents MaxScale from routing traffic to the server and prevents it from being elected as the new primary server during failover or switchover.

MaxCtrl is a command-line utility that can perform administrative tasks using MaxScale's REST API. It can be used to set a server to maintenance mode.

## Setting a Server to Maintenance Mode

1. Configure the REST API if the default configuration is not sufficient.
2. Use MaxCtrl to execute the set server command with the maintenance option:

```bash
$ maxctrl --secure 
   --user=maxscale_rest_admin 
   --password=maxscale_rest_admin_password 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem 
   set server server1 maintenance
```

Replace `server1` with the name of the specific server.

3. If the specified server is a primary server, then MaxScale will allow open transactions to complete before closing any connections.

## Forcing a Server to Maintenance Mode

1. Use MaxCtrl to execute the set server command with the `maintenance --force` option:

```bash
$ maxctrl --secure 
   --user=maxscale_rest_admin 
   --password=maxscale_rest_admin_password 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem 
```

2. Replace `server1` with the specific server name. When `--force` is used, MaxScale immediately closes all connections, even if the server is a primary server with open transactions.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
