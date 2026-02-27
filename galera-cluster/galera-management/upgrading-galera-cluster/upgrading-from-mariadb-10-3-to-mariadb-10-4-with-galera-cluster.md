# Upgrading from MariaDB 10.3 to MariaDB 10.4 with Galera Cluster

**MariaDB starting with** [**10.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1)

Since [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), the [MySQL-wsrep](https://github.com/codership/mysql-wsrep) patch has been merged into MariaDB Server. Therefore, in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and above, the functionality of MariaDB Galera Cluster can be obtained by installing the standard MariaDB Server packages and the Galera wsrep provider library package.

Beginning in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) ships with the MariaDB Server. Upgrading a Galera Cluster node is very similar to upgrading a server from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104). For more information on that process as well as incompatibilities between versions, see the [Upgrade Guide](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104).

## Performing a Rolling Upgrade

The following steps can be used to perform a rolling upgrade from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) when using Galera Cluster. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational. There is no downtime from the application's perspective.

First, before you get started:

1. First, take a look at [Upgrading from MariaDB 10.3 to MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104) to see what has changed between the major versions.
2. Check whether any system variables or options have been changed or removed. Make sure that your server's configuration is compatible with the new MariaDB version before upgrading.
3. Check whether replication has changed in the new MariaDB version in any way that could cause issues while the cluster contains upgraded and non-upgraded nodes.
4. Check whether any new features have been added to the new MariaDB version. If a new feature in the new MariaDB version cannot be replicated to the old MariaDB version, then do not use that feature until all cluster nodes have been upgrades to the new MariaDB version.
5. Next, make sure that the Galera version numbers are compatible.
6. If you are upgrading from the most recent [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) release to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), then the versions will be compatible. [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) uses Galera 3 (i.e. Galera wsrep provider versions 25.3.x), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) uses Galera 4 (i.e. Galera wsrep provider versions 26.4.x). This means that upgrading to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) also upgrades the system to Galera 4. However, Galera 3 and Galera 4 should be compatible for the purposes of a rolling upgrade, as long as you are using Galera 26.4.2 or later.
7. See [What is MariaDB Galera Cluster](../../readme/mariadb-galera-cluster-guide.md)? [Galera wsrep provider Versions](../../reference/galera-cluster-status-variables.md#wsrep_provider_version) for information on which MariaDB releases uses which Galera wsrep provider versions.
8. Ideally, you want to have a large enough gcache to avoid a [State Snapshot Transfer (SST)](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) during the rolling upgrade. The gcache size can be configured by setting [gcache.size](../../reference/wsrep-variable-details/wsrep_provider_options.md#gcachesize) For example:`wsrep_provider_options="gcache.size=2G"`

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup).

Then, for each node, perform the following steps:

{% stepper %}
{% step %}
Modify the repository configuration, so the system's package manager installs [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104).

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see [Updating the MariaDB APT repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see [Updating the MariaDB YUM repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see [Updating the MariaDB ZYpp repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
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
```bash
sudo apt-get remove mariadb-server galera
```
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
```bash
sudo yum remove MariaDB-server galera
```
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
```bash
sudo zypper remove MariaDB-server galera
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Install the new version of MariaDB and the Galera wsrep provider.

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see [Installing MariaDB Packages with APT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-alongside-mysql) for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see [Installing MariaDB Packages with YUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) for more information.
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see [Installing MariaDB Packages with ZYpp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper) for more information.
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Make any desired changes to configuration options in [option files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files), such as `my.cnf`. This includes removing any system variables or options that are no longer supported.
{% endstep %}

{% step %}
On Linux distributions that use `systemd` you may need to increase the service startup timeout as the default timeout of 90 seconds may not be sufficient. See [Systemd: Configuring the Systemd Service Timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd#configuring-the-systemd-service-timeout) for more information.
{% endstep %}

{% step %}
[Start MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb).
{% endstep %}

{% step %}
Run [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) with the `--skip-write-binlog` option.

`mysql_upgrade` does two things:

1. Ensures that the system tables in the [mysql ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables) `l` database are fully compatible with the new version.
2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB.
{% endstep %}
{% endstepper %}

When this process is done for one node, move onto the next node.

{% hint style="warning" %}
When upgrading the Galera wsrep provider, sometimes the Galera protocol version can change. The Galera wsrep provider should not start using the new protocol version until all cluster nodes have been upgraded to the new version, so this is not generally an issue during a rolling upgrade. However, this can cause issues if you restart a non-upgraded node in a cluster where the rest of the nodes have been upgraded.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
