# MariaDB 5.3.3 Release Notes

The most recent release in the [MariaDB 5.3 series](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) is:[**MariaDB 5.3.12**](mariadb-5312-release-notes.md)

[Download](https://downloads.askmonty.org/mariadb/5.3.3) |**Release Notes** |[Changelog](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) |[Overview of 5.3](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md)

**Release date:** 21 Dec 2011

[MariaDB 5.3.3](mariadb-533-release-notes.md) is a [Release Candidate](../../about/release-criteria.md) release. In general\
this means that there are no known serious bugs, except for those marked as\
feature requests and no bugs were fixed since last the release which caused any\
notable code changes. We believe the code is ready for general usage (based on\
bug inflow), but we want more testing before calling it stable.

[MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) radically improves performance for subqueries as well as for joins\
and single-table queries over large data sets.

**For a detailed description of** [**MariaDB 5.3**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) **see the** [**What is MariaDB 5.3**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) **page.**

Compared to [MariaDB 5.3.0](mariadb-530-release-notes.md), 5.3.1, and 5.3.2, [MariaDB 5.3.3](mariadb-533-release-notes.md) is a bug-fix release\
with a focus on stability, performance, and usability. It is the third beta\
release of the 5.3 series and fixes bugs found in the initial 5.3.0 and\
5.3.1 beta releases.

* New feature: [GIS precise operations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/gis-features-in-533) were added (Documentation is being worked on)
* Stability: All known critical bugs have been fixed.
* Performance:
  * More optimizer features have been thoroughly tested, and switched on by default:
    * [Subquery materialization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations#materialization-for-non-correlated-in-subqueries) is now ON by default (materialization=on)
    * [Semi-join optimizations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/semi-join-subquery-optimizations) is now ON by default (semijoin=on,firstmatch=on,loosescan=on)
    * [Derived table optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/derived-table-merge-optimization) is now ON by default (derived\_merge=on,derived\_with\_keys=on)
    * [Index Condition Pushdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) is now ON by default (index\_condition\_pushdown=on)
    * Nested loop join will use its [Block-based variant](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) more aggressively
      * Block-based join for OUTER JOINs is ON by default (outer\_join\_with\_cache=on)
      * Block-based join for semi-joins is ON by default (semijoin\_with\_cache=on)
      * Linked join buffers (more aggressive buffering of multi-way joins) is ON by default (@@join\_cache\_level==2)
  * DISTINCT and GROUP BY clauses are removed from subqueries when possible. This allows for more efficient query plans (backported from MySQL 5.6)
* Usability:
  * [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) output has been improved to be easier to understand
    * `select_type` column now shows `MATERIALIZED` for subqueries that are executed with Materialization (it used to show `SUBQUERY` before which made it hard to distinguish materialized subqueries from other kinds subqueries.
    * For [Duplicate Elimination](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/duplicateweedout-strategy) strategy, `Start temporary` is now shown at the first table from the subquery.
* Other:
  * Ubuntu 11.10 "Oneiric" [repositories](https://downloads.askmonty.org/mariadb/repositories/) are now available for [MariaDB 5.3.3](mariadb-533-release-notes.md).

For a list of every change made in [MariaDB 5.3.3](mariadb-533-release-notes.md), with links to detailed\
information on each push, see the [MariaDB 5.3.3 Changelog](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md). It is worth noting that [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md) is built on [MariaDB 5.2](../release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md),[MariaDB 5.1](../release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md), and MySQL 5.1.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
