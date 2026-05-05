---
description: >-
  Load delimited data files from S3-compatible cloud object storage into
  MariaDB Enterprise ColumnStore using the columnstore_info.load_from_s3
  stored procedure, available from CS 23.02.
---

# Data Loading With load\_from\_s3

## Overview

MariaDB Enterprise ColumnStore includes a stored procedure called `columnstore_info.load_from_s3`, which can load data from a plain-text file containing delimiter-separated values (such as `CSV or TSV`) stored on S3-compatible cloud object storage.

## Compatibility

Available from MariaDB Enterprise ColumnStore 23.02.

## System Variables

Before you import data with the `columnstore_info.load_from_s3` stored procedure, the authentication credentials and the region can be configured using system variables:

* `columnstore_s3_key`
* `columnstore_s3_secret`
* `columnstore_s3_region`

For example, the following statements show how to set the system variables for your current session:

```sql
SET columnstore_s3_key='S3_KEY';
SET columnstore_s3_secret='S3_SECRET';
SET columnstore_s3_region='S3_REGION';
```

## Import Data

To import data with the `columnstore_info.load_from_s3` stored procedure, use the `CALL` statement:

```sql
CALL columnstore_info.load_from_s3('BUCKET_URL',
      'FILE_NAME',
      'DATABASE_NAME',
      'TABLE_NAME',
      'TERMINATED_BY',
      'ENCLOSED_BY',
      'ESCAPED_BY');
```

* Replace `'BUCKET_URL'` with the URL of your bucket. The protocol in the URL must be `s3: for AWS S3 or gs:` for Google Cloud Storage
* Replace `'FILE_NAME'` with the file name to load from. The file must be a plain-text file containing delimiter-separated values, such as a comma-separated values (CSV) or tab-separated values (TSV) file. The supported file format is similar to the plain-text file formats supported by `cpimport` and `LOAD DATA [LOCAL] INFILE`. Please note that this stored procedure can't load dump files created by mariadb-dump
* Replace `'DATABASE_NAME'` with the database to import into
* Replace `'TABLE_NAME'` with the table name to import into
* Replace `'TERMINATED_BY'` with the field terminator used in the file, similar to the `-s command-line` option for `cpimport`
* Replace `'ENCLOSED_BY'` with the quotes used in the file, similar to the `-E command-line` option for cpimport
* Replace `'ESCAPED_BY'` with the escape character used in the file, similar to the `-C command-line` option for `cpimport`

All parameters are mandatory.

For example, to load a comma-separated values (CSV) file from AWS S3:

```sql
CALL columnstore_info.load_from_s3('s3://mariadb-columnstore-test-data/',
   'test-data-db1-tab1.csv',
   'db1',
   'tab1',
   ',',
   '"',
   '\\');
```

When the stored procedure completes, it returns JSON containing the status of the operation. If the JSON shows an error or "success": false, check your table to see if some or all of your data was loaded, because many errors are non-fatal.

## Permissions

When the data file is stored in Amazon S3, the AWS user only requires the `s3:GetObject` action on the bucket.

For example, the AWS user can use a user policy like the following:

```sql
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "readBucket",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket",
                "arn:aws:s3:::my-bucket/*"
            ]
        }
    ]
}
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
