---
description: >-
  Logical (mariadb-dump) backup examples for MariaDB Cloud via the SkySQL
  Backup API, with both one-time and scheduled backup workflows for SQL-level
  data export.
---

# Logical Backup Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## **Logical Dump Backup**

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "dump",
    "schedule": "once",
    "service_id": "dbtgf28044362"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

## Logical Cron Backup

To set up an cron _Logical(dump)_ backup, you need to make the following API call:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "dump",
    "schedule": "0 3 * * *",
    "service_id": "dbtgf28044362"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx

{% hint style="info" %}
Backup status can be fetched using 'https://api.skysql.com/skybackup/v1/backups'. See the 'Backup Status' section for an example.
{% endhint %}
