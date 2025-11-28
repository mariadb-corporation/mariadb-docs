---
description: >-
  The pam_user_map PAM module allows administrators to map external PAM users
  and groups to specific MariaDB accounts for flexible authorization management.
---

# User and Group Mapping with PAM

## Overview

Even when using the [pam](authentication-plugin-pam.md) authentication plugin, the authenticating PAM user account still needs to exist in MariaDB, and the account needs to have privileges in the database. Creating these MariaDB accounts and making sure the privileges are correct can be a lot of work. To decrease the amount of work involved, some users would like to be able to map a PAM user to a different MariaDB user. For example, let’s say that `alice` and `bob` are both DBAs. It would be nice if each of them could log into MariaDB with their own PAM username and password, while MariaDB sees both of them as the same `dba` user. That way, there is only one MariaDB account to keep track of.

Although most PAM modules usually do not do things like this, PAM supports the ability to change the user name in the process of authentication.The MariaDB `pam` authentication plugin fully supports this feature of PAM.

### The pam\_user\_map PAM Module

Rather than building user and group mapping into the `pam` authentication plugin, MariaDB thought that it would cover the most use cases and offer the most flexibility to offload this functionality to an external PAM module. The `pam_user_map` PAM module was implemented by MariaDB to facilitate this. This PAM module can be [configured in the PAM service](authentication-plugin-pam.md#configuring-the-pam-service) used by the `pam` authentication plugin, just like other PAM modules.

#### Lack of Support for MySQL/Percona Group Mapping Syntax

Unlike MariaDB, MySQL and Percona implemented group mapping in their PAM authentication plugins. If you've read through [MySQL's PAM authentication documentation on group mapping](https://dev.mysql.com/doc/refman/8.0/en/pam-pluggable-authentication.html#pam-authentication-unix-with-proxy) or [Percona's PAM authentication documentation on group mapping](https://www.percona.com/doc/percona-server/8.0/management/pam_plugin.html#supplementary-groups-support), you've probably seen syntax where the group mappings are provided in the [CREATE USER](../../../sql-statements/account-management-sql-statements/create-user.md) statement like this:

```sql
CREATE USER ''@''
  IDENTIFIED WITH authentication_pam
  AS 'mysql, root=developer, users=data_entry';
```

Since MariaDB's user and group mapping is performed by an external PAM module, MariaDB's `pam` authentication plugin does not support this syntax. Instead, the user and group mappings for the `pam_user_map` PAM module are configured in an external configuration file. This is discussed in a later section.

### Installing the pam\_user\_map PAM Module

The `pam_user_map` PAM module gets installed as part of all our MariaDB server packages.

Some Linux distributions have not picked up this change in their own packages yet. When using such an installation, it may be necessary to compile the PAM module from source as described in the next section, or to manually extract it from one of our server packages and copy it to the target system.

#### Installing the pam\_user\_map PAM Module from Source

**Installing Compilation Dependencies**

Before the module can be compiled from source, you may need to install some dependencies.

On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/), you need to install `gcc`, `pam-devel` and `MariaDB-devel`:

```bash
sudo yum install gcc pam-devel MariaDB-devel
```

On Debian, Ubuntu, and other similar Linux distributions that use [DEB packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md), you need to install `gcc`, `libpam0g-dev`:

```bash
sudo apt-get install gcc libpam0g-dev libmariadb-dev
```

**Compiling and Installing the pam\_user\_map PAM Module**

The `pam_user_map` PAM module can be built by downloading `plugin/auth_pam/mapper/pam_user_map.c` file from the MariaDB source tree and compiling it after minor adjustments. Once it is built, it can be installed to the system's PAM module directory, which is typically `/lib64/security/`:

```bash
wget https://raw.githubusercontent.com/MariaDB/server/10.4/plugin/auth_pam/mapper/pam_user_map.c
sed -ie 's/config_auth_pam/plugin_auth_common/' pam_user_map.c
gcc -I/usr/include/mysql/ pam_user_map.c -shared -lpam -fPIC -o pam_user_map.so
sudo install --mode=0755 pam_user_map.so /lib64/security/
```

You also need to adjust the major version number in the URL on the first line to match your installed MariaDB version, and the `#-I` include path argument on the `gcc` line, as depending on operating system and MariaDB server version, the `plugin_auth_common.h` file may be installed in a directory other than `/usr/include/mysql/` .

### Configuring the pam\_user\_map PAM Module

The `pam_user_map` PAM module uses the configuration file at the path `/etc/security/user_map.conf` to determine its user and group mappings. The file's format is described below.

To map a specific PAM user to a specific MariaDB user:

```
orig_pam_user_name: mapped_mariadb_user_name
```

Or to map any PAM user in a specific PAM group to a specific MariaDB user, the group name is prefixed with `@`:

```
@orig_pam_group_name: mapped_mariadb_user_name
```

For example, here is an example `/etc/security/user_map.conf`:

```
=========================================================
#comments and empty lines are ignored
john: jack
bob:  admin
top:  accounting
@group_ro: readonly
```

### Configuring PAM

With user and group mapping, configuring PAM is done similar to how it is [normally done with the pam authentication plugin](authentication-plugin-pam.md#configuring-pam). However, when configuring the PAM service, you will have to add an `auth` line for the `pam_user_map` PAM module to the service's PAM configuration file:

```
auth required pam_unix.so audit
auth required pam_user_map.so
account required pam_unix.so audit
```

### Creating Users

With user and group mapping, creating users is done similar to how it is [normally done with the pam authentication plugin](authentication-plugin-pam.md#creating-users). However, one major difference is that you will need to [GRANT](../../../sql-statements/account-management-sql-statements/grant.md) the [PROXY](../../../sql-statements/account-management-sql-statements/grant.md#proxy-privileges) privilege on the mapped user to the original user.

Consider having the following configured in `/etc/security/user_map.conf`:

```
foo: bar
@dba:dba
```

Then you could execute the following to grant the relevant privileges:

```sql
CREATE USER 'bar'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'bar'@'%' ;

CREATE USER 'dba'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' ;

CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
GRANT PROXY ON 'bar'@'%' TO ''@'%';
GRANT PROXY ON 'dba'@'%' TO ''@'%';
```

Note that the `''@'%'` account is a special catch-all [anonymous account](../../../sql-statements/account-management-sql-statements/create-user.md#anonymous-accounts). Any login by a user that has no more specific account match in the system will be matched by this anonymous account.

Also note that you might not be able to create the `''@'%'` anonymous account by default on some systems without doing some extra steps first. See [Fixing a Legacy Default Anonymous Account](../../../sql-statements/account-management-sql-statements/create-user.md#fixing-a-legacy-default-anonymous-account) for more information.

### Verifying that Mapping is Occurring

In case any user mapping is performed, the original user name is returned by the SQL function [USER()](../../../sql-functions/secondary-functions/information-functions/user.md), while the authenticated user name is returned by the SQL function [CURRENT\_USER()](../../../sql-functions/secondary-functions/information-functions/current_user.md). The latter actually defines what privileges are available to a connected user.

Consider having the following configured:

```
foo: bar
```

Then the following output would verify that it is working properly:

```bash
$ mysql -u foo -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------+----------------+
| USER()                                         | CURRENT_USER() |
+------------------------------------------------+----------------+
| foo@ip-172-30-0-198.us-west-2.compute.internal | bar@%          |
+------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `foo` PAM user was properly mapped to the `bar` MariaDB user by looking at the return value of `CURRENT_USER()`.

### Logging

By default, the `pam_user_map` PAM module does not perform any logging. However, if you want to enable debug logging, then you can add the `debug` module argument to the service's PAM configuration file:

```
auth required pam_unix.so audit
auth required pam_user_map.so debug
account required pam_unix.so audit
```

When debug logging is enabled, the `pam_user_map` PAM module will write log entries to the [same syslog location](authentication-plugin-pam.md#logging) as other PAM modules, which is typically `/var/log/secure` on many systems.

For example, this debug log output can look like the following:

```
Jan  9 05:42:13 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Opening file '/etc/security/user_map.conf'.
Jan  9 05:42:13 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Incoming username 'alice'.
Jan  9 05:42:13 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User belongs to 2 groups [alice,dba].
Jan  9 05:42:13 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Check if user is in group 'dba': YES
Jan  9 05:42:13 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User mapped as 'dba'
Jan  9 05:43:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Opening file '/etc/security/user_map.conf'.
Jan  9 05:43:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Incoming username 'bob'.
Jan  9 05:43:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User belongs to 2 groups [bob,dba].
Jan  9 05:43:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Check if user is in group 'dba': YES
Jan  9 05:43:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User mapped as 'dba'
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Opening file '/etc/security/user_map.conf'.
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Incoming username 'foo'.
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User belongs to 1 group [foo].
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Check if user is in group 'dba': NO
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): Check if username 'foo': YES
Jan  9 06:08:36 ip-172-30-0-198 mysqld: pam_user_map(mariadb:auth): User mapped as 'bar'
```

### Known Issues

#### PAM User with Same Name as Mapped MariaDB User Must Exist

With user and group mapping, any PAM user or any PAM user in a given PAM group can be mapped to a specific MariaDB user account. However, due to the way PAM works, a PAM user with the same name as the mapped MariaDB user account must exist.

Consider the configuration file for the PAM service file containing the following:

```
auth required pam_sss.so
auth required pam_user_map.so debug
account sufficient pam_unix.so
account sufficient pam_sss.so
```

Consider `etc/security/user_map.conf` containing the following:

```
@dba: dba
```

In that case, any PAM user in the PAM group `dba` are mapped to the MariaDB user account `dba`. But if a PAM user with the name `dba` doesn't exist, the `pam_user_map` PAM module's debug logging writes errors to the syslog, like the following:

```
Sep 27 17:17:05 dbserver1 mysqld: pam_user_map(mysql:auth): Opening file '/etc/security/user_map.conf'.
Sep 27 17:17:05 dbserver1 mysqld: pam_user_map(mysql:auth): Incoming username 'alice'.
Sep 27 17:17:05 dbserver1 mysqld: pam_user_map(mysql:auth): User belongs to 4 groups [dba,mongod,mongodba,mysql].
Sep 27 17:17:05 dbserver1 mysqld: pam_user_map(mysql:auth): Check if user is in group 'mysql': YES
Sep 27 17:17:05 dbserver1 mysqld: pam_user_map(mysql:auth): User mapped as 'dba'
Sep 27 17:17:05 dbserver1 mysqld: pam_unix(mysql:account): could not identify user (from getpwnam(dba))
Sep 27 17:17:05 dbserver1 mysqld: pam_sss(mysql:account): Access denied for user dba: 10 (User not known to the underlying authentication module)
Sep 27 17:17:05 dbserver1 mysqld: 2018-09-27 17:17:05 72 [Warning] Access denied for user 'alice'@'localhost' (using password: NO)
```

In the above log snippet, notice that both the `pam_unix` and the `pam_sss` PAM modules are complaining that the `dba` PAM user does not appear to exist, and that these complaints cause the PAM authentication process to fail, which causes the MariaDB authentication process to fail as well.

This can be fixed by creating a PAM user with the same name as the mapped MariaDB user account, which is `dba` in this case.

You may also be able to work around this problem by essentially disabling PAM's account verification for the service with the [pam\_permit](https://linux.die.net/man/8/pam_permit) PAM module. For example, in the above case, that would be:

```
auth required pam_sss.so
auth required pam_user_map.so debug
account required pam_permit.so
```

See [MDEV-17315](https://jira.mariadb.org/browse/MDEV-17315) for more information.

### Tutorials

You may find the following PAM and user mapping-related tutorials helpful:

* [Configuring PAM Authentication and User Mapping with Unix Authentication](configuring-pam-authentication-and-user-mapping-with-unix-authentication.md)
* [Configuring PAM Authentication and User Mapping with LDAP Authentication](configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md)

### See Also

* [Configuring PAM Authentication and User Mapping with MariaDB](https://mariadb.com/resources/blog/configuring-pam-authentication-and-user-mapping-with-mariadb/)
* [Configuring PAM Group Mapping with MariaDB](https://mariadb.com/resources/blog/configuring-pam-group-mapping-with-mariadb/)
* [Configuring LDAP Authentication and Group Mapping With MariaDB](https://www.geoffmontee.com/configuring-ldap-authentication-and-group-mapping-with-mariadb/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
