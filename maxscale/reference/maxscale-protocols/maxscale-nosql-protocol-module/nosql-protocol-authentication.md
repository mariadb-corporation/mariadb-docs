---
description: >-
  How nosqlprotocol authenticates and authorizes NoSQL clients with SCRAM, maps
  NoSQL users and roles to MariaDB users, and bootstraps the account database.
---

# MaxScale NoSQL Protocol Authentication

This page describes how nosqlprotocol authenticates NoSQL clients and authorizes their operations.

Nosqlprotocol supports _SCRAM_ _authentication_ as implemented by MongoDB®. The mechanisms `SCRAM-SHA-1` and `SCRAM-SHA-256` are both supported.

If nosqlprotocol has been setup so that no authentication is required, then when connecting only the host and port should be provided, but neither a username nor a password.

For instance, if the _MongoDB Node.JS Driver_ is used, then the connection string should look like:

```
const uri = "mongodb://127.0.0.1:17017"
```

Similarly, if the _Mongo Shell_ is used, only the host and port should be provided:

```
$ mongo --host 127.0.0.1 --port 17017
MongoDB shell version v4.4.1
...
>
```

## NoSQL and MariaDB Users

A MariaDB user consists of a name and a host part. A user `'user'@'%'` and a user `'user'@'127.0.0.1'` are completely different. The host part specifies where a user may connect from, with `%` being a wildcard that matches all hosts. What data a user is allowed to access and modify is specified by what _privileges_ are granted to the user.

A NoSQL user is somewhat different. It is created in the context of a particular database, so there may be a user `userx` in the database `dbA` and different user with the same name `userx` in the database `dbB`. What hosts a user may connect from can be restricted, but that is a property of the user and not an implicit part of it. What data a user is allowed to access and modify is specified by the _roles_ that have been assigned to the user.

From the above it should be clear that there is not a 1-to-1 correspondence between the concept of a user in NoSQL and the concept of a user in MariaDB, but that some additional conventions are needed.

To make it possible to have different NoSQL users with the same name, the database in whose context the user is created is prepended to the user name, separated with a dot, when the MariaDB user is created.

This is perhaps easiest to illustrate using an example:

```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| bob         | %         |
| mysql       | localhost |
+-------------+-----------+
2 rows in set (0.001 sec)
```

Currently there are two user accounts defined. Even though there is a user `bob`, creating a NoSQL user `bob` succeeds.

```
> use test;
switched to db test
> db.runCommand({createUser: "bob", pwd: "bobspwd", roles: []});
{ "ok" : 1 }
```

If we now, from the MariaDB prompt, check the users we will see:

```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| bob         | %         |
| test.bob    | %         |
| mysql       | localhost |
+-------------+-----------+
3 rows in set (0.001 sec)
```

The MariaDB user corresponding to the NoSQL user `bob`, created in the context of the database `test`, has `test` as a prefix.

### The `mariadb` database

The fact that NoSQL users have the database embedded in the MariaDB name may be inconvenient if the same data is accessed both as NoSQL via nosqlprotocol and as SQL directly from MariaDB. It also makes it impossible to use an existing MariaDB account from NoSQL.

To provide a solution for this problem, the database `mariadb` is treated in a specific fashion. A user created in the context of the `mariadb` database is created in the MariaDB server without the database prefix. If we now try to create a user `bob` in the `mariadb` database it will fail, because the user `'bob'@'%'` exists already.

```
> use mariadb
switched to db mariadb
> db.runCommand({createUser: "bob", pwd: "bobspwd", roles: []});
{
    "ok" : 0,
    "errmsg" : "User \"bob\" already exists",
    "code" : 51003,
    "codeName" : "Location51003"
}
```

If we create a user with another name it will succeed.

```
> db.runCommand({createUser: "alice", pwd: "alicespwd", roles: []});
{ "ok" : 1 }
```

And if we check the situation from MariaDB,

```
MariaDB [(none)]> select user, host from mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| alice       | %         |
| bob         | %         |
| test.bob    | %         |
| mysql       | localhost |
+-------------+-----------+
4 rows in set (0.001 sec)
```

we will see that `alice` was created without a database prefix.

## Roles and Privileges

When creating a user nosqlprotocol accepts all roles as predefined by MongoDB®, but not all of them are translated into GRANT privileges. The following table shows what privilege(s) a particular role is converted to.

| Role      | Privileges                                    |
| --------- | --------------------------------------------- |
| dbAdmin   | ALTER, CREATE, DROP, SHOW DATABASES, SELECT   |
| read      | SELECT                                        |
| readWrite | CREATE, DELETE, INDEX, INSERT, SELECT, UPDATE |
| userAdmin | CREATE USER, GRANT OPTION                     |

The following roles are shorthands for several other roles.

| Role    | Shorthand for                 |
| ------- | ----------------------------- |
| dbOwner | dbAdmin, readWrite, userAdmin |
| root    | dbAdmin, readWrite, userAdmin |

`dbOwner` differs from `root` in that the privileges of the former apply only to a particular database, while the privileges of the latter apply to _all_ databases. However, the role `root` can only be assigned to a user in the `admin` database.

In addition there are `AnyDatabase` versions of `dbAdmin`, `read` and`readWrite` (e.g `readAnyDatabase`) that can be assigned to a user in the `admin` database. If so, then the privilege is granted on `*.*`, otherwise on `<db>.*`.

If the `root` role is assigned to a user in the `admin` database, then the privileges are granted on `*.*`, otherwise on `<db>.*`.

Other pre-defined roles are recognized and stored in the local nosqlprotocol account database, but they do not affect what privileges are granted to the MariaDB user. User-defined roles are not supported.

## Client Authentication

Authenticationwise nosqlprotocol can be used in three different ways:

* Anonymously
* Shared credentials
* Unique credentials

### Anonymously

If there is an anonymous user on the MariaDB server and if nosqlprotocol is configured without a user/password, then all nosqlprotocol clients will access the MariaDB server as anonymous users.

Note that the anonymous MariaDB user is only intended for testing and should in general not be used, but deleted.

### Shared Credentials

If nosqlprotocol is configured with

```
...
nosqlprotocol.user=theuser
nosqlprotocol.password=thepassword
```

then each MongoDB® client will use those credentials when accessing the MariaDB server. Note that from the perspective of the MariaDB server, it is not possible to distinguish between different MongoDB® clients.

### Unique Credentials

If nosqlprotocol authentication has been taken into use and a MongoDB® client authenticates, either when connecting or later, then the credentials of MongoDB® client will be used when accessing the MariaDB server.

Note that even if nosqlprotocol authentication has been enabled, authentication is not required, and if the MongoDB® client has not authenticated itself, the credentials specified with `nosqlprotocol.[user|password]` (or the anonymous user) will be used when accessing the MariaDB server.

### Enforce Authentication

To enforce authentication, specify

```
nosqlprotocol.authentication_required=true
```

in the configuration. If authentication is required, then any command that requires access to the MariaDB server will fail, unless the client has authenticated.

## Authorization

By default nosqlprotocol does no authorization. However, a nosqlprotocol client is _always_ subject to the authorization performed by the MariaDB server.

When nosqlprotocol authorization is enabled by adding

```
nosqlprotocol.authorization_enabled=true
```

to the configuration file, some commands will be subject to authorization, by nosqlprotocol. The following table lists the commands and what role they require.

| Command                                                                      | Role      |
| ---------------------------------------------------------------------------- | --------- |
| [createUser](nosql-protocol-database-commands.md#createuser)                   | userAdmin |
| [dropUser](nosql-protocol-database-commands.md#dropuser)                       | userAdmin |
| [grantRolesToUser](nosql-protocol-database-commands.md#grantrolestouser)       | userAdmin |
| [revokeRolesFromUser](nosql-protocol-database-commands.md#revokerolesfromuser) | userAdmin |
| [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser)                   | userAdmin |
| [mxsRemoveUser](nosql-protocol-database-commands.md#mxsremoveuser)             | userAdmin |
| [mxsUpdateUser](nosql-protocol-database-commands.md#mxsupdateuser)             | userAdmin |
| [updateUser](nosql-protocol-database-commands.md#updateuser)                   | userAdmin |
| [usersInfo](nosql-protocol-database-commands.md#usersinfo)                     | userAdmin |

It is important to note that even if nosqlprotocol authorization is enabled, the MariaDB server has the final word. That is, even if the roles of a user would be sufficient for a particular operation, if the granted privileges are not, the operation will not succeed. There may be a mismatch between roles and privileges, for instance, if the wrong roles were specified when the user was added, or if the privileges have been altered directly and not via nosqlprotocol.

## Bootstrapping the Authentication/Authorization

The authentication/authorization can be bootstrapped explicitly or implicitly. Bootstrapping explicitly provides more control, while bootstrapping implicitly is much more convenient.

### Explicit bootstrapping

In order to enable authorization you need to have NoSQL users and those can be created with [createUser](nosql-protocol-database-commands.md#createuser) or added with [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser).

If you want to _create_ a user, then you first need to configure nosqlprotocol with credentials that are sufficient for creating a user:

```
nosqlprotocol.user = user_with_privileges_for_creating_a_user
nosqlprotocol.password = the_users_password
```

At this point `nosqlprotocol.authentication_required` and`nosqlprotocol.authorization_enabled` should both be `false`. Note that as those are their default values, they do not have to be specified.

Start MaxScale and connect to it with the MongoDB® command line client

```
$ mongo --port 17017
...
>
```

Then create the user.

```
> use admin;
switched to db admin
> db.runCommand({createUser: "nosql_admin", pwd: "nosql_pwd", roles: ["userAdmin"]});
{ "ok" : 1 }
```

Alternatively you can add an existing user. Note that it should be added to the `mariadb` database, unless it was created with the convention of having the database as a prefix, e.g. `db.bob`.

```
> use mariadb;
switched to db admin
> db.runCommand({mxsAddUser: "bob", pwd: "bob_pwd", roles: ["userAdmin"]});
{ "ok" : 1 }
```

Now you should shutdown MaxScale and add the entries

```
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```

and start MaxScale.

The `nosqlprotocol.user` and `nosqlprotocol.password` can be removed but as they will be ignored with `nosqlprotocol.authentication_required=true` being present, it is not mandatory.

If you now try to create a user when not having been authenticated or when authenticated as a user without the `userAdmin` role, the result will be:

```
> use test;
switched to db test
> db.runCommand({createUser: "alice", pwd: "alices_pwd", roles: []});
{
    "ok" : 0,
    "errmsg" : "command createUser requires authentication",
    "code" : 13,
    "codeName" : "Unauthorized"
}
```

**NOTE** When a client authenticates, the password will not be transferred in cleartext over the network, so, even without SSL, it is not possible to gain access to a password by monitoring the network traffic.

However, when a user is created or added (or the password is changed), the password will be transferred in _cleartext_. To prevent eavesdropping, create/add users when connecting over a domain socket, or use [TLS/SSL](nosql-protocol-authentication.md#tls-ssl)

### Implicit bootstrapping

With implicit bootstrapping, you should first create the MariaDB user that should appear as the initial NoSQL user. As explained [here](nosql-protocol-authentication.md#nosql-and-mariadb-users), the concept of a user is somewhat different in MariaDB and NoSQL, which means that certain factors must be taken into account when creating the MariaDB user. Then at first startup, nosqlprotocol will create the corresponding NoSQL user, which will enable the authenticated and authorized use of nosqlprotocol.

When MaxScale is started, if the following hold

* `nosqlprotocol.authentication_required` and`nosqlprotocol.authorization_enabled` are true in the configuration section of the nosqlprotocol listener,
* `nosqlprotocol.user` and `nosqlprotocol.password` are provided, and
* there are no NoSQL users in the NoSQL account database.

then, MaxScale will

* wait until the primary of the service pointed to by the listener is available,
* connect using the credentials specified in `nosqlprotocol.user` and `nosqlprotocol.password`,
* execute `SHOW GRANTS`,
* translate the privileges into the equivalent NoSQL roles, and
* create a corresponding NoSQL user into the NoSQL account database.

Immediately thereafter it is possible to connect to the nosqlprotocol port with a MongoDB® client using the specified credentials.

Note that after the bootstrapping, nosqlprotocol will not use the `user` and `password` settings and they can be removed.

**Grants**

When a NoSQL user is created using [createUser](nosql-protocol-database-commands.md#createuser) the MariaDB grants are obtained from the specified NoSQL roles as explained [here](nosql-protocol-authentication.md#roles-and-privileges).

When implicitly creating a NoSQL user from an existing user in MariaDB, the inverse operation must be performed. There are many factors that affect what NoSQL roles the grants of a user are translated into:

* whether the user is a regular or admin user,
* whether the privileges are on `*.*` or some specific `db.*`, and
* the privileges themselves, e.g. `SELECT`, `DELETE`, etc.

In NoSQL, every user resides in a specific database. Note that this does **not** mean that the database would have to exist in MariaDB.

When it comes to users, the database effectively means a scope, which in the case of nosqlprotocol is handled by prefixing the corresponding MariaDB user name with the database/scope name.

When creating a user to be used from NoSQL, there are three options for the user's name:

* The name can be of the format `some_db.user_name` where`some_db` can be anything (subject to the naming rules of MariaDB), except `admin` or `mariadb`. In this case, the user will be a regular user, who can access data in databases that she has been granted access to.
* The name can be of the format `admin.user_name` where `admin` is exactly just that. In this case, the user will be an admin user, who can access any database.
* The name can be of the format `user_name`. In this case, the user will be a regular user that from the NoSQL side appears to reside in the `mariadb` database. The primary purpose of this alternative is to enable the use of existing users from the NoSQL side.

What database the privileges can be specified `ON` depends on what kind of user is being created.

* If it is a regular user, the privileges must be granted on a specific database, such as `\`dbA\`\`.\*\`. Note that there is no dependency between this database and the (conceptual) database the user resides in.
* If it is an admin user, the privileges must be granted on the `*.*` database.

In NoSQL, a role can be database specific or generic. However, a generic role can _only_ be assigned to a user in the _admin_ database. In practice this means that if the privileges are on `*.*`, then the user must reside in the _admin_ database (e.g. `admin.bob`) or it is treated as an error.

The following table shows what privileges are required for a role to be assigned. Note that `ALL PRIVILEGES` can be used as well.

| ALTER | CREATE | CREATE USER | DROP | DELETE | INDEX | INSERT | SHOW DATABASES(1) | SELECT | UPDATE | WITH GRANT OPTION | Role                    |
| ----- | ------ | ----------- | ---- | ------ | ----- | ------ | ----------------- | ------ | ------ | ----------------- | ----------------------- |
| X     | X      |             | X    |        |       |        | X                 | X      |        |                   | dbAdmin\[AnyDatabase]   |
|       |        |             |      |        |       |        |                   | X      |        |                   | read\[AnyDatabase]      |
|       | X      |             |      | X      | X     | X      |                   | X      | X      |                   | readWrite\[AnyDatabase] |
|       |        | X           |      |        |       |        |                   |        |        | X                 | userAdmin\[AnyDatabase] |

1. Only required if the user is an admin user.

The `AnyDatabase` version will be assigned, if the user is an _admin_ user.

If certain roles are assigned, then other roles will be assigned as well.

* If the roles `dbAdmin`, `readWrite` and `userAdmin` are assigned, then `dbOwner` will be assigned as well.
* If the roles `dbAdminAnyDatabase`, `readWriteAnyDatabase` and `userAdminAnyDatabase` are assigned, then `root` will be assigned as well.

Once the user has been created and the desired privileges have been granted, the NoSQL listener should be configured as follows:

```
[NoSQL-Listener]
...
nosqlprotocol.user=db.the_user
nosqlprotocol.password=the_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
...
```

At MaxScale startup, the NoSQL user will then be created.

**Examples**

**Admin User**

We want the initial NoSQL user to be an administrator, with full rights.

```
CREATE USER 'admin.nosql_admin'@'%' IDENTIFIED BY 'nosql_password';
GRANT ALL PRIVILEGES ON *.* TO 'admin.nosql_admin'@'%' WITH GRANT OPTION;
```

As we want an admin user, the name is prefixed with `admin`, which will have that effect. And since it is an admin user, the privileges are granted ON `*.*`.

Thereafter, we specify the following in the configuration file,

```
[NoSQL-Listener]
type=listener
service=...
protocol=nosqlprotocol
nosqlprotocol.user=admin.nosql_admin
nosqlprotocol.password=nosql_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```

and start MaxScale.

As the creation of the initial user can be made only after the monitor for the listener's service has marked one server as primary, whether the creation succeeded or not must be checked from MaxScale' log file:

```
... notice : [nosqlprotocol] Created initial NoSQL user 'admin.nosql_admin'.
```

Under normal conditions, the bootstrapping will be almost instantaneous.

It is now possible to connect using any MongoDB® client application.

```
$ mongo --quiet --port 17017 -u nosql_admin -p nosql_password admin
>
```

Note that when connecting the user is passed as `nosql_admin` and _not_ as `admin.nosql_admin`. The fact that we want to authenticate against the `admin` database is expressed by passing the database as the last argument.

```
> db.runCommand({usersInfo: 1});
{
    "users" : [
        {
            "_id" : "admin.nosql_admin",
            "userId" : UUID("7d921459-3099-42a7-ad06-ed37ac002161"),
            "user" : "nosql_admin",
            "db" : "admin",
            "roles" : [
                {
                    "db" : "admin",
                    "role" : "dbAdminAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "readWriteAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "userAdminAnyDatabase"
                },
                {
                    "db" : "admin",
                    "role" : "root"
                }
            ],
            "mechanisms" : [
                "SCRAM-SHA-256"
            ]
        }
    ],
    "ok" : 1
}
```

As can be seen, the user has the _any_ roles on the `admin` database, which means that all databases can be accessed and modified, and that new users can be created.

**Test User**

We want the initial NoSQL user to be a user with limited rights, intended to be used for testing.

```
CREATE USER 'test.test_user'@'%' IDENTIFIED BY 'test_password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX ON `test`.* TO 'test.test_user'@'%';
```

As we want a user with limited rights, the name is _not_ prefixed with `admin`. The privileges are granted specifically on database`test.*`. Indeed, if `*.*` had been used, the creation of the initial NoSQL user would have failed with an error. Here, the user is created in the same database that the user is given access to, but it could have been another one. Further, several `GRANT` statements could have been used, had we wanted to give access to several databases.

Thereafter, we specify the following in the configuration file,

```
[NoSQL-Listener]
type=listener
service=...
protocol=nosqlprotocol
nosqlprotocol.user=test.test_user
nosqlprotocol.password=test_password
nosqlprotocol.authentication_required=true
nosqlprotocol.authorization_enabled=true
```

and start MaxScale.

As the creation of the initial user can be made only after the monitor for the listener's service has marked one server as primary, whether the creation succeeded or not must be checked from MaxScale' log file:

```
... notice : [nosqlprotocol] Created initial NoSQL user 'test.test_user'.
```

Under normal conditions, the bootstrapping will be almost instantaneous.

It is now possible to connect using any MongoDB® client application.

```
$ mongo --quiet --port 17017 -u test_user -p test_password test
>
```

Note that when connecting the user is passed as `test_user` and _not_ as `test.test_user`. The fact that we want to authenticate against the `test` database is expressed by passing the database as the last argument.

```
> db.runCommand({usersInfo: 1});
{
    "users" : [
        {
            "_id" : "test.test_user",
            "userId" : UUID("714f35e7-4276-45af-863c-0be4d1f5dd74"),
            "user" : "test_user",
            "db" : "test",
            "roles" : [
                {
                    "db" : "test",
                    "role" : "readWrite"
                }
            ],
            "mechanisms" : [
                "SCRAM-SHA-256"
            ]
        }
    ],
    "ok" : 1
}
```

As can be seen, the user has the `readWrite` role on the `test` database, which means that only the `test` database can be accessed and modified.

### TLS/SSL

Since `nosqlprotocol` is a regular protocol module used in a listener, the TLS/SSL support of listeners is available. Please see [TLS/SSL encryption](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#tls-ssl-encryption) for details.

## NoSQL Account Database

So as to be able to connect to the MariaDB server on behalf of clients, nosqlprotocol must know their password. As the password is not transferred to nosqlprotocol during the authentication in a way that could be used when logging into MariaDB, the password must be stored when the user is created with [createUser](nosql-protocol-database-commands.md#createuser) or added with [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser).

Note that the password is not stored in cleartext but as three different hashes; hashed with sha1 for use with MariaDB, salted and hashed with sha1 for use with the `SCRAM-SHA-1` authentication mechanism (if that is enabled for the user) and salted and hashed with sha256 for use with the `SCRAM-SHA-256` authentication mechanism (if that is enabled for the user).

The account information can be stored _privately_, in which case it can be used only by a particular MaxScale instance, or in a\_shared\_ manner, in which case multiple MaxScale instances can share the information and a user created/added on one instance can be used on another.

### Private

In the private case, the account information of nosqlprotocol is stored in an [sqlite3](https://sqlite.org/index.html) database whose name is `<libdir>/nosqlprotocol/<listener-name>-v1.db`, where `<libdir>` is the _libdir_ of MaxScale, typically`/var/lib/maxscale`, `<listener-name>` is the name of the listener section in the MaxScale configuration file, and `-v1` a suffix for making schema evolution easier, should there be a need for that.

For instance, given a configuration like

```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
...
```

the account information will be stored in the file`<libdir>/nosqlprotocol/NoSQL-Listener-v1.db`.

Note that since the database name is derived from the listener name, changing the name of the listener in the configuration file will have the effect of making all accounts disappear. To retain the accounts, the database file should also be renamed.

At first startup, the `nosqlprotocol` directory and the file `NoSQL-Listener-v1.db` will be created. They will be created with file permissions that only allow MaxScale access. At subsequent startups the permissions will be checked and MaxScale will refuse to start if the permissions allow access to others.

**We strongly recommend that no manual modifications are made to the database.**

Note that we make **no** guarantees that the way in which the account information is stored by `nosqlprotocol` will remain the same _even_ between maintenance releases. We do guarantee, however, that even if the way in which the account information is stored changes, existing account information will automatically be converted and no manual intervention, such as re-creation of accounts, will be needed.

### Shared

In the shared case, the account information of nosqlprotocol is stored in the cluster of the service in front of which the NoSQL listener resides. The primary of the cluster will be used both for reading and writing data.

A table whose name is the same as the listener's name in the MaxScale configuration will be created in the database specified with the [authentication\_db](nosql-protocol-settings.md#authentication_db) parameter. If it is not specified explicitly, the default is`nosqlprotocol`. The name of the table will be the name of the listener section in the MaxScale configuration file.

For instance, given a configuration like

```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
...
```

the account information will be stored in the table`nosqlprotocol.NoSQL-Listener`.

Note that since the table name is derived from the listener name, changing the name of the listener in the configuration file will have the effect of making all accounts disappear. To retain the accounts, the table should also be renamed.

`nosqlprotocol` will create the table when needed, so the user specified with [authentication\_user](nosql-protocol-settings.md#authentication_user) must have sufficient grants to be able to do that.

`nosqlprotocol` will store in the table, data that allow any MaxScale to authenticate a MongoDB® client, irrespective of which MaxScale instance was used when the user was created.

`nosqlprotocol` also stores in the table the SHA1 of a user's password, to be able to authenticate against the MariaDB server. Therefore it is **strongly** suggested to enable encryption key management in MaxScale and to provide an authentication key ID with [authentication\_key\_id](nosql-protocol-settings.md#authentication_key_id) so that the data will be encrypted.

If shared authentication has been enabled with [authentication\_shared](nosql-protocol-settings.md#authentication_shared) then [authentication\_user](nosql-protocol-settings.md#authentication_user) and [authentication\_password](nosql-protocol-settings.md#authentication_password) must also be provided. With [authentication\_db](nosql-protocol-settings.md#authentication_db) the database name can optionally be changed, and with [authentication\_key\_id](nosql-protocol-settings.md#authentication_key_id) an encryption key ID, using which the sensitive data is encrypted, can optionally be provided.

Note that we make **no** guarantees that the table in which the account information is stored by `nosqlprotocol` will remain the same _even_ between maintenance releases. We do guarantee, however, that even if the way in which the account information is stored changes, existing account information will automatically be converted and no manual intervention, such as re-creation of accounts, will be needed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
