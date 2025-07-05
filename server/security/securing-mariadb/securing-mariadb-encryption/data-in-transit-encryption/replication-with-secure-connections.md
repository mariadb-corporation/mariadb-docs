# Replication with Secure Connections

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

By default, MariaDB replicates data between primaries and replicas without encrypting it. This is generally acceptable when the primary and replica run are in networks where security is guaranteed through other means. However, in cases where the primary and replica exist on separate networks or they are in a high-risk network, the lack of encryption does introduce security concerns as a malicious actor could potentially eavesdrop on the traffic as it is sent over the network between them.

To mitigate this concern, MariaDB allows you to encrypt replicated data in transit between primaries and replicas using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix `ssl_`, but internally, MariaDB only supports its secure successors.

In order to secure connections between the primary and replica, you need to ensure that both servers were compiled with TLS support. See [Secure Connections Overview](secure-connections-overview.md) to determine how to check whether a server was compiled with TLS support.

You also need an X509 certificate, a private key, and the Certificate Authority (CA) chain to verify the X509 certificate for the primary. If you want to use two-way TLS, then you will also an X509 certificate, a private key, and the Certificate Authority (CA) chain to verify the X509 certificate for the replica. If you want to use self-signed certificates that are created with OpenSSL, then see [Certificate Creation with OpenSSL](certificate-creation-with-openssl.md) for information on how to create those.

## Securing Replication Traffic

In order to secure replication traffic, you will need to ensure that TLS is enabled on the primary. If you want to use two-way TLS, then you will also need to ensure that TLS is enabled on the replica. See [Securing Connections for Client and Server](securing-connections-for-client-and-server.md) for information on how to do that.

For example, to set the TLS system variables for each server, add them to a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) on each server:

```
[mariadb]
...
ssl_cert = /etc/my.cnf.d/certificates/server-cert.pem
ssl_key = /etc/my.cnf.d/certificates/server-key.pem
ssl_ca = /etc/my.cnf.d/certificates/ca.pem
```

And then restart the server to make the changes persistent.

At this point, you can reconfigure the replicas to use TLS to encrypt replicated data in transit. There are two methods available to do this:

* Executing the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement to set the relevant TLS options.
* Setting TLS client options in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

### Executing CHANGE MASTER

TLS can be enabled on a replication replica by executing the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. In order to do so, there are a number of options that you would need to set. The specific options that you would need to set would depend on whether you want one-way TLS or two-way TLS, and whether you want to verify the server certificate.

#### Enabling Two-Way TLS with CHANGE MASTER

Two-way TLS means that both the client and server provide a private key and an X509 certificate. It is called "two-way" TLS because both the client and server can be authenticated. In this case, the "client" is the replica. To configure two-way TLS, you would need to set the following options:

* You need to set the path to the server's certificate by setting the [MASTER\_SSL\_CERT](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_cert) option.
* You need to set the path to the server's private key by setting the [MASTER\_SSL\_KEY](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_key) option.
* You need to set the path to the certificate authority (CA) chain that can verify the server's certificate by setting either the [MASTER\_SSL\_CA](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_ca) or the [MASTER\_SSL\_CAPATH](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_capath) options.
* If you want [server certificate verification](secure-connections-overview.md#server-certificate-verification), then you also need to set the [MASTER_SSL_VERIFY_SERVER_CERT](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_verify_server_cert) option (enabled by default from [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113)).
* If you want to restrict the server to certain ciphers, then you also need to set the [MASTER\_SSL\_CIPHER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_cipher) option.

If the [replica threads](../../../../ha-and-performance/standard-replication/replication-threads.md#threads-on-the-replica) are currently running, you first need to stop them by executing the [STOP SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) statement. For example:

```sql
STOP SLAVE;
```

Then, execute the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement to configure the replica to use TLS. For example:

```sql
CHANGE MASTER TO
   MASTER_SSL_CERT = '/path/to/client-cert.pem',
   MASTER_SSL_KEY = '/path/to/client-key.pem',
   MASTER_SSL_CA = '/path/to/ca/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
```

At this point, you can start replication by executing the [START SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement. For example:

```sql
START SLAVE;
```

The replica now uses TLS to encrypt data in transit as it replicates it from the primary.

#### Enabling One-Way TLS with CHANGE MASTER

**Enabling One-Way TLS with CHANGE MASTER with Server Certificate Verification**

One-way TLS means that only the server provides a private key and an X509 certificate. When TLS is used without a client certificate, it is called "one-way" TLS, because only the server can be authenticated, so authentication is only possible in one direction. However, encryption is still possible in both directions. [Server certificate verification](secure-connections-overview.md#server-certificate-verification) means that the client verifies that the certificate belongs to the server. In this case, the "client" is the replica. This mode is enabled by default starting from [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113). To configure one-way TLS in earlier versions, you would need to set the following options:

* You need to set the path to the certificate authority (CA) chain that can verify the server's certificate by setting either the [MASTER\_SSL\_CA](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_ca) or the [MASTER\_SSL\_CAPATH](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_capath) options.
* You need to set the [MASTER\_SSL\_VERIFY\_SERVER\_CERT](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_verify_server_cert) option.
* If you want to restrict the server to certain ciphers, then you also need to set the [MASTER\_SSL\_CIPHER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_cipher) option.

If the [replica threads](../../../../ha-and-performance/standard-replication/replication-threads.md#threads-on-the-replica) are currently running, you first need to stop them by executing the [STOP SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) statement. For example:

```sql
STOP SLAVE;
```

Then, execute the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement to configure the replica to use TLS. For example:

```sql
CHANGE MASTER TO
   MASTER_SSL_CA = '/path/to/ca/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
```

At this point, you can start replication by executing the [START SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement. For example:

```sql
START SLAVE;
```

The replica now uses TLS to encrypt data in transit as it replicates it from the primary.

**Enabling One-Way TLS with CHANGE MASTER without Server Certificate Verification**

One-way TLS means that only the server provides a private key and an X509 certificate. When TLS is used without a client certificate, it is called "one-way" TLS, because only the server can be authenticated, so authentication is only possible in one direction. However, encryption is still possible in both directions. In this case, the "client" is the replica. To configure two-way TLS without server certificate verification, you would need to set the following options:

* You need to configure the replica to use TLS by setting the [MASTER\_SSL](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl) option.
* If you want to restrict the server to certain ciphers, then you also need to set the [MASTER\_SSL\_CIPHER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_cipher) option.
* Starting from [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113) you need to disable the [MASTER\_SSL\_VERIFY\_SERVER\_CERT](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl_verify_server_cert) option.

If the [replica threads](../../../../ha-and-performance/standard-replication/replication-threads.md#threads-on-the-replica) are currently running, you first need to stop them by executing the [STOP SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) statement. For example:

```sql
STOP SLAVE;
```

Then, execute the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement to configure the replica to use TLS. For example:

```sql
CHANGE MASTER TO
   MASTER_SSL=1, MASTER_SSL_VERIFY_SERVER_CERT=0;
```

At this point, you can start replication by executing the [START SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement. For example:

```sql
START SLAVE;
```

The replica now uses TLS to encrypt data in transit as it replicates it from the primary.

### Setting TLS Client Options in an Option File

In cases where you don't mind restarting the server or you are setting the server up from scratch for the first time, you may find it more convenient to configure TLS options for replication through an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). This is done the same way as it is for other clients. The specific options that you would need to set would depend on whether you want one-way TLS or two-way TLS, and whether you want to verify the server certificate. See [Securing Connections for Client and Server: Enabling TLS for MariaDB Clients](securing-connections-for-client-and-server.md#enabling-tls-for-mariadb-clients) for more information.\
For example, to enable two-way TLS with [server certificate verification](secure-connections-overview.md#server-certificate-verification), then you could specify the following options in a relevant client [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[client-mariadb]
...
ssl_cert = /etc/my.cnf.d/certificates/client-cert.pem
ssl_key = /etc/my.cnf.d/certificates/client-key.pem
ssl_ca = /etc/my.cnf.d/certificates/ca.pem
ssl-verify-server-cert
```

Before you restart the server, you may also want to set the [--skip-slave-start](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-skip-slave-start) option in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). This option prevents the [replica threads](../../../../ha-and-performance/standard-replication/replication-threads.md#threads-on-the-replica) from restarting automatically when the server starts. Instead, they will have to be restarted manually.\
After these changes have been made, you can restart the server.\
Once the server is back online, set the [MASTER\_SSL](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_ssl) option by executing the [CHANGE MASTER](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. This will enable TLS. For example:

```sql
CHANGE MASTER TO
   MASTER_SSL=1;
```

The certificate and keys will be read from the option file.\
At this point, you can start replication by executing the [START SLAVE](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement.

```sql
START SLAVE;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
