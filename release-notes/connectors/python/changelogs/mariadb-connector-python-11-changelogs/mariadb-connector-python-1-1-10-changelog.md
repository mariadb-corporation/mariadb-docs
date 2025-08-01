# Connector/Python 1.1.10 Changelog

{% include "../../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="../../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-10-release-notes.md" class="button secondary">Release Notes</a> <a href="mariadb-connector-python-1-1-10-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 22 Feb 2024

For the highlights of this release, see the [release notes](../../mariadb-connector-python-1-1-release-notes/mariadb-connector-python-1-1-10-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-python/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #d672551](https://github.com/mariadb-corporation/mariadb-connector-python/commit/d672551)\
  2024-02-05 07:02:39 +0100
  * Fix for [CONPY-277](https://jira.mariadb.org/browse/CONPY-277): To avoid a syntax error when running under sql\_mode ANSI\_QUOTES parameter substitution will be done by using single quotes instead of double quotes.
* [Revision #b65fd44](https://github.com/mariadb-corporation/mariadb-connector-python/commit/b65fd44)\
  2024-02-02 16:08:32 +0100
  * Fix of previous commit: Skip test\_conpy278 instead of test\_conpy279.
* [Revision #7bc789a](https://github.com/mariadb-corporation/mariadb-connector-python/commit/7bc789a)\
  2024-02-02 08:58:17 +0100
  * Skip test\_conc279 when running with MaxScale (see [MXS-4961](https://jira.mariadb.org/browse/MXS-4961))
* [Revision #8620d49](https://github.com/mariadb-corporation/mariadb-connector-python/commit/8620d49)\
  2024-02-01 12:41:33 +0100
  * Fix for test\_conpy279
* [Revision #d9e33de](https://github.com/mariadb-corporation/mariadb-connector-python/commit/d9e33de)\
  2024-02-01 07:10:29 +0100
  * Fix for [CONPY-281](https://jira.mariadb.org/browse/CONPY-281): unittest test\_conpy175 fails with sql\_mode="NO\_BACKSLASH\_ESCAPES"
* [Revision #7c2134d](https://github.com/mariadb-corporation/mariadb-connector-python/commit/7c2134d)\
  2024-01-31 17:21:48 +0100
  * Fix for [CONPY-278](https://jira.mariadb.org/browse/CONPY-278): Update connection\_id in case of reconnect
* [Revision #2882798](https://github.com/mariadb-corporation/mariadb-connector-python/commit/2882798)\
  2024-01-31 15:15:49 +0100
  * [CONPY-280](https://jira.mariadb.org/browse/CONPY-280): Performance optimization for internal methods
* [Revision #f00bc26](https://github.com/mariadb-corporation/mariadb-connector-python/commit/f00bc26)\
  2024-01-30 15:55:34 +0100
  * Fix for [CONPY-279](https://jira.mariadb.org/browse/CONPY-279): change\_user method doesn't allow None values
* [Revision #7fe141e](https://github.com/mariadb-corporation/mariadb-connector-python/commit/7fe141e)\
  2023-12-20 19:07:13 +0100
  * Bump version

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
