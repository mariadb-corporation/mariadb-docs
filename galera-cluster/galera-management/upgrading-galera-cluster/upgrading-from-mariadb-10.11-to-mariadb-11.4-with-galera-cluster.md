---
description: >-
  Rolling upgrade procedure for moving a Galera Cluster from MariaDB 10.11 to
  MariaDB 11.4, covering pre-upgrade checks, repository changes, drain steps,
  and per-node restart workflow.
---

# Upgrading from MariaDB 10.11 to MariaDB 11.4 with Galera Cluster

[Galera Cluster](../../) ships with the MariaDB Server. Upgrading a Galera Cluster node is very similar to upgrading a server from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011) to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114). For more information on that process as well as incompatibilities between versions, see the [Upgrade Guide](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths).&#x20;

## Performing a Rolling Upgrade

The following steps can be used to perform a rolling upgrade from MariaDB 10.11 to MariaDB 11.4 when using Galera Cluster. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational. There is no downtime from the application's perspective\[cite: 5, 6, 7, 8].&#x20;

First, before you get started:&#x20;

1. First, take a look at [Upgrading from MariaDB 10.11 to MariaDB 11.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-11-to-mariadb-11-4) to see what has changed between the major versions.&#x20;
2. Check whether any system variables or options have been changed or removed. For example, the `old_alter_table` variable has been completely removed in MariaDB 11.x. Make sure that your server's configuration is compatible with the new MariaDB version before upgrading&#x20;
3. Check whether replication has changed in the new MariaDB version in any way that could cause issues while the cluster contains upgraded and non-upgraded nodes.&#x20;
4. Check whether any new features have been added to the new MariaDB version. If a new feature in the new MariaDB version cannot be replicated to the old MariaDB version, then do not use that feature until all cluster nodes have been upgraded to the new MariaDB version.&#x20;
5. Next, make sure that the Galera version numbers are compatible.&#x20;
6. If you are upgrading from standard releases of [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011) to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114), note your specific maintenance version numbers. Both MariaDB 10.11 and 11.4 initially shipped with Galera 3. However, Galera 4 (wsrep API 26) was introduced in maintenance releases starting with [MariaDB 10.11.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.11) and [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.5). For the purposes of a rolling upgrade, ensure your versions align across these ecosystem baselines.&#x20;
7. See [What is MariaDB Galera Cluster](../../readme/mariadb-galera-cluster-guide.md)?: Galera wsrep provider Versions for information on which MariaDB releases use which Galera wsrep provider versions.&#x20;
8. You want to have a large enough gcache to avoid a State Snapshot Transfer (SST) during the rolling upgrade. The gcache size can be configured by setting gcache.size. For example: [wsrep\_provider\_options](../../reference/wsrep-variable-details/wsrep_provider_options.md)="gcache.size=2G".&#x20;

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend mariadb-backup.&#x20;

Then, for each node, perform the following steps:

{% stepper %}
{% step %}
Modify the repository configuration, so the system's package manager installs MariaDB 11.4.

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see [Updating the MariaDB APT repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see [Updating the MariaDB YUM repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) for more information.
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see [Updating the MariaDB ZYpp repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper) for more information.ser
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
If you use a load balancing proxy such as MaxScale or HAProxy, make sure to drain the server from the pool so it does not receive any new connections.
{% endstep %}

{% step %}
[Stop MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb).
{% endstep %}

{% step %}
Uninstall the old version of MariaDB and the Galera wsrep provider.

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
{% code overflow="wrap" expandable="true" %}
```bash
sudo apt-get remove mariadb-server galera
```
{% endcode %}
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
{% code overflow="wrap" expandable="true" %}
```bash
sudo yum remove MariaDB-server galera
```
{% endcode %}
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
{% code overflow="wrap" expandable="true" %}
```bash
sudo zypper remove MariaDB-server galera
```
{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Install the new version of MariaDB and the Galera wsrep provider\[cite: 5, 6, 7, 8].

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see Installing MariaDB Packages with APT for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see [Installing MariaDB Packages with YUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) for more information\[cite: 5, 6, 7, 8].
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see [Installing MariaDB Packages with ZYpp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper) for more information.
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Make any desired changes to configuration [options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) in option files, such as `my.cnf`. This includes removing any system variables or options that are no longer supported.
{% endstep %}

{% step %}
On Linux distributions that use systemd you may need to increase the service startup timeout as the default timeout of ninety seconds may not be sufficient. See [Systemd: Configuring the Systemd Service Timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) for more information.
{% endstep %}

{% step %}
[Start MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb).
{% endstep %}

{% step %}
Run [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) (or [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade)) with the `--skip-write-binlog` option. `mysql_upgrade` does two things:&#x20;

1. Ensures that the system tables in the mysql database are fully compatible with the new version.&#x20;
2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB
{% endstep %}
{% endstepper %}

When this process is done for one node, move onto the next node.

{% hint style="warning" %}
When upgrading the Galera wsrep provider, sometimes the Galera protocol version can change. The Galera wsrep provider should not start using the new protocol version until all cluster nodes have been upgraded to the new version, so this is not generally an issue during a rolling upgrade. However, this can cause issues if you restart a non-upgraded node in a cluster where the rest of the nodes have been upgraded.
{% endhint %}

{% @marketo/form formId="4316" %}
