---
description: >-
  Rolling upgrade procedure for moving a Galera Cluster from MariaDB 11.4 to
  MariaDB 11.8, covering pre-upgrade checks, repository changes,
  system-versioned table constraints
---

# Upgrading from MariaDB 11.4 to MariaDB 11.8 with Galera Cluster

[Galera Cluster](../../) ships with the MariaDB Server. Upgrading a Galera Cluster node is very similar to upgrading a server from [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114) to [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118). For more information on that process as well as incompatibilities between versions, see the [Upgrade Guide](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading).&#x20;

## Performing a Rolling Upgrade

The following steps can be used to perform a rolling upgrade from MariaDB 10.11 to MariaDB 11.4 when using Galera Cluster. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational. There is no downtime from the application's perspective\[cite: 5, 6, 7, 8].&#x20;

First, before you get started:&#x20;

1. Take a look at [Upgrading from MariaDB 11.4 to MariaDB 11.8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-11-4-to-mariadb-11-8) to see what has changed between the major versions.&#x20;
2. System-Versioned Tables Performance Warning: MariaDB 11.8 extends the maximal allowed value for timestamps up to `'2106-02-07 06:28:15 UTC'`. If you are using system-versioned tables, all rows and indexes must be updated to use this extended range. Upgrading to 11.8 can take a long time if you have many rows in your system-versioned tables! If you are not using system-versioned tables, the upgrade should execute rapidly.
3. Check whether any system variables or options have been changed or removed. For example, the `alter_algorithm` system variable has been deprecated and is ignored since [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115). Make sure that your server's configuration is compatible with the new MariaDB version before upgrading.
4. Character Set Default Shift: The default character set changes from `latin1` to `utf8mb4`. Ensure your database parameters align or explicitly define your previous collation options in your configuration files if you maintain legacy replication branches.
5. Check whether replication has changed in the new MariaDB version in any way that could cause issues while the cluster contains upgraded and non-upgraded nodes.&#x20;
6. Check whether any new features have been added to the new MariaDB version. If a new feature (such as the new [VECTOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors) data type or parsec authentication plugin) cannot be replicated to the old MariaDB version, then do not use that feature until all cluster nodes have been upgraded.
7. Next, make sure that the Galera version numbers are compatible. Both MariaDB 11.4 and 11.8 releases ship with modern releases of Galera 4 (wsrep API 26). For the purposes of a rolling upgrade, ensure your versions align across these ecosystem baselines.
8. See [What is MariaDB Galera Cluster](../../readme/mariadb-galera-cluster-guide.md)?: Galera wsrep provider Versions for information on which MariaDB releases use which Galera wsrep provider versions.&#x20;
9. You want to have a large enough gcache to avoid a State Snapshot Transfer (SST) during the rolling upgrade. The gcache size can be configured by setting gcache.size. For example: [wsrep\_provider\_options](../../reference/wsrep-variable-details/wsrep_provider_options.md)="gcache.size=2G".&#x20;

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend mariadb-backup.&#x20;

Then, for each node, perform the following steps:

{% stepper %}
{% step %}
Modify the repository configuration, so the system's package manager installs [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118).

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
If you use a load balancing proxy such as [MaxScale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-quickstart-guides) or HAProxy, make sure to drain the server from the pool so it does not receive any new connections.
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
On Linux distributions that use `systemd` you may need to increase the service startup timeout as the default timeout of ninety seconds may not be sufficient(especially if system-versioned tables trigger structural row scans). See [Systemd: Configuring the Systemd Service Timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) for more information.
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

When this process is done for one node, move onto the next node\[cite: 5, 6, 7, 8].

{% hint style="warning" %}
When upgrading the Galera wsrep provider, sometimes the Galera protocol version can change. The Galera wsrep provider should not start using the new protocol version until all cluster nodes have been upgraded to the new version, so this is not generally an issue during a rolling upgrade. However, this can cause issues if you restart a non-upgraded node in a cluster where the rest of the nodes have been upgraded.
{% endhint %}

{% @marketo/form formId="4316" %}
