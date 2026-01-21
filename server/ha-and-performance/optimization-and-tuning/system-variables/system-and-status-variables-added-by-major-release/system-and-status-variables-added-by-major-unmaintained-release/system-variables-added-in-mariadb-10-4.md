# System Variables Added in MariaDB 10.4

This is a list of [system variables](../../server-system-variables.md) that have been added in the [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) series. The list does not include variables that are not part of the default release.

| Variable                                                                                                                                                     | Added                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [analyze\_sample\_percentage](../../server-system-variables.md#analyze_sample_percentage)                                                                    | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [default\_password\_lifetime](../../server-system-variables.md#default_password_lifetime)                                                                    | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [disconnect\_on\_expired\_password](../../server-system-variables.md#disconnect_on_expired_password)                                                         | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [gtid\_cleanup\_batch\_size](../../../../standard-replication/gtid.md#gtid_cleanup_batch_size)                                                               | [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes)   |
| [innodb\_encrypt\_temporary\_ables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                           | [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes)   |
| [innodb\_instant\_alter\_column\_allowed](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed) | [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes) |
| [max\_password\_errors](../../server-system-variables.md#max_password_errors)                                                                                | [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)   |
| [optimizer\_trace](../../server-system-variables.md#optimizer_trace)                                                                                         | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [optimizer\_trace\_max\_mem\_size](../../server-system-variables.md#optimizer_trace_max_mem_size)                                                            | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [tcp\_nodelay](../../server-system-variables.md#tcp_nodelay)                                                                                                 | [MariaDB 10.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1040-release-notes)   |
| [tls\_version](../../../../../security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version)                        | [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes)   |
| [wsrep\_certification\_rules](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_certification_rules)            | [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)   |
| [wsrep\_trx\_fragment\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size)               | [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)   |
| [wsrep\_trx\_fragment\_unit](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_unit)               | [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)   |

For system variables that have been removed or deprecated, see [Upgrading from MariaDB 10.3 to MariaDB 10.4](../../../../../server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md).

## See Also

* [Status Variables Added in MariaDB 10.4](status-variables-added-in-mariadb-104.md)
* [System Variables Added in MariaDB 10.5](system-variables-added-in-mariadb-10-5.md)
* [System Variables Added in MariaDB 10.3](system-variables-added-in-mariadb-10-3.md)
* [System Variables Added in MariaDB 10.2](system-variables-added-in-mariadb-102.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
