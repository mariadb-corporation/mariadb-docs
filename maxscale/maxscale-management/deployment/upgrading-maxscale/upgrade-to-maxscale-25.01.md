# Upgrade to MaxScale 25.01

These instructions detail the upgrade to **MariaDB MaxScale 25.01** in a **MaxScale Instance** configuration on a range of [supported Operating Systems](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/compatibility).

MariaDB MaxScale is an advanced database proxy and query router.

## Term Definitions

| Term              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MaxScale instance | <ul><li>MariaDB MaxScale running by itself on a single host.</li><li>It interacts with other hosts, such as deployments using <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication">MariaDB Replication</a>, <a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/">Galera Cluster</a>, and <a href="https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore">ColumnStore</a>.</li><li>It serves as the database proxy and load balancer.</li></ul> |
| upgrade           | <ul><li>A change from lower-versioned release of MariaDB MaxScale to a higher-versioned release of MariaDB MaxScale.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                      |

## Backing Up Configuration

Upgrades can move or change configuration files. Before starting an upgrade, always back up your configuration files to ensure you can revert to the working system in the event that you encounter any issues during the upgrade.

To back up a configuration file, create a copy:

```bash
sudo cp /etc/maxscale.cnf /data/backups/config/maxscale.cnf
```

## Upgrade

MariaDB Corporation provides package repositories for YUM (RHEL, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

### Stop the MaxScale Process

Before upgrading MariaDB MaxScale, first stop the current process.

For distributions that use systemd (most supported OSes), you can manage the Server process using the `systemctl` command:

```bash
sudo systemctl stop maxscale
```

### Upgrade MaxScale

Upgrade MaxScale following the instructions for your Linux distribution:

{% tabs %}
{% tab title="RHEL" %}
#### Upgrade via DNF (RHEL)

{% stepper %}
{% step %}
**Customer Download Token**

Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
{% endstep %}

{% step %}
**Configure YUM / DNF package repository**

Pass the version you want to install using the `--mariadb-maxscale-version` flag to the [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) script. The following directions reference `25.01`.

To configure YUM package repositories:

```bash
sudo yum install curl
```

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-maxscale-version="25.01"
```
{% endstep %}

{% step %}
**Upgrade MariaDB MaxScale and package dependencies:**

```
sudo dnf update maxscale
```
{% endstep %}

{% step %}
**Configure MaxScale**

The upgrade process only loads MaxScale onto the system. MaxScale requires configuration before MaxScale is ready for use.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Debian / Ubuntu" %}
#### Upgrade via APT (Debian, Ubuntu)

{% stepper %}
{% step %}
**Customer Download Token**

Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
{% endstep %}

{% step %}
**Configure APT package repository**

Pass the version you want to install using the `--mariadb-maxscale-version` flag to the [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) script. The following directions reference `25.01`.

To configure APT package repositories:

```bash
sudo apt install curl
```

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-maxscale-version="25.01"
```

```bash
sudo apt update
```
{% endstep %}

{% step %}
**Upgrade MariaDB MaxScale and package dependencies**

```bash
sudo apt install --only-upgrade maxscale
```
{% endstep %}

{% step %}
**Configure MaxScale**

The upgrade process only loads MaxScale onto the system. MaxScale requires configuration before MaxScale is ready for use.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="SLES" %}
#### Upgrade via ZYpp (SLES)

{% stepper %}
{% step %}
**Customer Download Token**

Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.\\
{% endstep %}

{% step %}
**Configure ZYpp package repository**

Pass the version you want to install using the `--mariadb-maxscale-version` flag to the [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) script. The following directions reference `25.01`.

To configure ZYpp package repositories:

```bash
sudo zypper install curl
```

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
echo "4d483b4df193831a0101d3dfa7fb3e17411dda7fc06c31be4f9e089c325403c0  mariadb_es_repo_setup" \
    | sha256sum -c -
```

```bash
chmod +x mariadb_es_repo_setup
```

```bash
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-maxscale-version="25.01"
```
{% endstep %}

{% step %}
**Upgrade MariaDB MaxScale and package dependencies**

```bash
sudo zypper update maxscale
```
{% endstep %}

{% step %}
**Configure MaxScale**

The upgrade process only loads MaxScale onto the system. MaxScale requires configuration before MaxScale is ready for use.
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

## Configuration

Configuration parameters can change between releases of MariaDB MaxScale, which can have unexpected results.

1. Determine which parameters have changed by reviewing **all** the changes made between your current release and the upgrade release.
2. Change the specific parameters in `maxscale.cnf`.

### Changes in MaxScale Versions

{% tabs %}
{% tab title="MaxScale 23.02" %}
#### Changes in MaxScale 23.02

When upgrading from MaxScale 22.08 and earlier to MaxScale 25.01, the changes introduced in MaxScale 23.02 must be taken into consideration.

MariaDB MaxScale 22.08 is fully compatible with MariaDB MaxScale 23.02 with the exception that some features have been removed.

**Removed Features**

* The `csmon` monitor has been removed after previously being deprecated in MaxScale 22.08.2.
* The `auroramon` monitor has been removed after previously being deprecated in MaxScale 22.08.2.
* The `maxctrl cluster` commands have been removed after previously being deprecated in MaxScale 22.08.2
* The `maxctrl drain` command has been removed, because it is obsolete.

**Removed Deprecated `maxctrl` Commands**

In MariaDB MaxScale 23.02, some deprecated MaxCtrl commands were removed:

* `maxctrl cluster`
* `maxctrl drain` has been removed and can be replaced with `maxctrl set server SERVER_NAME drain`

**Removed Deprecated `maxctrl` Options**

In MariaDB MaxScale 23.02, several deprecated MaxCtrl command-line options were removed, since MaxScale previously added the ability to specify module parameters to MaxCtrl as key-value pairs.

This change can impact backward compatibility. Some scripts and tools written for previous versions of MaxCtrl will require updates to continue functioning with MaxCtrl from MaxScale 23.02. The old command-line parameters have been deprecated since MaxScale 22.08. The new syntax to specify parameters as key-value pairs has been supported since MariaDB MaxScale 6.2.0.

For example, in previous releases, the following `maxctrl create monitor` command could be executed:

```bash
maxctrl create monitor mdb_monitor mariadbmon \
   --monitor-user mxs \
   --monitor-password 'maxscale_passwd' \
   replication_user='repl_user' \
   replication_password='repl_pass' \
   --servers node1 node2 node3
```

Starting with MariaDB MaxScale 23.02, some deprecated command-line options have been removed and must be replaced with a key-value pair using the corresponding module parameter:

```bash
maxctrl create monitor mdb_monitor mariadbmon \
   user='mxs' \
   password='maxscale_passwd' \
   replication_user='repl_user' \
   replication_password='repl_pass' \
   --servers node1 node2 node3
```

For `maxctrl create listener`, the following deprecated command-line options were removed and must be replaced with a key-value pair using the listed parameter:

| Command-line Option             | Replaced by Parameter         |
| ------------------------------- | ----------------------------- |
| `--authenticator`               | `authenticator`               |
| `--authenticator-options`       | `authenticator_options`       |
| `--interface`                   | `interface`                   |
| `--protocol`                    | `protocol`                    |
| `--tls-ca-cert`                 | `ssl_ca`                      |
| `--tls-cert`                    | `ssl_cert`                    |
| `--tls-cert-verify-depth`       | `ssl_cert_verify_depth`       |
| `--tls-crl`                     | `ssl_crl`                     |
| `--tls-key`                     | `ssl_key`                     |
| `--tls-verify-peer-certificate` | `ssl_verify_peer_certificate` |
| `--tls-verify-peer-host`        | `ssl_verify_peer_host`        |
| `--tls-version`                 | `ssl_version`                 |

For `maxctrl create monitor`, the following deprecated command-line options were removed and must be replaced with a key-value pair using the listed parameter:

| Command-line Option  | Replaced by Parameter |
| -------------------- | --------------------- |
| `--monitor-password` | `password`            |
| `--monitor-user`     | `user`                |
{% endtab %}

{% tab title="MaxScale 22.08" %}
#### Changes in MaxScale 22.08

When upgrading from MaxScale 6 and earlier to MaxScale 25.01, the changes introduced in MaxScale 22.08 must be taken into consideration.

**Database Firewall Filter**

* The `dbfwfilter` that was deprecated in MaxScale 6 has been removed in MaxScale 22.08.

**Deprecated Parameters**

* The server parameter `ssl_ca_cert` has been renamed to `ssl_ca` and `ssl_ca_cert` has been deprecated. `ssl_ca_cert` is now an alias for `ssl_ca` and can still be used, but MariaDB recommends using `ssl_ca`, as support for `ssl_ca_cert` will be removed in a future release.
* The server parameter `admin_ssl_ca_cert` has been renamed to `admin_ssl_ca` and `admin_ssl_ca_cert` has been deprecated. `admin_ssl_ca_cert` is now an alias for `admin_ssl_ca` and can still be used, but MariaDB recommends using `admin_ssl_ca`, as support for `admin_ssl_ca_cert` will be removed in a future release.

**Removed Parameters**

* The following MariaDB Monitor (`mariadbmon`) parameters have been removed:
  * `ignore_external_masters`
  * `detect_replication_lag`
  * `detect_standalone_master`
  * `detect_stale_master` (replaced by `master_conditions`)
  * `detect_stale_slave` (replaced by `slave_conditions`)

**Default Changed for Logging Behavior**

* Prior to MaxScale 22.08.1, by default MaxScale logs to `syslog` in addition to the MaxScale log.
* Starting with MaxScale 22.08.1, by default MaxScale only logs to the MaxScale log and no longer logs to `syslog`.
*   To retain the behavior of prior releases, in your MaxScale configuration, under the `[maxscale]` section, specify `syslog=true`:

    ```editorconfig
    [maxscale]
    syslog=true
    ```

**REST API Endpoint Removed**

* The `/v1/maxscale/tasks/` endpoint has been removed from the REST API.
{% endtab %}

{% tab title="MaxScale 6" %}
#### Changes in MaxScale 6

When upgrading from MaxScale 2.5 and earlier to MaxScale 25.01, the changes introduced in MaxScale 6 must be taken into consideration.

**TLS/SSL**

* MaxScale's `ssl` parameter can no longer be set to `required` or `disabled`:
  * `ssl=true` replaces `ssl=required`
  * `ssl=false` replaces `ssl=disabled`

**Deprecated Features**

* dbfwfilter is deprecated (but not removed) in MaxScale 6.
* Multi-line configuration parameters are deprecated (but not removed) in MaxScale 6.

**Defaults Changed**

* The default value of `threads` has changed from `1` to `auto`

**ColumnStore**

* When using MaxScale with ColumnStore 5 and later, MariaDB Monitor (`mariadbmon`) is used instead of ColumnStore Monitor (`csmon`).
{% endtab %}

{% tab title="MaxScale 2.5" %}
**Changes in MaxScale 2.5**

When upgrading from MaxScale 2.4 and earlier to MaxScale 25.01, the changes introduced in MaxScale 2.5 must be taken into consideration.

**Passwords**

* MaxScale's password encryption features have been updated to be more secure. Passwords encrypted in old versions will still work, but it is recommended to generate a new encryption key with the maxkeys command and to re-encrypt passwords with the maxpasswd command.

**User Account Privileges**

MaxScale's user account requires additional privileges in MaxScale 2.5.

Ensure that the user account has the following privileges:

```sql
GRANT SHOW DATABASES ON *.*
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.columns_priv
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.db
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.procs_priv
        TO 'mxs'@'192.0.2.1';
GRANT SELECT ON mysql.proxies_priv
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.roles_mapping
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.tables_priv
     TO 'maxscale'@'192.0.2.1';
GRANT SELECT ON mysql.user
     TO 'maxscale'@'192.0.2.1';
```

**MariaDB Monitor**

MaxScale 2.5 includes configuration changes for [MariaDB Monitor (mariadbmon)](../../../reference/maxscale-monitors/mariadb-monitor.md):

*   The `detect_stale_master` and the `detect_standalone_master` parameters have been deprecated. They can still be used, but they will be removed in a later version of MaxScale. Users should use the `master_conditions` parameter instead.

    For example:

    ```editorconfig
    [repl-monitor]
    type          = monitor
    module        = mariadbmon
    servers       = server1,server2,server3
    user          = maxscale
    password      = max_passwd
    auto_failover = ON
    auto_rejoin   = ON
    master_conditions = connected_slave,running_slave
    ```
*   The `detect_stale_slave` parameter has been deprecated. It can still be used, but it will be removed in a later version of MaxScale. Users should use the `slave_conditions` parameter instead.

    For example:

    ```editorconfig
    [repl-monitor]
    type          = monitor
    module        = mariadbmon
    servers       = server1,server2,server3
    user          = maxscale
    password      = max_passwd
    auto_failover = ON
    auto_rejoin   = ON
    slave_conditions  = running_master,writable_master
    ```

**ColumnStore Monitor**

MaxScale 2.5 includes configuration changes for [ColumnStore Monitor (csmon)](../../../maxscale-archive/archive/mariadb-maxscale-21-06/mariadb-maxscale-2106-maxscale-21-06-monitors/maxscale-mariadb-monitor-usage/maxscale-mariadb-monitor-usage-columnstore-monitor.md):

*   The `version` parameter was previously optional, but it is now required.

    For example:

    ```
    [col-monitor]
    type          = monitor
    module        = csmon
    servers       = server1,server2,server3
    user          = maxscale
    password      = max_passwd
    version       = 1.2
    ```

**Binlog Router**

MaxScale 2.5 includes a completely re-implemented [Binlog Router (binlogrouter)](../../../reference/maxscale-routers/maxscale-binlogrouter.md):

* Thoroughly test your configuration with the new implementation to ensure that the new version meets your needs.
{% endtab %}
{% endtabs %}

## Starting the MaxScale Instance

MariaDB MaxScale installations includes configuration to start, stop, restart, enable/disable on boot, and check the status of the MaxScale Instance using the operating system default process management system.

For distributions that use systemd (most supported OSes), you can manage the MaxScale process using the `systemctl` command:

| Operation              | Command                           |
| ---------------------- | --------------------------------- |
| Start                  | `sudo systemctl start maxscale`   |
| Stop                   | `sudo systemctl stop maxscale`    |
| Restart                | `sudo systemctl restart maxscale` |
| Enable during startup  | `sudo systemctl enable maxscale`  |
| Disable during startup | `sudo systemctl disable maxscale` |
| Status                 | `sudo systemctl status maxscale`  |

## Testing

When you have MariaDB MaxScale up and running, you should test it to ensure that it is working and that weren't any issues during startup.

### Checking MaxScale Status

Check that MaxScale is running properly by using the [MaxCtrl](../../administrative-tools-for-mariadb-maxscale-maxctrl/) utility:

```bash
sudo maxctrl show maxscale
```

```
┌──────────────┬──────────────────────────────────────────────────────────────────────┐
│ Version      │ 25.01.2                                                              │
├──────────────┼──────────────────────────────────────────────────────────────────────┤
│ Commit       │ 61b8bbf7f63c38ca9c408674e66f3627a0b2192e                             │
├──────────────┼──────────────────────────────────────────────────────────────────────┤
│ Started At   │ Fri, 03 Jan 2025 18:05:18 GMT                                        │
├──────────────┼──────────────────────────────────────────────────────────────────────┤
│ Activated At │ Fri, 03 Jan 2025 18:05:18 GMT                                        │
├──────────────┼──────────────────────────────────────────────────────────────────────┤
│ Uptime       │ 109                                                                  │
├──────────────┼──────────────────────────────────────────────────────────────────────┤
│ Parameters   │ {                                                                    │
│              │     "libdir": "/usr/lib/x86_64-linux-gnu/maxscale",                  │
│              │     "datadir": "/var/lib/maxscale",                                  │
│              │     "process_datadir": "/var/lib/maxscale/data3850",                 │
│              │     "cachedir": "/var/cache/maxscale",                               │
│              │     "configdir": "/etc",                                             │
│              │     "config_persistdir": "/var/lib/maxscale/maxscale.cnf.d",         │
│              │     "module_configdir": "/etc/maxscale.modules.d",                   │
│              │     "piddir": "/var/run/maxscale",                                   │
│              │     "logdir": "/var/log/maxscale",                                   │
│              │     "langdir": "/var/lib/maxscale",                                  │
│              │     "execdir": "/usr/bin",                                           │
│              │     "connector_plugindir": "/usr/lib/x86_64-linux-gnu/mysql/plugin", │
│              │     "threads": 1,                                                    │
│              │     "thread_stack_size": 8388608,                                    │
│              │     "writeq_high_water": 0,                                          │
│              │     "writeq_low_water": 0,                                           │
│              │     "auth_connect_timeout": 3,                                       │
│              │     "auth_read_timeout": 1,                                          │
│              │     "auth_write_timeout": 2,                                         │
│              │     "skip_permission_checks": false,                                 │
│              │     "admin_auth": true,                                              │
│              │     "admin_enabled": true,                                           │
│              │     "admin_log_auth_failures": true,                                 │
│              │     "admin_host": "127.0.0.1",                                       │
│              │     "admin_port": 8989,                                              │
│              │     "admin_ssl_key": "",                                             │
│              │     "admin_ssl_cert": "",                                            │
│              │     "admin_ssl_ca_cert": "",                                         │
│              │     "admin_pam_readwrite_service": "",                               │
│              │     "admin_pam_readonly_service": "",                                │
│              │     "passive": false,                                                │
│              │     "query_classifier": "",                                          │
│              │     "query_classifier_cache_size": 155008819,                        │
│              │     "retain_last_statements": 0,                                     │
│              │     "dump_last_statements": "never",                                 │
│              │     "session_trace": 0,                                              │
│              │     "load_persisted_configs": true,                                  │
│              │     "max_auth_errors_until_block": 10                                │
│              │ }                                                                    │
└──────────────┴──────────────────────────────────────────────────────────────────────┘
```
