# Testing Connections

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)

The [S3 storage engine](./) has been available since [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes).

If you can't get the S3 storage engine to work, here are some steps to help verify where the problem could be.

## S3 Connection Variables

In most cases the problem is to correctly set the S3 connection variables.

Key [S3 variables](s3-storage-engine-status-variables.md) are:

* [s3\_access\_key](s3-storage-engine-system-variables.md#s3_access_key): The AWS access key to access your data
* [s3\_secret\_key](s3-storage-engine-system-variables.md#s3_secret_key): The AWS secret key to access your data
* [s3\_bucket](s3-storage-engine-system-variables.md#s3_bucket): The AWS bucket where your data should be stored. All MariaDB table data is stored in this bucket.
* [s3\_region](s3-storage-engine-system-variables.md#s3_region): The AWS region where your data should be stored.
* [s3\_host\_name](s3-storage-engine-system-variables.md#s3_host_name): Hostname for the S3 service.
* [s3\_provider](s3-storage-engine-system-variables.md#s3_provider): Enable S3 provider specific compatibility tweaks. "Default", "Amazon", or "Huawei".
* [s3\_protocol\_version](s3-storage-engine-system-variables.md#s3_protocol_version): Protocol used to communicate with S3. One of "Amazon" or "Original"

There are several ways to ensure you get them right:

### Using aria\_s3\_copy to Test the Connection

[aria\_s3\_copy](aria_s3_copy.md) is a tool that allows you to copy [aria](../aria/) tables to and from S3. It's useful for testing the connection as it allows you to specify all s3 options on the command line.

Execute the following sql commands to create a trivial sql table:

```sql
USE test;
CREATE TABLE s3_test (a INT) ENGINE=aria row_format=page transactional=0;
INSERT INTO s3_test VALUES (1),(2);
FLUSH TABLES s3_test;
```

Now you can use the [aria\_s3\_copy](aria_s3_copy.md) tool to copy this to S3 from your\
shell/the command line:

```bash
shell> cd mariadb-data-directory/test
shell> aria_s3_copy --op=to --verbose --force --**other*options* s3_test.frm

Copying frm file s3_test.frm
Copying aria table: test.s3_test to s3
Creating aria table information test/s3_test/aria
Copying index information test/s3_test/index
Copying data information test/s3_test/data
```

As you can see from the above, [aria\_s3\_copy](aria_s3_copy.md) is using the current directory as the database name.

You can also set the [aria\_s3\_copy](aria_s3_copy.md) options in your my.cnf file to avoid\
some typing.

### Using mariadb-test-run to Test the Connection and the S3 Storage Engine

One can use the [MariaDB test system](../../../clients-and-utilities/testing-tools/mariadb-test/) to run all default S3 test against your S3 storage.

To do that you have to locate the `mysql-test` directory in your system and`cd` to it.

The config file for the S3 test system can be found at `suite/s3/my.cnf`.\
To enable testing you have to edit this file and add the s3 connection options\
to the end of the file. It should look something like this after editing:

```ini
!include include/default_mysqld.cnf
!include include/default_client.cnf

[mysqld.1]
s3=ON
#s3-host-name=s3.amazonaws.com
#s3-protocol-version=Amazon
s3-bucket=MariaDB
s3-access-key=
s3-secret-key=
s3-region=
```

You must give values for `s3-access-key`, `s3-secret-key` and `s3-region` that reflects your S3 provider. The `s3-bucket` name is defined by your administrator.

If you are not using Amazon Web Services as your S3 provider you must\
also specify `s3-hostname` and possibly change`s3-protocol-version` to "Original".

Now you can test the configuration:

```bash
shell> cd **mysql-test** directory
shell> ./mysql-test-run --suite=s3
...
s3.no_s3                                 [ pass ]      5
s3.alter                                 [ pass ]  11073
s3.arguments                             [ pass ]   2667
s3.basic                                 [ pass ]   2757
s3.discovery                             [ pass ]   7851
s3.select                                [ pass ]   1325
s3.unsupported                           [ pass ]    363
```

Note that there may be more tests in your output as we are constantly adding more tests to S3 when needed.

## Create a trace of the S3 connection to see what goes wrong

One can use the `s3_debug` variable to get a trace of the S3 engines interaction with the S3 storage. The trace is sent to the error log.

Here follows one example on can use to get a trace if `ALTER TABLE .. ENGINE=S3` fails:

```sql
USE test;
CREATE TABLE s3_test (a INT) ENGINE=aria row_format=page transactional=0;
INSERT INTO s3_test VALUES (1),(2);
SET @@global.s3_debug=1;
ALTER TABLE s3_test ENGINE=S3;
SET @@global.s3_debug=0;
```

If you have problems deciper the trace, you can always create a ticket on [MariaDB Jira](https://jira.mariadb.org/) and explain the problem you have, including any errors. Don't forget to include the trace!

## What to do when you have got things to work

When you got the connection to work, you should add the options to your global my.cnf file.\
Now you can start testing S3 from your [mariadb command client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) by converting some existing table to S3 with [ALTER TABLE ... ENGINE=S3](using-the-s3-storage-engine.md).

## See Also

* [Using the S3 Storage Engine](using-the-s3-storage-engine.md)
* [Using MinIO with mysql-test-run to test the S3 storage engine](../../../clients-and-utilities/testing-tools/mariadb-test/installing-minio-for-usage-with-mariadb-test-run.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
