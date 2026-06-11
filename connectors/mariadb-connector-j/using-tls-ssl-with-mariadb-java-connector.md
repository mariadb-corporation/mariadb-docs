---
description: >-
  Configure TLS and SSL for MariaDB Connector/J using sslMode, serverSslCert,
  and keyStore options, supporting trust, verify-ca, verify-full, and
  zero-configuration encryption modes.
---

# Using TLS/SSL with MariaDB Connector/J

## Overview

This document explains how to configure the MariaDB Java driver to support TLS/SSL.

Data can be encrypted during transfer using the Transport Layer Security (TLS) protocol.\
TLS/SSL permits transfer encryption and, optionally, server and client identity validation.

{% hint style="info" %}
The term SSL (Secure Sockets Layer) is often used interchangeably with TLS, although strictly-speaking the SSL protocol is the predecessor of TLS, and is not implemented as it is now considered insecure.
{% endhint %}

### Server configuration

To ensure that SSL is correctly configured on the server, the query "SELECT @@have\_ssl;" must return YES. If not, please refer to the [server documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption).

Connecting to a server that doesn't support TLS with the TLS option set, an exception "Trying to connect with SSL, but SSL not enabled in the server" will be thrown.

### TLS Protocol Version Selection

The MariaDB Java driver by default uses Java's default supported protocols. If the servers are MariaDB on Unix or version >= 10.2, consider adding the TLSv1.2 protocol. This can be set using the "enabledSslProtocolSuites" option (example: enabledSslProtocolSuites=TLSv1.2, TLSv1.3).

In addition to the protocol, the driver relies on the Java default cipher list. The Java default enabled ciphers are [listed here](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SupportedCipherSuites). JAVA allows cipher suites to be removed/excluded from use in the security policy using the Java system property "jdk.tls.disabledAlgorithms." The specific list of ciphers to be used can be set using the "enabledSslCipherSuites" driver option (example: "enabledSSLCipherSuites=TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256,...")

## One-way SSL authentication

By default, the driver can be configured to use TLS even if the authentication user is not explicitly required to use it. However, it is recommended to create a user with the `REQUIRE SSL` option to enforce TLS. For details, see _CREATE USER_ to ensure the connector always uses TLS.

Example:

```sql
CREATE USER 'myUser'@'%' IDENTIFIED BY 'MyPwd';
GRANT ALL ON db_name.* TO 'myUser'@'%' REQUIRE SSL;
```

Since version 3 of the connector, TLS is enabled with the client-side setting option "sslMode."\
The following values are supported:

* Disable: Do not use SSL/TLS (default)
* Trust: Only use SSL/TLS for encryption. Do not perform certificate or hostname verification.
* verify-ca: Use SSL/TLS for encryption and perform certificate verification, but do not perform hostname verification.
* verify-full:Use SSL/TLS for encryption, certificate verification, and hostname verification. This is the standard TLS behavior. Aliases "true"/"1" are possible like "sslMode=true."

{% hint style="info" %}
Before connector 3 version, other options were used in order to use TLS:

* useSsl: boolean, indicate if TLS has to be enable.
* trustServerCertificate: boolean, when enable with useSsl=true, corresponds to sslMode=trust
* disableSslHostnameVerification: boolean, when enable with useSsl=true and trustServerCertificate is not enable, corresponds to sslMode=verify-ca
{% endhint %}

To ensure TLS is enabled server-side, first try with the option "sslMode=trust."

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd"
		+ "&sslMode=trust")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

This configuration is not safe for production. While all data exchanges are encrypted, the server’s identity is not verified, leaving the connection vulnerable to man-in-the-middle attacks by malicious servers.

To ensure the server’s identity is validated, the client must trust the server’s root and intermediate certificates. This can be accomplished in several ways:

* Java includes a default truststore containing certificates from well-known Certificate Authorities (CAs), such as Let’s Encrypt (added in Java 8u101), VeriSign, Entrust, and GTE CyberTrust. If the server’s certificate chain is signed by a root CA present in this default truststore, no additional client-side configuration is required. The default truststore location is defined by the system property `javax.net.ssl.trustStore`.
* Alternatively, you can explicitly provide the server’s certificate using the `serverSslCert` option.
* Starting with Connector version 3.4+ and MariaDB Server 11.4+, zero-configuration TLS encryption is supported. For details, see the dedicated chapter.

By default, when `sslMode` is enabled (and not set to `DISABLED`), the connector will use the certificate specified in `serverSslCert`if provided, or fall back to the default truststore if not. This fallback behavior can be disabled by setting the `fallbackToSystemTrustStore` option to `false`.

### Java default truststore

Java trustStore is a file that contains certificates of trusted SSL servers or certificate authorities trusted to identify servers. Truststore can be protected by a password.

The Java search order for locating the trust store is

1. system property "javax.net.ssl.trustStore"
2. $JAVA\_HOME/lib/security/jssecacerts
3. $JAVA\_HOME/lib/security/cacerts (shipped by default)

To include a certificate from a CA that is not already in the truststore, first locate your system’s default truststore. By default, it can be found at: `$JAVA_HOME/jre/lib/security/cacerts`.

```java
//copy the java truststore to jssecacerts
cp $JAVA_HOME/jre/lib/security/cacerts $JAVA_HOME/jre/lib/security/jssecacerts
//add your certificate to the truststore
keytool -importcert -file myCA-root.cer -alias myCA -keystore /usr/java/default/jre/lib/security/jssecacerts -storepass changeit
```

If you’re referring to the database connection string from our earlier example, switching `sslMode` to `"verify-full"` just means updating that property in your config or connection URL.

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd"
		+ "&sslMode=verify-full")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

### Provide the certificate directly

The `serverSslCert` option specifies the location of the server’s SSL certificate. The location can be provided in one of the following three formats:

1. **Full file path** – e.g., `serverSslCert=/path/to/cert.pem`
2. **Classpath-relative path** – e.g., `serverSslCert=classpath:relative/cert.pem` (relative to the current classpath)
3. **Inline certificate string** – a verbatim DER-encoded certificate, e.g., `"-----BEGIN CERTIFICATE-----..."`

Example :

```java
try (Connection con = DriverManager.getConnection("jdbc:mariadb://localhost/myDb?user=myUser&password=MyPwd&serverSslCert=/path/to/cert.pem&&sslMode=verify-full")) {
	try (Statement stmt = con.createStatement()) {
		stmt.execute("select 1");
	}
}
```

### Zero-configuration TLS encryption

In MariaDB Server 11.4, TLS configuration is simpler than before. When connecting with MariaDB Connector/J 3.4 or later, you can enable SSL encryption by setting `sslMode=verify-full`—no other SSL parameters are needed.\
During the TLS handshake, the server provides its certificate, and the client confirms the server’s identity using the certificate fingerprint along with password hashing. For this verification to succeed, the password must not be empty.

## Mutual (2-way) authentication

Mutual SSL authentication, also known as certificate-based mutual authentication, is a process where two parties verify each other’s identity by validating the digital certificates presented, ensuring that both sides can trust the authenticity of the other.

To enable mutual authentication, the user must be created with "REQUIRE X509" so the server asks the driver for client certificates. See [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) for more details.

Example:

```sql
CREATE USER 'myUser'@'%' IDENTIFIED BY 'MyPwd';
GRANT ALL ON db_name.* TO 'myUser'@'%' REQUIRE X509;
```

**If the user is not set with REQUIRE X509, only one- way authentication will be done**

The client (driver) must also have its own certificate along with the corresponding private key. If the driver does not present a certificate and the user account is configured with **`REQUIRE X509`**, the server will respond with a simple “Access denied for user” message.

In Java, the client certificate and its private key are stored in a **keystore** file. A keystore is similar to a **truststore**—in fact, they are often the same file.

**Example: Generating a keystore in JKS format**

```bash
# generate a keystore with the client cert & key
  openssl pkcs12 \
    -export \
    -in "${clientCertFile}" \
    -inkey "${clientKeyFile}" \
    -out "${tmpKeystoreFile}" \
    -name "mariadbAlias" \
    -passout pass:kspass

  # convert PKSC12 to JKS
  keytool \
    -importkeystore \
    -deststorepass kspass \
    -destkeypass kspass \
    -destkeystore "${clientKeystoreFile}" \
    -srckeystore ${tmpKeystoreFile} \
    -srcstoretype PKCS12 \
    -srcstorepass kspass \
    -alias "mariadbAlias"
```

Like the truststore, you can use the Java default keystore without requiring any additional options.\
Alternatively, you can specify a dedicated keystore by using the `keyStore` option to provide its location and the `keyStorePassword` option to set its password.\
If the JKS keystore includes a separate password for a specific key, you can set it with the `keyPassword` option.

## Troubleshooting

### SSL not enabled on server

If you encounter the error:

```
pgsqlCopyEditjava.sql.SQLException: Trying to connect with ssl, but ssl not enabled in the server
```

It means SSL is disabled on the server. Since the connection was made with the `useSSL=true` option, it failed.\
To verify the SSL status on the server, run:

```sql
sqlCopyEditSHOW VARIABLES LIKE '%ssl%';
```

### Server certificate not provided to the client

When the driver attempts an SSL connection without a provided certificate, or when `trustServerCertificate=true` is not set, the connection will fail with an exception similar to:

```
luaCopyEditCaused by: sun.security.validator.ValidatorException: PKIX path building failed:
sun.security.provider.certpath.SunCertPathBuilderException:
unable to find valid certification path to requested target
```

Solution:

* **Not recommended:** Set the `sslMode` option to `trust`.
* Add the server certificate to the driver (see documentation above).

### **Access Denied for User** Error:

```
pgsqlCopyEditjava.sql.SQLInvalidAuthorizationSpecException: Could not connect: Access denied for user
```

This can occur due to:

1. Incorrect username or password.
2.  SSL requirements are set for the user that the connection does not meet.\
    You can check the SSL settings for a user with:

    ```sql
    sqlCopyEditSELECT SSL_TYPE, SSL_CIPHER, X509_ISSUER, X509_SUBJECT
    FROM mysql.user u
    WHERE u.User = '';
    ```

{% @marketo/form formId="4316" %}
