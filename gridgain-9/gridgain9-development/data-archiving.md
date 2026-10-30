---
description: >-
  How data archiving in GridGain 9 removes aged data from primary storage after
  moving it to secondary storage for HTAP workloads.
---

# Data Archiving

## Overview

Data archiving removes aged data from primary storage after it has been moved to secondary storage, keeping the primary dataset small. This lets you retain growing historical data in secondary storage without impacting transactional performance, while still keeping it accessible for analytics.

This feature is particularly useful for hybrid transactional/analytical processing (HTAP) workloads where recent data requires fast transactional access while historical data is primarily used for analytical queries.

## Prerequisites

To use data archiving, you need a license with support for columnar storage and data archiving.

## Configuring Data Archiving

### Step 1: Create a Columnar Storage Profile

First, configure a columnar storage profile in your node configuration:

```bash
node config update ignite.storage.profiles.columnar_storage '{"engine":"columnar"}'
```

### Step 2: Create Distribution Zones

Create a distribution zone that will be used for data storage.

Depending on your needs, you can configure a distribution zone in different ways:

- To have both the primary and secondary storage distributed in the same way, create a single zone with both storage profiles:

  ```sql
  CREATE ZONE htap_zone STORAGE PROFILES['default','columnar_storage'];
  ```
- If you want to separate data zones for primary and secondary storage:

  ```sql
  CREATE ZONE primary_zone STORAGE PROFILES['default'];
  CREATE ZONE secondary_zone STORAGE PROFILES['columnar_storage'];
  ```

### Step 3: Create Table with Archive Condition

Create a table with both primary and secondary storage, specifying the `ARCHIVE AT` condition:

```sql
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  order_date TIMESTAMP WITH LOCAL TIME ZONE,
  amount DECIMAL(10,2),
  ttl TIMESTAMP WITH LOCAL TIME ZONE
)
PRIMARY ZONE htap_zone
PRIMARY STORAGE PROFILE 'default'
SECONDARY ZONE htap_zone
SECONDARY STORAGE PROFILE 'columnar_storage'
ARCHIVE AT ttl;
```

In this example, rows will be removed from primary storage when the current time exceeds the value in the `ttl` column, but will be kept in the secondary storage.

## Using Archived Data

### Writing Data

Data is always written to primary storage and automatically propagated to secondary storage:

```sql
-- Archive data after 30 days
INSERT INTO orders (id, customer_id, order_date, amount, ttl)
VALUES (1, 100, CURRENT_TIMESTAMP, 1500.00,
        CURRENT_TIMESTAMP + INTERVAL '30' DAYS);
```

### Reading Archived Data

To read from secondary storage (including archived data), use the `use_secondary_storage` hint:

```sql
-- Read from secondary storage
SELECT /*+ use_secondary_storage */
  customer_id, SUM(amount) as total_spent
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY customer_id;
```
