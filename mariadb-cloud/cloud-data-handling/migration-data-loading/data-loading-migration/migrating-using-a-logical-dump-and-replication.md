# Migrating Using a Logical Dump and Replication

To minimize downtime during migration, you can set up live replication from your source database to the MariaDB Cloud database.

## Prerequisites

1. An active MariaDB Cloud account. Identify requirements for your MariaDB Cloud implementation prior to [deployment](../../../cloud-usage/launch-page.md), including:

* Topology - Mariadb Server Single node or with Replica(s)
* Instance size
* Storage requirements
* Desired server version

2. An existing source database with the IP added to your MariaDB Cloud allowlist.

## Steps

{% stepper %}
{% step %}
### Dump Source Database

Take a dump of your source database using `mysqldump` or `mariadb-dump`. Include triggers, procedures, views, and schedules in the dump, and ignore the system databases to avoid conflicts with the existing MariaDB Cloud schemas.

```bash
mysqldump -u [username] -p -h [hostname] 
          --single-transaction 
          --master-data=2 
          --routines 
          --triggers 
          --all-databases 
          --ignore-database=mysql 
          --ignore-database=information_schema 
          --ignore-database=performance_schema 
          --ignore-database=sys > dump.sql
```
{% endstep %}

{% step %}
### Create Users and Grants Separately

To avoid conflicts with the existing MariaDB Cloud users, use `SELECT CONCAT` on your source database to create users and grants in separate files. Note that you may need to create the schema and table grants separately as well.

```
mysql -u [username] -p -h [hostname] \
      --silent \
      --skip-column-names \
      -e "SELECT CONCAT('CREATE USER \'', user, '\'@\'', host, '\' 
      IDENTIFIED BY PASSWORD \'', authentication_string, '\';') \
      FROM mysql.user;" > users.sql

mysql -h [hostname] -u [username] -p \
      --silent \
      --skip-column-names \
      -e "SELECT CONCAT('GRANT ', privilege_type, ' ON ', table_schema, '.* \
          TO \'', grantee, '\';') \
          FROM information_schema.schema_privileges;" > grants.sql

mysql -h [hostname] -u [username] -p \
      --silent \
      --skip-column-names -e "SELECT CONCAT('GRANT ', privilege_type, ' ON ', table_schema, '.', table_name, ' \
      TO \'', grantee, '\';') \
      FROM information_schema.table_privileges;" >> grants.sql
```
{% endstep %}

{% step %}
### **Import Dumps Into MariaDB Cloud**

Import the logical dumps (SQL files) into your MariaDB Cloud database, ensuring to load the user and grant dumps after the main dump.

```bash
mariadb -u [MariaDB Cloud username] -p -h [MariaDB Cloud hostname] --port 3306 --ssl-verify-server-cert < dump.sql
mariadb -u [MariaDB Cloud username] -p -h [MariaDB Cloud hostname] --port 3306 --ssl-verify-server-cert < users.sql
mariadb -u [MariaDB Cloud username] -p -h [MariaDB Cloud hostname] --port 3306 --ssl-verify-server-cert < grants.sql
```

If you encounter an error while importing your users, you may need to uninstall the `simple_password_check` plugin on your MariaDB Cloud instance.
{% endstep %}

{% step %}
### **Start Replication**

Turn on replication using MariaDB Cloud stored procedures. There are procedures allowing you to set and start replication. See our [documentation](../../../reference-guide/stored-procedures.md) for details. The `dump.sql` file you created in step 1 will contain the GTID and binary log information needed for the `change_external_primary` procedure.

```sql
CALL sky.change_external_primary(host VARCHAR(255), port INT, logfile TEXT, logpos LONG,
     use_ssl_encryption BOOLEAN );
CALL sky.replication_grants();
CALL sky.start_replication();
UNINSTALL PLUGIN simple_password_check;
```
{% endstep %}
{% endstepper %}

## Hints

### Performance Optimization During Migration

*   **Disable Foreign Key Checks**: Temporarily disable foreign key checks during import to speed up the process.

    ```sql
    SET foreign_key_checks = 0;
    ```
* **Disable Binary Logging**: If binary logging is not required during the import process, and you are using a standalone instance, it can potentially be disabled to improve performance. SkyDBA Services can assist with this as part of a detailed migration plan.

### Data Integrity and Validation

*   **Consistency Checks**: Perform consistency checks on the source database before migration. Use a [supported SQL client](../../../../Connecting%20to%20Sky%20DBs/) to connect to your MariaDB Cloud instance and run the following.

    ```sql
    CHECK TABLE [table_name] FOR UPGRADE;
    ```
*   **Post-Import Validation**: Validate the data integrity and consistency after the import.

    ```sql
    CHECKSUM TABLE [table_name];
    ```

### Advanced Migration Techniques

*   **Adjust Buffer Sizes**: Temporarily increase buffer sizes to optimize the import performance. This can be done via the Configuration Manager in the portal.

    ```ini
    innodb_buffer_pool_size = 2G
    innodb_log_file_size = 512M
    ```
*   **Parallel Dump and Import**: Use tools that support parallel processing for dumping and importing data.

    ```bash
    mysqldump -u [username] -p --default-parallelism=4 --add-drop-database \
        --databases [database_name] > dump.sql
    ```
* **Incremental Backups**: For large datasets, incremental backups can be used to minimize the amount of data to be transferred. SkyDBA Services can assist you with setting these up as part of a custom migration plan.

### Monitoring and Logging

* **Enable Detailed Logging**: Enable detailed logging while testing the migration process to monitor and troubleshoot effectively. The slow\_log can be enabled in the MariaDB Cloud configuration manager.
* **Resource Monitoring**: Use monitoring tools to track resource usage (CPU, memory, I/O) during the migration to ensure system stability. See our [monitoring documentation](../../../cloud-usage/service-monitoring-panels.md) for details.

## See Also

* [Backup with mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)
* [MariaDB Backup Documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore)
* [Advanced Backup Techniques](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/backup-optimization)
* [Migrate RDS MySQL to MariaDB Cloud using the AWS Data Migration Service (DMS)](../../../Data%20loading,%20Migration/migrate-rds-mysql-to-skysql-using-amazon-data-migration-service_whitepaper_1109.pdf)
