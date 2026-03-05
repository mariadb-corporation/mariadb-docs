---
description: >-
  Highlights the administrative tools within the Workspace, including the Schema
  Inspector, Object Browser, user management, and live process list viewing.
---

# Database Administration

The MariaDB Enterprise Manager Workspace includes a powerful set of integrated tools that allow DBAs and developers to perform common administrative tasks graphically, without needing to write raw SQL commands. These features are primarily accessed through the **Schemas Sidebar** and dedicated tabs in the main worksheet area.

## Schema Inspector

The Schema Inspector provides detailed, read-only metadata views for any selected schema object. This allows you to quickly understand the structure, data types, constraints, and dependencies of your tables, views, and other objects without querying the `information_schema`. To use it, simply click on an object in the Object Browser.

## Object Browser

The Object Browser is the hierarchical tree view located in the **Schemas Sidebar** on the left side of the Workspace. It is your primary tool for navigating and exploring your database instances. You can expand databases to see their tables, views, stored procedures, and triggers, and use the filter box at the top to quickly locate specific objects.

## Object Editor

The Object Editor allows you to create, modify, and delete schema objects using graphical forms and dialogs. You can access these functions by right-clicking on an object (or object type) in the **Object Browser**. This will open a context menu with actions such as:

* `CREATE TABLE`, `CREATE VIEW`
* `ALTER TABLE`
* `DROP TABLE`
* Managing constraints and relationships
* Renaming or copying objects

## User Management

This dedicated tab provides a grid-based interface for managing database users and their privileges directly, without writing `GRANT` or `CREATE USER` statements.

From this interface, you can:

* **View** a list of all database users and their assigned global privileges.
* **Create** new database users using a simple form.
* **Edit** an existing user's password or modify their privileges.
* **Delete** users who no longer require access.

## Process List Viewer

The **Processlist** tab provides a real-time view of the database server's active sessions and the commands they are executing, equivalent to running `SHOW FULL PROCESSLIST`. This is an essential tool for diagnosing performance issues.

Using the Processlist Viewer, you can:

* **Monitor** all active connections, their current status (e.g., `Query`, `Sleep`), and how long they have been running.
* **Identify** long-running or problematic queries that may be impacting server performance.
* **Manage** live sessions, which may include the ability to terminate (kill) a specific process.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
