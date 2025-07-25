# Connector/J 3.0.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-j-300-release-notes.md)[Changelog](../changelogs/3.0/mariadb-connector-j-300-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 04 May 2021

MariaDB Connector/J 3.0.0 is a [_**Alpha**_](../../../community-server/about/release-criteria.md) _**(Alpha)**_ release.

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

**NOTE:** MariaDB Connector/J 3.0.0 is fully compatible with the latest release\
of version 2.7. Further maintenance releases will not be provided for version\
2.7 after MariaDB Connector/J 3.0 becomes stable (GA).

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a complete rewrite of the Java driver. The goal being to have a\
more performant, easy to read, extendable, small driver.

* Complete rewrite, code simplification / clarification, reduced size (15%),\
  more than 90% coverage tested.
* Performance Improvements:
  * Prepare and execution are now using pipelining when using option `useServerPrepStmts`
  * Performance enhancement with [MariaDB 10.6](../../../community-server/mariadb-10-6-series/what-is-mariadb-106.md) server when using option `useServerPrepStmts`, skipping metadata (see [MDEV-19237](https://jira.mariadb.org/browse/MDEV-19237))

### SSL configuration

New Options :

The options `useSsl`, `trustServerCertificate`, and `disableSslHostnameVerification` still exist, but `sslMode` allows for easier configuration.

### Easy logging

If using `slf4j`, just enable the package "org.mariadb.jdbc" log.

* Level `ERROR` will log connection errors
* Level `WARNING` will log query errors
* Level `DEBUG` will log queries
* Level `TRACE` will log all exchanges with server

If not using `slf4j`, console logging will be used.

If you really want to use the JDK logger, the System property\
"`mariadb.logging.fallback`" set to `JDK` will indicate to use common\
logging.

### Failover

The Failover implementation now permits redoing transactions : when creating a\
transaction, all commands will be cached, and can be replayed in case of\
failover.

This functionality can be enabled using the option `transactionReplay`.

This is not enabled by default, because it requires that the application avoid using non-idempotent commands.

Example:

```sql
START TRANSACTION;
SELECT next_val(hibernate_sequence);
INSERT INTO myCar(id, name) VALUE (?, ?) //WITH PARAMETERS: 1, 'car1'
INSERT INTO myCarDetail(id, carId, name) VALUE (?, ?, ?) //WITH PARAMETERS: 2, 1, 'detail1'
INSERT INTO myCarDetail(id, carId, name) VALUE (?, ?, ?) //WITH PARAMETERS: 3, 2, 'detail2'
COMMIT;
```

### Allow setup of socket TCP\_KEEPIDLE, TCP\_KEEPCOUNT, TCP\_KEEPINTERVAL

Equivalent options are `tcpKeepIdle`, `tcpKeepCount`, `tcpKeepInterval`

Because these are available only with Java 11, setting these options with java < 11 will have no effect.

### permit authentication plugin restriction

New Options :

example setting `restrictedAuth` to "mysql\_native\_password,client\_ed25519,auth\_gssapi\_client", only those plugins can be use. If server return ask for an authentication plugin not listed in `restrictedAuth`, driver will throw an exception.

### Extendable

The driver is built with a Service Provider Interface (SPI), permitting easy ways to extend the driver.

Possible extensions:

* `org.mariadb.jdbc.codec.Codec` : Allows encoding/decoding types
* `org.mariadb.jdbc.plugin.authentication.AuthenticationPlugin` : Allows authentication plugin additions. Defaults are "mysql\_clear\_password", "auth\_gssapi\_client", "client\_ed25519", "mysql\_native\_password", "dialog" (PAM), and "caching\_sha2\_password"
* `org.mariadb.jdbc.plugin.credential.CredentialPlugin` : Allows login/password retrieval. Defaults are "AwsIamCredentialPlugin" to permit retrieve a temporary IAM authentication, "EnvCredentialPlugin" to get environment authentication, and "PropertiesCredentialPlugin" to get authentication info from java property
* `org.mariadb.jdbc.plugin.tls.TlsSocketPlugin` : Allows extended TLS implementation

## Bugs Fixed

* [CONJ-864](https://jira.mariadb.org/browse/CONJ-864) - `includeThreadDumpInDeadlockExceptions` always includes the thread dump, even when it is not a deadlock exception
* [CONJ-858](https://jira.mariadb.org/browse/CONJ-858) - Properties parameters that differ from string not taken in account

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.0.0, with links to detailed\
information on each push, see the [changelog](../changelogs/3.0/mariadb-connector-j-300-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
