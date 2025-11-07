# MariaDB Cloud Managed Migration

## Prerequisites

1. An active MariaDB Cloud account. Identify requirements for your MariaDB Cloud implementation prior to [deployment](../../../cloud-usage/launch-page.md), including:
   * Topology: Mariadb Server Single node or with Replica(s)
   * Instance size
   * Storage requirements
   * Desired server version
2. An existing source database with the IP added to your MariaDB Cloud allowlist.

## Migration Steps

1. Dump using logical or physical backup. Refer to the steps mentioned in the [Backup and Restore](../../backup-and-restore/) tutorial.
2. Upload the dump. Transfer the data dump to an S3/GCS bucket under your control.
3. Call the migration API. Refer to the [MariaDB Cloud Managed Migration Tutorial](../../backup-and-restore/restore-examples/restore-from-your-own-bucket.md).
4. Start Replication. To minimize downtime during migration, set up live replication from your source database to your MariaDB Cloud database. Refer to the [Replicating data from external DB Tutorial](../data-loading/replicating-data-from-external-db.md).

## Additional Resources

* [Backup with mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)
* [MariaDB Backup Documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [Advanced Backup Techniques](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations)
