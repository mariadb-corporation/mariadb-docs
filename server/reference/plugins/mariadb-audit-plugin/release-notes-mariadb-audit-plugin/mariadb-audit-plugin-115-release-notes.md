# MariaDB Audit Plugin 1.1.5 Release Notes

**Release date:** 25 Feb 2014

This is a [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) _**(GA)**_ release. In general this means that there are no known serious bugs, except for those marked as feature requests, that no bugs were fixed since last release that caused a notable code changes, and that we believe the code is ready for general usage (based on bug inflow).

## Important Notices

* MariaDB will include the [Audit Plugin](../) by default from versions 5.5.37 and 10.0.10. At the time of writing these versions haven't yet been released.
* The MariaDB Audit Plugin works for MariaDB, MySQL and Percona Server.

## Download

If you want to download the MariaDB Audit Plugin separately from the MariaDB server, it is available at [SkySQL's site](https://www.skysql.com/downloads/mariadb-audit-plugin).

## Main Improvements

* This version includes only one bug fix, but an important one without which crashes can occur with version 1.1.4 of the Audit Plugin. See below for more details and look at [mariadb-audit-plugin-114-release-notes](mariadb-audit-plugin-114-release-notes.md) for other recent changes in the Audit Plugin.

## Bug Fixes

* [MDEV-5722](https://jira.mariadb.org/browse/MDEV-5722) MariaDB audit plugin crashes when MariaDB Audit Plugin variables are set in my.cnf.

## MariaDB Audit Plugin 1.1.5 Changelog

The issue number links will take you to the corresponding issue in MariaDB project tracking.

* Revision 3914, 2014-02-24
  * [MDEV-5722](https://jira.mariadb.org/browse/MDEV-5722) MariaDB audit plugin crashes when variables set in .my.cnf. The 'thd' parameter is NULL when variables are changed in server\_audit\_init(). That we should take into account.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
