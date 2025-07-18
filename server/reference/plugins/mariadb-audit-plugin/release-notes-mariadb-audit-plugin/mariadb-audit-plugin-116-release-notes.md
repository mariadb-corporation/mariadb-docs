# MariaDB Audit Plugin 1.1.6 Release Notes

**Release date:** 27 Mar 2014

This is a [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) _**(GA)**_ release. In general this means that there are no known serious bugs, except for those marked as feature requests, that no bugs were fixed since last release that caused a notable code changes, and that we believe the code is ready for general usage (based on bug inflow).

## Important Notices

* MariaDB will include the [Audit Plugin](../) by default from versions 5.5.37 and 10.0.10. At the time of writing these versions haven't yet been released.
* The MariaDB Audit Plugin works for MariaDB, MySQL and Percona Server.

## Download

If you want to download the MariaDB Audit Plugin separately from the MariaDB server, it is available at [SkySQL's site](https://www.skysql.com/downloads/mariadb-audit-plugin).

## Bug Fixes

* [MDEV-5681](https://jira.mariadb.org/browse/MDEV-5681) audit log will not rotate when the file size exceeds global variable setting. The variables [server\_audit\_file\_rotate\_now](../mariadb-audit-plugin-options-and-system-variables.md) and [server\_audit\_file\_rotations](../mariadb-audit-plugin-options-and-system-variables.md) are now handled and one doesn't need to stop/start logging to make them effective.
* [MDEV-5862](https://jira.mariadb.org/browse/MDEV-5862) server\_audit test fails in buildbot on Mac (labrador). The RTLD\_DEFAULT value on Labrador machine is not NULL, so the dlsym() commands in the server\_audit just fail to bind the necessary functions. Fixed by using RTLD\_DEFAULT explicitly.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
