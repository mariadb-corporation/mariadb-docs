---
description: >-
  This feature enables transparent page-level compression for tables using
  algorithms like LZ4 or Zlib, reducing storage requirements.
---

# InnoDB Page Compression

## Overview

InnoDB page compression provides a way to compress InnoDB tables.

## Use Cases

* InnoDB page compression can be used on any storage device and any file system.
* InnoDB page compression is most efficient on file systems that support sparse files. See [Saving Storage Space with Sparse Files](innodb-page-compression.md#saving-storage-space-with-sparse-files) for more information.
* InnoDB page compression is most beneficial on solid state drives (SSDs) and other flash storage. See [Optimized for Flash Storage](innodb-page-compression.md#optimized-for-flash-storage) for more information.
* InnoDB page compression performs best when your storage device and file system support atomic writes, since that allows the [InnoDB doublewrite buffer](innodb-doublewrite-buffer.md) to be disabled. See [Atomic Write Support](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md) for more information.

## Comparison with the `COMPRESSED` Row Format

InnoDB page compression is a modern way to compress your InnoDB tables. It is similar to InnoDB's [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, but it has many advantages. Some of the differences are:

* With InnoDB page compression, compressed pages are immediately decompressed after being read from the tablespace file, and only uncompressed pages are stored in the buffer pool. In contrast, with InnoDB's [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, compressed pages are decompressed immediately after they are read from the tablespace file, and both the uncompressed and compressed pages are stored in the buffer pool. This means that the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format uses more space in the buffer pool than InnoDB page compression does.
* With InnoDB page compression, pages are compressed just before being written to the tablespace file. In contrast, with InnoDB's [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, pages are re-compressed immediately after any changes, and the compressed pages are stored in the buffer pool alongside the uncompressed pages. These changes are then occasionally flushed to disk. This means that the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format re-compresses data more frequently than InnoDB page compression does.
* With InnoDB page compression, multiple compression algorithms are supported. In contrast, with InnoDB's [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, [zlib](https://www.zlib.net/) is the only supported compression algorithm. This means that the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format has less compression options than InnoDB page compression does.

In general, InnoDB page compression is superior to the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format.

## Comparison with Storage Engine-Independent Column Compression

* See [Storage Engine-Independent Column Compression - Comparison with InnoDB Page Compression](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md#comparison-with-innodb-page-compression).

## Configuring the InnoDB Page Compression Algorithm

There is not currently a table option to set different InnoDB page compression algorithms for individual tables.

However, the server-wide InnoDB page compression algorithm can be configured by setting the [innodb\_compression\_algorithm](innodb-system-variables.md#innodb_compression_algorithm) system variable.

When this system variable is changed, the InnoDB page compression algorithm does not change for existing pages that were already compressed with a different InnoDB page compression algorithm. InnoDB is able to handle this situation without issues, because every page in an InnoDB tablespace contains metadata about the InnoDB page compression algorithm in the page header. This means that InnoDB supports having uncompressed pages and pages compressed with different InnoDB page compression algorithms in the same InnoDB tablespace at the same time.

This system variable can be set to one of the following values:

| System Variable Value | Description                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| none                  | Pages are not compressed. This is the default value in [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3) and before, and [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.21) and before.                                                                 |
| zlib                  | Pages are compressed using the bundled [zlib](https://www.zlib.net/) compression algorithm. This is the default value in [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4) and later, and [MariaDB 10.1.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.22) and later. |
| lz4                   | Pages are compressed using the [lz4](https://code.google.com/p/lz4/) compression algorithm.                                                                                                                                                                                                                                                                                |
| lzo                   | Pages are compressed using the [lzo](https://www.oberhumer.com/opensource/lzo/) compression algorithm.                                                                                                                                                                                                                                                                     |
| lzma                  | Pages are compressed using the [lzma](https://tukaani.org/xz/) compression algorithm.                                                                                                                                                                                                                                                                                      |
| bzip2                 | Pages are compressed using the [bzip2](https://www.bzip.org/) compression algorithm.                                                                                                                                                                                                                                                                                       |
| snappy                | Pages are compressed using the [snappy](https://google.github.io/snappy/) algorithm.                                                                                                                                                                                                                                                                                       |

However, on many distributions, the standard MariaDB builds do not support all InnoDB page compression algorithms by default. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107), algorithms can be [installed as a plugin](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).

This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```
SET GLOBAL innodb_compression_algorithm='lzma';
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_compression_algorithm=lzma
```

### Checking Supported InnoDB Page Compression Algorithms

On many distributions, the standard MariaDB builds do not support all InnoDB page compression algorithms by default. Therefore, if you want to use a specific InnoDB page compression algorithm, then you should check whether your MariaDB build supports it.

The [zlib](https://www.zlib.net/) compression algorithm is always supported. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107), algorithms can be [installed as a plugin](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).

A MariaDB build's support for other InnoDB page compression algorithms can be checked by querying the following status variables with [SHOW GLOBAL STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md):

| Status Variable                                                                                                                            | Description                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| [Innodb\_have\_lz4](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_have_lz4)       | Whether InnoDB supports the [lz4](https://code.google.com/p/lz4/) compression algorithm.            |
| [Innodb\_have\_lzo](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_have_lzo)       | Whether InnoDB supports the [lzo](https://www.oberhumer.com/opensource/lzo/) compression algorithm. |
| [Innodb\_have\_lzma](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_have_lzma)     | Whether InnoDB supports the [lzma](https://tukaani.org/xz/) compression algorithm.                  |
| [Innodb\_have\_bzip2](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_have_bzip2)   | Whether InnoDB supports the [bzip2](https://www.bzip.org/) compression algorithm.                   |
| [Innodb\_have\_snappy](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_have_snappy) | Whether InnoDB supports the [snappy](https://google.github.io/snappy/) compression algorithm.       |

For example:

```sql
SHOW GLOBAL STATUS WHERE Variable_name IN (
   'Innodb_have_lz4', 
   'Innodb_have_lzo', 
   'Innodb_have_lzma', 
   'Innodb_have_bzip2', 
   'Innodb_have_snappy'
);
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| Innodb_have_lz4    | OFF   |
| Innodb_have_lzo    | OFF   |
| Innodb_have_lzma   | ON    |
| Innodb_have_bzip2  | OFF   |
| Innodb_have_snappy | OFF   |
+--------------------+-------+
```

### Adding Support for an InnoDB Page Compression Algorithm

On many distributions, the standard MariaDB builds do not support all InnoDB page compression algorithms by default. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107), algorithms can be [installed as a plugin](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md), but in earlier versions, if you want to use certain InnoDB page compression algorithms, then you may need to do the following:

* Download the package for the desired compression library from the above links.
* Install the package for the desired compression library.
* Compile MariaDB from the source distribution.

The general steps for compiling MariaDB are:

* Download and unpack the source code distribution:

```bash
wget https://downloads.mariadb.com/MariaDB/mariadb-10.4.8/source/mariadb-10.4.8.tar.gz
tar -xvzf mariadb-10.4.8.tar.gz
cd mariadb-10.4.8/
```

* Configure the build using [cmake](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md#using-cmake):

```bash
cmake .
```

* Check [CMakeCache.txt](https://cmake.org/runningcmake/) to confirm that it has found the desired compression library on your system.
* Compile the build:

```bash
make
```

* Either install the build:

```bash
make install
```

Or make a package to install:

```bash
make package
```

See [Compiling MariaDB From Source](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/) for more information.

## Enabling InnoDB Page Compression

InnoDB page compression is not enabled by default. However, InnoDB page compression can be enabled for just individual InnoDB tables or it can be enabled for all new InnoDB tables by default.

InnoDB page compression is also only supported if the InnoDB table is in a [file per-table](innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespace. Therefore, the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable must be set to `ON` to use InnoDB page compression.

InnoDB page compression is only supported if the InnoDB table uses the `Barracuda` [file format](innodb-file-format.md).Therefore, in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and before, the [innodb\_file\_format](innodb-system-variables.md#innodb_file_format) system variable must be set to `Barracuda` to use InnoDB page compression.

InnoDB page compression is also only supported if the InnoDB table's [row format](innodb-row-formats/innodb-row-formats-overview.md) is [COMPACT](innodb-row-formats/innodb-compact-row-format.md) or [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md).

### Enabling InnoDB Page Compression by Default

In [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3) and later, InnoDB page compression can be enabled for all new InnoDB tables by default by setting the [innodb\_compression\_default](innodb-system-variables.md#innodb_compression_default) system variable to `ON`.

This system variable can be set to one of the following values:

| System Variable Value | Description                                                                      |
| --------------------- | -------------------------------------------------------------------------------- |
| OFF                   | New InnoDB tables do not use InnoDB page compression. This is the default value. |
| ON                    | New InnoDB tables use InnoDB page compression.                                   |

This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```
SET GLOBAL innodb_compression_default=ON;
```

This system variable's session value can be changed dynamically with [SET SESSION](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

SET GLOBAL innodb_default_row_format='dynamic';

SET GLOBAL innodb_compression_algorithm='lzma';

SET SESSION  innodb_compression_default=ON;

CREATE TABLE users (
   user_id INT NOT NULL, 
   b VARCHAR(200), 
   PRIMARY KEY(user_id)
) 
   ENGINE=InnoDB;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_compression_default=ON
```

### Enabling InnoDB Page Compression for Individual Tables

InnoDB page compression can be enabled for individual tables by setting the [PAGE\_COMPRESSED](../../../reference/sql-statements/data-definition/create/create-table.md#page_compressed) table option to `1`:

```sql
SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

SET GLOBAL innodb_default_row_format='dynamic';

SET GLOBAL innodb_compression_algorithm='lzma';

CREATE TABLE users (
   user_id INT NOT NULL, 
   b VARCHAR(200), 
   PRIMARY KEY(user_id)
) 
   ENGINE=InnoDB
   PAGE_COMPRESSED=1;
```

## Configuring the Compression Level

Some InnoDB page compression algorithms support a compression level option, which configures how the InnoDB page compression algorithm will balance speed and compression.

The compression level's supported values range from `1` to `9`. The range goes from the fastest to the most compact, which means that `1` is the fastest and `9` is the most compact.

Only the following InnoDB page compression algorithms currently support compression levels:

* [zlib](https://www.zlib.net/)
* [lzma](https://tukaani.org/xz/)

If an InnoDB page compression algorithm does not support compression levels, then it ignores any provided compression level value.

### Configuring the Default Compression Level

The default compression level can be configured by setting the [innodb\_compression\_level](innodb-system-variables.md#innodb_compression_level) system variable.

This system variable's default value is `6`.

This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_compression_level=9;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_compression_level=9
```

### Configuring the Compression Level for Individual Tables

The compression level for individual tables can also be configured by setting the [PAGE\_COMPRESSION\_LEVEL](../../../reference/sql-statements/data-definition/create/create-table.md#page_compression_level) table option for the table:

```sql
SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

SET GLOBAL innodb_default_row_format='dynamic';

SET GLOBAL innodb_compression_algorithm='lzma';

CREATE TABLE users (
   user_id INT NOT NULL, 
   b VARCHAR(200), 
   PRIMARY KEY(user_id)
) 
   ENGINE=InnoDB
   PAGE_COMPRESSED=1
   PAGE_COMPRESSION_LEVEL=9;
```

## Configuring the Failure Threshold and Maximum Padding

InnoDB page compression can encounter compression failures.

InnoDB page compression's failure threshold can be configured. If InnoDB encounters more compression failures than the failure threshold, then it pads pages with zeroed out bytes before attempting to compress them as a way to reduce failures. If the failure rate stays above the failure threshold, then InnoDB pads pages with more zeroed out bytes in 128 byte increments.

InnoDB page compression's maximum padding can also be configured.

### Configuring the Failure Threshold

The failure threshold can be configured by setting the [innodb\_compression\_failure\_threshold\_pct](innodb-system-variables.md#innodb_compression_failure_threshold_pct) system variable.

This system variable's supported values range from `0` to `100`.

This system variable's default value is `5`.

This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```
SET GLOBAL innodb_compression_failure_threshold_pct=10;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_compression_failure_threshold_pct=10
```

### Configuring the Maximum Padding

The maximum padding can be configured by setting the [innodb\_compression\_pad\_pct\_max](innodb-system-variables.md#innodb_compression_pad_pct_max) system variable.

This system variable's supported values range from `0` to `75`.

This system variable's default value is `50`.

This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_compression_pad_pct_max=75;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_compression_pad_pct_max=75
```

## Saving Storage Space with Sparse Files

When InnoDB page compression is used, InnoDB may still write the compressed page to the tablespace file with the original size of the uncompressed page, which would be equivalent to the value of the [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) system variable. This is done by design, because when InnoDB's I/O code needs to read the page from disk, it can only read the full page size. However, this is obviously not optimal.

On file systems that support sparse files, this problem is solved by writing the tablespace file as a sparse file using the _punch hole_ technique. With the _punch hole_ technique, InnoDB will only write the actual compressed page size to the tablespace file, aligned to sector size. The rest of the page is trimmed.

This _punch hole_ technique allows InnoDB to read the compressed page from disk as the full page size, even though the compressed page really takes up less space on the file system.

There are some potential disadvantages to using sparse files:

* Some utilities may require special options in order to handle sparse files in an efficient manner.
* Most existing file systems are slow to [unlink()](https://linux.die.net/man/2/unlink) sparse files. As a consequence, if a tablespace file is a sparse file, then dropping the table can be very slow.

### Sparse File Support on Linux

On Linux, the following file systems support sparse files:

* `ext3`
* `ext4`
* `xfs`
* `btrfs`
* `nvmfs`

On Linux, file systems need to support the [fallocate()](https://linux.die.net/man/2/fallocate) system call with the `FALLOC_FL_PUNCH_HOLE` and `FALLOC_FL_KEEP_SIZE` flags:

```
fallocate(file_handle, FALLOC_FL_PUNCH_HOLE | FALLOC_FL_KEEP_SIZE, file_offset, remainder_len);
```

Some Linux utilities may require special options in order to work with sparse files efficiently:

* The [ls](https://linux.die.net/man/1/ls) utility will report the non-sparse size of the tablespace file when executed with default behavior, but [ls -s](https://linux.die.net/man/1/ls) will report the actual amount of storage allocated for the tablespace file.
* The [cp](https://linux.die.net/man/1/cp) utility is pretty good at auto-detecting sparse files, but it also provides the [cp --sparse=always](https://linux.die.net/man/1/cp) and [cp --sparse=never](https://linux.die.net/man/1/cp) options, if the auto-detection is not desired.
* The [tar](https://linux.die.net/man/1/tar) utility will archive sparse files with their non-sparse size when executed with default behavior, but [tar --sparse](https://linux.die.net/man/1/tar) will auto-detect sparse files, and archive them with their sparse size.

### Sparse File Support on Windows

On Windows, the following file systems support sparse files:

* `NTFS`

On Windows, file systems need to support the [DeviceIoControl()](https://docs.microsoft.com/en-us/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the [FSCTL\_SET\_SPARSE](https://docs.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_set_sparse) and [FSCTL\_SET\_ZERO\_DATA](https://docs.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_set_zero_data) control codes:

```
DeviceIoControl(file_handle, FSCTL_SET_SPARSE, inbuf, inbuf_size, 
   outbuf, outbuf_size,  NULL, &overlapped)
...
DeviceIoControl(file_handle, FSCTL_SET_ZERO_DATA, inbuf, inbuf_size, 
   outbuf, outbuf_size,  NULL, &overlapped)
```

### Configuring InnoDB to use Sparse Files

In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and later, InnoDB uses the _punch hole_ technique to create sparse files used automatically when the underlying file system supports sparse files.

In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and before, InnoDB can be configured to use the _punch hole_ technique to create sparse files by configuring the [innodb\_use\_trim](innodb-system-variables.md#innodb_use_trim) and [innodb\_use\_fallocate](innodb-system-variables.md#innodb_use_fallocate) system variables. These system variables can be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_use_trim=ON
innodb_use_fallocate=ON
```

## Optimized for Flash Storage

InnoDB page compression was designed to be optimized on solid state drives (SSDs) and other flash storage.

InnoDB page compression was originally developed by collaborating with [Fusion-io](https://fusionio.com). As a consequence, it was originally designed to work best on [FusionIO devices](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/fusion-io/fusion-io-introduction.md) using [NVMFS](https://ieeexplore.ieee.org/document/6558434). [Fusion-io](https://fusionio.com) has since been acquired by [Western Digital](https://www.westerndigital.com/), and they have decided not to continue supporting [NVMFS](https://ieeexplore.ieee.org/document/6558434).

However, InnoDB page compression is still likely to be most optimized on solid state drives (SSDs) and other flash storage.

InnoDB page compression works without any issues on hard disk drives (HDDs). However, since its compression relies on the use of sparse files, the data may be somewhat fragmented on disk. This fragmentation may hurt performance on HDDs, since they handle random reads and writes much more slowly than flash storage.

## Configuring InnoDB Page Flushing

With InnoDB page compression, pages are compressed when they are flushed to disk. Therefore, it can be helpful to optimize the configuration of InnoDB's page flushing. See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.

## Monitoring InnoDB Page Compression

InnoDB page compression can be monitored by querying the following status variables with [SHOW GLOBAL STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md):

| Status Variable                                                                                                                                                                            | Description                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| [Innodb\_page\_compression\_saved](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_saved)                          | Bytes saved by compression      |
| [Innodb\_page\_compression\_trim\_sect512](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect512)           | Number of 512 sectors trimmed   |
| [Innodb\_page\_compression\_trim\_sect1024](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect1024)         | Number of 1024 sectors trimmed  |
| [Innodb\_page\_compression\_trim\_sect2048](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect2048)         | Number of 2048 sectors trimmed  |
| [Innodb\_page\_compression\_trim\_sect4096](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect4096)         | Number of 4096 sectors trimmed  |
| [Innodb\_page\_compression\_trim\_sect8192](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect8192)         | Number of 8192 sectors trimmed  |
| [Innodb\_page\_compression\_trim\_sect16384](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect16384)       | Number of 16384 sectors trimmed |
| [Innodb\_page\_compression\_trim\_sect32768](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_compression_trim_sect32768)       | Number of 32768 sectors trimmed |
| [Innodb\_num\_pages\_page\_compressed](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_num_pages_page_compressed)                   | Number of pages compressed      |
| [Innodb\_num\_page\_compressed\_trim\_op](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_num_page_compressed_trim_op)              | Number of trim operations       |
| [Innodb\_num\_page\_compressed\_trim\_op\_saved](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_num_page_compressed_trim_op_saved) | Number of trim operations saved |
| [Innodb\_num\_pages\_page\_decompressed](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_num_pages_page_decompressed)               | Number of pages decompressed    |
| [Innodb\_num\_pages\_page\_compression\_error](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_num_pages_page_compression_error)    | Number of compression errors    |

With InnoDB page compression, a page is only compressed when it is flushed to disk. This means that if you are monitoring InnoDB page compression via these status variables, then the status variables values will only get incremented when the dirty pages are flushed to disk, which does not necessarily happen immediately:

```sql
CREATE TABLE `tab` (
     `id` INT(11) NOT NULL,
     `str` VARCHAR(50) DEFAULT NULL,
     PRIMARY KEY (`id`)
   ) ENGINE=InnoDB;
 
INSERT INTO tab VALUES (1, 'str1');

SHOW GLOBAL STATUS LIKE 'Innodb_num_pages_page_compressed';
+----------------------------------+-------+
| Variable_name                    | Value |
+----------------------------------+-------+
| Innodb_num_pages_page_compressed | 0     |
+----------------------------------+-------+
 
SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

SET GLOBAL innodb_default_row_format='dynamic';

SET GLOBAL innodb_compression_algorithm='lzma';
 
ALTER TABLE tab PAGE_COMPRESSED=1;

SHOW GLOBAL STATUS LIKE 'Innodb_num_pages_page_compressed';
+----------------------------------+-------+
| Variable_name                    | Value |
+----------------------------------+-------+
| Innodb_num_pages_page_compressed | 0     |
+----------------------------------+-------+
 
SELECT SLEEP(10);
+-----------+
| SLEEP(10) |
+-----------+
|         0 |
+-----------+
 
SHOW GLOBAL STATUS LIKE 'Innodb_num_pages_page_compressed';
+----------------------------------+-------+
| Variable_name                    | Value |
+----------------------------------+-------+
| Innodb_num_pages_page_compressed | 3     |
+----------------------------------+-------+
```

## Compatibility with Backup Tools

[mariadb-backup](../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md) supports InnoDB page compression.

[Percona XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) does not support InnoDB page compression.

## Acknowledgements

* InnoDB page compression was developed by collaborating with [Fusion-io](https://fusionio.com). Special thanks especially to Dhananjoy Das and Torben Mathiasen.

## See Also

* [Storage-Engine Independent Column Compression](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md)
* [Atomic Write Support](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md)
* [MariaDB Introduces Atomic Writes](https://blog.mariadb.org/mariadb-introduces-atomic-writes/)
* [Small Datum: Third day with InnoDB transparent page compression](https://smalldatum.blogspot.com/2015/09/third-day-with-innodb-transparent-page.html)
* [InnoDB holepunch compression vs the filesystem in MariaDB 10.1](https://blog.mariadb.org/innodb-holepunch-compression-vs-the-filesystem-in-mariadb-10-1/)
* [Significant performance boost with new MariaDB page compression on FusionIO](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/)
* [INFLOW '14: NVM Compression—Hybrid Flash-Aware Application Level Compression](https://www.usenix.org/conference/inflow14/workshop-program/presentation/das)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
