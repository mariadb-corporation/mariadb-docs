---
title: Authentication
---

Go to the MariaDB Cloud [API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API key. Export the value from the token field to an environment variable `$API_KEYexport API_KEY='... key data ...'`

Use it on subsequent request, e.g: `bash curl --request`

```
GET 'https://api.skysql.com/skybackup/v1/backups/schedules' \
    --header "X-API-Key: ${API_KEY}"
```
