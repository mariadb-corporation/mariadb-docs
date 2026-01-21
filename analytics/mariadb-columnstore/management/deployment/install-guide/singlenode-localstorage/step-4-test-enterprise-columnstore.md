# Step 4: Test Enterprise ColumnStore

## Overview

This page details step 4 of a 5-step procedure for deploying [Single-Node Enterprise ColumnStore with Local storage](./).

This step tests MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test Local Connection

Connect to the server using MariaDB Client using the root@localhost user account:

```bash
$ sudo mariadb
```

```sql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

## Test ColumnStore Plugin Status

Query [information\_schema.PLUGINS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) and confirm that the ColumnStore storage engine plugin is `ACTIVE`:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS
FROM information_schema.PLUGINS
WHERE PLUGIN_LIBRARY LIKE 'ha_columnstore%';
```

```sql
+---------------------+---------------+
| PLUGIN_NAME         | PLUGIN_STATUS |
+---------------------+---------------+
| Columnstore         | ACTIVE        |
| COLUMNSTORE_COLUMNS | ACTIVE        |
| COLUMNSTORE_TABLES  | ACTIVE        |
| COLUMNSTORE_FILES   | ACTIVE        |
| COLUMNSTORE_EXTENTS | ACTIVE        |
+---------------------+---------------+
```

## Test ColumnStore Table Creation

1. Create a test database, if it does not exist:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

2. Create a ColumnStore table:

```sql
CREATE TABLE IF NOT EXISTS test.contacts (
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
) ENGINE=ColumnStore;
```

3. Add sample data into the table:

```sql
INSERT INTO test.contacts (first_name, last_name, email)
   VALUES
   ("Kai", "Devi", "kai.devi@example.com"),
   ("Lee", "Wang", "lee.wang@example.com");
```

4. Read data from table:

```sql
SELECT * FROM test.contacts;
```

```sql
+------------+-----------+----------------------+
| first_name | last_name | email                |
+------------+-----------+----------------------+
| Kai        | Devi      | kai.devi@example.com |
| Lee        | Wang      | lee.wang@example.com |
+------------+-----------+----------------------+
```

## Test Cross Engine Join

1. Create an InnoDB table:

```sql
CREATE TABLE test.addresses (
   email VARCHAR(100),
   street_address VARCHAR(255),
   city VARCHAR(100),
   state_code VARCHAR(2)
) ENGINE = InnoDB;
```

2. Add data to the table:

```sql
INSERT INTO test.addresses (email, street_address, city, state_code)
   VALUES
   ("kai.devi@example.com", "1660 Amphibious Blvd.", "Redwood City", "CA"),
   ("lee.wang@example.com", "32620 Little Blvd", "Redwood City", "CA");
```

3. Perform a cross-engine join:

```sql
SELECT name AS "Name", addr AS "Address"
FROM (SELECT CONCAT(first_name, " ", last_name) AS name,
   email FROM test.contacts) AS contacts
INNER JOIN (SELECT CONCAT(street_address, ", ", city, ", ", state_code) AS addr,
   email FROM test.addresses) AS addr
WHERE  contacts.email = addr.email;
```

```sql
+----------+-----------------------------------------+
| Name     | Address                                 |
+----------+-----------------------------------------+
| Kai Devi | 1660 Amphibious Blvd., Redwood City, CA |
| Lee Wang | 32620 Little Blvd, Redwood City, CA     |
+----------+-----------------------------------------+

+-------------------+-------------------------------------+
| Name              | Address                             |
+-------------------+-------------------------------------+
| Walker Percy      | 500 Thomas More Dr., Covington, LA  |
| Flannery O'Connor | 300 Tarwater Rd., Milledgeville, GA |
+-------------------+-------------------------------------+
```

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Local storage deployment procedure:

This page was step 4 of 5.

[Next: Step 5: Bulk Import of Data.](step-5-bulk-import-of-data.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
