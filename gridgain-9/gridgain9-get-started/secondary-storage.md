---
description: >-
  Configure GridGain 9 secondary columnar storage to run analytical queries
  alongside transactional workloads in a hybrid HTAP setup.
---

# Secondary Storage for Analytics

## Overview

GridGain secondary storage allows you to create hybrid transactional/analytical processing (HTAP) systems by configuring tables to store data in both primary and secondary storage engines. This approach enables you to optimize your database for both transactional and analytical workloads simultaneously. The primary storage engine (usually `aipersist`) handles write operations and transactional queries, while the secondary storage (`columnar`) is optimized for analytical queries.

This guide will show you how to configure and use secondary storage for analytical workloads.

## Prerequisites

Before you begin, ensure you have:

- A license with secondary storage add-on;
- Basic understanding of [distribution zones](../architecture/storage/distribution-zones.md);
- Basic understanding of [storage profiles](../architecture/storage/storage-profiles.md).

## Configuring Secondary Storage

### Step 1: Create a Columnar Storage Profile

First, create a storage profile that uses the `columnar` storage engine:

```bash
node config update "ignite.storage.profiles:{columnar{engine:columnar}}"
```

After updating the configuration, restart the node for the changes to take effect.

### Step 2: Create a Distribution Zone with Multiple Storage Profiles

{% hint style="info" %}
This tutorial uses `default` storage profile for primary storage. You can use any other storage profile as long as it uses the `aipersist` storage engine.
{% endhint %}

After restarting the node, enter the sql editing mode of the CLI tool with the `sql` command.

Then, create a distribution zone that supports both the default storage profile (for primary storage) and the columnar storage profile (for secondary storage):

```sql
CREATE ZONE HTAP STORAGE PROFILES['default', 'columnar'];
```

This distribution zone will now be able to store data using either the `default` or `columnar` storage profiles.

### Step 3: Create Tables with Primary and Secondary Storage

Now you can create tables that use both storage profiles:

```sql
CREATE TABLE Person (
  id INT PRIMARY KEY,
  city_id INT,
  name VARCHAR,
  age INT,
  company VARCHAR
)
PRIMARY ZONE HTAP PRIMARY STORAGE PROFILE 'default'
SECONDARY ZONE HTAP SECONDARY STORAGE PROFILE 'columnar';
```

In this example:

- The `PRIMARY ZONE` and `PRIMARY STORAGE PROFILE` clauses define where and how the primary data will be stored
- The `SECONDARY ZONE` and `SECONDARY STORAGE PROFILE` clauses define where and how the secondary data will be stored

{% hint style="info" %}
The primary and secondary storage can be in the same or different distribution zones. Using different zones allows for more flexible data placement strategies.
{% endhint %}

## Using Secondary Storage

### Writing Data

Data is always written to the primary storage first, then automatically propagated to the secondary storage. You cannot write directly to the secondary storage.

Example of inserting data:

```sql
-- Load sample data
INSERT INTO Person (id, city_id, name, age, company) VALUES 
    (1, 101, 'Alice Smith', 29, 'Acme Corp'),
    (2, 102, 'Bob Johnson', 35, 'TechNova'),
    (3, 103, 'Charlie Lee', 41, 'InnovaWorks'),
    (4, 104, 'Diana Chen', 33, 'Quantum Solutions'),
    (5, 105, 'Ethan Patel', 27, 'NextGen Inc'),
    (6, 106, 'Fiona Garcia', 38, 'CloudCore'),
    (7, 107, 'George Adams', 30, 'EcoTech'),
    (8, 108, 'Hannah Kim', 26, 'NeoWare'),
    (9, 109, 'Ivan Kuznetsov', 44, 'AltLogic'),
    (10, 110, 'Jasmine Nguyen', 31, 'BrightEdge');
```

### Reading from Primary Storage

By default, all queries read from the primary storage:

```sql
SELECT name, age FROM Person WHERE company = 'TechNova';
```

### Reading from Secondary Storage

To read from the secondary storage, use the `use_secondary_storage` query hint:

```sql
SELECT /*+ use_secondary_storage */ name, age 
FROM Person 
WHERE company = 'TechNova';
```

### Understanding Query Plans

You can use the `EXPLAIN PLAN` statement to see how queries will be executed against either the primary or secondary storage:

```sql
-- View plan for primary storage query
EXPLAIN PLAN FOR 
SELECT name, age FROM Person WHERE company = 'TechNova';

-- View plan for secondary storage query
EXPLAIN PLAN FOR 
SELECT /*+ use_secondary_storage */ name, age 
FROM Person 
WHERE company = 'TechNova';
```

You can see the `useSecondaryStorage: true` explanation when using secondary storage, for example:

```
╔═════════════════════════════════════════════╗
║ PLAN                                        ║
╠═════════════════════════════════════════════╣
║ Exchange                                    ║
║     distribution: single                    ║
║     est. row count: 1                       ║
║   TableScan                                 ║
║       table: [PUBLIC, PERSON]               ║
║       filters: =(COMPANY, _UTF-8'TechNova') ║
║       fields: [$f0, $f1]                    ║
║       projects: [NAME, AGE]                 ║
║       useSecondaryStorage: true             ║
║       est. row count: 1                     ║
╚═════════════════════════════════════════════╝
```

## Mixed Workloads

You can mix data from primary and secondary storage in a single query by applying the `use_secondary_storage` hint to specific tables.

First, let's create an extra table that will not be using secondary storage and add some data to it:

```sql
-- Create sample table
CREATE TABLE Orders (
  CustomerId int primary key,
  Company varchar
);

-- Load sample data
INSERT INTO Orders (CustomerId, Company) VALUES
  (1, 'Acme Corp'),
  (2, 'TechNova');
```

Since no distribution zone or storage profile is specified, this table will be created in the default distribution zone, and will not be replicated to secondary storage.

```sql
SELECT Person.name, Orders.CustomerId
FROM Person /*+ use_secondary_storage */
JOIN Orders 
ON Person.id = Orders.CustomerId
WHERE Person.company = 'TechNova';
```

In this example, data from the `Person` table is read from secondary storage, while data from the `Orders` table is read from primary storage.

## Considerations

### Data Consistency

Be aware that secondary storage is updated asynchronously after primary storage. This means that secondary storage may be slightly behind primary storage (typically under a second). For queries requiring absolute consistency, use primary storage.

### Workload Separation

- Use primary storage for transactional workloads (OLTP) that require frequent writes and point queries;
- Use secondary storage for analytical workloads (OLAP) that involve scanning large amounts of data.

### Query Optimization

- Analytical queries that scan large portions of tables will typically perform better on columnar secondary storage;
- Point lookups by primary key often perform better on primary storage;
- Use `EXPLAIN PLAN` to understand how your queries will be executed.

### Resource Planning

Consider allocating different nodes or resource pools for transactional and analytical workloads to prevent analytical queries from affecting the performance of transactional operations.
