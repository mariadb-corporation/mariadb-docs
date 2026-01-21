---
description: >-
  The gssapi authentication plugin enables passwordless single sign-on by
  authenticating users via the Generic Security Services API, supporting
  Kerberos on Unix and Windows.
---

# Authentication Plugin - GSSAPI

The `gssapi` authentication plugin allows the user to authenticate with services that use the [Generic Security Services Application Program Interface (GSSAPI)](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface). Windows has a slightly different but very similar API called [Security Support Provider Interface (SSPI)](https://docs.microsoft.com/en-us/windows/desktop/secauthn/sspi). The GSSAPI is a standardized API described in [RFC2743](https://tools.ietf.org/html/rfc2743.html) and [RFC2744](https://tools.ietf.org/html/rfc2744.html). The client and server negotiate using a standardized protocol described in [RFC7546](https://tools.ietf.org/html/rfc7546.html).

On Windows, this authentication plugin supports [Kerberos](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-kerberos) and [NTLM](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-ntlm) authentication. Windows authentication is supported regardless of whether a [domain](https://en.wikipedia.org/wiki/Windows_domain) is used in the environment.

On Unix systems, the most dominant GSSAPI service is [Kerberos](https://en.wikipedia.org/wiki/Kerberos_\(protocol\)). However, it is less commonly used on Unix systems than it is on Windows. Regardless, this authentication plugin also supports Kerberos authentication on Unix.

The `gssapi` authentication plugin is most often used for authenticating with [Microsoft Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).

This article gives instructions on configuring the `gssapi` authentication plugin\
for MariaDB for passwordless login.

## Installing the Plugin's Package

{% hint style="info" %}
Since [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), on Windows, the plugin is included in the server. There is no need for separate installation.
{% endhint %}

The `gssapi` authentication plugin's shared library is included in MariaDB packages as the `auth_gssapi.so` or `auth_gssapi.dll` shared library on systems where it can be built.

### Installing on Linux

The `gssapi` authentication plugin is included in [binary tarballs](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) on Linux.

#### Installing with a Package Manager

The `gssapi` authentication plugin can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [yum](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/yum.md) or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`:

```bash
sudo yum install MariaDB-gssapi-server
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md) from MariaDB's repository using [apt-get](https://wiki.debian.org/apt-get):

```bash
sudo apt-get install mariadb-plugin-gssapi-server
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [zypper](../../../server-management/getting-installing-and-upgrading-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md):

```bash
sudo zypper install MariaDB-gssapi-server
```

### Installing on Windows

{% hint style="info" %}
Before [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), the `gssapi` authentication plugin is included in [MSI](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) and [ZIP](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md) packages on Windows.
{% endhint %}

## Installing the Plugin

{% hint style="info" %}
Since [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), on Windows, the plugin is included in the server. There is no need for separate installation.
{% endhint %}

On Windows, and on other operating systems, although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'auth_gssapi';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = auth_gssapi
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'auth_gssapi';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options must be removed to prevent the plugin from being loaded the next time the server is restarted.

## Configuring the Plugin

If the MariaDB server is running on Unix, then some additional configuration steps will need to be implemented in order to use the plugin.

If the MariaDB server is running on Windows, then no special configuration steps will need to be implemented in order to use the plugin, as long as the following is true:

* The Windows server is joined to a domain.
* The MariaDB server process is running as either a [NetworkService Account](https://docs.microsoft.com/en-us/windows/desktop/services/networkservice-account) or a [Domain User Account](https://docs.microsoft.com/en-us/windows/desktop/ad/domain-user-accounts).

### Creating a Keytab File on Unix

If the MariaDB server is running on Unix, then the KDC server will need to create a keytab file for the MariaDB server. The keytab file contains the service principal name, which is the identity that the MariaDB server will use to communicate with the KDC server. The keytab will need to be transferred to the MariaDB server, and the `mysqld` server process will need read access to this keytab file.

How this keytab file is generated depends on whether the KDC server is [Microsoft Active Directory KDC](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) or [MIT Kerberos KDC](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html).

#### Creating a Keytab File with Microsoft Active Directory

If you are using [Microsoft Active Directory KDC](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview), you may need to create a keytab using the [ktpass.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass) utility on a Windows host. The service principal will need to be mapped to an existing domain user. To do so, follow the steps listed below.

Be sure to replace the following items in the step below:

* Replace `${HOST}` with the fully qualified DNS name for the MariaDB server host.
* Replace `${DOMAIN}` with the Active Directory domain.
* Replace `${AD_USER}` with the existing domain user.
* Replace `${PASSWORD}` with the password for the service principal.

To create the service principal, execute the following command:

```bash
ktpass.exe /princ mariadb/${HOST}@${DOMAIN} /mapuser ${AD_USER} /pass ${PASSWORD} /out mariadb.keytab /crypto all /ptype KRB5_NT_PRINCIPAL /mapop set
```

#### Creating a Keytab File with MIT Kerberos

If you are using [MIT Kerberos KDC](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html), then you can create a [keytab](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/install_appl_srv.html#the-keytab-file) file using the [kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html) utility. To do so, follow the steps listed below.

In the following steps, be sure to replace `${HOST}` with the fully qualified DNS name for the MariaDB server host.

First, create the service principal using the [kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html) utility:

```bash
kadmin -q "addprinc -randkey mariadb/${HOST}"
```

Then, export the newly created user to the keytab file using the [kadmin](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/admin_commands/kadmin_local.html) utility:

```bash
kadmin -q "ktadd -k /path/to/mariadb.keytab mariadb/${HOST}"
```

More details can be found at the following links:

* [MIT Kerberos Documentation: Database administration](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/database.html)
* [MIT Kerberos Documentation: Application servers](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/appl_servers.html)

### Configuring the Path to the Keytab File on Unix

If the MariaDB server is running on Unix, then the path to the keytab file that was previously created can be set by configuring the [gssapi\_keytab\_path](authentication-plugin-gssapi.md#gssapi_keytab_path) system variable. This can be specified as a command-line argument to mariadbd, or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
gssapi_keytab_path=/path/to/mariadb.keytab
```

### Configuring the Service Principal Name

The service principal name can be set by configuring the [gssapi\_principal\_name](authentication-plugin-gssapi.md#gssapi_principal_name) system variable. This can be specified as a command-line argument to mariadbd, or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
gssapi_principal_name=service_principal_name/host.domain.com@REALM
```

If a service principal name is not provided, the plugin tries to use `mariadb/host.domain.com@REALM` by default.

If the MariaDB server is running on Unix, the plugin needs a service principal name in order to function.

If the MariaDB server is running on Windows, the plugin does not usually need a service principal in order to function. However, if you want to use one, anyway, it can be created with the `setspn` utility.

Different KDC implementations may use different canonical forms to identify principals. See [RFC2744: Section 3.10](https://tools.ietf.org/html/rfc2744.html#section-3.10) to learn what the standard says about principal names.

More details can be found at the following links:

* [Active Directory Domain Services: Service Principal Names](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names)
* [MIT Kerberos Documentation: Realm configuration decisions](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/realm_config.html)
* [MIT Kerberos Documentation: Principal names and DNS](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/princ_dns.html)

## Creating Users

To create a user account via [CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md), specify the name of the plugin in the [IDENTIFIED VIA](../../sql-statements/account-management-sql-statements/create-user.md#identified-via-or-with-authentication_plugin) clause:

```sql
CREATE USER username@hostname IDENTIFIED VIA gssapi;
```

If [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) does not have `NO_AUTO_CREATE_USER` set, then you can also create the user account via [GRANT](../../sql-statements/account-management-sql-statements/grant.md):

```sql
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA gssapi;
```

You can also specify the user's [realm](https://docs.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-crp-realm-names) for MariaDB with the `USING` clause:

```sql
CREATE USER username@hostname IDENTIFIED VIA gssapi USING 'username@EXAMPLE.COM';
```

The format of the realm depends on the specific authentication mechanism that is used. For example, the format would need to be `machine\\username` for Windows users authenticating with NTLM.

If the realm is not provided in the user account's definition, then the realm is **not** used for comparison. Therefore, 'usr1@EXAMPLE.COM', 'usr1@EXAMPLE.CO.UK' and 'mymachine\usr1' would all identify as the following user account:

```sql
CREATE USER usr1@hostname IDENTIFIED VIA gssapi;
```

### Creating Users Identified Via Group Membership or SID (Windows-specific)

On Windows only, it is possible to login using a AD or local group-membership. This is achieved by using the `GROUP` prefix in `IDENTIFIED ... AS`:

```sql
CREATE USER root IDENTIFIED VIA gssapi AS 'GROUP:Administrators'
CREATE USER root IDENTIFIED VIA gssapi AS 'GROUP:BUILTIN\\Administrators'
```

The effect of the above definition is that every user that identifies as a member of group `Administrators` can log in using the user name `root` without a password.

User can also login using own or group [SID](https://en.wikipedia.org/wiki/Security_Identifier) (Security Identifier):

```sql
CREATE USER root IDENTIFIED VIA gssapi AS 'SID:S-1-5-32-544'
```

Using SIDs will perform slightly faster than using name (since it will spare translation between SID and name which is otherwise done). SIDs are immune against user or group renaming.

## Passwordless login on Windows

{% hint style="info" %}
This feature is available from MariaDB 10.11.
{% endhint %}

On Windows, in addition to the usual authentication with a password, passwordless authentication is permitted when creating the `root` user during installation. This works in a similar manner to [Unix socket authentication](../../../security/user-account-management/authentication-from-mariadb-10-4.md). However, since auth\_gssapi, unlike unix\_socket, requires client support, to avoid failures when MariaDB is used with third-party drivers, authentication on Windows first attempts password-based `native_authentication`, and only if it fails, falls back to passwordless `auth_gssapi`.

## Client Authentication Plugins

For clients that use the `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) libraries, MariaDB provides one client authentication plugin that is compatible with the `gssapi` authentication plugin:

* `auth_gssapi_client`

When connecting with a [client or utility](../../../clients-and-utilities/) to a server as a user account that authenticates with the `gssapi` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option:

```bash
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

### `auth_gssapi_client`

The `auth_gssapi_client` client authentication plugin receives the principal name from the server, and then uses either the [gss\_init\_sec\_context](https://web.mit.edu/kerberos/krb5-devel/doc/appdev/gssapi.html#initiator-credentials) function (on Unix) or the [InitializeSecurityContext](https://docs.microsoft.com/en-us/windows/desktop/api/sspi/nf-sspi-initializesecuritycontexta) function (on Windows) to establish a security context on the client.

## Support in Client Libraries

### Using the Plugin with MariaDB Connector/C

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) supports `gssapi` authentication using the [client authentication plugins](authentication-plugin-gssapi.md#client-authentication-plugins) mentioned in the previous section.

### Using the Plugin with MariaDB Connector/ODBC

[MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc) supports `gssapi` authentication using the [client authentication plugins](authentication-plugin-gssapi.md#client-authentication-plugins) mentioned in the previous section.

### Using the Plugin with MariaDB Connector/J

[MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) supports `gssapi` authentication. Current documentation can be found [here](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/gssapi-authentication-with-mariadb-connector-j).

### Using the Plugin with MariaDB Connector/Node.js

[MariaDB Connector/Node.js](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs) does not yet support `gssapi` authentication. See [CONJS-72](https://jira.mariadb.org/browse/CONJS-72) for more information.

### Using the Plugin with MySqlConnector for .NET

[MySqlConnector for ADO.NET](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-net/mariadb-connector-net-guide) supports `gssapi` authentication.

The support is transparent. Normally, the connector only needs to be provided the correct user name, and no other parameters are required.

However, this connector also supports the [ServerSPN](https://mysql-net.github.io/MySqlConnector/connection-options) connection string parameter, which can be used for mutual authentication.

#### .NET specific problems/workarounds

When connecting from Unix client to Windows server with ADO.NET, in an Active Directory domain environment, be aware that .NET Core on Unix does not support principal names in UPN(User Principal Name) form, which is default on Windows (e.g machine$@domain.com) . Thus, upon encountering an authentication exception with "server not found in Kerberos database", use one of workarounds below

* Force host-based SPN on server side.
  * For example, this can be done by setting the [gssapi\_principal\_name](authentication-plugin-gssapi.md#gssapi_principal_name) system variable to `HOST/machine` in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).
* Pass host-based SPN on client side.
  * For example, this can be done by setting the connector's [ServerSPN](https://mysql-net.github.io/MySqlConnector/connection-options) connection string parameter to `HOST/machine`.

## System Variables

### `gssapi_keytab_path`

* Description: Defines the path to the server's keytab file.
  * This system variable is only meaningful on Unix.
  * See [Creating a Keytab File on Unix](authentication-plugin-gssapi.md#creating-a-keytab-file) and [Configuring the Path to the Keytab File on Unix](authentication-plugin-gssapi.md#configuring-the-path-to-the-keytab-file-on-unix) for more information.
* Command line: `--gssapi-keytab-path`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: ''
* Introduced: MariaDB 10.1.11

### `gssapi_principal_name`

* Description: Name of the service principal.
  * See [Configuring the Service Principal Name](authentication-plugin-gssapi.md#configuring-the-service-principal-name) for more information.
* Command line: `--gssapi-principal-name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: ''
* Introduced: MariaDB 10.1.11

### `gssapi_mech_name`

* Description: Name of the SSPI package used by server. Can be either 'Kerberos' or 'Negotiate'. Set it to 'Kerberos', to prevent less secure NTLM in domain environments, but leave it as default (Negotiate) to allow non-domain environments (e.g if server does not run in a domain environment).
  * This system variable is only meaningful on Windows.
* Command line: `--gssapi-mech-name`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `Negotiate`
* Valid Values: `Kerberos`, `Negotiate`
* Introduced: MariaDB 10.1.11

## Options

### `gssapi`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--gssapi=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`
* Introduced: MariaDB 10.1.11

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
