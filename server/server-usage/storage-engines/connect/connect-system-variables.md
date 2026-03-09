---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT System Variables

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

This page documents system variables related to the [CONNECT storage engine](./). See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `connect_class_path`

* Description: Java class path
* Command line: `--connect-class-path=value`
* Scope: Global
* Dynamic:
* Data Type: `string`
* Default Value:

#### `connect_cond_push`

* Description: Enable condition pushdown
* Command line: `--connect-cond-push={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `connect_conv_size`

* Description: The size of the [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) created when converting from a [TEXT](../../../reference/data-types/string-data-types/text.md) type. See [connect\_type\_conv](connect-system-variables.md#connect_type_conv).
* Command line: `--connect-conv-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * > \= [MariaDB 10.4.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.8): `1024`
  * <= [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.7): `8192`
* Range: `0` to `65500`

#### `connect_default_depth`

* Description: Default depth used by Json, XML and Mongo discovery.
* Command line: `--connect-default-depth=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:`5`
* Range: `-1` to `16`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.16)

#### `connect_default_prec`

* Description: Default precision used for doubles.
* Command line: `--connect-default-prec=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:`6`
* Range: `0` to `16`
* Introduced: [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18)

#### `connect_enable_mongo`

* Description: Enable the [Mongo table type](connect-table-types/connect-mongo-table-type.md).
* Command line: `--connect-enable-mongo={0|1}`
* Scope: Global, Session
* Dynamic:
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9)
* Removed: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

#### `connect_exact_info`

* Description: Whether the CONNECT engine should return an exact record number value to information queries. It is OFF by default because this information can take a very long time for large variable record length tables or for remote tables, especially if the remote server is not available. It can be set to ON when exact values are desired, for instance when querying the repartition of rows in a partition table.
* Command line: `--connect-exact-info={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `connect_force_bson`

* Description: Force using BSON for JSON tables. Starting with these releases, the internal way JSON was parsed and handled was changed. The main advantage of the new way is to reduce the memory required to parse JSON (from 6 to 10 times the size of the JSON source to now only 2 to 4 times). However, this is in Beta mode and JSON tables are still handled using the old mode. To use the new mode, tables should be created with TABLE\_TYPE=BSON, or by setting this session variable to 1 or ON. Then, all JSON tables are handled as BSON. This is temporary until the new way replaces the old way by default.
* Command line: `--connect-force-bson={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18)

#### `connect_indx_map`

* Description: Enable file mapping for index files. To accelerate the indexing process, CONNECT makes an index structure in memory from the index file. This can be done by reading the index file or using it as if it was in memory by “file mapping”. Set to 0 (file read, the default) or 1 (file mapping).
* Command line: `--connect-indx-map=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `connect_java_wrapper`

* Description: Java wrapper.
* Command line: `--connect-java-wrapper=val`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `wrappers/JdbcInterface`

#### `connect_json_all_path`

* Description: Discovery to generate json path for all columns if ON (the default) or do not when the path is the column name.
* Command line: `--connect-json-all-path={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.16)

#### `connect_json_grp_size`

* Description: Max number of rows for JSON aggregate functions.
* Command line: `--connect-json-grp-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50` (>= Connect 1.7.0003), `10` (<= Connect 1.7.0002)
* Range: `1` to `2147483647`

#### `connect_json_null`

* Description: Representation of JSON null values.
* Command line: `--connect-json-null=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `<null>`

#### `connect_jvm_path`

* Description: Path to JVM library.
* Command line: `--connect-jvm_path=value`
* Scope: Global
* Dynamic:
* Data Type: `string`
* Default Value:

#### `connect_type_conv`

* Description: Determines the handling of [TEXT](../../../reference/data-types/string-data-types/text.md) columns.
  * `NO`: The default until Connect 1.06.005, no conversion takes place, and a TYPE\_ERROR is returned, resulting in a “not supported” message.
  * `YES`: The default from Connect 1.06.006. The column is internally converted to a column declared as VARCHAR(n), `n` being the value of [connect\_conv\_size](connect-system-variables.md#connect_conv_size).
  * `FORCE` (>= Connect 1.06.006): Also convert ODBC blob columns to TYPE\_STRING.
  * `SKIP`: No conversion. When the column declaration is provided via Discovery (meaning the CONNECT table is created without a column description), this column is not generated. Also applies to ODBC tables.
* Command line: `--connect-type-conv=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Valid Values: `NO`, `YES`, `FORCE` or `SKIP`
* Default Value: `YES`

#### `connect_use_tempfile`

* Description:
  * `NO`: The first algorithm is always used. Because it can cause errors when updating variable record length tables, this value should be set only for testing.
  * `AUTO`: This is the default value. It leaves CONNECT to choose the algorithm to use. Currently it is equivalent to `NO`, except when updating variable record length tables ([DOS](connect-table-types/connect-table-types-data-files.md#dos-and-fix-table-types), [CSV](connect-table-types/connect-table-types-data-files.md#csv-and-fmt-table-types) or [FMT](connect-table-types/connect-table-types-data-files.md#fmt-type)) with file mapping forced to OFF.
  * `YES`: Using a temporary file is chosen with some exceptions. These are when file mapping is ON, for [VEC](connect-table-types/connect-table-types-data-files.md#vec-table-type-vector) tables and when deleting from [DBF](connect-table-types/connect-table-types-data-files.md#dbf-type) tables (soft delete). For variable record length tables, file mapping is forced to OFF.
  * `FORCE`: Like YES but forces file mapping to be OFF for all table types.
  * `TEST`: Reserved for CONNECT development.
* Command line: `--connect-use-tempfile=#`
* Scope: Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `AUTO`

#### `connect_work_size`

* Description: Size of the CONNECT work area used for memory allocation. Permits allocating a larger memory sub-allocation space when dealing with very large if sub-allocation fails. If the specified value is too big and memory allocation fails, the size of the work area remains but the variable value is not modified and should be reset.
* Command line: `--connect-work-size=#`
* Scope: Global, Session (Session-only from CONNECT 1.03.005)
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `67108864`
* Range: `4194304` upwards, depending on the physical memory size

#### `connect_xtrace`

* Description: Console trace value. Set to `0` (no trace), or to other values if a console tracing is desired. Note that to test this handler, MariaDB should be executed with the [--console](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) parameter because CONNECT prints some error and trace messages on the console. In some Linux versions, this is re-routed into the error log file. Console tracing can be set on the command line or later by names or values. Valid values (from Connect 1.06.006) include:
  * `0`: No trace
  * `YES` or `1`: Basic trace
  * `MORE` or `2`: More tracing
  * `INDEX` or `4`: Index construction
  * `MEMORY` or `8`: Allocating and freeing memory
  * `SUBALLOC` or `16`: Sub-allocating in work area
  * `QUERY` or `32`: Constructed query sent to external server
  * `STMT` or `64`: Currently executing statement
  * `HANDLER` or `128`: Creating and dropping CONNECT handlers
  * `BLOCK` or `256`: Creating and dropping CONNECT objects
  * `MONGO` or `512`: Mongo and REST (from [Connect 1.06.0010](./)) tracing :
  * `set global connect_xtrace=0; No trace`
  * `set global connect_xtrace='YES'; By name`
  * `set global connect_xtrace=1; By value`
  * `set global connect_xtrace='QUERY,STMT'; By name`
  * `set global connect_xtrace=96; By value`
  * `set global connect_xtrace=1023; Trace all`
* Command line: `--connect-xtrace=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `set`
* Default Value: `0`
* Valid Values: See description

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
