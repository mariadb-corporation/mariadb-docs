# Google Season of Docs 2019

## Google Season of Docs 2019

MariaDB applied to participate in the first Google Season of Docs. Unfortunately, as a pilot project, Google were only able to accept a limited number of applications, and we were unsuccessful.

## Where to Start

Please join us on [Zulip](https://mariadb.zulipchat.com/) to mingle with the community. You can also subscribe to [maria-docs@lists.launchpad.net](https://launchpad.net/~maria-docs), the documentation mailing list.

[List of beginner friendly bugs](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC)

## List of Tasks

### Stored Procedures Documentation

The [Stored Procedures](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures) capabilities of MariaDB Server are critical to producing large-scale applications. The current documentation lacks sufficient examples, and the examples warrant testing. Getting Started content would make this easier to adopt. MariaDB's implementation is based on ISO SQL/PSM.

### Getting Started with Connector/C and Connector/J

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) and [MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) provide the ability to access a MariaDB Server from applications built in C/C++ and Java, respectively. The current documentation for these connectors lacks Getting Started guides.

### Spider Documentation

The [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) Storage Engine uses partitioning to provide data sharding through multiple servers. This task involves greatly expanding the existing documentation, including more detail about when to use Spider, basic usage, updating the [Spider Feature Matrix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-feature-matrix), detailed examples of the effects of the [server system variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) and [table system variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-table-parameters), as well as the [Spider functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-functions). You will also ensure changes in the most recent Spider releases are properly documented.

### Mroonga Documentation

[Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) is a full text search storage engine based on Groonga, which is an open-source CJK-ready fulltext search engine using column base. This project involves greatly expanding the existing MariaDB documentation on the use of this storage engine.\
A detailed tutorial and user guide, including examples of the various Mroonga [user-defined functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga/mroonga-user-defined-functions), [system variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga/mroonga-system-variables) and the effects of changing their settings, as well as the parser and [parser settings](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga/mroonga-overview).

### Translation

You will choose a major language and ensure that a substantial subsection of the documentation is translated into that language.

### Migration Documentation

You will choose a major relational DBMS, and, focusing on the most recent stable releases, document the process to migrate to MariaDB, including MariaDB equivalents to features in that system, and a detailed list of features that exist in one but not the other, as well as possible workarounds. For an example, see the documentation on [migrating from MySQL to MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql) (bearing that MariaDB is a MySQL fork, and is substantially more similar to MySQL than to other systems).

_Loaded from the_ [_MariaDB issue tracker_](https://jira.mariadb.org/issues/?jql=labels=gsdocs19)\
Loading Issues from \[Jira]\(https://jira.mariadb.org/issues/?jql=labels=gsdocs19 and project=mdev order by key)

#### %fields.summary%

%renderedFields.description%

| Details: | Mentor:                                        |
| -------- | ---------------------------------------------- |
| Details: | %key% |
| Mentor:  | %fields.assignee.displayName%                  |

<>

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
