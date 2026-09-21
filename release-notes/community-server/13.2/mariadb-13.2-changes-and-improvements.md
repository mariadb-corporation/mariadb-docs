---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 13.2
---

# MariaDB 13.2 Changes & Improvements

{% include "../../.gitbook/includes/unreleased-13.2.md" %}

MariaDB 13.2 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 13.1](../13.1/mariadb-13.1-changes-and-improvements.md) with many entirely new features.

## New Features

 * ANY_VALUE function ([MDEV-10426](https://jira.mariadb.org/browse/MDEV-10426))
 * GROUPING() function ([MDEV-22269](https://jira.mariadb.org/browse/MDEV-22269))
 * Aggregate functions now support the SQL standard FILTER clause, letting you filter which rows are included in an aggregation without writing a CASE expression ([MDEV-24943](https://jira.mariadb.org/browse/MDEV-24943))
 * Atomic CREATE OR REPLACE TABLE ([MDEV-25292](https://jira.mariadb.org/browse/MDEV-25292))
 * I_S optimization: avoid temp table ([MDEV-31342](https://jira.mariadb.org/browse/MDEV-31342))
 * NEW and OLD in a trigger as row variables ([MDEV-34723](https://jira.mariadb.org/browse/MDEV-34723))
 * Mariadb-binlog to Convert InnoDB Binlog Format to Legacy Format ([MDEV-37605](https://jira.mariadb.org/browse/MDEV-37605))
 * Extend Binlog-in-Engine with Semi-sync Support ([MDEV-38190](https://jira.mariadb.org/browse/MDEV-38190))
 * BLOBs in MEMORY (HEAP) Engine ([MDEV-38975](https://jira.mariadb.org/browse/MDEV-38975))
 * Direct multi-table update/delete interface and FederatedX implementation ([MDEV-39226](https://jira.mariadb.org/browse/MDEV-39226))
 * Allow prepared statements in stored functions in assignment right hand ([MDEV-39518](https://jira.mariadb.org/browse/MDEV-39518))
 * Implement UPDATE ... RETURNING ... INTO ([MDEV-39563](https://jira.mariadb.org/browse/MDEV-39563))
 * Memory tables now support CHECK TABLE ([MDEV-40030](https://jira.mariadb.org/browse/MDEV-40030))
 * hide #mysql50# under old mode ([MDEV-40406](https://jira.mariadb.org/browse/MDEV-40406))
 * Pluggable aggregate functions ([MDEV-40672](https://jira.mariadb.org/browse/MDEV-40672))
 * Prefetch unseen MHNSW neighbour ([MDEV-40827](https://jira.mariadb.org/browse/MDEV-40827))
 * Update default datadir for debian to be /var/lib/mariadb ([MDEV-40964](https://jira.mariadb.org/browse/MDEV-40964))

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
