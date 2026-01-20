# Securing Communications in Galera Cluster

By default, Galera Cluster replicates data between each node without encrypting it. This is generally acceptable when the cluster nodes runs on the same host or in networks where security is guaranteed through other means. However, in cases where the cluster nodes exist on separate networks or they are in a high-risk network, the lack of encryption does introduce security concerns as a malicious actor could potentially eavesdrop on the traffic or get a complete copy of the data by [triggering an SST](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster).

To mitigate this concern, Galera Cluster allows you to encrypt data in transit as it is replicated between each cluster node using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix `ssl_`, but internally, MariaDB only supports its secure successors.

In order to secure connections between the cluster nodes, you need to ensure that all servers were compiled with TLS support. See [Secure Connections Overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview) to determine how to check whether a server was compiled with TLS support.

For each cluster node, you also need a certificate, private key, and the Certificate Authority (CA) chain to verify the certificate. If you want to use self-signed certificates that are created with OpenSSL, then see [Certificate Creation with OpenSSL](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/certificate-creation-with-openssl) for information on how to create those.

## Securing Galera Cluster Replication Traffic

In order to enable TLS for Galera Cluster's replication traffic, there are a number of [wsrep\_provider\_options](../reference/wsrep-variable-details/wsrep_provider_options.md) that you need to set, such as:

* You need to set the path to the server's certificate by setting the [socket.ssl\_cert](../reference/wsrep-variable-details/wsrep_provider_options.md#socketssl_cert) wsrep\_provider\_option.
* You need to set the path to the server's private key by setting the [socket.ssl\_key](../reference/wsrep-variable-details/wsrep_provider_options.md#socketssl_key) wsrep\_provider\_option.
* You need to set the path to the certificate authority (CA) chain that can verify the server's certificate by setting the [socket.ssl\_ca](../reference/wsrep-variable-details/wsrep_provider_options.md#socketssl_ca) wsrep\_provider\_option.
* If you want to restrict the server to certain ciphers, then you also need to set the [socket.ssl\_cipher](../reference/wsrep-variable-details/wsrep_provider_options.md#socketssl_cipher) wsrep\_provider\_option.

It is also a good idea to set MariaDB Server's regular TLS-related system variables, so that TLS will be enabled for regular client connections as well. See [Securing Connections for Client and Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server) for information on how to do that.

For example, to set these variables for the server, add the system variables to a relevant server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#including-option-files):

```ini
[mariadb]
...
ssl_cert = /etc/my.cnf.d/certificates/server-cert.pem
ssl_key = /etc/my.cnf.d/certificates/server-key.pem
ssl_ca = /etc/my.cnf.d/certificates/ca.pem
wsrep_provider_options="socket.ssl_cert=/etc/my.cnf.d/certificates/server-cert.pem;socket.ssl_key=/etc/my.cnf.d/certificates/server-key.pem;socket.ssl_ca=/etc/my.cnf.d/certificates/ca.pem"
```

And then restart the server to make the changes persistent.

By setting both MariaDB Server's TLS-related system variables and Galera Cluster's TLS-related wsrep\_provider\_options, the server can secure both external client connections and Galera Cluster's replication traffic.

## Securing State Snapshot Transfers

The method that you would use to enable TLS for [State Snapshot Transfers (SSTs)](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) would depend on the value of [wsrep\_sst\_method](../reference/galera-cluster-system-variables.md#wsrep_sst_method).

### mariadb-backup

See [mariadb-backup SST Method: TLS](../galera-management/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method.md#tls) for more information.

### xtrabackup-v2

See [xtrabackup-v2 SST Method](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/obsolete-replication-information/xtradb-option-innodb-release-locks-early): TLS for more information.

### mysqldump

This SST method simply uses the [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) (previously mysqldump) utility, so TLS would be enabled by following the guide at [Securing Connections for Client and Server: Enabling TLS for MariaDB Clients](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server#enabling-tls-for-mariadb-clients)

### rsync

This SST method supports encryption in transit via [stunnel](https://www.stunnel.org/). See [Introduction to State Snapshot Transfers (SSTs): rsync](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md#rsync) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
