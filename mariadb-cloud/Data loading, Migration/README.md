# Migrations

SkySQL provides a range of options to suit different migration scenarios.

* Databases can be migrated to SkySQL from many different database platforms, including Oracle, MySQL, PostgreSQL, Microsoft SQL Server, IBM DB2, and more.
* SkySQL supports migration from both on-premise and cloud-based infrastructure and provides a range of options to suit different migration scenarios.

Below are the most common scenarios for database migration to SkySQL.

***

## Prerequisites

1. An active SkySQL account.
2. An existing source database with the IP added to your SkySQL allowlist.

<details>

<summary>Considerations</summary>

\


Ensure that your SkySQL servce deploymned configuration is compatible with your existing source database one, including:

* Deployment region - Ensure that the SkySQL deployment region is the same as the source database region.
* Topology - Mariadb Server Single node or with Replica(s)
* Server version - Ensure that the SkySQL server version is compatible with the source database version.
* Instance size - Ensure that the SkySQL instance is compatible with the source database instance type and size
* Storage - Ensure that the SkySQL storage type and size is compatible with the source database

</details>

\---

## SkyDBA Assisted Migration

* Existing customers can submit a [support case](https://support.skysql.com) to request assistance with a migration.
* New customers can [contact us](mailto:support@skysql.com) to begin the migration planning process.

Our [SkyDBA team](https://skysqlinc.github.io/skysql-docs/FractionalDBA/) can help design a migration plan to suit your needs.

<details>

<summary>SkyDBA Assisted Migration Approach</summary>

\
We use a multi-step process to assist customers with migrations:

* Assessment of application requirements, inventory, and identified challenges
* Schema Migration including tables, constraints, indexes, and views
* Application Code Migration by porting and testing SQL and application code
* Data Migration and Replication with import of data, with conversion to the new schema, and ongoing inbound replication of new data
* Quality Assurance to assess data validity, data integrity, performance, accuracy of query results, stored code, and running code such as client applications, APIs, and batch jobs
* Cutover including final database preparation, fallback planning, switchover, and decommissioning of old databases
* \


</details>

\---

## Self-Service Migration to SkySQL

SkySQL provides two diffeent options for self-service migration

### Option 1: Migrate using the SkySQL REST API

SkySQL Managed Migration is a REST-based service that handles the migration process, including data migration, schema migration, and user migration. It provides a follow us steps to set up a live replication of your database to SkySQL and various insights to monitor the migration process.

* [Sky SQL Managed Migration Tutorial](SkySQL-managed-migration.md)

### Option 2: Custom Migration

For most small, mid-size and large migrations SkySQL Managed Migration is the quickest and safest option. However, for large migrations or migrations with specific requirements, you and your team may require more flexibility and control over the migration process. In these cases, you and your team can design a custom migration plan considering the options suggested below.

* [Migrating Using a Logical Dump and Replication](https://skysqlinc.github.io/skysql-docs/Data%20loading,%20Migration/Migrating%20Using%20a%20Logical%20Dump%20and%20Replication/)
* [Importing data using Mariadb Import](Install-mariadb-import.md)
* [Importing using CSV Data](Import-CSV-data.md)
* [Replicating Data from an External DB](https://skysqlinc.github.io/skysql-docs/Data%20loading,%20Migration/Replicating%20data%20from%20external%20DB/)
