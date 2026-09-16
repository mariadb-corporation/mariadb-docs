---
description: >-
  Reference for the Data Definition Language (DDL) commands supported by
  GridGain 9, including CREATE, ALTER, and DROP for tables, indexes, schemas,
  caches, and sequences.
---

# Data Definition Language (DDL)

This section walks you through all data definition language (DDL) commands supported by GridGain 9.0.

## CREATE TABLE

Creates a new table.

{% hint style="info" %}
This can also be done via the [Java API](../developers-guide/java-to-tables.md).
{% endhint %}

```bnf
CREATE TABLE [IF NOT EXISTS] qualified_table_name
  ( { column_definition | constraint } [, ...] )
  [COLOCATE [BY] ( column_list )]
  [[PRIMARY] ZONE zone_name]
  [[PRIMARY] STORAGE PROFILE profile_name]
  [SECONDARY ZONE zone_name SECONDARY STORAGE PROFILE profile_name]
  [{ EXPIRE AT expiry_column_name | ARCHIVE AT archive_column_name }]
  [WITH ( paramName paramValue [, ...] )]
```

<!-- railroad-source:
Diagram(Terminal('CREATE'),Terminal('TABLE'),Optional(Terminal('IF NOT EXISTS')),NonTerminal('qualified_table_name'),Terminal('('),Choice(1,NonTerminal('constraint'),NonTerminal('column_definition'),Terminal(',')),Terminal(')'),Optional(Sequence(Terminal('COLOCATE'),Optional('BY'),Terminal('('),NonTerminal('column_list'),Terminal(')'))),End({type:'complex'}))
Diagram(Start({type:'complex'}),Optional(Sequence(Optional('PRIMARY'),Terminal('ZONE'),NonTerminal('zone_name'))),Optional(Sequence(Optional('PRIMARY'),Terminal('STORAGE PROFILE'),NonTerminal('profile_name'))),End({type:'complex'}))
Diagram(Start({type:'complex'}),Optional(Sequence(Terminal('SECONDARY'),Terminal('ZONE'),NonTerminal('zone_name'),Terminal('SECONDARY'),Terminal('STORAGE PROFILE'),NonTerminal('profile_name'))),Optional(Choice(0,Sequence(Terminal('EXPIRE'),Terminal('AT'),NonTerminal('expiry_column_name')),Sequence(Terminal('ARCHIVE'),Terminal('AT'),NonTerminal('archive_column_name')))),Optional(Sequence(Terminal('WITH'),Terminal('('),OneOrMore(Sequence(NonTerminal('paramName'),NonTerminal('paramValue')),Terminal(',')),Terminal(')'))))
-->

![Railroad diagram of CREATE TABLE (part 1)](../../.gitbook/assets/gg9-sql-reference-create_table_bnf1.svg)

![Railroad diagram of CREATE TABLE (part 2)](../../.gitbook/assets/gg9-sql-reference-create_table_bnf2.svg)

**Keywords and parameters:**

- `IF NOT EXISTS` - create the table only if a table with the same name does not exist.
- `COLOCATE BY` - colocation key. The key can be composite. Primary key must include colocation key.
- `ZONE` - sets the [Distribution Zone](distribution-zones.md). Can be preceded by `PRIMARY` to signify the primary distribution zone, or by `SECONDARY` to signify the secondary distribution zone. Can be specified as a case-sensitive string or case-insensitive identifier. Does not need to exist at the moment of table creation, and can be created before writing data.
- `STORAGE PROFILE` - sets the [storage profile](../administrators-guide/config/node-config.md#storage-configuration) that will be used to store the table. Can be preceded by `PRIMARY` to signify the primary storage, or by `SECONDARY` to signify the secondary ([columnar](../administrators-guide/storage/engines/columnar.md)) storage profile. Must be specified as a case-sensitive string. Can be preceded by `PRIMARY` to signify the primary storage profile.
- `EXPIRE AT` - defines when a record should be deleted based on the provided point in time. Unlike `ARCHIVE AT`, deletes the data both in primary and secondary storage when the specified time is reached.
- `ARCHIVE AT` - defines when a record should be removed from primary storage based on the provided point in time. The data will still be available for reading in secondary storage. Currently, this condition comes with several limitations:
  - You cannot use this condition without [secondary storage](../administrators-guide/storage/storage-profiles.md#secondary-storage-profiles). Table must have secondary storage attached.
  - You cannot use this condition together with `EXPIRE AT`.
  - After the `ARCHIVE AT` timestamp is reached, you cannot modify the archived data with `UPDATE` or `DELETE` operations. Only the data that exists in the primary storage can be modified.
- `WITH` - defines the list of additional table parameters. Currently, the following parameters are supported:
  - `min stale rows` - number of updates since the last query plan update required to automatically recreate query execution plan. Overrides `ignite.sql.createTable.minStaleRowsCount`. Default value is `500`.
  - `stale rows fraction` - fraction of the table that must change for query execution plan to be recreated automatically. Overrides `ignite.sql.createTable.staleRowsFraction`. Default value is `0.2`.
  - `row level security` - enables (`ON`) or disables (`OFF`) [row-level security](../administrators-guide/security/row-level-security.md) on the table. If omitted, row-level security is disabled. This is equivalent to creating the table and then running `ALTER TABLE ... SET ROW LEVEL SECURITY ON`. Available only in GridGain 9 Enterprise and Ultimate editions; setting it requires the `MANAGE_RLS` privilege on the table.

{% hint style="info" %}
Secondary storage profiles and distribution zones are only available as part of the HTAP add-on license.
{% endhint %}

**Examples:**

Creates a Person table:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
);
```

Creates a Person table that uses distribution zone `exampleZone`:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
) ZONE exampleZone;
```

Creates a Person table that uses distribution zone `myExampleZone` that is specified as a case-sensitive string:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
) ZONE "myExampleZone";
```

Creates a Person table that uses the `default` storage profile regardless of the storage profile specified in the distribution zone:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
) PRIMARY ZONE MYZONE PRIMARY STORAGE PROFILE 'default';
```

Creates a Person table that uses the secondary distribution zone and a secondary storage profile for columnar data:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
) PRIMARY ZONE MYZONE PRIMARY STORAGE PROFILE 'default' SECONDARY ZONE COLUMNARZONE SECONDARY STORAGE PROFILE 'columnar_storage';
```

Creates a Person table where the records expire at timestamps in the `ttl` column:

```sql
CREATE TABLE IF NOT EXISTS Person ( 
  id int PRIMARY KEY,
  name varchar,
  ttl timestamp with local time zone
) EXPIRE AT ttl;
```

Creates a Person table where the default value if the `city_id` column is 1:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int default 1,
  name varchar,
  age int,
  company varchar
);
```

Creates a Person table where a random personal identifier is generated automatically:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id uuid default rand_uuid() PRIMARY KEY,
  city_id int default 1,
  name varchar,
  age int,
  company varchar
);
```

Creates a Person table with the `duration` column automatically set a week into the future:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int,
  city_id int,
  name varchar,
  age int,
  company varchar,
  duration timestamp with local time zone default CURRENT_TIMESTAMP + INTERVAL '7' DAYS,
  PRIMARY KEY (id, duration)
);
```

{% hint style="info" %}
INTERVAL is required when specifying the timestamp as the default column value. You can specify INTERVAL '0' SECONDS to use current time.
{% endhint %}

Archives old data while keeping it accessible in secondary storage:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  name varchar,
  ttl TIMESTAMP WITH LOCAL TIME ZONE)
  ZONE zone1 SECONDARY ZONE secondary_zone SECONDARY STORAGE PROFILE 'columnar_storage' ARCHIVE AT ttl;
```

Reads the archived data, explicitly using the secondary storage access [hint](../performance-tuning/sql-tuning.md#hints-format):

```sql
SELECT * FROM Person /*+ use_secondary_storage */;
```

Creates a Person table with [row-level security](../administrators-guide/security/row-level-security.md) enabled. The property can be combined with other table properties:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  name varchar
) WITH (ROW LEVEL SECURITY ON);

CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  name varchar
) WITH (MIN STALE ROWS 100, ROW LEVEL SECURITY ON);
```

## ALTER TABLE

Modifies the structure of an existing table.

### ALTER TABLE IF EXISTS table ADD COLUMN (column1 int, column2 int)

Adds column(s) to an existing table.

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ADD [COLUMN] [IF NOT EXISTS] column_definition_or_list
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ADD'),Optional(Terminal('COLUMN')),Optional(Terminal('IF NOT EXISTS')),End({type:'complex'}))
Diagram(Start({type:'complex'}),NonTerminal('column_definition_or_list'))
-->

![Railroad diagram of ALTER TABLE ADD COLUMN (part 1)](../../.gitbook/assets/gg9-sql-reference-alter_table_column_no_bnf1.svg)

![Railroad diagram of ALTER TABLE ADD COLUMN (part 2)](../../.gitbook/assets/gg9-sql-reference-alter_table_column_no_bnf2.svg)

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `IF NOT EXISTS` - do not throw an error if a column with the specified column name already exists.

**Examples:**

Add a column to the table:

```sql
ALTER TABLE Person ADD COLUMN city varchar;
```

Add a column only if the table exists:

```sql
ALTER TABLE IF EXISTS Person ADD number bigint;
```

Add several columns to the table at once:

```sql
ALTER TABLE Person ADD COLUMN (code varchar, gdp double);
```

### ALTER TABLE IF EXISTS table DROP COLUMN (column1, column2 int)

Removes column(s) from an existing table. Once a column is removed, it cannot be accessed within queries. This command has the following limitations:

- If the column was indexed, the index has to be dropped manually in advance by using the 'DROP INDEX' command.
- It is not possible to remove a column if it represents the whole value stored in the cluster. The limitation is relevant for primitive values.

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  DROP [COLUMN] column_list
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('DROP'),Optional(Terminal('COLUMN')),End({type:'complex'}))
Diagram(Start({type:'complex'}),NonTerminal('column_list'))
-->

![Railroad diagram of ALTER TABLE DROP COLUMN (part 1)](../../.gitbook/assets/gg9-sql-reference-alter_table_column_yes_bnf1.svg)

![Railroad diagram of ALTER TABLE DROP COLUMN (part 2)](../../.gitbook/assets/gg9-sql-reference-alter_table_column_yes_bnf2.svg)

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.

**Examples:**

Drop a column from the table:

```sql
ALTER TABLE Person DROP COLUMN city;
```

Drop a column only if the table exists:

```sql
ALTER TABLE IF EXISTS Person DROP COLUMN number;
```

Drop several columns from the table at once:

```sql
ALTER TABLE Person DROP COLUMN (code, gdp);
```

### ALTER TABLE IF EXISTS table ALTER COLUMN column SET DATA TYPE

Changes the data type for the column(s) in an existing table.

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ALTER COLUMN column_name_or_list
  SET DATA TYPE data_type [( { NULLABLE | NOT NULL } )]
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ALTER COLUMN'),NonTerminal('column_name_or_list'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Terminal('SET DATA TYPE'),NonTerminal('data_type'),Optional(Sequence(Terminal('('),Choice(0,'NULLABLE','NOT NULL'),Terminal(')'))))
-->

Keywords and parameters:

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `data_type` - a valid [data type](data-types.md).

**Examples:**

Alter a column in the table:

```sql
ALTER TABLE Person ALTER COLUMN city SET DATA TYPE varchar;
```

#### Supported Transitions

Not all data type transitions are supported. The limitations are listed below:

- `FLOAT` can be transitioned to `DOUBLE`
- `INT8`, `INT16` and `INT64` can be transitioned to `INT32`
- `TYPE SCALE` change is forbidden
- `TYPE PRECISION` increase is allowed for DECIMAL non PK column
- `TYPE LENGTH` increase is allowed for STRING and BYTE_ARRAY non PK column

Other transitions are not supported.

**Examples:**

Changes the possible range of IDs to BIGINT ranges:

```sql
ALTER TABLE Person ALTER COLUMN age SET DATA TYPE BIGINT;
```

Sets the length of a column text to 11:

```sql
ALTER TABLE Person ALTER COLUMN Name SET DATA TYPE varchar(11);
```

### ALTER TABLE IF EXISTS table ALTER COLUMN column SET NOT NULL

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ALTER COLUMN column_name_or_list SET NOT NULL
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ALTER COLUMN'),NonTerminal('column_name_or_list'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Terminal('SET NOT NULL'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.

#### Supported Transitions

Not all data type transitions are supported. The limitations are listed below:

- `NULLABLE` to `NOT NULL` transition is forbidden

### ALTER TABLE IF EXISTS table ALTER COLUMN column DROP NOT NULL

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ALTER COLUMN column_name_or_list DROP NOT NULL
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ALTER COLUMN'),NonTerminal('column_name_or_list'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Terminal('DROP NOT NULL'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.

#### Supported Transitions

Not all data type transitions are supported. The limitations are listed below:

- `NOT NULL` to `NULLABLE` transition is allowed for any non-PK column

### ALTER TABLE IF EXISTS table ALTER COLUMN column SET DEFAULT

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ALTER COLUMN column_name_or_list
  SET DATA TYPE data_type [{ NULL | NOT NULL }] [DEFAULT literal_value]
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ALTER COLUMN'),NonTerminal('column_name_or_list'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Terminal('SET DATA TYPE'),NonTerminal('data_type'),Optional(Sequence(Choice(0,'NULL','NOT NULL'))),Optional(Sequence(Terminal('DEFAULT'),Sequence(Choice(0,NonTerminal('literal_value'))))))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - do not throw an error if a table with the specified table name does not exist.

### ALTER TABLE IF EXISTS table ALTER COLUMN column DROP DEFAULT

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  ALTER COLUMN column_name_or_list DROP DEFAULT
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('ALTER COLUMN'),NonTerminal('column_name_or_list'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Terminal('DROP DEFAULT'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.

### ALTER TABLE IF EXISTS table SET EXPIRE AT

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name EXPIRE AT expiry_column_name
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('EXPIRE'),Terminal('AT'),NonTerminal('expiry_column_name'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `EXPIRE AT` - allows specifying a column with a point in time when a record should be deleted.

### ALTER TABLE IF EXISTS table DROP EXPIRE

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name DROP EXPIRE
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('DROP'),Terminal('EXPIRE'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `DROP EXPIRE` - disables row expiration for the table.

### ALTER TABLE IF EXISTS table DROP SECONDARY ZONE

Removes the table from a secondary distribution zone.

{% hint style="danger" %}
This action is irreversible.
{% endhint %}

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name DROP SECONDARY ZONE
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('DROP'),Terminal('SECONDARY ZONE'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `DROP SECONDARY ZONE` - removes the secondary zone for the table.

**Examples:**

```sql
ALTER TABLE Person DROP SECONDARY ZONE;
```

### ALTER TABLE IF EXISTS SET PARAMETER

Modifies the value of the specified parameter.

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  SET { paramName paramValue | ( paramName paramValue [, ...] ) }
```

<!-- railroad-source:
Diagram(Start({type:'complex'}),Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('SET'),Choice(0,Sequence(NonTerminal('paramName'),NonTerminal('paramValue')),Sequence(Terminal('('),OneOrMore(Sequence(NonTerminal('paramName'),NonTerminal('paramValue')),Terminal(',')),Terminal(')'))))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `param_name` - the name of a parameter to modify. Currently, the following parameters are supported:
  - `stale rows fraction` - fraction of the table that must change for query execution plan to be recreated automatically. Default value is `0.2`.
  - `min stale rows` - number of updates since the last query plan update required to automatically recreate query execution plan. Default value is `500`.

**Examples:**

```sql
ALTER TABLE Person SET min stale rows 1000;
```

### ALTER TABLE IF EXISTS table SET ROW LEVEL SECURITY

Enables or disables row-level security on an existing table. When enabled, only rows permitted by the applicable policies are visible to a user. If no policy applies, the user sees no rows. For a conceptual overview, see [Row-Level Security](../administrators-guide/security/row-level-security.md).

{% hint style="info" %}
Row-level security is available only in GridGain 9 Enterprise and Ultimate editions. Enabling or disabling it requires the `MANAGE_RLS` privilege on the target table.
{% endhint %}

```bnf
ALTER TABLE [IF EXISTS] qualified_table_name
  SET ROW LEVEL SECURITY { ON | OFF }
```

<!-- railroad-source:
Diagram(Terminal('ALTER TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'),Terminal('SET ROW LEVEL SECURITY'),Choice(0,Terminal('ON'),Terminal('OFF')))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the specified table name does not exist.
- `ON` / `OFF` - whether to enable or disable row-level security on the table.

**Examples:**

```sql
ALTER TABLE employees SET ROW LEVEL SECURITY ON;
ALTER TABLE employees SET ROW LEVEL SECURITY OFF;
```

## DROP TABLE

The `DROP TABLE` command drops an existing table. The table will be marked for deletion and will be removed by garbage collection after the [low watermark](../administrators-guide/storage/data-partitions.md#version-storage) point is reached. Until the data is removed, it will be available to [read-only transactions](../developers-guide/transactions.md#read-only-transactions) that check the time before the table was marked for deletion.

{% hint style="info" %}
This can also be done via the [Java API](../developers-guide/java-to-tables.md).
{% endhint %}

```bnf
DROP TABLE [IF EXISTS] qualified_table_name
```

<!-- railroad-source:
Diagram(Terminal('DROP TABLE'),Optional(Terminal('IF EXISTS')),NonTerminal('qualified_table_name'))
-->

![Railroad diagram of DROP TABLE](../../.gitbook/assets/gg9-sql-reference-drop_table_bnf.svg)

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a table with the same name does not exist.

Schema changes applied by this command are persisted on disk. Thus, the changes can survive full cluster restarts.

**Examples:**

Drop Person table if the one exists:

```sql
DROP TABLE IF EXISTS "Person";
```

## CREATE INDEX

Creates a new index.

{% hint style="info" %}
This can also be done via the [Java API](../developers-guide/java-to-tables.md).
{% endhint %}

When you create a new index, it will start building only after all transactions started before the index creation had been completed. Index build will not start if there are any “hung“ transactions in the logical topology of the cluster.

The index status, with the status reason description (e.g., `PENDING` - “Waiting for transaction ABC to complete”) is reflected in the system view.

{% hint style="info" %}
The index cannot include the same column more than once.
{% endhint %}

```bnf
CREATE INDEX [IF NOT EXISTS] name ON qualified_table_name
  { USING { SORTED sorted_column_list | HASH column_list } | sorted_column_list }
```

<!-- railroad-source:
Diagram(Terminal('CREATE INDEX'),Optional(Terminal('IF NOT EXISTS')),NonTerminal('name'),Terminal('ON'),NonTerminal('qualified_table_name'),End({type:'complex'}))
Diagram(Start({type:'complex'}),Sequence(Choice(0,Sequence(Terminal('USING'),Choice(0,Sequence('SORTED',NonTerminal('sorted_column_list')),Sequence('HASH',NonTerminal('column_list')))),NonTerminal('sorted_column_list'))),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - create the index only if an index with the same name does not exist.
- `name` - name of the index.
- `ON` - create index on the defined table.
- `USING SORTED` - if specified, creates a sorted index.
- `USING HASH` - if specified, creates a hash index.

**Examples:**

Create an index `department_name_idx` for the Person table:

```sql
CREATE INDEX IF NOT EXISTS department_name_idx ON Person (department_id DESC, name ASC);
```

Create a hash index `department_name_idx` for the Person table:

```sql
CREATE INDEX name_surname_idx ON Person USING HASH (name, surname);
```

Create a sorted index `department_city_idx` for the Person table:

```sql
CREATE INDEX department_city_idx ON Person USING SORTED (age ASC, city_id DESC);
```

## DROP INDEX

Drops an index.

{% hint style="info" %}
This can also be done via the [Java API](../developers-guide/java-to-tables.md).
{% endhint %}

When you drop an index, it stays in the STOPPING status until all transactions started before the DROP INDEX command had been completed (even those that do not affect any of the tables for which the index is being dropped).
Upon completion of all transactions described above, the space the dropped index had occupied is freed up only when LWM of the relevant partition becomes greater than the time when the index dropping had been activated.
The index status, with the status reason description (e.g., PENDING - “Waiting for transaction ABC to complete”) is reflected in the system view.

```bnf
DROP INDEX [IF EXISTS] index_name
```

<!-- railroad-source:
Diagram(Terminal('DROP INDEX'),Optional(Terminal('IF EXISTS')),NonTerminal('index_name'))
-->

**Keywords and parameters:**

- `index_name` - the name of the index.
- `IF EXISTS` - do not throw an error if an index with the specified name does not exist.

**Examples:**

Drop index if the one exists:

```sql
DROP INDEX IF EXISTS department_name_idx;
```

## CREATE SCHEMA

Creates a new SQL schema.

```bnf
CREATE SCHEMA [IF NOT EXISTS] schema_name
```

<!-- railroad-source:
Diagram(Terminal('CREATE'),Terminal('SCHEMA'),Optional(Terminal('IF NOT EXISTS')),NonTerminal('schema_name'))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - create the schema only if a cache with the same name does not exist.

The `SYSTEM` schema containing meta information is reserved for system use, for example for [system views](../administrators-guide/metrics/system-views.md).

In conformance with SQL standard, `INFORMATION_SCHEMA` and `DEFINITION_SCHEMA` schema names are reserved, but are currently not used.

Additionally, GridGain uses the predefined `PUBLIC` schema as the default schema for simple name resolution.

## DROP SCHEMA

Drops an existing SQL schema. Reserved schemas cannot be dropped.

```bnf
DROP SCHEMA [IF EXISTS] name { RESTRICT | CASCADE }
```

<!-- railroad-source:
Diagram(Terminal('DROP SCHEMA'),Optional(Terminal('IF EXISTS')),NonTerminal('name'),Choice(0,Terminal('RESTRICT'),Terminal('CASCADE')))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a schema with the specified name does not exist.
- `RESTRICT` - used by default. Schema will only be dropped if there are no objects in it.
- `CASCADE` - schema and all objects in it will be dropped.

## CREATE CACHE

{% hint style="warning" %}
Caches must use the storage profile or distribution zone with `aimem` storage engine.
{% endhint %}

Creates a new [cache](../developers-guide/cache.md).

```bnf
CREATE CACHE [IF NOT EXISTS] cache_name
  ( { column_definition | constraint } [, ...] )
  [COLOCATE [BY] ( column_list )]
  [[PRIMARY] ZONE zone_name]
  [[PRIMARY] STORAGE PROFILE profile_name]
  [WRITE MODE { SYNC | ASYNC }]
  [EXPIRE AT expiry_column_name]
```

<!-- railroad-source:
Diagram(Terminal('CREATE'),Terminal('CACHE'),Optional(Terminal('IF NOT EXISTS')),NonTerminal('cache_name'),Terminal('('),Choice(1,NonTerminal('constraint'),NonTerminal('column_definition'),Terminal(',')),Terminal(')'),Optional(Sequence(Terminal('COLOCATE'),Optional('BY'),Terminal('('),NonTerminal('column_list'),Terminal(')'))),End({type:'complex'}))
Diagram(Start({type:'complex'}),Optional(Sequence(Optional('PRIMARY'),Terminal('ZONE'),NonTerminal('zone_name'))),Optional(Sequence(Optional('PRIMARY'),Terminal('STORAGE PROFILE'),NonTerminal('profile_name'))),Optional(Sequence(Terminal('WRITE MODE'),Choice(0,NonTerminal('SYNC'),NonTerminal('ASYNC')))),Optional(Sequence(Terminal('EXPIRE'),Terminal('AT'),NonTerminal('expiry_column_name'))))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - create the cache only if a cache with the same name does not exist.
- `COLOCATE BY` - colocation key. The key can be composite. Primary key must include colocation key. Was `affinity_key` in GridGain 2.x.
- `ZONE` - sets the [Distribution Zone](distribution-zones.md). Can be specified as a case-sensitive string or case-insensitive identifier. Can be preceded by `PRIMARY` to signify the primary distribution zone.
- `STORAGE PROFILE` - sets the [storage profile](../administrators-guide/storage/storage-profiles.md) that will be used to store the table. Must be specified as a case-sensitive string. Can be preceded by `PRIMARY` to signify the primary storage profile.
- `WRITE MODE` - configures if the data is written to [external store](../developers-guide/cache.md#caches-as-external-storage). Default value: `SYNC`. Possible values:
  - `SYNC` - External Cache store writes are synchronous. KeyValueView operations won't return until external cache store write is complete.
  - `ASYNC` - External Cache store writes are asynchronous and performed in background. KeyValueView operations may return before external cache store write completes.
- `EXPIRE AT` - allows specifying a column with a point in time when a record should be deleted.
- `expiry_column_name` - name of the column that contains values on which the record expiry is based.

Example:

Creates a cache `Accounts`:

```sql
CREATE CACHE Accounts (
    accountNumber INT,
    firstName VARCHAR,
    lastName VARCHAR,
    balance DOUBLE,
    ttl TIMESTAMP WITH LOCAL TIME ZONE DEFAULT CURRENT_TIMESTAMP + INTERVAL '2' HOURS,
    PRIMARY KEY (accountNumber, TTL)
) ZONE CACHES EXPIRE AT ttl;
```

## DROP CACHE

Drops an existing cache. The cache will be marked for deletion and will be removed by garbage collection after the [low watermark](../administrators-guide/storage/data-partitions.md#version-storage) point is reached.

```bnf
DROP CACHE [IF EXISTS] cache_name
```

<!-- railroad-source:
Diagram(Terminal('DROP CACHE'),Optional(Terminal('IF EXISTS')),NonTerminal('cache_name'))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a cache with the same name does not exist.

**Examples:**

Drops `Accounts` cache if it exists:

```sql
DROP CACHE IF EXISTS Accounts;
```

## ALTER CACHE

Modifies the settings of an existing cache.

### ALTER CACHE IF EXISTS cache SET EXPIRE AT

Sets or updates the expiration column for a cache. Records will be automatically deleted when the timestamp in the specified column is reached.

```bnf
ALTER CACHE [IF EXISTS] cache_name SET EXPIRE AT expiry_column_name
```

<!-- railroad-source:
Diagram(Terminal('ALTER CACHE'),Optional(Terminal('IF EXISTS')),NonTerminal('cache_name'),Terminal('SET'),Terminal('EXPIRE'),Terminal('AT'),NonTerminal('expiry_column_name'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a cache with the specified name does not exist.
- `expiry_column_name` - the name of the column with expiration timestamps.

**Examples:**

Sets the expiration column for the `Accounts` cache:

```sql
ALTER CACHE Accounts SET EXPIRE AT ttl;
```

### ALTER CACHE IF EXISTS cache DROP EXPIRE

Removes the expiration configuration from a cache. Records will no longer be automatically deleted.

```bnf
ALTER CACHE [IF EXISTS] cache_name DROP EXPIRE
```

<!-- railroad-source:
Diagram(Terminal('ALTER CACHE'),Optional(Terminal('IF EXISTS')),NonTerminal('cache_name'),Terminal('DROP'),Terminal('EXPIRE'),End({type:'simple'}))
-->

**Keywords and parameters:**

- `IF EXISTS` - do not throw an error if a cache with the specified name does not exist.
- `DROP EXPIRE` - disables row expiration for the cache.

**Examples:**

Removes expiration from the `Accounts` cache:

```sql
ALTER CACHE Accounts DROP EXPIRE;
```

## CREATE SEQUENCE

Creates a new sequence object. You can use sequences to generate a sequence of numeric values in ascending or descending order. You can then use [sequence functions](operators-and-functions.md#sequence-functions) to use them in your tables.

```bnf
CREATE SEQUENCE [IF NOT EXISTS] name
  [INCREMENT [BY] increment_value]
  [{ MINVALUE minimum_value | NO MINVALUE }]
  [{ MAXVALUE maximum_value | NO MAXVALUE }]
  [START start_value]
  [CACHE value]
```

<!-- railroad-source:
Diagram(Terminal('CREATE SEQUENCE'),Optional(Terminal('IF NOT EXISTS')),NonTerminal('name'),Optional(Sequence(Terminal('INCREMENT'),Optional('BY'),NonTerminal('increment_value'))))
Diagram(Optional(Choice(1,Sequence(Terminal('MINVALUE'),NonTerminal('minimum_value')),Sequence(Terminal('NO MINVALUE')))),Optional(Choice(1,Sequence(Terminal('MAXVALUE'),NonTerminal('maximum_value')),Sequence(Terminal('NO MAXVALUE')))),Optional(Sequence(Terminal('START'),NonTerminal('start_value'))),Optional(Sequence(Terminal('CACHE'),NonTerminal('value'))))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - create the sequence only if a sequence with the same name does not exist.
- `INCREMENT BY` - how much the sequence is incremented by each time. Can be both positive and negative.  Default value: 1.
  - If positive value is specified, the sequence is ascending.
  - If negative value is specified, the sequence is descending.
- `MINVALUE` - the minimum value of the sequence. Default value: 1 for ascending sequences, minimum value supported by data type for descending sequences.
- `MAXVALUE` - the maximum value of the sequence.Default value: maximum value supported by data type for ascending sequences, -1 for descending sequences.
- `START` - the value the sequence starts at. Default value: same as `MINVALUE` for ascending sequences, or `MAXVALUE` for descending sequences.
- `CACHE` - the amount of sequence numbers that are pre-allocated and stored in memory. Default value: 1000. When preallocated values run out, next access to any sequence method will preallocate values again. `ALTER SEQUENCE` ddl command and [SETVAL()](operators-and-functions.md#nextval) function reset the cache. Any numbers allocated but not used will be lost, resulting in “holes” in the sequence. All generated values are all distinct, not that they are generated purely sequentially.

**Examples:**

Creates a basic ascending sequence with default values:

```sql
CREATE SEQUENCE IF NOT EXISTS defaultSequence;
```

Creates an ascending sequence that starts at 10, and increments by 10 up to the maximum value of 1000

```sql
CREATE SEQUENCE IF NOT EXISTS ascendingSequence INCREMENT BY 10 START 10 MAXVALUE 100000;
```

Creates a descending sequence that starts at 15, and decrements by 50 up to the minimum value of -100;

```sql
CREATE SEQUENCE IF NOT EXISTS descendingSequence INCREMENT BY -5 START 15 MAXVALUE 15 MINVALUE -10000;
```

Uses the `defaultSequence` sequence and the [NEXTVAL()](operators-and-functions.md#nextval) function to automatically increment the ID column in the table. When inserting values, you can skip the ID column and it will get incremented automatically:

```sql
CREATE SEQUENCE IF NOT EXISTS defaultSequence;

CREATE TABLE IF NOT EXISTS Person (
  id bigint default NEXTVAL('defaultSequence') primary key ,
  city_id bigint,
  name varchar,
  age int,
  company varchar
);

INSERT INTO Person (city_id, name, age, company) values (1, 'John', 30, 'newCorp'), (2, 'Jane', 24, 'oldCorp');
```

## ALTER SEQUENCE

Changes the properties of an existing sequence object.

```bnf
ALTER SEQUENCE [IF EXISTS] name
  [INCREMENT [BY] increment_value]
  [MINVALUE minimum_value]
  [MAXVALUE maximum_value]
  [START [WITH] start]
  [CACHE value]
```

<!-- railroad-source:
Diagram(Terminal('ALTER SEQUENCE'),Optional(Terminal('IF EXISTS')),NonTerminal('name'),Optional(Sequence(Terminal('INCREMENT'),Optional('BY'),NonTerminal('increment_value'))),Optional(Sequence(Terminal('MINVALUE'),NonTerminal('minimum_value'))),Optional(Sequence(Terminal('MAXVALUE'),NonTerminal('maximum_value'))),Optional(Sequence(Terminal('START'),Optional('WITH'),NonTerminal('start'))),Optional(Sequence(Terminal('CACHE'),NonTerminal('value'))))
-->

**Keywords and parameters:**

- `IF NOT EXISTS` - create the sequence only if a sequence with the same name does not exist.
- `INCREMENT BY` - how much the sequence is incremented by each time. Can be both positive and negative.  Default value: 1.
  - If positive value is specified, the sequence is ascending.
  - If negative value is specified, the sequence is descending.
- `MINVALUE` - the minimum value of the sequence. Default value: 1 for ascending sequences, minimum value supported by data type for descending sequences.
- `MAXVALUE` - the maximum value of the sequence.Default value: maximum value supported by data type for ascending sequences, -1 for descending sequences.
- `START` - the value the sequence starts at. Default value: same as `MINVALUE` for ascending sequences, or `MAXVALUE` for descending sequences.
- `CACHE` - the amount of sequence numbers that are pre-allocated and stored in memory. Default value: 1000.

**Examples:**

Alters the default sequence to have 20000 as maximum value:

```sql
ALTER SEQUENCE IF EXISTS defaultSequence MAXVALUE 20000;
```

## DROP SEQUENCE

Drops an existing sequence object.

```bnf
DROP SEQUENCE [IF EXISTS] name
```

<!-- railroad-source:
Diagram(Terminal('DROP SEQUENCE'),Optional(Terminal('IF EXISTS')),NonTerminal('name'))
-->
