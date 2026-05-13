---
description: >-
  Import CSV and TSV files into MariaDB Cloud with the LOAD DATA LOCAL INFILE
  statement, executable from any MariaDB client or connector with local-infile
  support enabled.
---

# Import CSV Data

MariaDB Cloud customers can import data into a MariaDB Cloud service using the `LOAD DATA LOCAL INFILE` SQL statement:

* The `LOAD DATA LOCAL INFILE` statement can import data from TSV and CSV files
* The `LOAD DATA LOCAL INFILE` statement can be executed by any client or connector

{% hint style="warning" %}
Make sure your schema is already created in the database. If you need to import entire databases or create tables, you should use [mariadb-import](install-mariadb-import.md).
{% endhint %}

## **Enable Local Infiles**

Support for local infiles must be enabled on the client side and on the MariaDB Cloud service.

### **Enable Local Infiles on the Client or Connector**

To execute the [`LOAD DATA LOCAL INFILE`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement, most clients and connectors require a specific option to be enabled.

If you are using `mariadb` client, the [`--local-infile` option](https://mariadb.com/docs/skysql-previous-release/data-operations/data-import/load-data-local-infile/) must be specified.

### **Enable Local Infiles in MariaDB Cloud**

Support for local infiles must be enabled on the MariaDB Cloud service.

For MariaDB Cloud services that use MariaDB Server, the [local\_infile system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) must be enabled:

* For Replicated Transactions and Single Node Transactions services, the `local_infile` system variable is `OFF` by default

[Configuration Manager](../../../../config/) can be used to modify the value of the `local_infile` system variable.

## **Import Data**

1. Determine the [connection parameters](../../../../Connecting%20to%20Sky%20DBs/) for your MariaDB Cloud service.
2. Connect with the `mariadb` client and specify the [-local-infile option](https://mariadb.com/docs/skysql-previous-release/data-operations/data-import/load-data-local-infile/), which is needed by the next step:

```bash
mariadb --host FULLY_QUALIFIED_DOMAIN_NAME --port TCP_PORT \
      --user DATABASE_USER --password \
      --ssl-verify-server-cert \
      --default-character-set=utf8 \
      --local-infile
```

After the command is executed, you will be prompted for a password. Enter the default password for your default user, the password you set for the default user, or the password for the database user you created.

For each table that you want to import, execute the LOAD DATA LOCAL INFILE statement to import the data from the TSV or CSV file into your MariaDB Cloud database service.

For a TSV file:

```sql
LOAD DATA LOCAL INFILE 'contacts.tsv'
INTO TABLE accounts.contacts;
```

For a CSV file:

```sql
LOAD DATA LOCAL INFILE 'contacts.csv'
INTO TABLE accounts.contacts
FIELDS TERMINATED BY ',';
```

## **Using a Connector**

If you are using a MariaDB Connector, then you must select the method for the specific connector from the list below.

If you are using `MariaDB Connector/C`, the `MYSQL_OPT_LOCAL_INFILE` option can be set with the `mysql_optionsv()` function:

```c
/* enable local infile */
unsigned int enable_local_infile = 1;
mysql_optionsv(mysql, MYSQL_OPT_LOCAL_INFILE, (void *) &enable_local_infile);
```

If you are using `MariaDB Connector/J`, the `allowLocalInfile` parameter can be set for the connection:

```java
Connection connection = DriverManager.getConnection("jdbc:mariadb://FULLY_QUALIFIED_DOMAIN_NAME:TCP_PORT/test?user=DATABASE_USER&password=DATABASE_PASSWORD&allowLocalInfile=true");
```

If you are using `MariaDB Connector/Node.js`, the `permitLocalInfile` parameter can be set for the connection:

```js
mariadb.createConnection({
   host: 'FULLY_QUALIFIED_DOMAIN_NAME',
   port: 'TCP_PORT',
   user:'DATABASE_USER',
   password: 'DATABASE_PASSWORD',
   permitLocalInfile: 'true'
 });
```

If you are using `MariaDB Connector/Python`, the `local_infile` parameter can be set for the connection:

```python
conn = mariadb.connect(
   user="DATABASE_USER",
   password="DATABASE_PASSWORD",
   host="FULLY_QUALIFIED_DOMAIN_NAME",
   port=TCP_PORT,
   local_infile=true)
```
