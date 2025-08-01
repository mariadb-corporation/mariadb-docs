# Connector/J 1.5.1 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.1/)[Release Notes](mariadb-connector-j-151-release-notes.md)[Changelog](../changelogs/1.5/mariadb-connector-j-151-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 16 Aug 2016

MariaDB Connector/J 1.5.1 is a [_**Release candidate**_](../../../community-server/about/release-criteria.md) _**(RC)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

### Evolution

**Aurora host auto-discovery**\
([CONJ-325](https://jira.mariadb.org/browse/CONJ-325))

Aurora now auto discovers nodes from the cluster endpoint.

**Aurora endpoints**

Every aurora instance has a specific endpoint, i.e. a URL that identifies the\
host. These endpoints look like `xxx.yyy.zzz.rds.amazonaws.com`.

There is another endpoint named "cluster endpoint" (format`xxx.cluster-yyy.zzz.rds.amazonaws.com`) which is assigned to the current\
master instance and will change when a new master is promoted.

In previous versions, cluster endpoint use was discouraged, since, when a\
failover occurs, this cluster endpoint can point for a limited time to a host\
that is no longer the current master. Old recommendation was to list all\
specific end-points, like:

```java
jdbc:mysql:aurora://a.yyy.zzz.rds.amazonaws.com.com,b.yyy.zzz.rds.amazonaws.com.com/db
```

This kind of URL string will still work, but now the recommended URL string has to use only the cluster endpoint:

```java
jdbc:mysql:aurora://xxx.cluster-yyy.zzz.rds.amazonaws.com/db
```

The driver will automatically discover master and slaves of this cluster from\
the current cluster endpoint during connection time. This permits adding new\
replicas to the cluster instance that will be discovered without changing the\
driver configuration.

This discovery appends at connection time, so if you are using a pool\
framework, check if this framework has a property that controls the maximum\
lifetime of a connection in the pool, and set a value to avoid infinite\
lifetime. When this lifetime is reached, pool will discarded for the current\
connection, and will create a new one (if needed). New connections will use the\
new replicas.

(If connections are never discarded, new replicas will begin to be used only\
when a failover occurs.)

### Bugfix

* [CONJ-329](https://jira.mariadb.org/browse/CONJ-329) and [CONJ-330](https://jira.mariadb.org/browse/CONJ-330) : rewriteBatchedStatements execute single query exceptions correction.

## Changelog

For a list of all changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/1.5/mariadb-connector-j-151-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
