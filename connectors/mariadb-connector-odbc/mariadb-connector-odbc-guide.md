# About MariaDB Connector/ODBC

[Download MariaDB Connector/ODBC](https://mariadb.com/downloads/#connectors)

**MariaDB Connector/ODBC** is a database driver that uses the industry standard [Open Database Connectivity (ODBC) API](https://en.wikipedia.org/wiki/Open_Database_Connectivity). Some of the key features of the driver are:

* It is [LGPL-licensed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/faq/licensing-questions/licensing-faq).
* It is compliant with the ODBC 3.5 standard.
* It can be used as a drop-in replacement for MySQL Connector/ODBC.
* It supports both Unicode and ANSI modes.
* It primarily uses the MariaDB/MySQL binary protocol (i.e. server-side [prepared statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements)).

The current release series are:

* MariaDB Connector/ODBC 3.1 is the current stable release series.
* MariaDB Connector/ODBC 3.0 and 2.0 are both previous stable release series.

## Recent Releases

{% hint style="info" %}
The most recent [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes)
{% endhint %}

| Date        | Release                       | Status      | Release Notes                                                                                                                                                        | Changelog                                                                                                                                                           |
| ----------- | ----------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date        | Release                       | Status      | Release Notes                                                                                                                                                        | Changelog                                                                                                                                                           |
| 24 Feb 2025 | MariaDB Connector/ODBC 3.2.5  | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes)  | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-5-changelog) |
| 14 Nov 2024 | MariaDB Connector/ODBC 3.2.4  | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-4-release-notes)  | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-4-changelog) |
| 26 Aug 2024 | MariaDB Connector/ODBC 3.2.3  | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-3-release-notes)  | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-3-changelog) |
| 24 Feb 2025 | MariaDB Connector/ODBC 3.1.21 | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-21-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-21-changelog) |
| 4 Dec 2023  | MariaDB Connector/ODBC 3.1.20 | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-20-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-20-changelog) |
| 7 Jul 2023  | MariaDB Connector/ODBC 3.1.19 | Stable (GA) | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-19-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3-1-19-changelog) |

[see all releases](list-of-mariadb-connector-odbc-releases.md)

## Installing MariaDB Connector/ODBC

MariaDB Connector/ODBC packages can also be downloaded by selecting **ODBC connector** as the **Product** on the following page:

* [#connectors](https://mariadb.com/downloads/#connectors)

See the instructions below for information on how to install the MariaDB Connector/ODBC package for your operating system.

### Installing MariaDB Connector/ODBC on Windows

To install MariaDB Connector/ODBC on Windows, we distribute [MSI packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows). The MSI installation process is fairly straightforward.

MariaDB Connector/ODBC supports the built-in ODBC Driver Manager on Windows, so nothing else needs to be installed. The MSI installation process will even take care of registering MariaDB Connector/ODBC with the ODBC Driver Manager, so that it is ready to use immediately.

It is generally a good idea to download and install both the 32-bit and 64-bit [MSI packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows). Otherwise, the ODBC Driver Manager may sometimes load the wrong version of the driver for your application, which can cause errors like the following:

```
[Microsoft][ODBC Driver Manager] The specified DSN contains an
 architecture mismatch between the Driver and Application.
```

### Installing MariaDB Connector/ODBC on Linux

To install MariaDB Connector/ODBC on Linux, we currently only distribute [binary tarball packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs).

The installation process is fairly easy. First, you need to extract the files from the binary tarball. Then, you need to install the driver's shared library to the appropriate place in your system. The driver's shared library is called `libmaodbc.so` and it is located in either the `lib` directory or the `lib64` directory, depending on whether you downloaded a 32-bit or 64-bit package. The driver's shared library can be installed anywhere, but for simplicity, the instructions below will assume that you are installing it to `/usr/lib64`, which is a common directory for 64-bit shared libraries on many Linux distributions.

Installation steps for some common Linux distributions are shown below. The commands would be similar for other Linux distributions. However, the URL of the package and the installation path may be different.

#### Installing MariaDB Connector/ODBC on RHEL/CentOS

The following commands would download and install MariaDB Connector/ODBC 3.1.7 on RHEL or CentOS 7:

```bash
mkdir odbc_package
cd odbc_package
wget https://downloads.mariadb.com/Connectors/odbc/connector-odbc-3.1.7/mariadb-connector-odbc-3.1.7-ga-rhel7-x86_64.tar.gz
tar -xvzf mariadb-connector-odbc-3.1.7-ga-rhel7-x86_64.tar.gz
sudo install lib64/libmaodbc.so /usr/lib64/
sudo install -d /usr/lib64/mariadb/
sudo install -d /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/auth_gssapi_client.so /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/caching_sha2_password.so /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/client_ed25519.so /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/dialog.so /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/mysql_clear_password.so /usr/lib64/mariadb/plugin/
sudo install lib64/mariadb/plugin/sha256_password.so /usr/lib64/mariadb/plugin/
```

#### Installing MariaDB Connector/ODBC on Debian/Ubuntu

The following commands would download and install MariaDB Connector/ODBC 3.1.7 on Debian or Ubuntu:

```bash
mkdir odbc_package
cd odbc_package
wget https://downloads.mariadb.com/Connectors/odbc/connector-odbc-3.1.7/mariadb-connector-odbc-3.1.7-ga-debian-x86_64.tar.gz
tar -xvzf mariadb-connector-odbc-3.1.7-ga-debian-x86_64.tar.gz
sudo install lib64/libmaodbc.so /usr/lib/
sudo install -d /usr/lib/mariadb/
sudo install -d /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/auth_gssapi_client.so /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/caching_sha2_password.so /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/client_ed25519.so /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/dialog.so /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/mysql_clear_password.so /usr/lib/mariadb/plugin/
sudo install lib/mariadb/plugin/sha256_password.so /usr/lib/mariadb/plugin/
```

These steps may not work on the following operating system versions due to the packaging bug [ODBC-278](https://jira.mariadb.org/browse/ODBC-278):

* Debian 9 (Stretch)
* Debian 10 (Buster)
* Ubuntu 19.10 (Eoan Ermine)
* Ubuntu 20.04 LTS (Focal Fossa)

### Installing MariaDB Connector/ODBC on Mac OS X

To install MariaDB Connector/ODBC on Mac OS X, we distribute [PKG packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-server-pkg-packages-on-macos) for releases starting with MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC supports the built-in [iODBC](https://www.iodbc.org) Driver Manager on Mac OS X, so nothing else needs to be installed.

### Installing MariaDB Connector/ODBC from Source

See [Building MariaDB Connector/ODBC from Source](building-mariadb-connectorodbc-from-source.md) for information on how to build MariaDB Connector/ODBC from source.

## Installing UnixODBC on Linux

In order to use MariaDB Connector/ODBC on Linux, you will also need to install a supported Driver Manager. The only Driver Manager that we currently support on Linux is [UnixODBC](https://www.unixodbc.org/). In most Linux distributions, you can install UnixODBC by using your Linux distribution's package manager.

For example, the following command would install the `unixODBC` package on RHEL, CentOS, and similar Linux distributions:

```bash
sudo yum install unixODBC
```

And the following command would install the `unixodbc` and `odbcinst` packages on Debian, Ubuntu, and similar Linux distributions:

```bash
sudo apt-get update
sudo apt-get install unixodbc odbcinst
```

If you plan to compile an application from source against MariaDB Connector/ODBC and UnixODBC, then you also need the development header files that define the ODBC API function prototypes, ODBC data types, etc. In most Linux distributions, you can install these UnixODBC development files by using your Linux distribution's package manager.

For example, the following command would install the `unixODBC-devel` package on RHEL, CentOS, and similar Linux distributions:

```bash
sudo yum install unixODBC-devel
```

And the following command would install the `unixodbc-dev` package on Debian, Ubuntu, and similar Linux distributions:

```bash
sudo apt-get update
sudo apt-get install unixodbc-dev
```

If you can't find the UnixODBC packages with your Linux distribution's package manager, then you may want to look at the download page at [UnixODBC.org](https://www.unixodbc.org/) for other installation options.

## Creating a Data Source with MariaDB Connector/ODBC

See [Creating a Data Source with MariaDB Connector/ODBC](creating-a-data-source-with-mariadb-connectorodbc.md) for information on how to create a data source.

## Installing Client Authentication Plugins

Authentication plugins are all compiled in statically on Windows since [3.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-18-release-notes)

In MariaDB Connector/ODBC 3.1 and later, MariaDB Connector/ODBC bundles client authentication plugins with the connector.

In MariaDB Connector/ODBC 3.0 and before, MariaDB Connector/ODBC does not bundle client authentication plugins with the connector.

The connector will need to use client authentication plugins in the following scenarios:

* The server uses the [pam](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam) authentication plugin.
* The server uses the [gssapi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin.
* The server uses the [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) authentication plugin.
* You are connecting to a MySQL server that uses one of the [SHA-256](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) authentication plugins--i.e. either the [sha256_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html) or the [caching_sha2_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html) authentication plugins. However, MariaDB Connector/ODBC is more compatible with MariaDB than with MySQL, and it may not yet fully support these MySQL-only authentication plugins. See [ODBC-241](https://jira.mariadb.org/browse/ODBC-241) for more information.

If you need client authentication plugins in a version which does not bundle them with the connector, then you will also need to install [MariaDB Connector/C](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/about-mariadb-connector-c/README.md), which installs the client authentication plugins as shared libraries, which can be used by MariaDB Connector/ODBC.

MariaDB Connector/ODBC can be configured to use MariaDB Connector/C's client authentication plugins by setting the `PLUGINDIR` parameter to the MariaDB Connector/C's plugin directory. The plugin directory can also be specified with the `MARIADB_PLUGIN_DIR` environment variable.

On Windows, MariaDB Connector/C often installs plugins to one of the following directories:

* `C:\Program Files\MariaDB\MariaDB Connector C\lib\plugin`
* `C:\Program Files (x86)\MariaDB\MariaDB Connector C\lib\plugin`

On Linux, MariaDB Connector/C often installs client authentication plugins to one of the following directories:

* `/usr/lib64/mysql/plugin`
* `/usr/lib/mysql/plugin`

When you install the client authentication plugins, ensure that they are for the same architecture as your MariaDB Connector/ODBC installation. If your MariaDB Connector/ODBC installation is 64-bit, then you should install 64-bit client authentication plugins. Likewise, if your MariaDB Connector/ODBC installation is 32-bit, then you should install 32-bit client authentication plugins.

## Parameters

### DSN-Related Parameters

* `DSN`: Name of the DSN
* `Driver`: The name of the MariaDB ODBC Driver. On Windows, this must be `{MariaDB ODBC 3.1 Driver}` for 3.1 drivers, or for versions from other release series, you must use the corresponding version number for that release series. On Linux, either this must be a path to the driver's shared library or it must match the `Driver` name that you provided when you [configured the Driver with UnixODBC](creating-a-data-source-with-mariadb-connectorodbc.md#configuring-mariadb-connectorodbc-as-a-unixodbc-driver-on-linux).
* `Description`: Description of the data source.
* `SaveFile`: Save a string representation of the DSN to this file.
* `FileDSN`: The file where the string representation of the DSN can be read.

### Logging-Related Parameters

* `Trace`: Whether to enable the ODBC trace log.
* `TraceFile`: If the ODBC trace log is enabled, then this is the path to the output file.

### General Connection Parameters

* `SERVER`: name or IP of the MariaDB database server. Aliases: `SERVERNAME`
* `USER`: user name for database authentication. Aliases: `UID`,
* `PASSWORD`: password for database authentication. Aliases: `PWD`
* `DATABASE`: default database. Aliases: `DB`
* `PORT`: TCP/IP Port of the database server
* `OPTION`: For MySQL Connector/ODBC compatibility. Aliases: `OPTIONS`. Here are used bits meaning:
  * 0(1) - Currently is not used
  * 1(2) - Tells connector to return the number of matched rows instead of number of changed rows
  * 4(16) - See `NO_PROMPT`
  * 5(32) - Forces use of dynamic cursor
  * 6(64) - Forbids the use of database.tablename.column syntax
  * 7(128) Allows `[load-data-infile|LOAD DATA INFILE LOCAL]`
  * 11(2048) - Tells connector to use compression protocol
  * 13(8192) - See `NAMEDPIPE`
  * 16(65536) - See `USE_MYCNF`
  * 21(2097152) - See `FORWARDONLY`
  * 22(4194304) - See `AUTO_RECONNECT`
  * 26(67108864) - Allows to send multiple statements in one query
* `NAMEDPIPE`: This parameter accepts a boolean value, where all non-zero values are treated as true. When this parameter is enabled, the value of the `SOCKET` parameter is treated as a named pipe name, rather than a path to a Unix domain socket. Alternatively, setting the 13th bit in the `OPTIONS` bitmask is equivalent to setting this parameter. This parameter only has an effect on Windows.
* `TCPIP`: This parameter has the opposite meaning of the `NAMEDPIPE` parameter. When `TCPIP=0` is set, `NAMEDPIPE=1` is effectively set. This parameter only has an effect on Windows.
* `SOCKET`: By default, this parameter accepts a path to a Unix domain socket. If `NAMEDPIPE=1` is set on Windows, this parameter accepts the name of a named pipe instead. When this parameter is specified, the value of the `SERVER` parameter and its aliases are ignored.
* `INITSTMT`: SQL command(s) to be run at connection time
* `CONN_TIMEOUT` : connect timeout in seconds
* `AUTO_RECONNECT`: enabling/disabling automatic reconnect, the same as setting/resetting 22th(4194304) `OPTIONS` bit
* `NO_PROMPT`: suppresses prompt dialog display at the connection time. This has the same meaning as setting/resetting bit #4(16) of the `OPTIONS`
* `CHARSET`: connection character set. Connector assumes that all incoming string data is encoded in this character set, and uses it if recoding to/from Unicode(utf16) encoding is required.
* `PLUGIN_DIR`: Specify the location of client plugins. Starting from the version 3.1.12, all authentication plugins are compiled in for Windows releases, thus with option becomes Linux/MacOS-specific
  * The plugin directory can also be specified with the `MARIADB_PLUGIN_DIR` environment variable.
  * See [Installing Client Authentication Plugins](mariadb-connector-odbc-guide.md#installing-client-authentication-plugins) for more information.
* `USE_MYCNF`: whether to read options from the \[odbc] option group in the system's default `my.cnf` option file.
  * Since MariaDB Connector/ODBC relies on MariaDB Connector/C, see [Configuring MariaDB Connector/C with Option Files](../mariadb-connector-c/configuring-mariadb-connectorc-with-option-files.md) for more information.
  * This parameter is available starting with MariaDB Connector/ODBC versions 2.0.19, 3.0.9, and 3.1.1.
* `SERVERKEY`: Specifies the name of the file which contains the RSA public key of the database server. The format of this file must be in PEM format. This option is used by the [caching_sha2_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) client authentication plugin.
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.4.
* `INTERACTIVE`: tells server, that the client is interactive, and it should use interactive\_timeout for this connection
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.10.
* `FORWARDONLY`: forces all cursors to be forward only.
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.10
* `PREPONCLIENT`: forces SQLPrepare to use client side prepare if possible.
  * This parameter is available starting with MariaDB Connector/ODBC version 3.2.0
* `ATTR`: option to set connection attributes. Using it makes sense only if performance schema is enabled on server. Format: `ATTR={<attrname1>=<attrvalue1>[,<attrname2=attrvalue2,...]}`
  * This parameter is available starting with MariaDB Connector/ODBC version 3.2.0
* `EDSERVER`: forces SQLExecDirect to use server side prepare if possible. It is useful if binary protocol is preferable to use for the queries.
  * This parameter is available starting with MariaDB Connector/ODBC version 3.2.5

#### General Connection Parameters Example

For example, to set these parameters in a connection string via C/C++ code, you could do something like the following:

```c
SQLWCHAR *ConnStr= L"Driver={MariaDB ODBC 3.2 Driver};SERVER=mydatabase.mydomain.com;USER=odbc_user;PASSWORD=odbc_pw;DATABASE=odbc_test;PORT=3306";
```

To set these same parameters in a UnixODBC or iODBC configuration file, you could do something like the following:

```
[MariaDB-server]
Description = MariaDB server
Driver = MariaDB ODBC 3.2 Driver
Trace = Yes
TraceFile = /tmp/trace.log
SERVER = mydatabase.mydomain.com
USER = odbc_user
PASSWORD = odbc_pw
DATABASE = odbc_test
PORT = 3306
```

### TLS-Related Connection Parameters

The following TLS-related connection parameters are available in MariaDB Connector/ODBC 3.0 and later:

* `SSLCERT`: Defines a path to the X509 certificate file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This parameter requires that you use the absolute path, not a relative path.
* `SSLKEY`: Defines a path to a private key file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). The key file must be unencrypted. This parameter requires that you use the absolute path, not a relative path.
* `SSLCA`: Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This parameter requires that you use the absolute path, not a relative path.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.
* `SSLCAPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This parameter requires that you use the absolute path, not a relative path. The directory specified by this parameter needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.
  * This parameter is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this parameter is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* `SSLCIPHER`: Defines a list of permitted ciphers or cipher suites to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption)..
* `SSLVERIFY`: Enables (or disables) [server certificate verification](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#server-certificate-verification).
* `SSLCRL`: Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This parameter requires that you use the absolute path, not a relative path.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information.
  * This parameter is only supported if the connector was built with OpenSSL or Schannel. If the connector was built with GnuTLS, then this parameter is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* `SSLCRLPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This parameter requires that you use the absolute path, not a relative path. The directory specified by this parameter needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information.
  * This parameter is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this parameter is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* `TLSVERSION`: Specify which [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) versions are allowed. The value can be a comma-separated list of string names consisting of TLSv1.1, TLSv1.2, and TLSv1.3, or it can be an integer value that represents a bitmap, where TLSv1.1 corresponds to bit 1, TLSv1.2 corresponds to bit 2, and TLSv1.3 corresponds to bit 3.
  * This parameter is available starting with MariaDB Connector/ODBC versions 3.0.9 and 3.1.1.
* `FORCETLS`: Whether to force [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption).
  * This parameter is available starting with MariaDB Connector/ODBC versions 3.0.9 and 3.1.1.
* `TLSPEERFP`: Specify the SHA1 fingerprint of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake. Aliases: `SSLFP`
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.4.
* `TLSPEERFPLIST`: Specify a file which contains one or more SHA1 fingerprints of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake. Aliases: `SSLFPLIST`
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.4.
* `TLSKEYPWD`: Specify a passphrase for a passphrase-protected private key, as configured by the SSLKEY option. This option is only supported if the connector was built with OpenSSL or GnuTLS. If the connector was built with Schannel, then this option is not supported.
  * This parameter is available starting with MariaDB Connector/ODBC version 3.1.8.

#### TLS-Related Connection Parameters Examples

**Two-Way TLS Example**

Two-way TLS means that both the client and server provide TLS certificates and keys.

For example, to set these parameters in a connection string via C/C++ code, you could do something like the following:

```c
SQLWCHAR *ConnStr= L"Driver={MariaDB ODBC 3.2 Driver};SERVER=mydatabase.mydomain.com;USER=odbc_user;PASSWORD=odbc_pw;DATABASE=odbc_test;PORT=3306;SSLCERT=/etc/my.cnf.d/certificates/client-cert.pem;SSLKEY=/etc/my.cnf.d/certificates/client-key.pem;SSLCA=/etc/my.cnf.d/certificates/ca.pem;SSLVERIFY=1";
```

To set these same parameters in a UnixODBC or iODBC configuration file, you could do something like the following:

```
[MariaDB-server]
Description = MariaDB server
Driver = MariaDB ODBC 3.2 Driver
Trace = Yes
TraceFile = /tmp/trace.log
SERVER = mydatabase.mydomain.com
USER = odbc_user
PASSWORD = odbc_pw
DATABASE = odbc_test
PORT = 3306
SSLCERT = /etc/my.cnf.d/certificates/client-cert.pem
SSLKEY = /etc/my.cnf.d/certificates/client-key.pem
SSLCA = /etc/my.cnf.d/certificates/ca.pem
SSLVERIFY = 1
```

**One-Way TLS Examples**

**One-Way TLS with Server Certificate Verification Example**

One-way TLS means that only the server provides TLS certificates and keys. [Server certificate verification](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#server-certificate-verification) means that the client verifies that the certificate belongs to the server.

For example, to set these parameters in a connection string via C/C++ code, you could do something like the following:

```c
SQLWCHAR *ConnStr= L"Driver={MariaDB ODBC 3.2 Driver};SERVER=mydatabase.mydomain.com;USER=odbc_user;PASSWORD=odbc_pw;DATABASE=odbc_test;PORT=3306;SSLCA=/etc/my.cnf.d/certificates/ca.pem;SSLVERIFY=1";
```

To set these same parameters in a UnixODBC or iODBC configuration file, you could do something like the following:

```
[MariaDB-server]
Description = MariaDB server
Driver = MariaDB ODBC 3.2 Driver
Trace = Yes
TraceFile = /tmp/trace.log
SERVER = mydatabase.mydomain.com
USER = odbc_user
PASSWORD = odbc_pw
DATABASE = odbc_test
PORT = 3306
SSLCA = /etc/my.cnf.d/certificates/ca.pem
SSLVERIFY = 1
```

**One-Way TLS without Server Certificate Verification Example**

One-way TLS means that only the server provides TLS certificates and keys.

For example, to set these parameters in a connection string via C/C++ code, you could do something like the following:

```c
SQLWCHAR *ConnStr= L"Driver={MariaDB ODBC 3.2 Driver};SERVER=mydatabase.mydomain.com;USER=odbc_user;PASSWORD=odbc_pw;DATABASE=odbc_test;PORT=3306;SSLCIPHER=DHE-RSA-AES256-GCM-SHA384";
```

To set these same parameters in a UnixODBC or iODBC configuration file, you could do something like the following:

```
[MariaDB-server]
Description = MariaDB server
Driver = MariaDB ODBC 3.2 Driver
Trace = Yes
TraceFile = /tmp/trace.log
SERVER = mydatabase.mydomain.com
USER = odbc_user
PASSWORD = odbc_pw
DATABASE = odbc_test
PORT = 3306
SSLCIPHER = DHE-RSA-AES256-GCM-SHA384
```

### Data Source Specific Attributes

ODBC 3.8 allows drivers to define and use their own connection and statement attributes. MariaDB Connector/ODBC conforms ODBC 3.8 starting from 3.2 release series. In the version 3.2.5 we introduce our first MariaDB specific statement and connection attribute types.

Independence from the data source is one of the greatest values that using of the ODBC gives to application developers, and use of such attributes won't cause the vendor lock, i.e. dependency on concrete ODBC driver. If application sets these attributes with other 3.8 conforming driver, it will simply get the HYC00 error "Optional feature not implemented". If the driver manager or the driver does not support ODBC 3.8, it will return error about unknown attribute HY024. In any case the application should simply ignore the error(or process it in some way but not to stop normal execution) and using of these attributes with other data sources will not have any bad outcomes, while improving performance if used with the data source they have been designed for MariaDB Connector/ODBC in this case.

The values of these attribute types are defined in the sqlmariadb.h that will be included in our distribution packages and installed under include/mariadb. However application developers might consider to use attribute type literal values and not their defined names in order to avoid extra build dependency.

Here is the list of currently supported attributes

* `SQL_ATTR_EXECDIRECT_ON_SERVER`=`25100` Can be set at statement or connection level.\
  It controls if SQLExecDirect should use server(if set to `SQL_TRUE`) or client side(if set to `SQL_FALSE`, the default) prepared statements. At the connection level it will define default attribute value for all statements created for the connection and is equivalent of use of the `EDSERVER` connection string option. The type of the attribute value is `SQLLEN`.

To set the attribute value:

```c
// If sqlmariadb.h included
// This makes Stmt to use server side prepared statement in SQLExecDirect
SQLSetStmtAttr(Stmt, SQL_ATTR_EXECDIRECT_ON_SERVER, (SQLPOINTER)SQL_TRUE, 0);
// This makes all statements created on Connection after this, to use client side prepared statement in
// SQLExecDirect, unless attribute is set to different value for that statement handle
SQLSetConnectAttr(Conn, SQL_ATTR_EXECDIRECT_ON_SERVER, (SQLPOINTER)SQL_FALSE, 0);

// If sqlmariadb.h is *not* included
// This makes Stmt to use client side prepared statement in SQLExecDirect
SQLSetStmtAttr(Stmt, SQL_ATTR_EXECDIRECT_ON_SERVER, (SQLPOINTER)SQL_FALSE, 0);
// This makes all statements created on Connection after this, to use server side prepared statement in
// SQLExecDirect, unless attribute is set to different value for that statement handle
SQLSetConnectAttr(Conn, SQL_ATTR_EXECDIRECT_ON_SERVER, (SQLPOINTER)SQL_TRUE, 0);
```

To read the attribute value

```c
SQLLEN attributeValue= -1;
// If sqlmariadb.h included
SQLGetStmtAttr(Stmt, SQL_ATTR_EXECDIRECT_ON_SERVER, &attributeValue, 0, NULL);
if (attributeValue == SQL_TRUE) {
// SQLExecDirect will prepare a query on the server and use binary protocol
}
SQLGetConnectAttr(Conn, SQL_ATTR_EXECDIRECT_ON_SERVER, &attributeValue, 0, NULL);

// If sqlmariadb.h is *not* included
SQLGetStmtAttr(Stmt, 25100,  &attributeValue, 0, NULL);
if (attributeValue == SQL_FALSE) {
// SQLExecDirect will prepare a query on the client and use text protocol
}
SQLGetConnectAttr(Conn, 25100, &attributeValue, 0, NULL);
```

**This attribute is available starting with MariaDB Connector/ODBC version 3.2.5.**

* `SQL_ATTR_PREPARE_ON_CLIENT`=`25101` Can be set at statement or connection level. It controls if SQLPrepare should use server(if set to `SQL_FALSE`, the default) or client side(if set to `SQL_TRUE`) prepared statements. At the connection level it will define default attribute value for all statements created for the connection and is equivalent of use of the `PREPONCLIENT` connection string option. The type of the attribute value is `SQLLEN`.

To set the attribute value:

```c
// If sqlmariadb.h included
// This makes Stmt to use client side prepared statement in SQLPrepare
SQLSetStmtAttr(Stmt, SQL_ATTR_PREPARE_ON_CLIENT, (SQLPOINTER)SQL_TRUE, 0);
// This makes all statements created on Conn after this, to use server side prepared statement in
// SQLPrepare, unless attribute is set to different value for that statement handle
SQLSetConnectAttr(Conn, SQL_ATTR_PREPARE_ON_CLIENT, (SQLPOINTER)SQL_FALSE, 0);

// If sqlmariadb.h is *not* included
// This makes Stmt to use server side prepared statement in SQLPrepare
SQLSetStmtAttr(Stmt, 25101, (SQLPOINTER)SQL_FALSE, 0);
// This makes all statements created on Conn after this, to use client side prepared statement in
// SQLPrepare, unless attribute is set to different value for that statement handle
SQLSetConnectAttr(Conn, 25101, (SQLPOINTER)SQL_TRUE, 0);
```

To read the attribute value

```c
SQLLEN attributeValue= -1;
// If sqlmariadb.h included
SQLGetStmtAttr(Stmt, SQL_ATTR_PREPARE_ON_CLIENT, &attributeValue, 0, NULL);
if (attributeValue == SQL_TRUE) {
// SQLPrepare will prepare a query on the client side and use text protocol
}
SQLGetConnectAttr(Conn, SQL_ATTR_PREPARE_ON_CLIENT, &attributeValue, 0, NULL);

// If sqlmariadb.h is *not* included
SQLGetStmtAttr(Stmt, 25101,  &attributeValue, 0, NULL);
if (attributeValue == SQL_FALSE) {
// SQLPrepare will prepare a query on the server side and use binary protocol
}
SQLGetConnectAttr(Conn, 25101, &attributeValue, 0, NULL);
```

**This attribute is available starting with MariaDB Connector/ODBC version 3.2.5.**

## Known Issues

### Multiple Statement Execution

Multiple statement execution is not fully supported. This means that if you try to prepare a multi-statement query where one of statements depends on the execution result of one of the previous statements, then it may fail. For example, the following may return an error in some versions:

```c
SQLPrepare(hstmt, "CREATE VIEW some_table_view AS SELECT * FROM some_table;SELECT * FROM some_table_view ", SQL_NTS);
```

Some bugs related to this have been fixed, such as [ODBC-159](https://jira.mariadb.org/browse/ODBC-159). If you find similar cases, please [report a bug](mariadb-connector-odbc-guide.md#reporting-bugs).

3.2 eliminates this issue, but option allowing to send multiple statements in one query(bit 26 = 67108864) has to be selected.

### Authenticating with PAM

If you try to authenticate with a user account that is configured to use the [pam](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam) authentication plugin, then you might see one of the following errors.

You might see this error:

```
Authentication plugin 'dialog' cannot be loaded: The specified module could not be found.
```

Or if the server has the [pam_use_cleartext_plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam#pam_use_cleartext_plugin) system variable set, then you might see this error instead:

```
Authentication plugin 'mysql_clear_password' cannot be loaded: The specified module could not be found.
```

These errors occur because the [pam](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam) authentication plugin requires specific client authentication plugins in order to work, and MariaDB Connector/ODBC does not install these plugins. To fix the problem, please [install the client authentication plugins](mariadb-connector-odbc-guide.md#installing-client-authentication-plugins).

See [ODBC-23](https://jira.mariadb.org/browse/ODBC-23) for more information.

Authentication plugins are all compiled in statically on Windows since [3.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/odbc/mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-18-release-notes)

## Reporting Bugs

If you find a bug, please report it via the [ODBC project](https://jira.mariadb.org/projects/ODBC/issues) on [MariaDB's Jira bug tracker](https://jira.mariadb.org).

## Source Code

The source code is available at the [mariadb-connector-odbc repository](https://github.com/MariaDB/mariadb-connector-odbc) on GitHub.

## License

GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

For licensing questions, see the [Licensing FAQ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/faq/licensing-questions/licensing-faq).

{% @marketo/form formId="4316" %}
