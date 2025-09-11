# Restore Delete Examples

<details>

<summary>Authentication</summary>

#### Go to the SkySQL [API Key management page](https://app.skysql.com/user-profile/api-keys) and generate an API keyExport the value from the token field to an environment variable $API\_KEYexport API\_KEY='... key data ...'Use it on subsequent request, e.g:    \`\`\`bash    curl --request GET 'https://api.skysql.com/skybackup/v1/backups/schedules' --header "X-API-Key: ${API\_KEY}"    \`\`\`

</details>

In order to delete an already scheduled Restore, users need to make the following API call:

```bash
curl --location --request DELETE 'https://api.skysql.com/skybackup/v1/restores/<ID>' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}'
```

* ID : the SkySQL Restore ID. To get the restore id, you can use the following API call:

```bash
curl --location 'https://api-test.skysql.com/skybackup/v1/backups?service_id=d<SERVICE_ID>' \
  --header 'Accept: application/json' \
  --header "X-API-Key: skysql.1zzz.mh2oe85a.5aXjdyqgef7facjgAQ6DcLlVfx8imkkybIan.87c113e7"
```

* SERVICE\_ID : SkySQL service identifier, format dbtxxxxxx. You can fetch your service ID from the Fully qualified domain name(FQDN) of your service.\
  E.g: in dbpgf17106534.sysp0000.db2.skysql.com, 'dbpgf17106534' is the service ID. You will find the FQDN in the [Connect window](https://app.skysql.com/dashboard)
