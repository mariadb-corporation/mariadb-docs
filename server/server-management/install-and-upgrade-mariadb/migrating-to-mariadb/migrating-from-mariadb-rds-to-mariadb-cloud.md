---
description: >-
  Guide for migrating from MariaDB RDS to MariaDB Cloud using AWS Database
  Migration Service (DMS).
hidden: true
---

# Migrating From MariaDB RDS to MariaDB Cloud

This guide covers migrating from a self-managed or AWS MariaDB RDS instance to MariaDB Cloud using [AWS Database Migration Service (DMS)](https://aws.amazon.com/dms/), utilizing binary log streaming for [Change Data Capture (CDC)](#user-content-fn-1)[^1] to enable a near-zero downtime cutover.

## Phase 1: Preparing Your Source and Target Environments

DMS reads changes from MariaDB using binary log replication. These settings must be in place before creating DMS endpoints or starting any task.

{% stepper %}
{% step %}
#### Source AWS MariaDB RDS Configuration

* Enable automated backups: Set _Backup Retention Period_ to at least 1 day.
* Create a custom parameter group: Apply the following parameters to ensure DMS can read row-level changes:
* `binlog_format = ROW`
* `binlog_row_image = FULL`
* `binlog_checksum = NONE`

<div align="left"><img src="../../../.gitbook/assets/unknown.png" alt="The DB instance parameter group displays mariadb118custom (In sync)." height="338" width="364"></div>

* Apply and reboot: Associate the custom parameter group with your RDS instance and **reboot** to finalize the `ROW` mode.
* Set log retention: Provide a buffer for DMS to read the continuous logs. Run this command:\
  `CALL mysql.rds_set_configuration('binlog retention hours', 24);`
* Verify that all of the following variables are set, by running the following statements:

{% code overflow="wrap" %}
```sql
MariaDB [(none)]> SHOW VARIABLES LIKE 'net%';
+-------------------+-------+
| Variable_name     | Value |
+-------------------+-------+
| net_buffer_length | 16384 |
| net_read_timeout  | 30    |
| net_retry_count   | 10    |
| net_write_timeout | 60    |
+-------------------+-------+

MariaDB [(none)]> SHOW VARIABLES LIKE 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+
```
{% endcode %}
{% endstep %}

{% step %}
#### MariaDB Cloud Target Configuration

* Create database: Log into MariaDB Cloud and run `CREATE DATABASE db_name;`.
* Create user (optional): Use the default user to create additional users with privileges (for instance, users in RDS, `dms_admin` etc.), setting the Allowed Host to `%` or to the specific IP of your DMS instance.
* Verify settings: Issue the same `SHOW VARIABLES` statements as in the previous step.
* Enable connectivity: Open the MariaDB Cloud allowlist during setup, narrow it to the _NAT Gateway EIP_ (or _DMS Public IP_) before go-live.

<div align="left"><img src="../../../.gitbook/assets/unknown (2).png" alt="Several IPs are whitelisted, including 13.205.232.134/32 labeled as AWS DMS, and 172.168.55.21/32 labeled as APP SERVER." height="246" width="417"></div>

{% hint style="info" %}
Note on Serverless: Unlike Provisioned instances, MariaDB Serverless creates temporary Elastic Network Interfaces (ENIs) in your subnets. These ENIs lack default Public IPs and cannot reach the internet via an Internet Gateway. A NAT Gateway in your VPC is required.
{% endhint %}
{% endstep %}
{% endstepper %}

## Phase 2: Provisioning the AWS DMS Networking and Compute

The replication instance is the compute resource that handles the data migration.

* Instance type: Using a _Provisioned_ instance is highly recommended for static IP stability.
* VPC architecture: Deploy resources within private subnets for enhanced security, utilizing a NAT Gateway to establish the required outbound internet connection to MariaDB Cloud.
* Public accessibility: Select _Publicly Accessible: Yes_ if your traffic is routing over the internet. Note the allocated _Public IP_ and add it to your MariaDB Cloud allowlist if you are not using an open `0.0.0.0/0` rule.

<div align="left"><img src="../../../.gitbook/assets/unknown (3).png" alt="AWS DMS Replication instances list - a provisioned instance named dmsprovisionedinstance is shown with Status = Available, Publicly accessible = Yes, and an assigned Public IP address." height="104" width="624"></div>

* Test Connections: Ensure both endpoints return a _Successful_ status.

<div align="left"><img src="../../../.gitbook/assets/unknown (4).png" alt="Successful connection test results in the DMS console. The endpoint identifier mdbprovisioned successfully connected via the dmsprovisionedinstance replication instance." height="171" width="624"></div>

{% hint style="info" %}
Serverless Limits: Similar to the target database, DMS Serverless relies on ENIs without Public IPs and inherently struggles to reach MariaDB Cloud over the internet without a properly configured NAT Gateway.
{% endhint %}

## Phase 3: Migrating Schema Definitions and Secondary Objects

AWS DMS only migrates table data and basic primary keys. It does not migrate secondary objects such as views, stored procedures, or triggers.

Export metadata from RDS source: Use `mariadb-dump` from your terminal to grab all schema objects except the table data. Run this command:

{% code overflow="wrap" %}
```bash
mariadb-dump 
  -h [RDS_HOST] -u [USER] -p 
  --no-data --no-create-info --routines --triggers 
  --databases db_name | sed -e 's/DEFINER=`[^`]*`@`[^`]*`//g'  > metadata.sql
```
{% endcode %}

## Phase 4: Configuring Migration Endpoints and Sync Tasks

Before creating endpoints, establish secure CA certificate trust between AWS DMS and your database servers.

### Source Endpoint (RDS)

1. Download the Global Bundle or Regional CA from the AWS RDS connection information section.

<div align="left"><img src="../../../.gitbook/assets/unknown (5).png" alt="Under Connect using > Code snippets, commands are provided: 
curl -o global-bundle.pem https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem and the corresponding mariadb connection string." height="279" width="520"></div>

2. In the DMS Console, go to _Certificates > Import Certificate_. Upload the `global-bundle.pem` file and rename it to `rds-source-ca`.
3. In the _Source Endpoint_ settings, select SSL mode: `verify-ca` and choose the `rds-source-ca` certificate. Point to your RDS endpoint using the MariaDB user.

<div align="left"><img src="../../../.gitbook/assets/unknown (6).png" alt="The Source engine is MariaDB RDS. The Server name points to an RDS AWS domain. Secure Socket Layer (SSL) mode is set to verify-ca and the imported CA certificate is uploaded from AWS MariaDB RDS." height="448" width="513"></div>

### Target Endpoint (MariaDB Cloud)

1. Download the MariaDB Cloud CA Certificate from your MariaDB Cloud portal (found in the Security or Connect tab).

<div align="left"><img src="../../../.gitbook/assets/unknown (7).png" alt="Primary Endpoint service details in MariaDB Cloud and a download link for the Certificate authority chain." height="332" width="376"></div>

2. Import this into the DMS Console as MariaDB Cloud-target-ca.
3. Create the Target Endpoint, select SSL mode: `verify-full`, and point it to the MariaDB Cloud endpoint on Port `3306`.

<div align="left"><img src="../../../.gitbook/assets/unknown (8).png" alt="The target engine is MariaDB Cloud. The Server name points to a .skysql.com domain. SSL mode is set to verify-full with the appropriate CA certificate uploaded from MariaDB Cloud." height="433" width="503"></div>

### Create the DMS Migration Task

* Migration type: Select Migrate existing data and replicate ongoing changes (enables Snapshot + Replica mode).
* Target table preparation mode: Choose _Drop tables on target_ if you want DMS to build the structures, or _Do nothing_ if you precreated the tables.
* Stop task after full load completes: Select _Don't stop_ so it transitions into CDC mode automatically.
* Include LOB columns in replication: Select _Limited LOB_ mode.
* Table Mappings: Add a selection rule with _Schema \<your Schema Name>_, _Table name_ `%`, and _Action Include_.
* Transformation Rules: Add rules here if you need to rename schemas (for instance, rename `sakila` to `sakila_prod`).
* _Premigration Assessment_: Enable this to let AWS check for potential issues (unsupported data types, missing primary keys) before launching.

## Phase 5: Live Replication, Target Cutover, and Decommissioning

1. Executing the _Snapshot + Replica:_ Select _Start on create_ to initiate the _Full Load_. Watch the _Full Load_ progress bar until it hits 100%. The task status will transition to _Load complete, replication ongoing_. From this point forward, any `INSERT` or `UPDATE` statement on the RDS source is replicated to MariaDB Cloud instantaneously.

<div align="left"><img src="../../../.gitbook/assets/unknown (9).png" alt="A task named provisioned-cdc-snap-r has a Status of Load completed, replication ongoing. The load progress reads 100% and CDC replication is active." height="126" width="458"></div>

2. Post-table migration (views, triggers, and procedures): AWS DMS does not migrate secondary objects. Once DMS shows the load is complete, apply the metadata you exported in Part 3 to your MariaDB Cloud Instance:

{% code overflow="wrap" %}
```bash
mariadb -h [MariaDB Cloud_HOST] -P 4000 -u [USER] -p db_name < metadata.sql
```
{% endcode %}

{% hint style="info" %}
Important CDC considerations for triggers: If you have triggers on the Target (MariaDB Cloud) that update other tables, DMS might accidentally trigger them again while replicating CDC events, causing duplicate data. It is best practice to keep triggers disabled on the target until the final cutover.
{% endhint %}

3. Cutover: Identify a low-traffic window, stop the application from writing to the RDS source, and wait for the CDC lag to hit zero. Update your connection strings to point to MariaDB Cloud, re-enable your triggers, and finally terminate the DMS task and infrastructure.

## Phase 6 (Optional): Reverse Replication

Switch master and slave to make MariaDB Cloud the master.

Establishe MariaDB SkySQL as the primary (master) and AWS RDS as the replica (slave).

1. Prepare MariaDB Cloud (new master)

Before RDS can follow MariaDB Cloud, the target environment must be configured to allow inbound replication.

* Add the AWS RDS _Public IP_ (or _NAT Gateway EIP_) to the SkySQL Allowlist (Port `3306`).
* Identity: Create a dedicated replication user on MariaDB Cloud (SkySQL):

{% code overflow="wrap" %}
```sql
CREATE USER 'repl_user'@'%' IDENTIFIED BY 'YourSecurePassword';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'repl_user'@'%';
```
{% endcode %}

* Checkpoint: Capture the current binary log coordinates to tell RDS where to start:

{% code overflow="wrap" %}
```sql
SHOW MASTER STATUS; -- note the file and position
```
{% endcode %}

2. Configure AWS RDS (new slave): Because RDS is a managed service, standard `CHANGE MASTER` statements are restricted. You must use AWS stored procedures.

* Initialize: Clear old migration metadata and point RDS to the SkySQL endpoint using the file and position from step 1:

{% code overflow="wrap" %}
```sql
CALL mysql.rds_set_external_master ('skysql-hostname.net', 4000, 'repl_user', 'YourSecurePassword', '[File_from_SkySQL]', [Position_from_SkySQL], 1 );
```
{% endcode %}

* Activate: Start the replication threads:

{% code overflow="wrap" %}
```sql
CALL mysql.rds_start_replication;
```
{% endcode %}

3. Monitoring & verification: The "source of truth" for the health of this link moves from the DMS Console to the database command line.

* Status check on RDS: Run `CALL mysql.rds_replica_status\G;` to verify connectivity.
* Success criteria: Ensure `Slave_IO_Running` is `Yes`, `Slave_SQL_Running` is `Yes`, and `Seconds_Behind_Master` is `0`.
* Status check on MariaDB Cloud: Run `SHOW MASTER STATUS\G` and `SHOW SLAVE STATUS\G` (this should return an empty set).

Decommissioning: Once `Seconds_Behind_Master` remains at `0`, the AWS DMS infrastructure is redundant. To eliminate unnecessary costs:

1. Stop and Delete the AWS DMS Task.
2. Terminate the DMS Replication Instance.
3. Delete the NAT Gateway (if no longer required for outbound RDS traffic).

{% hint style="info" %}
The DMS Task Console will now show _Zero Activity_ and may report _High Source Latency_. This is expected, as the data flow has successfully moved from the DMS pipe to native MariaDB replication.
{% endhint %}

[^1]: In databases, change data capture (CDC) is a set of software design patterns used to determine and track the data that has changed (the "deltas") so that action can be taken using the changed data. The result is a delta-driven dataset.
