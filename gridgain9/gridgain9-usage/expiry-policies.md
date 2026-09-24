---
description: >-
  Configure data expiry in GridGain 9 with a dedicated TIMESTAMP column and the
  EXPIRE AT keyword, and enable or disable expiration on existing tables.
---

# Expiry Policies

Expiry Policy specifies the point of time at which an entry is considered expired. The expiration time must be specified using the `TIMESTAMP WITH LOCAL TIME ZONE` data type.

## Configuration

GridGain 9 relies on a dedicated table column to configure data expiry. When creating a table, make sure to have the dedicated `TIMESTAMP WITH LOCAL TIME ZONE` column to store TTL. Once the timestamp is reached, data will be marked for deletion and deleted when the check is triggered. You can control the frequency of the checks for expired data by setting the `ignite.expiration.checkInterval` [node configuration](../reference/configuration/node-configuration-parameters.md).

Then specify it as a TTL column by using the `EXPIRE AT` keyword. For example:

```sql
CREATE TABLE Person (
    id INT PRIMARY KEY,
    name VARCHAR,
    ttl TIMESTAMP WITH LOCAL TIME ZONE
) EXPIRE AT ttl;
```

The table above uses a `ttl` column to store the expiration data for each row.

You can also set a default value to the column by using the `DEFAULT` keyword:

```sql
CREATE TABLE Person (
    id INT PRIMARY KEY,
    name VARCHAR,
    ttl TIMESTAMP WITH LOCAL TIME ZONE DEFAULT CURRENT_TIMESTAMP + INTERVAL '2' HOURS
) EXPIRE AT ttl;
```

When specifying the default timestamp, the time must be specified in the `CURRENT_TIMESTAMP + {interval}` format. The interval can be specified in:

- `SECONDS`
- `MINUTES`
- `HOURS`
- `DAYS`
- `MONTHS`

In the table above, all newly created rows will be scheduled for removal after 2 hours.

### Enabling Expiration Policy for Existing Table

To enable data expiration on an existing table, first add a column to it that you will use for TTL definition. Then, use the `SET EXPIRE AT` command to set the column as the TTL definition.

```sql
ALTER TABLE Person ADD COLUMN ttl TIMESTAMP WITH LOCAL TIME ZONE;
ALTER TABLE Person SET EXPIRE AT ttl;
```

### Disabling Expiration Policy

To disable data expiration for the table, use the `DROP EXPIRE` command:

```sql
ALTER TABLE Person DROP EXPIRE;
```

You can also drop the column you used to TTL if you no longer need it to save space.
