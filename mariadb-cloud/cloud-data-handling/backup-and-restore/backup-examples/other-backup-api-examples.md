---
description: >-
  Additional MariaDB Cloud backup API examples for working with backup
  schedules: listing schedules within an organization and managing existing
  schedules.
---

# Other Backup API Examples

{% include "../../../.gitbook/includes/authentication.md" %}

## Working With Backup Schedules

### Getting Backup Schedules Inside the Organization

```bash
curl --location '<https://api.skysql.com/skybackup/v1/backups/schedules>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

#### **Getting all Backup Schedules per Service**

To get backup schedules for specific service :

```bash
curl --location '<https://api.skysql.com/skybackup/v1/backups/schedules?service_id=dbtgf28044362>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

#### **Getting Backup Schedules by ID**

To get specific backup schedule by id :

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules/200' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

#### **Updating Backup Schedules**

In the following example, we update the backup schedule to 9 AM UTC. Remember, you cannot change the schedules for one-time backups. To update specific backup schedule you need to make the following API call:

```bash
curl --location --request PATCH '<https://api.skysql.com/skybackup/v1/backups/schedules/215>' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
  "schedule": "0 9 ** *"
}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)
* SCHEDULE : Cron schedule, see [Cron](https://en.wikipedia.org/wiki/Cron)

#### **Deleting Backup Schedules**

To delete a backup schedule you need to provide the backup schedule id. Example of the api call below:

```bash
curl --location --request DELETE 'https://api.skysql.com/skybackup/v1/backups/schedules/215' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

### Backup Status

The following API illustrates how to get the available backups and status of backup jobs .

#### Listing all Backups Inside the Organization

Here is an example to fetch all the available Backups in your org:

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

#### Listing all Backups by Service

To list all backups available for your service :

```bash
curl --location 'https://api.skysql.com/skybackup/v1/backups?service_id=dbtgf28216706' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* API\_KEY : SKYSQL API KEY, see [MariaDB Cloud API Keys](https://app.skysql.com/user-profile/api-keys/)

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

The Backup id is the most important part of this data as you need to provide it in the restore api call to schedule restore execution.
