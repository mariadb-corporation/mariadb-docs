# Connector/J 1.3.0 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.0/)[Release Notes](../../1.3/mariadb-connector-j-130-release-notes.md)[Changelog](mariadb-connector-j-130-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md)

**Release date:** 16 Nov 2015

MariaDB Connector/J 1.3.0 is a [_**Stable (GA)**_](../../../../community-server/about/release-criteria.md) release.

For the highlights of this release, see the [release notes](../../1.3/mariadb-connector-j-130-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

Major change :

* [CONJ-94](https://jira.mariadb.org/browse/CONJ-94) : new Date/Time/Timstamps implementation that handle timezone and daylight correctly.
  * [Revision #b186cc5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b186cc5) 2015-09-17
  * [Revision #27d41bf](https://github.com/mariadb-corporation/mariadb-connector-j/commit/27d41bf) 2015-09-21
  * [Revision #2619ff5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2619ff5) 2015-09-29
* [CONJ-189](https://jira.mariadb.org/browse/CONJ-189) : implementation of loadbalancing without failover
  * [Revision #8e05ce6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8e05ce6) 2015-09-17
  * [Revision #c6150f6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c6150f6) 2015-09-21
* [CONJ-22](https://jira.mariadb.org/browse/CONJ-22) : Implementation of prepareStatement server side
  * [Revision #9c0389b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9c0389b) 2015-09-08
  * [Revision #c04e4e3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c04e4e3) 2015-09-10
  * [Revision #fb995b8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fb995b8) 2015-09-15
  * [Revision #0f78c03](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f78c03) 2015-09-15
  * [Revision #b300e40](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b300e40) 2015-09-15
  * [Revision #69eed3e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/69eed3e) 2015-09-16
  * [Revision #2bcf2d8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2bcf2d8) 2015-09-16
  * [Revision #df6bf2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/df6bf2f) 2015-09-16
  * [Revision #8f65a6a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8f65a6a) 2015-09-16
  * [Revision #bbefaa7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bbefaa7) 2015-09-16
  * [Revision #7abf691](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7abf691) 2015-09-16
  * [Revision #ce5cd77](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ce5cd77) 2015-09-17
  * [Revision #e8652c1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e8652c1) 2015-09-17
  * [Revision #9bfe1ca](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9bfe1ca) 2015-09-17
  * [Revision #5a1772f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5a1772f) 2015-09-18
  * [Revision #cc7b8e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cc7b8e2) 2015-09-18
  * [Revision #8960d97](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8960d97) 2015-09-20
  * [Revision #25cfbec](https://github.com/mariadb-corporation/mariadb-connector-j/commit/25cfbec) 2015-09-21

Minor change :

* [CONJ-177](https://jira.mariadb.org/browse/CONJ-177) : new option (assureReadonly) to validate that slave is read-only - [Revision #02449e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/02449e8) 2015-09-21
* [CONJ-200](https://jira.mariadb.org/browse/CONJ-200) : fixing insert ... select error in prepare statement
* [CONJ-192](https://jira.mariadb.org/browse/CONJ-192) : Correct driver metadata version - [Revision #40a1c83](https://github.com/mariadb-corporation/mariadb-connector-j/commit/40a1c83) 2015-09-04
* [CONJ-185](https://jira.mariadb.org/browse/CONJ-185) : Handle setObject java.lang.Character type - [Revision #9f3eb20](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9f3eb20) 2015-09-15
* [CONJ-182](https://jira.mariadb.org/browse/CONJ-182) : Correction of "Self assignment of field correction - [Revision #c317981](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c317981) 2015-09-15

MISC :

* add developpement snapshot repository information - [Revision #3a2a4d2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3a2a4d2) 2015-09-04
* deletion of slf4j requirement - [Revision #7425c5d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7425c5d) 2015-09-15
* code formatting unification - [Revision #bb04ba9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bb04ba9) 2015-09-15
* javadoc formatting unification - [Revision #3d8dfb3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3d8dfb3) 2015-09-15
* correct LOAD DATA LOCAL INFILE handling - [Revision #d5fbf83](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d5fbf83) + [Revision #b01686a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b01686a) 2015-09-23

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
