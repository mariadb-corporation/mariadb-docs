# mysql\_optionsv

## Syntax

```c
int mysql_optionsv(MYSQL * mysql,
                   enum mysql_option,
                   const void * arg,
                   ...);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `mysql_option` - the option you want to set. See description below.
* `arg` - the value for the option.
* `...` - variable argument list

## Description

Used to set extra connect options and affect behavior for a connection. This function may be called multiple times to set several options. `mysql_optionsv()` should be called after [mysql\_init()](mysql_init.md).

Some of these options can also be set in [option files](../configuring-mariadb-connectorc-with-option-files.md), such as `my.cnf`.

### Returns

Returns zero on success, non zero if an error occurred (invalid option or value).

### Options

*   `MYSQL_INIT_COMMAND`: Command(s) which will be executed when connecting and reconnecting to the server.

    ```c
    mysql_optionsv(mysql, MYSQL_INIT_COMMAND, (void *)"CREATE TABLE ...");
    ```
*   `MYSQL_OPT_CONNECT_TIMEOUT`: Connect timeout in seconds. This value will be passed as an unsigned `int` parameter.

    ```c
    unsigned int timeout= 5;
    mysql_optionsv(mysql, MYSQL_OPT_CONNECT_TIMEOUT, (void *)&timeout);
    ```
*   `MARIADB_OPT_VERIFY_LOCAL_INFILE_CALLBACK`: Specifies a callback function for filename and/or directory verification.\
    This option was added in Connector/C 2.3.0

    ```c
    int my_verify_filename(void *data, const char *filename)
    {
     return strcmp((char *)data, filename);
    }
    ...
    char *filename= "mydata.csv";
    mysql_optionsv(mysql, MARIADB_OPT_VERIFY_LOCAL_INFILE_CALLBACK, my_verify_filename, (void *)filename);
    ```
*   `MYSQL_PROGRESS_CALLBACK`: Specifies a callback function which will be able to visualize the progress of certain long running statements (i.e. [LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) or [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table)).

    ```c
    static void report_progress(const MYSQL *mysql __attribute__((unused)),
     uint stage, uint max_stage,
     double progress __attribute__((unused)),
     const char *proc_info __attribute__((unused)),
     uint proc_info_length __attribute__((unused)))
    {
     ...
    }
    mysql_optionsv(mysql, MYSQL_PROGRESS_CALLBACK, (void *)report_progress);
    ```
*   `MYSQL_OPT_RECONNECT`: Enable or disable automatic reconnect.

    ```c
    my_bool reconnect= 1; /* enable reconnect */
    mysql_optionsv(mysql, MYSQL_OPT_RECONNECT, (void *)&reconnect);
    ```
*   `MYSQL_OPT_READ_TIMEOUT`: Specifies the timeout in seconds for reading packets from the server.

    ```c
    unsigned int timeout= 5;
    mysql_optionsv(mysql, MYSQL_OPT_READ_TIMEOUT, (void *)&timeout);
    ```
*   `MYSQL_OPT_WRITE_TIMEOUT`:\
    Specifies the timeout in seconds for sending packets to the server.

    ```c
    unsigned int timeout= 5;
    mysql_optionsv(mysql, MYSQL_OPT_WRITE_TIMEOUT, (void *)&timeout);
    ```
*   `MYSQL_REPORT_DATA_TRUNCATION`: Enable or disable reporting data truncation errors for prepared statements.

    ```c
    mysql_optionsv(mysql, MYSQL_REPORT_DATA_TRUNCATION, NULL); /* disable */
    mysql_optionsv(mysql, MYSQL_REPORT_DATA_TRUNCATION, (void *)"1"); /* enable */
    ```
*   `MYSQL_SET_CHARSET_DIR`: [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) files.

    ```c
    mysql_optionsv(mysql, MYSQL_SET_CHARSET_DIR, (void *)"/usr/local/mysql/share/mysql/charsets");
    ```
*   `MYSQL_SET_CHARSET_NAME`: Specify the default [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) for the connection.

    ```c
    mysql_optionsv(mysql, MYSQL_SET_CHARSET_NAME, (void *)"utf8");
    ```
*   `MYSQL_OPT_BIND`: Specify the network interface from which to connect to MariaDB Server.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_BIND, (void *)"192.168.8.3");
    ```
*   `MYSQL_OPT_NONBLOCK`: Specify stack size for non blocking operations.\
    The argument for MYSQL\_OPT\_NONBLOCK is the size of the stack used to save the state of a non-blocking operation while it is waiting for I/O and the application is doing other processing. Normally, applications will not have to change this, and it can be passed as zero to use the default value.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_NONBLOCK, 0);
    ```
*   `MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS`: If this option is set, the client indicates that it will be able to handle expired passwords by setting the CLIENT\_CAN\_HANDLE\_EXPIRED\_PASSWORDS capability flag.\
    If the password has expired and CLIENT\_CAN\_HANDLE\_EXPIRED\_PASSWORDS is set, the server will not return an error when connecting, but put the connection in sandbox mode, where all commands will return error 1820 (ER\_MUST\_CHANGE\_PASSWORD) unless a new password was set. This option was added in MariaDB Connector/C 3.0.4

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS, 1);
    ```
*   `MYSQL_OPT_MAX_ALLOWED_PACKET`: The maximum packet length to send to or receive from server. The default is 16MB, the maximum 1GB.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_MAX_ALLOWED_PACKET, 0x40000000);
    ```
*   `MYSQL_OPT_NET_BUFFER_LENGTH`: The buffer size for TCP/IP and socket communication. Default is 16KB.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_NET_BUFFER_LENGTH, 0x40000000);
    ```

#### Connection Options

Some of these options can also be set as arguments to the [mysql_real_connect](mysql_real_connect.md) function.

*   `MARIADB_OPT_HOST`: Hostname or IP address of the server to connect to.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_HOST, (void *)"dbserver.example.com");
    ```
*   `MARIADB_OPT_USER`: User to login to the server.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_USER, (void *)"myuser");
    ```
*   `MARIADB_OPT_PASSWORD`: Password of the user to login to the server.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_PASSWORD, (void *)"horsebattery");
    ```
*   `MARIADB_OPT_SCHEMA`: Database to use.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SCHEMA, (void *)"mydb");
    ```
*   `MARIADB_OPT_PORT`: Port number to use for connection.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_PORT, 3307);
    ```
*   `MARIADB_OPT_UNIXSOCKET`: For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_UNIXSOCKET, (void *)"/var/lib/mysql/mysql.sock");
    ```
*   `MYSQL_OPT_NAMED_PIPE`: For Windows operating systems only: Use named pipes for client/server communication.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_NAMED_PIPE, NULL);
    ```
* `MYSQL_OPT_PROTOCOL`: Specify the type of client/server protocol. Possible values are:
  * MYSQL\_PROTOCOL\_TCP
  * MYSQL\_PROTOCOL\_SOCKET
  * MYSQL\_PROTOCOL\_PIPE
  *   MYSQL\_PROTOCOL\_MEMORY.

      ```c
      enum mysql_protocol_type prot_type= MYSQL_PROTOCOL_SOCKET;
      mysql_optionsv(mysql, MYSQL_OPT_PROTOCOL, (void *)&prot_type);
      ```
*   `MARIADB_OPT_FOUND_ROWS`: Return the number of matched rows instead of number of changed rows.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_FOUND_ROWS, 1);
    ```
*   `MYSQL_OPT_COMPRESS`: Use the compressed protocol for client server communication. If the server doesn't support compressed protocol, the default protocol will be used.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_COMPRESS, NULL);
    ```
*   `MYSQL_OPT_LOCAL_INFILE`: Enable or disable the use of [LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile)

    ```c
    unsigned int enable= 1, disable= 0;
    mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *)&disable);/* disable */
    mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *)NULL);     /* enable */
    mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *)&enable); /* enable */
    ```
*   `MARIADB_OPT_MULTI_STATEMENTS`: Allows the client to send multiple statements in one command. Statements will be divided by a semicolon.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_MULTI_STATEMENTS, (void *)"");
    ```
*   `MARIADB_OPT_MULTI_RESULTS`: Indicates that the client is able to handle multiple result sets from stored procedures or multi statements. This option will be automatically set if `MARIADB_OPT_MULTI_STATEMENTS` is set.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_MULTI_RESULTS, 1);
    ```
*   `MYSQL_SHARED_MEMORY_BASE_NAME`: Shared-memory name to use for Windows connections using shared memory to a local server (started with the --shared-memory option). Case-sensitive.

    ```c
    mysql_optionsv(mysql, MYSQL_SHARED_MEMORY_BASE_NAME, (void *)"mariadb");
    ```

#### TLS Options

*   `MYSQL_OPT_SSL_KEY`: Defines a path to a private key file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. If the key is protected with a passphrase, the passphrase needs to be specified with `MARIADB_OPT_TLS_PASSPHRASE` option.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_KEY, (void *)"certs/client-key.pem");
    ```
*   `MYSQL_OPT_SSL_CERT`: Defines a path to the X509 certificate file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CERT, (void *)"certs/client-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CA`: Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CA, (void *)"certs/ca-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CAPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information. This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CIPHER`: Defines a list of permitted ciphers or cipher suites to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption).

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CIPHER, (void *)"DHE-RSA-AES256-SHA");
    ```
*   `MYSQL_OPT_SSL_CRL`: Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information. This option is only supported if the connector was built with OpenSSL or Schannel. If the connector was built with GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");\\\\<<code>>mysql_optionsv(mysql, MYSQL_OPT_SSL_CRL, (void *)"certs/crl.pem");
    ```
*   `MYSQL_OPT_SSL_CRLPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information. This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");\\\\<<code>>mysql_optionsv(mysql, MYSQL_OPT_SSL_CRLPATH, (void *)"certs/crls");
    ```
*   `MARIADB_OPT_SSL_FP`: Specify the SHA1 fingerprint of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake. This is deprecated. Use `MARIADB_OPT_TLS_PEER_FP` instead.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_FP, (void *)"3a079e1a14ad326953a5d280f996b93d772a5bea");
    ```
*   `MARIADB_OPT_TLS_PEER_FP`: Specify the SHA1 fingerprint of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_PEER_FP, (void *)"3a079e1a14ad326953a5d280f996b93d772a5bea");
    ```
*   `MARIADB_OPT_SSL_FP_LIST`: Specify a file which contains one or more SHA1 fingerprints of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake. This is deprecated. Use `MARIADB_OPT_TLS_PEER_FP_LIST` instead.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_FP_LIST, (void *)"certs/fingerprints.txt");
    ```
*   `MARIADB_OPT_TLS_PEER_FP_LIST`: Specify a file which contains one or more SHA1 fingerprints of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_PEER_FP_LIST, (void *)"certs/fingerprints.txt");
    ```
*   `MARIADB_OPT_TLS_PASSPHRASE`: Specify a passphrase for a passphrase-protected private key, as configured by the `MYSQL_OPT_SSL_KEY` option. This option is only supported if the connector was built with OpenSSL or GnuTLS. If the connector was built with Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_PASSPHRASE, (void *)"thisisashortpassphrase");
    ```
*   `MARIADB_OPT_TLS_VERSION`: Defines which [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) protocol versions are allowed. This should be a comma-separated list of TLS protocol versions to allow. Valid TLS protocol versions are `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. Both the client and server should support the allowed TLS protocol versions. See [Secure Connections Overview: TLS Protocol Version Support](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#tls-protocol-version-support) for information on which TLS libraries support which TLS protocol versions. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which TLS libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_VERSION, (void *)"TLSv1.2,TLSv1.3");
    ```
*   `MYSQL_OPT_SSL_VERIFY_SERVER_CERT`: Enables (or disables) [server certificate verification](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#server-certificate-verification).

    ```c
    my_bool verify= 1;
    mysql_optionsv(mysql, MYSQL_OPT_SSL_VERIFY_SERVER_CERT, (void *)&verify);
    ```
*   `MYSQL_OPT_SSL_ENFORCE`: Whether to force [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview). This enables TLS with the default system settings. It does not prevent the connection from being created if the server does not support TLS.

    ```c
    my_bool enforce_tls= 1;
    mysql_optionsv(mysql, MYSQL_OPT_SSL_ENFORCE, (void *)&enforce_tls);
    ```
*   `MARIADB_OPT_TLS_CIPHER_STRENGTH`: Cipher strength. This value will be passed as an unsigned `int` parameter.

    ```c
    unsigned int cipher_strength= 128;
    mysql_optionsv(mysql, MARIADB_OPT_TLS_CIPHER_STRENGTH, (void*)&cipher_strength);
    ```

#### Plugin Options

*   `MYSQL_DEFAULT_AUTH`: Default authentication client-side plugin to use.

    ```c
    mysql_optionsv(mysql, MYSQL_DEFAULT_AUTH, (void *)"ed25519");
    ```
*   `MYSQL_ENABLE_CLEARTEXT_PLUGIN`: This option is supported to be compatible with MySQL client libraries. MySQL client libraries use this option to determine whether the [mysql_clear_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam#client-authentication-plugins) authentication plugin can be used. However, MariaDB clients and client libraries do not need to set any options in order to use this authentication plugin. Therefore, this option does not actually do anything in MariaDB Connector/C.

    ```c
    mysql_optionsv(mysql, MYSQL_ENABLE_CLEARTEXT_PLUGIN, 1);
    ```
*   `MARIADB_OPT_CONNECTION_HANDLER`: Specify the name of a connection handler plugin.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_CONNECTION_HANDLER, (void *)"aurora");
    ```
*   `MARIADB_OPT_USERDATA`: Bundle user data to the current connection, e.g. for use in connection handler plugins. This option requires 4 parameters: connection, option, key and value.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_USERDATA, (void *)"ssh_user", (void *)ssh_user);
    ```
*   `MARIADB_OPT_CONNECTION_READ_ONLY`: This option is used by connection handler plugins and indicates that the current connection will be used for read operations only.

    ```c
    my_bool read_only= 1;
    mysql_optionsv(mysql, MARIADB_OPT_CONNECTION_READ_ONLY, (void *)&read_only);
    ```
*   `MYSQL_PLUGIN_DIR`: Specify the location of client plugins. The plugin directory can also be specified with the `MARIADB_PLUGIN_DIR` environment variable.

    ```c
    mysql_optionsv(mysql, MYSQL_PLUGIN_DIR, (void *)"/opt/mariadb/lib/plugins");
    ```
*   `MYSQL_SECURE_AUTH`: Refuse to connect to the server if the server uses the [mysql_old_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password) authentication plugin. This mode is off by default, which is a difference in behavior compared to MySQL 5.6 and later, where it is on by default.

    ```c
    mysql_optionsv(mysql, MYSQL_SECURE_AUTH, 1);
    ```
*   `MYSQL_SERVER_PUBLIC_KEY`: Specifies the name of the file which contains the RSA public key of the database server. The format of this file must be in PEM format. This option is used by the [caching_sha2_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) client authentication plugin. It was introduced in Connector/C 3.1.0.

    ```c
    mysql_optionsv(mysql, MYSQL_SERVER_PUBLIC_KEY, (void *)(void *)"certs/server-cert.pem);
    ```

#### Option File Options

* `MYSQL_READ_DEFAULT_FILE`: Read options from an [option file](../configuring-mariadb-connectorc-with-option-files.md).
* `MYSQL_READ_DEFAULT_GROUP`: Read options from the named [option group](../configuring-mariadb-connectorc-with-option-files.md#option-groups) from an [option file](../configuring-mariadb-connectorc-with-option-files.md).

These options work together, according to the following rules:

* if both are set to `NULL`, then no option files are read.
* if `MYSQL_READ_DEFAULT_FILE` is set to an empty string (or `NULL` and `MYSQL_READ_DEFAULT_GROUP` is set) then all [default option files](../configuring-mariadb-connectorc-with-option-files.md#default-option-file-locations) are read.
* if `MYSQL_READ_DEFAULT_FILE` is set to a non-empty string, then it is interpreted as a path to a [custom option file](../configuring-mariadb-connectorc-with-option-files.md#custom-option-file-locations), and only that option file is read.
* if `MYSQL_READ_DEFAULT_GROUP` is an empty string (or `NULL` and `MYSQL_READ_DEFAULT_FILE` is set) then only default groups — `[client]`, `[client-server]`, `[client-mariadb]` are read.
* if `MYSQL_READ_DEFAULT_GROUP` is a non-empty string, then it is interpreted as a custom option group, and that custom option group is read in addition to default groups from above.

#### Connection Attribute Options

Connection attributes are stored in the [session\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-session_connect_attrs-table) and [session\_account\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-session_account_connect_attrs-table) Performance Schema tables.\
By default, MariaDB Connector/C sends the following connection attributes to the server:

* \_client\_name: always "libmariadb"
* \_client\_version: version of MariaDB Connector/C
* \_os: operation system
* \_pid: process id
* \_platform: e.g. x86 or x64
* \_server\_host: the hostname (as specified in mysql\_real\_connect). This attribute was added in Connector/C 3.0.5

{% hint style="info" %}
If the [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema) is disabled, connection attributes will not be stored on server.
{% endhint %}

*   `MYSQL_OPT_CONNECT_ATTR_DELETE`: Deletes a connection attribute for the given key.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_CONNECT_ATTR_DELETE, (void *)"app_version");
    ```
*   `MYSQL_OPT_CONNECT_ATTR_ADD`: Adds a key/value pair to connection attributes.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_CONNECT_ATTR_ADD, (void *)"app_version", (void *)"2.0.1");
    ```
*   `MYSQL_OPT_CONNECT_ATTR_RESET`: Clears the current list of connection attributes.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_CONNECT_ATTR_RESET, 0);
    ```

## See Also

* [mysql\_init()](mysql_init.md)
* [mysql\_options()](mysql_options.md)
* [mysql\_real\_connect()](mysql_real_connect.md)


{% @marketo/form formId="4316" %}
