---
description: >-
  Instructions for manually installing MariaDB on Windows from a ZIP archive,
  useful for portable installations or advanced configuration needs.
---

# Installing MariaDB Windows ZIP Packages

Users need to run [mariadb-install-db.exe](../installing-system-tables-mariadb-install-db/mariadb-install-db-exe.md), without parameters to create a data directory, e.g

```bash
C:\zip_unpack\directory> bin\mariadb-install-db.exe
```

Then you can start server like this

```bash
C:\zip_unpack\directory> bin\mariadbd.exe --console
```

If you like to customize the server instance (data directory, install as service etc), please refer to [mariadb-install-db.exe documentation](../installing-system-tables-mariadb-install-db/mariadb-install-db-exe.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
