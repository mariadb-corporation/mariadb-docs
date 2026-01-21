---
description: >-
  This guide covers typical use cases for the S3 engine, such as archiving
  inactive tables, and details supported operations like ALTER TABLE and SELECT.
---

# Using the S3 Storage Engine

The [S3 storage engine](./) is read only and allows one to archive MariaDB tables in Amazon S3, or any third-party public or private cloud that implements S3 API (of which there are many), but still have them accessible for reading in MariaDB.

## Installing the Plugin

The S3 storage engine is [gamma maturity](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria), so the following step can be omitted.

On earlier releases, when it was [alpha maturity](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria), it does not load by default on a stable release of the server due to the default value of the [plugin\_maturity](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity) variable. Set to `alpha` (or below) in your config file to permit installation of the plugin:

```ini
[mariadbd]
plugin-maturity = alpha
```

and restart the server.

Now [install the plugin library](../../../reference/plugins/plugin-overview.md#installing-a-plugin), for example:

```sql
INSTALL SONAME 'ha_s3';
```

If the library is not available, for example:

```sql
INSTALL SONAME 'ha_s3';
ERROR 1126 (HY000): Can't open shared library '/var/lib/mysql/lib64/mysql/plugin/ha_s3.so' 
  (errno: 13, cannot open shared object file: No such file or directory)
```

you may need to install a separate package for the S3 storage engine, for example:

```bash
shell> yum install MariaDB-s3-engine
```

or for Debian/Ubuntu

```bash
shell> apt install mariadb-plugin-s3
```

## Creating an S3 Table

As S3 tables are read only, one cannot create a S3 table with `CREATE TABLE`. You should use instead use `ALTER TABLE old_table ENGINE=S3` to convert an existing table to be stored on S3.

## Moving Data to S3

To move data from an existing table to S3, you can run:

```sql
ALTER TABLE old_table ENGINE=S3 COMPRESSION_ALGORITHM=zlib
```

To get data back to a 'normal' table, you can do:

```sql
ALTER TABLE s3_table ENGINE=INNODB
```

## New Options for [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/)

* `S3_BLOCK_SIZE` : Set to 4M as default. This is the block size for all index and data pages stored in S3.
* `COMPRESSION_ALGORITHM` : Set to 'none' as default. Which compression algorithm to use for block stored in S3. Options are: `none` or `zlib`.

[ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) can be used on S3 tables as normal to add columns or change column definitions.

## mariadbd Startup Options for S3

To be able to use S3 for storage one _**must**_ define how to access S3 and where data are stored in S3:

* [s3\_access\_key](s3-storage-engine-system-variables.md#s3_access_key): The AWS access key to access your data
* [s3\_secret\_key](s3-storage-engine-system-variables.md#s3_secret_key): The AWS secret key to access your data
* [s3\_bucket](s3-storage-engine-system-variables.md#s3_bucket): The AWS bucket where your data should be stored. All MariaDB table data is stored in this bucket.
* [s3\_region](s3-storage-engine-system-variables.md#s3_region): The AWS region where your data should be stored.

For compatibility tweaks with different providers:

* [s3\_provider](s3-storage-engine-system-variables.md#s3_provider): Enable S3 provider specific compatibility tweaks. "Default", "Amazon", or "Huawei". From [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes).

If you are using an S3 service that is using HTTP to connect (like) you also need the set the following variables:

* [s3\_port](s3-storage-engine-system-variables.md#s3_port): Port number to connect to (0 means use default)
* [s3\_use\_http](s3-storage-engine-system-variables.md#s3_use_http): If true, force use of HTTP protocol

If you are going to use a primary-replica setup, you should look at the following variables:

* [s3\_replicate\_alter\_as\_create\_select](s3-storage-engine-system-variables.md#s3-replicate-alter-as-create-select): When converting an S3 table to local table, log all rows in binary log. Defaults to `TRUE`. This allows the replica to replicate `CREATE TABLE .. SELECT FROM s3_table` even it the replica doesn't have access to the original `s3_table`.
* [s3\_slave\_ignore\_updates](s3-storage-engine-system-variables.md#s3-slave-ignore-updates): Should be set if primary and replica share the same S3 instance. This tells the replica that it can ignore any updates to the S3 tables as they are already applied on the primary. Defaults to `FALSE`.

The above defaults assume that the primary and replica don't share the same S3 instance.

Other, less critical options, are:

* [s3\_host\_name](s3-storage-engine-system-variables.md#s3_host_name): Hostname for the S3 service. "s3.amazonaws.com", Amazon S3 service, by default.
* [s3\_protocol\_version](s3-storage-engine-system-variables.md#s3_protocol_version): Protocol used to communication with S3. One of "Auto", "Amazon" or "Original" where "Auto" is the default. If you get errors like "8 Access Denied" when you are connecting to another service provider, then try to change this option. The reason for this variable is that Amazon has changed some parts of the S3 protocol since they originally introduced it but other service providers are still using the original protocol.
* [s3\_block\_size](s3-storage-engine-system-variables.md#s3_block_size): Set to 4M as default. This is the default block size for a table, if not specified in [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md).
* [s3\_pagecache\_buffer\_size](s3-storage-engine-system-variables.md#s3_pagecache_buffer_size): Default 128M. The size of the buffer used for data and index blocks for S3 tables. Increase this to get better index handling (for all reads and multiple writes) to as much as you can afford.
* [s3\_ssl\_no\_verify](s3-storage-engine-system-variables.md#s3_ssl_no_verify): If true, SSL certificate verification for the S3 endpoint is disabled. From [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes).
* [ss3\_no\_content\_type](s3-storage-engine-system-variables.md#s3_no_content_type): If true (false is default), disables the Content-Type header, required for some providers. From [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes).

Last some options you probably don't have to ever touch:

* [s3\_pagecache\_age\_threshold](s3-storage-engine-system-variables.md#s3_pagecache_age_threshold) : Default 300: This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in the page cache.
* [s3\_pagecache\_division\_limit](s3-storage-engine-system-variables.md#s3_pagecache_division_limit): Default 100. The minimum percentage of warm blocks in key cache.
* [s3\_pagecache\_file\_hash\_size](s3-storage-engine-system-variables.md#s3_pagecache_file_hash_size): Default 512. Number of hash buckets for open files. If you have a lot of S3 files open you should increase this for faster flush of changes. A good value is probably 1/10 of number of possible open S3 files.
* [s3\_debug](s3-storage-engine-system-variables.md#s3_debug): Default 0. Generates a trace file from libmarias3 on stderr (mysqld.err) for debugging the S3 protocol.

## Typical my.cnf Entry for connecting to Amazon S3 service

```
[mariadb]
s3=ON
s3-bucket=mariadb
s3-access-key=xxxx
s3-secret-key=xxx
s3-region=eu-north-1
s3-host-name=s3.amazonaws.com
# The following is useful if you want to use minio as a S3 server. (https://min.io/)
#s3-port=9000
#s3-use-http=ON

# Primary and replica share same S3 tables.
s3-slave-ignore-updates=1

[aria_s3_copy]
s3-bucket=mariadb
s3-access-key=xxxx
s3-secret-key=xxx
s3-region=eu-north-1
s3-host-name=s3.amazonaws.com
# The following is useful if you want to use minio as a S3 server. (https://min.io/)
#s3-port=9000
#s3-use-http=ON
```

## Typical my.cnf entry for connecting to a [minio](https://min.io) S3 server

```
[mariadb]
s3=ON
s3-host-name="127.0.0.1"
s3-bucket=storage-engine
s3-access-key=minio
s3-secret-key=minioadmin
s3-port=9000
s3-use-http=ON

[aria_s3_copy]
s3=ON
s3-host-name="127.0.0.1"
s3-bucket=storage-engine
s3-access-key=minio
s3-secret-key=minioadmin
s3-port=9000
s3-use-http=ON
```

## Typical Usage Case for S3 Tables

The typical use case would be that there exists tables that after some time would become fairly inactive, but are still important so that they can not be removed. In that case, an option is to move such a table to an archiving service, which is accessible through an S3 API.

Notice that S3 means the Cloud Object Storage API defined by Amazon AWS. Often the whole of Amazon’s Cloud Object Storage is referred to as S3. In the context of the S3 archive storage engine, it refers to the API itself that defines how to store objects in a cloud service,\
being it Amazon’s or someone else’s. OpenStack for example provides an S3 API for storing objects.

The main benefit of storing things in an S3 compatible storage is that the cost of storage is much cheaper than many other alternatives. Many S3 implementations also provide reliable long-term storage.

## Operations Allowed on S3 Tables

* [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) S3 supports all types, keys and other options that are supported by the [Aria](../aria/aria-storage-engine.md) engine. One can also perform [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) on an S3 table to add or modify columns etc.
* [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md)
* [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) Any SELECT operations you can perform on a normal table should work with an S3 table.
* [SHOW TABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-tables.md) will show all tables that exist in the current defined S3 location.
* S3 tables can be part of [partitions](../../partitioning-tables/partitions-files.md). See Discovery below.

## Discovery

The S3 storage engine supports full [MariaDB discovery](../../../reference/product-development/plugin-development/storage-engines-storage-engine-development/table-discovery.md). This means that if\
you have the S3 storage engine enabled and properly configured, the\
table stored in S3 will automatically be discovered when it's accessed with [SHOW TABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-tables.md), [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) or any other operation that\
tries to access it. In the case of SELECT, the .frm file from S3 will\
be copied to the local storage to speed up future accesses.

When an S3 table is opened for the first time (it's not in the table cache)\
and there is a local .frm file, the S3 engine will check if it's still\
relevant, and if not, update or delete the .frm file.

This means that if the table definition changes on S3 and it's in the\
local cache, one has to execute [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) to\
get MariaDB to notice the change and update the .frm file.

If partitioning S3 tables are used, the partition definitions will also be stored on S3 storage and are discovered by other servers.

Discovery of S3 tables is not done for tables in the [mysql databases](../../../reference/system-tables/the-mysql-database-tables/) to make mariadbd boot faster and more securely.

## Replication

S3 works with [replication](../../../ha-and-performance/standard-replication/replication-overview.md). One can use replication in two different scenarios:

* The primary and replica share the same S3 storage. In this case the primary will make all changes to the S3 data and the replica will ignore any changes in the replication stream to S3 data . This scenario is achieved by setting [s3\_slave\_ignore\_updates](s3-storage-engine-system-variables.md#s3-slave-ignore-updates) to 1.
* The primary and replica don't share the same S3 storage or the replica uses another storage engine for the S3 tables. This scenario is achieved by setting [s3\_slave\_ignore\_updates](s3-storage-engine-system-variables.md#s3-slave-ignore-updates) to 0.

## aria\_s3\_copy

[aria\_s3\_copy](aria_s3_copy.md) is an external tool that one can use to copy [Aria](../aria/aria-storage-engine.md) tables to and from S3. Use `aria_s3_copy --help` to get the options of how to use it.

## mariadb-dump

* [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) will by default ignore S3 tables. If `mariadb-dump` is run with the `--copy-s3-tables` option, the resulting file will contain a CREATE statement for a similar [Aria](../aria/aria-storage-engine.md) table, followed by the table data and ending with an `ALTER TABLE xxx ENGINE=S3`.

## ANALYZE TABLE

As of [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10514-release-notes), [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) is supported for S3 tables.\
As the S3 tables are read-only, a normal `ANALYZE TABLE` will not do anything. However\
using `ANALYZE TABLE table_name PERSISTENT FOR...` will now work.

## CHECK TABLE

As of [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10514-release-notes), [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md) will work. As S3 tables are read only\
it is very unlikely that they can become corrupted. The only known way an S3 table could be corrupted if either the original table copied to S3 was corrupted or the process of copying the original table to S3 was somehow interrupted.

## Current Limitations

* [mysql-test-run](../../../clients-and-utilities/testing-tools/mariadb-test/) doesn't by default test the S3 engine as we can't embed AWS keys into mysql-test-run.
* Replicas should not access S3 tables while they are ALTERed! This is because there is no locking implemented to S3 between servers. However, after a table (either the original S3 table or the partitioned S3 table) is changed on the primary, the replica will notice this on the next access and update its local definition.

### Limitations in [ALTER .. PARTITION](../../../reference/sql-statements/data-definition/alter/alter-table/)

All [ALTER PARTITION](../../../reference/sql-statements/data-definition/alter/alter-table/) operations are supported on S3 partitioning tables except:

* REBUILD PARTITION
* TRUNCATE PARTITION
* REORGANIZE PARTITION

## Performance Considerations

Depending on your connection speed to your S3 provider, there can be some notable slowdowns in some\
operations.

### Discovery

As S3 is supporting discovery (automatically making tables available that are in S3) this can cause some\
small performance problems if the S3 engine is enabled. Partitioning S3 tables also support discovery.

* CREATE TABLE is a bit slower as the S3 engine has to check if the to-be-created table is already S3.
* Queries on information\_schema tables are slower as S3 has to check if there is new tables in S3.
* DROP of non existing tables are slower as S3 has to check if the table is in S3.

There are no performance degradation's when accessing existing tables on the server. Accessing the S3\
table the first time will copy the .frm file from S3 to the local disk, speeding up future accesses to the table.

### Caching

* Accessing a table on S3 can take some time , especially if you are using big packets ([s3\_block\_size](s3-storage-engine-system-variables.md#s3_block_size)). However the second access to the same data should be fast as it's then cached in the S3 page cache.

### Things to Try to Increase Performance

If you have performance problems with the S3 engine, here are some things you can try:

* Decreasing [s3\_block\_size](s3-storage-engine-system-variables.md#s3_block_size). This can be done both globally and per table.
* Use COMPRESSION\_ALGORITHM=zlib when creating the table. This will decrease the amount of data transferred from S3 to the local cache.
* Increasing the size of the s3 page cache: [s3\_pagecache\_buffer\_size](s3-storage-engine-system-variables.md#s3_pagecache_buffer_size)

Try also to execute the query twice to check if the problem is that the data was not properly cached. When data is cached locally the performance should be excellent.

## Future Development Ideas

* Store aws keys and region in the mysql.servers table (as [Spider](../spider/) and [FederatedX](../federatedx-storage-engine/)). This will allow one to have different tables on different S3 servers.
* Store s3 bucket, access\_key and secret key in a cache to better be able to better to reuse connections. This would save some memory and make some S3 accesses a bit faster as we could reuse old connections.

## Troubleshooting S3 on SELinux

If you get errors such as:

```sql
ERROR 3 (HY000): Got error from put_object(bubu/produkt/frm): 5 Couldn't connect to server
```

one reason could be that your system doesn't allow MariaDB to connect to ports other than 3306.\
To procedure to enable other ports is the following:

Search for the ports allowed for MariaDB:

```bash
$ sudo semanage port -l | grep mysqld_port_t
mysqld_port_t                tcp   1186, 3306, 63132-63164
```

Say you want to allow MariaDB to connect to port 32768:

```bash
$ sudo semanage port -a -t mysqld_port_t -p tcp 32768
```

You can verify that the new port, 32768, is now allowed for MariaDB:

```bash
$ sudo semanage port -l | grep mysqld_port_t
mysqld_port_t                tcp   32768,1186, 3306, 63132-63164
```

## See Also

* [S3 storage engine internals](s3-storage-engine-internals.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
