---
description: >-
  Install MinIO to provide S3-compatible storage for testing the S3 storage
  engine with mariadb-test-run.
---

# Installing MinIO for Usage With mariadb-test-run

When testing the S3 storage engine with the s3 test suite, [mariadb-test-run](./) needs access to Amazon S3 compatible storage.

The easiest way to achieve this is to install [MinIO](https://min.io), an open source S3 compatible storage.

Here is a shell script that you can use to install MinIO with the right credentials for [mariadb-test-run](./).\
This should work on most Linux systems as the binaries are statically linked.\
You can alternatively download MinIO binaries directly from [here](https://min.io/download).

```
# Where to install the MinIO binaries and where to store the data
install=/my/local/minio
data=/tmp/shared

# Get the MinIO binaries. You can skip this test if you already have MinIO installed.
mkdir -p $install
wget https://dl.min.io/server/minio/release/linux-amd64/minio -O $install/minio
wget https://dl.min.io/client/mc/release/linux-amd64/mc -O $install/mc
chmod a+x $install/minio $install/mc

# Setup MinIO for usage with mariadb-test-run
MINIO_ACCESS_KEY=minio MINIO_SECRET_KEY=minioadmin $install/minio server $data 2>&1 &
$install/mc config host add local http://127.0.0.1:9000 minio minioadmin
$install/mc mb --ignore-existing local/storage-engine
```

Now you can run the S3 test suite:

```
cd "mysql-source-dir"/mariadb-test
./mariadb-test-run --suite=s3
```

If there is an issue while running the test suite, you can see the files created by MinIO with:

```
$install/mc ls -r local/storage-engine
```

or

```
ls $data/storage-engine
```

If you want to use MinIO with different credentials or you want to run the test against another S3 storage you ave to update the update the following files:

```
mariadb-test/suite/s3/my.cnf
mariadb-test/suite/s3/slave.cnf
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
