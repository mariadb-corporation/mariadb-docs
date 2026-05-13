---
description: >-
  Full physical backup examples for MariaDB Cloud via the SkySQL Backup API,
  with one-time and scheduled execution patterns for file-level MariaDB Server
  data backups.
---

# Physical Backup Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## Full Physical Backup Scheduling

### **One-Time Full Physical Backup Example**

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
     --header 'Content-Type: application/json' \
     --header 'X-API-Key: $API_KEY' \
      --data '{
       "backup_type": "full",
       "schedule": "once",
       "service_id": "$SERVICE_ID"
     }'"

```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

### **Cron Full Physical Example**

```bash
    curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
         --header 'Content-Type: application/json' \
         --header 'X-API-Key: $API_KEY' \
         --data '{
           "backup_type": "full",
           "schedule": "0 3 * * *",
           "service_id": "$SERVICE_ID"
         }'"
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : MariaDB Cloud service identifier, format `dbtxxxxxx`

{% hint style="info" %}
Backup status can be fetched using 'https://api.skysql.com/skybackup/v1/backups'. \
See the 'Backup Status' section for an example.
{% endhint %}
