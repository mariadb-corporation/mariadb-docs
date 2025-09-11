---
description: Advice for writing and maintaining applications using databases.
---

# Database Applications

> By Anders Karlsson, Principal Sales Engineer at MariaDB Plc — 24 minutes read

This document offers guidance on creating and maintaining database applications with minimal downtime and effort, covering aspects from database schema design to application code.

Here's a summary of key areas and advice covered; find the full guide on the subsequent pages.

* Database Design: A well-designed database is crucial. Standardization in naming conventions (e.g., `orders_t`), data types, character sets (preferably UTF-8 for full Unicode support, `utf8mb4`), and collations is highly recommended to ensure ease of maintenance.
* Data Types:
  * Choosing appropriate types: Consider if a number will be computed; if not, a string might be better (e.g., `VARCHAR` for product codes with leading zeros).
  * Text/String: Use `VARCHAR` and be generous with sizing, as schema upgrades for length extensions are undesirable. UTF-8 (specifically `utf8mb4`) is generally preferred for character sets, and consistency in collations simplifies maintenance.
  * Numeric: Use `BIGINT` for auto-generated primary keys to prevent overflow issues. Avoid `FLOAT` and `DOUBLE` for monetary values due to rounding issues; `DECIMAL` is more accurate.
  * Temporal: Understand the differences between `DATETIME` (stores time as is) and `TIMESTAMP` (affected by client-side time zones) before using them.
  * Other: Be cautious with `ENUM` and `SET` types, as adding values requires schema alteration.
* Schema Objects:
  * Views: Excellent for hiding complexity and supporting different schema versions. Naming views with version strings (`orders_v_1`) can be beneficial. They can also be used to reference data in newer schemas during migration.
* Application Code:
  * Separation of Concerns: While complete separation of application logic and database logic is difficult, practices like using ORMs and stored procedures can help.
  * Object Relational Mappers (ORM): Tools like Hibernate allow applications to be less reliant on specific database schema details, aiding maintenance, though performance and complex operations might still require attention.
  * Stored Procedures and Functions: Isolate database logic from application logic, making maintenance easier by centralizing complex SQL operations in the database layer.
  * Best Practices in Application SQL:
    * Avoid `SELECT *`: Explicitly list columns to prevent issues if table schema changes (column order or addition).
    * Avoid `INSERT` without column names: Always specify column names in `INSERT` statements to avoid errors when table schema changes.
    * Processing of column data: Be consistent; processing in the application can sometimes make SQL more readable.
    * Use of reserved words: Avoid using SQL reserved words for schema objects and column names, even if quoting them makes them valid.
    * Relying on non-explicit assumptions: Never assume row ordering without an `ORDER BY` clause. The order of returned rows is otherwise undetermined. Be cautious with `LIMIT` in `UPDATE` or `DELETE` without `ORDER BY`.
* Code and Schema Standardization: Adhering to internal standards for data types, column names, and database interaction improves maintainability and code readability.
* Complex SQL: Break down very complex SQL (especially `SELECT JOIN`s) into multiple statements or use temporary tables to improve readability and maintainability.
* Canary Testing:
  * Database Naming: Utilize the MariaDB `database` concept (similar to schema) as a namespace to allow different schemas to coexist, avoiding hard-coding database names.
  * Views: Create separate databases for new versions with views referencing data in older or newer schemas to manage transitions.
  * Replication: Use MariaDB replication, particularly statement-based replication (SBR), for canary testing by replicating from the production system to a new server with the updated schema.
  * Invisible Columns: A MariaDB feature allowing columns to exist without being exposed by default, useful in scenarios where old applications use `SELECT *` or `INSERT` without column names, allowing new columns to be added without breaking existing code.
