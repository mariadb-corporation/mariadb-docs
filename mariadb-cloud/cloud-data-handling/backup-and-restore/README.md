---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Backup and Restore

## **MariaDB Cloud Snapshot Backups**

MariaDB Cloud database snapshots create a point-in-time copy of the database persistent volume. Compared to full backups, snapshots provide a faster method for restoring your database with the same data.&#x20;

Snapshots are incremental in nature. After the initial full snapshot of a database's persistent volumes, subsequent snapshots only capture and store the changes made since the last snapshot. This approach saves a lot of storage space and reduces the time it takes to create a snapshot database backup and the related cloud storage cost.&#x20;

Users have the flexibility to trigger a snapshot as per their scheduling requirements - either on-demand or according to a predefined schedule. The MariaDB Cloud snapshots benefit from MariaDB's backup stage flush to create a consistent backup of the database - database lock temporarily suspends write operations and replication for just a few seconds.&#x20;

In a Primary/Replica topology, snapshot backups are prioritized and performed on the replica node. This is to ensure that the primary server can continue to operate in read/write mode, as the backup process is carried out on the replica node. After the backup process on the replica is completed, replication resumes automatically.

{% hint style="danger" %}
Database snapshots are deleted immediately upon service deletion.
{% endhint %}

**Snapshot Backup Examples**

MariaDB Cloud supports database snapshot backups either on-demand or according to a pre-established schedule. Below are examples of how to schedule a snapshot backup using the MariaDB Cloud API.

* [Snapshot Backup Examples](backup-examples/snapshot-backup-examples.md)

### References

* [Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
* [Google Cloud Kubernetes Engine - Snapshot Persistent Volume](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/snapshot-persistentvolume)
* [Kubernetes - Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)
* [MariaDB - How Mariabackup Works/Create a Consistent Backup Point](mariadb-backup.md)

## **Full (physical) Backups**

Full backups create a complete backup of the database server into a new backup folder. It uses [mariabackup](mariadb-backup.md) under the hood. Physical backups are performed by copying the individual data files or directories. The physical backup uses backup stages to create a consistent backup of the database without requiring a global read lock for the entire duration of the backup, while allowing the database to continue processing transactions. Instead, the server read lock is only needed briefly during the BACKUP STAGE FLUSH stage, which flushes the tables to ensure that all of them are in a consistent state at the exact same point in time, independent of the storage engine. The database lock temporarily suspends write operations and replication; the duration of the lock is typically just a few seconds. In a Primary/Replica topology, backups are prioritized and performed on the replica node. This approach ensures that the primary server can continue to operate in read/write mode, as the backup process is carried out on the replica node. After the backup process on the replica is completed, replication resumes automatically.

### Full (physical) Backup Examples

MariaDB Cloud supports database physical backups either on-demand or according to a pre-established schedule. Below are examples of how to schedule a physical backup using the MariaDB Cloud API.

* [Physical Backup Examples](backup-examples/physical-backup-examples.md)

### **References**

[**mariabackup**](mariadb-backup.md)

## **Incremental Backups**

Incremental backups update a previous backup with any changes to the data that have occurred since the initial backup was taken. InnoDB pages contain log sequence numbers, or LSNs. Whenever you modify a row on any InnoDB table in the database, the storage engine increments this number. When performing an incremental backup, Mariabackup checks the most recent LSN for the backup against the LSNs contained in the database. It then updates any of the backup files that have fallen behind.

### **Incremental Backup Examples**

MariaDB Cloud supports database incremental backups either on-demand or according to a pre-established schedule. Below are examples of how to schedule an incremental backup using the MariaDB Cloud API.

* [Incremental Backup Examples](backup-examples/incremental-backup-examples.md)

## **Logical (Mariadb-dump) Backups**

Logical backups consist of the SQL statements necessary to restore the data, such as CREATE DATABASE, CREATE TABLE, and INSERT. This is done using mariadb-dump ([mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)) and is the most flexible way to perform a backup and restore, and a good choice when the data size is relatively small.

### Logical Backup Examples

MariaDB Cloud supports database logical backups either on-demand or according to a pre-established schedule. Below are examples of how to schedule a logical backup using the MariaDB Cloud API.

* [Logical Backup Examples](backup-examples/logical-backup-examples.md)

### References

[mariadb-dump](../migration-data-loading/data-loading/install-mariadb-dump.md)

## **BinaryLog Backups**

Binlogs record database changes (data modifications, table structure changes) in a sequential, binary format. You can preserve binlogs for setting up replication or to recover to a certain point-in-time.

BinaryLog Backup Examples

### **Additional Backup Options (with Examples)**

*   Replication as Backup: In situations where the service cannot be locked or stopped, or is under heavy load, performing backups directly on a primary server may not be the preferred option. Using a replica database instance for backups allows the replica to be shut down or locked, enabling backup operations without impacting the primary server.<br>

    > **Hint:** To implement this approach, the primary server replicates data to a replica. Backups are initiated from the replica to avoid disrupting the primary server. \
    > \
    > For detailed instructions on setting up replication with your MariaDB Cloud instance, click [here](../data-offloading/replicating-data-from-mariadb-cloud-to-external-database.md).


* Automatic Nightly Backups: Automated nightly backups include a full backup of every database in the service to ensure that your MariaDB Cloud Database service is backed up regularly. Nightly backups are running for every MariaDB Cloud database by default.
* Bring Your Own Bucket (BYOB): You can back up or restore data to/from your own bucket in either GCP or AWS. Sample GCP and AWS scripts can be found [here](restore-examples/restore-from-your-own-bucket.md).
* Point-in-time Recovery: You can restore from a full or a logical backup and then use a binlog backup to restore to a point-in-time.
* Secure Backup/Restores: Control backup/restore privileges by granting roles to users in MariaDB Cloud.
* Other Backup API Examples: Various API scripts providing examples of listing backups, checking backup statuses, and working with backup schedules can be found [here](backup-examples/other-backup-api-examples.md).

## Restores

### Warning

> Restoring from a backup will, by default, erase all data in your target DB service. If you are uncertain, it is advisable to first create a backup of the DB service before initiating the restore process. Consider restoring to a new database instance as a preferred approach. For restores other than logical dumps, the database being restored will be temporarily stopped during the restoration.

Users can instruct the restoration of their MariaDB Cloud Database from their own MariaDB Cloud storage or from an external storage they own. The restore API provides options for listing, adding, and deleting a scheduled restore operation.

### **List Restore Schedules**

MariaDB Cloud Users can fetch their already existing database restore schedules using the backup API. Check the provided API examples for details.

#### Restore List Examples

* [Restore Listing Examples](restore-examples/restore-listing-examples.md)

### **Create a Restore**

MariaDB Cloud Users can restore their databases using their own MariaDB Cloud managed backup storage or using an external storage they own. Check the provided service API examples for details.

#### Database Restore Examples

* [Restore Examples](restore-examples/)

### **Delete Restore Schedule**

MariaDB Cloud Users can delete their already defined database restore schedules with the provided service API.

#### Delete Restore Examples

* [Restore Delete Examples](restore-examples/restore-delete-examples.md)

### **GTID Considerations for Logical Dumps**

When restoring from a logical dump in MariaDB:

* The GTID state is not preserved by default in logical dumps
* If you're using replication, you'll need to:
  1. Either reset the GTID state after restore
  2. Or use `mysqldump --dump-slave` to include GTID information in the backup
* Consider using physical backups (mariabackup) instead, as they preserve GTID state

## Limitations

* Currently, MariaDB Cloud services deployed in Azure can only be backed up and restored using [MariaDB Cloud Snapshots](./#mariadb-cloud-snapshot-backups).
* MariaDB Cloud Managed backups can only be restored within the same cloud provider. If you need to restore to a MariaDB Cloud service hosted on a different cloud provider, you must export your backup to S3 or GCS storage and follow the steps described [here](restore-examples/restore-from-your-own-bucket.md).
