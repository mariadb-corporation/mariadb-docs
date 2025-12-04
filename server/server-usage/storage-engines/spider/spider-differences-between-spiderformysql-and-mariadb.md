# Spider Differences Between SpiderForMySQL and MariaDB

### SQL Syntax

* With `SpiderForMySQL`, the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement uses `CONNECTION` to define spider table variables whereas MariaDB uses `COMMENT`.

### Features

* [HANDLER](../../../reference/sql-structure/nosql/handler/) can not be translated to SQL in MariaDB
* Concurrent background search is not yet implemented in MariaDB
* Vertical partitioning storage engine VP is not implemented in MariaDB
* `CREATE TABLE` can use [table discovery](../storage-engines-storage-engine-development/table-discovery.md) in MariaDB
* [JOIN](../../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax.md) performance improvement using [join\_cache\_level](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level)>1`and`[join\_buffer\_size](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size) in MariaDB

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
