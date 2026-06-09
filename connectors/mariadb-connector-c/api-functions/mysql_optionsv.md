---
description: >-
  mysql_optionsv sets connection, TLS, plugin, and option-file options on a
  MariaDB Connector/C handle before mysql_real_connect, supporting a variable
  argument list.
---

# mysql\_optionsv

## Syntax

```c
int mysql_optionsv(MYSQL * mysql,
                   enum mysql_option,
                   const void * arg,
                   ...);
```

* `mysql` - a `mysql` handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `mysql_option` - the option to set. See description below.
* `arg` - the value for the option.
* `...` - variable argument list.

## Description

Used to set extra connect options and affect behavior for a connection. This function may be called multiple times to set several options. All calls pass numeric literal values for a `const void *`. `mysql_optionsv()` should be called after [mysql\_init()](mysql_init.md).

Some of these options can also be set in [option files](../configuring-mariadb-connectorc-with-option-files.md), such as `my.cnf`.

## Return Value

Returns zero on success, non-zero if an error occurred (invalid option or value).

### Variable Types

The following table shows the C variable type required for the `arg` parameter of each option:

| Variable type                 | Options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `my_bool`, `unsigned char`    | `MYSQL_OPT_RECONNECT`, `MYSQL_SECURE_AUTH`, `MYSQL_REPORT_DATA_TRUNCATION`, `MYSQL_OPT_SSL_ENFORCE`, `MYSQL_OPT_SSL_VERIFY_SERVER_CERT`, `MARIADB_OPT_SKIP_READ_RESPONSE`, `MYSQL_OPT_ZSTD_COMPRESSION_LEVEL`                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `unsigned int`                | `MYSQL_OPT_PORT`, `MYSQL_OPT_LOCAL_INFILE`, `MYSQL_OPT_CONNECT_TIMEOUT`, `MYSQL_OPT_PROTOCOL`, `MYSQL_OPT_READ_TIMEOUT`, `MYSQL_OPT_WRITE_TIMEOUT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `unsigned long`               | `MYSQL_OPT_NET_BUFFER_LENGTH`, `MYSQL_OPT_MAX_ALLOWED_PACKET`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `const char *`                | `MYSQL_INIT_COMMAND`, `MARIADB_OPT_UNIXSOCKET`, `MARIADB_OPT_PASSWORD` , `MARIADB_OPT_USER`, `MARIADB_OPT_HOST`, `MARIADB_OPT_SCHEMA`, `MYSQL_OPT_SSL_KEY`, `MYSQL_OPT_SSL_CERT`, `MYSQL_OPT_SSL_CA`, `MYSQL_OPT_SSL_CAPATH`, `MYSQL_SET_CHARSET_NAME`, `MYSQL_SET_CHARSET_DIR`, `MYSQL_OPT_SSL_CIPHER`, `MYSQL_SHARED_MEMORY_BASE_NAME`, `MYSQL_PLUGIN_DIR`, `MYSQL_DEFAULT_AUTH`, `MARIADB_OPT_SSL_FP`, `MARIADB_OPT_SSL_FP_LIST`, `MARIADB_OPT_TLS_PASSPHRASE`, `MARIADB_OPT_TLS_VERSION`, `MYSQL_OPT_BIND`, `MYSQL_OPT_CONNECT_ATTR_DELETE`, `MYSQL_OPT_CONNECT_ATTR_ADD`, `MARIADB_OPT_CONNECTION_HANDLER`, `MYSQL_SERVER_PUBLIC_KEY`, `MARIADB_OPT_RESTRICTED_AUTH` |
| `const char*`, `unsigned int` | `MARIADB_OPT_RPL_REGISTER_REPLICA`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -                             | `MYSQL_OPT_CONNECT_ATTR_RESET`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `void *`                      | `MARIADB_OPT_PROXY_HEADER`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Options

*   `MYSQL_INIT_COMMAND`: lets you specify a command to execute immediately after connecting (and also after a reconnect if enabled).

    ```c
    mysql_optionsv(mysql, MYSQL_INIT_COMMAND, (void *)"CREATE TABLE test.t1(a int)");
    mysql_optionsv(mysql, MYSQL_INIT_COMMAND, (void *)"SET @value := 1");
    ```

    * Each call adds one SQL statement to an internal list; all stored commands are executed in order.
    * You cannot concatenate multiple statements with semicolons; each statement must be added with a separate call.

    **Note**: When multiple option files are used, `init_command` entries are aggregated from all files read (for example, `/etc/my.cnf` and `~/.my.cnf`). The resulting combined list of statements executes on every connection and reconnection, without any clear indication that they originated from different sources. If unexpected statements run during a connection, review all active option files to identify their source.
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
*   `MYSQL_PROGRESS_CALLBACK`: Specifies a callback function which will be able to visualize the progress of certain long running statements (i.e. [LOAD DATA LOCAL INFILE](broken-reference/) or [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table)).

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
*   `MYSQL_OPT_NONBLOCK`: Specify stack size for non-blocking operations.\
    The argument for MYSQL\_OPT\_NONBLOCK is the size of the stack used to save the state of a non-blocking operation while it is waiting for I/O and the application is doing other processing. Normally, applications will not have to change this, and it can be passed as zero to use the default value.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_NONBLOCK, 0);
    ```
*   `MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS`: If this option is set, the client indicates that it will be able to handle expired passwords by setting the `CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS` capability flag.\
    If the password has expired and `CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS` is set, the server will not return an error when connecting, but put the connection in sandbox mode, where all commands will return error 1820 (`ER_MUST_CHANGE_PASSWORD`) unless a new password was set. This option was added in MariaDB Connector/C 3.0.4

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

Some of these options can also be set as arguments to the [mysql\_real\_connect](mysql_real_connect.md) function.

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
* `MYSQL_OPT_ZSTD_COMPRESSION_LEVEL`: The compression level to use for connections that use the `zstd` compression algorithm. Acceptable values are integers in the range 1 (fastest) to 22 (maximum compression). This option has no effect if `zstd` compression is not in use. Added in MariaDB Connector/C 3.3.14 and 3.4.4 versions.
*   `MYSQL_OPT_LOCAL_INFILE`: Enable or disable the use of [LOAD DATA LOCAL INFILE](broken-reference/)

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

*   `MYSQL_OPT_SSL_KEY`: Defines a path to a private key file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. If the key is protected with a passphrase, the passphrase needs to be specified with `MARIADB_OPT_TLS_PASSPHRASE` option.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_KEY, (void *)"certs/client-key.pem");
    ```
*   `MYSQL_OPT_SSL_CERT`: Defines a path to the X509 certificate file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CERT, (void *)"certs/client-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CA`: Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CA, (void *)"certs/ca-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CAPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information. This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");
    ```
*   `MYSQL_OPT_SSL_CIPHER`: Defines a list of permitted ciphers or cipher suites to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption).

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CIPHER, (void *)"DHE-RSA-AES256-SHA");
    ```
*   `MYSQL_OPT_SSL_CRL`: Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information. This option is only supported if the connector was built with OpenSSL or Schannel. If the connector was built with GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");\\\\<<code>>mysql_optionsv(mysql, MYSQL_OPT_SSL_CRL, (void *)"certs/crl.pem");
    ```
*   `MYSQL_OPT_SSL_CRLPATH`: Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information. This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MYSQL_OPT_SSL_CAPATH, (void *)"certs/ca-cert.pem");\\\\<<code>>mysql_optionsv(mysql, MYSQL_OPT_SSL_CRLPATH, (void *)"certs/crls");
    ```
*   `MARIADB_OPT_SSL_FP`: Specify the fingerprint hash of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption) handshake. Before version 3.4.0, Connector/C accepted only `SHA1` hashes. Starting with version 3.4.0, support was extended to include `SHA256`, `SHA384`, and `SHA512`. This option is deprecated. Use `MARIADB_OPT_TLS_PEER_FP` instead.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_FP, (void *)"3a079e1a14ad326953a5d280f996b93d772a5bea");
    ```
*   `MARIADB_OPT_TLS_PEER_FP`: Specify the SHA1 fingerprint of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption) handshake.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_PEER_FP, (void *)"3a079e1a14ad326953a5d280f996b93d772a5bea");
    ```
*   `MARIADB_OPT_SSL_FP_LIST`: Specify a file containing one or more fingerprint hashes of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption) handshake. Before version 3.4.0, Connector/C accepted only `SHA1` hashes. Starting with version 3.4.0, support was extended to include `SHA256`, `SHA384`, and `SHA512`. This is deprecated. Use `MARIADB_OPT_TLS_PEER_FP_LIST` instead.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_FP_LIST, (void *)"certs/fingerprints.txt");
    ```
*   `MARIADB_OPT_TLS_PEER_FP_LIST`: Specify a file which contains one or more SHA1 fingerprints of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption) handshake.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_PEER_FP_LIST, (void *)"certs/fingerprints.txt");
    ```
*   `MARIADB_OPT_TLS_PASSPHRASE`: Specify a passphrase for a passphrase-protected private key, as configured by the `MYSQL_OPT_SSL_KEY` option. This option is only supported if the connector was built with OpenSSL or GnuTLS. If the connector was built with Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_SSL_PASSPHRASE, (void *)"thisisashortpassphrase");
    ```
*   `MARIADB_OPT_TLS_VERSION`: Defines which [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption) protocol versions are allowed. This should be a comma-separated list of TLS protocol versions to allow. Valid TLS protocol versions are `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. Both the client and server should support the allowed TLS protocol versions. See [Secure Connections Overview: TLS Protocol Version Support](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#tls-protocol-version-support) for information on which TLS libraries support which TLS protocol versions. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which TLS libraries are used on which platforms.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_TLS_VERSION, (void *)"TLSv1.2,TLSv1.3");
    ```
*   `MYSQL_OPT_SSL_VERIFY_SERVER_CERT`: Enables (or disables) [server certificate verification](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview#server-certificate-verification).

    ```c
    my_bool verify= 1;
    mysql_optionsv(mysql, MYSQL_OPT_SSL_VERIFY_SERVER_CERT, (void *)&verify);
    ```
*   `MYSQL_OPT_SSL_ENFORCE`: Enables [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview) using the default system settings. Does not require TLS certificates, keys, or CAs to be explicitly configured.

    ```c
    my_bool enforce_tls= 1;
    mysql_optionsv(mysql, MYSQL_OPT_SSL_ENFORCE, (void *)&enforce_tls);
    ```
* **Note**: Despite the option name, this does **not** enforce TLS. If the server does not support TLS, the\
  connection falls back to unencrypted communication without error. To prevent fallback and enforce TLS, use `MYSQL_OPT_SSL_VERIFY_SERVER_CERT` instead.
*   `MARIADB_OPT_TLS_CIPHER_STRENGTH`: **Deprecated**. This option is no longer in use and has no effect. Cipher strength. This value will be passed as an unsigned `int` parameter.

    ```c
    unsigned int cipher_strength= 128;
    mysql_optionsv(mysql, MARIADB_OPT_TLS_CIPHER_STRENGTH, (void*)&cipher_strength);
    ```

#### Plugin Options

*   `MYSQL_DEFAULT_AUTH`: Default authentication client-side plugin to use.

    ```c
    mysql_optionsv(mysql, MYSQL_DEFAULT_AUTH, (void *)"ed25519");
    ```
*   `MYSQL_ENABLE_CLEARTEXT_PLUGIN`: This option is supported to be compatible with MySQL client libraries. MySQL client libraries use this option to determine whether the [mysql\_clear\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam#client-authentication-plugins) authentication plugin can be used. However, MariaDB clients and client libraries do not need to set any options in order to use this authentication plugin. Therefore, this option does not actually do anything in MariaDB Connector/C.

    ```c
    mysql_optionsv(mysql, MYSQL_ENABLE_CLEARTEXT_PLUGIN, 1);
    ```
*   `MARIADB_OPT_CONNECTION_HANDLER`: Specify the name of a connection handler plugin.

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_CONNECTION_HANDLER, (void *)"aurora");
    ```
*   `MARIADB_OPT_RESTRICTED_AUTH`: Specifies a comma-separated list of authentication plugins that are permitted for authenticating this connection. If the server requests an authentication plugin that is not in this list, MariaDB Connector/C returns an error and the connection is refused. This option can be used to prevent the use of weaker authentication methods.\
    Added in MariaDB Connector/C 3.3.0 version.

    ```c
    c mysql_optionsv(mysql, MARIADB_OPT_RESTRICTED_AUTH, (void *)"ed25519,caching_sha2_password");
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
* `MARIADB_OPT_SKIP_READ_RESPONSE`: Disables server response packet reading in the binary protocol. Designed for specialized connection handlers, not for typical application use. Added in Connector/C 3.1.13 version.&#x20;
*   `MYSQL_PLUGIN_DIR`: Specify the location of client plugins. The plugin directory can also be specified with the `MARIADB_PLUGIN_DIR` environment variable.

    ```c
    mysql_optionsv(mysql, MYSQL_PLUGIN_DIR, (void *)"/opt/mariadb/lib/plugins");
    ```
*   `MYSQL_SECURE_AUTH`: Refuse to connect to the server if the server uses the [mysql\_old\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password) authentication plugin. This mode is off by default, which is a difference in behavior compared to MySQL 5.6 and later, where it is on by default.

    ```c
    mysql_optionsv(mysql, MYSQL_SECURE_AUTH, 1);
    ```
*   `MYSQL_SERVER_PUBLIC_KEY`: Specifies the name of the file which contains the RSA public key of the database server. The format of this file must be in PEM format. This option is used by the [caching\_sha2\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) client authentication plugin. It was introduced in Connector/C 3.1.0.

    ```c
    mysql_optionsv(mysql, MYSQL_SERVER_PUBLIC_KEY, (void *)(void *)"certs/server-cert.pem);
    ```

#### Callback Options

*   `MARIADB_OPT_STATUS_CALLBACK`: Specifies a callback function that is invoked whenever the server sends a status change or session tracking information to the client. This can be used to monitor server status flags and session variable changes without polling.&#x20;



    ```c
    mysql_optionsv(mysql, MARIADB_OPT_STATUS_CALLBACK, (void *)my_status_callback, (void *)user_data);
    ```

    \
    The callback function must match the following signature:

    ```c
    void status_callback(void *data, enum enum_mariadb_status_info type, ..)
    ```

&#x20;**Parameters**

| Parameter | Type                            | Description                                                                                                                    |
| --------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `data`    | `void *`                        | The pointer passed as the second argument when registering the callback (typically a connection handle or application context) |
| `type`    | `enum enum_mariadb_status_info` | Indicates the category of information being delivered. Either `STATUS_TYPE` or `SESSION_TRACK_TYPE`.                           |

**Variadic Parameters (vary by `type`)**

When type is `STATUS_TYPE`:

| Position | Type           | Description                      |
| -------- | -------------- | -------------------------------- |
| 1st      | `unsigned int` | The current server status flags. |

When type is `SESSION_TRACK_TYPE`:

<table><thead><tr><th width="211.22222900390625">Position</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td>1st</td><td><code>enum enum_session_state_type</code></td><td>The session tracking type.</td></tr><tr><td>2nd</td><td><code>MARIADB_CONST_STRING *</code></td><td>If <code>track_type</code> is <code>SESSION_TRACK_SYSTEM_VARIABLES</code>: the variable name.</td></tr><tr><td>3rd </td><td><code>MARIADB_CONST_STRING *</code></td><td>If <code>track_type</code> is <code>SESSION_TRACK_SYSTEM_VARIABLES</code>: the variable value.</td></tr></tbody></table>

{% hint style="info" %}
When a status callback is registered, the connector’s built‑in session tracking functions are disabled. After calling `mysql_optionsv()` with `MARIADB_OPT_STATUS_CALLBACK`, the functions `mysql_session_track_get_first()` and `mysql_session_track_get_next()` will no longer provide session tracking data. Instead, all session tracking must be managed within the callback itself.
{% endhint %}

An example implementation can be found in the Connector/C source tree at `unittest/libmariadb/connection.c` (function `test_status_callback`). Added in MariaDB Connector/C 3.3.2 version.

#### Replication/Binlog API Options

*   `MARIADB_OPT_RPL_REGISTER_REPLICA`: Specifies the host name and port that the Binlog API will report when registering this client as a replica with the connected server. When this option is set, `mariadb_rpl_open()` will register the client using the provided host, port, and the server ID configured via `mariadb_rpl_optionsv()`. The registration is visible in the output of `SHOW SLAVE STATUS` on the server. <br>

    ```c
    mysql_optionsv(mysql, MARIADB_OPT_RPL_REGISTER_REPLICA, (void *)"replica-host.example.com", (unsigned int)3306);
    ```

    \
    Added in MariaDB Connector/C 3.3.1 version.  See [Replication API Reference](../mariadb-binlogreplication-api-reference/).

#### Option File Options

* `MYSQL_READ_DEFAULT_FILE`: Read options from an [option file](../configuring-mariadb-connectorc-with-option-files.md).
* `MYSQL_READ_DEFAULT_GROUP`: Read options from the named [option group](../configuring-mariadb-connectorc-with-option-files.md#option-groups) from an [option file](../configuring-mariadb-connectorc-with-option-files.md).

These options work together, according to the following rules:

* if both are set to `NULL`, then no option files are read.
* if `MYSQL_READ_DEFAULT_FILE` is set to an empty string (or `NULL` and `MYSQL_READ_DEFAULT_GROUP` is set) then all [default option files](../configuring-mariadb-connectorc-with-option-files.md#default-option-file-locations) are read.
* if `MYSQL_READ_DEFAULT_FILE` is set to a non-empty string, then it is interpreted as a path to a [custom option file](../configuring-mariadb-connectorc-with-option-files.md#custom-option-file-locations), and only that option file is read.
* if `MYSQL_READ_DEFAULT_GROUP` is an empty string (or `NULL` and `MYSQL_READ_DEFAULT_FILE` is set) then only default groups — `[client]`, `[client-server]`, `[client-mariadb]` are read.
* if `MYSQL_READ_DEFAULT_GROUP` is a non-empty string, then it is interpreted as a custom option group, and that custom option group is read in addition to default groups from above.

#### Proxy Settings&#x20;

As defined by the [proxy protocol specification](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt), a client may prefix its first packet with a proxy protocol header. The server will parse this header and treat the IP address it contains as the client's actual IP address, rather than the address of the connecting process.&#x20;

* `MARIADB_OPT_PROXY_HEADER`: Specifies the proxy protocol header to prefix to the first packet sent to the server. The option requires two additional arguments:&#x20;
  * a `void *` pointer to the header buffer, and&#x20;
  * a `size_t` value for the buffer length.

```sql
const char *hdr = "PROXY TCP4 192.168.0.1 192.168.0.11 56324 443\r\n"; mysql_optionsv(mysql, MARIADB_OPT_PROXY_HEADER, (void *)hdr, strlen(hdr));
```

#### Connection Attribute Options

Connection attributes are stored in the [session\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-session_connect_attrs-table) and [session\_account\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-session_account_connect_attrs-table) Performance Schema tables.\
By default, MariaDB Connector/C sends the following connection attributes to the server:

* \_client\_name: always "libmariadb"
* \_client\_version: version of MariaDB Connector/C
* \_os: operation system
* \_pid: process id
* \_platform: e.g. x86 or x64
* \_server\_host: the hostname (as specified in mysql\_real\_connect). This attribute was added in Connector/C 3.0.5

{% hint style="info" %}
If the [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) is disabled, connection attributes will not be stored on server.
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
