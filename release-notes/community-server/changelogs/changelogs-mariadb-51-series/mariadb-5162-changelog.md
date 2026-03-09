# MariaDB 5.1.62 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.1.62) |[Release Notes](../../old-releases/5.1/5.1.62.md) |**Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 6 Apr 2012

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.62.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3145](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3145) \[merge]\
  Thu 2012-04-05 10:49:38 +0200
  * mysql-5.1.62 merge
* [Revision #3144](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3144)\
  Wed 2012-04-04 15:41:50 +0200
  * [MDEV-212](https://jira.mariadb.org/browse/MDEV-212) sporadic main.connect failures in 5.3
  * don't cast implicitly an int to a char, when a boolean value is desired.
* [Revision #3143](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3143) \[merge]\
  Wed 2012-04-04 13:38:19 +0300
  * Merge in deleted fixes
  * [Revision #3142.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3142.1.2)\
    Wed 2012-04-04 13:20:06 +0300
    * Fixed test cases that changed as part of fixing bugs with record count and partitioning
  * [Revision #3142.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3142.1.1)\
    Wed 2012-04-04 00:14:07 +0300
    * Fixed [Bug #970528](https://bugs.launchpad.net/bugs/970528) "Server crashes in my\_strnncollsp\_simple on LEFT JOIN with CSV table, TEXT field"
    * The main problem was a bug in CSV where it provided wrong statistics (it claimed the table was empty when it wasn't)
    * I also fixed wrong freeing of blob's in the CSV handler. (Any call to handler::read\_first\_row() on a CSV table with blobs would fail)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
