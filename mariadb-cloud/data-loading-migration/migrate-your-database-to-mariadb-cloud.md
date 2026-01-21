# Migrate your database to MariaDB Cloud

MariaDB Cloud provides a range of options to suit different migration scenarios.
<ul>
   <li> Databases can be migrated to MariaDB Cloud from many different database platforms, including Oracle, MySQL, PostgreSQL, Microsoft SQL Server, IBM DB2, and more. </li>
   <li> MariaDB Cloud supports migration from both on-premise and cloud-based infrastructure and provides a range of options to suit different migration scenarios. </li>
</ul>

Below are the most common scenarios for database migration to MariaDB Cloud.

---
## Prerequisites

1. An active MariaDB Cloud account. 
2. An existing source database with the IP added to your MariaDB Cloud allowlist.

<details>
<summary>Considerations</summary>
<br>

Ensure that your MariaDB Cloud servce deploymned configuration is compatible with your existing source database one, including:
<ul>
   <li><b>Deployment region</b> - Ensure that the MariaDB Cloud deployment region is the same as the source database region.</li>
   <li><b>Topology</b> - Mariadb Server Single node or with Replica(s)</li>
   <li> <b>Server version</b> - Ensure that the MariaDB Cloud server version is compatible with the source database version. </li>
   <li><b>Instance size</b> - Ensure that the MariaDB Cloud instance is compatible with the source database instance type and size</li>
   <li><b>Storage</b> - Ensure that the MariaDB Cloud storage type and size is compatible with the source database</li>
</details>
---

## CloudDBA Assisted Migration 

 - Existing customers can submit a [support case](https://support.skysql.com) to request assistance with a migration.
 - New customers can [contact us](mailto:support@skysql.com) to begin the migration planning process.

Our [CloudDBA team](https://skysqlinc.github.io/skysql-docs/FractionalDBA/) can help design a migration plan to suit your needs.

<details>
<summary>CloudDBA Assisted Migration Approach</summary>
<br>
 We use a multi-step process to assist customers with migrations:
<ul>
   <li><b>Assessment</b> of application requirements, inventory, and identified challenges</li>
   <li><b>Schema Migration</b> including tables, constraints, indexes, and views</li>
   <li><b>Application Code Migration</b> by porting and testing SQL and application code</li>
   <li><b>Data Migration and Replication</b> with import of data, with conversion to the new schema, and ongoing inbound replication of new data</li>
   <li><b>Quality Assurance</b> to assess data validity, data integrity, performance, accuracy of query results, stored code, and running code such as client applications, APIs, and batch jobs</li>
   <li><b>Cutover</b> including final database preparation, fallback planning, switchover, and decommissioning of old databases</li>
</br>
</details>
---

## Self-Service Migration to MariaDB Cloud

MariaDB Cloud provides two different options for self-service migration 

### Option 1: Migrate using the MariaDB Cloud REST API
MariaDB Cloud Managed Migration is a REST-based service that handles the migration process, including data migration, schema migration, and user migration. It provides a follow us steps to set up a live replication of your database to MariaDB Cloud and various insights to monitor the migration process.

- [Sky SQL Managed Migration Tutorial](./MariaDB Cloud-managed-migration.md)

### Option 2: Custom Migration

For most small, mid-size and large migrations MariaDB Cloud Managed Migration is the quickest and safest option. However, for large migrations or migrations with specific requirements, you and your team may require more flexibility and control over the migration process. In these cases, you and your team can design a custom migration plan considering the options suggested below.

- [Migrating Using a Logical Dump and Replication](https://skysqlinc.github.io/skysql-docs/Data%20loading,%20Migration/Migrating%20Using%20a%20Logical%20Dump%20and%20Replication/)
- [Importing data using Mariadb Import](./Install-mariadb-import.md)
- [Importing using CSV Data](./Import-CSV-data.md)
- [Replicating Data from an External DB](https://skysqlinc.github.io/skysql-docs/Data%20loading,%20Migration/Replicating%20data%20from%20external%20DB/)
