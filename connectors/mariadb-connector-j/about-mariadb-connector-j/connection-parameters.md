---
description: >-
  Reference for MariaDB Connector/J connection string options: essential,
  TLS, pool, and infrequently used parameters, plus removed options.
---

# MariaDB Connector/J Connection Parameters

Connection parameters are appended to the [connection string](README.md#connection-strings) as `?option1=value1&option2=value2`. Unknown options are accepted and silently ignored.

General remark: Unknown options are accepted and silently ignored.

The following options are supported.

## Essential Parameters

### **allowLocalInfile**

* Description: Permit loading data from file. see [LOAD DATA LOCAL INFILE](jdbc-api-implementation-notes.md#load-data-infile). Having this option enable can impact batch performance. Disabling it can permit some batch improvement
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.2.1

### **connectTimeout**

* Description: The connect timeout value, in milliseconds, or zero for no timeout. Since 4.0.0, when the host name resolves to several addresses (IPv4 and IPv6), each address is tried in turn until one connects, and the timeout bounds the attempts as a whole: each attempt gets the remaining time divided by the number of addresses left.
* Data Type: `integer`
* Default Value: `30 000`
* Introduced: 1.1.8

### **initSql**

* Description: permit to execute commands at connection creation. Multiple commands can be passed. example: initSql=SET @myVar='YourVar';SET @myVar2='YourVar2'.
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.0.0

### **password**

* Description: password
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.0.0

### **user**

* Description: Username.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.0.0

### **useServerPrepStmts**

{% hint style="warning" %}
**For Upgraders**

In version 3.x, enabling this option (or relying on defaults) often results in a significantly higher `prepared_stmt_count` on the server compared to version 2.7. This is due to more aggressive caching. Monitor your server status variables after upgrading.
{% endhint %}

*   Description: The **Text protocol** (default) is a universally safe option that works reliably in all situations. The **Binary protocol** (`useServerPrepStmts=true`) can offer performance benefits, but its impact depends on whether the prepared statement cache is used:

    * **Cache miss:** Preparing before execution adds overhead, potentially causing up to \~50% performance loss.
    * **Cache hit:** Can improve performance by around 5–10%, though the gain is often small since most queries have simple execution plans.

    The actual benefit depends entirely on your query patterns.

    Starting with **MariaDB 10.6** ([MDEV-19237](https://jira.mariadb.org/browse/MDEV-19237)), the server can skip resending metadata for result-set–returning SQL commands when `useServerPrepStmts` is enabled and the metadata hasn’t changed. This eliminates unnecessary network traffic and metadata parsing, which can yield **significant improvements (around 10–30%)**—especially when metadata is large compared to the result set itself.

    **Recommendation:**\
    If you are using [MariaDB 10.6](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/10.6) or later and your application runs mostly repeated queries (not constantly changing), enabling the Binary protocol with `useServerPrepStmts` is generally recommended.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.3.0

## TLS Parameters

more information on [Using TLS/SSL with MariaDB java connector](../using-tls-ssl-with-mariadb-java-connector.md)

### **sslMode**

* Description: Enables SSL/TLS in a specific mode. This option replaces the deprecated options `disableSslHostnameVerification`, `trustServerCertificate`, and `useSsl`. Since 4.0.0, TLS is enabled by default: the default value is `verify-full`, and `sslMode=disable` must be set to connect without TLS (the legacy `useSsl=false` also disables it). In 3.x, the default value is `disable`.
* Data Type: `string`
* Default Value: `verify-full` since 4.0.0, `disable` in 3.x
* Valid Values:
  * disable: Do not use SSL/TLS (alias 'false', '0')
  * trust: Only use SSL/TLS for encryption. Do not perform certificate or hostname verification. (alias 'required')
  * verify-ca: Use SSL/TLS for encryption and perform certificates verification, but do not perform hostname verification. (alias 'verify\_ca')
  * verify-full: Use SSL/TLS for encryption, certificate verification, and hostname verification (alias 'verify\_identity', 'true', '1')
  * allow: `verify-full` when the server announces TLS, no encryption otherwise. This is a migration mode for a mix of servers with and without TLS behind one connection string: the choice is made from the capability flags the server sends. Replace it with `verify-full` once every server has TLS. Available since 3.5.11 and 4.0.0.
* Introduced: 3.0.0

### **serverSslCert**

* Description: |Permits providing the server's certificate in DER form, or the server's CA certificate. The server will be added to trustStore. This permits a self-signed certificate to be trusted.Can be used in one of 3 forms : \* `serverSslCert=/path/to/cert.pem` (full path to certificate)\* `serverSslCert=classpath:relative/cert.pem` (relative to current classpath)\* or as verbatim DER-encoded certificate string "------BEGIN CERTIFICATE-----"
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.0

### **keyStore**

* Description: File path of the keyStore file that contains the client private keycontains store and associate certificates (similar to java System property "javax.net.ssl.keyStore", but ensure that only the private key's entries are used).
* Data Type: `string`
* Default Value: `null`
* Alias: clientCertificateKeyStoreUrl
* Introduced: 1.1.1

### **keyStorePassword**

* Description: Password for the client certificate keyStore (similar to java System property "javax.net.ssl.keyStorePassword")
* Data Type: `string`
* Default Value: `null`
* Alias: clientCertificateKeyStorePassword
* Introduced: 1.3.4

### **enabledSslCipherSuites**

* Description: Force TLS/SSL cipher (comma separated list). Example : "`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_DHE_DSS_WITH_AES_256_GCM_SHA384`"
* Data Type: `string`
* Default Value: `use JRE ciphers`
* Introduced: 1.5.0

### **enabledSslProtocolSuites**

* Description: Force TLS/SSL protocol to a specific set of TLS versions (comma separated list). Example : "`TLSv1.3`,`TLSv1.2`"
* Data Type: `string`
* Default Value: `TLSv1.3,TLSv1.2` since 4.0.0, whatever the JSSE defaults of the running JVM. `use JRE default` in 3.x
* Alias: enabledSSLProtocolSuites
* Introduced: 1.5.0

### **fallbackToSystemKeyStore**

* Description: keystoreXXX options are used to permit mutual authentication. When keystore option is not specified, this setting determines the connector's behavior: if set to false, not using any keystore; if set to true, the connector will follow standard Java convention and use the trust store defined by the "javax.net.ssl.trustStore" system property.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.3.2

### **fallbackToSystemTrustStore**

* Description: Server certificates can be validated using either the serverSslCert or trustStore options. When neither option is specified, this setting determines the connector's behavior: if set to false, all certificates will be rejected; if set to true, the connector will follow standard Java convention and use the trust store defined by the "javax.net.ssl.trustStore" system property.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.3.2

### **deferCertificateValidation**

* Description: When the server certificate cannot be validated against the trust store (self-signed certificate, or unknown issuer), permit deferring the server identity validation to authentication, where the certificate fingerprint is verified together with the password. This is the zero-configuration TLS of MariaDB Server 11.4 and later, which requires a MitM-proof authentication plugin and a non-empty password. When disabled, such a certificate is rejected at the TLS handshake.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 4.0.0

### **disableSslHostnameVerification**

* Description: _deprecated, use `sslMode` instead_ When using ssl, the driver checks the hostname against the server's identity as presented in the server's certificate (checking alternative names or the certificate CN) to prevent man-in-the-middle attacks. This option permits deactivating this validation. Hostname verification is disabled when the trustServerCertificate option is set
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.1.0
* Deprecated: 3.0.0

### **useSsl**

* Description: _deprecated, use sslMode instead_ Force [SSL/TLS on connection](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview)(useSSL can be used as alias). Since 4.0.0, TLS is enabled by default and `useSsl=false` still disables it.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.0
* Deprecated: 3.0.0

### **trustServerCertificate**

* Description: _deprecated, use sslMode instead_ When using SSL/TLS, do not check server's certificate
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.1
* Deprecated: 3.0.0

## Pool Parameters

See the [pool documentation](../pool-datasource-implementation.md) for pool configuration.

### **pool**

* Description: Use pool. This option is useful only if not using a DataSource object, but only a connection object
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.2.0

### **poolName**

* Description: Pool name that permits identifying threads.default: auto-generated as MariaDb-pool-
* Data Type: `string`
* Default Value: `MariaDB-pool`
* Introduced: 2.2.0

### **maxPoolSize**

* Description: The maximum number of physical connections that the pool should contain
* Data Type: `integer`
* Default Value: `8`
* Introduced: 2.2.0

### **minPoolSize**

* Description: When connections are removed due to not being used for longer than "maxIdleTime", connections are closed and removed from the pool. "minPoolSize" indicates the number of physical connections the pool should keep available at all times. Should be less or equal to maxPoolSize.
* Data Type: `integer`
* Default Value: `maxPoolSize value`
* Introduced: 2.2.0

### **poolValidMinDelay**

* Description: When asking a connection to pool, the pool will validate the connection state. "poolValidMinDelay" permits disabling this validation if the connection has been borrowed recently avoiding useless verifications in case of frequent reuse of connections. 0 means validation is done each time the connection is asked. In milleseconds.
* Data Type: `integer`
* Default Value: `1000`
* Introduced: 2.2.0

### **maxIdleTime**

* Description: The maximum amount of time in seconds that a connection can stay in the pool when not used. This value must always be below @wait\_timeout value - 45s
* Data Type: `integer`
* Default Value: `600` minimum value is 60 seconds
* Introduced: 2.2.0

### **useResetConnection**

* Description: When a connection is closed() (given back to pool), the pool resets the connection state. Setting this option, the prepare command will be deleted, session variables changed will be reset, and user variables will be destroyed when the server permits it (>= MySQL 5.7.3), permitting saving memory on the server if the application make extensive use of variables
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.2.0

### **registerJmxPool**

* Description: Register JMX monitoring pools
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 2.2.0

## Infrequently Used Parameters

### **allowMultiQueries**

* Description: permit multi-queries like `insert into ab (i) values (1); insert into ab (i) values (2)`.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.0.0

### **allowPublicKeyRetrieval**

* Description: Authorize client to retrieve RSA server public key when serverRsaPublicKeyFile is not set (for sha256\_password and caching\_sha2\_password authentication password)
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.5.0

### **autocommit**

* Description: Set default autocommit value on connection initialization.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 2.2.0

### **blankTableNameMeta**

* Description: Resultset metadata getTableName always return blank. This option is mainly for ORACLE db compatibility.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.4.3

### **cacheCodecs**

* Description: permit to enable/disable caching of the codec (FIELD encoder/decoder) list loaded through `ServiceLoader`, so it is loaded once per JVM instead of on each connection. Disable only when codecs are registered dynamically after the first connection.
* Data Type: `boolean`
* Default Value: `true` since 4.0.0, `false` in 3.x
* Introduced: 3.5.4

### **cachePrepStmts**

* Description: Enable caching of PREPARE commands using an LRU (Least Recently Used) cache to prevent redundant command preparation. Note that in versions prior to 3.x, this cache was only activated when the useServerPrepStmts option was enabled.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.3.0

### **connectionAttributes**

* Description: When performance\_schema is active, permit sending the server some client information in a key;value pair format (example: connectionAttributes=key1:value1,key2,value2).The information can be retrieved on the server in the tables performance\_schema.session\_connect\_attrs and performance\_schema.session\_account\_connect\_attrs. This can enable the server to identify the client/application
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.4.0

### **connectionCollation**

* Description: Connector force `utf8mb4` charset at connection. Indicate what utf8mb4 collation to use if set. if not set, the server default collation for `utf8mb4` will be used. Useful only for the server before [MariaDB 11.4](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.4), because then a better solution would be to set `character_set_collations`
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0

### **createDatabaseIfNotExist**

* Description: the specified database in the url will be created if nonexistent.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.7

### **credentialType**

* Description: Indicate the credential plugin type to use. Plugin must be present in classpath. See [Credential service](services.md#credential-service) for the available plugins. Since 4.0.0, the `AWS-IAM` plugin ships in the separate `org.mariadb.jdbc:mariadb-java-client-aws` artifact.
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

### **defaultFetchSize**

* Description: The driver will call setFetchSize(n) with this value on all newly-created Statements. Since 4.0.0, the value `Integer.MIN_VALUE` (`-2147483648`) means sequential access: a forward-only result set reads each row from the socket one column at a time, `Blob`, `Clob`, `InputStream`, and `Reader` columns are streamed without being loaded in memory, and columns must be read in increasing index order.
* Data Type: `integer`
* Default Value: `0`
* Introduced: 2.4.2

### **disconnectOnExpiredPasswords**

* Description: On the connection creation, indicate behavior when password is expired. When true (default) throw an expired password error. When false, the connection succeed in "sandbox" mode, only queries related to password change are allowed.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 3.5.2

### **dumpQueriesOnException**

* Description: If set to 'true', an exception is thrown during query execution containing a query string. This is useful in development, but can lead to security issue if logs are available.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.0

### **galeraAllowedState**

* Description: Usually, Connection.isValid just send an empty packet to server, and server send a small response to ensure connectivity. When this option is set, connector will ensure Galera server state "wsrep\_local\_state" correspond to allowed values (separated by comma). example "4,5", recommended is "4". see [galera state to know more](https://galeracluster.com/library/documentation/node-states.html#node-state-changes)
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.2.5

### **includeInnodbStatusInDeadlockExceptions**

* Description: add "SHOW ENGINE INNODB STATUS" result to exception trace when having a deadlock exception.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.3.0

### **includeThreadDumpInDeadlockExceptions**

* Description: add thread dump to exception trace when having a deadlock exception.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.3.0

### **localSocket**

* Description: Permits connecting to the database via Unix domain socket, if the server allows it. The value is the path of Unix domain socket (i.e "socket" database parameter : select @@socket). Since 4.0.0, the JDK implementation is used, so no JNA dependency is needed, and Unix domain sockets are also supported on Windows (for example, for an SSH tunnel).
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.4

### **localSocketAddress**

* Description: Hostname or IP address to bind the connection socket to a local (UNIX domain) socket.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.7

### **maxAllowedColumns**

* Description: Maximum number of columns the driver accepts in result-set or prepare metadata sent by the server. Reading column metadata allocates memory in proportion to the announced column count, so a malicious proxy that announces a huge count could exhaust client memory. When the server announces more columns than this limit, the command is interrupted with an error.
* Data Type: `integer`
* Default Value: `65535`
* Introduced: 2.7.15, 3.3.6, 3.4.4, 3.5.10

### **maxAllowedPacket**

* Description: Maximum size, in bytes, of a packet the driver sends or receives. The value is advertised to the server during the handshake (capped to 16MB for the connection phase), lets the driver reject a command that is too big to send — throwing an error instead of having the server drop the connection — and rejects an oversized packet received from the server. When unset, no send-side limit applies, and the receive side falls back to a server-independent heap-relative ceiling: a quarter of the JVM maximum heap, clamped between 16MB and 1GB.
* Data Type: `integer`
* Default Value: `null`
* Introduced: 3.5.10

### **maxQuerySizeToLog**

* Description: Only the first characters corresponding to this options size will be displayed in logs
* Data Type: `integer`
* Default Value: `1024`
* Introduced: 1.5.0

### **metaExportedKeys**

* Description: Possible implementation `DatabaseMetadata.getExportedKey`. Either use `INFORMATION_SCHEMA` or `SHOW CREATE TABLE` to retrieve metadata information. When set to "auto", the method will automatically choose between the `INFORMATION_SCHEMA` approach or the `SHOW CREATE` implementation based on whether the database server is running locally or remotely. Possible values: "UseInformationSchema", "UseShowCreate", or "auto".
* Data Type: `string`
* Default Value: `auto`
* Introduced: 3.5.4

### **oldModeNoPrecisionTimestamp**

* Description: When enabled, Timestamps string representation will be compatible with 2.7's behavior (fractional part will only be displayed if required, not according to timestamp precision) .
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.5.3

### **permitMysqlScheme**

* Description: when added to connection string, permit `jdbc:mysql:` prefix in connection string
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.0.0

### **permitNoResults**

* Description: Indicate if Statement/PreparedStatement.executeQuery for a command that produces no result set returns an empty result set instead of throwing an exception. When enabled, such a command returns an empty result set. When disabled, it throws an `SQLException`, as the JDBC specification requires. Disabled by default since 4.0.0: enable it to restore the former behavior.
* Data Type: `boolean`
* Default Value: `false` since 4.0.0, `true` in 3.x
* Introduced: 3.5.2

### **pinGlobalTxToPhysicalConnection**

* Description: When set, commands with a specific XID will reuse the previous connection used for this XID.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.4.1

### **pipe**

* Description: On Windows, specify named pipe name to connect (windows equivalent of unix socket)
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.3

### **prepStmtCacheSize**

* Description: When cachePrepStmts is enabled, this value indicates the prepared statement cache size.
* Data Type: `integer`
* Default Value: `250`
* Introduced: 1.3.0

### **restrictedAuth**

* Description: permits to restrict authentication plugins (comma separated). For example, the following connection string only allows the mysql\_native\_password and client\_ed25519 client authentication plugins:`jdbc:mariadb:HOST/DATABASE?restrictedAuth=mysql_native_password,client_ed25519`. If not set, permit all authentication plugins.
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.0.0

### **returnMultiValuesGeneratedIds**

* Description: for connector 2.x compatibility only, getGeneratedKeys() will then returns all ids of multi-value inserts. This is not compatible with galera servers
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.3.2

### **rewriteBatchedStatements**

* Description: For insert queries, rewrite batchedStatement to execute in a single executeQuery.
  * example: 'insert into ab (i) values (?)' with first batch values = 1, second = 2 will be rewritten as 'insert into ab (i) values (1), (2)'.
  * **Upgrade Note:** This option is ignored in Connector/J versions 3.0.0 through 3.5.5.
  * When enabled, the `useServerPrepStmts` option will be forced to false.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: since `1.1.8`, on `3` version since `3.5.6`

### **serverRsaPublicKeyFile**

* Description: Indicate path to RSA server public key file for sha256\_password and caching\_sha2\_password authentication password
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

### **servicePrincipalName**

* Description: When using [GSSAPI authentication](../gssapi-authentication-with-mariadb-connector-j.md), use this value as the Service Principal Name (SPN) instead of the one defined for the user account on the database server.
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.4.0

### **sessionVariables**

* Description: = pairs separated by comma, mysql session variables, set upon establishing successful connection.
* Data Type: `string`
* Default Value: `null`
* Introduced: 1.1.4

### **socketFactory**

* Description: to use a custom socket factory, set it to the full name of the class that implements javax.net.SocketFactory
* Introduced: 1.1.0

### **socketTimeout**

* Description: Defined the network socket timeout (SO\_TIMEOUT) in milliseconds. Value of 0 disables this timeout. If the goal is to set a timeout for all queries, the server has permitted a solution to limit the query time by setting a system variable, [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_statement_time). The advantage is that the connection then is still usable.
* Data Type: `integer`
* Default Value: `0`
* Introduced: 1.1.7

### **tcpAbortiveClose**

* Description: This option can be used in environments where connections are created and closed in rapid succession. Often, it is not possible to create a socket in such an environment after a while, since all local "ephemeral" ports are used up by TCP connections in TCP\_WAIT state. Using tcpAbortiveClose works around this problem by resetting TCP connections (abortive or hard close) rather than doing an orderly close. It is accomplished by using socket.setSoLinger(true,0) for abortive close.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.1.1

### **tcpKeepAlive**

* Description: Sets corresponding option on the connection socket. Default to true since 3.0.0 (was false before)
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0

### **tcpKeepCount**

* Description: Permit to set socket option TCP\_KEEPCOUNT (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

### **tcpKeepIdle**

* Description: Permit to set socket option TCP\_KEEPIDLE (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

### **tcpKeepInterval**

* Description: Permit to set socket option TCP\_KEEPINTERVAL (only if java 11+)
* Data Type: `integer`
* Default Value: `0`
* Introduced: 3.0.0

### **tinyInt1isBit**

* Description: Datatype mapping flag, handle MySQL Tiny as BIT(boolean).
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0

### **tlsSocketType**

* Description: Indicate the TLS org.mariadb.jdbc.tls.TlsSocketPlugin plugin type to use. Plugin must be present in classpath
* Data Type: `string`
* Default Value: `null`
* Introduced: 2.5.0

### **transactionReplay**

* Description: Enables transaction caching. If a failover occurs before a transaction is committed or rolled back, the transaction's cached statements are re-executed on the new primary server. Connector/J requires that applications only use idempotent queries. If the number of statements in the transaction cache exceeds transactionReplaySize, caching will be disabled until the transaction is committed or rolled back.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.0.0

### **transactionReplaySize**

* Description: Sets the number of statements that should be saved in the transaction cache when transactionReplay is enabled.
* Data Type: `integer`
* Default Value: `64`
* Introduced: 3.0.0

### **trustStore**

* Description: File path of the trustStore file (similar to java System property "javax.net.ssl.trustStore"). (legacy alias trustCertificateKeyStoreUrl)Use the specified file for trusted root certificates.When set, overrides serverSslCert. (see trustStorePassword in case if a jks truststore with a password)
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 1.3.4 in 1.x, 2.0.0 in 2.x)

### **trustStorePassword**

* Description: Password for the trusted root certificate file (similar to java System property "javax.net.ssl.trustStorePassword").(legacy alias trustCertificateKeyStorePassword).
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 1.3.4 in 1.x, 2.0.0 in 2.x)

### **trustStoreType**

* Description: Indicate trust store type (JKS/PKCS12). default is null, then using java default type.(legacy alias trustCertificateKeystoreType).
* Data Type: `string`
* Default Value: `null`
* Introduced: 3.5.0 (or 2.4.0 in 2.x)

### **useBulkStmts**

* Description: Use dedicated COM\_STMT\_BULK\_EXECUTE protocol for batch insert when possible. (batch without Statement.RETURN\_GENERATED\_KEYS and streams) to have faster batch.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.0.0 (was false since version >= 2.3.0)

### **useCatalogTerm**

* Description: "schema" and "database" are server synonymous. Connector historically get/set database using Connection.setCatalog()/getCatalog(), setSchema()/getSchema() being no-op. Setting option useCatalogTerm to "schema" will change that behavior to use Schema in place of Catalog. Affected changes : database change will be done with either Connection.setCatalog()/getCatalog() or Connection.setSchema()/getSchema(), 2: DatabaseMetadata methods that use catalog or schema filtering, 3: ResultsetMetadata getCatalogName/getSchemaName
* Data Type: `string`
* Default Value: `CATALOG`
* Introduced: 3.2.0

### **useCompression**

* Description: Compresses the exchange with the database through gzip. This permits better performance when the database is not in the same location.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 1.0.0

### **useIpForKillQuery**

* Description: When cancelling a running query (for example with `Statement.cancel()` or a query timeout), the driver opens a new connection to send the `KILL QUERY` command. When enabled, that connection is established using the **socket IP** of the current connection instead of the configured host name. This is useful when the host name resolves to several servers (DNS round-robin, load balancer): the kill must reach the exact server running the query, which the IP guarantees. Leave it disabled when TLS is configured with host name / DNS certificate validation, since in that case the host name is required to validate the certificate.
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 3.5.9

### **useMysqlMetadata**

* Description: [databaseMetaData.getDatabaseProductName()](https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/java/sql/DatabaseMetaData.html#getDatabaseProductName\(\)) return "MariaDB" or "MySQL" according to server type
* Data Type: `boolean`
* Default Value: `false`
* Introduced: 2.4.0

### **yearIsDateType**

* Description: returns Year as date type, rather than numerical.
* Data Type: `boolean`
* Default Value: `true`
* Introduced: 1.0.0

## **Removed options**

<table><thead><tr><th width="275">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>allowMasterDownConnection</code></td><td>When the replication Failover and Load Balancing Mode is in use, allow the creation of connections when the master is down. If no masters are available, then the default connection will be a replica, and Connection.isReadOnly() will return true. Default: false. Since 2.2.0, removed in 3.0.0</td></tr><tr><td><code>interactiveClient</code></td><td>Session timeout is defined by the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout">wait_timeout</a> server variable. Setting interactiveClient to true will tell the server to use the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables">interactive_timeout</a> server variable.Default: false. Since 1.1.7</td></tr><tr><td><code>assureReadOnly</code></td><td>When this parameter is enabled, when a failover and load balancing mode is in use and a read-only connection is made to a host, ensure that this connection is in read-only mode by setting the session to read-only. Default to false. Since 1.3.0, removed in 3.0.0</td></tr><tr><td><code>autoReconnect</code></td><td>If this parameter is enabled and Failover and Load Balancing Mode is not in use, the connector will simply try to reconnect to its host after a failure. This is referred to as Basic Failover. If this parameter is enabled and Failover and Load Balancing Mode is in use, the connector will blacklist the failed host and try to connect to a different host of the same type. This is referred to as Standard Failover. Default is false.since 1.1.7, removed in 3.0.0</td></tr><tr><td><code>callableStmtCacheSize</code></td><td>This sets the number of callable statements that the driver will cache per VM if "cacheCallableStmts" is enabled.Default: true. Since 1.4.0, removed in 3.0.0</td></tr><tr><td><code>enablePacketDebug</code></td><td>Driver will save the last 16 MySQL packet exchanges (limited to first 1000 bytes). Hexadecimal value of those packets will be added to stacktrace when an IOException occur.This option has no impact on performance but driver will then take 16kb more memory.Default: false. Since 1.6.0, 2.0.1, removed in 3.0.0</td></tr><tr><td><code>failoverLoopRetries</code></td><td>When the connector is searching silently for a valid host, this parameter defines the maximum number of connection attempts the connector will make before throwing an exception.This parameter differs from the "retriesAllDown" parameter because this silent search is used in situations where the connector can temporarily workaround the problem, such as by using the master connection to execute reads when the replica connection fails.Default: 120.since 1.2.0, removed in 3.0.0</td></tr><tr><td><code>loadBalanceBlacklistTimeout</code></td><td>When a connection fails, this host will be blacklisted for the amount of time defined by this parameter.When connecting to a host, the driver will try to connect to a host in the list of non-blacklisted hosts and, only if none are found, attempt blacklisted ones.This blacklist is shared inside the classloader.Default: 50 seconds.since 1.2.0, removed in 3.0.0</td></tr><tr><td><code>log</code></td><td>Enable log information. require Slf4j version > 1.4 dependency.Log level correspond to Slf4j logging implementationDefault: false. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>passwordCharacterEncoding</code></td><td>Indicate password encoding charset. Charset value must be a <a href="https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html">Java charset</a>. Example : "UTF-8" Default: null (= platform's default charset) . Since 1.5.9, removed in 3.0.0</td></tr><tr><td><code>profileSql</code></td><td>log query execution time.Default: false. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>slowQueryThresholdNanos</code></td><td>Will log query with execution time superior to this value (if defined )Default: 1024. Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>serverTimezone</code></td><td>Defines the server time zone.to use only if the jre server has a different time implementation of the server.(best to have the same server time zone when possible).since 1.1.7, removed in 3.0.0</td></tr><tr><td><code>sharedMemory</code></td><td>Permits connecting to the database via shared memory, if the server allows it. The value is the base name of the shared memory.since 1.1.4, removed in 3.0.0</td></tr><tr><td><code>staticGlobal</code></td><td>Indicates the values of the global variables <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet">max_allowed_packet</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#wait_timeout">wait_timeout</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit">autocommit</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables">auto_increment_increment</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#time_zone">time_zone</a>, <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#system_time_zone">system_time_zone</a> and <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tx_isolation">tx_isolation</a>) won't be changed, permitting the pool to create new connections faster.Default: false. Since 2.2.0, removed in 3.0.0</td></tr><tr><td><code>tcpNoDelay</code></td><td>Sets corresponding option on the connection socket.since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>tcpRcvBuf</code></td><td>set buffer size for TCP buffer (SO_RCVBUF).since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>tcpSndBuf</code></td><td>set buffer size for TCP buffer (SO_SNDBUF).since 1.0.0, removed in 3.0.0</td></tr><tr><td><code>trackSchema</code></td><td>Permit to disabled "session_track_schema" setting when server has CLIENT_SESSION_TRACK capabilityDefault: True. Since 2.5.4, removed in 3.0.0</td></tr><tr><td><code>useBatchMultiSend</code></td><td><em>Not compatible with aurora</em> Driver will can send queries by batch. If set to false, queries are sent one by one, waiting for the result before sending the next one. If set to true, queries will be sent by batch corresponding to the useBatchMultiSendNumber option value (default 100) or according to the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_allowed_packet">max_allowed_packet</a> server variable if the packet size does not permit sending as many queries. Results will be read later, avoiding a lot of network latency when the client and server aren't on the same host. This option is mainly effective when the client is distant from the server. More information <a href="../option-batchmultisend-description.md">here</a> Default: true (false if using aurora failover) . Since 1.5.0, removed in 3.0.0</td></tr><tr><td><code>useBatchMultiSendNumber</code></td><td>When option useBatchMultiSend is active, indicate the maximum query send in a row before reading results.Default: 100. Since 1.5.0</td></tr><tr><td><code>useFractionalSeconds</code></td><td>Correctly handle subsecond precision in timestamps. May confuse 3rd party components (Hibernated).Default: true. Since 1.0.0</td></tr><tr><td><code>useReadAheadInput</code></td><td>Use a buffered input stream that reads the socket's available data. Default: false. Since 2.4.0, removed in 4.0.0</td></tr><tr><td><code>useOldAliasMetadataBehavior</code></td><td>Metadata ResultSetMetaData.getTableName() returns the physical table name. "useOldAliasMetadataBehavior" permits activating the legacy code that sends the table alias if set. Default: false. Since 1.1.9</td></tr><tr><td><code>validConnectionTimeout</code></td><td>When multiple hosts are configured, the connector verifies that the connections haven't been lost after this much time in seconds has elapsed.When this parameter is set to 0, no verification will be done. Default:120 secondssince 1.2.0, removed in 3.0.0</td></tr></tbody></table>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
