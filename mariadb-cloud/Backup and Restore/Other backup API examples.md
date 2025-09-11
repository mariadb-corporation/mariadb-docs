<details>
<summary>
Authentication
</summary>
<h3>
<ol>
<li>
Go to the SkySQL <a href="https://app.skysql.com/user-profile/api-keys">API Key management page</a>  and generate an API key
</li>
<li>
Export the value from the token field to an environment variable $API_KEY

  ```
  export API_KEY='... key data ...'
  ```
</li>
<li>
Use it on subsequent request, e.g:

        ```bash
        curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API_KEY}"
        ```
</li>
</ol>
</details>  

## Working with Backup Schedules

### Get backup schedules inside the Organization :

```bash
curl --location '<https://api.skysql.com/skybackup/v1/backups/schedules>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)

#### Get all Backup Schedules per service

To get backup schedules for specific service :

```bash
curl --location '<https://api.skysql.com/skybackup/v1/backups/schedules?service_id=dbtgf28044362>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```
- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)

#### Get Backup Schedule by ID

To get specific backup schedule by id :

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules/200' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)


#### Update Backup Schedule

In the following example, we update the backup schedule to 9 AM UTC. Remember, you cannot change the schedules for one-time backups.
To update specific backup schedule you need to make the following API call:

```bash
curl --location --request PATCH '<https://api.skysql.com/skybackup/v1/backups/schedules/215>' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
  "schedule": "0 9 ** *"
}'
```
- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)
- SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)
  
#### Delete Backup Schedule

To delete a backup schedule you need to provide the backup schedule id. Example of the api call below:

```bash
curl --location --request DELETE 'https://api.skysql.com/skybackup/v1/backups/schedules/215' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)


## Backup Status 

The following API illustrates how to get the available backups and status of backup jobs .

### List all backups inside the organization

Here is an example to fetch all the available Backups in your org:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```
- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)

### List all backups by service

To list all backups available for your service :

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups?service_id=dbtgf28216706' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```
- API_KEY : SKYSQL API KEY, see [SkySQL API Keys](https://app.skysql.com/user-profile/api-keys/)


The typical response of either of two calls should look like:

```json
{
    "backups": [
        {
            "id": "eda3b72460c8c0d9d61a7f01b6a22e32:dbtgf28216706:tx-filip-mdb-ms-0",
            "service_id": "dbtgf28216706",
            "type": "full",
            "method": "skybucket",
            "server_pod": "tx-filip-mdb-ms-0",
            "backup_size": 5327326,
            "reference_full_backup": "",
            "point_in_time": "2024-03-26 17:18:21",
            "start_time": "2024-03-26T17:18:57Z",
            "end_time": "2024-03-26T17:19:01Z",
            "status": "Succeeded"
        }
    ],
    "backups_count": 1,
    "pages_count": 1
}
```

> The ** Backup id is the most important part of this data as you need to provide it in the restore api call** to schedule restore execution.
