# OQGRAPH System and Status Variables

This page documents system and status variables related to the [OQGRAPH storage engine](../../../server-usage/storage-engines/oqgraph-storage-engine/). See [Server Status Variables](server-status-variables.md) and [Server System Variables](server-system-variables.md) for complete list of all system and status variables.

## System Variables

#### `oqgraph_allow_create_integer_latch`

* Description: Created when the [OQGRAPH](../../../server-usage/storage-engines/oqgraph-storage-engine/) storage engine is installed, if set to `1` (`0` is default), permits the `latch` field to be an integer (see [OQGRAPH Overview](../../../server-usage/storage-engines/oqgraph-storage-engine/oqgraph-overview.md#creating-a-table)). This deprecated feature was removed in [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115).
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115).

## Status Variables

#### `Oqgraph_boost_version`

* Description: [OQGRAPH](../../../server-usage/storage-engines/oqgraph-storage-engine/) boost version.
* Scope: Global, Session
* Data Type: `string`

#### `Oqgraph_compat_mode`

* Description: Whether or not legacy tables with integer latches are supported.
* Scope: Global, Session
* Data Type: `string`

#### `Oqgraph_verbose_debug`

* Description: Whether or not verbose debugging is enabled. If it is, performance may be adversely impacted
* Scope: Global, Session
* Data Type: `string`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
