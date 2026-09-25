---
description: >-
  GridGain's Major.Minor.Maintenance versioning convention, the standard support
  lifecycle, and the release support dates for GridGain platform versions.
---

# Versioning and Support Lifecycle

GridGain releases new versions on a regular basis following a *Major.Minor.Maintenance* naming convention.

{% hint style="info" %}
Each GridGain distribution includes a [SWID tag](software-identification.md) encoding the edition, major and minor version, and support lifecycle dates for use with software asset management (SAM) tools.
{% endhint %}

* *Major Releases* -  represent major product changes, some of which are not backward-compatible. [Rolling Upgrades](upgrade/rolling-upgrades.md) for Enterprise and Ultimate Editions are not supported for major versions changes and assume a special upgrade procedure for production clusters.
* *Minor Releases* - introduce new features and significant improvements. Rolling Upgrades are supported for all minor releases unless there are any breaking changes.
* *Maintenance Releases* - deliver bug fixes, security patches, and performance optimizations. Rolling Upgrades are supported similarly to minor releases as described above.

## Support Lifecycle

Standard support for GridGain minor versions lasts for at least 2 years from the minor version release date. Issues found in a minor version will be fixed in a maintenance release for the minor version, or in a future minor version.

After standard support ends, new releases and patches are no longer provided. Customers with an active support subscription can contact GridGain support regarding their issues after the end of standard support.

The following support options are available for Standard and Premium support customers:

| Description | During Standard Support Period | After Standard Support Period |
|---|---|---|
| Support via ticket system for service requests | Yes | Yes |
| Security alerts and updates | Yes | No |
| Critical patch updates | Yes | No |
| Regular patches and improvements | Yes | No |
| New features | Yes | No |

## List of Releases

### GridGain Platform Releases: Standard Support

| Version | Release Date | End of Standard Support |
|---|---|---|
| 8.9.X | October 4, 2023 | -- |
| 8.8.X | December 30, 2020 | December 31, 2024 |
| 8.7.X | March 4, 2019 | December 31, 2021 |
| 8.5.X | October 31, 2018 | October 31, 2020 |
| 8.4.X | April 28, 2018 | April 28, 2020 |
| 8.3.X | November 2, 2017 | November 2, 2019 |

### GridGain Web Console Releases: Extended Support

Standard support for GridGain Web Console has ended on October 2, 2021.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
