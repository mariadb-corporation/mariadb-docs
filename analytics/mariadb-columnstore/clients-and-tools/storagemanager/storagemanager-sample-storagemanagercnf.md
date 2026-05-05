---
description: >-
  Sample storagemanager.cnf for MariaDB ColumnStore showing [ObjectStorage],
  [S3], and [LocalStorage] sections with credentials, paths, and concurrency
  tuning options.
---

# Sample storagemanager.cnf

```ini
# Sample storagemanager.cnf

[ObjectStorage]
service = S3
object_size = 5M
metadata_path = /var/lib/columnstore/storagemanager/metadata
journal_path = /var/lib/columnstore/storagemanager/journal
max_concurrent_downloads = 21
max_concurrent_uploads = 21
common_prefix_depth = 3

[S3]
region = us-west-1
bucket = my_columnstore_bucket
endpoint = s3.amazonaws.com
aws_access_key_id = AKIAR6P77BUKULIDIL55
aws_secret_access_key = F38aR4eLrgNSWPAKFDJLDAcax0gZ3kYblU79

[LocalStorage]
path = /var/lib/columnstore/storagemanager/fake-cloud
fake_latency = n
max_latency = 50000

[Cache]
cache_size = 2g
path = /var/lib/columnstore/storagemanager/cache
```

{% hint style="info" %}
Note: A region is required even when using an on-premises solution like [ActiveScale](https://qsupport.quantum.com/kb/flare/Content/ActiveScale/PDFs/ActiveScale_OS_S3_API_Reference.pdf) due to header expectations within the API.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
