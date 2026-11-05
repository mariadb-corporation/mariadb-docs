---
description: >-
  The DISA Security Technical Implementation Guide (STIG) for MariaDB
  Enterprise Server: which versions it covers, where to download it, and how to
  use it to harden a deployment.
---

# MariaDB Enterprise Server STIG

A Security Technical Implementation Guide (STIG) is a set of configuration requirements that the [Defense Information Systems Agency](https://www.disa.mil/) (DISA) publishes for a product. US Department of Defense (DoD) systems must be configured according to the STIGs for their products, and many other US government agencies and contractors use them as a hardening baseline.

The **MariaDB Enterprise Server STIG** was developed by MariaDB and DISA. Version 1, Release 1 is dated 30 September 2026, and DISA released it for immediate use.

## Supported Versions

The STIG applies to MariaDB Enterprise Server 11.4, 11.8, and 12.x, installed on Red Hat Enterprise Linux (RHEL) or a compatible enterprise Linux distribution.

{% hint style="info" %}
The STIG covers MariaDB Enterprise Server only. One of its requirements is that MariaDB runs in a version supported by the vendor, and it names MariaDB Enterprise as the only supported product. MariaDB Community Server can't be used in a STIG-compliant deployment.
{% endhint %}

An earlier STIG, for MariaDB Enterprise 10.x, was approved in 2022.

## Downloading the STIG

DISA publishes STIGs in its [STIG library](https://public.cyber.mil/stigs/downloads/). You don't need a DoD Common Access Card (CAC) to download the MariaDB Enterprise Server STIG.

Download the STIG directly:

* [U\_MariaDB\_Enterprise\_Server\_V1R1\_STIG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MariaDB_Enterprise_Server_V1R1_STIG.zip)

The ZIP file contains:

* The requirements in XCCDF format (`U_MariaDB_Enterprise_Server_STIG_V1R1_Manual-xccdf.xml`). Each requirement comes with a check procedure and a fix procedure.
* An overview, a release memo, and a revision history, as PDF files.

## Using the STIG

The STIG has 68 requirements. 12 of them have high severity (Category I) and 56 have medium severity (Category II). They cover these areas:

* Authentication and account management, including integration with an organization-level authentication mechanism and password policies.
* Authorization and access to the software installation and to PKI private keys.
* Auditing, including what audit records must contain.
* Encryption of data in transit and at rest, using FIPS 140-3 validated cryptographic modules.

To read the requirements and record the results of an assessment, open the XCCDF file in [DISA STIG Viewer](https://public.cyber.mil/stigs/srg-stig-tools/), or import it into a compliance scanning tool that supports XCCDF.

Use the MariaDB Enterprise Server STIG together with the STIGs for the rest of the system, such as the RHEL STIG and the applicable network STIGs.

These pages help with the configuration that the STIG requires:

* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
* [Data-in-Transit Encryption](../encryption/data-in-transit-encryption/README.md)
* [Data-at-Rest Encryption](../encryption/data-at-rest-encryption/README.md)
* [MariaDB on SELinux](selinux.md)

## Getting Help

For help with a STIG-compliant deployment, [contact MariaDB](https://mariadb.com/contact/).

To comment on the STIG itself or propose changes, email the DISA STIG Support Desk at `disa.stig_spt@mail.mil`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
