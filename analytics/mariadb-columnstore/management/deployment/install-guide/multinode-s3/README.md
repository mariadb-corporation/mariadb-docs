---
description: >-
  This guide provides steps for deploying a multi-node S3 ColumnStore, setting
  up the environment, installing the software, and bulk importing data for
  online analytical processing (OLAP) workloads.
---

# Multi-Node S3

This procedure describes the deployment of a Multi-Node Enterprise ColumnStore topology with Object Storage (S3). This High Availability (HA) configuration delivers production-grade analytics with fault tolerance and scalable storage by leveraging S3-compatible object storage for data and a distributed proxy layer.

The topology consists of:

* One or more MariaDB MaxScale nodes to monitor health and route queries.
* An odd number of ColumnStore nodes (minimum of 3) running MariaDB Enterprise Server, Enterprise ColumnStore, and the Cluster Management API (CMAPI).
* S3-compatible object storage for data.
* Shared local storage (e.g., NFS, EBS Multi-Attach) for the Storage Manager metadata directory.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

## Procedure

{% stepper %}
{% step %}
### Prepare ColumnStore Nodes

MariaDB Enterprise ColumnStore performs best with specific Linux kernel optimizations. Perform these actions on each ColumnStore node.

#### Optimize Linux Kernel Parameters

MariaDB Enterprise ColumnStore performs best with Linux kernel optimizations.

On each server to host an Enterprise ColumnStore node, optimize the kernel:

1. Set the relevant kernel parameters in a sysctl configuration file. To ensure proper change management, use an Enterprise ColumnStore-specific configuration file.

Create a `/etc/sysctl.d/90-mariadb-enterprise-columnstore.conf` file:

```apache
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

2. Use the sysctl command to set the kernel parameters at runtime

```bash
$ sudo sysctl --load=/etc/sysctl.d/90-mariadb-enterprise-columnstore.conf
```

#### Temporarily Configure Linux Security Modules (LSM)

The Linux Security Modules (LSM) should be temporarily disabled on each Enterprise ColumnStore node during installation.

The LSM will be configured and re-enabled later in this deployment procedure.

The steps to disable the LSM depend on the specific LSM used by the operating system.

**CentOS / RHEL**

SELinux must be set to permissive mode before installing MariaDB Enterprise ColumnStore.

To set SELinux to permissive mode:

1. Set SELinux to permissive mode:

```bash
$ sudo setenforce permissive
```

2. Set SELinux to permissive mode by setting SELINUX=permissive in /etc/selinux/config.

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

3. Confirm that SELinux is in permissive mode:

```bash
$ sudo getenforce
Permissive
```

SELinux will be configured and re-enabled later in this deployment procedure. This configuration is not persistent. If you restart the server before configuring and re-enabling SELinux later in the deployment procedure, you must reset the enforcement to permissive mode.

**Debian / Ubuntu**

AppArmor must be disabled before installing MariaDB Enterprise ColumnStore.

1. Disable AppArmor:

```bash
$ sudo systemctl disable apparmor
```

2. Reboot the system.
3. Confirm that no AppArmor profiles are loaded using aa-status:

```bash
$ sudo aa-status
```

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

AppArmor will be configured and re-enabled later in this deployment procedure.

#### Configure Character Encoding

When using MariaDB Enterprise ColumnStore, it is recommended to set the system's locale to UTF-8.

1. On RHEL 8, install additional dependencies:

```bash
$ sudo yum install glibc-locale-source glibc-langpack-en
```

2. Set the system's locale to en\_US.UTF-8 by executing localedef:

```bash
$ sudo localedef -i en_US -f UTF-8 en_US.UTF-8
```

#### Create an S3 Bucket

If you want to use S3-compatible storage, it is important to create the S3 bucket before you start ColumnStore. If you already have an S3 bucket, confirm that the bucket is empty.

S3 bucket configuration will be performed later in this procedure.
{% endstep %}

{% step %}
### Install Enterprise ColumnStore

Retrieve your Customer Download Token from the MariaDB Customer Portal and perform these steps on each ColumnStore node.

#### Retrieve Download Token

MariaDB Corporation provides package repositories for CentOS / RHEL (YUM) and Debian / Ubuntu (APT). A download token is required to access the MariaDB Enterprise Repository.

Customer Download Tokens are customer-specific and are available through the MariaDB Customer Portal.

To retrieve the token for your account:

1. Navigate to [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/)
2. Log in.
3. Copy the Customer Download Token.

Substitute your token for `CUSTOMER_DOWNLOAD_TOKEN` when configuring the package repositories.

#### Set Up Repository

1. On each Enterprise ColumnStore node, install the prerequisites for downloading the software from the Web.\
   **Install on CentOS / RHEL (YUM):**

```bash
$ sudo yum install curl
```

**Install on Debian / Ubuntu (APT):**

```bash
$ sudo apt install curl apt-transport-https
```

2. On each Enterprise ColumnStore node, configure package repositories and specify Enterprise Server:

```bash
$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
$ echo "${checksum}  mariadb_es_repo_setup" \
      
 | sha256sum -c -
```

```bash
$ chmod +x mariadb_es_repo_setup
```

```bash
$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
      --skip-maxscale \
      --skip-tools \
      --mariadb-server-version="11.4"
```

_Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ _Versions_ _section at the bottom of the_ _MariaDB Package Repository Setup and Usage_ _page. Substitute `${checksum}` in the example above with the latest checksum._

#### Install Enterprise ColumnStore

**Install additional dependencies:**

Install on CentOS / RHEL (YUM)

```bash
$ sudo yum install epel-release

$ sudo yum install jemalloc
```

Install of Debian 10 and Ubuntu 20.04 (APT):

```bash
$ sudo apt install libjemalloc2
```

Install on Debian 9 and Ubuntu 18.04 (APT):

```bash
$ sudo apt install libjemalloc1
```

**Install MariaDB Enterprise Server and MariaDB Enterprise ColumnStore:**

Install on CentOS / RHEL (YUM):

```bash
$ sudo yum install MariaDB-server \
   MariaDB-backup \
   MariaDB-shared \
   MariaDB-client \
   MariaDB-columnstore-engine
```

Install on Debian / Ubuntu (APT):

```bash
$ sudo apt install mariadb-server \
   mariadb-backup \
   libmariadb3 \
   mariadb-client \
   mariadb-plugin-columnstore
```
{% endstep %}

{% step %}
### Start and Configure Enterprise ColumnStore

#### Configure Enterprise ColumnStore

Mandatory system variables and options for Single-Node Enterprise ColumnStore include:

<table><thead><tr><th width="342">Connector</th><th>MariaDB Connector/R2DBC</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server">character_set_server</a></td><td>Set this system variable to <code>utf8</code></td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_server">collation_server</a></td><td>Set this system variable to <code>utf8_general_ci</code></td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-insert-select.md#batch-insert-mode">loose-columnstore_use_import_for_batchinsert</a></td><td>Set this system variable to <code>ALWAYS</code> to always use <code>cpimport</code> for <a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md">LOAD DATA INFILE</a> and <a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md">INSERT...SELECT</a> statements.</td></tr></tbody></table>

{% hint style="warning" %}
The `loose-` prefix is required for ColumnStore system variables in the configuration file. Without it, MariaDB Server will fail to start if the ColumnStore plugin is not installed or has been removed.
{% endhint %}

#### Example Configuration

```ini
[mariadb]
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci
```

#### Configure the S3 Storage Manager

Configure Enterprise ColumnStore S3 Storage Manager to use S3-compatible storage by editing the `/etc/columnstore/storagemanager.cnf` configuration file:

```apache
[ObjectStorage]
…
service = S3
…
[S3]
bucket                = your_columnstore_bucket_name
endpoint              = your_s3_endpoint
aws_access_key_id     = your_s3_access_key_id
aws_secret_access_key = your_s3_secret_key
# iam_role_name       = your_iam_role
# sts_region          = your_sts_region
# sts_endpoint        = your_sts_endpoint
# ec2_iam_mode        = enabled

[Cache]
cache_size = your_local_cache_size
path       = your_local_cache_path
```

The S3-compatible object storage options are configured under `[S3]`:

* The `bucket` option must be set to the name of the bucket that you created in "Create an S3 Bucket".
* The `endpoint` option must be set to the endpoint for the S3-compatible object storage.
* The `aws_access_key_id` and `aws_secret_access_key` options must be set to the access key ID and secret access key for the S3-compatible object storage.
* To use a specific IAM role, you must uncomment and set `iam_role_name`, `sts_region`, and `sts_endpoint`.
* To use the IAM role assigned to an EC2 instance, you must uncomment `ec2_iam_mode=enabled`.

The local cache options are configured under \[Cache]:

* The `cache_size` option is set to 2 GB by default.
* The `path` option is set to `/var/lib/columnstore/storagemanager/cache` by default.

Ensure that the specified path has sufficient storage space for the specified cache size.

#### Start the Enterprise ColumnStore Services

Start and enable the MariaDB Enterprise Server service, so that it starts automatically upon reboot:

```bash
$ sudo systemctl start mariadb
$ sudo systemctl enable mariadb
```

Start and enable the MariaDB Enterprise ColumnStore service, so that it starts automatically upon reboot:

```bash
$ sudo systemctl start mariadb-columnstore
$ sudo systemctl enable mariadb-columnstore
```

#### Create the Utility User

Enterprise ColumnStore requires a mandatory utility user account to perform cross-engine joins and similar operations.

1. Create the user account with the [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) statement:

```sql
CREATE USER 'util_user'@'127.0.0.1'
IDENTIFIED BY 'util_user_passwd';
```

2. Grant the user account `SELECT` privileges on all databases with the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement:

```sql
GRANT SELECT, PROCESS ON *.*
TO 'util_user'@'127.0.0.1';
```

3. Configure Enterprise ColumnStore to use the utility user:

```bash
$ sudo mcsSetConfig CrossEngineSupport Host 127.0.0.1
$ sudo mcsSetConfig CrossEngineSupport Port 3306
$ sudo mcsSetConfig CrossEngineSupport User util_user
```

4. Set the password:

```bash
$ sudo mcsSetConfig CrossEngineSupport Password util_user_passwd
```

For details about how to encrypt the password, see "[Credentials Management for MariaDB Enterprise ColumnStore](../../../../security/enterprise-columnstore-credentials-management.md)".

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, then the password should also meet the configured requirements.

#### Configure Linux Security Modules (LSM)

The specific steps to configure the security module depend on the operating system.

**Configure SELinux (CentOS, RHEL)**

Configure SELinux for Enterprise ColumnStore:

1. To configure SELinux, you have to install the packages required for audit2allow.\
   On CentOS 7 and RHEL 7, install the following:

```bash
$ sudo yum install policycoreutils policycoreutils-python
```

On RHEL 8, install the following:

```bash
$ sudo yum install policycoreutils python3-policycoreutils policycoreutils-python-utils
```

2. Allow the system to run under load for a while to generate SELinux audit events.
3. After the system has taken some load, generate an SELinux policy from the audit events using audit2allow:

```bash
$ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local
```

If no audit events were found, this will print the following:

```bash
$ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local

Nothing to do
```

4. If audit events were found, the new SELinux policy can be loaded using semodule:

```
$ sudo semodule -i mariadb_local.pp
```

5. Set SELinux to enforcing mode by setting `SELINUX=enforcing` in `/etc/selinux/config`.

For example, the file will usually look like this after the change:

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

6. Set SELinux to enforcing mode:

```bash
$ sudo setenforce enforcing
```

**Configure AppArmor (Ubuntu)**

For information on how to create a profile, see [How to create an AppArmor Profile](https://ubuntu.com/tutorials/beginning-apparmor-profile-development#1-overview) on ubuntu.com.
{% endstep %}

{% step %}
### Test Enterprise ColumnStore

#### Test S3 Connection

MariaDB Enterprise ColumnStore 23.10 includes a testS3Connection command to test the S3 configuration, permissions, and connectivity.

On each Enterprise ColumnStore node, test the S3 configuration:

```bash
$ sudo testS3Connection
```

```
StorageManager[26887]: Using the config file found at /etc/columnstore/storagemanager.cnf
StorageManager[26887]: S3Storage: S3 connectivity & permissions are OK
S3 Storage Manager Configuration OK
```

If the `testS3Connection` command does not return `OK`, investigate the S3 configuration.

#### Test Local Connection

Connect to the server using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) using the `root@localhost` user account:

```bash
$ sudo mariadb
```

```sql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

#### Test ColumnStore Plugin Status

Query [information\_schema.PLUGINS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and confirm that the ColumnStore storage engine plugin is `ACTIVE`:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS
FROM information_schema.PLUGINS
WHERE PLUGIN_LIBRARY LIKE 'ha_columnstore%';
```

```sql
+---------------------+---------------+
| PLUGIN_NAME         | PLUGIN_STATUS |
+---------------------+---------------+
| Columnstore         | ACTIVE        |
| COLUMNSTORE_COLUMNS | ACTIVE        |
| COLUMNSTORE_TABLES  | ACTIVE        |
| COLUMNSTORE_FILES   | ACTIVE        |
| COLUMNSTORE_EXTENTS | ACTIVE        |
+---------------------+---------------+
```

#### Test ColumnStore Table Creation

1. Create a test database, if it does not exist:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

2. Create a ColumnStore table:

```sql
CREATE TABLE IF NOT EXISTS test.contacts (
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
) ENGINE=ColumnStore;
```

3. Add sample data into the table:

```sql
INSERT INTO test.contacts (first_name, last_name, email)
   VALUES
   ("Kai", "Devi", "kai.devi@example.com"),
   ("Lee", "Wang", "lee.wang@example.com");
```

4. Read data from table:

```sql
SELECT * FROM test.contacts;

+------------+-----------+----------------------+
| first_name | last_name | email                |
+------------+-----------+----------------------+
| Kai        | Devi      | kai.devi@example.com |
| Lee        | Wang      | lee.wang@example.com |
+------------+-----------+----------------------+
```

#### Test Cross Engine Join

1. Create an InnoDB table:

```sql
CREATE TABLE test.addresses (
   email VARCHAR(100),
   street_address VARCHAR(255),
   city VARCHAR(100),
   state_code VARCHAR(2)
) ENGINE = InnoDB;
```

2. Add data to the table:

```sql
INSERT INTO test.addresses (email, street_address, city, state_code)
   VALUES
   ("kai.devi@example.com", "1660 Amphibious Blvd.", "Redwood City", "CA"),
   ("lee.wang@example.com", "32620 Little Blvd", "Redwood City", "CA");
```

3. Perform a cross-engine join:

```sql
SELECT name AS "Name", addr AS "Address"
FROM (SELECT CONCAT(first_name, " ", last_name) AS name,
   email FROM test.contacts) AS contacts
INNER JOIN (SELECT CONCAT(street_address, ", ", city, ", ", state_code) AS addr,
   email FROM test.addresses) AS addr
WHERE  contacts.email = addr.email;
```

```sql
+----------+-----------------------------------------+
| Name     | Address                                 |
+----------+-----------------------------------------+
| Kai Devi | 1660 Amphibious Blvd., Redwood City, CA |
| Lee Wang | 32620 Little Blvd, Redwood City, CA     |
+----------+-----------------------------------------+

+-------------------+-------------------------------------+
| Name              | Address                             |
+-------------------+-------------------------------------+
| Walker Percy      | 500 Thomas More Dr., Covington, LA  |
| Flannery O'Connor | 300 Tarwater Rd., Milledgeville, GA |
+-------------------+-------------------------------------+
```
{% endstep %}

{% step %}
### Bulk Import of Data

#### Import the Schema

Before data can be imported into the tables, create a matching schema.

**On the primary server**, create the schema:

1. For each database that you are importing, create the database with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

```sql
CREATE DATABASE inventory;
```

2. For each table that you are importing, create the table with the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table) statement:

```sql
CREATE TABLE inventory.products (
   product_name VARCHAR(11) NOT NULL DEFAULT '',
   supplier VARCHAR(128) NOT NULL DEFAULT '',
   quantity VARCHAR(128) NOT NULL DEFAULT '',
   unit_cost VARCHAR(128) NOT NULL DEFAULT ''
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

#### Import the Data

Enterprise ColumnStore supports multiple methods to import data into ColumnStore tables.

#### cpimport

MariaDB Enterprise ColumnStore includes [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server run [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport):

```bash
$ sudo cpimport -s '\t' inventory products /tmp/inventory-products.tsv
```

#### LOAD DATA INFILE

When data is loaded with the LOAD DATA INFILE statement, MariaDB Enterprise ColumnStore loads the data using [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server use LOAD DATA INFILE statement:

```sql
LOAD DATA INFILE '/tmp/inventory-products.tsv'
INTO TABLE inventory.products;
```

#### Import from Remote Database

MariaDB Enterprise ColumnStore can also import data directly from a remote database. A simple method is to query the table using the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement, and then pipe the results into [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility that is designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a remote MariaDB database:

```bash
$ mariadb --quick \
   --skip-column-names \
   --execute="SELECT * FROM inventory.products" \
   | cpimport -s '\t' inventory products
```
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
