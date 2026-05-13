---
description: >-
  Incremental backup examples for MariaDB Cloud via the SkySQL Backup API;
  incremental backups require an existing full backup and capture only changes
  since the last backup.
---

# Incremental Backup Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## Incremental Backup

Incremental backups can be taken once you have full backup. Read [here](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup) for more details.

### One-Time Incremental

To set up an one-time _incremental_ backup, you need to make the following API call:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "incremental",
    "schedule": "once",
    "service_id": "$SERVICE_ID"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

### Cron Incremental

To set up an cron _incremental_ backup, you need to make the following API call:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "incremental",
    "schedule": "0 3 * * *",
    "service_id": "$SERVICE_ID"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx

{% hint style="info" %}
Backup status can be fetched using 'https://api.skysql.com/skybackup/v1/backups'. See the 'Backup Status' section for an example.
{% endhint %}
