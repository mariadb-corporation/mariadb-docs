# Community Server with ColumnStore

These instructions detail the deployment of **MariaDB ColumnStore 6** with **MariaDB Community Server 10.6** in a **Single-node ColumnStore Deployment** configuration on a range of supported Operating Systems.

These instructions detail how to deploy a single-node columnar database, which is suited for an analytical or OLAP workload that does not require high availability (HA). This deployment type is generally for non-production use cases, such as for development and testing.

## Community Server Components

These instructions detail the deployment of the following MariaDB Community Server components:

<table><thead><tr><th width="234.1480712890625" valign="top">Component</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">MariaDB ColumnStore 6</td><td valign="top"><ul><li>It is a columnar storage engine that provides distributed, columnar storage for scalable analytical processing and smart transactions.</li><li>It is the analytical component of MariaDB's single stack <a href="../htap/">Hybrid Transactional/Analytical Processing (HTAP)</a> solution.</li></ul></td></tr></tbody></table>

## Term Definitions

<table><thead><tr><th width="205.70361328125" valign="top">Term</th><th valign="top">Definition</th></tr></thead><tbody><tr><td valign="top">columnar database</td><td valign="top"><ul><li>A database where the columns of each row are stored separately.</li><li>Best suited for analytical and OLAP workloads.</li><li>Also known as a "column-oriented database".</li></ul></td></tr><tr><td valign="top">row database</td><td valign="top"><ul><li>A database where all columns of each row are stored together.</li><li>Best suited for transactional and OLTP workloads.</li><li>Also known as a "row-oriented database".</li></ul></td></tr></tbody></table>

## High Availability

Single-node ColumnStore 6 does not support high availability.

For high availability and scalability, instead see "[ColumnStore Object Storage Topology](../columnstore-object-storage/)" or "[ColumnStore Shared Local Storage Topology](../columnstore-shared-local-storage/)".

## System Preparation

Systems hosting a ColumnStore deployment requires some additional configuration prior to installation:

1. [Optimize Linux kernel parameters](community-server-with-columnstore.md#optimize-linux-kernel-parameters)
2. [Configure the Linux security module to support installation](community-server-with-columnstore.md#lsm-configuration-for-install)
3. [Configure the character encoding](community-server-with-columnstore.md#configure-the-character-encoding)
4. [Optionally configure S3-compatible storage](community-server-with-columnstore.md#s3-compatible-storage)

## Optimize Linux Kernel Parameters

MariaDB ColumnStore performs best when certain Linux kernel parameters are optimized.

1.  Set the relevant kernel parameters in a sysctl configuration file. For proper change management, we recommend setting them in a ColumnStore-specific configuration file.

    For example, create a `/etc/sysctl.d/90-mariadb-columnstore.conf` file with the following contents:

    ```editorconfig
    # minimize swapping
    vm.swappiness = 1

    # Increase the TCP max buffer size
    net.core.rmem_max = 16777216
    net.core.wmem_max = 16777216

    # Increase the TCP buffer limits
    # min, default, and max number of bytes to use
    net.ipv4.tcp_rmem = 4096 87380 16777216
    net.ipv4.tcp_wmem = 4096 65536 16777216

    # don't cache ssthresh from previous connection
    net.ipv4.tcp_no_metrics_save = 1

    # for 1 GigE, increase this to 2500
    # for 10 GigE, increase this to 30000
    net.core.netdev_max_backlog = 2500
    ```
2.  Set the same kernel parameters at runtime using the `sysctl` command:

    ```bash
    $ sudo sysctl --load=/etc/sysctl.d/90-mariadb-columnstore.conf
    ```

## LSM Configuration for Install

To avoid confusion and potential problems, we recommend configuring the system's Linux Security Module (LSM) during installation. The specific steps to configure the security module will depend on the platform.

In the [Configure the Linux Security Module](community-server-with-columnstore.md#lsm-configuration-for-install) section, we will configure the security module and restart it.

### SELinux (RHEL, CentOS)

SELinux must be set to `permissive` mode before installing MariaDB ColumnStore.

1.  Set SELinux to permissive mode by setting `SELINUX=permissive` in `/etc/selinux/config`.

    For example, the file will usually look like this after the change:

    ```editorconfig
    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #     enforcing - SELinux security policy is enforced.
    #     permissive - SELinux prints warnings instead of enforcing.
    #     disabled - No SELinux policy is loaded.
    SELINUX=permissive
    # SELINUXTYPE= can take one of three values:
    #     targeted - Targeted processes are protected,
    #     minimum - Modification of targeted policy. Only selected processes are protected.
    #     mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ```
2. Reboot the system.
3.  Confirm that SELinux is in `permissive` mode using `getenforce`:

    ```bash
    $ sudo getenforce
    ```

    ```
    Permissive
    ```

{% hint style="info" %}
Remember to [configure and re-enable SELinux](community-server-with-columnstore.md#configure-selinux-rhel-centos) after the installation is complete.
{% endhint %}

### AppArmor (Debian, Ubuntu)

AppArmor must be disabled before installing MariaDB ColumnStore.

1.  Disable AppArmor:

    ```bash
    $ sudo systemctl disable apparmor
    ```
2. Reboot the system.
3.  Confirm that no AppArmor profiles are loaded using `aa-status`:

    ```bash
    $ sudo aa-status
    ```

    Example output:

    ```
    apparmor module is loaded.
    0 profiles are loaded.
    0 profiles are in enforce mode.
    0 profiles are in complain mode.
    0 processes have profiles defined.
    0 processes are in enforce mode.
    0 processes are in complain mode.
    0 processes are unconfined but have a profile defined.
    ```

{% hint style="info" %}
Remember to [configure and re-enable AppArmor](community-server-with-columnstore.md#configure-apparmor-debian-ubuntu) after the installation is complete.
{% endhint %}

## Configure the Character Encoding

When using MariaDB ColumnStore, it is recommended to set the system's locale to UTF-8.

1.  On RHEL 8, install additional dependencies.

    ```bash
    $ sudo yum install glibc-locale-source glibc-langpack-en
    ```
2.  Set the system's locale to `en_US.UTF-8` by executing `localedef`:

    ```bash
    $ sudo localedef -i en_US -f UTF-8 en_US.UTF-8
    ```

## S3-Compatible Storage

MariaDB ColumnStore supports S3-compatible object storage.

S3-compatible object storage is optional, but **highly recommended**.

S3-compatible object storage is:

* **Compatible**: Many object storage services are compatible with the Amazon S3 API.
* **Economical**: S3-compatible object storage is often very low cost.
* **Flexible**: S3-compatible object storage is available for both cloud and on-premises deployments.
* **Limitless**: S3-compatible object storage is often virtually limitless.
* **Resilient**: S3-compatible object storage is often low maintenance and highly available, since many services use resilient cloud infrastructure.
* **Scalable**: S3-compatible object storage is often highly optimized for read and write scaling.
* **Secure**: S3-compatible object storage is often encrypted-at-rest.

Many S3-compatible object storage services exist. MariaDB Corporation cannot make guarantees about all S3-compatible object storage services, because different services provide different functionality.

If you have any questions about using specific S3-compatible object storage with MariaDB ColumnStore, [contact us](https://mariadb.com/contact/).

### Create an S3 Bucket

If you want to use S3-compatible storage, it is important to create the S3 bucket before you start ColumnStore.

If you already have an S3 bucket, confirm that the bucket is empty.

We will configure ColumnStore to use the S3 bucket later in the [Configure the S3 Storage Manager](community-server-with-columnstore.md#configure-the-s3-storage-manager) section.

{% hint style="info" %}
The specific steps to create the S3 bucket will depend on what S3-compatible storage you are using.
{% endhint %}

## ColumnStore Installation

MariaDB Corporation provides package repositories for YUM (RHEL, CentOS) and APT (Debian, Ubuntu).

MariaDB ColumnStore ships as a storage engine plugin for MariaDB Community Server and a platform engine to handle back-end storage processes. MariaDB Community Server 10.6 does not require any additional software to operate as a single-node analytics database.

### Install ColumnStore via YUM (RHEL, CentOS)

1.  Configure the YUM package repository.

    MariaDB ColumnStore `6` is available on MariaDB Community Server `10.6`.

    To configure YUM package repositories:

    ```bash
    $ sudo yum install curl
    ```

    ```bash
    $ curl -LsSO https://r.mariadb.com/downloads/mariadb_repo_setup
    ```

    ```bash
    $ echo "${checksum} mariadb_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    $ chmod +x mariadb_repo_setup
    ```

    ```bash
    $ sudo ./mariadb_repo_setup \
       --mariadb-server-version="mariadb-10.6"
    ```

    1. _Checksums of the various releases of the `mariadb_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
2.  Install the EPEL repository:

    ```bash
    $ sudo yum install epel-release
    ```
3.  Install some additional dependencies for ColumnStore:

    ```bash
    $ sudo yum install jemalloc
    ```
4.  Install MariaDB ColumnStore and package dependencies:

    ```bash
    $ sudo yum install MariaDB-server MariaDB-backup \
       MariaDB-shared MariaDB-client \
       MariaDB-columnstore-engine
    ```
5.  Configure MariaDB ColumnStore.

    Installation only loads MariaDB ColumnStore to the system. MariaDB ColumnStore requires configuration and additional post-installation steps before the database server is ready for use.

    See [ColumnStore Configuration](community-server-with-columnstore.md#columnstore-configuration).

### Install ColumnStore via APT (Debian, Ubuntu)

1.  Configure the APT package repository.

    MariaDB ColumnStore `6` is available on MariaDB Community Server `10.6`.

    To configure APT package repositories:

    ```bash
    $ sudo apt install curl
    ```

    ```bash
    $ curl -LsSO https://r.mariadb.com/downloads/mariadb_repo_setup
    ```

    ```bash
    $ echo "${checksum} mariadb_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    $ chmod +x mariadb_repo_setup
    ```

    ```bash
    $ sudo ./mariadb_repo_setup \
       --mariadb-server-version="mariadb-10.6"
    ```

    ```bash
    $ sudo apt update
    ```

    1. _Checksums of the various releases of the `mariadb_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
2.  Install some additional dependencies for ColumnStore.

    On Debian 10 and Ubuntu 20.04, install the following:

    ```bash
    $ sudo apt install libjemalloc2
    ```

    On Debian 9 and Ubuntu 18.04, install the following:

    ```bash
    $ sudo apt install libjemalloc1
    ```
3.  Install MariaDB ColumnStore and package dependencies:

    ```bash
    $ sudo apt install mariadb-server mariadb-backup \
       libmariadb3 mariadb-client \
       mariadb-plugin-columnstore
    ```
4.  Configure MariaDB ColumnStore.

    Installation only loads MariaDB ColumnStore to the system. MariaDB ColumnStore requires configuration and additional post-installation steps before the database server is ready for use.

    See [ColumnStore Configuration](community-server-with-columnstore.md#columnstore-configuration).

## ColumnStore Configuration

MariaDB ColumnStore requires configuration after it is installed. The configuration file location depends on your operating system.

### Community Server Configuration

MariaDB Community Server can be configured in the following ways:

* [System variables](../../../ha-and-performance/optimization-and-tuning/system-variables/) and [options](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md) can be set in a configuration file (such as `/etc/my.cnf`). MariaDB Community Server must be restarted to apply changes made to the configuration file.
* [System variables](../../../ha-and-performance/optimization-and-tuning/system-variables/) and [options](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md) can be set on the command-line.
* If a system variable supports dynamic changes, then it can be set on-the-fly using the [SET](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

### Configuration Files

MariaDB's packages include several bundled configuration files. It is also possible to create custom configuration files.

On RHEL and CentOS, MariaDB's packages bundle the following configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

And on RHEL and CentOS, custom configuration files from the following directories are read by default:

* `/etc/my.cnf.d/`

On Debian and Ubuntu, MariaDB's packages bundle the following configuration files:

* `/etc/mysql/my.cnf`
* `/etc/mysql/mariadb.cnf`
* `/etc/mysql/mariadb.conf.d/50-client.cnf`
* `/etc/mysql/mariadb.conf.d/50-mysql-clients.cnf`
* `/etc/mysql/mariadb.conf.d/50-mysqld_safe.cnf`
* `/etc/mysql/mariadb.conf.d/50-server.cnf`
* `/etc/mysql/mariadb.conf.d/60-galera.cnf`

And on Debian and Ubuntu, custom configuration files from the following directories are read by default:

* `/etc/mysql/conf.d/`
* `/etc/mysql/mariadb.conf.d/`

### Configuring MariaDB for ColumnStore

1.  Determine which [system variables](../../../ha-and-performance/optimization-and-tuning/system-variables/) and [options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) you need to configure.

    Mandatory system variables and options for single-node MariaDB ColumnStore include:

<table><thead><tr><th width="342">Connector</th><th>MariaDB Connector/R2DBC</th></tr></thead><tbody><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">character_set_server</a></td><td>Set this system variable to <code>utf8</code></td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md">collation_server</a></td><td>Set this system variable to <code>utf8_general_ci</code></td></tr><tr><td>columnstore_use_import_for_batchinsert</td><td>Set this system variable to <code>ALWAYS</code> to always use <code>cpimport</code> for <a href="../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md">LOAD DATA INFILE</a> and <a href="../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md">INSERT...SELECT</a> statements.</td></tr></tbody></table>

2. Choose a configuration file in which to configure your system variables and options.

We recommend **not** making custom changes to one of the bundled configuration files. Instead, create a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. If you want your custom configuration file to override the bundled configuration files, it is a good idea to prefix the custom configuration file's name with a string that will be sorted last, such as `z-`.

* On RHEL and CentOS, a good custom configuration file would be: `/etc/my.cnf.d/z-custom-my.cnf`
* On Debian and Ubuntu, a good custom configuration file would be: `/etc/mysql/mariadb.conf.d/z-custom-my.cnf`

3.  Set your system variables and options in the configuration file.\
    \
    They need to be set in a group that will be read by [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd.md), such as `[mariadb]` or `[server]`.\
    \
    For example:

    ```
    [mariadb]
    log_error                              = mariadbd.err
    character_set_server                   = utf8
    collation_server                       = utf8_general_ci
    ```

### Configure Cross Engine Joins

When a cross engine join is executed, the ExeMgr process connects to the server using the `root` user with no password by default. MariaDB Community Server 10.6 will reject this login attempt by default. If you plan to use Cross Engine Joins, you need to configure ColumnStore to use a different user account and password. These directions are for configuring the cross engine join user. Directions for creating the cross engine join user are in the [Create the Cross Engine Join User](community-server-with-columnstore.md#create-the-cross-engine-join-user) section.

To configure cross engine joins, perform the following steps, use the mcsSetConfig command.

For example, to configure ColumnStore to use the `cross_engine` user account to connect to the server at `127.0.0.1`:

```bash
$ sudo mcsSetConfig CrossEngineSupport Host 127.0.0.1
$ sudo mcsSetConfig CrossEngineSupport Port 3306
$ sudo mcsSetConfig CrossEngineSupport User cross_engine
$ sudo mcsSetConfig CrossEngineSupport Password cross_engine_passwd
```

{% hint style="info" %}
Please choose a password that meets your organization's password policies. If your MariaDB Community Server instance has a password validation plugin installed, then the password should also meet the configured requirements.
{% endhint %}

### Configure the S3 Storage Manager

MariaDB ColumnStore can use [S3-compatible storage](community-server-with-columnstore.md#s3-compatible-storage), but it is not required. S3-compatible storage must be configured before it can be used.

To configure ColumnStore to use S3-compatible storage, edit `/etc/columnstore/storagemanager.cnf`:

```
[ObjectStorage]
…
service = S3
…
[S3]
bucket = your_columnstore_bucket_name
endpoint = your_s3_endpoint
aws_access_key_id = your_s3_access_key_id
aws_secret_access_key = your_s3_secret_key
# iam_role_name = your_iam_role
# sts_region = your_sts_region
# sts_endpoint = your_sts_endpoint

[Cache]
cache_size = your_local_cache_size
path = your_local_cache_path
```

* The default local cache size is 2 GB.
* The default local cache path is `/var/lib/columnstore/storagemanager/cache`.
* Ensure that the local cache path has sufficient store space to store the local cache.
* The `bucket` option must be set to the name of the bucket that you created in the [Create an S3 Bucket](community-server-with-columnstore.md#create-an-s3-bucket) step.
* To use an IAM role, you must also uncomment and set `iam_role_name`, `sts_region`, and `sts_endpoint`.

### Start the ColumnStore Processes

The Community Server and ColumnStore processes can be started using the `systemctl` command. In case the processes were started during the installation process, use the restart command to ensure that the processes pick up the new configuration. Perform the following procedure.

1.  Start the MariaDB Community Server process and configure it to start automatically:

    ```bash
    $ sudo systemctl restart mariadb
    ```

    ```
    $ sudo systemctl enable mariadb
    ```
2.  Start the MariaDB ColumnStore processes and configure them to start automatically:

    ```bash
    $ sudo systemctl restart mariadb-columnstore
    ```

    ```
    $ sudo systemctl enable mariadb-columnstore
    ```

## Create User Accounts

For single-node ColumnStore deployments, only a single user account needs to be created.

### Create the Cross Engine Join User

The credentials for cross engine joins were previously configured in the [Cross Engine Joins](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/management/managing-columnstore-database-environment/configuring-columnstore-cross-engine-joins) section. The user account must also be created and granted the necessary privileges to access data.

1.  Connect to the server using [MariaDB Client](../../../clients-and-utilities/server-client-software/client-libraries/connect-and-query.md#mariadb-client) using the `root@localhost` user account:

    ```bash
    $ sudo mariadb
    ```
2.  Create the user account with the [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement:

    ```sql
    CREATE USER 'cross_engine'@'127.0.0.1'
       IDENTIFIED BY "cross_engine_passwd";
    ```

    ```
    CREATE USER 'cross_engine'@'localhost'
       IDENTIFIED BY "cross_engine_passwd";
    ```

{% hint style="info" %}
Please choose the same user name and password that was configured in the [Cross Engine Joins](community-server-with-columnstore.md#configure-cross-engine-joins) section.
{% endhint %}

1.  Grant the user account `SELECT` privileges on all databases with the [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md) statement:

    ```sql
    GRANT SELECT, PROCESS ON *.*
       TO 'cross_engine'@'127.0.0.1';
    ```

    ```
    GRANT SELECT, PROCESS ON *.*
       TO 'cross_engine'@'localhost';
    ```

## Bulk Import Data

Now that the ColumnStore system is running, you can bulk import your data.

### Import the Schema

Before data can be imported into the tables, the schema needs to be created.

1.  Connect to the server using [mariadb Client](../../../clients-and-utilities/mariadb-client/) using the `root@localhost` user account:

    ```bash
    $ sudo mariadb
    ```
2.  For each database that you are importing, create the database with the [CREATE DATABASE](../../../reference/sql-statements/data-definition/create/create-database.md) statement:

    ```sql
    CREATE DATABASE inventory;
    ```
3.  For each table that you are importing, create the table with the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement:

    ```sql
    CREATE TABLE inventory.products (
       product_name VARCHAR(11) NOT NULL DEFAULT '',
       supplier VARCHAR(128) NOT NULL DEFAULT '',
       quantity VARCHAR(128) NOT NULL DEFAULT '',
       unit_cost VARCHAR(128) NOT NULL DEFAULT ''
    ) ENGINE=Columnstore DEFAULT CHARSET=utf8;
    ```

### cpimport

MariaDB ColumnStore includes cpimport, which is a command-line utility that is designed to efficiently load data in bulk.

To import your data from a TSV (tab-separated values) file with cpimport:

```bash
$ sudo cpimport -s '\t' inventory products /tmp/inventory-products.tsv
```

### LOAD DATA INFILE

When data is loaded with the [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement, MariaDB ColumnStore loads the data using [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/architecture/columnstore-architectural-overview#cpimport), which is a command-line utility that is designed to efficiently load data in bulk.

To import your data from a TSV (tab-separated values) file with [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement:

```sql
LOAD DATA INFILE '/tmp/inventory-products.tsv'
INTO TABLE inventory.products;
```

### Import from Remote Database

MariaDB ColumnStore can also import data directly from a remote database. A simple method is to query the table using the [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement, and then pipe the results into cpimport, which is a command-line utility that is designed to efficiently load data in bulk.

To import your data from a remote MariaDB database:

```bash
$ mariadb --quick \
   --skip-column-names \
   --execute="SELECT * FROM inventory.products" \
   | cpimport -s '\t' inventory products
```

## Configure the Linux Security Module

If you stopped the Linux Security Module (LSM) during installation, you can restart the module and configure.

The specific steps to configure the security module depend on the operating system.

### Configure SELinux (RHEL, CentOS)

We set SELinux to permissive mode in the [SELinux](community-server-with-columnstore.md#selinux-rhel-centos) section, but we have to create an SELinux policy for ColumnStore before re-enabling it. This will ensure that SELinux does not interfere with ColumnStore's functionality. A policy can be generated while SELinux is still in permissive mode using the `audit2allow` command.

1.  To configure SELinux, you have to install the packages required for `audit2allow`.

    On RHEL 7 and CentOS 7, install the following:

    ```bash
    $ sudo yum install policycoreutils policycoreutils-python
    ```

    On RHEL 8, install the following:

    ```bash
    $ sudo yum install policycoreutils python3-policycoreutils policycoreutils-python-utils
    ```
2. Allow the system to run under load for a while to generate SELinux audit events.
3.  After the system has taken some load, generate an SELinux policy from the audit events using `audit2allow`:

    ```bash
    $ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local
    ```

    If no audit events were found, this will print the following:

    ```bash
    $ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local
    ```

    ```
    Nothing to do
    ```
4.  If audit events were found, the new SELinux policy can be loaded using `semodule`:

    ```bash
    $ sudo semodule -i mariadb_local.pp
    ```
5.  Set SELinux to enforcing mode by setting `SELINUX=enforcing` in `/etc/selinux/config`:

    ```editorconfig
    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #     enforcing - SELinux security policy is enforced.
    #     permissive - SELinux prints warnings instead of enforcing.
    #     disabled - No SELinux policy is loaded.
    SELINUX=enforcing
    # SELINUXTYPE= can take one of three values:
    #     targeted - Targeted processes are protected,
    #     minimum - Modification of targeted policy. Only selected processes are protected.
    #     mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ```
6. Reboot the system.
7.  Confirm that SELinux is in enforcing mode using `getenforce`:

    ```bash
    $ sudo getenforce
    ```

### Configure AppArmor (Debian, Ubuntu)

We disabled AppArmor in the [AppArmor](community-server-with-columnstore.md#apparmor-debian-ubuntu) section, but we have to create an AppArmor profile for ColumnStore before re-enabling it. This will ensure that AppArmor does not interfere with ColumnStore's functionality.

For information on how to create a profile, see [How to create an AppArmor Profile](https://ubuntu.com/tutorials/beginning-apparmor-profile-development) on ubuntu.com.

## Administration

ColumnStore has several components. Each of those components needs to be administered.

### Community Server Administration

MariaDB Community Server uses `systemctl` to start and stop the server processes:

<table><thead><tr><th width="234.148193359375">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb</code></td></tr></tbody></table>

### ColumnStore Administration

MariaDB ColumnStore uses `systemctl` to start and stop the ColumnStore processes:

<table><thead><tr><th width="228.22216796875">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb-columnstore</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb-columnstore</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb-columnstore</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb-columnstore</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb-columnstore</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb-columnstore</code></td></tr></tbody></table>

## Testing

When you have MariaDB ColumnStore up and running, you should test it to ensure that it is in working order and that there were not any issues during startup.

### Checking Server Status

1.  Connect to the server using [mariadb Client](../../../clients-and-utilities/mariadb-client/) using the `root@localhost` user account:

    ```bash
    $ sudo mariadb
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 38
    Server version: 10.6.21-MariaDB MariaDB Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
