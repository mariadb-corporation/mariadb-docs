# Configuring MaxScale for MaxGUI

## Overview

[MaxGUI](./) is a graphical utility that can perform administrative tasks using [MaxScale's REST API](../../reference/maxscale-rest-api/). It is available starting in MaxScale 2.5. It supports many different operations.

[MaxGUI](./) is not available out-of-the box. MaxScale requires some configuration before [MaxGUI](./) can be used.

## Enabling MaxGUI

1. If you want to use MaxGUI remotely, [configure the REST API](../configuring-maxscales-rest-api.md#configuring-maxscales-rest-api-for-remote-connections) for remote connections.
   Several global parameters must be configured in maxscale.cnf.

| Parameter                                                                                                                                                                            | Description                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [admin\_host](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_host) | • This parameter defines the network address that the REST API listens on.• The default value is 127.0.0.1. |
| [admin\_port](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_port) | • This parameter defines the network port that the REST API listens on.• The default value is 8989.         |

For example:

```
[maxscale]
...
admin_host            = 0.0.0.0
admin_port            = 8443
```

2. MaxGUI requires TLS, so you must [enable TLS for MaxScale's REST API](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/data-in-transit-encryption-enabling-tls-on-mariadb-server).
   Several global parameters must be configured in maxscale.cnf.

| Parameter                                                                                                                                                                                            | Description                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [admin\_ssl\_key](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_key)          | \* This parameter defines the private key used by the REST API.                     |
| [admin\_ssl\_cert](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_cert)        | \* This parameter defines the certificate used by the REST API.                     |
| [admin\_ssl\_ca\_cert](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#admin_ssl_ca_cert) | \*This parameter defines the CA certificate that signed the REST API's certificate. |

For example:

```
[maxscale]
...
admin_ssl_key=/certs/server-key.pem
admin_ssl_cert=/certs/server-cert.pem
admin_ssl_ca_cert=/certs/ca-cert.pem
```

3. Ensure that the admin\_gui global parameter is enable. It is enabled by default, so it will only be disabled if it was previously disabled manually.
4. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

5. [Create a new admin REST API](../administrative-tools-for-mariadb-maxscale-maxctrl/creating-a-rest-api-user-for-maxscale-with-maxctrl.md#creating-an-admin-user) user with MaxCtrl:

```
$ maxctrl --secure 
   --user=admin 
   --password=mariadb 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem 
   create user "maxscale_rest_admin" "maxscale_rest_admin_password" --type=admin
```

Replace maxscale\_rest\_admin and maxscale\_rest\_admin\_password with the desired user and password.

6. [Delete the default REST API](../administrative-tools-for-mariadb-maxscale-maxctrl/deleting-a-rest-api-user-for-maxscale-with-maxctrl.md#deleting-a-user) named admin with MaxCtrl:

```
$ maxctrl --secure 
   --user=maxscale_rest_admin 
   --password=maxscale_rest_admin_password 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem 
   destroy user "admin"
```

7. Visit MaxGUI in your web browser.

For example:

* If you were accessing it from local host with the default port, then you would visit this address: [127.0.0.1:8989](https://127.0.0.1:8989)
* If you were accessing it with the above example configuration, then you would visit this address: [192.168.2.100:8443](https://192.168.2.100:8443)

8. Enter your user and password to login.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
