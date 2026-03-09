# wsrep\_sst\_common

#### `wsrep_sst_common` Variables

The `wsrep_sst_common` script provides shared functionality used by various State Snapshot Transfer (SST) methods in Galera Cluster. It centralizes the handling of common configurations such as authentication credentials, `SSL/TLS` encryption parameters, and other security-related settings. This ensures consistent and secure communication between cluster nodes during the SST process.

The `wsrep_sst_common` script parses the following options:

***

* `wsrep-sst-auth` (WSREP\_SST\_OPT\_AUTH)
  * Description: Defines the authentication credentials used by the State Snapshot Transfer (SST) process, typically formatted as `user:password`. These credentials are essential for authenticating the SST user on the donor node, ensuring that only authorized joiner nodes can initiate and receive data during the SST operation. Proper configuration of this variable is critical to maintain the security and integrity of the replication process between Galera cluster nodes.

***

* `tca` (tcert)
  * Description: Specifies the Certificate Authority (CA) certificate file used for SSL/TLS encryption during State Snapshot Transfers (SSTs). When encryption is enabled, this certificate allows the joining node (client) to authenticate the identity of the donor node, ensuring secure and trusted communication between them.

***

* `tcapath` (tcap)
  * Description: Specifies the path to a directory that contains a collection of trusted Certificate Authority (CA) certificates. Instead of providing a single CA certificate file, this option allows the use of multiple CA certificates stored in separate files within the specified directory. It is useful in environments where trust needs to be established with multiple certificate authorities.

***

* `tcert` (tpem)
  * Description: This variable stores the path to the TLS/SSL certificate file for the specific node. The certificate, typically in PEM format, is used by the node to authenticate itself to other nodes during secure SST operations. It is derived from the `tcert` option in the `[sst]` section.

***

* `tkey` (tkey)
  * Description: Represents the private key file that corresponds to the public key certificate specified by `tpem`. This private key is essential for decrypting data and establishing a secure connection during State Snapshot Transfer (SST). It enables the receiving node to authenticate encrypted information and participate in secure replication within the cluster.

### Example

#### Set in Configuration File

To configure common SST options, add them to the `[sst]` group in your configuration file:

{% code overflow="wrap" %}
```ini
[sst] 
wsrep-sst-auth=sstuser:s3cretPass 
tca=/etc/my.cnf.d/certificates/ca-cert.pem 
tcert=/etc/my.cnf.d/certificates/server-cert.pem 
tkey=/etc/my.cnf.d/certificates/server-key.pem
```
{% endcode %}
