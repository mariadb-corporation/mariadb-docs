# Data offloading

There are multiple options to copy/offload data from a SkySQL DB. You can do a logical dump(i.e. output all data and DDL as SQL) to your local machine. Or, dump large data sets securely using the SkySQL Backup service to your own S3 or GCS bucket. 

You can then use the offloaded data to resurrect the DB elsewhere. You can also optionally setup "outbound replication" to keep the new DB in sync with SkySQL. 

## **1. Offload your Database using `mariadb-dump`**

The [`mariadb-dump`](https://mariadb.com/kb/en/mariadb-dump/) utility is a powerful command-line tool that allows you to export databases, tables, or specific data from your MariaDB instance in SkySQL. 

### **Prerequisites**
Ensure you have the mariadb-dump utility installed on your system. See [here](<../Data loading, Migration/Install Mariadb-dump.md>)
Obtain the necessary connection details for your SkySQL instance, including the host, username, and password.

### **Exporting All Databases**

To export all databases from your SkySQL instance, use the following command:

```bash
mariadb-dump -h your_skysql_host -u your_username -p \
    --all-databases > all_databases_backup.sql
```

- `-h your_skysql_host`: Specifies the host of your SkySQL instance.
- `-u your_username`: Specifies the username to connect to the SkySQL instance.
- `-p`: Prompts for the password for the specified username.
- `--all-databases`: Exports all databases in the SkySQL instance.
- `> all_databases_backup.sql`: Redirects the output to a file named all_databases_backup.sql.


### **Exporting Selected Databases**

To export specific databases, list the database names after the connection details:

```bash
mariadb-dump -h your_skysql_host -u your_username \
    -p database1 database2 > selected_databases_backup.sql
```

- `database1 database2`: Replace with the names of the databases you want to export.
- ``> selected_databases_backup.sql`: Redirects the output to a file named selected_databases_backup.sql.

### **Exporting Just the Schema**
To export only the schema (structure) of a database without the data, use the --no-data option:

```bash
mariadb-dump -h your_skysql_host -u your_username -p \
    --no-data your_database > schema_backup.sql
```

- `--no-data`: Ensures that only the schema is exported, not the data.
- `your_database`: Replace with the name of the database whose schema you want to export.
- `> schema_backup.sql`: Redirects the output to a file named schema_backup.sql.


### **File Format of Exported Data**
The files exported by mariadb-dump are in plain text format and contain SQL statements. These files can be used to recreate the databases, tables, and data by executing the SQL statements in a MariaDB instance.

- Database Creation: The file begins with statements to create the databases.
- Table Creation: For each table, the file includes CREATE TABLE statements that define the table structure.
- Data Insertion: If data is included, the file contains INSERT INTO statements to populate the tables with data.
- Comments: The file may include comments that provide additional information about the export process.

**Example of Exported File Content** 

Here is a snippet of what an exported file might look like:
```sql 
-- MariaDB dump 10.16  Distrib 10.5.9-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: your_skysql_host    Database: 
-- ------------------------------------------------------
-- Server version	10.5.9-MariaDB-1:10.5.9+maria~focal

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `your_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `your_table`
--

DROP TABLE IF EXISTS `your_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `your_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `your_table`
--

LOCK TABLES `your_table` WRITE;
/*!40000 ALTER TABLE `your_table` DISABLE KEYS */;
INSERT INTO `your_table` VALUES (1,'Example Name','2023-01-01 00:00:00'),(2,'Another Name','2023-01-02 00:00:00');
/*!40000 ALTER TABLE `your_table` ENABLE KEYS */;
UNLOCK TABLES;
```

Finally, here is the reference to the utility where you will find all the [many command-line options](https://mariadb.com/kb/en/mariadb-dump/)

> **Note**  
>
> Egress charges may apply when data is exported


## **2. Using MariaDB client**

Use [MariaDB Client](<../Connecting to Sky DBs/Connect using MariaDB CLI.md>) with the connection information to export your schema from your SkySQL database service. Here is an example to export all rows from a single table:

```bash
mariadb --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --default-character-set=utf8 \
      --batch \
      --skip-column-names \
      --execute='SELECT * FROM accounts.contacts;' \
      > contacts.tsv
```

- Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the Fully Qualified Domain Name of your service.
- Replace `TCP_PORT` with the read-write or read-only port of your service.
- Replace `DATABASE_USER` with the default username for your service, or the username you created.
- Optionally, for large tables, specify the `-quick command-line option` to disable result caching and reduce memory usage.
- You can customize the SQL along with providing multiple SQL statements to `-execute`. 


## **3. Exporting Data Using SkySQL Backup Service API to S3 or GCS Bucket**
The [SkySQL Backup service API](<../Backup and Restore/README.md>) allows you to perform logical and physical dumps of your SkySQL databases to external storage buckets such as Amazon S3 or Google Cloud Storage (GCS). 

### **Prerequisites**
- Obtain the necessary credentials for your S3 bucket.
- Ensure you have access to the SkySQL Backup service API. You need to generate the API Key from the portal. 
- Obtain the service ID for your SkySQL instance.
- Base64 encodes your S3 credentials.

###  **Performing a Logical Dump to an S3 Bucket**
To perform a logical dump of a SkySQL database to an S3 bucket, you need to make an API call to the SkySQL Backup service. Below is an example of how to do this.

Example API Call for Logical Dump (The output is all SQL statements)
```shell
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "logical",
    "schedule": "once",
    "service_id": "your_service_id",
    "external_storage": {
        "bucket": {
            "path": "s3://your_s3_bucket_name/path/to/backup",
            "credentials": "your_base64_encoded_credentials"
        }
    }
}'
```

- backup_type: Set to "logical" for a logical dump.
- schedule: Set to "once" to schedule the backup immediately.
- service_id: The ID of your SkySQL service.
- external_storage.bucket.path: The S3 bucket path where the backup will be stored.
- external_storage.bucket.credentials: Base64 encoded S3 credentials.

### **Performing a Physical Dump to an S3 Bucket**

**When databases are large and you want to move the data around securely this is likely the best option.** To perform a physical dump of a SkySQL database to an S3 bucket, you need to make a similar API call but specify the backup type as "physical".

Example API Call for Physical Dump
```shell
curl --location 'https://api.skysql.com/skybackup/v1/backups/schedules' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "backup_type": "physical",
    "schedule": "once",
    "service_id": "your_service_id",
    "external_storage": {
        "bucket": {
            "path": "s3://your_s3_bucket_name/path/to/backup",
            "credentials": "your_base64_encoded_credentials"
        }
    }
}'
```

- backup_type: Set to "physical" for a physical dump.
- schedule: Set to "once" to schedule the backup immediately.

### **Checking the Status of Initiated Backups**
Backups are always scheduled as jobs and the time taken will depend on the size of yourDB. To check the status of the initiated backups, you can use the following API call:

```shell
Example API Call to Check Backup Status
curl --location 'https://api.skysql.com/skybackup/v1/backups/status' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-API-Key: ${API_KEY}' \
--data '{
    "service_id": "your_service_id"
}'
```

- service_id: The ID of your SkySQL service.
This API call will return the status of the backups, including whether they are in progress, completed, or failed.


## **4. Replicating changes from SkySQL to a compatible external DB**

See [Replicating data From SkySQL to External Database](<./Replicating data from SkySQL to external database.md>) for details.
