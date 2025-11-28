# Point-In-Time Restore

{% include "../../../.gitbook/includes/authentication.md" %}

## Important Note

For Point-in-Time Restore to work, you must have a preconfigured backup schedule that ensures:

* Your backup schedule creates snapshot backups with a time gap shorter than your `expire_logs_days` database configuration setting (required for binary log availability)
* Your selected restore point must be between two consecutive snapshot backups from this schedule
* By default, MariaDB Cloud sets `expire_logs_days` to 4 days, but you can configure this value to match your backup schedule requirements

## Usage Examples

### API Example

```bash
curl --location 'https://api.skysql.com/skybackup/v1/restores' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header "X-API-Key: ${API_KEY}" \
--data '{
  "service_id": "<SERVICE_ID>",
  "id":"<BACKUP_SOURCE_SERVICE_ID>",
  "point_in_time":"<RESTORE_POINT_IN_TIME, UTC, FORMAT: YYYY-MM-DD HH:MM:SS>"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : MariaDB Cloud service identifier, format dbtxxxxxx. This is your restore target service
* BACKUP\_SOURCE\_SERVICE\_ID: MariaDB Cloud service identifier, format dbtxxxxxx. This is your backup source service id
* You can fetch the MariaDB Cloud service identifier from the Fully Qualified Domain Name (FQDN) of your service. For example: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

### MariaDB Cloud Portal Example

To perform a Point-in-Time Restore through the MariaDB Cloud Portal:

1. Navigate to Backups→Restores
2. Click the "Point-in-Time Restore" Button
3. In the restore form, provide:
   1. Database restore target service
   2. Backup source service
   3. Selected restoration point in time
4. Click the "Restore" button to start the restore process

## Limitations

* Cross-cloud restore is not supported. Your restore target service must be in the same cloud provider as your backup source service.
* Only MariaDB Cloud native snapshots can be used as restore source. External backups are not supported for Point-in-Time Restore.
* Point-in-Time Restore requires [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.8/10.8.6) or later, which introduced the binary log search functionality needed for this feature.
* Support for Serverless databases as Point-in-Time Restore sources is coming soon.
