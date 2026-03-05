---
description: >-
  Explains how to manage database objects like users, databases, and privileges
  natively through Kubernetes Custom Resources (CRDs).
---

# SQL Resources

MariaDB Operator Enterprise enables you to manage SQL resources declaratively through CRs. By SQL resources, we refer to users, grants, and databases that are typically created using SQL statements.

The key advantage of this approach is that, unlike executing SQL statements manually, which is a one-time operation, declaring a SQL resource via a CR ensures that the resource is periodically reconciled by the operator. This provides a guarantee that the resource will be recreated if it gets manually deleted. Additionally, it prevents state drifts, as the operator will regularly update the resource according to the CR specification.

## `User` CR

By creating this resource, you are declaring an intent to create an user in the referred `MariaDB` instance, just like a [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) statement would do:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: bob
spec:
  mariaDbRef:
    name: mariadb
  passwordSecretKeyRef:
    name: bob-password
    key: password
  maxUserConnections: 20
  host: "%"
  cleanupPolicy: Delete
```

In the example above, a user named `bob` identified by the password available in the `bob-password` `Secret` will be created in the `mariadb` instance.

Refer to the [API reference](api-reference.md) for more detailed information about every field.

#### Custom name

By default, the CR name is used to create the user in the database, but you can specify a different one providing the `name` field under spec:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  name: user-custom
```

## `Grant` CR

By creating this resource, you are declaring an intent to grant permissions to a given user in the referred `MariaDB` instance, just like a [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement would do.

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Grant
metadata:
  name: grant-bob
spec:
  mariaDbRef:
    name: mariadb
  privileges:
    - "SELECT"
    - "INSERT"
    - "UPDATE"
  database: "*"
  table: "*"
  username: bob
  grantOption: true
  host: "%"
```

You may provide any set of [privileges supported by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#privilege-levels).

Refer to the [API reference](api-reference.md) for more detailed information about every field.

## `Database` CR

By creating this resource, you are declaring an intent to create a logical database in the referred `MariaDB` instance, just like a [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement would do:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Database
metadata:
  name: wordpress
spec:
  mariaDbRef:
    name: mariadb
  characterSet: utf8
  collate: utf8_general_ci
```

Refer to the [API reference](api-reference.md) for more detailed information about every field.

#### Custom name

By default, the CR name is used to create the user in the database, but you can specify a different one providing the `name` field under spec:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: Database
metadata:
  name: database
spec:
  name: database-custom
```

## Initial `User`, `Grant` and `Database`

If you only need one user to interact with a single logical database, you can use of the `MariaDB` resource to configure it, instead of creating the `User`, `Grant` and `Database` resources separately:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  username: bob
  passwordSecretKeyRef:
    name: bob-password
    key: password
  database: wordpress
```

Behind the scenes, the operator will be creating an `User` resource with `ALL PRIVILEGES` in the initial `Database`.

## Authentication plugins

{% hint style="warning" %}
This feature requires the `skip-strict-password-validation` option to be set. See: [strict-password-validation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#strict_password_validation).
{% endhint %}

Passwords can be supplied using the `passwordSecretKeyRef` field in the `User` CR. This is a reference to a `Secret` that contains a password in plain text.

Alternatively, you can use [MariaDB authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) to avoid passing passwords in plain text and provide the password in a hashed format instead. This doesn't affect the end user experience, as they will still need to provide the password in plain text to authenticate.

#### Password hash

Provide the password hashed using the [MariaDB PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password) function:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mariadb-auth
stringData:
  passwordHash: "*57685B4F0FF9D049082E296E2C39354B7A98774E"
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user-password-hash
spec:
  mariaDbRef:
    name: mariadb
  passwordHashSecretKeyRef:
    name: mariadb-auth
    key: passwordHash
  host: "%"
```

The password hash can be obtained by executing `SELECT PASSWORD('<password>');` in an existing MariaDB installation.

#### Password plugin

Provide the password hashed using any of the available [MariaDB authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins), for example `mysql_native_password`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mariadb-auth
stringData:
  passwordHash: "*57685B4F0FF9D049082E296E2C39354B7A98774E"
  nativePasswordPlugin: mysql_native_password
---
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user-password-plugin
spec:
  mariaDbRef:
    name: mariadb
  passwordPlugin:
    pluginNameSecretKeyRef:
        name: mariadb-auth
        key: nativePasswordPlugin
    pluginArgSecretKeyRef:
        name: mariadb-auth
        key: passwordHash
  host: "%"
```

The plugin name should be available in a `Secret` referenced by `pluginNameSecretKeyRef` and the argument passed to it in `pluginArgSecretKeyRef`. The argument is the hashed password in most cases, refer to the [MariaDB docs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) for further detail.

## Configure reconciliation

As we previously mentioned, SQL resources are periodically reconciled by the operator into SQL statements. You are able to configure the reconciliation interval using the following fields:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  requeueInterval: 30s
  retryInterval: 5s
```

If the SQL statement executed by the operator is successful, it will schedule the next reconciliation cycle using the `requeueInterval`. If the statement encounters an error, the operator will use the `retryInterval` instead.

## Cleanup policy

Whenever you delete a SQL resource, the operator will also delete the associated resource in the database. This is the default behaviour, that can also be achieved by setting `cleanupPolicy=Delete`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: User
metadata:
  name: user
spec:
  cleanupPolicy: Delete
```

You can opt-out from this cleanup process using `cleanupPolicy=Skip`. Note that this resources will remain in the database.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
