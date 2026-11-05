---
description: >-
  MariaDB Enterprise Server enables a predictable development and operations
  experience through an enterprise lifecycle — incorporating optimized builds,
  predictable release behavior, and vendor support
---

# Enterprise Server Lifecycle

## Enterprise Server Builds

MariaDB Enterprise Server incorporates enhancements that are not present in MariaDB Community Server, including

* Premium features meet enterprise scaling and operations requirements.
* Priority bug fixes are available first to enterprise customers.
* Increased the code stability through restricted release of new functionality.
* Risk reduction from untested or incompatible features through the inclusion of only features with level 3 support (engineering code-level support) from MariaDB Corporation.
* Optimized the configuration defaults.

For details on features added to enhance, harden, and secure MariaDB Enterprise Server, see the following pages:

* [What's New in MariaDB Enterprise Server 12.3](../12.3/whats-new.md)
* [What's New in MariaDB Enterprise Server 11.8](../11.8/whats-new.md)
* [What's New in MariaDB Enterprise Server 11.4](../11.4/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.6](../10.6/whats-new.md)

## Enterprise Server Releases <a href="#enterprise-server-releases" id="enterprise-server-releases"></a>

Releases of MariaDB Enterprise Server are predictable because,

* Major releases are delivered on a schedule.
* The minor releases are focused on small, incremental defect remediation.
* Critical fixes from newer release series are selectively backported.
* Enterprise-grade testing drives a low defect rate.
* Specific changes present in each release are communicated.
* A [Software Bill of Materials (SBOM)](sbom.md) is published for every release.

Additional information on the release cycle for MariaDB Enterprise Server can be found in [MariaDB Corporation Engineering Policy](https://mariadb.com/engineering-policies/).

### Upcoming Minor and Maintenance Releases <a href="#upcoming-minor-and-maintenance-releases" id="upcoming-minor-and-maintenance-releases"></a>

Planned releases of MariaDB Enterprise Server are [scheduled](enterprise-server-release-schedule.md).

### Obtaining MariaDB Enterprise Server <a href="#obtaining-mariadb-enterprise-server" id="obtaining-mariadb-enterprise-server"></a>

MariaDB Enterprise Server is available to MariaDB subscription customers:

* From the [Enterprise Server download page](https://mariadb.com/downloads/enterprise/enterprise-server/)
* From the [MariaDB Enterprise Repository](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage#mariadb-enterprise-server-repository)
* As [Enterprise Docker images](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)
* As part of the [MariaDB Enterprise Kubernetes Operator](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD/enterprise/mariadb-enterprise-operator)

MariaDB Enterprise Server is also available as a managed service in [MariaDB Cloud](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd), on the [Power and PowerPlus service tiers](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd/service-tiers).

If you are not yet a MariaDB subscription customer, [contact MariaDB Corporation](https://mariadb.com/contact) for more information.

### Enterprise Server Release Identifiers <a href="#enterprise-server-release-identifiers" id="enterprise-server-release-identifiers"></a>

Releases of MariaDB Enterprise Server are given an identifier such as 'MariaDB Enterprise Server 11.8.9-6,' whose components are,

* The product name (MariaDB Enterprise Server).
* Release series (11.8, spoken "eleven-eight").
* The point release of MariaDB Community Server used as the base of this Enterprise Server release (.9, spoken "eleven-eight-nine").
* The release postfix of MariaDB Enterprise Server starts with '-1' and is incremented for subsequent releases in that release series (-6, spoken "eleven-eight-nine-dash-six").
* On the Debian and Ubuntu platforms, the release postfix contains a period instead of a dash, such that release postfixes start with .1 and increment for subsequent releases in that release series (.6, spoken "eleven-eight-nine-dot-six").

{% hint style="info" %}
**Note:** The release postfix (for example, the `-4` in `11.8.6-4`) increases consecutively with each new Enterprise Server release in a series, but the Community Server point release it is based on does not. As a result:

* An Enterprise Server release can **skip** a Community Server point release. For example, `11.8.6-4` is followed by `11.8.8-5`, skipping `11.8.7`.
* Two consecutive Enterprise Server releases can be based on the **same** Community Server point release. For example, `11.8.6-3` is followed by `11.8.6-4`.

The release postfix — not the point release — is the reliable indicator of release order.
{% endhint %}

Additional information on the release numbering for MariaDB Enterprise Server can be found in [MariaDB Corporation Engineering Policy](https://mariadb.com/engineering-policies).

## Enterprise Server Support <a href="#enterprise-server-support" id="enterprise-server-support"></a>

MariaDB Enterprise Server is part of the [MariaDB Enterprise Platform](https://mariadb.com/products/platform/) subscription. MariaDB Corporation offers vendor support for MariaDB Enterprise Server, including,

* Customer support as detailed in the [Subscription Services Policy](https://mariadb.com/subscription-services-policies)
* [Professional services](https://mariadb.com/services), including migration services, remote DBA services, and consulting
* Customer communications, managed via the [MariaDB Customer Portal](https://customers.mariadb.com/)
* [Training](https://mariadb.com/services/training)
* [Documentation](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/1H8tuThi64HJmOJHG6nV/)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
