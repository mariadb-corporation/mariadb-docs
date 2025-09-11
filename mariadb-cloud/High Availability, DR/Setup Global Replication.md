# Setup Global Replication
SkySQL offers a robust platform for managing databases in the cloud and supports Global Replication for various use cases including disaster recovery, cross-region failover and global distribution of data. In this guide, we’ll explore how to automate the creation, restoration and replication of SkySQL database services for global availability using the SkySQL API. We will use the following SkySQL resources for the setup:

- Provisioning APIs: To launch primary and secondary SkySQL services.
- Backup APIs: To backup the primary service and restore the data to the secondary service.
- Replication Procedures: To setup active replication between the primary and the secondary services.

### **Step 1: Generate SkySQL API Key**
1\. Go to the [User Profile](https://app.skysql.com/user-profile/api-keys/) page of the SkySQL Portal to generate an API key.
2\. Export the value from the token field to an environment variable $API_KEY

   ```bash
   $ export API_KEY='... key data ...'
   ```
    
The `API_KEY` environment variable will be used in the subsequent steps.

### **Step 2: Launch SkySQL Services**
Launch two SkySQL services - a Primary that your application(s) will connect to and a Secondary that will act as a globally available service. If you already have your Primary service running, you simply need to create a new Secondary service. 

!!! Note
    You can launch these services using the [Portal](https://app.skysql.com) or [Using the REST API](./Launch%20DB%20using%20the%20REST%20API) as shown below. Launching a new service will take about 5 minutes. 

1\. Following API requests will create two services in Google Cloud - 'skysql-primary' in the Virginia region and 'skysql-secondary' in the Oregon region. 

```bash
curl --location --request POST https://api.skysql.com/provisioning/v1/services \
   --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json" \
   --data '{
"service_type": "transactional",
"topology": "standalone",
"provider": "gcp",
"region": "us-east4",
"architecture": "amd64",
"size": "sky-2x8",
"storage": 100,
"nodes": 1,
"name": "skysql-primary",
"ssl_enabled": true
}'
```

```bash
curl --location --request POST https://api.skysql.com/provisioning/v1/services \
   --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json" \
   --data '{
"service_type": "transactional",
"topology": "standalone",
"provider": "gcp",
"region": "us-west1",
"architecture": "amd64",
"size": "sky-2x8",
"storage": 100,
"nodes": 1,
"name": "skysql-secondary",
"ssl_enabled": true
}'
```

2\. Each SkySQL service has a unique identifier. Please make note of the identifier shown in the API response. We will need it later.

### **Step 3: Backup the Primary and Restore to the Secondary Service**
In a real world scenario, the Primary service will contain data which will need to be restored to the Standby service before the replication can be set up. SkySQL performs full backup of your services every night. You can either use an existing nightly backup or create a schedule to perform a new full backup.

!!! Note
    Depending on the size of your databases, backing up a service can take substantial time. Creating a new backup is not necessary if you already have an existing full backup of your service. If you have a recent backup (usually available) you can skip the step. After we restore from the backup we have to replay all the subsequent DB changes from the Source DB 'binlog'. Binlogs expire in 4 days, by default. So, you cannot use a backup older than 4 days. 

1\. Use the following API to list backups associated with the Primary service. Replace {id} with the database id of the Primary service. Look for a "FULL" backup or "snapshot". 

   ```bash
   curl --location --request GET https://api.skysql.com/skybackup/v1/backups?service_id={id} \
      --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json"
   ```

You can also look for recent "FULL" backups from the [Portal](https://app.skysql.com/backups/service-backups). If not available you can also initiate a backup from the Portal or using the API below. 

1\. Use the following API to create a one-time schedule to perform a new full backup. Replace {id} with the id of the Primary service.

   ```bash
   curl --location --request POST https://api.skysql.com/skybackup/v1/backups/schedules \
      --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json" \
      --data '{
   "backup_type": "full",
   "schedule": "once",
   "service_id": "{id}"
   }'
   ```

2\. Each backup also has a unique identifier. Make note of the identifier shown in the API response. Now use the following API to restore the backup to the Secondary service. 

!!! Note
      Please note that restoring the backup on a SkySQL service will stop the service if it is running and will wipe out all existing data. 

Replace {backup-id} with the backup id that you want to restore and {service-id} with the id of the Secondary service.

   ```bash
   curl --location --request POST https://api.skysql.com/skybackup/v1/restores \
      --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json" \
      --data '{
   "id": "{backup-id}}",
   "service_id": "{service-id}"
   }'
   ```

!!! Note
      As of July 2024, you can only restore from Backups within the same Cloud provider. To restore to a different provider, you would need to explicitly Backup to your own S3/GCS bucket, copy the folder over to the other provider's bucket and initiate a Restore. Please refer to the [Backup Service](../Backup%20and%20Restore/README.md) docs.

!!! Note
      Once the restore is complete, the default username and password displayed in the "connect" window of the Secondary service will not work. Restore overwrites this information with the username and password of the Primary service. Hence, you will have to use Primary service's username and password to connect to the Secondary service.

### **Step 4: Set up Replication between the Primary and the Secondary**
1\. Since we want to set up replication between the two SkySQL services, the Secondary service should be able to connect to the Primary service. Add the Outbound IP address of the Secondary service to the Allowlist of the Primary service. Outbound IP can be obtained from the "Service Details" page in the SkySQL portal. Please add this IP to the allowlist of Primary service in the portal.

2\. Next, obtain the GTID position from which to start the replication by using the following API. Please replace {service_id} with the service id of the primary service.
```bash
curl --location --request GET "https://api.skysql.com/skybackup/v1/backups?service_id={service_id}" \
  --header "X-API-Key: ${API_KEY}" --header "Content-type: application/json" | jq
```
Make  note of the gtid position ("binlog_gtid_position") in the API response output. 

3\. Now configure the Secondary service by calling the following stored procedure. Replace 'host' and 'port' with the Primary service's hostname and port. Replace 'gtid' with the GTID position obtained from the previous step. Use true/false for whether to use SSL.

```bash
CALL sky.change_external_primary_gtid(host, port, gtid, use_ssl_encryption);
```
Alternatively, the above command can be used with "binlog_file" and "binlog_position" output from step #2 above. 

```bash
CALL sky.change_external_primary
  ('dbpwfxxxx.sysp0000.db1.skysql.com',
   3306,
   'mariadb-bin.000007',
   xxxxx,
   true);
```


If successful, you should see an output similar to below. 

```bash

+-----------------------------------------------------------------------------------------------------------------------------------------+
| Run_this_grant_on_your_external_primary                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+
| GRANT REPLICATION SLAVE ON *.* TO 'skysql_replication_dbpwxxxxx'@'174.x.x.x' IDENTIFIED BY 'xxxxxxxxxx'; |
+-----------------------------------------------------------------------------------------------------------------------------------------+
```

Please copy the "GRANT REPLICATION..." command from the output and run in the primary service. 

4\. Start replication and check status on the Secondary service using the following procedures:

```bash
CALL sky.start_replication();
CALL sky.replication_status();
```

5\. Once the replication is setup, verify the status of the new database service in the SkySQL console. Ensure that the service is replicating for your use case for global replication.

