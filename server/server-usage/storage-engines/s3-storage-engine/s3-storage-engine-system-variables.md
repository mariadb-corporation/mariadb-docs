# S3 System Variables

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)

The [S3 storage engine](./) has been available since [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes).

This page documents system variables related to the [S3 storage engine](./).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting system variables.

Also see the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md)

## Variables

#### `s3_access_key`

* Description: The AWS access key to access your data. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Command line: `--s3-access-key=val`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_block_size`

* Description: The default block size for a table, if not specified in [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md). Set to 4M as default. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Command line: `--s3-block-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `4194304`
* Range: `4194304` to `16777216`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_bucket`

* Description: The AWS bucket where your data should be stored. All MariaDB table data is stored in this bucket. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Command line: `--s3-bucket=val`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `MariaDB`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_debug`

* Description: Generates a trace file from libmarias3 on stderr (mysqld.err) for debugging the S3 protocol.
* Command line: `--s3-debug=[0|1]`
* Scope: Global
* Dynamic:
  * Yes (>= [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes))
  * No (<= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes), [MariaDB 11.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes))
* Data Type: Boolean
* Valid Values: 0 or 1
* Default Value: `0`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_host_name`

* Description: Hostname for the S3 service. "s3.amazonaws.com", Amazon S3 service, by default
* Command line: `--s3-host-name=val`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `s3.amazonaws.com`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_no_content_type`

* Description: If true (false is default), disables the Content-Type header, required for some providers.
* Command line: `--s3-no-content-type=[0|1]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `0`
* Introduced: [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes)

#### `s3_pagecache_age_threshold`

* Description: This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in the page cache.
* Command line: `--s3-pagecache-age-threshold=val`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `300`
* Range: `100` to `18446744073709551615`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_pagecache_buffer_size`

* Description: The size of the buffer used for index blocks for S3 tables. Increase this to get better index handling (for all reads and multiple writes) to as much as you can afford. Size can be adjusted in blocks of `8192`.
* Command line: `--s3-pagecache-buffer-size=val`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `134217728` (128M)
* Range: `33554432` to `18446744073709551615`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_pagecache_division_limit`

* Description: The minimum percentage of warm blocks in key cache.
* Command line: `--s3-pagecache-division-limit=val`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `100`
* Range: `1` to `100`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_pagecache_file_hash_size`

* Description: Number of hash buckets for open files. Default 512. If you have a lot of S3 files open you should increase this for faster flush of changes. A good value is probably 1/10 of number of possible open S3 files.
* Command line: `--s3-pagecache-file-hash-size=#`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `512`
* Range: `32` to `16384`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_port`

* Description: The TCP port number on the S3 host to connect to. A values of 0 means determine automatically.
* Command line: `--s3-port=#`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `0`
* Range: `0` to `65535`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1057-release-notes)

#### `s3_protocol_version`

* Description: Protocol used to communication with S3. "Auto" is the default. If you get errors like "8 Access Denied" when you are connecting to another service provider, then try to change this option. The reason for this variable is that Amazon has changed some parts of the S3 protocol since they originally introduced it but other service providers are still using the original protocol. Can also be set numerically.
  * `Auto` (`0`):
  * `Original` or (`1`): Same as "Auto". Deprecated from [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes).
  * `Amazon` (`2`) Same as "Auto". Deprecated from [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes).
  * `Legacy` (`3`): v1 protocol. From [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes)
  * `Path` (`4`): From [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes)
  * `Domain` (`5`): From [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes)
* Command line: `--s3-protocol-version=val`
* Scope: Global
* Dynamic: Yes
* Data Type: Enum
* Valid Values:
  * `Auto`(`0`) , `Original` (`1`), `Amazon` (`2`), `Legacy` (`3`), `Path` (`4`), `Domain` (`5`) (>= [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes))
  * `Auto`, `Original`, `Amazon` (<= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes), [MariaDB 11.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes))
* Default Value: `Auto`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_provider`

* Description: Enable S3 provider specific compatibility tweaks. "Default", "Amazon", or "Huawei".
  * `Default`:
  * `Amazon`: Effectively sets [s3\_protocol\_version](s3-storage-engine-system-variables.md#s3_protocol_version) to `5` (`Domain`), overriding any other setting it may have.
  * `Huawei`: Effectively sets [s3\_no\_content\_type](s3-storage-engine-system-variables.md#s3_no_content_type) to 1, overriding any other setting it may have.
* Command line: `--s3-provider=val`
* Scope: Global
* Dynamic: Yes
* Data Type: enum
* Valid Values: `Default`, `Amazon`, `Huawei`
* Default Value: `Default`
* Introduced: [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes)

#### `s3_region`

* Description: The AWS region where your data should be stored. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Command line: `--s3-region=val`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_replicate_alter_as_create_select`

* Description: When converting S3 table to local table, log all rows in binary log. This allows the slave to replicate `CREATE TABLE .. SELECT FROM s3_table` even it the slave doesn't have access to the original `s3_table`.
* Command line: `--s3-replicate-alter-as-create-select=[0|1]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `1`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_secret_key`

* Description: The AWS secret key to access your data. See [mariadbd startup options for S3](using-the-s3-storage-engine.md#mariadbd-startup-options-for-s3).
* Command line: `--s3-secret-key=val`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: (Empty)
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_slave_ignore_updates`

* Description: Should be set if master and slave share the same S3 instance. This tells the slave that it can ignore any updates to the S3 tables as they are already applied on the master.
* Command line: `--s3-slave-ignore-updates=[0|1]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `0`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `s3_ssl_no_verify`

* Description: If true, SSL certificate verification for the S3 endpoint is disabled
* Command line: `--s3-ssl-no-verify=[0|1]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `0`
* Introduced: [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes)

#### `s3_use_http`

* Description: If enabled, HTTP are used instead of HTTPS.
* Command line: `--s3-use-http=[0|1]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `0`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1057-release-notes)

## See Also

[Using the S3 Storage Engine](using-the-s3-storage-engine.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
