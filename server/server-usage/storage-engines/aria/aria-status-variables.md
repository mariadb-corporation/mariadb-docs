---
description: >-
  A list of status variables specific to the Aria engine, providing metrics on
  page cache usage, transaction log syncs, and other internal operations.
---

# Aria Status Variables

This page documents status variables related to the [Aria storage engine](./). See [Server Status Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Aria_pagecache_blocks_not_flushed`

* Description: The number of dirty blocks in the Aria page cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status).
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_blocks_unused`

* Description: Free blocks in the Aria page cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status).
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_blocks_used`

* Description: Blocks used in the Aria page cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status).
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_read_requests`

* Description: The number of requests to read something from the Aria page cache.
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_reads`

* Description: The number of Aria page cache read requests that caused a block to be read from the disk.
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_write_requests`

* Description: The number of requests to write a block to the Aria page cache.
* Scope: Global
* Data Type: `numeric`

#### `Aria_pagecache_writes`

* Description: The number of blocks written to disk from the Aria page cache.
* Scope: Global
* Data Type: `numeric`

#### `Aria_transaction_log_syncs`

* Description: The number of Aria log fsyncs.
* Scope: Global
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
