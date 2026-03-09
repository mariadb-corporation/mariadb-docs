# MariaDB 5.2.3 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.3) | [Release Notes](../../old-releases/5.2/5.2.3.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 10 Nov 2010

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.3.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

**Build Script Update** _(22 Nov 2010)_

* [Revision #88](https://bazaar.launchpad.net/~maria-captains/ourdelta/ourdelta-montyprogram-fixes/revision/88)
  * [Bug #674413](https://bugs.launchpad.net/bugs/674413): Misconfigured debian-sys-maint user, warnings from default my.cnf\
    Fix two problems reported in [Bug #674413](https://bugs.launchpad.net/bugs/674413):
    * The debian-sys-maint account was not created, due to new field auth\_string\
      added in [mysql.user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-user-table) in 5.2 with no default value and postinst script\
      not updated.
    * Default my.cnf in 5.1+ uses log\_slow\_admin\_statements without enabling\
      the slow log, causing warnings. Fix by commenting out this by default.
* [Revision #2883](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2883)
  * Removed version number from test case
* [Revision #2882](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2882) \[merge]
  * Automatic merge
  * [Revision #2881.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2881.1.3)
    * Updated state and version number
  * [Revision #2881.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2881.1.2) \[merge]
    * Automatic merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
  * [Revision #2881.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2881.1.1) \[merge]
    * Automatic merge with 5.1
* [Revision #2881](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2881)
  * fix LIKE in a vcol function, broken by a fix for mysql bug#54568.
  * don't set view\_prepare\_mode when opening a base table
  * (either in SHOW CREATE or in I\_S.TABLES)
* [Revision #2880](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2880) \[merge]
  * merge w/ 5.1
* [Revision #2879](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2879)
  * sane implementation of Key\_% status variables.
* [Revision #2878](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2878)
  * fixes for windows
* [Revision #2877](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2877) \[merge]
  * merge with 5.1
* [Revision #2876](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2876)
  * forgotten option handled
* [Revision #2875](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2875)
  * bugfix: engine defined table options were not showing up in INFORMATION\_SCHEMA.TABLES.CREATE\_OPTIONS
* [Revision #2874](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2874) \[merge]
  * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
* [Revision #2873](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2873) \[merge]
  * Automatic merge with 5.1
* [Revision #2872](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2872)
  * fixes for gcc 4.5
* [Revision #2871](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2871) \[merge]
  * Automatic merge
  * [Revision #2849.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2849.1.3)
    * mysqld: Move `--skip-new` to `--safe` and remove old usage of `--skip-new`
  * [Revision #2849.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2849.1.2)
    * Change some my\_bool in C++ classes and a few functions to bool to detect wrong usage of bool/my\_bool.
    * Fix some bugs where we stored values other than 0 or 1 in my\_bool
    * Fixed some compiler warnings
  * [Revision #2849.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2849.1.1)
    * Fix usage of mysqld option `--new`, `--old`, `--safe` and `--skip_new` to not disable things that are proven stable or enable things that are not usefull.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
