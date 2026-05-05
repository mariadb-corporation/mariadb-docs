---
description: >-
  The User Module in MariaDB ColumnStore orchestrates end-user queries,
  turning MariaDB query plans into ColumnStore Job Lists and handling hash
  joins, final aggregation, and concurrency.
hidden: true
---

# ColumnStore User Module

The User Module manages and controls the operation of end user queries. It maintains the state of each query, issues requests to one or more Performance Modules to process the query, and resolves the query by aggregating the various result-sets from all participating Performance Modules into the one returned to the end user.

## Usage

The primary purpose of the User Module is to handle concurrency scaling. It never directly touches database files and doesn't require visibility to them. It uses a machine's RAM in a transitory manner to assemble partial query results into a complete answer that's returned to the user.

It is responsible for the following core functions:

* Transforming the MariaDB query plan into a ColumnStore Job List.
* Performing InfiniDB Object ID lookups from the MariaDB ColumnStore system catalog.
* Inspecting the Extent Map to reduce I/O. It accomplishes this through the elimination of unnecessary extents. For more information, see [Storage Architecture](columnstore-storage-architecture.md).
* Issuing instructions (sometimes called 'primitive operation'), to Performance Modules.
* Executing hash joins as needed, depending on the size of smaller tables in the join. Helps manage distributed hash joins by sending needed hash maps to the Performance Modules.
* Executing cross-table-scope functions and expressions that occur after a hash join.
* Receiving data from the Performance Modules, re-transmitting it back to them where necessary.
* Executing follow-up steps for all aggregation and distinct processing.
* Returning data to the MariaDB interface.

## Processes

The User Module contains several processes, including [mysqld](columnstore-user-module.md#mariadb-server), [ExeMgr](columnstore-user-module.md#execution-manager), and [distribution managers](columnstore-user-module.md#distribution-managers).

### MariaDB Server

The User Module runs `mysqld`. This is the MariaDB Server running with ColumnStore. It performs the same tasks as a normal MariaDB Server deployment: validating connections, parsing SQL statements, SQL plan generation, and final result-set distribution.

Additionally, this server converts MariaDB Server query plans into ColumnStore query plan format. This format is essentially a parse tree, but adds execution hints from the optimizer to assist the User Module in converting the parse tree to a Job List.

### Execution Manager

The ExeMgr listens on a TCP/IP port for query parse trees from the MariaDB Server. It's responsible for converting these query parse trees into a Job List.

Job Lists represent the sequence of instructions necessary to answer the query. The ExeMgr walks the query parse tree and iteratively generates the job steps, optimizing and re-optimizing the Job List as it goes.

The major categories of job steps are the application of a column filter, processing table joins, and the projection of returned columns. Each operation in the query plan executes in parallel by the Job List itself and has the capability of running entirely on the User Module, entirely on the Performance Module or in some combination.

Each node uses the Extent Map to determine which Performance Modules to send work orders. For more information on Extent Maps, see [Storage Architecture](columnstore-storage-architecture.md).

### Distribution Managers

In addition to these, the User Module also runs processes for DMLProc, DDLPrc and cpimport.

DMLProc and DDLProc distribute DML and DDL statements to the appropriate Performance Modules. When cpimport runs on the User Module, it distributes source files to the Performance Modules.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
