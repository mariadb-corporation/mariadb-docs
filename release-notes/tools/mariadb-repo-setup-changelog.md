---
description: >-
  Changelog for mariadb_repo_setup, the MariaDB Community Server package
  repository setup script.
icon: clock-rotate-left
---

# mariadb\_repo\_setup Changelog

`mariadb_repo_setup` configures access to the MariaDB Package Repositories for MariaDB Community Server. For download, verification, and usage instructions, see [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage).

The version of the script is a date, which you can display by running the script with the `--version` option. The changes made in each version are listed below, reproduced from the changelog comments at the top of the script. For the checksum of each released version, see the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage#versions) section of the setup and usage page.

* **2026-06-30**
  * TODO-3939 Write Deb822 (mariadb.sources) format by default; add --list flag to force the old one-line .list format
  * Store the signing key at /etc/apt/keyrings/mariadb-keyring.gpg and reference it via Signed-By; remove old trusted.gpg.d key on key import
  * Disable any pre-existing old-format apt source file (mariadb.list or mariadb.sources) to avoid apt "configured multiple times" errors after OS upgrades
  * Accept 'latest' and 'latest-LTS' for --mariadb-server-version WARNING: Using this option in production could result in an unintended upgrade to a higher series of MariaDB Community Server when a new GA series is released, these are mainly useful for automated testing
  * Match 'latest'/'beta' case-insensitively for --mariadb-maxscale-version
  * Fix typo in processing of --arch flag
  * Add Ubuntu 26.04 LTS "resolute"
* **2026-04-23**
  * Deprecate RHEL/CentOS 7 and Ubuntu 20.04
  * Update URLs for tools repository
  * Update URL for legacy MariaDB repositories
  * Remove unneeded Enterprise key from key list
* **2025-12-10**
  * Update key used by MaxScale repositories
* **2025-11-18**
  * Fix 12.x matching
* **2025-08-07**
  * Update MariaDB default to 12.rolling
  * Change SLES version/arch default to $releasever/$basearch
  * Add Debian 13 "Trixie", RHEL/Rocky/Alma 10,
  * Change tools repo to not be included by default, it will now only be included if new '--include-tools' option is given
  * Update documentation links
* **2025-02-13**
  * Add support for 11.8
* **2024-11-14**
  * Add support for 11.7
* **2024-08-14**
  * Add support for 11.6
* **2024-06-06**
  * Update MariaDB default to 11.rolling
* **2024-05-30**
  * Update MariaDB default to 11.4, add support for 11.5
  * Add Ubuntu 24.04 LTS "noble"
* **2024-02-16**
  * Update MariaDB default to 11.3, add support for 11.4
* **2023-11-21**
  * Update MariaDB default to 11.2, add support for 11.3
* **2023-08-21**
  * Update MariaDB default to 11.1, add support for 11.2
* **2023-08-14**
  * Add Debian 12 Bookworm
* **2023-06-09**
  * Update MariaDB default to 11.0, add support for 11.1
* **2023-06-08**
  * Fix for uname reporting alternate arch names
* **2023-02-16**
  * Update MariaDB default to 10.11, add support for 11.0
* **2023-01-23**
  * Add to the error message about missing/wrong version
* **2023-01-23**
  * Better support for setting up old repositories
* **2022-11-17**
  * Update MariaDB default to 10.10, add support for 10.11
* **2022-09-12**
  * Minor updates to some info messages
* **2022-08-22**
  * Fix 10.10 issue with Ubuntu 22.04 and Debian 11
* **2022-08-15**
  * Update MariaDB to 10.9, add support for 10.10
* **2022-08-09**
  * Add RHEL/Rocky 9
* **2022-07-27**
  * Remove Debian 9 Stretch
* **2022-06-14**
  * Add --skip-verify option for skipping version verification
* **2022-06-13**
  * Handle case where invalid os+server combo, but Maxscale OK
* **2022-06-06**
  * Add function to test for known invalid os+server combinations
* **2022-06-03**
  * Update MariaDB to 10.8, add support for 10.9
* **2022-06-02**
  * Look up current MariaDB versions
* **2022-06-01**
  * Add --skip-eol-check and --skip-os-eol-check options for testing old eol versions of mariadb
* **2022-05-31**
  * move all repos to dlm.mariadb.com
* **2022-05-03**
  * Add Rocky 8 to usage/help output, Remove CentOS 8
* **2022-04-21**
  * add Ubuntu 22.04 LTS "jammy"
* **2022-02-08**
  * Adjust repo pinning for Ubuntu/Debian, update MariaDB to 10.7
* **2022-01-31**
  * Verify that server version is valid
* **2022-01-18**
  * Add aarch64 RHEL/SLES repositories
* **2021-12-10**
  * Update keyring URL
* **2021-11-18**
  * Update default URL of script
* **2021-11-08**
  * Add support for 10.7
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
* **2021-06-21**
  * Download repo keys to pki folder on RHEL, SLES
* **2021-06-09**
  * Limit deb repos to amd64,arm64 architectures
* **2021-06-07**
  * MDEV-25805 fix detection for Rocky and Alma Linux 8
* **2021-06-01**
  * Clean Package Cache after yum/dnf/zyp repository configuration
* **2021-05-26**
  * Fix URL handling, remove unneeded warning
* **2021-05-21**
  * Set 10.6 repos to pull from the correct place
* **2021-05-03**
  * Fix MaxScale repository paths, add --skip-check-installed flag
* **2021-03-04**
  * Add chmod step to ensure apt can read the keyring
* **2021-02-12**
  * Include dbgsym ddeb packages for Ubuntu
* **2021-01-26**
  * Validate manually supplied --os-type and --os-version
* **2021-01-22**
  * Remove ambiguous $releasever and $basearch from rhel repo
* **2021-01-22**
  * Remove ambiguous $basearch from sles repo
* **2021-01-14**
  * Add --version flag
* **2020-12-16**
  * Fix issue with detecting CentOS 8.3+
* **2020-12-16**
  * remove CentOS 6, deprecated as of Nov 2020
* **2020-12-07**
  * remove Debian 8 Jessie, deprecated as of Jun 2020
* **2020-10-15**
  * Add check\_installed function to ensure script can run
* **2020-10-15**
  * Update MariaDB MaxScale to use CDN
* **2020-10-15**
  * Change default MaxScale to 'latest'
* **2020-09-11**
  * Update default MaxScale version to 2.5
* **2020-06-25**
  * Update MariaDB to 10.5, also deprecate Ubuntu 14.04 'trusty'
* **2020-05-12**
  * update curl command to correctly handle CDN redirects
* **2020-03-27**
  * add Ubuntu 20.04 "focal"
* **2020-01-22**
  * add "module\_hotfixes = 1" to RHEL/CentOS 8 config (MDEV-20673)
* **2020-01-22**
  * update msg strings for better output and consistency
* **2020-01-08**
  * add autorefresh=1 to sles repo configs
* **2019-12-04**
  * add RHEL 8, and CentOS 8
* **2019-09-25**
  * add Debian 10 "buster"
* **2019-09-25**
  * MDEV-20654 - change gpg key importing
* **2019-09-24**
  * Update to MaxScale Version 2.4
* **2019-06-18**
  * Update to MariaDB 10.4
* **2018-12-24**
  * Update to MaxScale Version 2.3

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
