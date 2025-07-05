# Connect with MariaDB Connector/C++

MariaDB Connector/C++ enables C++ applications to establish client connections to MariaDB database products over TLS.

## Connection URL Syntax

MariaDB Connector/C++ supports two different formats for connection URLs, the [JDBC syntax](connect-with-mariadb-connectorcpp.md#jdbc-syntax) and the [compatibility syntax](connect-with-mariadb-connectorcpp.md#compatibility-syntax).

### JDBC Syntax

MariaDB Connector/C++ supports a connection URL syntax similar to JDBC.

The JDBC syntax for connection URLs is:

```c++
jdbc:mariadb://<hostDescription>/[<database>] [?<key1>=<value1>[&<key2>=<value2>]]
```

The connection URL:

* Requires `jdbc:mariadb://` as the protocol component.
* Requires the [host description](connect-with-mariadb-connectorcpp.md#host-description) in the `hostDescription` field.
* Accepts an optional database name. If no database is provided, the connection will not select a database.
* Accepts [optional connection parameters](connect-with-mariadb-connectorcpp.md#optional-connection-parameters) in `key=value` format.

Some example connection URLs using the JDBC syntax:

* `jdbc:mariadb:192.0.2.1/`
* `jdbc:mariadb:192.0.2.1/?user=db_user&password=db_user_password`
* `jdbc:mariadb:192.0.2.1/database?user=db_user&password=db_user_password`
* `jdbc:mariadb:192.0.2.1:3307/database?user=db_user&password=db_user_password`
* `jdbc:mariadb:mariadb.example.com/database?user=db_user&password=db_user_password`
* `jdbc:mariadb:mariadb.example.com:3307/database?user=db_user&password=db_user_password`
* `jdbc:mariadb:localhost/database?localSocket=/var/lib/mysql/mysql.sock&user=db_user&password=db_user_password`

### Compatibility Syntax

MariaDB Connector/C++ supports a connection URL syntax for compatibility with MySQL Connector/C++.

The compatibility syntax for connection URLs is only supported for the [sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method.

The compatibility syntax for connection URLs is:

```c++
(tcp|unix|pipe)://<hostDescription>[/]
```

The connection URL:

* Requires tcp: as the protocol component to connect via TCP/IP.
* Requires unix: as the protocol component to connect via Unix socket file. The `hostDescription` field should be set to `localhost`, and the `localSocket` [connection parameter](connect-with-mariadb-connectorcpp.md#optional-connection-parameters) should be set in the properties when you call the [sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method.
* Requires `pipe://` as the protocol component to connect via Windows named pipe. The `hostDescription` field should be set to `localhost`, and the `pipe` [connection parameter](connect-with-mariadb-connectorcpp.md#optional-connection-parameters) should be set in the properties when you call the [sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method.
* Requires the [host description](connect-with-mariadb-connectorcpp.md#host-description) in the `hostDescription` field.

Some example connection URLs using the compatibility syntax:

* `tcp:192.0.2.1/`
* `tcp:192.0.2.1:3307/`
* `tcp:mariadb.example.com/`
* `tcp:mariadb.example.com:3307/`
* `unix:localhost/`
* `pipe:localhost/`

## Host Description

The host description syntax for MariaDB Connector/C++ is:

```c++
<host>[:<portNumber>]
```

The host description:

* Requires the `host` field to set the destination host to connect.
* Accepts the `host` field as a host name, IPv4 address, or IPv6 address to connect via TCP/IP.
* Accepts the `host` field as `localhost` to connect via Unix socket file, when the `localSocket` [connection parameter](connect-with-mariadb-connectorcpp.md#optional-connection-parameters) is also set.
* Accepts an optional `portNumber` field to set the TCP/IP port. If it is not provided, the TCP port `3306` is used by default.

Some example host descriptions:

* `192.0.2.1`
* `192.0.2.1:3307`
* `mariadb.example.com`
* `mariadb.example.com:3307`

```c++
jdbc:mariadb://192.0.2.1:3306/database?user=db_user&password=db_user_password
```

## Optional Connection Parameters

MariaDB Connector/C++ accepts optional connection parameters in multiple contexts for both [connection methods](connect-with-mariadb-connectorcpp.md#connection-methods):

* They can be specified in a [connection URL with JDBC syntax](connect-with-mariadb-connectorcpp.md#jdbc_syntax).
* They can be specified in a `Properties` object.

MariaDB Connector/C++ supports several optional connection parameters:

| Parameter Name           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type   | Default         | Aliases                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------------- | ------------------------------------------------------------------------------------------------------------------- |
| Parameter Name           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type   | Default         | Aliases                                                                                                             |
| autoReconnect            | Defines whether the connector automatically reconnects after a connection failure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | bool   | FALSE           | • OPT\_RECONNECT                                                                                                    |
| cachePrepStmts           | Defines whether the prepared statement cache is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | bool   | FALSE           |                                                                                                                     |
| connectTimeout           | Defines the connect timeout value in milliseconds. When set to 0, there is no connect timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | int    | 30000           |                                                                                                                     |
| enabledTlsCipherSuites   | A list of permitted ciphers or cipher suites to use for TLS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | string |                 | • enabledSslCipherSuites • enabledSSLCipherSuites                                                                   |
| hostName                 | The host name, IPv4 address, or IPv6 address to connect via TCP/IP. This parameter is only supported by the [sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method that does not use a connection URL. If a [connection URL](connect-with-mariadb-connectorcpp.md#connection-url-syntax) is provided, the host name, IPv4 address, or IPv6 address should be specified in the connection URL.                                                                                                                                                                                                    |        |                 |                                                                                                                     |
| jdbcCompliantTruncation  | This mode is enabled by default. This mode configures the connector to add STRICT\_TRANS\_TABLES to [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode), which causes ES to handle truncation issues as errors instead of warnings.                                                                                                                                                                                                                                                                                                                                                  | bool   | TRUE            |                                                                                                                     |
| keyPassword              | Password for the private key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | string |                 | • MARIADB\_OPT\_TLS\_PASSPHRASE                                                                                     |
| localSocket              | Defines the Unix socket file to use for connections to localhost via Unix domain socket. Specify the path of Unix socket file, which can be obtained by querying the [socket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#socket) system variable: SHOW GLOBAL VARIABLES LIKE'socket';                                                                                                                                                                                                                                                               | string |                 | • socket ([sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method only)   |
| log                      | Non-zero value turns on logging and determines logging level. 0 = no logging 1 = error 2 = warning 3 = info 4 = debug 5 = trace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | int    | 0               |                                                                                                                     |
| logname                  | The name of file to write the log in. If logname set, and log is not, log will be set to 1(error). Default name is mariadbccpp.log, and it's written to %TEMP% or %USERPROFILE% or current dir on Windows, and in $HOME or in /tmp on other systems. Logging is synchronized between threads, but not between processes.                                                                                                                                                                                                                                                                                                                    | string | mariadbccpp.log |                                                                                                                     |
| password                 | Defines the password of the user account to connect with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |        |                 |                                                                                                                     |
| pipe                     | Defines the name of the named pipe to use for connections to localhost via named pipe on Windows. Specify the name of the named pipe, which is MySQL by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | string |                 |                                                                                                                     |
| prepStmtCacheSize        | Defines the number of prepared statements that are cached for each connection. This parameter only applies if cachePrepStmts is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | int    | 250             |                                                                                                                     |
| prepStmtCacheSqlLimit    | Defines the maximum length for a prepared statement in the cache. This parameter only applies if cachePrepStmts is enabled. This value consists of length of query itself + length of schema name + 1                                                                                                                                                                                                                                                                                                                                                                                                                                       | int    | 2048            |                                                                                                                     |
| rewriteBatchedStatements | An optimized mode of executeBatch/executeLargeBatch PreparedStatement methods execution. For INSERT queries, the connector will construct a single query using batch parameter sets. If used with useBulkStmts, rewriteBatchedStatements takes precedence.                                                                                                                                                                                                                                                                                                                                                                                  |        |                 |                                                                                                                     |
| schema                   | The database to select for the connection. If no database is provided, the connection will not select a database. This parameter is only supported by the [sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method that does not use a connection URL. If a [connection URL](connect-with-mariadb-connectorcpp.md#connection-url-syntax) is provided, the database should be specified in the connection URL.                                                                                                                                                                                      |        |                 |                                                                                                                     |
| serverRsaPublicKeyFile   | The name of the file that contains the RSA public key of the database server. The format of this file must be in PEM format. This option is used by the caching\_sha2\_password client authentication plugin.                                                                                                                                                                                                                                                                                                                                                                                                                               | string |                 | • rsaKey                                                                                                            |
| socketTimeout            | Defines the network socket timeout (SO\_TIMEOUT) in milliseconds. When set to 0, there is no socket timeout. This connection parameter is not intended to set a maximum time for statements. To set a maximum time for statements, please see the [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_statement_time) system variable.                                                                                                                                                                                            | int    | 0               | • OPT\_READ\_TIMEOUT                                                                                                |
| tcpRcvBuf                | The buffer size for TCP/IP and socket communication. tcpSndBuf changes the same buffer value, and the biggest value of the two is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | int    | 0x4000          | • tcpSndBuf                                                                                                         |
| tcpSndBuf                | The buffer size for TCP/IP and socket communication. tcpRcvBuf changes the same buffer value, and the biggest value of the two is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | int    | 0x4000          | • tcpRcvBuf                                                                                                         |
| tlsCA                    | A path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string |                 | • tlsCa • sslCA                                                                                                     |
| tlsCAPath                | A path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use. The directory specified by this option must be processed by the openssl rehash command. This option is only supported if the connector was built with OpenSSL.                                                                                                                                                                                                                                                                                                                     | string |                 | • tlsCaPath • sslCAPath                                                                                             |
| tlsCert                  | Path to the X509 certificate file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | string |                 | • sslCert                                                                                                           |
| tlsCRL                   | Path to a PEM file that should contain one or more revoked X509 certificates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | string |                 | • tlsCrl • sslCRL                                                                                                   |
| tlsCRLPath               | A path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate. The directory specified by this option must be processed by the openssl rehash command. This option is only supported if the connector was built with OpenSSL.                                                                                                                                                                                                                                                                                                                                                             | string |                 | • tlsCrlPath • sslCRLPath                                                                                           |
| tlsKey                   | File path to a private key file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | string |                 | • sslKey                                                                                                            |
| tlsPeerFP                | A SHA1 fingerprint of a server certificate for validation during the TLS handshake.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | string |                 | • tlsPeerFp • MARIADB\_OPT\_SSL\_FP                                                                                 |
| tlsPeerFPList            | A file containing one or more SHA1 fingerprints of server certificates for validation during the TLS handshake.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | string |                 | • tlsPeerFpList • MARIADB\_OPT\_SSL\_FP\_LIST                                                                       |
| trustServerCertificate   | When using TLS, do not check server's certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | bool   | TRUE            |                                                                                                                     |
| useBulkStmts             | An optimized mode of executeBatch/executeLargeBatch PreparedStatement methods execution that uses the MariaDB bulk execution feature. If used with rewriteBatchedStatements, rewriteBatchedStatements takes precedence.                                                                                                                                                                                                                                                                                                                                                                                                                     |        |                 |                                                                                                                     |
| useCompression           | Compresses network traffic between the client and server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | bool   | FALSE           | • CLIENT\_COMPRESS                                                                                                  |
| user                     | Defines the user name of the user account to connect with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |        |                 | • userName ([sql::Driver::connect()](connect-with-mariadb-connectorcpp.md#sqldriverconnect) connection method only) |
| useServerPrepStmts       | Defines whether the connector uses server-side prepared statements using the [PREPARE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/prepare-statement), [EXECUTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/execute-statement), and [DROP PREPARE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements/deallocate-drop-prepare) statements. By default, the connector uses client-side prepared statements. | bool   | FALSE           |                                                                                                                     |
| useTls                   | Whether to force TLS. This enables TLS with the default system settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | bool   | FALSE           | • useSsl • useSSL                                                                                                   |

## Connection Methods

Two categories of methods are available to establish a connection.

### sql::Driver::connect()

MariaDB Connector/C++ can connect using the non-static connect() methods in the sql::Driver class.

The non-static connect() methods in the sql::Driver class have the following prototypes:

* Connection\* connect(const SQLString& url, Properties& props);
* Connection\* connect(const SQLString& host, const SQLString& user, const SQLString& pwd);
* Connection\* connect(const Properties& props);

The non-static connect() methods in the sql::Driver class:

* Require an instance of the sql::Driver class to establish a connection.
* Accept both forms of [connection URL syntax](connect-with-mariadb-connectorcpp.md#connection-url-syntax).
* Provide two prototypes that do not use connection URLs at all.
* Return nullptr as the Connection\* value when an error occurs, so applications should check the return value before use.

For example:

```c++
// Instantiate Driver
sql::Driver* driver = sql::mariadb::get_driver_instance();

// Configure Connection
// The URL or TCP connection string format is
// ``jdbc:mariadb://host:port/database``.
sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

// Use a properties map for the other connection options
sql::Properties properties({
      {"user", "db_user"},
      {"password", "db_user_password"},
   });

// Establish Connection
// Use a smart pointer for extra safety
std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

if (!conn) {
   cerr << "Invalid database connection" << endl;
   exit (EXIT_FAILURE);
}
```

### sql::DriverManager::getConnection()

MariaDB Connector/C++ can connect using the static getConnection() methods in the sql::DriverManager class.

The static getConnection() methods in the sql::DriverManager class have the following prototypes:

* static Connection\* getConnection(const SQLString& url);
* static Connection\* getConnection(const SQLString& url, Properties& props);
* static Connection\* getConnection(const SQLString& url, const SQLString& user, const SQLString& pwd);

The static getConnection() methods in the sql::DriverManager class:

* Do not require an instance of the sql::DriverManager class to establish a connection, because they are static.
* Accept only the [JDBC syntax for connection URLs](connect-with-mariadb-connectorcpp.md#jdbc-syntax).
* Throw an exception when an error occurs, so applications should use try { .. } catch ( .. ) { .. } to catch the exception.

For example:

```c++
try {
    // Configure Connection
    // The URL or TCP connection string format is
    // ``jdbc:mariadb://host:port/database``.
    sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

    // Use a properties map for the other connection options
    sql::Properties properties({
          {"user", "db_user"},
          {"password", "db_user_password"},
       });

    // Establish Connection
    // Use a smart pointer for extra safety
    std::unique_ptr<sql::Connection> conn(DriverManager::getConnection(url, properties));
 } catch (...) {
    cerr << "Invalid database connection" << endl;
    exit (EXIT_FAILURE);
}
```

## Code Example: Connect

The following code demonstrates how to connect using the [example database and user account](setup-for-connector-cpp-examples.md):

```c++
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Main Process
int main(int argc, char **argv)
{
   try {
      // Instantiate Driver
      sql::Driver* driver = sql::mariadb::get_driver_instance();

      // Configure Connection
      // The URL or TCP connection string format is
      // ``jdbc:mariadb://host:port/database``.
      sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

      // Use a properties map for the other connection options
      sql::Properties properties({
            {"user", "db_user"},
            {"password", "db_user_password"},
         });

      // Establish Connection
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

      // Use Connection
      // ...

      // Close Connection
      conn->close();
   }

   // Catch Exceptions
   catch (sql::SQLException& e) {
      std::cerr << "Error Connecting to the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

## Code Example: TLS

The following `code` demonstrates how to connect with TLS (Transport Layer Security, the successor to SSL) for the [example database and user account](setup-for-connector-cpp-examples.md):

```c++
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Main Process
int main(int argc, char **argv)
{
   try {
      // Instantiate Driver
      sql::Driver* driver = sql::mariadb::get_driver_instance();

      // Configure Connection
      // The URL or TCP connection string format is
      // ``jdbc:mariadb://host:port/database``.
      sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

      // Use a properties map for the user name and password
      //The ``useTls`` option enables TLS
      //The ``tlsCA`` option specifies path to a PEM file that contains a X509 certificate for trusted Certificate Authorities (CAs).
      sql::Properties properties({
            {"user", "db_user"},
            {"password", "db_user_password"},
            {"useTls", "true"},
            {"tlsCA", "tls-ca-root.pem"}
         });

      // Establish Connection
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

      // Use Connection
      // ...

      // Close Connection
      conn->close();
   }

   // Catch Exceptions
   catch (sql::SQLException& e) {
      std::cerr << "Error Connecting to the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
