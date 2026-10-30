---
description: >-
  Reference documentation for GridGain 9 SQL — statements, data types,
  functions, operators, keywords, and standards conformance.
---

# SQL Reference

This section is the reference for GridGain 9 SQL. It covers the supported SQL statements — data definition, data manipulation, operational commands, and distribution zone management — along with data types, functions and operators, optimizer hints, keywords, the `EXPLAIN` command, and GridGain's conformance with the ANSI SQL:2016 standard.

Use the pages in this section to look up exact syntax, parameters, and behavior for the SQL supported by GridGain 9.

{% columns %}
{% column %}
{% content-ref url="ddl.md" %}
[Data Definition Language (DDL)](ddl.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the Data Definition Language (DDL) commands supported by GridGain 9, including CREATE, ALTER, and DROP for tables, indexes, schemas, caches, and sequences.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dml.md" %}
[Data Manipulation Language (DML)](dml.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Data manipulation language (DML) commands supported by GridGain 9: DELETE, INSERT, MERGE, and UPDATE, with their syntax and parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="operational-commands.md" %}
[Operational Commands](operational-commands.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Operational SQL commands in GridGain 9: SELECT, COPY INTO for data import and export, and the KILL QUERY, KILL TRANSACTION, and KILL COMPUTE commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="distribution-zones.md" %}
[Distribution Zones](distribution-zones.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Distribution zones in GridGain 9 and the SQL commands that manage them: CREATE ZONE, ALTER ZONE, and DROP ZONE, with keywords, parameters, and examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions.md" %}
[Transactions](transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL transaction control in GridGain 9 using START TRANSACTION and COMMIT, including read-only and read-write modes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="operators-and-functions.md" %}
[Operators and Functions](operators-and-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL functions reference for GridGain 9, covering aggregate, date/time, JSON, numeric, string, and other functions built on Apache Calcite.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-types.md" %}
[Data Types](data-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL data types available in GridGain 9 — boolean, numeric, character, binary, date/time, UUID, and NULL — and how each maps to Java, .NET, and C++ types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="keywords.md" %}
[Keywords](keywords.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reserved and non-reserved SQL keywords in GridGain 9, with their reserved status in GridGain 9 and in the SQL:2016 standard.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-hints.md" %}
[Optimizer Hints](optimizer-hints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL optimizer hints in GridGain 9: hint block syntax, precedence rules, and the supported hints such as FORCE_INDEX, NO_INDEX, and ENFORCE_JOIN_ORDER.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="access-control-functions.md" %}
[Access Control Functions](access-control-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the GridGain 9 access control SQL functions — creating and managing users, roles, privileges, and row-level security policies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain-statement.md" %}
[EXPLAIN Statement](explain-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The EXPLAIN command in GridGain 9 displays the execution plan of an SQL query, including relational operators, attributes, and query-to-cluster mapping.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain-operators-list.md" %}
[List of Operators](explain-operators-list.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for all relational operators that can appear in a GridGain 9 EXPLAIN plan, with their semantics and supported attributes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="grammar-reference.md" %}
[Grammar Reference](grammar-reference.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the shared SQL grammar elements used across GridGain 9 DDL, DML, and other SQL statements, with the BNF syntax for each production.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-conformance/" %}
[SQL Conformance](sql-conformance/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain 9 conformance with the ANSI SQL:2016 standard — the features that are supported and those that are not.
{% endcolumn %}
{% endcolumns %}
