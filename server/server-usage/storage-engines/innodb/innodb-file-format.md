---
description: >-
  Learn about the different file formats supported by InnoDB, such as Antelope
  and Barracuda, and how they impact table features and storage.
---

# InnoDB File Format

## Setting a Table's File Format

A table's tablespace is tagged with the lowest InnoDB file format that supports the table's [row format](innodb-row-formats/innodb-row-formats-overview.md). So, even if the `Barracuda` file format is enabled, tables that use the `COMPACT` or `REDUNDANT` row formats are tagged with the `Antelope` file format in the [information\_schema.INNODB\_SYS\_TABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table.

## Supported File Formats

The [InnoDB](./) storage engine supports two different file formats:

* `Antelope`
* `Barracuda`

### Antelope

In [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.1) and before, the default file format is `Antelope`. In [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2) and later, the `Antelope` file format is deprecated.

`Antelope` is the original InnoDB file format. It supports the `COMPACT` and `REDUNDANT` row formats, but not the `DYNAMIC` or `COMPRESSED` row formats.

### Barracuda

In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and before, the `Barracuda` file format is only supported if the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable is set to `ON`. In [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2) and later, the default file format is `Barracuda` and `Antelope` is deprecated.

`Barracuda` is a newer InnoDB file format. It supports the `COMPACT`, `REDUNDANT`, `DYNAMIC` and `COMPRESSED` row formats. Tables with large BLOB or TEXT columns in particular could benefit from the dynamic row format.

### Future Formats

InnoDB might use new file formats in the future. Each format will have an identifier from 0 to 25, and a name. The names have already been decided, and are animal names listed in an alphabetical order: Antelope, Barracuda, Cheetah, Dragon, Elk, Fox, Gazelle, Hornet, Impala, Jaguar, Kangaroo, Leopard, Moose, Nautilus, Ocelot, Porpoise, Quail, Rabbit, Shark, Tiger, Urchin, Viper, Whale, Xenops, Yak and Zebra.

## Checking a Table's File Format.

The [information\_schema.INNODB\_SYS\_TABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table can be queried to see the file format used by a table.

A table's tablespace is tagged with the lowest InnoDB file format that supports the table's [row format](innodb-row-formats/innodb-row-formats-overview.md). So, even if the `Barracuda` file format is enabled, tables that use the `COMPACT` or `REDUNDANT` row formats are tagged with the `Antelope` file format in the [information\_schema.INNODB\_SYS\_TABLES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table.

## Compatibility

Each tablespace is tagged with the id of the most recent file format used by one of its tables. All versions of InnoDB can read tables that use an older file format. However, it can not read from more recent formats. For this reason, each time InnoDB opens a table it checks the tablespace's format, and returns an error if a newer format is used.

This check can be skipped via the [innodb\_file\_format\_check](innodb-system-variables.md#innodb_file_format_check) variable. Beware that, is InnoDB tries to repair a table in an unknown format, the table are corrupted! This happens on restart if innodb\_file\_format\_check is disabled and the server crashed, or it was closed with fast shutdown.

To downgrade a table from the Barracuda format to Antelope, the table's `ROW_FORMAT` can be set to a value supported by Antelope, via an [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) statement. This recreates the indexes.

The Antelope format can be used to make sure that tables work on MariaDB and MySQL servers which are older than 5.5.

## See Also

* [InnoDB Storage Formats](innodb-row-formats/innodb-row-formats-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
