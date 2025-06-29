# CHANGE MASTER TO

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

## Syntax

```sql
CHANGE MASTER ['connection_name'] TO master_def  [, master_def] ... 
  [FOR CHANNEL 'channel_name']

master_def:
    MASTER_BIND = 'interface_name'
  | MASTER_HOST = 'host_name'
  | MASTER_USER = 'user_name'
  | MASTER_PASSWORD = 'password'
  | MASTER_PORT = port_num
  | MASTER_CONNECT_RETRY = interval
  | MASTER_HEARTBEAT_PERIOD = interval
  | MASTER_LOG_FILE = 'master_log_name'
  | MASTER_LOG_POS = master_log_pos
  | RELAY_LOG_FILE = 'relay_log_name'
  | RELAY_LOG_POS = relay_log_pos
  | MASTER_DELAY = interval
  | MASTER_SSL = {0|1}
  | MASTER_SSL_CA = 'ca_file_name'
  | MASTER_SSL_CAPATH = 'ca_directory_name'
  | MASTER_SSL_CERT = 'cert_file_name'
  | MASTER_SSL_CRL = 'crl_file_name'
  | MASTER_SSL_CRLPATH = 'crl_directory_name'
  | MASTER_SSL_KEY = 'key_file_name'
  | MASTER_SSL_CIPHER = 'cipher_list'
  | MASTER_SSL_VERIFY_SERVER_CERT = {0|1}
  | MASTER_USE_GTID = {current_pos|slave_pos|no}
  | MASTER_DEMOTE_TO_SLAVE = bool
  | IGNORE_SERVER_IDS = (server_id_list)
  | DO_DOMAIN_IDS = ([N,..])
  | IGNORE_DOMAIN_IDS = ([N,..])
  | MASTER_RETRY_COUNT = long
```

## Description

`CHANGE MASTER` is used on a replica to set up or change [replication](../../../../ha-and-performance/standard-replication/) settings for connecting to the primary.

{% tabs %}
{% tab title="Current" %}
The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to using the channel\_name directly after `CHANGE MASTER`.
{% endtab %}

{% tab title="< 10.7.0" %}
`FOR CHANNEL` is not available.
{% endtab %}
{% endtabs %}

## Multi-Source Replication

If you are using [multi-source replication](../../../../ha-and-performance/standard-replication/multi-source-replication.md), then you need to specify a connection name when you execute `CHANGE MASTER`. There are two ways to do this:

* Setting the [default\_master\_connection](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable prior to executing `CHANGE MASTER`.
* Setting the `connection_name` parameter when executing `CHANGE MASTER`.

### default\_master\_connection

```sql
SET default_master_connection = 'gandalf';
STOP SLAVE;
CHANGE MASTER TO 
   MASTER_PASSWORD='new3cret';
START SLAVE;
```

### connection\_name

```sql
STOP SLAVE 'gandalf';
CHANGE MASTER 'gandalf' TO 
   MASTER_PASSWORD='new3cret';
START SLAVE 'gandalf';
```

## Options

### Connection Options

#### MASTER\_USER

The `MASTER_USER` option for `CHANGE MASTER` defines the user account that the [replica](../../../../ha-and-performance/standard-replication/setting-up-replication.md) will use to connect to the [primary](../../../../ha-and-performance/standard-replication/setting-up-replication.md).

{% tabs %}
{% tab title="Current" %}
This user account will need the [REPLICATION REPLICA](../../account-management-sql-statements/grant.md#replication-replica) privilege on the primary.
{% endtab %}

{% tab title="< 10.5.1" %}
This user account will need the [REPLICATION SLAVE](../../account-management-sql-statements/grant.md#replication-slave) privilege on the primary.
{% endtab %}
{% endtabs %}

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_USER='repl',
   MASTER_PASSWORD='new3cret';
START SLAVE;
```

{% tabs %}
{% tab title="Current" %}
The maximum length of the `MASTER_USER` string is 128 characters.
{% endtab %}

{% tab title="< 10.6" %}
The maximum length of the `MASTER_USER` string is 96 characters.
{% endtab %}
{% endtabs %}

#### MASTER\_PASSWORD

The `MASTER_PASSWORD` option for `CHANGE MASTER` defines the password that the [replica](../../../../ha-and-performance/standard-replication/setting-up-replication.md) will use to connect to the [primary](../../../../ha-and-performance/standard-replication/setting-up-replication.md) as the user account defined by the [MASTER\_USER](change-master-to.md#master_user) option.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   MASTER_PASSWORD='new3cret';
START SLAVE;
```

The maximum length of the `MASTER_PASSWORD` string is 32 characters. The effective maximum length of the string depends on how many bytes are used per character and can be up to 96 characters.

{% hint style="warning" %}
Due to [MDEV-29994](https://jira.mariadb.org/browse/MDEV-29994), the password can be silently truncated to 41 characters when MariaDB is restarted. For this reason it is recommended to use a password that is shorter than this.
{% endhint %}

#### MASTER\_HOST

The `MASTER_HOST` option for `CHANGE MASTER` defines the hostname or IP address of the [primary](../../../../ha-and-performance/standard-replication/setting-up-replication.md).

{% tabs %}
{% tab title="Current" %}
If you set the value of the `MASTER_HOST` option to the empty string, then that is not the same as not setting the option's value at all. If you set the value of the `MASTER_HOST` option to the empty string, then the `CHANGE MASTER` command will fail with an error.
{% endtab %}

{% tab title="< 5.4" %}
If you set the value of the `MASTER_HOST` option to the empty string, then that is not the same as not setting the option's value at all. If you set the value of the `MASTER_HOST` option to the empty string, then the `CHANGE MASTER` command will fail with an error. In MariaDB 5.3 and before, if you set the value of the `MASTER_HOST` option to the empty string, then the `CHANGE MASTER` command would succeed, but the subsequent [START SLAVE](start-replica.md) command would fail.
{% endtab %}
{% endtabs %}

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_HOST='dbserver1.example.com',
   MASTER_USER='repl',
   MASTER_PASSWORD='new3cret',
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

{% hint style="info" %}
If you set the value of the `MASTER_HOST` option in a `CHANGE MASTER` command, then the replica assumes that the primary is different from before, even if you set the value of this option to the same value it had previously. In this scenario, the replica will consider the old values for the primary's [binarylog](../../../../server-management/server-monitoring-logs/binary-log/) file name and position to be invalid for the new primary. As a side effect, if you do not explicitly set the values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options in the statement, then the statement will be implicitly appended with `MASTER_LOG_FILE=''` and `MASTER_LOG_POS=4`. However, if you enable [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement, then these values will effectively be ignored anyway.
{% endhint %}

{% hint style="info" %}
Replicas cannot connect to primaries using Unix socket files or Windows named pipes. The replica must connect to the primary using TCP/IP.
{% endhint %}

{% tabs %}
{% tab title="Current" %}
The maximum length of the `MASTER_HOST` string is 255 characters.
{% endtab %}

{% tab title="< 10.6" %}
The maximum length of the `MASTER_HOST` string is 60 characters.
{% endtab %}
{% endtabs %}

#### MASTER\_PORT

The `MASTER_PORT` option for `CHANGE MASTER` defines the TCP/IP port of the [primary](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/administrative-sql-statements/replication-statements/broken-reference/README.md).

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_HOST='dbserver1.example.com',
   MASTER_PORT=3307,
   MASTER_USER='repl',
   MASTER_PASSWORD='new3cret',
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

{% hint style="info" %}
If you set the value of the `MASTER_PORT` option in a `CHANGE MASTER` command, then the replica assumes that the primary is different from before, even if you set the value of this option to the same value it had previously. In this scenario, the replica will consider the old values for the primary's [binarylog](../../../../server-management/server-monitoring-logs/binary-log/) file name and position to be invalid for the new primary. As a side effect, if you do not explicitly set the values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options in the statement, then the statement will be implicitly appended with `MASTER_LOG_FILE=''` and `MASTER_LOG_POS=4`. However, if you enable [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement, then these values will effectively be ignored anyway.
{% endhint %}

{% hint style="info" %}
Replicas cannot connect to primaries using Unix socket files or Windows named pipes. The replica must connect to the primary using TCP/IP.
{% endhint %}

#### MASTER\_CONNECT\_RETRY

The `MASTER_CONNECT_RETRY` option for `CHANGE MASTER` defines how many seconds that the replica will wait between connection retries. The default is `60`.

```sql
STOP SLAVE;
CHANGE MASTER TO 
   MASTER_CONNECT_RETRY=20;
START SLAVE;
```

#### MASTER\_RETRY\_COUNT

{% tabs %}
{% tab title="Current" %}
The `MASTER_RETRY_COUNT` option limits the number of connection attempts (i.e., `Connects_Tried` in [SHOW REPLICA STATUS][]). For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
  MASTER_RETRY_COUNT=1; # attempt only once; do not retry if it fails
START SLAVE;
```

Setting this option resets the `Connects_Tried` statistic in [SHOW REPLICA STATUS][] to 0.

The default is the [`--master-retry-count`][] option, which be set either on the command-line or in a server [option group][] in an [option file][] prior to starting up the server. For example:

[SHOW REPLICA STATUS]: ../show/show-replica-status.md
{% endtab %}

{% tabs %}
{% tab title="< 12.0" %}

The `MASTER_RETRY_COUNT` option for `CHANGE MASTER` is only supported by MariaDB 12.0.1 and later and by MySQL. Please use the [`--master-retry-count`][] option instead, which be set either on the command-line or in a server [option group][] in an [option file][] prior to starting up the server. For example:

{% endtab %}
{% endtabs %}

```ini
[mariadb]
...
master_retry_count=4294967295
```

[`--master-retry-count`]: ../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#master-retry-count
[option group]: ../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups
[option file]: ../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md

#### MASTER\_BIND

{% hint style="warning" %}
The `MASTER_BIND` option for `CHANGE MASTER` is only supported by MySQL 5.6.2 and later and by MySQL NDB Cluster 7.3.1 and later. This option is not supported by MariaDB. See [MDEV-19248](https://jira.mariadb.org/browse/MDEV-19248) for more information.
{% endhint %}

The `MASTER_BIND` option for `CHANGE MASTER` can be used on replicas that have multiple network interfaces to choose which network interface the replica will use to connect to the primary.

#### MASTER\_HEARTBEAT\_PERIOD

The `MASTER_HEARTBEAT_PERIOD` option for `CHANGE MASTER` can be used to set the interval in seconds between replication heartbeats. Whenever the primary's [binary log](../../../../server-management/server-monitoring-logs/binary-log/) is updated with an event, the waiting period for the next heartbeat is reset.

This option's _interval_ argument has the following characteristics:

* It is a decimal value with a range of `0` to `4294967` seconds.
* It has a resolution of hundredths of a second.
* Its smallest valid non-zero value is `0.001`.
* Its default value is the value of the [slave\_net\_timeout](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable divided by 2.
* If it's set to `0`, then heartbeats are disabled.

Heartbeats are sent by the primary only if there are no unsent events in the binary log file for a period longer than the interval.

If the [RESET SLAVE](reset-replica.md) statement is executed, then the heartbeat interval is reset to the default.

{% hint style="info" %}
If the [slave\_net\_timeout](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable is set to a value that is lower than the current heartbeat interval, then a warning will be issued.
{% endhint %}

### TLS Options

The TLS options are used for providing information about [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). The options can be set even on replicas that are compiled without TLS support. The TLS options are saved to either the default `master.info` file or the file that is configured by the [master\_info\_file](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option, but these TLS options are ignored unless the replica supports TLS.

See [Replication with Secure Connections](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/replication-with-secure-connections.md) for more information.

#### MASTER\_SSL

The `MASTER_SSL` option for `CHANGE MASTER` tells the replica whether to force [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) for the connection. The valid values are `0` or `1`. Required to be set to `1` for the other `MASTER_SSL*` options to have any effect.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL=1;
START SLAVE;
```

#### MASTER\_SSL\_CA

The `MASTER_SSL_CA` option for `CHANGE MASTER` defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Certificate Authorities (CAs)](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information.

The maximum length of `MASTER_SSL_CA` string is 511 characters.

#### MASTER\_SSL\_CAPATH

The `MASTER_SSL_CAPATH` option for `CHANGE MASTER` defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CAPATH='/etc/my.cnf.d/certificates/ca/',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Certificate Authorities (CAs)](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information.

The maximum length of `MASTER_SSL_CA_PATH` string is 511 characters.

#### MASTER\_SSL\_CERT

The `MASTER_SSL_CERT` option for `CHANGE MASTER` defines a path to the X509 certificate file to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

The maximum length of `MASTER_SSL_CERT` string is 511 characters.

#### MASTER\_SSL\_CRL

The `MASTER_SSL_CRL` option for `CHANGE MASTER` defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

This option is only supported if the server was built with OpenSSL. If the server was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1,
   MASTER_SSL_CRL='/etc/my.cnf.d/certificates/crl.pem';
START SLAVE;
```

See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.

The maximum length of `MASTER_SSL_CRL` string is 511 characters.

#### MASTER\_SSL\_CRLPATH

The `MASTER_SSL_CRLPATH` option for `CHANGE MASTER` defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this variable needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

This option is only supported if the server was built with OpenSSL. If the server was built with yaSSL, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1,
   MASTER_SSL_CRLPATH='/etc/my.cnf.d/certificates/crl/';
START SLAVE;
```

See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information.

The maximum length of `MASTER_SSL_CRL_PATH` string is 511 characters.

#### MASTER\_SSL\_KEY

The `MASTER_SSL_KEY` option for `CHANGE MASTER` defines a path to a private key file to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

The maximum length of `MASTER_SSL_KEY` string is 511 characters.

#### MASTER\_SSL\_CIPHER

The `MASTER_SSL_CIPHER` option for `CHANGE MASTER` defines the list of permitted ciphers or cipher suites to use for [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). Besides cipher names, if MariaDB was compiled with OpenSSL, this option could be set to "SSLv3" or "TLSv1.2" to allow all SSLv3 or all TLSv1.2 ciphers. Note that the TLSv1.3 ciphers cannot be excluded when using OpenSSL, even by using this option. See [Using TLSv1.3](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/using-tlsv13.md) for details.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1,
   MASTER_SSL_CIPHER='TLSv1.2';
START SLAVE;
```

The maximum length of `MASTER_SSL_CIPHER` string is 511 characters.

#### MASTER\_SSL\_VERIFY\_SERVER\_CERT

{% tabs %}
{% tab title="Current" %}
The `MASTER_SSL_VERIFY_SERVER_CERT` option for `CHANGE MASTER` enables [server certificate verification](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is enabled by default.
{% endtab %}

{% tab title="< 11.4" %}
The `MASTER_SSL_VERIFY_SERVER_CERT` option for `CHANGE MASTER` enables [server certificate verification](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.
{% endtab %}
{% endtabs %}

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_SSL_CERT='/etc/my.cnf.d/certificates/server-cert.pem',
   MASTER_SSL_KEY='/etc/my.cnf.d/certificates/server-key.pem',
   MASTER_SSL_CA='/etc/my.cnf.d/certificates/ca.pem',
   MASTER_SSL_VERIFY_SERVER_CERT=1;
START SLAVE;
```

See [Secure Connections Overview: Server Certificate Verification](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) for more information.

### Binary Log Options

These options are related to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position on the primary.

#### MASTER\_LOG\_FILE

The `MASTER_LOG_FILE` option for `CHANGE MASTER` can be used along with `MASTER_LOG_POS` to specify the coordinates at which the [replica's I/O thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-io-thread) should begin reading from the primary's [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) the next time the thread starts.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_LOG_FILE='master2-bin.001',
   MASTER_LOG_POS=4;
START SLAVE;
```

{% hint style="info" %}
The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options cannot be specified if the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options were also specified.
{% endhint %}

{% hint style="info" %}
The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options are effectively ignored if you enable [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement.
{% endhint %}

#### MASTER\_LOG\_POS

The `MASTER_LOG_POS` option for `CHANGE MASTER` can be used along with `MASTER_LOG_FILE` to specify the coordinates at which the [replica's I/O thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-io-thread) should begin reading from the primary's [binary logs](../../../../server-management/server-monitoring-logs/binary-log/) the next time the thread starts.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_LOG_FILE='master2-bin.001',
   MASTER_LOG_POS=4;
START SLAVE;
```

{% hint style="info" %}
The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options cannot be specified if the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options were also specified.
{% endhint %}

{% hint style="info" %}
The [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options are effectively ignored if you enable [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode for replication by setting the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option to some value other than `no` in the statement.
{% endhint %}

### Relay Log Options

These options are related to the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position on the replica.

#### RELAY\_LOG\_FILE

The `RELAY_LOG_FILE` option for `CHANGE MASTER` can be used along with the [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) option to specify the coordinates at which the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) should begin reading from the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) the next time the thread starts.

The `CHANGE MASTER` statement usually deletes all [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files. However, if the `RELAY_LOG_FILE` and/or `RELAY_LOG_POS` options are specified, then existing [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files are kept.

When you want to change the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position, you only need to stop the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread). The [replica's I/O thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-io-thread) can continue running. The [STOP SLAVE](stop-replica.md) and [START SLAVE](start-replica.md) statements support the `SQL_THREAD` option for this scenario. For example:

```sql
STOP SLAVE SQL_THREAD;
CHANGE MASTER TO
   RELAY_LOG_FILE='slave-relay-bin.006',
   RELAY_LOG_POS=4025;
START SLAVE SQL_THREAD;
```

When the value of this option is changed, the metadata about the [replica's SQL thread's](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) position in the [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) will also be changed in the `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.

{% hint style="info" %}
The [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options cannot be specified if the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options were also specified.
{% endhint %}

#### RELAY\_LOG\_POS

The `RELAY_LOG_POS` option for `CHANGE MASTER` can be used along with the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) option to specify the coordinates at which the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) should begin reading from the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) the next time the thread starts.

The `CHANGE MASTER` statement usually deletes all [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files. However, if the `RELAY_LOG_FILE` and/or `RELAY_LOG_POS` options are specified, then existing [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files are kept.

When you want to change the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position, you only need to stop the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread). The [replica's I/O thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-io-thread) can continue running. The [STOP SLAVE](stop-replica.md) and [START SLAVE](start-replica.md) statements support the `SQL_THREAD` option for this scenario. For example:

```sql
STOP SLAVE SQL_THREAD;
CHANGE MASTER TO
   RELAY_LOG_FILE='slave-relay-bin.006',
   RELAY_LOG_POS=4025;
START SLAVE SQL_THREAD;
```

When the value of this option is changed, the metadata about the [replica's SQL thread's](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) position in the [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) will also be changed in the `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.

{% hint style="info" %}
The [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options cannot be specified if the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options were also specified.
{% endhint %}

### GTID Options

#### MASTER\_USE\_GTID

{% tabs %}
{% tab title="Current" %}
The `MASTER_USE_GTID` option for `CHANGE MASTER` can be used to configure the replica to use the [global transaction ID (GTID)](../../../../ha-and-performance/standard-replication/gtid.md) when connecting to a primary. The possible values are:

* `current_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_current\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_current_pos) as the position to start downloading transactions from the primary. Using to transition to primary can break the replication state if the replica executes local transactions due to actively updating gtid\_current\_pos with gtid\_binlog\_pos and gtid\_slave\_pos. Use the new, safe, [MASTER\_DEMOTE\_TO\_SLAVE=](change-master-to.md#master_demote_to_slave) option instead.
* `replica_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) as the position to start downloading transactions from the primary.
* `no` - Don't replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode.
{% endtab %}

{% tab title="< 10.5.1" %}
The `MASTER_USE_GTID` option for `CHANGE MASTER` can be used to configure the replica to use the [global transaction ID (GTID)](../../../../ha-and-performance/standard-replication/gtid.md) when connecting to a primary. The possible values are:

* `current_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_current\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_current_pos) as the position to start downloading transactions from the primary. Using to transition to primary can break the replication state if the replica executes local transactions due to actively updating gtid\_current\_pos with gtid\_binlog\_pos and gtid\_slave\_pos. Use the new, safe, [MASTER\_DEMOTE\_TO\_SLAVE=](change-master-to.md#master_demote_to_slave) option instead.
* `slave_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) as the position to start downloading transactions from the primary.
* `no` - Don't replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode.
{% endtab %}
{% endtabs %}

The `MASTER_USE_GTID` option for `CHANGE MASTER` can be used to configure the replica to use the [global transaction ID (GTID)](../../../../ha-and-performance/standard-replication/gtid.md) when connecting to a primary. The possible values are:

* `current_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_current\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_current_pos) as the position to start downloading transactions from the primary. Using to transition to primary can break the replication state if the replica executes local transactions due to actively updating gtid\_current\_pos with gtid\_binlog\_pos and gtid\_slave\_pos. Use the new, safe, [MASTER\_DEMOTE\_TO\_SLAVE=](change-master-to.md#master_demote_to_slave) option instead.
* `slave_pos` - Replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode and use [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) as the position to start downloading transactions from the primary. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes), `replica_pos` is an alias for `slave_pos`.
* `no` - Don't replicate in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_USE_GTID = current_pos;
START SLAVE;
```

Or:

```sql
STOP SLAVE;
SET GLOBAL gtid_slave_pos='0-1-153';
CHANGE MASTER TO
   MASTER_USE_GTID = slave_pos;
START SLAVE;
```

#### MASTER\_DEMOTE\_TO\_SLAVE

{% tabs %}
{% tab title="Current" %}
Used to transition a primary to become a replica. Replaces the old [MASTER\_USE\_GTID=current\_pos](change-master-to.md#master_use_gtid) with a safe alternative by forcing users to set `Using_Gtid=Slave_Pos` and merging `gtid_binlog_pos` into `gtid_slave_pos` once at `CHANGE MASTER TO` time. If `gtid_slave_pos` is morerecent than `gtid_binlog_pos` (as in the case of chain replication), the replication state should be preserved.

For example:

```sql
STOP SLAVE;
CHANGE MASTER TO
   MASTER_DEMOTE_TO_SLAVE = 1;
START SLAVE;
```
{% endtab %}

{% tab title="< 10.10" %}
`MASTER_DEMOTE_TO_SLAVE` is not available.
{% endtab %}
{% endtabs %}

### Replication Filter Options

Also see [Replication filters](../../../../ha-and-performance/standard-replication/replication-filters.md).

#### IGNORE\_SERVER\_IDS

The `IGNORE_SERVER_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/administrative-sql-statements/replication-statements/broken-reference/README.md) to ignore [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events that originated from certain servers. Filtered [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events will not get logged to the replica’s [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [server\_id](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id) values. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   IGNORE_SERVER_IDS = (3,5);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   IGNORE_SERVER_IDS = ();
START SLAVE;
```

#### DO\_DOMAIN\_IDS

The `DO_DOMAIN_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/administrative-sql-statements/replication-statements/broken-reference/README.md) to only apply [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events if the transaction's [GTID](../../../../ha-and-performance/standard-replication/gtid.md) is in a specific [gtid\_domain\_id](../../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id) value. Filtered [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events will not get logged to the replica’s [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [gtid\_domain\_id](../../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id) values. Duplicate values are automatically ignored. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   DO_DOMAIN_IDS = (1,2);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   DO_DOMAIN_IDS = ();
START SLAVE;
```

{% hint style="info" %}
The [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option cannot both be set to non-empty values at the same time. If you want to set the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option, and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option was previously set, then you need to clear the value of the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option. For example:
{% endhint %}

```sql
STOP SLAVE;
CHANGE MASTER TO 
   IGNORE_DOMAIN_IDS = (), 
   DO_DOMAIN_IDS = (1,2);
START SLAVE;
```

{% hint style="info" %}
The `DO_DOMAIN_IDS` option can only be specified if the replica is replicating in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode. Therefore, the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option must also be set to some value other than `no` in order to use this option.
{% endhint %}

#### IGNORE\_DOMAIN\_IDS

The `IGNORE_DOMAIN_IDS` option for `CHANGE MASTER` can be used to configure a [replica](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/administrative-sql-statements/replication-statements/broken-reference/README.md) to ignore [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events if the transaction's [GTID](../../../../ha-and-performance/standard-replication/gtid.md) is in a specific [gtid\_domain\_id](../../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id) value. Filtered [binary log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/binary_log/README.md) events will not get logged to the replica’s [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

The option's value can be specified by providing a comma-separated list of [gtid\_domain\_id](../../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id) values. Duplicate values are automatically ignored. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   IGNORE_DOMAIN_IDS = (1,2);
START SLAVE;
```

If you would like to clear a previously set list, then you can set the value to an empty list. For example:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   IGNORE_DOMAIN_IDS = ();
START SLAVE;
```

{% hint style="info" %}
The [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option and the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option cannot both be set to non-empty values at the same time. If you want to set the [IGNORE\_DOMAIN\_IDS](change-master-to.md#ignore_domain_ids) option, and the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option was previously set, then you need to clear the value of the [DO\_DOMAIN\_IDS](change-master-to.md#do_domain_ids) option. For example:
{% endhint %}

```sql
STOP SLAVE;
CHANGE MASTER TO 
   DO_DOMAIN_IDS = (), 
   IGNORE_DOMAIN_IDS = (1,2);
START SLAVE;
```

{% hint style="info" %}
The `IGNORE_DOMAIN_IDS` option can only be specified if the replica is replicating in [GTID](../../../../ha-and-performance/standard-replication/gtid.md) mode. Therefore, the [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) option must also be set to some value other than `no` in order to use this option.
{% endhint %}

### Delayed Replication Options

#### MASTER\_DELAY

The `MASTER_DELAY` option for `CHANGE MASTER` can be used to enable [delayed replication](../../../../ha-and-performance/standard-replication/delayed-replication.md). This option specifies the time in seconds (at least) that a replica should lag behind the primary up to a maximum value of 2147483647, or about 68 years. Before executing an event, the replica will first wait, if necessary, until the given time has passed since the event was created on the primary. The result is that the replica will reflect the state of the primary some time back in the past. The default is zero, no delay.

```sql
STOP SLAVE;
CHANGE MASTER TO 
   MASTER_DELAY=3600;
START SLAVE;
```

## Changing Option Values

If you don't specify a given option when executing the `CHANGE MASTER` statement, then the option keeps its old value in most cases. Most of the time, there is no need to specify the options that do not need to change. For example, if the password for the user account that the replica uses to connect to its primary has changed, but no other options need to change, then you can just change the [MASTER\_PASSWORD](change-master-to.md#master_password) option by executing the following commands:

```sql
STOP SLAVE;
CHANGE MASTER TO 
   MASTER_PASSWORD='new3cret';
START SLAVE;
```

There are some cases where options are implicitly reset, such as when the [MASTER\_HOST](change-master-to.md#master_host) and [MASTER\_PORT](change-master-to.md#master_port) options are changed.

## Option Persistence

The values of the [MASTER\_LOG\_FILE](change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](change-master-to.md#master_log_pos) options (i.e. the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position on the primary) and most other options are written to either the default `master.info` file or the file that is configured by the [master\_info\_file](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option. The [replica's I/O thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-io-thread) keeps this [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position updated as it downloads events only when [MASTER\_USE\_GTID](change-master-to.md#master_use_gtid) optionis set to `NO`. Otherwise the file is not updated on a per event basis.

The [master\_info\_file](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option can be set either on the command-line or in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
...
master_info_file=/mariadb/myserver1-master.info
```

The values of the [RELAY\_LOG\_FILE](change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](change-master-to.md#relay_log_pos) options (i.e. the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position) are written to either the default `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable. The [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) keeps this [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) position updated as it applies events.

The [relay\_log\_info\_file](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable can be set either on the command-line or in a server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
...
relay_log_info_file=/mariadb/myserver1-relay-log.info
```

## GTID Persistence

If the replica is replicating [binary log](../../../../server-management/server-monitoring-logs/binary-log/) events that contain [GTIDs](../../../../ha-and-performance/standard-replication/gtid.md), then the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) will write every GTID that it applies to the [mysql.gtid\_slave\_pos](../system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This GTID can be inspected and modified through the [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) system variable.

If the replica has the [log\_slave\_updates](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates) system variable enabled and if the replica has the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) enabled, then every write by the [replica's SQL thread](../../../../ha-and-performance/standard-replication/replication-threads.md#slave-sql-thread) will also go into the replica's [binary log](../../../../server-management/server-monitoring-logs/binary-log/). This means that [GTIDs](../../../../ha-and-performance/standard-replication/gtid.md) of replicated transactions would be reflected in the value of the [gtid\_binlog\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_binlog_pos) system variable.

## Creating a Replica from a Backup

The `CHANGE MASTER` statement is useful for setting up a replica when you have a backup of the primary and you also have the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position or [GTID](../../../../ha-and-performance/standard-replication/gtid.md) position corresponding to the backup.

After restoring the backup on the replica, you could execute something like this to use the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) position:

```sql
CHANGE MASTER TO
   MASTER_LOG_FILE='master2-bin.001',
   MASTER_LOG_POS=4;
START SLAVE;
```

Or you could execute something like this to use the [GTID](../../../../ha-and-performance/standard-replication/gtid.md) position:

```sql
SET GLOBAL gtid_slave_pos='0-1-153';
CHANGE MASTER TO
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

See [Setting up a Replication Slave with mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/setting-up-a-replica-with-mariadb-backup.md) for more information on how to do this with [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/).

## Example

The following example changes the primary and primary's binary log coordinates.This is used when you want to set up the replica to replicate the primary:

```sql
CHANGE MASTER TO
   MASTER_HOST='master2.mycompany.com',
   MASTER_USER='replication',
   MASTER_PASSWORD='bigs3cret',
   MASTER_PORT=3306,
   MASTER_LOG_FILE='master2-bin.001',
   MASTER_LOG_POS=4,
   MASTER_CONNECT_RETRY=10;
START SLAVE;
```

## See Also

* [Setting up replication](../../../../ha-and-performance/standard-replication/setting-up-replication.md)
* [START SLAVE](start-replica.md)
* [Multi-source replication](../../../../ha-and-performance/standard-replication/multi-source-replication.md)
* [RESET SLAVE](reset-replica.md). Removes a connection created with `CHANGE MASTER TO`.
* [Global Transaction ID](../../../../ha-and-performance/standard-replication/gtid.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
