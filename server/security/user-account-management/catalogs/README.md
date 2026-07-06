---
description: >-
  Introduction to Catalogs, a multi-tenancy feature for isolating database
  objects and users, planned for future MariaDB releases.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Catalogs

{% include "../../../.gitbook/includes/catalogs.md" %}

Catalogs are a user account management feature. This section explains their role in organizing database objects and controlling access permissions.

{% columns %}
{% column %}
{% content-ref url="catalogs-overview.md" %}
[catalogs-overview.md](catalogs-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduces MariaDB catalogs, a multi-tenancy feature that lets a single server host multiple independent tenants, each with their own users, schemas, and logs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="starting-with-catalogs.md" %}
[starting-with-catalogs.md](starting-with-catalogs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to initializing a MariaDB server with catalog support using `mariadb-install-db --catalogs` and adding new catalogs to a running instance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="catalog-specific-functions-and-variables.md" %}
[catalog-specific-functions-and-variables.md](catalog-specific-functions-and-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the catalog() function, which returns the current catalog name, and the @@catalogs system variable, which indicates if the server is configured for catalogs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="catalog-status-variables.md" %}
[catalog-status-variables.md](catalog-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Covers status variables related to catalog operations and performance, useful for monitoring multi-tenant environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connecting-to-a-server-configured-for-catalogs.md" %}
[connecting-to-a-server-configured-for-catalogs.md](connecting-to-a-server-configured-for-catalogs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to connect to a specific catalog using the --catalog client option or the catalog_name.database_name syntax.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-catalog.md" %}
[create-catalog.md](create-catalog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define external catalogs for data integration. This statement configures connections to remote storage systems, allowing query access to external data sources.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="show-create-catalog.md" %}
[show-create-catalog.md](show-create-catalog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the SHOW CREATE CATALOG statement, which displays the SQL statement used to create a specific catalog.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="show-catalogs.md" %}
[show-catalogs.md](show-catalogs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the SHOW CATALOGS statement, which lists all available catalogs on the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="use-catalog.md" %}
[use-catalog.md](use-catalog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the USE CATALOG statement, allowing a user to switch their current session's context to a different catalog.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-catalog.md" %}
[drop-catalog.md](drop-catalog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the DROP CATALOG statement, used to remove a catalog and all its associated databases and users.
{% endcolumn %}
{% endcolumns %}
