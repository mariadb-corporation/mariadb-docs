# About MariaDB MaxScale

## About MariaDB MaxScale

**MariaDB MaxScale** is a database proxy that forwards database statements to
one or more database servers.

The forwarding is performed using rules based on the semantic understanding of
the database statements and on the roles of the servers within the backend
cluster of databases.

MariaDB MaxScale is designed to provide, transparently to applications, load
balancing and high availability functionality. MariaDB MaxScale has a scalable
and flexible architecture, with plugin components to support different protocols
and routing approaches.

MariaDB MaxScale makes extensive use of the asynchronous I/O capabilities of the
Linux operating system, combined with a fixed number of worker threads. _epoll_
is used to provide the event driven framework for the input and output via
sockets.

Many of the services provided by MariaDB MaxScale are implemented as external
shared object modules loaded at runtime. These modules support a fixed
interface, communicating the entry points via a structure consisting of a set of
function pointers. This structure is called the "module object". Additional
modules can be created to work with MariaDB MaxScale.

Commonly used module types are _protocol_, _router_ and _filter_. Protocol
modules implement the communication between clients and MariaDB MaxScale, and
between MariaDB MaxScale and backend servers. Routers inspect the queries from
clients and decide the target backend. The decisions are usually based on
routing rules and backend server status. Filters work on data as it passes
through MariaDB MaxScale. Filter are often used for logging queries or modifying
server responses.

A Google Group exists for MariaDB MaxScale. The Group is used to discuss ideas,
issues and communicate with the MariaDB MaxScale community. Send email to [maxscale@googlegroups.com](mailto:maxscale@googlegroups.com) or use the [forum](https://groups.google.com/forum/#!forum/maxscale) interface.

Bugs can be reported in the MariaDB Jira [jira.mariadb.org](https://jira.mariadb.org)

### Installing MariaDB MaxScale

Information about installing MariaDB MaxScale, either from a repository or by
building from source code, is included in the [MariaDB MaxScale Installation
Guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-installation-guide.md).

The same guide also provides basic information on running MariaDB MaxScale. More
detailed information about configuring MariaDB MaxScale can be found in the [Configuration Guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
