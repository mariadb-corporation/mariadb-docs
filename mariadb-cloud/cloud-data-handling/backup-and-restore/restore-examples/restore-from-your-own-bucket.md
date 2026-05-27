---
description: >-
  Restore MariaDB Cloud data from external Google Cloud Storage or Amazon S3
  buckets, with backups created using mariabackup or mysqldump and replayed
  via the SkySQL Backup API.
---

# Restore From Your Own Bucket

{% include "../../../.gitbook/includes/authentication.md" %}

You can restore your data from external cloud storage. MariaDB Cloud supports restoration from both Google Cloud Storage (GCS) and Amazon S3 cloud storage buckets. Your backup data should be created using either `mariabackup` or `mysqldump`.

Below is a sample restore call:

```bash

curl --location 'https://api.skysql.com/skybackup/v1/restores' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "service_id": "<SERVICE_ID>",
    "id": "<ID>",
    "external_source": {
      "bucket": "<GCS_URI> оr <S3_URI> ",
      "method": "<BACKUP_METHOD>",
      "credentials": "<GCP_SERVICE_ACCOUNT_BASE64> or AWS_ACCOUNT_ACCESS_KEY_BASE64"
    }
  }'
```

* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch your service ID from the Fully qualified domain name(FQDN) of your service.\
  E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)
* ID : the backup data file reference, available in your GCS or S3 bucket.

{% hint style="warning" %}
A gzip compressed file is expected.
{% endhint %}

Example:

```bash
gzip <backup file> -c > <backup file>.gz
```

* GCS\_URI/S3\_URI : the GCS/S3 bucket URI where the backup file is stored.

Format: `gs://BUCKET_NAME/` or `s3://BUCKET_NAME/`&#x20;

{% hint style="warning" %}
Make sure the `BUCKET_NAME` contains a trailing slash.
{% endhint %}

* BACKUP\_METHOD : the backup method used to create the backup file.\
  Available options: `mariabackup` , `mysqldump`\\
*   GCP\_SERVICE\_ACCOUNT\_BASE64/AWS\_ACCOUNT\_ACCESS\_KEY\_BASE64 : Your base64 encoded GCP service account or AWS account access key.

    Information on how to create a GCP service account [here](https://cloud.google.com/iam/docs/keys-create-delete) Storage Admin role is required for the service account attempting the restore.

    Sample GCP service account key and command to encode it:

```bash
echo -n ' { "type": "service_account", "project_id": "XXXXXXX", "private_key_id": "XXXXXXX", "private_key": "-----BEGIN PRIVATE KEY-----XXXXX-----END PRIVATE KEY-----", "client_email": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX.iam.gserviceaccount.com", "client_id": "XXXXXXX", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/XXXXXXXXXXXXXX.iam.gserviceaccount.com", "universe_domain": "googleapis.com" } ' | base64
```

Sample AWS account access key and command to encode it:

```bash
echo -n ' { [default] aws_access_key_id = XXXXXXXXXXXXXEXAMPLE aws_secret_access_key = XXXXXXXXXXXXX/XXXXXXXXXXXXX/XXXXXXXXXXXXXEXAMPLEKEY region = XXXXXXXXXXXXX } ' | base64
```
