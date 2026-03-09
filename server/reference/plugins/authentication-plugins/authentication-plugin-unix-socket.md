---
description: >-
  Official Unix socket authentication: OS user login via SO_PEERCRED/uid
  matching, CREATE USER IDENTIFIED VIA unix_socket, and unix_socket force modes.
---

# Authentication Plugin - Unix Socket

The `unix_socket` authentication plugin is installed by default, and it is used by the `'root'@'localhost'` user account by default. See [Authentication](../../../security/user-account-management/authentication-from-mariadb-10-4.md) for more information.

The `unix_socket` authentication plugin allows the user to use operating system credentials when connecting to MariaDB via the local Unix socket file. This Unix socket file is defined by the [socket](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket) system variable.

The `unix_socket` authentication plugin works by calling the [getsockopt](https://man7.org/linux/man-pages/man7/socket.7.html) system call with the `SO_PEERCRED` socket option, which allows it to retrieve the `uid` of the process that is connected to the socket. It is then able to get the user name associated with that `uid`. Once it has the user name, it will authenticate the connecting user as the MariaDB account that has the same user name.

The `unix_socket` authentication plugin is not suited to multiple Unix users accessing a single MariaDB user account.

## Security

A `unix_socket` authentication plugin is a passwordless security mechanism. Its security lies in the strength of the access to the Unix user, rather than the complexity and the secrecy of the password.

{% hint style="warning" %}
As security differs from password security, the strengths and weaknesses need to be considered, and those can differ depending on the specific installation.
{% endhint %}

### Strengths

* Access is limited to the Unix user so, for example, a `www-data` user cannot access `root` with the `unix_socket` authentication plugin.
* There is no password which can be cracked by brute force.
* There is no password that can be accidentally exposed by user accident, poor security on backups, or poor security on passwords in configuration files.
* Default Unix user security is usually strong on preventing remote access and password brute force attempts.

### Weaknesses

The strength of a `unix_socket` authentication plugin is effectively the strength of the security of the Unix users on the system. In most cases, the Unix user default installation is sufficiently secure. However, the following is a non-exhaustive list of potential Unix user security issues that may arise.

* Common access areas without screen locks, where an unauthorized user accesses the logged in Unix user of an authorized user.
* Extensive sudo access grants that provide users with access to execute commands of a different Unix user.
* Scripts writable by Unix users other than the Unix user that are executed (via cron or directly) by the Unix user.
* Web pages that are susceptible to command injection, where the Unix user running the web page has elevated privileges in the database that weren't intended to be used.
* Poor Unix user password practices including weak user passwords, password exposure and password reuse accompanied by an access vulnerability/mechanism of an unauthorized user to exploit this weakness.
* Weak remote access mechanisms and network file system privileges.
* Poor user security behavior including running untrusted scripts and software.

In some of these scenarios a database password may prevent these security exploits, however it will remove all the strengths of the `unix_socket` authentication plugin previously mentioned.

## Disabling the Plugin

The `unix_socket` authentication plugin is installed by default.

{% hint style="warning" %}
If you do not want it to be available by default, you must disable it.
{% endhint %}

The `unix_socket` authentication plugin is also installed by default in new installations that use the [.deb](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md) packages provided by Debian's default repositories and Ubuntu's default repositories. See [Differences in MariaDB in Debian (and Ubuntu)](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md) for more information.

The `unix_socket` authentication plugin can be disabled by starting the server with the [unix\_socket](authentication-plugin-unix-socket.md#unix_socket) option set to `OFF`. This can be specified as a command-line argument to [mysqld](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
unix_socket=OFF
```

As an alternative, the [unix\_socket](authentication-plugin-unix-socket.md#unix_socket) option can also be set to `OFF` by pairing the option with the `disable` [option prefix](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-prefixes):

```ini
[mariadb]
...
disable_unix_socket
```

## Installing the Plugin

The `unix_socket` authentication plugin is installed by default in almost all MariaDB server versions. If you work with a version that doesn't have the plugin installed, you can install it as described in one of the following ways.

* Install the plugin without restarting the server. You can install the plugin dynamically, by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'auth_socket';
```

* Instruct the server to load the plugin at startup. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options. This can be specified as a command-line argument to [mysqld](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = auth_socket
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'auth_socket';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Creating Users

To create a user account via [CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md), specify the name of the plugin in the [IDENTIFIED VIA](../../sql-statements/account-management-sql-statements/create-user.md#identified-via-or-with-authentication_plugin) clause:

```sql
CREATE USER username@hostname IDENTIFIED VIA unix_socket;
```

If [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) does not have `NO_AUTO_CREATE_USER` set, then you can also create the user account via [GRANT](../../sql-statements/account-management-sql-statements/grant.md):

```sql
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA unix_socket;
```

{% tabs %}
{% tab title="Current" %}
The authentication string (if present) is compared with the socket's user name. Authentication proceeds if there's a match. In this case, the [external\_user](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#external_user) system variable contains the OS user.

Consider an OS user named 'bob' that has been created like this:

```sql
CREATE USER A identified via unix_socket as 'bob';




```

That user can connect like this:

```bash
mariadb -uA
```

Alternatively, accessing the sock file directly, the user can connect like this:

```bash
mariadb -uA -S /var/run/mysqld/mysqld.sock
```

Once connected, you can view that user like this:

```sql
SELECT USER(),@@external_user;
+-------------+-----------------+
| user()      | @@external_user |
+-------------+-----------------+
| A@localhost | bob             |
+-------------+-----------------+
```
{% endtab %}

{% tab title="< 11.6" %}
The plugin only checks whether the OS socket user id matches the MariaDB user name. It ignores the authentication string.
{% endtab %}
{% endtabs %}

## Switching to Password-Based Authentication

If Unix socket authentication does not meet your needs, you can switch a user account back to password-based authentication, by telling MariaDB to use a different [authentication plugin](./) for the account. The specific authentication plugin is specified with the [IDENTIFIED VIA](../../sql-statements/account-management-sql-statements/alter-user.md#identified-via-or-with-authentication_plugin) clause. To switch to the [mysql\_native\_password](authentication-plugin-mysql_native_password.md) authentication plugin, you need to do this:

```sql
ALTER USER root@localhost IDENTIFIED VIA mysql_native_password;
SET PASSWORD = PASSWORD('foo');
```

{% hint style="warning" %}
If you use scripts that require passwordless access to MariaDB, this would cause them to break. You may be able to fix that by setting a password in the `[client]` [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in your /root/.my.cnf [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).
{% endhint %}

```ini
[client]
password=foo
```

## Client Authentication Plugins

The `unix_socket` authentication plugin does not require any specific client authentication plugins. It should work with all clients.

## Support in Client Libraries

The `unix_socket` authentication plugin does not require any special support in client libraries. It should work with all client libraries.

## Example

```bash
$ mysql -uroot
MariaDB []> CREATE USER serg IDENTIFIED VIA unix_socket;
MariaDB []> CREATE USER monty IDENTIFIED VIA unix_socket;
MariaDB []> quit
Bye
$ whoami
serg
$ mysql --user=serg
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2
Server version: 5.2.0-MariaDB-alpha-debug Source distribution
MariaDB []> quit
Bye
$ mysql --user=monty
ERROR 1045 (28000): Access denied for user 'monty'@'localhost' (using password: NO)
```

In this example, user `serg` is already logged into the operating system and has full shell access. The user has already authenticated with the operating system and the MariaDB account is configured to use the `unix_socket` authentication plugin, so there is no need to authenticate again for the database. MariaDB accepts the operating system credentials and allows the user to connect. However, any attempt to connect to the database as another operating system is denied.

## Options

### `unix_socket`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugin](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--unix-socket=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## See Also

* [Differences in MariaDB in Debian (and Ubuntu)](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md)
* [Authentication](../../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [Authentication from MariaDB 10 4 video tutorial](https://www.youtube.com/watch?v=aWFG4uLbimM)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
