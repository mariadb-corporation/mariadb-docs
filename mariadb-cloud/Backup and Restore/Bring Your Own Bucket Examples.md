
<details>
<summary>
Authentication
</summary>
<h3>
<ol>
<li>
Go to the SkySQL <a href="https://app.skysql.com/user-profile/api-keys">API Key management page</a>  and generate an API key
</li>
<li>
Export the value from the token field to an environment variable $API_KEY

  ```
  export API_KEY='... key data ...'
  ```
</li>
<li>
Use it on subsequent request, e.g:

        ```bash
        curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API_KEY}"
        ```
</li>
</ol>
</details>  

## Scheduling Backups to your own bucket (external storage)

To set up an external storage backup, you need to make the following API call:

- For *GCP* you need to create an service account key. Please follow the steps from this [documentation](https://cloud.google.com/iam/docs/keys-create-delete). Once you have created the service account key you will need to base64 encode it. You can encode it directly from a command line itself. For example the execution of command ```echo -n 'service-account-key' | base64``` will produce something like ```c2VydmljZS1hY2NvdW50LWtleQ==```

    ```bash
    curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'X-API-Key: ${API_KEY}' \
    --data '{
        "backup_type": "full",
        "schedule": "0 2 * * *",
        "service_id": "dbtgf28044362",
        "external_storage": {
            "bucket": {
                "path": "s3://my_backup_bucket",
                "credentials": "c2VydmljZS1hY2NvdW50LWtleQ=="
            }
        }
    }'
    ```

    The service account key will be in the following format:

    ```json
    {
        "type": "service_account",
        "project_id": "XXXXXXX",
        "private_key_id": "XXXXXXX",
        "private_key": "-----BEGIN PRIVATE KEY-----XXXXX-----END PRIVATE KEY-----",
        "client_email": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX.iam.gserviceaccount.com",
        "client_id": "XXXXXXX",
        "auth_uri": "<https://accounts.google.com/o/oauth2/auth>",
        "token_uri": "<https://oauth2.googleapis.com/token>",
        "auth_provider_x509_cert_url": "<https://www.googleapis.com/oauth2/v1/certs>",
        "client_x509_cert_url": "<https://www.googleapis.com/robot/v1/metadata/x509/XXXXXXXXXXXXXX.iam.gserviceaccount.com>",
        "universe_domain": "googleapis.com"
    }
    ```

- For AWS, you must provide your own credentials. These include the AWS access key associated with an IAM account and the bucket region. For more information about AWS credentials, please refer to the [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). The required credentials are *aws_access_key_id* , *aws_secret_access_key* and *region*. For example your credentials should look like:

    ```bash
    [default]
    aws_access_key_id = AKIAIOSFODNN7EXAMPLE
    aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    region = us-west-2
    ```

    You should encode your credentials base64 before passing it to the API. You can encode it directly from a command line itself. For example the execution of command ```echo '[default]\naws_access_key_id = AKIAIOSFODNN7EXAMPLE\naws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\nregion = us-west-2' | base64``` will produce the following ```W2RlZmF1bHRdCmF3c19hY2Nlc3Nfa2V5X2lkID0gQUtJQUlPU0ZPRE5ON0VYQU1QTEUKYXdzX3NlY3JldF9hY2Nlc3Nfa2V5ID0gd0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQpyZWdpb24gPSB1cy13ZXN0LTIK```.
    Using encoded credentials you will be able to pass it to the API server. To initiate a new backup to your external storage you need to execute an API call to the backup service:

    ``````bash
    curl --location '<https://api.skysql.com/skybackup/v1/backups/schedules>' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'X-API-Key: ${API_KEY}' \
    --data '{
        "backup_type": "full",
        "schedule": "0 2 ** *",
        "service_id": "dbpgf28044362",
        "external_storage": {
            "bucket": {
                "path": "s3://my_backup_bucket",
                "credentials": "W2RlZmF1bHRdCmF3c19hY2Nlc3Nfa2V5X2lkID0gQUtJQUlPU0ZPRE5ON0VYQU1QTEUKYXdzX3NlY3JldF9hY2Nlc3Nfa2V5ID0gd0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQpyZWdpb24gPSB1cy13ZXN0LTIK"
            }
        }
    }'
    ```