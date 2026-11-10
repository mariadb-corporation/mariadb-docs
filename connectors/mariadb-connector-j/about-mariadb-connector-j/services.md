---
description: >-
  Extend MariaDB Connector/J with credential, authentication, and SSL
  factory services, including the AWS IAM and environment credential plugins.
---

# MariaDB Connector/J Services

Services let you extend MariaDB Connector/J, for example to obtain credentials from an external source, without changing application code.

The driver implements 3 kinds of services:

* Credential service: permit giving credential
* Authentication service: permit adding client authentication plugins.
* SSL factory service: custom TSL implementation

## Credential service

Credentials are usually set using user/password in the connection string or by using DriverManager.getConnection(String url, String user, String password).

Credential plugins permit to provide credential information from other means. Those plugins have to be activated setting option `credentialType` to designated plugin.

The driver has 3 default plugins :

### **AWS IAM**

This permits AWS database IAM authentication. The plugin generate a token using IAM credential and region. Token is valid for 15 minutes and cached for 10 minutes.

The token is signed with the AWS credentials and region resolved by the AWS SDK default chains (environment variables, system properties, profile files, instance metadata). Connection string options can override them:

| Option                     | Role                                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| `accessKeyId`, `secretKey` | Static credentials in place of the default credential chain                                              |
| `region`                   | AWS region in place of the default region chain                                                          |
| `roleArn`                  | IAM role to assume through STS. The token is then signed with the role's temporary credentials. Since 4.0.0 |
| `roleSessionName`          | Session name of the assumed role, default `mariadb-connector-j`. Since 4.0.0                              |
| `externalId`               | External id of the assumed role, when the role requires one. Since 4.0.0                                  |

TLS is mandatory with IAM authentication: the plugin refuses `sslMode=disable`.

**Connector/J 4.0 and later:** the plugin is the separate `org.mariadb.jdbc:mariadb-java-client-aws` artifact, so that the connector itself carries no AWS SDK dependency. Add it next to the connector; it brings the AWS SDK modules it needs. The artifact ships the RDS root certificates, so the default `sslMode=verify-full` validates the RDS certificate chain and host name without any option. The system trust store stays trusted next to them, so RDS Proxy endpoints, which use publicly issued certificates, work as well. The `serverSslCert` or `trustStore` options override the bundle, for example for the AWS China or GovCloud regions, which publish their own bundles.

```xml
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client-aws</artifactId>
    <version>4.0.0</version>
</dependency>
```

Example: `jdbc:mariadb://mydb.123456789012.eu-west-1.rds.amazonaws.com/db?user=iam_user&credentialType=AWS-IAM`

**Connector/J 3.x:** the plugin is bundled with the connector, and the `software.amazon.awssdk:rds` dependency must be present in the classpath. The RDS certificate bundle must be provided with the `serverSslCert` option.

Example: `jdbc:mariadb://host/db?credentialType=AWS-IAM&sslMode=verify-full&serverSslCert=/somepath/global-bundle.pem`

with `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_REGION` environment variable set.

### **Environment**

User and Password are retrieved from environment variables. default environment variables are `MARIADB_USER` and `MARIADB_PWD`, but can be changed by setting additional option `userKey` and `pwdKey`

Example : using connection string `jdbc:mariadb://host/db?credentialType=ENV` user and password will be retrieved from environment variable `MARIADB_USER` and `MARIADB_PWD`.

### **Property**

User and Password are retrieved from java properties. default property name are mariadb.user and mariadb.pwd, but property names can be changed by setting additional option `userKey` and `pwdKey`

Example : using connection string `jdbc:mariadb://host/db?credentialType=PROPERTY&userKey=mariadbUser&pwdKey=mariadbPwd` user and password will be retrieved from java properties `mariadbUser` and `mariadbPwd`

## Authentication service

[Client authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) are now defined as services. This permits to easily add new client authentication plugins.

List of authentication plugins in java connector :

* mysql\_clear\_password
* auth\_gssapi\_client
* client\_ed25519
* mysql\_native\_password
* mysql\_old\_password
* dialog (PAM)
* sha256\_password
* caching\_sha2\_password

New authentication plugins can be created implementing interface `org.mariadb.jdbc.authentication`.`AuthenticationPlugin`, and listing new plugin in a `META-INF/services/org.mariadb.jdbc.authentication.AuthenticationPlugin` file.

## SSL factory service

Custom SSL implementation can be used implementing A connection to a server initially creates a socket. When set, SSL socket is layered over this existing socket. Implementing `org.mariadb.jdbc.tls.TlsSocketPlugin` permit to provide custom SSL implementation for example create a new [HostnameVerifier](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/net/ssl/HostnameVerifier.html) implementation.

Custom implementation need to implement `org.mariadb.jdbc.tls.TlsSocketPlugin` and register service `META-INF/services/org.mariadb.jdbc.tls.TlsSocketPlugin`

Custom implementation are activated using option `tlsSocketType`

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
