---
description: >-
  Changelog for mariadb_es_repo_setup, the MariaDB Enterprise Server package
  repository setup script.
icon: clock-rotate-left
---

# mariadb\_es\_repo\_setup Changelog

`mariadb_es_repo_setup` configures access to the MariaDB Package Repositories for MariaDB Enterprise Server. For download, verification, and usage instructions, see [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage).

The version of the script is a date, which you can display by running the script with the `--version` option. The changes made in each version are listed below, reproduced from the changelog comments at the top of the script. For the checksum of each released version, see the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage#versions) section of the setup and usage page.

* **2026-06-30**
  * TODO-3939 Write Deb822 (mariadb.sources) format by default; add --list flag to force the old one-line .list format; this option is for Debian/Ubuntu only, it has no effect when used on other systems
  * Store the signing key at /etc/apt/keyrings/mariadb-keyring.gpg and reference it via Signed-By; remove old trusted.gpg.d key (if it exists) on --apply
  * Disable any pre-existing old-format apt source file (mariadb.list or mariadb.sources) to avoid apt "configured multiple times" errors after OS upgrades
  * Accept 'latest' as a value for the --mariadb-server-version option to get the latest version of MariaDB Enterprise; WARNING: Using this option in production could result in an unintended upgrade to a higher series of MariaDB Enterprise Server when a new GA series is released, using 'latest' is mainly useful for automated testing; 'latest-LTS' is also supported because that is a valid value for the same option when using the Community Server `mariadb_repo_setup` script, but here it is treated only as a synonym of 'latest', as Enterprise Server only has LTS releases
  * Match 'latest'/'beta' case-insensitively for --mariadb-maxscale-version
  * Update MaxScale Default to 25.10
  * Clarify support of RHEL 10 in help text
  * Add support for Ubuntu 26.04 Resolute
  * Change 'Tools' repo to not be included by default, it will now only be included if new '--include-tools' option is given
* **2026-04-30**
  * Add error message handling for MaxScale repository failures
  * Re-enable MaxScale repository for RHEL 10
  * Fix Keyring and legacy Tools repo URLs
  * Fix key_urls variable copying
* **2026-03-10**
  * Fix Enterprise Tools repo selection on aarch64
  * Add --ignore-missing to checksum verify example because the checksum file includes more than just the repo setup script
* **2025-12-10**
  * Update key used by MaxScale repositories
* **2025-10-22**
  * Fix various URLs
  * Change Enterprise Server default to 11.8
  * Add support for Debian 13 'trixie'
* **2025-08-29**
  * New GPG key for RHEL 10 and equivalent
  * The MaxScale repository is disabled for RHEL 10 as there are no packages currently available for it
* **2025-06-04**
  * Add support for MariaDB ES 11.8 versions
* **2025-01-16**
  * Change default to 11.4, adjust MaxScale repo URL
* **2025-01-07**
  * Fixes for 11.4 regex
* **2024-11-19**
  * Fix default version, still 10.6
* **2024-11-13**
  * Add support for MariaDB ES 11.4 versions
* **2024-09-20**
  * Disable enterprise-tools repository setup
* **2024-09-09**
  * Add support for Ubuntu 24.04 Noble
  * Remove RHEL/CentOS 7, Debian 10 'buster'
  * Add --skip-eol-check and --skip-os-eol-check options for testing old eol versions of MariaDB Enterprise
* **2024-06-12**
  * Add support for RHEL 9 ppc64le
* **2023-07-27**
  * Adjust regex to support MariaDB ES 23.x versions
* **2023-07-27**
  * Add Debian 12 Bookworm
* **2023-03-13**
  * Add to the error message about missing/wrong version
* **2022-10-26**
  * Fix issue with Enterprise Tools repository on aarch64
* **2022-10-25**
  * Add support for the MariaDB Enterprise Tools repository
* **2022-09-12**
  * Minor updates to some info messages
* **2022-08-09**
  * Add RHEL/Rocky 9
* **2022-07-27**
  * Remove Debian 9 Stretch
* **2022-06-14**
  * Add --skip-verify option for skipping version verification
* **2022-06-02**
  * Look up current MariaDB and Maxscale versions
* **2022-05-31**
  * Check token locally for correct form before verifying
* **2022-05-03**
  * Add Rocky 8 to usage/help output, remove CentOS 8
* **2022-04-21**
  * add Ubuntu 22.04 LTS "jammy"
* **2022-04-05**
  * Fix issues with SLES 15 and RHEL 7 aarch64 repository setup
* **2022-03-11**
  * Update various documentation URLs
* **2022-01-31**
  * Verify that server version is valid
* **2022-01-18**
  * Add --arch flag to manually specify the CPU architecture
* **2021-12-10**
  * Update keyring URL
* **2021-12-01**
  * Update GPG URLs
* **2021-10-26**
  * Better default permissions for Ubuntu/Debian list file
* **2021-10-07**
  * Improve token verification
* **2021-10-04**
  * Fix MaxScale ARM support
* **2021-09-09**
  * Add aarch64/arm64 server repositories
* **2021-08-02**
  * Add Debian 11 Bullseye & aarch64/arm64 MaxScale repositories
* **2021-07-30**
  * Remove Ubuntu 16.04 Xenial
* **2021-07-06**
  * Update MariaDB to 10.6
* **2021-06-28**
  * Fix warnings with debug repositories on Ubuntu 18.04 Bionic
* **2021-06-24**
  * MDEV-25991, adjust apt-transport-https dependency
* **2021-06-09**
  * Limit deb repos to amd64 architecture
* **2021-06-07**
  * MDEV-25805 fix detection for Rocky and Alma Linux 8
* **2021-06-01**
  * Clean Package Cache after yum/dnf/zyp repository configuration
* **2021-05-04**
  * Fix MaxScale repository paths, change version to 'latest'
* **2021-03-04**
  * Add chmod step to ensure apt can read the keyring
* **2021-02-12**
  * Include dbgsym ddeb packages for Ubuntu
* **2021-01-26**
  * Validate manually supplied --os-type and --os-version
* **2021-01-22**
  * Remove ambiguous $basearch from sles repository config
* **2021-01-14**
  * Add --version flag
* **2020-12-16**
  * Fix issue with detecting CentOS 8.3+
* **2020-12-14**
  * Fix error when specifying centos as os-type
* **2020-12-14**
  * Remove deprecated Linux distributions
* **2020-12-05**
  * Update names of yum/zypper repos
* **2020-12-01**
  * Update urls for MaxScale and Tools repositories
* **2020-11-30**
  * Add ability to skip check\_installed
* **2020-11-30**
  * Add 'Unsupported' repository
* **2020-10-14**
  * Update MaxScale repos to use CDN
* **2020-10-13**
  * Add check\_installed function to ensure script can run
* **2020-10-13**
  * Update usage instructions
* **2020-10-05**
  * Fix incorrect exit code
* **2020-09-11**
  * Update default MaxScale version to 2.5
* **2020-09-08**
  * Add MariaDB Xpand
* **2020-07-16**
  * Update default to MariaDB Enterprise 10.5
* **2020-06-08**
  * add Ubuntu 20.04 "focal"
* **2020-05-15**
  * fix wording of what Ubuntu LTS releases are supported
* **2020-04-29**
  * update curl command to correctly handle CDN redirects
* **2020-01-24**
  * Verify tokens to ensure that they are valid
* **2020-01-22**
  * Add "module\_hotfixes = 1" to RHEL/CentOS 8 config (MDEV-20673)
* **2020-01-22**
  * Update msg strings for better output and consistency
* **2020-01-08**
  * Add autorefresh=1 to SLES repo configs
* **2019-11-18**
  * Add SLES 12 & 15
* **2019-09-26**
  * MDEV-20654 - change gpg key importing
* **2019-09-26**
  * Add RHEL 8, CentOS 8, and Debian 10
* **2019-09-24**
  * Update to MaxScale Version 2.4
* **2018-12-24**
  * Update to MaxScale Version 2.3

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
