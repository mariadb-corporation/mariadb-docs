# Incremental Backup Examples

<details>

<summary>Authentication</summary>

#### Go to the SkySQL [API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API keyExport the value from the token field to an environment variable $API\_KEYexport API\_KEY='... key data ...'Use it on subsequent request, e.g:    \`\`\`bash    curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API\_KEY}"    \`\`\`

</details>

### Incremental Backup

Incremental backups can be taken once you have full backup. Read [here](https://mariadb.com/kb/en/incremental-backup-and-restore-with-mariabackup/) for more details.

#### One-time Incremental

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

* API\_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)
* SERVICE\_ID : SkySQL service identifier, format dbtxxxxxx. You can fetch the service ID from the Fully qualified domain name(FQDN) of your service. E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID.You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)

#### Cron Incremental

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

* API\_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
* SERVICE\_ID : SkySQL service identifier, format dbtxxxxxx

**Backup status can be fetched using 'https://api.skysql.com/skybackup/v1/backups'. See the 'Backup Status' section for an example.**
