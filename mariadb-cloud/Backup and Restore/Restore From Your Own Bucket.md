# Restore From Your Own Bucket

<details>

<summary>Authentication</summary>

#### Go to the SkySQL [API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API keyExport the value from the token field to an environment variable $API\_KEYexport API\_KEY='... key data ...'Use it on subsequent request, e.g:    \`\`\`bash    curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API\_KEY}"    \`\`\`

</details>

### Restore From your Bucket (External Storage)

You can restore your data from external cloud storage. SkySQL supports restoration from both Google Cloud Storage (GCS) and Amazon S3 cloud storage buckets. Your backup data should be created using either `mariabackup` or `mysqldump`.

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

* SERVICE\_ID : SkySQL serivce identifier, format dbtxxxxxx. You can fetch your service ID from the Fully qualified domain name(FQDN) of your service.\
  E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)
* ID : the backup data file reference, available in your GCS or S3 bucket.

!!! Note Gzip compressed file expected.

````
Example:
```bash
gzip <backup file> -c > <backup file>.gz
```
````

* GCS\_URI/S3\_URI : the GCS/S3 bucket URI where the backup file is stored.

Format gs://BUCKET\_NAME/ or s3://BUCKET\_NAME/ !!! Note Make sure the BUCKET\_NAME contains a trailing slash.

* BACKUP\_METHOD : the backup method used to create the backup file.\
  Available options: `mariabackup` , `mysqldump`\

*   GCP\_SERVICE\_ACCOUNT\_BASE64/AWS\_ACCOUNT\_ACCESS\_KEY\_BASE64 : Your base64 encoded GCP service account or AWS account access key.

    Information on how to create a GCP service account [here](https://cloud.google.com/iam/docs/keys-create-delete) Storage Admin role is required for the service account attemping the restore.

    Sample GCP service account key and command to encode it:

    echo -n ' { "type": "service\_account", "project\_id": "XXXXXXX", "private\_key\_id": "XXXXXXX", "private\_key": "-----BEGIN PRIVATE KEY-----XXXXX-----END PRIVATE KEY-----", "client\_email": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX.iam.gserviceaccount.com", "client\_id": "XXXXXXX", "auth\_uri": "[https://accounts.google.com/o/oauth2/auth](https://accounts.google.com/o/oauth2/auth)", "token\_uri": "[https://oauth2.googleapis.com/token](https://oauth2.googleapis.com/token)", "auth\_provider\_x509\_cert\_url": "[https://www.googleapis.com/oauth2/v1/certs](https://www.googleapis.com/oauth2/v1/certs)", "client\_x509\_cert\_url": "[https://www.googleapis.com/robot/v1/metadata/x509/XXXXXXXXXXXXXX.iam.gserviceaccount.com](https://www.googleapis.com/robot/v1/metadata/x509/XXXXXXXXXXXXXX.iam.gserviceaccount.com)", "universe\_domain": "googleapis.com" } ' | base64

    Sample AWS account access key and command to encode it:

    echo -n ' { \[default] aws\_access\_key\_id = XXXXXXXXXXXXXEXAMPLE aws\_secret\_access\_key = XXXXXXXXXXXXX/XXXXXXXXXXXXX/XXXXXXXXXXXXXEXAMPLEKEY region = XXXXXXXXXXXXX } ' | base64
