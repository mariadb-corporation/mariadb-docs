# Encrypting Galera Cluster's GCache

##

## Overview

[MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) and MariaDB Community Server support [data-at-rest encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption), which secures data on the file system. The server and storage engines encrypt data before writes and decrypt it during reads, ensuring that the data is only unencrypted when accessed directly through the server.

In many versions of MariaDB Server, the GCache used by [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) does not support data-at-rest encryption.

However, [MariaDB Enterprise Server 10.4](../../old-releases/10-4/) and later support an enterprise version of Galera 4, which adds support for encrypting the GCache.

In those versions, the GCache supports the following data-at-rest encryption features:

* The GCache can be automatically encrypted.

For more information, see the following resources:

* [Enabling GCache Encryption](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide#enabling-gcache-encryption)
* [Disabling GCache Encryption](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide#disabling-gcache-encryption)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
