---
description: >-
  Guide to initializing a MariaDB server with catalog support using
  `mariadb-install-db --catalogs` and adding new catalogs to a running instance.
---

# Starting with Catalogs

{% include "../../../.gitbook/includes/catalogs.md" %}

## Background

[mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) initializes the MariaDB data directory and creates the [system tables](../../../reference/system-tables/) in the [mysql](../../../reference/system-tables/the-mysql-database-tables/) database.

When used with the `--catalog` options it will initialize MariaDB server to use catalogs.\
The [mariadbd server](../../../server-management/starting-and-stopping-mariadb/mariadbd.md) will automatically discover if catalogs are used or not.

Note that **one cannot change** a 'normal server' to a server with catalogs or a server with catalogs to\
a 'normal server'. In the future we will add tools that will allow one to easily move an existing server inside a catalog or move an server inside a catalog to a standalone server.

## Initializing a New Server with Catalog Support

To initialize a server with 4 catalogs (the `def` catalog, that holds the catalog root user (CRU) is automatically created):

```bash
mariadb_install_db --catalogs="cat1 cat2 cat3" --datadir=/my/data/
```

The above will create a directory `/my/data` and the 4 directories under it, one for each catalog.

## Adding More Catalogs to a Running Server

### Creating Catalogs with CREATE CATALOG

One can create a new catalog with [CREATE CATALOG catalog\_name](create-catalog.md)

### Creating Catalogs with mariadb\_install\_db

When adding more catalogs to an existing server, `mariadb_install_db` will start the [mariadb client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) to execute the needed commands on the running server. This is why one has to supply user and password to `mariadb_install_db`.

```bash
mariadb_install_db --catalogs="cat4 cat5 cat6" --datadir=/my/data --catalog-user=monty --catalog-password
```

One benefit of using `mariadb_install_db` is that it's possible to create many catalogs with one command.

## See Also

* [CREATE CATALOG](create-catalog.md)
* [DROP CATALOG](drop-catalog.md)
* [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
