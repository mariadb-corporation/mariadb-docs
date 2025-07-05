# Authentication Plugin - PAM

The `pam` authentication plugin allows MariaDB to offload user authentication to the system's [Pluggable Authentication Module (PAM)](https://en.wikipedia.org/wiki/Pluggable_authentication_module) framework. PAM is an authentication framework used by Linux, FreeBSD, Solaris, and other Unix-like operating systems.

**Note:** Windows does not support PAM, so the `pam` authentication plugin does not support Windows. However, one can use a MariaDB client on Windows to connect to MariaDB server that is installed on a Unix-like operating system and that is configured to use the `pam` authentication plugin. For an example of how to do this, see the blog post: [MariaDB: Improve Security with Two-Step Verification](https://mariadb.org/improve-security-with-two-step-verification/).

## Use Cases

PAM makes it possible to implement various authentication scenarios of\
different complexity. For example,

* Authentication using passwords from `/etc/shadow` (indeed, this is what a default PAM configuration usually does). See the [pam\_unix](authentication-plugin-pam.md#pam_unix) PAM module.
* Authentication using LDAP. See the [pam\_ldap](authentication-plugin-pam.md#pam_ldap) PAM module.
* Authentication using Microsoft's Active Directory. See the [pam\_lsass](authentication-plugin-pam.md#pam_lsass), [pam\_winbind](authentication-plugin-pam.md#pam_winbind), and [pam\_centrifydc](authentication-plugin-pam.md#pam_centrifydc) PAM modules.
* Authentication using one-time passwords (even with SMS confirmation!). See the [pam\_google\_authenticator](authentication-plugin-pam.md#pam_google_authenticator) and [pam\_securid](authentication-plugin-pam.md#pam_securid) PAM modules.
* Authentication using SSH keys. See the [pam\_ssh](authentication-plugin-pam.md#pam_ssh) PAM module.
* User and group mapping. See the [pam\_user\_map](authentication-plugin-pam.md#pam_user_map) PAM module.
* Combining different authentication modules in interesting ways in a [PAM service](authentication-plugin-pam.md#configuring-the-pam-service).
* Password expiration.
* Limiting access by time, date, day of the week, etc. See the [pam\_time](authentication-plugin-pam.md#pam_time) PAM module.
* Logging every login attempt.
* and so on, the list is in no way exhaustive.

## Installing the Plugin

The `pam` authentication plugin's library is provided in [binary packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/) in all releases on Linux.

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```
INSTALL SONAME 'auth_pam';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = auth_pam
```

### Installing the v1 Plugin

The `auth_pam` shared library actually refers to version `2.0` of the `pam` authentication plugin. Version `1.0` of the plugin as the `auth_pam_v1` shared library is also available.

If you need to install version `1.0` of the authentication plugin instead of version `2.0`, then you can do so. For example, with [INSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```
INSTALL SONAME 'auth_pam_v1';
```

Or by specifying in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
plugin_load_add = auth_pam_v1
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```
UNINSTALL SONAME 'auth_pam';
```

If you installed the plugin by providing the [--plugin-load](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

### Uninstalling the v1 Plugin

If you installed version `1.0` of the authentication plugin, then you can uninstall that by executing a similar statement for `auth_pam_v1`. For example:

```
UNINSTALL SONAME 'auth_pam_v1';
```

## Configuring PAM

The `pam` authentication plugin tells MariaDB to delegate the authentication to the PAM authentication framework. How exactly that authentication is performed depends on how PAM was configured.

### Configuring the PAM Service

PAM is divided into `services`. PAM services are configured by [PAM configuration files](https://www.linux-pam.org/Linux-PAM-html/sag-configuration-file.html). Typically, the global PAM configuration file is located at `/etc/pam.conf` and [PAM directory-based configuration files](https://www.linux-pam.org/Linux-PAM-html/sag-configuration-directory.html) for individual services are located in `/etc/pam.d/`.

If you want to use a PAM service called `mariadb` for your MariaDB PAM authentication, then the PAM configuration file for that service would also be called `mariadb`, and it would typically be located at `/etc/pam.d/mariadb`.

For example, here is a minimal PAM service configuration file that performs simple password authentication with UNIX passwords:

```
auth required pam_unix.so audit
account required pam_unix.so audit
```

Let's breakdown this relatively simple PAM service configuration file.

Each line of a PAM service configuration file has the following general format:

_type control module-path module-arguments_

The above PAM service configuration file instructs the PAM authentication framework that for successful **authentication** (i.e. type=[auth](https://www.linux-pam.org/Linux-PAM-html/mwg-expected-of-module-auth.html)), it is **required** that the `pam_unix.so` PAM module returns a success.

The above PAM service configuration file also instructs the PAM authentication framework that for an **account** (i.e. type=[account](https://www.linux-pam.org/Linux-PAM-html/mwg-expected-of-module-acct.html)) to be valid, it is **required** that the `pam_unix.so` PAM module returns a success.

PAM also supports [session](https://www.linux-pam.org/Linux-PAM-html/mwg-expected-of-module-session.html) and [password](https://www.linux-pam.org/Linux-PAM-html/mwg-expected-of-module-chauthtok.html) types, but MariaDB's `pam` authentication plugin does not support those.

The above PAM service configuration file also provides the `audit` module argument to the `pam_unix` PAM module. The [pam\_unix manual](https://linux.die.net/man/8/pam_unix) says that this module argument enables extreme debug logging to the syslog.

On most systems, you can find many other examples of PAM service configuration files in your `/etc/pam.d/` directory.

#### Configuring the pam\_unix PAM Module

If you configure PAM to use the [pam\_unix](https://linux.die.net/man/8/pam_unix) PAM module (as in the above example), then you might notice on some systems that this will fail by default with errors like the following:

```
Apr 14 12:56:23 localhost unix_chkpwd[3332]: check pass; user unknown
Apr 14 12:56:23 localhost unix_chkpwd[3332]: password check failed for user (alice)
Apr 14 12:56:23 localhost mysqld: pam_unix(mysql:auth): authentication failure; logname= uid=991 euid=991 tty= ruser= rhost=  user=alice
```

The problem is that on some systems, the `pam_unix` PAM module needs access to `/etc/shadow` in order to function, and most systems only allow `root` to access that file by default.

Newer versions of PAM do not have this limitation, so you may want to try upgrading your version of PAM to see if that fixes the issue.

If that does not work, then you can work around this problem by giving the user that runs [mysqld](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) access to `/etc/shadow`. For example, if the `mysql` user runs [mysqld](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md), then you could do the following:

```
sudo groupadd shadow
sudo usermod -a -G shadow mysql
sudo chown root:shadow /etc/shadow
sudo chmod g+r /etc/shadow
```

And then you would have to [restart the server](https://mariadb.com/kb/en/).

At that point, the server should be able to read `/etc/shadow`.

The `pam` authentication plugin uses a [setuid](https://linux.die.net/man/2/setuid) wrapper to perform its PAM checks, so it should not need any special workarounds to perform privileged operations, such as reading `/etc/shadow` when using the `pam_unix` PAM module. See [MDEV-7032](https://jira.mariadb.org/browse/MDEV-7032) for more information.\
<>

## Creating Users

Similar to all other [authentication plugins](../), to create a user in MariaDB which uses the `pam` authentication plugin, you would execute [CREATE USER](../../../sql-statements/account-management-sql-statements/create-user.md) while specifying the name of the plugin in the [IDENTIFIED VIA](../../../sql-statements/account-management-sql-statements/create-user.md#identified-viawith-authentication_plugin) clause. For example:

```
CREATE USER username@hostname IDENTIFIED VIA pam;
```

If [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) does not have `NO_AUTO_CREATE_USER` set, then you can also create the user this way with [GRANT](../../../sql-statements/account-management-sql-statements/grant.md). For example:

```
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA pam;
```

You can also specify a [PAM service name](authentication-plugin-pam.md#configuring-the-pam-service) for MariaDB to use by providing it with the `USING` clause. For example:

```
CREATE USER username@hostname IDENTIFIED VIA pam USING 'mariadb';
```

This line creates a user that needs to be authenticated via the `pam` authentication plugin using the [PAM service name](authentication-plugin-pam.md#configuring-the-pam-service) `mariadb`. As mentioned in a previous section, this service's configuration file will typically be present in `/etc/pam.d/mariadb`.

If no service name is specified, then the plugin will use `mysql` as the default [PAM service name](authentication-plugin-pam.md#configuring-the-pam-service).

## Client Authentication Plugins

For clients that use the `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) libraries, MariaDB provides two client authentication plugins that are compatible with the `pam` authentication plugin:

* `dialog`
* `mysql_clear_password`

When connecting with a [client or utility](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md) to a server as a user account that authenticates with the `pam` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option. For example:

```
mariadb --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

Both the `dialog` and the `mysql_clear_password` client authentication plugins transmit the password to the server in clear text. Therefore, when you use the `pam` authentication plugin, it is incredibly important to [encrypt client connections using TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) to prevent the clear-text passwords from being seen by unauthorized users.

### `dialog`

Usually the `pam` authentication plugin uses the `dialog` client authentication plugin to communicate with the user. This client authentication plugin allows MariaDB to support arbitrarily complex PAM configurations with regular or one-time passwords, challenge-response, multiple questions, or just about anything else. When using a MariaDB client library, there is no need to install or enable anything — the `dialog` client authentication plugin is loaded by the client library completely automatically and transparently for the application.

The `dialog` client authentication plugin was developed by MariaDB, so MySQL's clients and client libraries as well as third party applications that bundle MySQL's client libraries do not support the `dialog` client authentication plugin out of the box. If the server tells an unsupported client to use the `dialog` client authentication plugin, then the client is likely to throw an error like the following:

```
ERROR 2059 (HY000): Authentication plugin 'dialog' cannot be loaded: /usr/lib/mysql/plugin/dialog.so: cannot open shared object file: No such file or directory
```

For some libraries or applications, this problem can be fixed by copying `dialog.so` or `dialog.dll` from a MariaDB client installation that is compatible with the system into the system's MySQL client authentication plugin directory. However, not all clients are compatible with the `dialog` client authentication plugin, so this may not work for every client.

If your client does not support the `dialog` client authentication plugin, then you may need to use the [mysql\_clear\_password](authentication-plugin-pam.md#mysql_clear_password) client authentication plugin instead.

The `dialog` client authentication plugin transmits the password to the server in clear text. Therefore, when you use the `pam` authentication plugin, it is incredibly important to [encrypt client connections using TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) to prevent the clear-text passwords from being seen by unauthorized users.

### `mysql_clear_password`

Users can instruct the `pam` authentication plugin to use the `mysql_clear_password` client authentication plugin instead of the [dialog](authentication-plugin-pam.md#dialog) client authentication plugin by configuring the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable on the server. It can be set in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
pam_use_cleartext_plugin
```

It is important to note that the `mysql_clear_password` plugin has very limited functionality.

* The `mysql_clear_password` client authentication plugin only supports PAM services that require password-based authentication.
* The `mysql_clear_password` client authentication plugin also only supports PAM services that ask the user a single question.
* If the PAM service requires challenge-responses, multiple questions, or other similar complicated authentication schemes, then the PAM service is not compatible with `mysql_clear_password` client authentication plugin. In that case, the [dialog](authentication-plugin-pam.md#dialog) client authentication plugin will have to be used instead.

The `mysql_clear_password` client authentication plugin transmits the password to the server in clear text. Therefore, when you use the `pam` authentication plugin, it is incredibly important to [encrypt client connections using TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) to prevent the clear-text passwords from being seen by unauthorized users.

#### Compatiblity with MySQL Clients and Client Libraries

The `mysql_clear_password` client authentication plugin is similar to MySQL's [mysql\_clear\_password](https://dev.mysql.com/doc/refman/5.7/en/cleartext-pluggable-authentication.html) client authentication plugin.

The `mysql_clear_password` client authentication plugin is compatible with MySQL clients and most MySQL client libraries, while the [dialog](authentication-plugin-pam.md#dialog) client authentication plugin is not always compatible with them. Therefore, the `mysql_clear_password` client authentication plugin is most useful if you need some kind of MySQL compatibility in your environment, but you still want to use the `pam` authentication plugin.

Even though the `mysql_clear_password` client authentication plugin is compatible with MySQL clients and most MySQL client libraries, the `mysql_clear_password` client authentication plugin may be disabled by default by these clients and client libraries. For example, MySQL's version of the [mysql](https://dev.mysql.com/doc/refman/5.7/en/mysql.html) command-line client has the [--enable-cleartext-plugin](https://dev.mysql.com/doc/refman/5.7/en/mysql-command-options.html#option_mysql_enable-cleartext-plugin) option that must be set in order to use the `mysql_clear_password` client authentication plugin. For example:

```
mysql --enable-cleartext-plugin --user=alice -p
```

Other clients may require other methods to enable the authentication plugin. For example, [MySQL Workbench](https://www.mysql.com/products/workbench/) has a checkbox titled **Enable Cleartext Authentication Plugin** under the **Advanced** tab on the connection configuration screen.

For applications that use MySQL's `libmysqlclient`, the authentication plugin can be enabled by setting the `MYSQL_ENABLE_CLEARTEXT_PLUGIN` option with the `mysql_options()` function. For example:

```
mysql_options(mysql, MYSQL_ENABLE_CLEARTEXT_PLUGIN, 1);
```

For MySQL compatibility, [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) also allows applications to set the `MYSQL_ENABLE_CLEARTEXT_PLUGIN` option with the [mysql\_optionsv](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_optionsv) function. However, this option does not actually do anything in [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), because the `mysql_clear_password` client authentication plugin is always enabled for MariaDB clients and client libraries.

## Support in Client Libraries

### Using the Plugin with MariaDB Connector/C

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) supports `pam` authentication using the [client authentication plugins](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/client-authentication-plugins/README.md) mentioned in the previous section since MariaDB Connector/C 2.1.0, regardless of the value of the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable.

### Using the Plugin with MariaDB Connector/ODBC

[MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc) supports `pam` authentication using the [client authentication plugins](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/client-authentication-plugins/README.md) mentioned in the previous section since MariaDB Connector/ODBC 1.0.0, regardless of the value of the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable.

### Using the Plugin with MariaDB Connector/J

[MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) supports `pam v1` authentication since MariaDB Connector/J 1.4.0, regardless of the value of the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable.

[MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) supports `pam v2` authentication since MariaDB Connector/J 2.4.4, regardless of the value of the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable.

### Using the Plugin with MariaDB Connector/Node.js

[MariaDB Connector/Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/nodejs-connector/README.md) supports `pam` authentication since MariaDB Connector/Node.js 0.7.0, regardless of the value of the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable.

### Using the Plugin with MySqlConnector for .NET

[MySqlConnector for ADO.NET](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mysqlconnector-for-adonet/README.md) supports `pam` authentication since MySqlConnector 0.20.0, but only if the [pam\_use\_cleartext\_plugin](authentication-plugin-pam.md#pam_use_cleartext_plugin) system variable is enabled on the server.

## Logging

### PAM Module Logging

Errors and messages from PAM modules are usually logged using the [syslog](https://linux.die.net/man/8/rsyslogd) daemon with the `authpriv` facility. To determine the specific log file where the `authpriv` facility is logged, you can check [rsyslog.conf](https://linux.die.net/man/5/rsyslog.conf).

On RHEL, CentOS, Fedora, and other similar Linux distributions, the default location for these messages is usually `/var/log/secure`.

On Debian, Ubuntu, and other similar Linux distributions, the default location for these messages is usually `/var/log/auth.log`.

For example, the syslog can contain messages like the following when MariaDB's `pam` authentication plugin is configured to use the [pam\_unix](authentication-plugin-pam.md#pam_unix) PAM module, and the user enters an incorrect password:

```
Jan  9 05:35:41 ip-172-30-0-198 unix_chkpwd[1205]: password check failed for user (foo)
Jan  9 05:35:41 ip-172-30-0-198 mysqld: pam_unix(mariadb:auth): authentication failure; logname= uid=997 euid=997 tty= ruser= rhost=  user=foo
```

### PAM Authentication Plugin's Debug Logging

MariaDB's `pam` authentication plugin can also log additional verbose debug logging to the [error log](../../../../server-management/server-monitoring-logs/error-log.md). This is only done if the plugin is a [debug build](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/compiling-mariadb-for-debugging) and if [pam\_debug](authentication-plugin-pam.md#pam_debug) is set.

The output looks like this:

```
PAM: pam_start(mariadb, alice)
PAM: pam_authenticate(0)
PAM: conv: send(Enter PASSCODE:)
PAM: conv: recv(123456789)
PAM: pam_acct_mgmt(0)
PAM: pam_get_item(PAM_USER)
PAM: status = 0 user = ��\>
```

### Custom Logging with pam\_exec

The [pam\_exec](https://linux.die.net/man/8/pam_exec) PAM module can be used to implement some custom logging. This can be very useful when debugging certain kinds of issues.

For example, first, create a script that writes the log output:

```
tee /tmp/pam_log_script.sh <<EOF
#!/bin/bash
echo "\${PAM_SERVICE}:\${PAM_TYPE} - \${PAM_RUSER}@\${PAM_RHOST} is authenticating as \${PAM_USER}" 
EOF
chmod 0775 /tmp/pam_log_script.sh
```

And then change the [PAM service configuration](authentication-plugin-pam.md#configuring-the-pam-service) to execute the script using the [pam\_exec](https://linux.die.net/man/8/pam_exec) PAM module. For example:

```
auth optional pam_exec.so log=/tmp/pam_output.txt /tmp/pam_log_script.sh
auth required pam_unix.so audit
account optional pam_exec.so log=/tmp/pam_output.txt /tmp/pam_log_script.sh
account required pam_unix.so audit
```

Whenever the above PAM service is used, the output of the script will be written to `/tmp/pam_output.txt`. It may look similar to this:

```
*** Tue May 14 14:53:23 2019
mariadb:auth - @ is authenticating as alice
*** Tue May 14 14:53:25 2019
mariadb:account - @ is authenticating as alice
*** Tue May 14 14:53:28 2019
mariadb:auth - @ is authenticating as alice
*** Tue May 14 14:53:31 2019
mariadb:account - @ is authenticating as alice
```

## User and Group Mapping

Even when using the `pam` authentication plugin, the authenticating PAM user account still needs to exist in MariaDB, and the account needs to have privileges in the database. Creating these MariaDB accounts and making sure the privileges are correct can be a lot of work. To decrease the amount of work involved, some users would like to be able to map a PAM user to a different MariaDB user. For example, let’s say that `alice` and `bob` are both DBAs. It would be nice if each of them could log into MariaDB with their own PAM username and password, while MariaDB sees both of them as the same `dba` user. That way, there is only one MariaDB account to keep track of. See [User and Group Mapping with PAM](user-and-group-mapping-with-pam.md) for more information on how to do this.

## PAM Modules

There are many PAM modules. The ones described below are the ones that have been seen most often by MariaDB.

### pam\_unix

The [pam\_unix](https://linux.die.net/man/8/pam_unix) PAM module provides support for Unix password authentication. It is the default PAM module on most systems.

For a tutorial on setting up PAM authentication and user or group mapping with Unix authentication, see [Configuring PAM Authentication and User Mapping with Unix Authentication](configuring-pam-authentication-and-user-mapping-with-unix-authentication.md).

### pam\_user\_map

The [pam\_user\_map](user-and-group-mapping-with-pam.md) PAM module was developed by MariaDB to support user and group mapping.

### pam\_ldap

The [pam\_ldap](https://linux.die.net/man/5/pam_ldap) PAM module provides support for LDAP authentication.

For a tutorial on setting up PAM authentication and user or group mapping with LDAP authentication, see [Configuring PAM Authentication and User Mapping with LDAP Authentication](configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md).

This can also be configured for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication.

### pam\_sss

The [pam\_sss](https://linux.die.net/man/8/pam_sss) PAM module provides support for authentication with [System Security Services Daemon (SSSD)](https://en.wikipedia.org/wiki/System_Security_Services_Daemon).

This can be configured for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication.

### pam\_lsass

The `pam_lsass` PAM module provides support for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication. It is provided by [PowerBroker Identity Services – Open Edition](https://github.com/BeyondTrust/pbis-open/wiki).

### pam\_winbind

The [pam\_winbind](https://www.samba.org/samba/docs/current/man-html/pam_winbind.8.html) PAM module provides support for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication. It is provided by [winbindd](https://www.samba.org/samba/docs/current/man-html/winbindd.8.html) from the [samba](https://www.samba.org/samba/docs/current/man-html/samba.7.html) suite.

This PAM module converts all provided user names to lowercase. There is no way to disable this functionality. If you do not want to be forced to use all lowercase user names, then you may need to configure the [pam\_winbind\_workaround](authentication-plugin-pam.md#pam_winbind_workaround) system variable. See [MDEV-18686](https://jira.mariadb.org/browse/MDEV-18686) for more information.

### pam\_centrifydc

The [pam\_centrifydc](https://docs.centrify.com/en/css/2018-html/index.html#page/Planning,_preparation,_and_deployment/unix_pam_services.html) PAM module provides support for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication. It integrates with the commercial [Active Directory Bridge from Centrify](https://www.centrify.com/products/infrastructure-services/authentication/active-directory-bridge/integration/).

### pam\_krb5

The [pam\_krb5](https://linux.die.net/man/8/pam_krb5) PAM module provides support for [Kerberos](https://en.wikipedia.org/wiki/Kerberos_\(protocol\)) authentication.

This can be configured for [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication.

### pam\_google\_authenticator

The `pam_google_authenticator` PAM module provides two-factor identification with Google Authenticator. It is from Google's [google-authenticator-libpam](https://github.com/google/google-authenticator-libpam) open-source project. The PAM module should work with the open-source mobile apps built by Google's [google-authenticator](https://github.com/google/google-authenticator) and [google-authenticator-android](https://github.com/google/google-authenticator-android) projects as well as the closed source Google Authenticator mobile apps that are present in each mobile app store.

For an example of how to use this PAM module, see the blog post: [MariaDB: Improve Security with Two-Step Verification](https://mariadb.org/improve-security-with-two-step-verification/).

### pam\_securid

The `pam_securid` PAM module provides support for multi-factor authentication. It is part of the commercial [RSA SecurID Suite](https://www.rsa.com/en-us/products/rsa-securid-suite).

Note that current versions of this module are not [safe for multi-threaded environments](authentication-plugin-pam.md#multi-threaded-issues), and the vendor does not officially support the product on MariaDB. See [MDEV-10361](https://jira.mariadb.org/browse/MDEV-10361) about that. However, the module may work with a current version of MariaDB.

### pam\_ssh

The [pam\_ssh](https://linux.die.net/man/8/pam_ssh) PAM module provides authentication using SSH keys.

### pam\_time

The [pam\_time](https://linux.die.net/man/8/pam_time) PAM module provides time-controlled access.

## Known Issues

### Multi-Threaded Issues

MariaDB is a multi-threaded program, which means that different connections concurrently run in different threads. Current versions of MariaDB's `pam` authentication plugin execute PAM module code in the server address space. This means that any PAM modules used with MariaDB must be safe for multi-threaded environments. Otherwise, if multiple clients try to authenticate with the same PAM module in parallel, undefined behavior can occur. For example, the `pam_fprintd` PAM module is not safe for multi-threaded environments, and if you use it with MariaDB, you may experience server crashes.

The `pam` authentication plugin isolates PAM module code from the server address space, so even PAM modules that are known to be unsafe for multi-threaded environments should not cause issues with MariaDB. See [MDEV-15473](https://jira.mariadb.org/browse/MDEV-15473) for more information.

### Conflicts with Password Validation

When a [password validation plugin](../../password-validation-plugins/) is enabled, MariaDB won't allow an account to be created if the password validation plugin says that the account's password is too weak. This creates a problem for accounts that authenticate with the `pam` authentication plugin, since MariaDB has no knowledge of the user's password. When a user tries to create an account that authenticates with the `pam` authentication plugin, the password validation plugin would throw an error, even with [strict\_password\_validation=OFF](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) set.

The workaround is to uninstall the [password validation plugin](../../password-validation-plugins/) with [UNINSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md), and then create the account, and then reinstall the [password validation plugin](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/broken-reference/README.md) with [INSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md).

For example:

```
INSTALL PLUGIN simple_password_check SONAME 'simple_password_check';
Query OK, 0 rows affected (0.002 sec)

SET GLOBAL strict_password_validation=OFF;
Query OK, 0 rows affected (0.000 sec)

CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
UNINSTALL PLUGIN simple_password_check;
Query OK, 0 rows affected (0.000 sec)

CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
Query OK, 0 rows affected (0.000 sec)

INSTALL PLUGIN simple_password_check SONAME 'simple_password_check';
Query OK, 0 rows affected (0.001 sec)
```

#### Note:

Accounts that authenticate with the `pam` authentication plugin should be exempt from password validation checks. See [MDEV-12321](https://jira.mariadb.org/browse/MDEV-12321) and [MDEV-10457](https://jira.mariadb.org/browse/MDEV-10457) for more information.

### SELinux

[SELinux](../../../../security/securing-mariadb/selinux.md) may cause issues when using the `pam` authentication plugin. For example, using [pam\_unix](authentication-plugin-pam.md#pam_unix) with the `pam` authentication plugin while SELinux is enabled can sometimes lead to SELinux errors involving [unix\_chkpwd](https://linux.die.net/man/8/unix_chkpwd), such as the following::

```
Apr 14 12:37:59 localhost setroubleshoot: Plugin Exception restorecon_source
Apr 14 12:37:59 localhost setroubleshoot: SELinux is preventing /usr/sbin/unix_chkpwd from execute access on the file . For complete SELinux messages. run sealert -l c56fe6e0-c78c-4bdb-a80f-27ef86a1ea85
Apr 14 12:37:59 localhost python: SELinux is preventing /usr/sbin/unix_chkpwd from execute access on the file .

*****  Plugin catchall (100. confidence) suggests   **************************

If you believe that unix_chkpwd should be allowed execute access on the  file by default.
Then you should report this as a bug.
You can generate a local policy module to allow this access.
Do
allow this access for now by executing:
# grep unix_chkpwd /var/log/audit/audit.log | audit2allow -M mypol
# semodule -i mypol.pp
```

Sometimes issues like this can be fixed by updating the system's SELinux policies. You may be able to update the policies using [audit2allow](https://linux.die.net/man/1/audit2allow). See [SELinux: Generating SELinux Policies with audit2allow](../../../../security/securing-mariadb/selinux.md#generating-selinux-policies-with-audit2allow) for more information.

If you can't get the `pam` authentication plugin to work with SELinux at all, then it can help to disable SELinux entirely. See [SELinux: Changing SELinux's Mode](../../../../security/securing-mariadb/selinux.md#changing-selinuxs-mode) for information on how to do this.

### Memory Overcommit

You may run into authentication failures with the following log message in the MariaDB error log:

```
pam: cannot exec /usr/lib64/mysql/plugin/auth_pam_tool_dir/auth_pam_tool (errno: 12 "Cannot allocate memory")
```

This can happen on operating system setups that are configured to prevent memory overcommit. When the MariaDB server process spawns the `auth_pam_tool` helper process there's a brief period where the new process inherits the memory of the MariaDB process before releasing that memory and executing the new command. When having a MariaDB server configured to use more than 50% of the server machnines RAM -- which is common for dedicated database servers -- this duplication would lead to an over-commit situation.

Starting with [MariaDB 10.5.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10516-release-notes), [MariaDB 10.6.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1068-release-notes), and [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), we changed to use `posix_spawn()` instead of the classic `fork();exec()` to prevent this, but systems with older glibc versions prior to 2.26 still use `fork();exec()` to implement `posix_spawn()` internally and so are still affected; this is for example still the case on RedHat Enterprise Linux 7.

To solve this you can either:

* change the `vm.overcommit_memory` kernel setting to allow memory overcommit
* install the older `auth_pam_v1` plugin version that does not spawn a helper process (but may run into problems with file permissions or multi threading with some PAM modules)

See also [MDEV-26212](https://jira.mariadb.org/browse/MDEV-26212) and [MDEV-30734](https://jira.mariadb.org/browse/MDEV-30734)

## Tutorials

You may find the following PAM-related tutorials helpful:

* [Configuring PAM Authentication and User Mapping with Unix Authentication](configuring-pam-authentication-and-user-mapping-with-unix-authentication.md)
* [Configuring PAM Authentication and User Mapping with LDAP Authentication](configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md)

## Versions

| Version | Status | Introduced                                                                                                                                                                                                         |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Version | Status | Introduced                                                                                                                                                                                                         |
| 2.0     | Beta   | [MariaDB 10.4.0](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/broken-reference/README.md) |
| 1.0     | Stable | [MariaDB 10.0.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes)                                |
| 1.0     | Beta   | [MariaDB 5.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/mariadb-5210-release-notes)                                   |

## System Variables

### `pam_debug`

* Description: Enables verbose debug logging to the [error log](../../../../server-management/server-monitoring-logs/error-log.md) for all authentication handled by the plugin.
  * This system variable is only available when the plugin is a [debug build](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/compiling-mariadb-for-debugging).
* Commandline: `--pam-debug`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), [MariaDB 10.1.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10117-release-notes)

### `pam_use_cleartext_plugin`

* Description: Use the [mysql\_clear\_password](authentication-plugin-pam.md#mysql_clear_password) client authentication plugin instead of the [dialog](authentication-plugin-pam.md#dialog) client authentication plugin. This may be needed for compatibility reasons, but it only supports simple PAM configurations that don't require any input besides a password.
* Commandline: `--pam-use-cleartext-plugin`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), [MariaDB 5.5.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5532-release-notes)

### `pam_winbind_workaround`

* Description: Configures the authentication plugin to compare the user name provided by the client with the user name returned by the PAM module in a case insensitive manner. This may be needed if you use the [pam\_winbind](authentication-plugin-pam.md#pam_winbind) PAM module, which is known to convert all user names to lowercase, and which does not allow this behavior to be disabled.
* Commandline: `--pam-winbind-workaround`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes), [MariaDB 10.3.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10315-release-notes), [MariaDB 10.2.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10224-release-notes), [MariaDB 10.1.39](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes)

## Options

### `pam`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--pam=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

## See Also

* [Writing a MariaDB PAM Authentication Plugin](https://mariadb.org/writing-a-mariadb-pam-authentication-plugin/)
* [MariaDB: Improve Security with Two-Step Verification](https://mariadb.org/improve-security-with-two-step-verification/)
* [Using PAM with MaxScale](https://mariadb.com/kb/en/mariadb-maxscale-2208-pam-authenticator/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
