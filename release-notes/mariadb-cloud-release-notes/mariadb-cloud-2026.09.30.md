---
description: >-
  MariaDB Cloud 2026.09.30 is a GA release, released on 2026-09-30. It
  adds support for multiple MariaDB Server versions on MariaDB Cloud
  Serverless.
icon: rocket-launch
---

# MariaDB Cloud 2026.09.30: Serverless

**Release Date:** 30 September 2026

Release 2026.09.30 is a GA release.

## New Features

### Multiple MariaDB Server versions on Serverless

A Serverless database can now be created on any MariaDB Server version that MariaDB Cloud offers for provisioned single-node databases. Previously, a Serverless database could only be created on the current default version.

Choose the version with the **MariaDB Version** picker when you launch the database.

Availability and behavior:

* **Default version** — MariaDB Cloud keeps pre-provisioned instances on the default version, so a database created on it is ready in milliseconds. The picker preselects this version.
* **Any other available version** — the database is built on demand when you create it, so it takes longer to launch than the instant start. In every other respect it is a Serverless database: it scales to zero when idle, resumes on connection, and is billed by MCU-hour.
* Selecting a version other than the default requires a paid plan. On a trial with no payment method on file — including the Free Developer Tier database — the version picker offers the default version only.
* MariaDB Community Server versions are available on all service tiers. MariaDB Enterprise Server versions are available on the **Power** and **PowerPlus** tiers, in addition to the default Community version.

For details, see [MariaDB Cloud Serverless](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/readme/serverless) and [MariaDB Server Version Support](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/reference/mariadb-server-versions).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
