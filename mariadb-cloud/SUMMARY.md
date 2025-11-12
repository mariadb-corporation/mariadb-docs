# Table of contents

* [MariaDB Cloud](README.md)
  * [Key Features & Capabilities](about/key-features-and-capabilities.md)
  * [MariaDB Cloud Serverless](about/serverless.md)
  * [MariaDB Cloud Serverless Architecture](about/architecture.md)
* [Quickstart Guides](Quickstart/README.md)
  * [Using the Portal](quickstart/using-the-portal.md)
  * [Launch DB Using REST API](<Quickstart/Launch DB using the REST API.md>)
  * [Launch DB Using Terraform Provider](<Quickstart/Launch DB using the Terraform Provider.md>)
  * [Launch DB Using Python](<Quickstart/Launch DB using Python.md>)
* [Connecting](connecting-to-mariadb-cloud-dbs/README.md)
  * [Connect using MariaDB Client](connecting-to-mariadb-cloud-dbs/connect-using-mariadb-cli.md)
  * [Connect From Node.js App](connecting-to-mariadb-cloud-dbs/connect-from-node-js-app.md)
  * [Connect From Java App](connecting-to-mariadb-cloud-dbs/connect-from-java-app.md)
  * [Connect From Python App](connecting-to-mariadb-cloud-dbs/connect-from-python-app.md)
  * [Connect From C App](connecting-to-mariadb-cloud-dbs/connect-from-c-app.md)
  * [Connect From C++ App](connecting-to-mariadb-cloud-dbs/connect-from-c++-app.md)
  * [Connect From MongoDB Clients](connecting-to-mariadb-cloud-dbs/connect-from-mongodb-clients.md)
  * [Connect Using ODBC](connecting-to-mariadb-cloud-dbs/connect-using-odbc.md)
  * [Connect Using Connector/R2DBC](connecting-to-mariadb-cloud-dbs/connect-using-connector-r2dbc.md)
  * [Using VPC Connections](connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/README.md)
    * [AWS Private Link](connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/setting-up-aws-private-link.md)
    * [GCP Private Service Connect](connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/setting-up-gcp-private-service-connect.md)
    * [Azure Private Link](connecting-to-mariadb-cloud-dbs/using-aws-azure-gcp-private-vpc-connections/setting-up-azure-private-link.md)
  * [Database Tools](connecting-to-mariadb-cloud-dbs/database-tools/README.md)
    * [DBeaver](connecting-to-mariadb-cloud-dbs/database-tools/dbeaver.md)
    * [DBGate](connecting-to-mariadb-cloud-dbs/database-tools/dbgate.md)
    * [HeidiSQL](connecting-to-mariadb-cloud-dbs/database-tools/heidisql.md)
    * [TablePlus](connecting-to-mariadb-cloud-dbs/database-tools/tableplus.md)
  * [Partner Integrations](connecting-to-mariadb-cloud-dbs/partner-integrations/README.md)
    * [MindsDB Partner Integration](connecting-to-mariadb-cloud-dbs/partner-integrations/mindsdb-partner-integration.md)
    * [Qlik Partner Integration](connecting-to-mariadb-cloud-dbs/partner-integrations/qlik-partner-integration.md)
    * [Striim Partner Integration](connecting-to-mariadb-cloud-dbs/partner-integrations/striim-partner-integration.md)
* [Management & Configuration](cloud-management/README.md)
  * [Configuring Database Servers](cloud-management/config/README.md)
    * [MariaDB Serverless Single Node](cloud-management/config/mariadb-serverless-single-node.md)
    * [MariaDB Server Single Node](cloud-management/config/mariadb-server-single-node.md)
    * [MariaDB Server With Replicas](cloud-management/config/mariadb-server-with-replica-s.md)
    * [MariaDB Cloud Intelligent Proxy](cloud-management/config/maxscale.md)
  * [Autonomously Scale Compute & Storage](cloud-management/autonomously-scale-compute-storage.md)
  * [Observability](cloud-management/observability.md)
* [Cloud UI Portal](cloud-usage/README.md)
  * [MariaDB Cloud UI Portal](cloud-usage/portal-features.md)
  * [Launch Page](cloud-usage/launch-page.md)
  * [Manage Your Service](cloud-usage/manage-your-service.md)
  * [Service Details Page](cloud-usage/service-details-page.md)
  * [Infrastructure Upgrades](cloud-usage/infrastructure-upgrades.md)
  * [Notifications](cloud-usage/notifications.md)
  * [Service Monitoring Panels](cloud-usage/service-monitoring-panels.md)
  * [Billing](cloud-usage/billing.md)
* [Data Loading & Backup](cloud-data-handling/README.md)
  * [Migration, Data Loading](cloud-data-handling/migration-data-loading/README.md)
    * [Migrations](cloud-data-handling/migration-data-loading/data-loading-migration/README.md)
      * [MariaDB Cloud Managed Migration](cloud-data-handling/migration-data-loading/data-loading-migration/mariadb-cloud-managed-migration.md)
      * [Migrating Using a Logical Dump and Replication](cloud-data-handling/migration-data-loading/data-loading-migration/migrating-using-a-logical-dump-and-replication.md)
    * [Data Loading](cloud-data-handling/migration-data-loading/data-loading/README.md)
      * [Import CSV Data](cloud-data-handling/migration-data-loading/data-loading/import-csv-data.md)
      * [Install mariadb-dump](cloud-data-handling/migration-data-loading/data-loading/install-mariadb-dump.md)
      * [Install mariadb-import](cloud-data-handling/migration-data-loading/data-loading/install-mariadb-import.md)
      * [Replicating Data From an External Database to MariaDB Cloud](cloud-data-handling/migration-data-loading/data-loading/replicating-data-from-external-db.md)
  * [Data Offloading](cloud-data-handling/data-offloading/README.md)
    * [Replicating Data From MariaDB Cloud to External Database](cloud-data-handling/data-offloading/replicating-data-from-mariadb-cloud-to-external-database.md)
  * [Backup and Restore](cloud-data-handling/backup-and-restore/README.md)
    * [Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/README.md)
      * [Snapshot Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/snapshot-backup-examples.md)
      * [Physical Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/physical-backup-examples.md)
      * [Logical Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/logical-backup-examples.md)
      * [Incremental Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/incremental-backup-examples.md)
      * [Binary Log Backup Examples](cloud-data-handling/backup-and-restore/backup-examples/binarylog-backup-examples.md)
      * [Other Backup API Examples](cloud-data-handling/backup-and-restore/backup-examples/other-backup-api-examples.md)
    * [Restore Examples](cloud-data-handling/backup-and-restore/restore-examples/README.md)
      * [Restore Listing Examples](cloud-data-handling/backup-and-restore/restore-examples/restore-listing-examples.md)
      * [Restore from MariaDB Cloud Managed Storage](cloud-data-handling/backup-and-restore/restore-examples/restore-from-mariadb-cloud-managed-storage.md)
      * [Restore From Your Own Bucket](cloud-data-handling/backup-and-restore/restore-examples/restore-from-your-own-bucket.md)
      * [Point-In-Time Restore](cloud-data-handling/backup-and-restore/restore-examples/point-in-time-restore.md)
      * [Restore Delete Examples](cloud-data-handling/backup-and-restore/restore-examples/restore-delete-examples.md)
    * [MariaDB Backup](cloud-data-handling/backup-and-restore/mariadb-backup.md)
* [AI Agents & Copilot](cloud-ai/README.md)
  * [AI Agents](cloud-ai/copilot-guide.md)
  * [AI Agents API User Guide](cloud-ai/ai-api-guide.md)
  * [MariaDB Cloud MCP Server](cloud-ai/mcp-server.md)
* [HA & DR](<High Availability, DR/README.md>)
  * [HA & Replicated Topology](high-availability-dr/ha-and-replicated-topology.md)
  * [Global Replication](<High Availability, DR/Setup Global Replication.md>)
* [Security](Security/README.md)
  * [Managing Portal Users](<Security/Managing Portal Users.md>)
  * [Configuring Firewall](<Security/Configuring Firewall.md>)
  * [Encryption](Security/Encryption.md)
  * [Managing API keys](<Security/Managing API keys.md>)
  * [Private VPC Connections](<Security/Private VPC connections.md>)
  * [Portal Single Sign-On](<Security/Portal Single Sign-On.md>)
* [Reference](reference/README.md)
  * [FAQs](reference-guide/faqs.md)
  * [MariaDB Cloud Uptime SLA](reference-guide/uptime-sla.md)
  * [Fractional DBA Service: Remote DBA](reference-guide/fractionaldba.md)
  * [MariaDB Server Version Support](reference-guide/mariadb-server-versions.md)
  * [Supported Backup Types](reference-guide/backup-support.md)
  * [MariaDB Cloud Instance Sizes](reference/mariadb-cloud-instance-sizes.md)
  * [MariaDB Cloud Monitoring Metrics Reference](reference/mariadb-cloud-monitoring-metrics-reference.md)
  * [MariaDB Cloud Region Choices](reference-guide/region-choices.md)
  * [MariaDB Cloud REST API Reference](reference-guide/rest-api-reference.md)
  * [MariaDB Cloud Stored Procedures](reference-guide/stored-procedures.md)
  * [MariaDB Cloud API Reference Guide](reference-guide/mariadb-cloud-api-reference-guide/README.md)
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
    * ```yaml
      props:
        models: true
      type: builtin:openapi
      dependencies:
        spec:
          ref:
            kind: openapi
            spec: mariadb-api
      ```
  * [Pricing](reference/pricing.md)
  * [Maintenance Windows](reference/maintenance-windows.md)
  * [MaxScale Redundancy](reference/maxscale-redundancy.md)
