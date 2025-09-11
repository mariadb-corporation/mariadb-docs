# Restore Listing Examples

Authentication

Go to the SkySQL [API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API keyExport the value from the token field to an environment variable $API\_KEYexport API\_KEY='... key data ...'Use it on subsequent request, e.g:    \`\`\`bash    curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API\_KEY}"    \`\`\`In order to get all Restores scheduled in the past you need to make api call:curl --location 'https://api.skysql.com/skybackup/v1/restores' \\--header 'Accept: application/json' \\--header 'X-API-Key: ${API\_KEY}'

### Get Restore by ID

```bash
curl --location 'https://api.skysql.com/skybackup/v1/restores/<ID>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* ID : the SkySQL Restore ID. aTo get the restore id, check the above sample call listing all

Typical response of those two apis should look like:

In case restore is in progress:

```json
[
    {
        "id": 12,
        "service_id": "dbtgf28216706",
        "bucket": "gs://sky-syst0000-backup-us-84e9d84ecf265a/orgpxw1x",
        "key": "eda3b72460c8c0d9d61a7f01b6a22e32:dbtgf28216706:tx-filip-mdb-ms-0",
        "type": "physical",
        "status": "Running",
        "message": "server is not-ready"
    }
]
```

In case restore completed:

```json
[
    {
        "id": 13,
        "service_id": "dbtgf28216706",
        "bucket": "gs://sky-syst0000-backup-us-84e9d84ecf265a/orgpxw1x",
        "key": "dda9b72460c9c0d9d61a7f01b6a33e39:dbtgf28216706:tx-filip-mdb-ms-0",
        "type": "physical",
        "status": "Succeeded",
        "message": "Restore has succeeded!"
    }
]
```
