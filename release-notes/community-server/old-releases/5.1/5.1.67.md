# MariaDB 5.1.67 Release Notes

[Download](https://downloads.mariadb.org/mariadb/5.1.67) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5167-changelog.md) |[Overview of 5.1](changes-improvements-in-mariadb-5-1.md)

**Release date:** 30 Jan 2013

This is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In general this\
means that there are no known serious bugs, except for those marked as feature\
requests, that no bugs were fixed since last release that caused a notable code\
changes, and that we believe the code is ready for general usage (based on bug\
inflow).

**For a description of** [**MariaDB 5.1**](changes-improvements-in-mariadb-5-1.md) **see the**[**What is MariaDB 5.1**](changes-improvements-in-mariadb-5-1.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the [MariaDB 5.1.67 Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5167-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

This release is primarily a bug-fix release.

## Important Security Fixes

This release includes fixes for the following security vulnerabilities:

* A buffer overflow that can cause a server crash or arbitrary code execution (a variant of [CVE-2012-5611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5611))
* DoS - server lockup ([MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029))
* DoS - server crash ([MDEV-729](https://jira.mariadb.org/browse/MDEV-729))

Additionally, it includes all security fixes from MySQL 5.1.67, such as fix for a buffer overflow with stored routines (a variant of [CVE-2012-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5612)) and fixes for the following vulnerabilities:

* [CVE-2013-1531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1531)
* [CVE-2013-0384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0384)
* [CVE-2013-0389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0389)
* [CVE-2013-0385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0385)
* [CVE-2013-0375](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0375)
* [CVE-2012-1702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1702)
* [CVE-2013-0383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0383)
* [CVE-2012-0572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0572)
* [CVE-2012-0574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0574)
* [CVE-2012-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1705)

## Includes MySQL 5.1.67

This release includes MySQL 5.1.67. See [Changes in MySQL 5.1.67](https://dev.mysql.com/doc/relnotes/mysql/5.1/en/news-5-1-67.html)\
for what changed in MySQL.

## Discontinued builds

The MariaDB project tries to support as many different Operating Systems and\
Linux Distributions as we can. However, when a distribution or OS stops\
receiving security and other updates it becomes difficult to freely provide\
packages for that platform. In such cases, our policy is to deprecate that\
platform and stop providing binary packages for it.

As of 1 Feb 2013, we will stop building packages for the following:

* Fedora 16 "Verne"
* Debian 5 "Lenny"
* Ubuntu 10.10 "Maverick"
* Ubuntu 11.04 "Natty"

If your chosen Linux Distribution or Operating System is deprecated, packages\
or support are not completely unavailable. Companies such as [MariaDB Cloud](https://skysql.com) and [Monty Program](https://montyprogram.com)\
(and others) provide support for all versions of MariaDB back to even very old\
MySQL versions. This includes packaged binaries. Contact them for more details.

More information on our deprecation policy can be found at:

## Archived Releases

From the beginning of the MariaDB project in 2009 we've kept all of our old\
releases online via our network of mirrors. Doing this is great for those few\
who are interested in old releases, but the disk space required to host all of\
our old releases is over 130 Gigabytes at present and grows by several\
gigabytes with each new release. This is too much for some of our mirrors to\
handle. So, starting with this release our primary mirror will only host the\
most recent three or four releases in each series (5.5, 10.0, and so on).\
Mirrors are, of course, free to keep archiving every release, but the primary\
mirror that they pull from will not.

Old releases do have value, so for those that are interested in old releases,\
we are setting up a simple, no frills, archive server which will host them.\
Once the server is up and running, links to archived releases on [downloads.mariadb.org](https://downloads.mariadb.org) will point at the archive server. During the\
transition period, links to some old releases may disappear for a short time,\
but don't worry, they haven't been deleted, they're just being moved!

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
