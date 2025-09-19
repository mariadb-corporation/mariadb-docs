# Deleting a REST API User for MaxScale with MaxCtrl

## Overview

MaxScale has a [REST API](../../reference/maxscale-rest-api/), which can be configured to require authentication. When it is first installed, it has a single default admin user (admin) and password (mariadb). However, this user can be deleted, and other users can be created.

[MaxCtrl](./) is a command-line utility that can perform administrative tasks using MaxScale's [REST API](../../reference/maxscale-rest-api/). It can be used to delete a user for the REST API.

## Deleting a User

1. [Configure the REST API](../configuring-maxscales-rest-api.md) if the default configuration is not sufficient.
2. Use [MaxCtrl](./) to execute the [destroy user](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl.md#destroy-user) command:

```bash
$ maxctrl --secure 
   --user=maxscale_rest_admin 
   --password=maxscale_rest_admin_password 
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem 
   --tls-cert=/certs/client-cert.pem 
   --tls-ca-cert=/certs/ca.pem 
   destroy user "admin"
```

Replace `admin` with the actual user.

{% hint style="info" %}
MaxScale will refuse to delete the last remaining admin user.
{% endhint %}

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
