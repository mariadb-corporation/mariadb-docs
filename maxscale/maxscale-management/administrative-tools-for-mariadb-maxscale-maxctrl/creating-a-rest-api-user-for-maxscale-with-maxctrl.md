---
description: >-
  Create new users for the MaxScale REST API using MaxCtrl. This page explains
  the difference between basic and admin users and provides command examples for
  adding credentials to your system.
---

# Creating a REST API User for MaxScale with MaxCtrl

## Overview

MaxScale has a [REST API](../../reference/maxscale-rest-api/), which can be configured to require authentication. When first installed, it has a single default admin user (admin) and password (mariadb). However, this user can be deleted, and other users can be created.

_MaxCtrl_ is a command-line utility that can perform administrative tasks using MaxScale's [REST API](../../reference/maxscale-rest-api/). It can create a user for the REST API.

## User Types

There are two types of users:

| User Type | Description                                                             |
| --------- | ----------------------------------------------------------------------- |
| Basic     | The user has read-only access                                           |
| Admin     | The user can change global MaxScale parameters and reconfigure modules. |

## Creating a Basic User

1. Configure the [REST API](connecting-to-maxscale-using-tls-with-maxctrl.md) if the default configuration is not sufficient.
2. Use _MaxCtrl_ to execute the create user command:

```bash
$ maxctrl --secure
   --user=admin
   --password=mariadb
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem
   --tls-cert=/certs/client-cert.pem
   --tls-ca-cert=/certs/ca.pem
   create user "maxscale_rest" "maxscale_rest_password"
```

Replace maxscale\_rest and maxscale\_rest\_password with the desired user and password.

## Creating an Admin User

1. Configure the [REST API](connecting-to-maxscale-using-tls-with-maxctrl.md) if the default configuration is not sufficient.
2. Use _MaxCtrl_ to execute the create user command with the --type=admin option:

```bash
$ maxctrl --secure
   --user=admin
   --password=mariadb
   --hosts=192.0.2.100:8443
   --tls-key=/certs/client-key.pem
   --tls-cert=/certs/client-cert.pem
   --tls-ca-cert=/certs/ca.pem
   create user "maxscale_rest_admin" "maxscale_rest_admin_password" --type=admin
```

Replace `maxscale_rest_admin` and `maxscale_rest_admin_password` with the desired user and password.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
