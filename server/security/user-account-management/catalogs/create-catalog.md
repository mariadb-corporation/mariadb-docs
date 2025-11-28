---
description: >-
  Define external catalogs for data integration. This statement configures
  connections to remote storage systems, allowing query access to external data
  sources.
---

# CREATE CATALOG

{% include "../../../.gitbook/includes/catalogs.md" %}

## Syntax

```bnf
CREATE CATALOG [IF NOT EXISTS] catalog_name
    [create_specification] ...

create_specification:
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'comment'
```

## Description

Creates a [catalog](./) and the `mysql`, `sys` and `performance_schema` schemas inside the catalog.

`CREATE CATALOG` can only be performed by a user in the `def` catalog with the CATALOG privilege.

Note that no users are created.

## Example

```sql
CREATE CATALOG cat1;
USE CATALOG cat1;
CREATE USER root@localhost;
GRANT ALL PRIVILEGES ON *.* TO root@localhost;
CREATE DATABASE test;
```

## Limitations

The catalog name is limited to 64 characters. All characters must be in the basic ASCII set:\
(A-Z, a-z, -, \_)\
This limitations is to be able to run catalogs with engines like InnoDB which has limited\
space in their internal data dictionary.

## Pre-Creating Catalog Directories

`CREATE CATALOG` works even if the catalog directory already exists (as long as there is no `mysql` sub directory). This is to allow a database administrator to pre-create the catalog directory and mount it to disk volume and optionally add a [configuration file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) inside the catalog directory.\
The directory will not be recognized as a catalog or show up in [SHOW CATALOGS](show-catalogs.md) until the `mysql` sub directory is created by [CREATE CATALOG](create-catalog.md) or [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md).

## See Also

* [marriadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) can be used to create multiple catalogs with a default root user in one go.
* [DROP CATALOG](drop-catalog.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
