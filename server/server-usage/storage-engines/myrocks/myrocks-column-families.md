---
description: >-
  Learn about MyRocks column families, a mechanism for grouping data similar to
  tablespaces, to optimize compression and Bloom filter settings per family.
---

# MyRocks Column Families

[MyRocks](./) stores data in column families. These are similar to tablespaces.\
By default, the data is stored in the `default` column family.

One can specify which column family the data goes to by using index comments:

```sql
INDEX index_name(col1, col2, ...) COMMENT 'column_family_name'
```

If the column name starts with `rev:`, the column family is reverse-ordered.

## Reasons for Column Families

Storage parameters like

* Bloom filter settings
* Compression settings
* Whether the data is stored in reverse order

are specified on a per-column family basis.

## Creating a Column Family

When creating a table or index, you can specify the name of the column family for it. If the column family doesn't exist, it are automatically created.

## Dropping a Column Family

There is currently no way to drop a column family.\
RocksDB supports this internally but MyRocks doesn't provide any way to do it.

## Setting Column Family Parameters

Use these variables:

* [rocksdb\_default\_cf\_options](myrocks-system-variables.md#rocksdb_default_cf_options) - a my.cnf parameter specifying default options for all column families.
* [rocksdb\_override\_cf\_options](myrocks-system-variables.md#rocksdb_override_cf_options) - a my.cnf parameter specifying per-column family option overrides.
* [rocksdb\_update\_cf\_options](myrocks-system-variables.md#rocksdb_update_cf_options) - a dynamically-settable variable which allows to change parameters online. Not all parameters can be changed.

### rocksdb\_override\_cf\_options

This parameter allows one to override column family options for specific column families.\
Here is an example of how to set option1=value1 and option2=value for column family cf1, and option3=value3 for column family cf3:

```
rocksdb_override_cf_options='cf1={option1=value1;option2=value2};cf2={option3=value3}'
```

One can check the contents of `INFORMATION_SCHEMA.ROCKSDB_CF_OPTIONS` to see what options are available.

Options that are frequently configured are:

* Data compression. See [myrocks-and-data-compression](myrocks-and-data-compression.md).
* Bloom Filters. See [myrocks-and-bloom-filters](myrocks-and-bloom-filters.md).

## Examining Column Family Parameters

See the [INFORMATION\_SCHEMA.ROCKSDB\_CF\_OPTIONS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-myrocks-tables/information-schema-rocksdb_cf_options-table.md) table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
