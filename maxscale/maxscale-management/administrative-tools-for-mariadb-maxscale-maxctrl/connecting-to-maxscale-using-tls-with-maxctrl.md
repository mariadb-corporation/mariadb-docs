# Connecting to MaxScale using TLS with MaxCtrl

## Overview

[MaxCtrl](./) is a command-line utility that can perform administrative tasks using [MaxScale's REST API](broken-reference). It is possible to connect to MaxScale using TLS with MaxCtrl.

## Connecting to MaxScale using TLS

1. [Create a basic](creating-a-rest-api-user-for-maxscale-with-maxctrl.md#creating-a-basic-user) or [admin user](creating-a-rest-api-user-for-maxscale-with-maxctrl.md#creating-an-admin-user), depending on what kind of user you need:

```bash
$ maxctrl create user "maxscale_rest_admin" "maxscale_rest_admin_password" --type=admin
```

Replace maxscale\_rest\_admin and maxscale\_rest\_admin\_password with the desired user and password.

2. If you want to use MaxCtrl remotely, [configure the REST API for remote connections](../configuring-maxscales-rest-api.md#configuring-maxscales-rest-api-for-remote-connections).
   Several global parameters must be configured in maxscale.cnf.

| Parameter                                                                                                                                                                            | Description                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [admin\_host](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_host) | • This parameter defines the network address that the REST API listens on.• The default value is 127.0.0.1. |
| [admin\_port](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_port) | • This parameter defines the network port that the REST API listens on.• The default value is 8989.         |

For example:

```ini
[maxscale]
...
admin_host            = 0.0.0.0
admin_port            = 8443
```

3. [Enable TLS for MaxScale's REST API](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/data-in-transit-encryption-enabling-tls-on-mariadb-server).
   Several global parameters must be configured in maxscale.cnf.

| Parameter                                                                                                                                                                                            | Description                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [admin\_ssl\_key](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_key)          | \* This parameter defines the private key used by the REST API.                     |
| [admin\_ssl\_cert](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_cert)        | \* This parameter defines the certificate used by the REST API.                     |
| [admin\_ssl\_ca\_cert](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_ca_cert) | \*This parameter defines the CA certificate that signed the REST API's certificate. |

For example:

```ini
[maxscale]
...
admin_ssl_key=/certs/server-key.pem
admin_ssl_cert=/certs/server-cert.pem
admin_ssl_ca_cert=/certs/ca-cert.pem
```

4. Ensure that the client also has a TLS certificate, a private key, and the CA certificate.
5. Use [MaxCtrl](./) to connect with TLS:

```ini
$ maxctrl --secure 
   --user=maxscale_rest_admin 
   --password=maxscale_rest_admin_password 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem
```

Replace `maxscale_rest_admin` and `maxscale_rest_admin_password` with the actual user and password.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
