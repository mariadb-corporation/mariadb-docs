# MariaDB 10.0.15 Fusion-io Release Notes

[Download](https://archive.mariadb.org/mariadb-10.0.15-FusionIO/) | [Release Notes](mariadb-10015-fusion-io-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10015-fusion-io-changelog.md) | [Fusion-io Introduction](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/fusion-io/fusion-io-introduction)

**Release date:** 12 Dec 2014

{% hint style="info" %}
**For an overview of** **MariaDB 10.0** **Fusion-io see the** [**Fusion-io Introduction**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/fusion-io/fusion-io-introduction) **page.**
{% endhint %}

Thanks, and enjoy MariaDB!

## Notable Changes

Since the [MariaDB 10.0.9 Fusion-io preview](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/) release, the following notable changes have been made.

* Merged with [MariaDB 10.0.15](mariadb-10015-release-notes.md) release
* Added support for 4K sector size if supported
  * Added status variables for 1K, 2K, 4K, 8K, 16K, and 32K trims
* Added innodb-compression-algorithm configuration variable to select default compression method
* Added support for
  * LZO compression
  * LZMA compression
  * bzip2 compression

## Other Changes

For a complete list of changes made in MariaDB 10.0.15 Fustion-io, with links to detailed information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10015-fusion-io-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formId="4316" %}
