---
description: >-
  Snapshot backup examples for MariaDB Cloud via the SkySQL Backup API:
  one-time and scheduled point-in-time persistent-volume snapshots for fast
  database restoration.
---

# Snapshot Backup Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## Snapshot Backup Scheduling

### **One-Time Snapshot Example**

#### Example: Creating a One-time Snapshot Backup

To create a one-time snapshot backup using the SkySQL API, use the following `curl` command:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
     --header 'Content-Type: application/json' \
     --header 'X-API-Key: $API_KEY' \
     --data '{
         "backup_type": "snapshot",
         "schedule": "once",
         "service_id": "$SERVICE_ID"
     }'
```

* **backup\_type**: Specifies the type of backup. In this case, it is set to "snapshot".
* **schedule**: Indicates the backup schedule. Here, it is set to "once" for a one-time execution.
* **service\_id**: The unique identifier for the service you want to back up.

Ensure to replace `$API_KEY` and `$SERVICE_ID` with your actual API key and service ID values.

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

### **Cron Snapshot Example**

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
     --header 'Content-Type: application/json' \
     --header 'X-API-Key: $API_KEY' \
     --data '{
        "backup_type": "snapshot",
        "schedule": "0 3 * * *",
        "service_id": "$SERVICE_ID"
    }'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbxxxxxx

{% hint style="info" %}
Backup status can be fetched using 'https://api.skysql.com/skybackup/v1/backups'. See the 'Backup Status' section for an example.
{% endhint %}
