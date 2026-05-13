---
description: >-
  Delete a scheduled MariaDB Cloud restore operation via the SkySQL Backup API
  using a DELETE call to /skybackup/v1/restores/<ID> with API-key
  authentication.
---

# Restore Delete Examples

{% include "../../../.gitbook/includes/authentication.md" %}

In order to delete an already scheduled Restore, users need to make the following API call:

```bash
curl --location --request DELETE 'https://api.skysql.com/skybackup/v1/restores/<ID>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* ID : the MariaDB Cloud Restore ID. To get the restore id, you can use the following API call:

```bash
curl --location 'https://api-test.skysql.com/skybackup/v1/backups?service_id=d<SERVICE_ID>' \
  --header 'Accept: application/json' \
  --header "X-API-Key: skysql.1zzz.mh2oe85a.5aXjdyqgef7facjgAQ6DcLlVfx8imkkybIan.87c113e7"
```

* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch your service ID from the Fully qualified domain name(FQDN) of your service.\
  E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)
