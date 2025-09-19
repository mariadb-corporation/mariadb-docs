# Configuring Servers

The first step is to define the servers that make up the cluster. These servers will be used by the services and are monitored by the monitor.

```ini
[dbserv1]
type=server
address=192.168.2.1
port=3306

[dbserv2]
type=server
address=192.168.2.2
port=3306

[dbserv3]
type=server
address=192.168.2.3
port=3306
```

The `address` and `port` parameters tell where the server is located.

### Enabling TLS

To enable encryption for the MaxScale-to-MariaDB communication, add `ssl=true`
to the server section. To enable server certificate verification, add`ssl_verify_peer_certificate=true`.

The `ssl` and `ssl_verify_peer_certificate` parameters are similar to the`--ssl` and `--ssl-verify-server-cert` options of the `mysql` command line
client.

For more information about TLS, refer to the [Configuration Guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
