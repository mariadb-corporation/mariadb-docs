---
description: >-
  Binary log backup examples for MariaDB Cloud via the SkySQL Backup API:
  one-time and scheduled binary log capture for point-in-time recovery
  scenarios.
---

# Binary Log Backup Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## Binary Log Backup

### One-Time Binary Log

To set up an one-time _binary log_ backup:

````
```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "binarylog",
    "schedule": "once",
    "service_id": "$SERVICE_ID"
}'
````

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

### **Schedule Binary Log Backup**

To set up an cron _incremental_ backup:

```
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "binarylog",
    "schedule": "0 3 * * *",
    "service_id": "$SERVICE_ID"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx

{% hint style="info" %}
Backup status can be fetch using 'https://api.skysql.com/skybackup/v1/backups'. See the 'Backup Status' section for an example.
{% endhint %}
