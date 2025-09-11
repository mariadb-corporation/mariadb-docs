# SkySQL Managed Migration

## Prerequisites

1. An active SkySQL account. Identify requirements for your SkySQL implementation prior to [deployment](../Portal%20features/Launch%20page.md), including:
    - Topology: Mariadb Server Single node or with Replica(s)
    - [Instance size](../Reference%20Guide/Instance%20Size%20Choices.md)
    - Storage requirements
    - Desired server version

2. An existing source database with the IP added to your SkySQL allowlist.

## Migration Steps

1. Dump using logical or physical backup. Refer to  the steps mentioned in the [Backup and Restore](../Backup%20and%20Restore/README.md) tutorial.

2. Upload the dump. Transfer the data dump to an S3/GCS bucket under your control.

3. Call the migration API. Refer to the [SkySQL Managed Migration Tutorial](../Backup%20and%20Restore/Restore%20From%20Your%20Own%20Bucket.md).

4. Start Replication. To minimize downtime during migration, set up live replication from your source database to your SkySQL database. Refer to the [Replicating data from external DB Tutorial](./Replicating%20data%20from%20external%20DB.md).
    
## Additional Resources
- [Backup with mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)
- [MariaDB Backup Documentation](https://mariadb.com/kb/en/mariadb-backup-overview/)
- [Advanced Backup Techniques](https://mariadb.com/kb/en/backup-and-restore-overview/)