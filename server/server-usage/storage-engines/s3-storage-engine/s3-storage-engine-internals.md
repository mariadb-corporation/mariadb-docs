# Engine Internals

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)

The [S3 storage engine](./) has been available since [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes).

The [S3 storage engine](./) is based on the [Aria](../aria/aria-storage-engine.md) code.\
Internally the S3 storage inherits from the Aria code, with hooks\
that change reads, so that instead of reading data from the local disk it\
reads things from S3.

The S3 engine uses it's own page cache, modified to be able to handle reading blocks from S3 (of size `s3_block_size`). Internally the S3 page cache uses pages of [aria-block-size](../aria/aria-system-variables.md#aria_block_size) for splitting the blocks read from S3.

## ALTER TABLE

[ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) will first create a local table in the normal Aria on disk\
format and then move both index and data to S3 in buckets of S3\_BLOCK\_SIZE.\
The .frm file is also copied to S3 for discovery to support discovery for\
other MariaDB servers.\
One can also use ALTER TABLE to change the structure of an S3 table.

## Partitioning Tables

Starting from [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1053-release-notes), S3 tables can also be used with [Partitioning tables](../../partitioning-tables/).\
All [ALTER PARTITION](../../../reference/sql-statements/data-definition/alter/alter-table/) operations are supported except:

* REBUILD PARTITION
* TRUNCATE PARTITION
* REORGANIZE PARTITION

## Big Reads

One of the properties of many S3 implementations is that they favor large\
reads. It's said that 4M gives the best performance, which is why the\
default value for `S3_BLOCK_SIZE` is 4M.

## Compression

If compression (`COMPRESSION_ALGORITHM=zlib`) is used, then all index blocks and data blocks are compressed. The `.frm` file and Aria definition header (first page/pages in the index file) are not compressed as these are used by discovery/open.

If compression is used, then the local block size is `S3_BLOCK_SIZE`, but the block stored in S3 are the size of the compressed block.

Typical compression we have seen is in the range of 80% saved space.

## Structure Stored on S3

The table are copied in S3 into the following locations:

```
frm file (for discovery):
s3_bucket/database/table/frm

First index block (contains description of the Aria file):
s3_bucket/database/table/aria

Rest of the index file:
s3_bucket/database/table/index/block_number

Data file:
s3_bucket/database/table/data/block_number
```

block\_number is a 6-digit decimal number, prefixed with 0\
(Can be larger than 6 numbers, the prefix is just for nice output)

## Using the awsctl Python Tool to Examine Data

### Installing awsctl on Linux

```bash
# install python-pip (on an OpenSuse distribution)
# use the appropriate command for your distribution
zypper install python-pip
pip install --upgrade pip

# the following installs awscli tools in ~/.local/bin
pip install --upgrade --user awscli
export PATH=~/.local/bin:$PATH

# configure your aws credentials
aws configure
```

### Using the awsctl Tool

One can use the `aws` python tool to see how things are stored on S3:

```bash
shell> aws s3 ls --recursive s3://mariadb-bucket/
2019-05-10 17:46:48       8192 foo/test1/aria
2019-05-10 17:46:49    3227648 foo/test1/data/000001
2019-05-10 17:46:48        942 foo/test1/frm
2019-05-10 17:46:48    1015808 foo/test1/index/000001
```

To delete an obsolete table `foo.test1` one can do:

```bash
shell> ~/.local/bin/aws s3 rm --recursive s3://mariadb-bucket/foo/test1
delete: s3://mariadb-bucket/foo/test1/aria
delete: s3://mariadb-bucket/foo/test1/data/000001
delete: s3://mariadb-bucket/foo/test1/frm
delete: s3://mariadb-bucket/foo/test1/index/000001
```

## See Also

* [Using the S3 storage engine](using-the-s3-storage-engine.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
