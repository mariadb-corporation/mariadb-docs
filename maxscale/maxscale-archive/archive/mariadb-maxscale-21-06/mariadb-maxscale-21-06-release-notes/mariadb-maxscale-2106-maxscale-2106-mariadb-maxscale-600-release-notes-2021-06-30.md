# MariaDB MaxScale 6.0.0 Release Notes -- 2021-06-30

The versioning scheme has changed; the major number will be increased\
at the yearly major release, the minor number will be increased at\
intermediate scheduled releases and the patch number whenever a\
maintenance release is made. Each major release is separately maintained.

According to the old scheme, this MaxScale release would have been\
called 2.6 and the version number would have been 2.6.0.

Release 6.0.0 is a Beta release.

This document describes the changes in release 6, when compared to\
release 2.5.

For any problems you encounter, please consider submitting a bug\
report on [our Jira](https://jira.mariadb.org/projects/MXS).

### Changed Features

#### [MXS-3107](https://jira.mariadb.org/browse/MXS-3107) Columnstore monitor

The Columnstore monitor that in this release only supports Columnstore\
version 1.5, is now capable of adjusting itself automatically to any\
changes in the cluster. In the configuration it is only specified\
a node using which the monitor get in contact with the cluster, but\
after that the monitor autonomously figures out the cluster configuration\
and automatically adapts to any changes in the configuration. For more\
details, please consult the[monitor](../mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-columnstore-monitor.md)\
documentation.

#### [MXS-3499](https://jira.mariadb.org/browse/MXS-3499) `causal_reads` and Prepared Statements

The `causal_reads` feature now supports binary protocol prepared statements. For\
more information, refer to the[documentation](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-readwritesplit.md) for `causal_reads`.

#### [MXS-2838](https://jira.mariadb.org/browse/MXS-2838) Hintfilter and Prepared Statements

The hintfilter now supports routing hints in binary protocol prepared\
statements. For more information, refer to the hintfilter[documentation](../mariadb-maxscale-21-06-filters/mariadb-maxscale-2106-maxscale-2106-hintfilter.md).

#### [MXS-3219](https://jira.mariadb.org/browse/MXS-3219) Galera Server States

The servers monitored by a galeramon will now also display extra status\
information in the REST API output regarding the server state. MaxCtrl will\
automatically combine this for the output of `maxctrl list servers`.

#### [MXS-1245](https://jira.mariadb.org/browse/MXS-1245) Readwritesplit Statement Pipelining

Readwritesplit now supports "pipelined" execution of write statements. This\
significantly improves the performance of batch data loading with connectors\
that use it (e.g. the MariaDB JDBC and Node.JS connectors).

#### [MXS-3128](https://jira.mariadb.org/browse/MXS-3128) Runtime Alteration of TLS Parameters

The TLS parameters for listeners and servers can now be modified at\
runtime. Previously the parameters were only modifiable when the object was\
being created.

#### [MXS-3537](https://jira.mariadb.org/browse/MXS-3537) Default Value of `threads`

The default value of `threads` was changed from 1 to `auto`.

### Dropped Features

#### `ssl=required` and `ssl=disabled`

The `required` and `disabled` values for the `ssl` parameter have been\
removed. Replace them with `ssl=true` and `ssl=false`.

### Deprecated Features

#### Database Firewall filter

The filter is deprecated in MaxScale 6 and will be removed in MaxScale 22.08.

#### Multi-line Configuration Parameters

The ability to define a single configuration parameter[on multiple lines](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)\
is deprecated and will be removed in MaxScale 22.08.

### New Features

#### [MXS-2646](https://jira.mariadb.org/browse/MXS-2646) `nosqlprotocol` protocol module

This module implements a subset of the MongoDB® wire protocol and\
transparently converts MongoDB commands into the equivalent SQL\
statements that subsequently are executed on a MariaDB server. This\
allows client applications utilizing some MongoDB client library to\
use a MariaDB server as backend. As the conversion is performed in\
the protocol module, this functionality can be used together with\
all MaxScale routers and filters. Please see the `nosqlprotocol`[documentation](../mariadb-maxscale-21-06-protocols/mariadb-maxscale-2106-maxscale-2106-nosql-protocol-module.md) for more information.

#### [MXS-3482](https://jira.mariadb.org/browse/MXS-3482) Defaults can be specified for `maxctrl`

If the file `~/.maxctrl.cnf` exists, maxctrl will use any values in the section`[maxctrl]` as defaults for command line arguments. Please see the `maxctrl`[documentation](../mariadb-maxscale-21-06-reference/mariadb-maxscale-2106-maxscale-2106-maxctrl.md) for details.

#### [MXS-3411](https://jira.mariadb.org/browse/MXS-3411) TLS and Authentication for Kafka

The KafkaCDC as well as the new KafkaImporter both new support TLS and basic\
SASL authentication for Kafka.

For more information, refer to the [KafkaCDC](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-kafkacdc.md)\
and [KafkaImporter](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-kafkaimporter.md#kafka_ssl) documentation.

#### [MXS-3178](https://jira.mariadb.org/browse/MXS-3178) REST API Log Interface

The REST API is now able to deliver the MaxScale logs both as a normal HTTP\
resource as well as WebSocket stream. For more information, refer to the REST\
API [documentation](../mariadb-maxscale-21-06-rest-api/mariadb-maxscale-2106-maxscale-2106-maxscale-resource.md).

#### [MXS-3108](https://jira.mariadb.org/browse/MXS-3108) Session Alteration

The logging options for filters can be changed at runtime with `maxctrl alter filter` and the filters of a session can be modified with `maxctrl alter session-filters`. For more information, refer to the MaxCtrl[documentation](../mariadb-maxscale-21-06-reference/mariadb-maxscale-2106-maxscale-2106-maxctrl.md) as well as the REST API[documentation](../mariadb-maxscale-21-06-rest-api/mariadb-maxscale-2106-maxscale-2106-session-resource.md).

#### [MXS-2806](https://jira.mariadb.org/browse/MXS-2806) Stopping of Individual Listeners

Individual listeners can now be stopped with the `maxctrl stop listener`\
command. The new `--force` option added to the `stop` commands can be used to\
force all open connections to be closed when the associated object is stopped.

#### [MXS-2808](https://jira.mariadb.org/browse/MXS-2808) Configuration Synchronization

A new configuration synchronization feature has been added to MaxScale. This\
feature allows multiple MaxScale instances to share a configuration file that is\
synchronized via the database cluster monitored by MaxScale. For more\
information, refer to the `config_sync_cluster`[documentation](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md).

#### [MXS-2588](https://jira.mariadb.org/browse/MXS-2588) Data Ingestion From Kafka

The KafkaImporter module can be used to import JSON data from Kafka into\
MariaDB. For more information, refer to the KafkaImporter[documentation](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-kafkaimporter.md).

#### [MXS-2351](https://jira.mariadb.org/browse/MXS-2351) Prepared Statement Caching

Readwritesplit is now capable of caching prepared statements for individual\
sessions. For more information, refer to the[documentation](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-readwritesplit.md) for the`reuse_prepared_statements` parameter.

#### [MXS-1687](https://jira.mariadb.org/browse/MXS-1687) KafkaCDC and Avrorouter Failover

The KafkaCDC and Avrorouter modules now support automated failover of the\
replication stream when configured to replicate from servers or from a\
cluster. For more information, refer to the[KafkaCDC](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-kafkacdc.md) and[Avrorouter](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-avrorouter.md) documentation.

#### [MXS-2748](https://jira.mariadb.org/browse/MXS-2748) Session command history to RWS

Readwritesplit statistics now has two new entries:`avg_sescmd_history_length` and `max_sescmd_history_length`.\
These are helpful when tuning `max_sescmd_history` to avoid session command history\
to be too short, leading to potential inconsistencies, or to become too large,\
leading to wasted memory.

#### [MXS-3091](https://jira.mariadb.org/browse/MXS-3091) Restrict RCR reads to slaves

Readconnroute has a new option `master_accept_reads` similar to the one in Readwritesplit.\
When `master_accept_reads=false` RCR will not route reads to the current master.

#### [MXS-3257](https://jira.mariadb.org/browse/MXS-3257) SQL queries tool

A graphical user interface tool to write, run SQL queries and visualize the results.\
For more information, refer to the [MAXGUI](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-maxgui-guide.md) documentation.

#### [MXS-3154](https://jira.mariadb.org/browse/MXS-3154) Logs viewer

A graphical user interface for reading and filtering MaxScale's log.\
For more information, refer to the [MAXGUI](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-maxgui-guide.md) documentation.

#### MariaDB-Monitor

[MXS-2723](https://jira.mariadb.org/browse/MXS-2723)\
Can launch monitor script when slave server exceeds replication lag limit.\
See [documentation](../mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-mariadb-monitor.md)\
for more information.

[MXS-3268](https://jira.mariadb.org/browse/MXS-3268)\
Can disable _read\_only_ on master if it's set. See[documentation](../mariadb-maxscale-2106-maxscale-21-06-monitors/mariadb-maxscale-2106-maxscale-2106-mariadb-monitor.md)\
for more information.

#### [MXS-3475](https://jira.mariadb.org/browse/MXS-3475) PAM user mapping

PAM-Authenticator supports mapping incoming PAM users to MariaDB users. See[documentation](../mariadb-maxscale-21-06-authenticators/mariadb-maxscale-2106-maxscale-2106-pam-authenticator.md) for\
more information.

### Bug fixes

* [MXS-3592](https://jira.mariadb.org/browse/MXS-3592) MaxCtrl object creation doesn't convert values to JSON
* [MXS-3537](https://jira.mariadb.org/browse/MXS-3537) Default value of threads is not optimal
* [MXS-3515](https://jira.mariadb.org/browse/MXS-3515) COM\_STMT\_EXECUTE with ID -1 isn't handled correctly
* [MXS-3443](https://jira.mariadb.org/browse/MXS-3443) Query performance degradation in 2.5
* [MXS-3184](https://jira.mariadb.org/browse/MXS-3184) COM\_STMT\_EXECUTE with FOUND\_ROWS not routed to previous target
* [MXS-3028](https://jira.mariadb.org/browse/MXS-3028) Node wrongly in Maintenance, Running when the node is actually Down
* [MXS-2915](https://jira.mariadb.org/browse/MXS-2915) TLS version not used by mxq::MariaDB

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../mariadb-maxscale-21-06-about/mariadb-maxscale-2106-maxscale-2106-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the supported Linux distributions.

Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is `maxscale-X.Y.Z`. Further, the default branch is always the latest GA version\
of MaxScale.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
