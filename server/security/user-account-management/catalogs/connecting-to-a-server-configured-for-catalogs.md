---
description: >-
  Explains how to connect to a specific catalog using the --catalog client
  option or the catalog_name.database_name syntax.
---

# Connecting to a Server Configured for Catalogs

{% include "../../../.gitbook/includes/catalogs.md" %}

When connecting to a MariaDB server configured for [catalogs](./), one has to provide the catalog to connect to. There are several ways to do this:

All new native MariaDB clients will support the `--catalog` option:

```
mariadb --catalog=mine test
```

New and old clients can use the 'catalog\_name.database\_name' syntax to connect:

```
mariadb mine.test
```

This will connect the user to the 'mine' catalog and the database 'test'.

Note that one consequence of this is that one should not have a database that contains '.' in\
the name. If such a database exists, one can still connect to it by using the `--catalog=` option or prefixing the database with the catalog, like in `def.data.base.name`.

One will also be able to configure the MariaDB server to automatically choose catalogs depending on the port or IP they are using to connect to the server. This is done by adding the following to the catalog specific my.cnf file, residing in the catalog directory:

```
[[mariadbd]]
--port=#
--connect-ip=
```

If catalogs is not specified either directly (---catalog=#) or indirectly (with port or ip) the catalog `def` will be used.

When connecting to a server not configured for catalogs, one can still use `mariadb --catalog=def` or `mariadb def.datbase_name`.

To check if a server supports catalogs:

```sql
SELECT @@catalogs;
+------------+
| @@catalogs |
+------------+
|          0 |
+------------+
USE catalog foo;
ERROR 4193 (HY000): MariaDB is not configured to support catalogs
```

0 means that the server is not configured for catalogs.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
