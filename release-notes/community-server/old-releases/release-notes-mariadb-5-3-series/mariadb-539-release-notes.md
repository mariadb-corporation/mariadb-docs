# MariaDB 5.3.9 Release Notes

The most recent release in the [MariaDB 5.3 series](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) is:[**MariaDB 5.3.12**](mariadb-5312-release-notes.md)

[Download](https://downloads.mariadb.org/mariadb/5.3.9) |**Release Notes** |[Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-539-changelog.md) |[Overview of 5.3](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md)

**Release date:** 02 Oct 2012

[MariaDB 5.3.9](mariadb-539-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) _**(GA)**_ release. In\
general this means that there are no known serious bugs, except for those\
marked as feature requests, that no bugs were fixed since last release that\
caused notable code changes, and that we believe the code is ready for\
general usage (based on bug inflow).

**For a description of** [**MariaDB 5.3**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) **see the**[**What is MariaDB 5.3**](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/broken-reference/README.md) **page.**

For a list of changes made in [MariaDB 5.3.9](mariadb-539-release-notes.md), with links to detailed\
information on each push, see the [MariaDB 5.3.9 Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-539-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Includes [MariaDB 5.2](../release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and MySQL 5.1.65

This version of MariaDB includes the latest changes to [MariaDB 5.2](../release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md), and, by\
extension, [MariaDB 5.1](../release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md), including MySQL 5.1.65. See [Changes in MySQL 5.1.65](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-65.html)\
for what changed between this and previous MySQL versions.

## Bug fixes and other improvements

[MariaDB 5.3.9](mariadb-539-release-notes.md) includes a fix for a bug with EXT3 and EXT4 filesystems which could result in data loss after a crash. We've reported the bug to the upstream filesystem maintainers and they will be fixing it in the Linux kernel. This fix is a workaround to fix the issue now, rather than waiting for the kernel-level fix. See [MDEV-381](https://jira.mariadb.org/browse/MDEV-381) for more information.

This MariaDB release also includes several other bug fixes and improvements. It is\
recommended for all users of [MariaDB 5.3](changes-improvements-in-mariadb-5-3.md).

See the [MariaDB 5.3.9 Changelog](../../changelogs/changelogs-mariadb-53-series/mariadb-539-changelog.md) for a list of every\
change made in [MariaDB 5.3.9](mariadb-539-release-notes.md), with links to detailed information on each push.

## Alternative Linux binaries

This version of MariaDB includes alternative Linux binaries built on a\
different build machine. Binaries created on this box require at least\
GLIBC\_2.14. For continuity, we are still providing binaries built with the same\
toolchain (and on the same builder) as previous releases. The alternative\
binaries have a "(GLIBC\_2.14)" label to distinguish them from the others.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
