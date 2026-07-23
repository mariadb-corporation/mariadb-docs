---
description: >-
  Introduces MariaDB catalogs, a multi-tenancy feature that lets a single server
  host multiple independent tenants, each with their own users, schemas, and
  logs.
---

# Catalogs Overview

{% include "../../../.gitbook/includes/catalogs.md" %}

MariaDB catalogs will be a multi-tenancy feature where a single instance MariaDB server handles multiple independent tenants (customers), who have their own users, schemas etc.\
See [MDEV-31542](https://jira.mariadb.org/browse/MDEV-31542) "Add multi-tenancy catalogs to MariaDB" for details.

## Background

For hosting providers, a common solution, to drive down cost, is to have one MariaDB server support several different customers by creating one named schema for each of them.

This has however a lot of limitations:

* The user cannot have exactly the same schema(s) on the cloud as they have on premise.
* The user cannot use multiple schemas.
* The user cannot take a backup of all their data (not even with [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)). This is because the ‘mysql’ schema, which includes users, stored procedures etc. cannot be copied as its data is shared among all server users.
* The user cannot access the [general](../../../server-management/server-monitoring-logs/general-query-log.md) or [error log](../../../server-management/server-monitoring-logs/error-log.md).

The other option is to have a MariaDB container for each tenant. The problem with this is that, because of the memory needed per container, one can only have a very limited number of tenants per computer.

The suggested solution is to solve all of the above and thus create a better multi-tenant database is to add support for catalogs to MariaDB.

The following picture shows the change:

```mermaid
flowchart TB
    accTitle: Moving to catalogs
    accDescr {
        A comparison of multi-tenant approaches. In the container or VM approach, one physical
        machine runs several containers or virtual machines, each with its own database,
        requiring at least 1 GB per VM. In the shared-server, separate-schema approach, a single
        MySQL or MariaDB server holds one schema per customer, so customers have a limited number
        of schemas. The catalogs approach places many customer catalogs on a single MariaDB
        server, and each catalog can contain many schemas for a single customer, such as WebApp,
        WordPress, Messaging, Historical Data, Analytics, and MySQL schemas.
    }
    subgraph VM["Container / VM approach — 1 GB minimum per VM"]
        VM1[("Container or VM<br/>database")]
        VM2[("Container or VM<br/>database")]
        VM3[("Container or VM<br/>database")]
    end
    subgraph SH["Shared Server / Separate Schema — customers have limited schemas"]
        SHDB[("MySQL / MariaDB Server")]
        SHDB --- S1["Schema Customer 1"] & S2["Schema Customer 2"] & S3["Schema Customer 3"] & S4["Schema Customer 4"] & S5["Schema Customer 5"] & SMY["MySQL schema"]
    end
    subgraph CAT["Catalogs — many customer catalogs on one MariaDB server"]
        CATDB[("MariaDB Server")]
        CATDB --- C1["Catalog Customer 1"] & C2["Catalog Customer 2"] & C3["Catalog Customer 3"] & C4["Catalog Customer 4"] & C5["Catalog Customer 5"] & C6["Catalog Customer 6"]
    end
    subgraph ONE["Catalog for a single customer"]
        W["WebApp Schema"]
        WP["WordPress Schema"]
        MSG["Messaging Schema"]
        HD["Historical Data Schema"]
        AN["Analytics Schema"]
        CMY["MySQL schema"]
    end
    VM -->|Catalogs| CAT
    SH -->|Catalogs| CAT
    C3 -.-> ONE
    classDef db fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef schema fill:#eaeaf5,stroke:#5b4b8a,stroke-width:2px,color:#111;
    class VM1,VM2,VM3,SHDB,CATDB db
    class S1,S2,S3,S4,S5,SMY,C1,C2,C3,C4,C5,C6,W,WP,MSG,HD,AN,CMY schema
```

_Moving to catalogs: instead of one VM or one schema per customer, a single MariaDB server hosts many customer catalogs, and each catalog holds all of that customer's schemas._

By each user having their own catalog, they will get very close to the same user experience as if they would have the MariaDB server for themselves.

Catalogs make it possible for hosting providers to have 10-100x more 'not that active' database users on a server compared to having a container or MariaDB server per customer (which limits a 192G server to about 100 customers with a 1G InnoDB buffer each).

## User Experience With Catalogs

* Each user is assigned one catalog. The user can specify their catalog in their my.cnf file or as an argument to clients or when connecting to MariaDB server.
* Users can [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) of all their tables (including the ‘mysql’ database) and apply it on their own on premise MariaDB or to another ‘MariaDB catalog’ to duplicate their setup.
* Each catalog has its own privilege system. This allows a MariaDB admin to create users independently in their catalog to users in any other catalog. This also implies that the catalog has to be part of the connect information as otherwise the server does not know which user table to use.
* If the user is using applications that don’t yet support catalogs, they can specify the catalog as part of the database when connecting to the server ('catalog.database') or by connecting to a specific port that is associated with a catalog.
* After logging in, a normal user can only see the objects (databases, tables, users etc) from their database. They cannot access other catalogs or change catalogs.
* A normal user cannot change the active catalog with a command. They need to logout from the current catalog and login to another.

For the end user, the MariaDB server will act as a normal a standalone server, with the following differences:

* When connecting to the server, a normal user must specify the catalog. If the connector software does not support catalogs, then the catalog should be specified in the database string. If the catalog is not specified, the 'def' catalog is assumed.
* [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) and [SELECT … INTO OUTFILE](../../../reference/sql-statements/data-manipulation/selecting-data/select-into-outfile.md) can be configured to only be used with the catalog directory or a directory in it.
* [SHUTDOWN](../../../reference/sql-statements/administrative-sql-statements/shutdown.md) command is only for the 'catalog root users'
* Replication (MASTER and SLAVE commands) are only for 'catalog root users'
* Errors from background task (like write error) will be logged into the system error log, not the catalog error log.
* [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) will show status data for the whole server, not only for the active catalog.
* The server will handle legacy applications by extending the default database in the connection to contain the catalog in the form “catalog/database”. See Appendix for details.
* Tables that are only read from the ‘def.mysql’ schema:
  * [plugin](../../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md)
  * [help\_\*](../../../reference/system-tables/the-mysql-database-tables/mysql-help_category-table.md) tables
  * [time\_zone\*](../../../reference/system-tables/the-mysql-database-tables/mysql-time_zone_name-table.md) tables
  * [gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) (replication state)
  * [innodb\_index\_stats](../../../reference/system-tables/the-mysql-database-tables/mysql-innodb_index_stats.md) (innodb internal)
  * [servers](../../../reference/system-tables/the-mysql-database-tables/mysql-servers-table.md) (federated)
  * [transaction\_registry](../../../reference/system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md) (innodb internal)
  * [func](../../../reference/system-tables/the-mysql-database-tables/mysql-func-table.md) (udf)
  * [performance\_schema](../../../reference/system-tables/performance-schema/)

## New 'catalog root user'

* The 'def' catalog is reserved to store permissions for 'catalog root users', which can access any catalog. \* These are meant for admin users that need to do tasks like shutdown, upgrade, create/drop\
  catalogs, managing primaries and replicas etc.
* Only the ‘catalog root user’ can change to another catalog with ‘set catalog catalog\_name’.
* A normal user can do ‘set catalog current-catalog’. This will be needed to be able to execute a [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) that includes this command.

## New Storage Layout

MariaDB server will be able to run either on 'original mode', where the data layout is exactly as it was before, or on 'catalog' mode, with a new data layout:

When running [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) with --use-catalogs, it will create\
the following new data structure:

* data\_directory/
  * engine system data files
  * system files
  * replication files
  * general.log
  * error.log
  * mariadb/
    * mysql/
    * privilege tables
  * catalog1
  * general.log
  * error.log
  * mysql/
    * privilege tables
  * database1/
    * tables for database1
  * database2/
    * tables for database2
  * catalog2/
    * general.log
    * error.log
  * mysql/
    * privilege tables
  * database1/
    * tables for database1
  * database2/
    * tables for database2

The disk structure when not using catalogs is:

* data\_directory/
  * engine system data files
  * system files
  * replication files
  * general.log
  * error.log
  * mysql/
    * privilege tables
  * database1/
    * tables for database1
  * database2/
    * tables for database2

The above shows:

* There is a 'mariadb' catalog that stores admin users that can access all catalogs, shutdown servers, create new catalogs etc. The 'system root' user uses this when connecting.
* Each catalog has their own users, privilege tables, databases, error log and general logs

The MariaDB server will automatically start in catalog mode if it notices the new directory structure.

## Catalog SQL Commands/Functions

* [USE CATALOG catalog\_name](use-catalog.md);
* CREATE CATALOG
* [DROP CATALOG](drop-catalog.md)
* ALTER CATALOG
* SHOW CATALOGS (and also information\_schema.catalogs)
* SHOW CREATE CATALOG catalog\_name;
* SELECT CATALOG();

## Changes Needed in MariaDB Codebase

Client changes:

* Add --catalog option to all standard MariaDB clients
* Add support for looping over all existing catalogs to:
  * [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)
  * [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/)
  * [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md)

Changes to [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md):

* Allow one to create multiple catalogs at once: -–catalogs=”catalog1,catalog2”
* Init MariaDB with catalog support: —use-catalogs

Changes to mariadb (mysql client):

* Add support for 'USE CATALOG xxx’' (and later 'use database xxx').

Changes to mysql-test-run:

* Add support of running tests with catalogs (normal tests are run without catalogs)

Changes to MariaDB server (See [MDEV-31542](https://jira.mariadb.org/browse/MDEV-31542)):

* Add support for 'catalog' in the connection string. For old clients, the user can specify the catalog as part of the database. If catalog is not specified, the 'def' catalog (like now) is assumed.
* Add CATALOG() function that returns the current catalog.
* Add ‘USE CATALOG xxx’
* Add 'USE DATABASE xxx'
* Create a global CATALOG object to hold all information related to the catalog.
* Add the current catalog to the 'thd' object.
* Add catalog argument to all functions that take 'database' as an argument.
* Add SHOW CATALOGS and information\_schema.catalogs
* Move all relevant global variables (users, privileges, mdl-locks(?), open log files) to be stored in the CATALOG structure.
* Add 'catalog privilege', for ‘catalog super users’ to allow them to access data in any catalog.
* Add support for accessing tables with 'catalog.schema.table' (needed for catalog super users).
* For normal users, only show processes for the current catalog in 'show processlist'.
* Add loops over all catalogs for information schema for the 'catalog root user'.
* Update performance schema to take catalogs into account.
* Work with external connectors to get them to support connecting with a catalog.
* Check/update all storage engines to ensure they work also with catalogs.

Notes:

* The storage handler calls will probably not be changed. The storage engine will get the catalog name as part of the database name (catalog/database).
* We don't need a 'catalog' column for tables in the 'mysql' schema (like mysql.proc) as these are stored per catalog.

## Some Implementation Ideas

* Instead of sending a catalog string to function, use a pointer to the global catalog object. Do the same later for databases. This allows use to precompute things like 'filename' for catalogs and databases and we don't have to do this for every table open. It also allows us to later support logging information at a catalog and database level.
* Don't take a MDL lock for the catalog for each table. The metadata lock for the catalog will be taken when a user logs in or changes catalog.
* Add system variables ‘current\_catalog’ and ‘current\_database’ and allow users to change these.
* Add support for ‘catalog ports’ that are connected to catalog. This allows users to connect to a specific catalog from any client software.

## Limitations (in addition to limitations listed in “User experience with catalogs”)

* Database names cannot contain ‘.’ when connecting from clients without the new catalog connect option.
* One cannot refer to other catalogs in triggers, stored procedures, events etc. This is because a transaction cannot span catalogs.
* Only the catalog root user can use mariadb-backup. This is a normal restriction as one has to be system root to be able to use mariadb-backup.
* Events are global (to save resources). Catalog users can enable/disable events for their catalog.

## Stage 2 (not in first release)

* Support usage statistics per catalog and whole server (the last for the ‘catalog root user’). This allows the DBA to see the number of queries, type of queries etc. Some ‘system’ and ‘global innodb’ statistics will only be shown globally (number of open files, number of sync calls etc).
* Support a my.cnf file in each catalog directory to handle catalog (customer) unique defaults.
* Add quotas per catalog for tables and temporary files.
* Add more support to limit users from overusing resources (cpu, tables, databases, number of connections etc)
* Support 'drop catalog'. (This is in Stage 2 as there may be some issues to drop already active CATALOG objects)
* Add optional catalog support to the S3 engine
* More things will be added later.

## Stage 3

* Allow users to manage their own replication stream (maybe?).
* Allow users to have different options for the S3 engine
* More things will be added later.

Appendix

Legacy Connector Support

SQLALchemy test:

```
In [1]: from sqlalchemy.engine import make_url
In [2]: u = make_url('mariadb+mariadbconnector://app_user:Password123!@127.0.0.1:3306/catalog/company')
In [3]: u.database
Out[3]: 'catalog/company'
```

The following tests ensured that inside the server (mysql\_change\_db), the “catalog/test” was picked up as the database.

PHP PDO test:

```bash
$ php -r '$db = new \PDO("mysql:host=localhost;user=dan;dbname=catalog/test;charset=utf8mb4;unix_socket=/tmp/build-mariadb-server-10.4.sock");'
```

PHP mysqli test:

```bash
php -r '$dbcon = mysqli_connect("localhost","dan","nopass","catalog/test",3306,"/tmp/build-mariadb-server-10.4.sock");'
```

Nodejs test:

```javascript
var mysql = require('mysql')
var con = mysql.createConnection({
  socketPath: "/tmp/build-mariadb-server-10.4.sock",
  user: "dan",
  password: "yourpassword",
  database: "catalog/test",
})
con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
})
```

(need to map out a few other connectors here to make sure it’s supported well in this form).

Ref: [connection.md#handshake-response-packet](../../../reference/clientserver-protocol/1-connecting/connection.md#handshake-response-packet)

## Migration of Existing MariaDB Original Mode to the New Catalog Layout

As shared hosting services have a naming scheme from user/schema to database name in MariaDB, to provide a migration to the new catalog layout, the following steps will be required:

* Use [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) to dump the original data
* On the new server execute:
* [mariadb-install-db –catalogs=’catalog\_name’](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md)
* mariadb –catalog catalog\_name < dump\_file

This is needed as InnoDB needs to know where the new files are located.

## Migration of One Catalog User to Another MariaDB Server

Create a migration tool set / procedure that does the following

* Execute [FLUSH TABLES FOR EXPORT](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) for all tables in a catalog.
* Take a copy of the catalog directory
* Copy the data to a new catalog directory to the new server
* Run [ALTER TABLE ... IMPORT TABLESPACE](../../../reference/sql-statements/data-definition/alter/alter-table/#import-tablespace) on each InnoDB table

Note that for partitioned tables the process will be a bit more complex, see above link.

This procedure will be a bit easier after an in-the-works patch for InnoDB related to IMPORT will be pushed. (Should happen before we start on the catalog project)

## Other Things

* Drizzle’s default catalog was called "local". MariaDB’s default will be called ‘def’, as this is what we already have as the default catalog in information\_schema, in current connectors and other places.
* CONNECT engine will need testing against catalogs and maybe a small code change to support them. It could also be a way to join from one catalog to another.

## See Also

* [MDEV-31542](https://jira.mariadb.org/browse/MDEV-31542) Add multi-tenancy catalogs to MariaDB

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
