---
description: >-
  List existing MariaDB Cloud restore operations via the SkySQL Backup API:
  GET /skybackup/v1/restores returns scheduled and completed restores with
  status and metadata.
---

# Restore Listing Examples

{% include "../../../.gitbook/includes/authentication.md" %}

In order to get all Restores scheduled in the past you need to make api call:

```
curl --location 'https://api.skysql.com/skybackup/v1/restores' \
     --header 'Accept: application/json' \--header 'X-API-Key: ${API_KEY}'
```

## Get Restore by ID

```bash
curl --location 'https://api.skysql.com/skybackup/v1/restores/<ID>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* ID : the MariaDB Cloud Restore ID.
* To get the restore id, check the above sample call listing all

Typical response of those two APIs should look like:

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
