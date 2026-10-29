---
description: >-
  MariaDB Cloud backup and restore: snapshot, full physical, incremental,
  logical (mariadb-dump), and binary log backups, plus restore options from
  managed storage and external buckets.
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
* Bring Your Own Bucket (BYOB): You can back up or restore data to/from your own bucket in either GCP or AWS. For the AWS permissions that your bucket requires, see [External S3 Buckets](./#external-s3-buckets). Sample GCP and AWS scripts can be found [here](restore-examples/restore-from-your-own-bucket.md).
* Point-in-time Recovery: You can restore from a full or a logical backup and then use a binlog backup to restore to a point-in-time.
* Secure Backup/Restores: Control backup/restore privileges by granting roles to users in MariaDB Cloud.
* Other Backup API Examples: Various API scripts providing examples of listing backups, checking backup statuses, and working with backup schedules can be found [here](backup-examples/other-backup-api-examples.md).

## External S3 Buckets

Back up to your own Amazon S3 bucket (BYOB) with access keys that you supply when you create the backup schedule. The backup job uses these keys for every upload, inventory update, and restore.

### Required AWS permissions

Grant the IAM user that owns the access keys the following permissions:

| Permission | Resource | Used for |
| --- | --- | --- |
| `s3:ListBucket` | The bucket | Checking the bucket before each backup, finding the backup inventory, and listing backups for restore. |
| `s3:PutObject` | Objects in the bucket | Writing backup files, the backup inventory, and a small `.backup_manager` test object at the bucket path. |
| `s3:GetObject` | Objects in the bucket | Reading the backup inventory and backup files for the backup list and for restores. |
| `s3:AbortMultipartUpload` | Objects in the bucket | Cleaning up the incomplete parts of an upload that fails. Backup files are uploaded in multiple parts. |

The following IAM policy grants these permissions. Replace `YOUR_BUCKET_NAME` with the name of your bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListBackupBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    },
    {
      "Sid": "ReadWriteBackupObjects",
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject", "s3:AbortMultipartUpload"],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

{% hint style="warning" %}
Removing any of these permissions, or adding a bucket policy that denies them, can cause scheduled external backups to fail or stop appearing in the backup list. Without `s3:GetObject`, MariaDB Cloud cannot read the backup inventory, so existing backups might not appear in the backup list even though the files are still in your bucket.
{% endhint %}

{% hint style="info" %}
If you enter a path in the bucket URL, for example `s3://YOUR_BUCKET_NAME/backups`, MariaDB Cloud writes and reads only under that path. The `.backup_manager` test object, the `backup_manager/` inventory folder, and the backup folders all sit below it. You can limit the object permissions to that path.
{% endhint %}

{% hint style="info" %}
MariaDB Cloud doesn't delete or expire backup files in your bucket. Configure an S3 lifecycle rule to manage storage in your bucket, including a rule that aborts incomplete multipart uploads.
{% endhint %}

### Limitations

* **Server-side encryption headers:** MariaDB Cloud doesn't send the `x-amz-server-side-encryption` header when it uploads to your bucket. A bucket policy that denies `s3:PutObject` unless this header is present, for example one that requires `AES256`, causes backup uploads to fail. S3 already encrypts all new objects with SSE-S3 by default, with no request header required, so you don't need a policy that enforces the header.
* **AWS KMS encryption:** If your bucket's default encryption uses an AWS KMS key (SSE-KMS), the IAM user also needs the `kms:GenerateDataKey` and `kms:Decrypt` permissions on that key. Without them, uploads and restores fail even when the S3 permissions are correct.
* **IAM roles:** External S3 backups use IAM user access keys. Role-based access, such as cross-account role assumption, isn't supported.

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

### **Enterprise Cluster Backups**

Backup and restore operations for Enterprise Clusters must be cluster-aware to preserve synchronous consistency and avoid data divergence.

* **Snapshots:** Galera clusters default to cloud-native snapshot backups. Because Galera ensures write-set consistency, a snapshot from any single healthy node safely represents the entire cluster state.
* **Cluster Restores:** To ensure safe re-formation, restoring a Galera cluster initializes the backup on a single node to bootstrap the cluster. Once the primary node is healthy, MariaDB Cloud uses automated [State Snapshot Transfers (SST)](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) to bring the remaining nodes online and sync their state. You can restore a Galera snapshot to the existing service or to a new service.

* **Point-in-Time Recovery:** You can restore an [Enterprise Cluster](../../quickstart/enterprise-cluster.md) to a specific point in time between snapshots, in the same way as a Replicated service.

{% hint style="info" %}
**Snapshots Only**&#x20;

[MariaDB Enterprise Cluster](../../quickstart/enterprise-cluster.md) supports cloud-native snapshot backups only. Full (physical) backups and logical backups are not available for this topology.
{% endhint %}

## Limitations

* MariaDB Cloud services deployed in Azure can only be backed up and restored using [MariaDB Cloud Snapshots](./#mariadb-cloud-snapshot-backups).
* MariaDB Cloud Managed backups can only be restored within the same cloud provider. If you need to restore to a MariaDB Cloud service hosted on a different cloud provider, you must export your backup to S3 or GCS storage and follow the steps described [here](restore-examples/restore-from-your-own-bucket.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
