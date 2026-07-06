---
description: >-
  Find statements to remove database objects. This section details the syntax
  for deleting databases, tables, users, and other entities when they are no
  longer needed.
---

# DROP

{% columns %}
{% column %}
{% content-ref url="drop-database.md" %}
[drop-database.md](drop-database.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to removing databases in MariaDB. Complete DROP DATABASE syntax with IF EXISTS, permissions, and recovery options for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-event.md" %}
[drop-event.md](drop-event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a scheduled event from the server. This command stops the event from executing and deletes its definition from the system tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-index.md" %}
[drop-index.md](drop-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove an existing index from a table. This command deletes the index structure, potentially impacting query performance but freeing storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-logfile-group.md" %}
[drop-logfile-group.md](drop-logfile-group.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a log file group. This statement, primarily for NDB Cluster, deletes the undo log files associated with the specified log file group.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-package-body.md" %}
[drop-package-body.md](drop-package-body.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Delete the body of a stored package. This command removes the implementation logic while preserving the package specification and interface.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-package.md" %}
[drop-package.md](drop-package.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a stored package completely. This command deletes both the package specification (interface) and its body (implementation) from the database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-server.md" %}
[drop-server.md](drop-server.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a server definition. This command deletes the connection details for a remote server used by the FEDERATED or SPIDER storage engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-table.md" %}
[drop-table.md](drop-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete DROP TABLE syntax: TEMPORARY, IF EXISTS, WAIT/NOWAIT, RESTRICT/CASCADE options, metadata locks, atomic DROP, and replication behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-tablespace.md" %}
[drop-tablespace.md](drop-tablespace.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Delete a tablespace. This command removes the physical file container used for storing table data, applicable to engines like InnoDB or NDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-trigger.md" %}
[drop-trigger.md](drop-trigger.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a trigger from a table. This command deletes the trigger definition, preventing it from firing on future INSERT, UPDATE, or DELETE events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../../server-usage/views/drop-view.md" %}
[drop-view.md](../../../../server-usage/views/drop-view.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use the DROP VIEW statement to remove one or more views from the database, including required privileges.
{% endcolumn %}
{% endcolumns %}
