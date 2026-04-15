# Step 3: Start and Configure MariaDB Enterprise Server

## Overview

This page details step 3 of the 4-step procedure "[Deploy HTAP Topology](./)".

This step starts and configures MariaDB Enterprise Server and MariaDB Enterprise ColumnStore 23.10.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Stop the Enterprise ColumnStore Services

The installation process might have started some of the ColumnStore services. The services should be stopped prior to making configuration changes.

1. On each Enterprise ColumnStore node, stop the MariaDB Enterprise Server service:

```bash
$ sudo systemctl stop mariadb
```

2. On each Enterprise ColumnStore node, stop the MariaDB Enterprise ColumnStore service:

```bash
$ sudo systemctl stop mariadb-columnstore
```

3. On each Enterprise ColumnStore node, stop the CMAPI service:

```bash
$ sudo systemctl stop mariadb-columnstore-cmapi
```

## Configure Enterprise ColumnStore

**On each Enterprise ColumnStore node**, configure Enterprise Server.

<table><thead><tr><th width="269.70361328125">Connector</th><th>MariaDB Connector/R2DBC</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_do_db">binlog_do_db</a></td><td>Set this to the name of the database to replicate from InnoDB to ColumnStore.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format">binlog_format</a></td><td>Set this to STATEMENT for HTAP.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">character_set_server</a></td><td>Set this system variable to utf8</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">collation_server</a></td><td>Set this system variable to utf8_general_ci</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-insert-select.md#batch-insert-mode">loose-columnstore_use_import_for_batchinsert</a></td><td>Set this system variable to ALWAYS to always use cpimport for LOAD DATA INFILE and INSERT...SELECT statements.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid.md#gtid_strict_mode">gtid_strict_mode</a></td><td>Set this system variable to ON.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin">log_bin</a></td><td>Set this option to the file you want to use for the Binary Log. Setting this option enables binary logging.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_slave_updates">log_slave_updates</a></td><td>Set this system variable to ON.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_rewrite_db">replicate_rewrite_db</a></td><td>Set this option to the file you want to use for the Relay Logs. Setting this option enables relay logging.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_wild_do_table">replicate_wild_do_table</a></td><td>Set this option to the file you want to use to index Relay Log filenames.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id">server_id</a></td><td>Sets the numeric Server ID for this MariaDB Enterprise Server. The value set on this option must be unique to each node.</td></tr></tbody></table>

### Example Configuration

```
[mariadb]
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci

# Replication Configuration (HTAP Server)
server_id                     = 1
log_bin                       = mariadb-bin
binlog_format                 = STATEMENT
log_slave_updates             = OFF
loose-columnstore_replication_slave = ON

# HTAP filtering rules

# Transactions replicate from same server
replicate_same_server_id = ON

# Only write queries that touch 'innodb_db' to the binary log
binlog_do_db = innodb_db

# Rewrite innodb_db to columnstore_db prior to applying transaction
replicate_rewrite_db = innodb_db->columnstore_db

# Only replicate tables that begin with "htap"
replicate_wild_do_table = columnstore_db.htap%
```

{% hint style="warning" %}
The `loose-` prefix is required for ColumnStore system variables in the configuration file. Without it, MariaDB Server will fail to start if the ColumnStore plugin is not installed or has been removed.
{% endhint %}

## Configure the S3 Storage Manager

Configure Enterprise ColumnStore S3 Storage Manager to use S3-compatible storage by editing the `/etc/columnstore/storagemanager.cnf` configuration file:

```
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

The S3-compatible object storage options are configured under \[S3]:

* The bucket option must be set to the name of the bucket that you created in "Create an S3 Bucket".
* The endpoint option must be set to the endpoint for the S3-compatible object storage.
* The `aws_access_key_id and aws_secret_access_key` options must be set to the access key ID and secret access key for the S3-compatible object storage.
* To use a specific IAM role, you must uncomment and set `iam_role_name, sts_region, and sts_endpoint`.
* To use the IAM role assigned to an EC2 instance, you must uncomment `ec2_iam_mode=enabled`.

The local cache options are configured under \[Cache]:

* The `cache_size` option is set to 2 GB by default.
* The path option is set to `/var/lib/columnstore/storagemanager/cache` by default.
* Ensure that the specified path has sufficient storage space for the specified cache size.

## Start the Enterprise ColumnStore Services

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

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## Create User Accounts

The HTAP topology requires several user accounts.

### Create the Utility User

Enterprise ColumnStore requires a mandatory utility user account. By default, it connects to the server using the root user with no password. MariaDB Enterprise Server 10.6 will reject this login attempt by default, so you will need to configure Enterprise ColumnStore to use a different user account and password and create this user account on Enterprise Server.

1. On the Enterprise ColumnStore node, create the user account with the CREATE USER statement:

```sql
CREATE USER 'util_user'@'127.0.0.1'
IDENTIFIED BY 'util_user_passwd';
```

2. On the Enterprise ColumnStore node, grant the user account SELECT privileges on all databases with the GRANT statement:

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

For details about how to encrypt the password, see "[Credentials Management for MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/security/enterprise-columnstore-credentials-management)".

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, then the password should also meet the configured requirements.

### Create the Replication User

Enterprise HTAP uses [MariaDB Replication](../../../ha-and-performance/standard-replication/) to replicate writes between InnoDB tables and ColumnStore tables.

Create a replication user and grant it the required privileges:

1. Use the [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement to create replication users for each replica server:

```sql
CREATE USER 'repl'@'localhost' IDENTIFIED BY 'passwd';
```

2. Grant the user account several global privileges with the [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md) statement.

```sql
GRANT REPLICA MONITOR,
   REPLICATION REPLICA
ON *.* TO 'repl'@'localhost';
```

## Configure MariaDB Replication

1. Set the GTID position by setting the [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) system variable.\
   If this is a new deployment, then it would be set to the empty string:

```sql
SET GLOBAL gtid_slave_pos='';
```

2. Use the CHANGE MASTER TO statement to configure the server to replicate from itself starting from this position:

```sql
CHANGE MASTER TO
   MASTER_HOST='localhost',
   MASTER_USER='htap_replication',
   MASTER_PASSWORD='passwd',
   MASTER_USE_GTID=slave_pos;
```

3. Start replication using the START REPLICA statement:

```sql
START REPLICA;
```

4. Confirm that replication is working using the SHOW REPLICA STATUS statement:

```sql
SHOW REPLICA STATUS;
```

## Configure Linux Security Modules (LSM)

The specific steps to configure the security module depend on the operating system.

### Configure SELinux (CentOS, RHEL)

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

```bash
$ sudo semodule -i mariadb_local.pp
```

5. Set SELinux to enforcing mode by setting SELINUX=enforcing in /etc/selinux/config.

For example, the file will usually look like this after the change:

```systemd
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

## Configure AppArmor (Ubuntu)

For information on how to create a profile, see [How to create an AppArmor Profile](https://ubuntu.com/tutorials/beginning-apparmor-profile-development) on ubuntu.com.

## Next Step

Navigation in the procedure "Deploy HTAP Topology".

This page was step 3 of 4.

Next: Step 4: Test MariaDB Enterprise Server.

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
