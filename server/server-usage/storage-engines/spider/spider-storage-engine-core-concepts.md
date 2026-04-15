---
description: >-
  Explains the fundamental concepts behind Spider, including its architecture as
  a proxy storage engine, sharding capabilities, and support for XA transactions
  across data nodes.
---

# Spider Storage Engine Core Concepts

A typical Spider deployment has a shared-nothing clustered architecture. The system works with any inexpensive hardware, and with a minimum of specific requirements for hardware or software. It consists of a set of computers, with one or more MariaDB processes known as nodes.

The nodes that store the data are designed as `Backend Nodes`, and can be any MariaDB, MySQL, Oracle server instances using any storage engine available inside the backend.

The `Spider Proxy Nodes` are instances running at least MariaDB 10. `Spider Proxy Nodes` are used to declare per table attachment to the backend nodes. In addition `Spider Proxy Nodes` can be setup to enable the tables to be split and mirrored to multiple `Backend Nodes`.

### Spider Common Usage

![Spider3](../../../.gitbook/assets/Spider3.png) ![Spider4](../../../.gitbook/assets/Spider4.png)

In the default high availability setup Spider Nodes produce SQL errors when a backend server is not responding. Per table monitoring can be setup to enable availability in case of unresponsive backends `monotoring_bg_kind=1` or `monotoring_bg_kind=2`. The Monitoring Spider Nodes are inter-connected with usage of the system table `mysql.link_mon_servers` to manage network partitioning. Better known as split brain, an even number of `Spider Monitor Nodes` should be setup to allow a consensus based on the majority. Rather a single separated shared `Monitoring Node` instance or a minimum set of 3 `Spider Nodes`. More information can be found [here](https://fr.slideshare.net/Kentoku/spider-ha-20100922dtt7).

**MariaDB starting with** [**10.7.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.5)

Spider's high availability feature has been deprecated (MDEV-28479), and are deleted. Please use other high availability solutions like [replication](../myrocks/myrocks-and-replication.md) or [galera-cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera-cluster/README.md).

### Spider Storage Engine Federation

Spider is a pluggable Storage Engine, acting as a proxy between the optimizer and the remote backends. When the optimizer requests multiple calls to the storage engine, Spider enforces consistency using the 2 phase commit protocol to the backends and by creating transactions on the backends to preserve atomic operations for a single SQL execution.\
Preserving atomic operation during execution is used at multiple levels in the architecture. For the regular optimizer plan, it refers to `multiple split reads` and for concurrent partition scans, it will refer to `semi transactions`.

Costly queries can be more efficient when it is possible to fully push down part of the execution plan on each backend and reduce the result afterwards. Spider enables such execution with some direct execution shortcuts.

![Spider1](../../../.gitbook/assets/Spider1.png)

### Spider Threading Model

Spider uses the per partitions and per table model to concurrently access the remote backend nodes. For memory workload that property can be used to define multiple partitions on a single remote backend node to better adapt the concurrency to available CPUs in the hardware.

![Spider2](../../../.gitbook/assets/Spider2.png)

Spider maintains an internal dictionary of Table and Index statistics based on separated threads. The statistics are pulled per default on a time line basis and refer to `crd` for cardinality and `sts` for table status.

### Spider Memory Model

Spider stores resultsets into memory, but [spider\_quick\_mode](spider-system-variables.md)=3 stores resultsets into internal temporary tables if the resultsets are larger than quick\_table\_size.

### Specifying Connection Information for Spider Tables

Spider tables connect to remote servers by reading connection information from one or more sources. MariaDB supports several methods for defining this information, each introduced at different versions. When more than one method is present, a defined precedence order determines which takes effect.

Connection information for Spider tables can be provided at different levels:

* At the server level (using `CREATE SERVER`)
* Table-level (using `CONNECTION` or `COMMENT`)&#x20;
* Engine-defined options (such as `REMOTE_SERVER`, `REMOTE_DATABASE`, and `REMOTE_TABLE`)
* Partition-level overrides table-level parameters

Spider has a predefined precedence order when using multiple methods.

#### Community Server (CS) vs Enterprise Server (ES)

**Applies to both CS and ES**

The following behavior applies to both CS and ES:

* All connection specification methods (`CREATE SERVER`, `COMMENT`, `CONNECTION`, and engine-defined parameters).
* Precedence rules (`COMMENT` > `CONNECTION` > `SERVER OPTIONS`; partition-level overrides table-level; engine-defined options override `COMMENT`/`CONNECTION`)
* Version-based behavior, such as the deprecation of `COMMENT`/`CONNECTION` in 11.4.1 and the introduction of `REMOTE_SERVER`, `REMOTE_DATABASE`, and `REMOTE_TABLE` in 10.8.1
* Deprecation of the `CONNECTION` and `COMMENT` clauses

**ES Additional Behavior (ODBC)**

An ODBC connection string is used by Spider (an ODBC variation) in Enterprise Server to create connections.&#x20;

The source of the ODBC connection string could be:

* `COMMENT` clause
* `CONNECTION` clause
* `CREATE...OPTIONS(...)`

These values are combined and converted into a format that is compatible with ODBC.

#### Connection Methods

**CREATE SERVER with COMMENT or CONNECTION**

In earlier versions, connection information is specified by creating a named server object, then referencing it in the Spider table definition using `COMMENT=` or `CONNECTION=`.

```sql
CREATE SERVER s
  FOREIGN DATA WRAPPER mysql
  OPTIONS (HOST 'remote_host', PORT 3306, DATABASE 'db_name',
           USER 'user', PASSWORD 'secret');

CREATE TABLE t (id INT) ENGINE=SPIDER COMMENT='srv "s"';
```

The same server can also be referenced at the partition level.

```sql
CREATE TABLE t (id INT) ENGINE=SPIDER
  CONNECTION='host "remote_host", port "3306", database "db_name"';
```

**Engine-defined options: `REMOTE_SERVER`, `REMOTE_DATABASE`, `REMOTE_TABLE` (Since 10.8.1)**

Since [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) ([MDEV-27106](https://jira.mariadb.org/browse/MDEV-27106)), engine-defined table options can be used to directly specify connection details:

```sql
CREATE TABLE t (id INT) ENGINE=SPIDER
  REMOTE_SERVER='s'
  REMOTE_DATABASE='db_name'
  REMOTE_TABLE='remote_t';
```

These engine-defined options override `COMMENT=` when both are present. These options are more structured and are the recommended method for new configurations.

**Extended Engine-defined options (Since 11.3.1)**

Since [MariaDB 11.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/11.3.1) ([MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856)), more engine-defined options are available. `COMMENT=` and `CONNECTION=` are ignored if there are any engine-defined options and warnings may be generated. Set `spider_suppress_comment_ignored_warning = 1` to suppress the warning that is generated when they are ignored.

**COMMENT and CONNECTION Deprecated (Since 11.4.1)**

Since [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.1) ([MDEV-28861](https://jira.mariadb.org/browse/MDEV-28861)), the Spider connection information specified by `COMMENT=` and `CONNECTION=` has been deprecated. Instead, use the engine-defined parameters.

**ODBC Connection String via CONNECTION (Since 11.4.3-1 ES)**

In the following instances, `CONNECTION=` is used directly as the ODBC connection string since [MariaDB Enterprise Server 11.4.3-1 ](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.4/11.4.3-1)([MENT-2070](https://jira.mariadb.org/browse/MENT-2070)):

* `COMMENT=` / `CONNECTION=` are explicitly ignored (i.e., engine-defined options are present, per [MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856))
* The value of `CONNECTION=` follows the ODBC connection string format (`param1=val1;param2=val2;...`)

In previous ES versions, the chosen `COMMENT=`, `CONNECTION=`, and `OPTIONS` fields were used to create the ODBC connection string. See [MENT-2076](https://jira.mariadb.org/browse/MENT-2076) for a complete list of fields used.

**CREATE SERVER with FOREIGN DATA WRAPPER ODBC**

The above settings are automatically converted into an ODBC connection string when using `CREATE SERVER` with `FOREIGN DATA WRAPPER ODBC` ([MENT-796](https://jira.mariadb.org/browse/MENT-796)). The above-described precedence order is maintained.

```sql
CREATE SERVER s
  FOREIGN DATA WRAPPER odbc
  OPTIONS (DSN 'MyDSN', UID 'user', PWD 'secret');
```

### Precedence Order

When multiple methods are provided simultaneously, the following order of precedence applies (from highest to lowest):

| Level                   | Priority | Description                                     |
| ----------------------- | -------- | ----------------------------------------------- |
| Partition-level options | Highest  | Overrides all table-level settings              |
| Engine-defined options  | High     | Overrides `COMMENT`, `CONNECTION`, and `SERVER` |
| `COMMENT`               | Medium   | Overrides `CONNECTION` and `SERVER`             |
| `CONNECTION`            | Low      | Overrides `SERVER`                              |
| `CREATE SERVER` options | Lowest   | Base configuration                              |

**Note**: More specific levels overrides less specific levels (e.g. partition-level parameters overrides table-level parameters), regardless of the method used.

### Version-Specific Behavior

| MariaDB Version | Behavior                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| < 10.8.1        | Only legacy methods (`CREATE SERVER`, `COMMENT`, `CONNECTION`) available      |
| 10.8.1+         | Engine-defined options (`REMOTE_*`) introduced and take precedence            |
| 11.3.1+         | If engine-defined options are present, `COMMENT` and `CONNECTION` are ignored |
| 11.4.1+         | `COMMENT` and `CONNECTION` are deprecated                                     |

### Supported FOREIGN DATA WRAPPER Values

`CREATE SERVER ... FOREIGN DATA WRAPPER` supports the following wrapper types:

| Wrapper Value | Description                                         | Availability |
| ------------- | --------------------------------------------------- | ------------ |
| `mysql`       | Establishes a connection to a remote `mysql` server | CS + ES      |
| `mariadb`     | Connects to a remote MariaDB server                 | CS + ES      |
| `odbc`        | Connects through an ODBC data source                | ES only      |

**Note**: The `odbc` wrapper value is only available in MariaDB Enterprise Server (ES). It is not supported in Community Server (CS).

**Default Behavior When Connection Information is not Specified**

If connection information is not explicitly specified using engine-defined options, Spider can depend on the configuration provided by other methods, such as `COMMENT`, `CONNECTION`, or `CREATE SERVER` statements.

The MariaDB version and configuration method determine the exact resolution behavior. The default behavior when no connection information is provided is currently being reviewed. To ensure predictable behavior, it is advised to explicitly specify connection details using engine-defined options (such as `REMOTE_SERVER`, `REMOTE_DATABASE`, and `REMOTE_TABLE`).

### See Also

* [Spider Table Parameters](spider-table-parameters.md)
* [Spider System Variables](spider-system-variables.md)
* [CREATE SERVER Statement](../../../reference/sql-statements/data-definition/create/create-server.md)
* [Spider Storage Engine](../../../architecture/topologies/spider-storage-engine.md)&#x20;

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
