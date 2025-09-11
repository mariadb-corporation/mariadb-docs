# Disabling Data-at-Rest Encryption for Standalone Servers

In certain situations, you may need to turn off data-at-rest encryption in a standalone or single-node MariaDB Enterprise Server deployment. For instance, you might have originally enabled encryption using a key management plugin, but later determine that encryption is no longer necessary.

This page explains how to safely disable data-at-rest encryption on a single server. The steps assume that your server already contains encrypted tables or logs, and that your goal is to revert the system to an unencrypted state without losing any data.

{% hint style="info" %}
* This procedure is only intended for **standalone MariaDB Enterprise Server** environments.
* For replication or Galera Cluster setups, additional considerations are required and are not covered here.
* Always back up your data before performing encryption or decryption operations.
{% endhint %}

### Prerequisites

Before you can disable data-at-rest encryption in MariaDB Enterprise Server, ensure the following:

* **MariaDB Enterprise Server with Encryption Enabled**\
  The server must currently be running with data-at-rest encryption enabled.
* **Key Management Access**\
  You must have access to the same key management plugin and configuration that were originally used to encrypt the data.
* **Sufficient Disk Space**\
  Make sure adequate free disk space is available to decrypt and rewrite all affected data files.

### Related Documentation

* [Data-at-Rest Encryption](../)
* [Aria Table Encryption](../aria-encryption/)
* [InnoDB Table Encryption](../innodb-encryption/)
