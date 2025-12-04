# aria\_s3\_copy

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)

The [S3 storage engine](./) has been available since [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes).

`aria_s3_copy` is a tool for copying an [Aria](../aria/) table to and from [S3](./).

The Aria table must be non transactional and have [ROW\_FORMAT=PAGE](../aria/aria-storage-formats.md#page).

For `aria_s3_copy` to work reliably, the table should not be changed by the MariaDB server during the copy, and one should have first performed [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to ensure that the table is properly closed.

Example of properly created Aria table:

```sql
CREATE TABLE test1 (a INT) transactional=0 row_format=PAGE engine=aria;
```

Note that [ALTER TABLE table\_name ENGINE=S3](using-the-s3-storage-engine.md) will work for any kind of table. This internally converts the table to an Aria table and then moves it to S3 storage.

### Main Arguments

| Option                         | Description                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| -?, --help                     | Display this help and exit.                                                                      |
| -k, --s3-access-key=name       | AWS access key ID                                                                                |
| -r, --s3-region=name           | AWS region                                                                                       |
| -K, --s3-secret-key=name       | AWS secret access key ID                                                                         |
| -b, --s3-bucket=name           | AWS prefix for tables                                                                            |
| -h, --s3-host-name=name        | Host name to S3 provider                                                                         |
| -c, --compress                 | Use compression                                                                                  |
| -o, --op=name                  | Operation to execute. One of 'from\_s3', 'to\_s3' or 'delete\_from\_s3'                          |
| -d, --database=name            | Database for copied table (second prefix). If not given, the directory of the table file is used |
| -B, --s3-block-size=#          | Block size for data/index blocks in s3                                                           |
| -L, --s3-protocol-version=name | Protocol used to communication with S3. One of "Amazon" or "Original".                           |
| -f, --force                    | Force copy even if target exists                                                                 |
| -v, --verbose                  | Write more information                                                                           |
| -V, --version                  | Print version and exit.                                                                          |
| -#, --debug\[=name]            | Output debug log. Often this is 'd:t:o,filename'.                                                |
| --s3-debug                     | Output debug log from marias3 to stdout                                                          |

|                   |                                                 |
| ----------------- | ----------------------------------------------- |
| -p, --s3-port=#   | Port number to connect to (0 means use default) |
| -P, --s3-use-http | If true, force use of HTTP protocol             |

### Typical Configuration in a my.cnf File

```
[aria_s3_copy]
s3-bucket=mariadb
s3-access-key=xxxx
s3-secret-key=xxx
s3-region=eu-north-1
#s3-host-name=s3.amazonaws.com
#s3-protocol-version=Amazon
verbose=1
op=to
```

### Example Usage

The following code will copy an existing Aria table named `test1` to S3.\
If the `--database` option is not given, then the directory name where the table files exist are used as the database.

```bash
shell> aria_s3_copy --force --op=to --database=foo --compress --verbose --s3_block_size=4M test1
Delete of aria table: foo.test1
Delete of index information foo/test1/index
Delete of data information foo/test1/data
Delete of base information and frm
Copying frm file test1.frm
Copying aria table: foo.test1 to s3
Creating aria table information foo/test1/aria
Copying index information foo/test1/index
.
Copying data information foo/test1/data
.
```

When using `--verbose`, `aria_s3_copy` will write a dot for each #/79 part of the file copied.

## See Also

[Using the S3 storage engine](using-the-s3-storage-engine.md#aria_s3_copy). This pages has examples of .my.cnf entries for using `aria_s3_copy`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
