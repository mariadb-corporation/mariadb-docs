# Release Model

## Current Release Model (from [MariaDB 11.3](../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md))

* [MariaDB Community Server releases](../) happen four times a year.
* There is a new innovation release with new features every time. It is a Release Candidate (RC) release.
* Additionally, all maintained release series get a new patch version maintenance release, a release that was RC last time, becomes Generally Available (GA).
* There are no patch version releases of an innovation release after GA (except for emergency releases), instead users are supposed to upgrade to the next minor innovation release. In other words, innovation releases are rolling releases, one upgrades 11.3.2→11.4.2→11.5.2→11.6.2→11.7.2
* Approximately every fourth innovation release is a long-term support (LTS) release, [maintained for three years](https://mariadb.org/about/#maintenance-policy) after the GA release, with additional Enterprise and Extended support available.
* Between two innovation releases there is a preview, it is feature-complete, but has alpha maturity, its purpose is to showcase new upcoming features. Every feature that will be in a release must have been in a preview at some point
* The opposite is not true, the feature from a preview will not necessarily be in the upcoming RC innovation release — this depends on whether the feature itself can be considered RC. If it isn't stable enough, it'll stay on internal testing and bug fixing until it is ready.

The release schedule looks about the same every year:

* Every third month there's a new minor innovation release, and a new patch version for the previous innovation release to bring it to GA, and also a patch version for currently maintained LTS releases:
  * early February, early May, early August, early November
* Previews happen between innovation releases:
  * mid-March, mid-June, mid-September, mid-December
* New major release every year
  * GA is early February (so, RC in November, preview in mid-September)

References:

* [https://mariadb.org/challenges-visions/](https://mariadb.org/challenges-visions/)
* [https://mariadb.org/preview-releases/](https://mariadb.org/preview-releases/)
* [https://mariadb.org/new-innovation-release-model/](https://mariadb.org/new-innovation-release-model/)

## Historical Release Models

### From [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md) to [MariaDB 11.2](../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

Almost the same as above, except that

* An innovation release is maintained for one year after its first GA release (see, for example, [timeline of 10.10 releases](../old-releases/release-notes-mariadb-10-10-series/)), they are not rolling, but on short-term support.
* Approximately every eighth innovation release (+-1, aligned around Debian release schedules) is a long-term support (LTS) release, maintained for five years after its first GA release.
* An LTS release concludes a major release series, the next innovation release will have a new major version number

### From [MariaDB 10.2](../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) to [MariaDB 10.6](../mariadb-10-6-series/what-is-mariadb-106.md)

* There is a new release series every year
* It's maintained for five years after the first GA release
* A release is going through conventional alpha, beta, RC maturity phases until reaching GA
* The first GA is planned to happen in May
  * it didn't quite work, [10.2](../../enterprise-server/old-releases/10-2/) and [10.3](../../enterprise-server/old-releases/10-3/) were in May, [10.4](../../enterprise-server/old-releases/10-4/) and [10.5](../../enterprise-server/old-releases/10-5/) — in June, [10.6](../../enterprise-server/10.6/) — in July.

### From [MariaDB 10.0](../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) to [MariaDB 10.1](../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

* It is a feature based model
* A new release series is planned to have a specific set of features
* It is released when they are ready
* Conventional alpha/beta/RC/GA maturity phases.
* No fixed or predictable schedule
  * 10.0 took 2.75 years (first commit was in August 2011, GA in May 2014)
  * 10.1 took 1.83 years (first commit was in December 2013, GA in October 2015)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
