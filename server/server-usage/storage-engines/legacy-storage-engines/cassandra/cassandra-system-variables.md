# Cassandra System Variables

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

This page documents system variables related to the [Cassandra storage engine](./). See [Server System Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

#### `cassandra_default_thrift_host`

* Description: Host to connect to, if not specified on per-table basis.
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `cassandra_failure_retries`

* Description: Number of times to retry on timeout/unavailable failures.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3`
* Valid Values: `1` to `1073741824`

#### `cassandra_insert_batch_size`

* Description: INSERT batch size.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Valid Values: `1` to `1073741824`

#### `cassandra_multiget_batch_size`

* Description: Batched Key Access batch size.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Valid Values: `1` to `1073741824`

#### `cassandra_read_consistency`

* Description: Consistency to use for reading. See [Datastax's documentation](https://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html) for details.
* Scope: Global, Session
* Default Value: `ONE`
* Valid Values: `ONE`, `TWO`, `THREE`, `ANY`, `ALL`, `QUORUM`, `EACH_QUORUM`, `LOCAL_QUORUM`, \`\`

#### `cassandra_rnd_batch_size`

* Description: Full table scan batch size.
* Scope: Global, Session
* Default Value: `10000`
* Valid Values: `1` to `1073741824`

#### `cassandra_write_consistency`

* Description: Consistency to use for writing. See [Datastax's documentation](https://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html) for details.
* Scope: Global, Session
* Default Value: `ONE`
* Valid Values: `ONE`, `TWO`, `THREE`, `ANY`, `ALL`, `QUORUM`, `EACH_QUORUM`, `LOCAL_QUORUM`, \`\`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
