---
description: >-
  This table displays the configuration parameters used by the replica to
  connect to the primary server, such as host, port, and user credentials.
---

# Performance Schema replication\_connection\_configuration Table

{% hint style="info" %}
The `replication_connection_configuration` table is available from MariaDB 10.6.0.
{% endhint %}

The [Performance Schema](../) replication\_connection\_configuration table displays replica's configuration settings used for connecting to the primary.

It contains the following fields.

| Column                           | Type                                     | Null | Description                                                                                                                                     |
| -------------------------------- | ---------------------------------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| CHANNEL\_NAME                    | varchar(256)                             | NO   | The replication channel used.                                                                                                                   |
| HOST                             | char(60)                                 | NO   | The host name of the source that the replica is connected to.                                                                                   |
| PORT                             | int(11)                                  | NO   | The port used to connect to the source.                                                                                                         |
| USER                             | char(32)                                 | NO   | The user name of the replication user account used to connect to the source.                                                                    |
| USING\_GTID                      | enum('NO', 'CURRENT\_POS', 'SLAVE\_POS') | NO   | Whether replication is using GTIDs or not.                                                                                                      |
| SSL\_ALLOWED                     | enum('YES', 'NO', 'IGNORED')             | NO   | Whether SSL is allowed for the replica connection.                                                                                              |
| SSL\_CA\_FILE                    | varchar(512)                             | NO   | Path to the file that contains one or more certificates for trusted Certificate Authorities (CA) to use for TLS.                                |
| SSL\_CA\_PATH                    | varchar(512)                             | NO   | Path to a directory that contains one or more PEM files that contain X509 certificates for a trusted Certificate Authority (CA) to use for TLS. |
| SSL\_CERTIFICATE                 | varchar(512)                             | NO   | Path to the certificate used to authenticate the master.                                                                                        |
| SSL\_CIPHER                      | varchar(512)                             | NO   | Which cipher is used for encription.                                                                                                            |
| SSL\_KEY                         | varchar(512)                             | NO   | Path to the private key used for TLS.                                                                                                           |
| SSL\_VERIFY\_SERVER\_CERTIFICATE | enum('YES','NO')                         | NO   | Whether the server certificate is verified as part of the SSL connection.                                                                       |
| SSL\_CRL\_FILE                   | varchar(255)                             | NO   | Path to the PEM file containing one or more revoked X.509 certificates.                                                                         |
| SSL\_CRL\_PATH                   | varchar(255)                             | NO   | PATH to a folder containing PEM files containing one or more revoked X.509 certificates.                                                        |
| CONNECTION\_RETRY\_INTERVAL      | int(11)                                  | NO   | The number of seconds between connect retries.                                                                                                  |
| CONNECTION\_RETRY\_COUNT         | bigint(20) unsigned                      | NO   | The number of times the replica can attempt to reconnect to the source in the event of a lost connection.                                       |
| HEARTBEAT\_INTERVAL              | double(10,3) unsigned                    | NO   | Number of seconds after which a heartbeat will be sent.                                                                                         |
| IGNORE\_SERVER\_IDS              | longtext                                 | NO   | Binary log events from servers (ids) to ignore.                                                                                                 |
| REPL\_DO\_DOMAIN\_IDS            | longtext                                 | NO   | Only apply binary logs from these domain ids.                                                                                                   |
| REPL\_IGNORE\_DOMAIN\_IDS        | longtext                                 | NO   | Binary log events from domains to ignore.                                                                                                       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
