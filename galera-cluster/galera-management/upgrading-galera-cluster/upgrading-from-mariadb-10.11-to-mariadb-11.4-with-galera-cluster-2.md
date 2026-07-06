---
description: >-
  Rolling upgrade procedure for moving a Galera Cluster from MariaDB 11.8 to
  MariaDB 12.3, covering pre-upgrade checks, repository changes, critical
  package architecture changes (mariadb-server-galera)
---

# Upgrading from MariaDB 11.8 to MariaDB 12.3 with Galera Cluster

[Galera Cluster](../../) ships with the MariaDB Server. Upgrading a Galera Cluster node is very similar to upgrading a server from [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) to [MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements). For more information on that process as well as incompatibilities between versions, see the [Upgrade Guide](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths).&#x20;

## Galera Packaging Changes in MariaDB 12.3

As of MariaDB 12.3, Galera is no longer a dependency of the standard server packages ([MDEV-30953](https://jira.mariadb.org/browse/MDEV-30953)):

{% tabs %}
{% tab title="Up to MariaDB 11.8" %}
The standard server package (`mariadb-server` on Debian/Ubuntu, `MariaDB-server` on RHEL/SLES) depends directly on `galera-4`.
{% endtab %}

{% tab title="From MariaDB 12.3" %}
Galera is no longer a server dependency. A new package — `mariadb-server-galera` (Debian/Ubuntu) / `MariaDB-server-galera` (RHEL/SLES) — must be installed explicitly.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
`galera-4` did not *become* `mariadb-server-galera`. `galera-4` is the wsrep provider library and still exists in MariaDB 12.3 — `mariadb-server-galera` depends on it. What moved is the dependency, not the package identity: Galera is still shipped in the MariaDB repositories, but it is no longer installed automatically with `mariadb-server`.
{% endhint %}

The packages to remove (old 11.8) and install (new 12.3) per platform:

| Platform      | Remove (old 11.8)             | Install (new 12.3)                          |
| ------------- | ----------------------------- | ------------------------------------------- |
| Debian/Ubuntu | `mariadb-server galera-4`     | `mariadb-server mariadb-server-galera`      |
| RHEL/yum      | `MariaDB-server galera-4`     | `MariaDB-server MariaDB-server-galera`      |
| SLES/zypper   | `MariaDB-server galera-4`     | `MariaDB-server MariaDB-server-galera`      |

## Performing a Rolling Upgrade

The following steps can be used to perform a rolling upgrade from MariaDB 11.8 to MariaDB 12.3 when using Galera Cluster. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational. There is no downtime from the application's perspective.&#x20;

First, before you get started:&#x20;

1. First, take a look at Upgrading from MariaDB 11.8 to MariaDB 12.3 to see what has changed between the major versions.&#x20;
2. CRITICAL - Package Architecture Changes: As of MariaDB 12.3, Galera is no longer a dependency of the standard server packages. Galera itself remains available in the MariaDB repositories — it is simply no longer installed automatically with `mariadb-server`. A new `mariadb-server-galera` package now exists for Debian and RPM packages. You must explicitly install `mariadb-server-galera`. If you only upgrade the standard `mariadb-server` package, your systemd service definitions will not be Galera-capable for bootstrap or SST transfers.
3. Verify Configuration Files: Check whether any system variables or options have been changed or removed. For example, the use of `MYSQLD_OPTS` as an environment variable for systemd services is deprecated in 12.3. You should place configuration options directly into configuration files.
4. Assess Replication: Check whether replication behavior has changed in the new version.
5. Defer New Features: Do not use newly introduced features until all cluster nodes have been successfully upgraded to the new MariaDB version.
6. Ensure Compatibility: Verify your Galera provider version compatibility. Make sure you are prepared to manually supply `galera-4` if relying on RPMs.
7. Tune Gcache Size: You want to have a large enough `gcache` to avoid a [State Snapshot Transfer (SST)](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/) during the rolling upgrade. Ensure your `wsrep_provider_options="gcache.size=2G"` is adequately sized.
8. Take a Backup: It is always recommended to take a reliable backup of your database using a tool like [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview) before proceeding.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend mariadb-backup.&#x20;

Then, for each node, perform the following steps:

{% stepper %}
{% step %}
Modify the repository configuration, so the system's package manager installs [MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements).

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see [Updating the MariaDB APT repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see [Updating the MariaDB YUM repository to a New Major Release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) for more information.
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see [Updating the MariaDB ZYpp repository to a New Major Release](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper) for more information.
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
sudo apt-get remove mariadb-server galera-4
```
{% endcode %}
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
{% code overflow="wrap" expandable="true" %}
```bash
sudo yum remove MariaDB-server galera-4
```
{% endcode %}
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
{% code overflow="wrap" expandable="true" %}
```bash
sudo zypper remove MariaDB-server galera-4
```
{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Install the new version of MariaDB and the Galera wsrep provider. As of MariaDB 12.3, the Galera files are no longer part of the standard `mariadb-server` package, so you must explicitly install the new Galera package (`mariadb-server-galera` on Debian/Ubuntu, `MariaDB-server-galera` on RHEL/SLES) alongside the server.

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
Install both the server and the Galera package:

{% code overflow="wrap" expandable="true" %}
```bash
sudo apt-get install mariadb-server mariadb-server-galera
```
{% endcode %}

see Installing MariaDB Packages with APT for more information.
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
Install both the server and the Galera package:

{% code overflow="wrap" expandable="true" %}
```bash
sudo yum install MariaDB-server MariaDB-server-galera
```
{% endcode %}

see [Installing MariaDB Packages with YUM](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) for more information.
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
Install both the server and the Galera package:

{% code overflow="wrap" expandable="true" %}
```bash
sudo zypper install MariaDB-server MariaDB-server-galera
```
{% endcode %}

see [Installing MariaDB Packages with ZYpp](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper) for more information.
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
