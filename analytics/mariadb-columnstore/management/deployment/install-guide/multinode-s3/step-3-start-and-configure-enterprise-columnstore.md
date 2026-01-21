---
description: 'Step 3: Start and Configure Enterprise ColumnStore'
---

# Step 3: Start and Configure Enterprise ColumnStore

## Overview

This page details step 3 of a 5-step procedure for deploying [Single-Node Enterprise ColumnStore with Object storage](broken-reference/).

This step starts and configures MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Configure Enterprise ColumnStore

Mandatory system variables and options for Single-Node Enterprise ColumnStore include:

<table><thead><tr><th width="342">Connector</th><th>MariaDB Connector/R2DBC</th></tr></thead><tbody><tr><td><a href="broken-reference/">character_set_server</a></td><td>Set this system variable to <code>utf8</code></td></tr><tr><td><a href="broken-reference/">collation_server</a></td><td>Set this system variable to <code>utf8_general_ci</code></td></tr><tr><td>columnstore_use_import_for_batchinsert</td><td>Set this system variable to <code>ALWAYS</code> to always use <code>cpimport</code> for <a href="broken-reference/">LOAD DATA INFILE</a> and <a href="broken-reference/">INSERT...SELECT</a> statements.</td></tr></tbody></table>

### Example Configuration

```
[mariadb]
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci
```

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

## Create the Utility User

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

For details about how to encrypt the password, see "[Credentials Management for MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/managing-columnstore/enterprise-columnstore-credentials-management)".

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, then the password should also meet the configured requirements.

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

## Configure AppArmor (Ubuntu)

For information on how to create a profile, see [How to create an AppArmor Profile](https://ubuntu.com/tutorials/beginning-apparmor-profile-development#1-overview) on ubuntu.com.

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Object storage deployment procedure:

This page was step 3 of 5.

[Next: Step 4: Test MariaDB Enterprise ColumnStore.](step-4-test-enterprise-columnstore.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
