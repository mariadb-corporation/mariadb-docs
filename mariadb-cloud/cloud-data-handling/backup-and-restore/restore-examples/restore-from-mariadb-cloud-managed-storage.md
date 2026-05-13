---
description: >-
  Restore a MariaDB Cloud database from a backup stored in the default MariaDB
  Cloud managed backup storage, using a SkySQL Backup API call with the backup
  identifier.
---

# Restore from MariaDB Cloud Managed Storage

You can restore your database from the backup located in the default SkySQL managed backup storage. Below is a sample restore call.

```bash
curl --location 'https://api.skysql.com/skybackup/v1/restores' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header "X-API-Key: ${API_KEY}" \
--data '{
  "key": "xxx:dbtgf28044362:xxx",
  "service_id": "<SERVICE_ID>"
}'
```

* SERVICE\_ID : SkySQL service identifier, format dbtxxxxxx. You can fetch your service ID from the Fully qualified domain name(FQDN) of your service.\
  E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)
* KEY : the SkySQL backup key. To get the backup key, you can use the following API call:

```bash
curl --location 'https://api-test.skysql.com/skybackup/v1/backups?service_id=d<SERVICE_ID>' \
  --header 'Accept: application/json' \
  --header "X-API-Key: skysql.1zzz.mh2oe85a.5aXjdyqgef7facjgAQ6DcLlVfx8imkkybIan.87c113e7"
```

Key Format: \w\*SERVICE\_ID\w\* , where \w\*: Matches zero or more alphanumeric characters.
