---
description: >-
  The Performance Module in MariaDB ColumnStore handles I/O under User Module
  instructions, executing distributed scans, hash joins, and aggregations for
  massively parallel query processing.
hidden: true
---

# ColumnStore Performance Module

The Performance Module performs I/O operations in support of read and write processing. It doesn't see the query itself, but only a set of instructions given to it by a [User Module](columnstore-user-module.md).

There are three critical tasks key to scaling out database behavior:

* Distributed Scans
* Distributed Hash Joins
* Distributed Aggregation

The combination of these enables massive parallel processing (MPP) for query-intensive environments.

## Processes

The Performance Module is composed of a number of processes

### Managing and Monitoring Processes

The Process Manager, or ProcMgr, is the process responsible for starting, monitoring and restarting all MariaDB ColumnStore processes on the Performance Module.

In order to accomplish this, ProcMgr uses the Process Monitor, or ProcMon on each Performance Module to keep track of MariaDB ColumnStore processes.

### Processing Queries

The Primary Process, or PrimProc, handles query execution. The [User Modules](columnstore-user-module.md) process queries from the application into instructions that are sent to the Performance Module. PrimProc executes these instructions as block oriented I/O operations to perform predicate filtering, join processing, and the initial aggregation of data, after which PrimProc sends the data back to the User Module.

### Performing Loads and Writes

The Performance Module processes loads and writes to the underlying persistent storage. It uses two processes to handle this: WriteEngineServer and cpimport.

WriteEngineServer coordinates DML, DDL and imports on each Performance Module. DDL changes are made persistent within the System Catalog, which keeps track of all ColumnStore metadata.

User and Performance modules both use cpimport. On the Performance Module it updates database files when loading bulk data. This allows ColumnStore to support fully parallel loads.

## Shared Nothing Data Cache

The Performance Module uses a shared nothing data cache. When it first accesses data, it operates on data as instructed by the [User Module](columnstore-user-module.md) and caches it in an LRU-based buffer for subsequent access.

When the Performance Module runs on a dedicated server, you can dedicate the majority of the available to this data cache. As the Performance Module cache is shared nothing design:

* There is no data block pinging between participating Performance Module nodes, (as sometimes occurs in other multi-instance/shared disk database systems).
* More Performance Module nodes added to a system, the larger the overall cache size for the database.

## Failover

When deploying MariaDB ColumnStore with multiple Performance Module nodes, a heartbeat mechanism ensures that all nodes are online and there is transparent failover in the event that a particular node fails. If a node abnormally terminates, in-process queries return an error. Users that receive an error due to Performance Module can resubmit the query. ColumnStore then does the work using the remaining Performance Modules.

In cases of failover where the underlying storage data is externally mounted, (such as with EC2 EBS or SAN), the mapping of data blocks to Performance Modules is re-organized across working Performance Modules, and the Extent Maps on the User Modules are re-evaluated, so that queries are sent to the appropriate nodes. That is, the DB Roots attached to the failed Performance Module are attached to working Performance Modules. This process is transparent to the user and does not require manual intervention.

When the failed Performance Module is brought back online, ColumnStore auto-adopts it back into the configuration and begins using it for work.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
