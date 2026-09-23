---
description: >-
  Release notes for MariaDB Cloud YYYY.MM.DD, adding support for multiple
  MariaDB Server versions on MariaDB Cloud Serverless.
icon: rocket-launch
hidden: true
---

<!--
  HIDDEN DRAFT — DOCS-6483 · MCDEV-3699.

  Listed in SUMMARY.md but kept out of the published nav by `hidden: true` in
  the frontmatter above. The page still resolves by direct URL, for review.

  Keep the frontmatter at line 1: an HTML comment above it makes GitBook render
  the frontmatter as page text and silently breaks `hidden: true`.

  Blocked on, before reveal:
    1. Release date — not set as of 2026-09-14. UAT Go/No-Go passed 2026-09-11
       (GO, all stakeholders; docs + this RN were the open items). Date to come
       from Zhanna / the Cloud UAT calendar.
    2. `enable-dps-serverless-versions` enabled in production (currently OFF).
    3. Whether the feature is labeled GA. Nothing in the PRD, the UAT plan, or
       the Go/No-Go call marks it Tech Preview, so it is written as GA here —
       confirm with Naman / Vasiliy.

  Deliberately NOT claimed below: minor-version upgrades for Serverless. The
  capability is gated by `enable-dps-serverless-db-upgrades` and Vasiliy still
  owes a verification (open side item from the Go/No-Go call). Note that
  mariadb-cloud/readme/serverless.md currently does assert it — reconcile the
  two before reveal.

  At reveal:
    1. Set the date in the description and the Release Date line; rename this
       file to mariadb-cloud-<YYYY.MM.DD>.md and update the SUMMARY.md path.
    2. Remove `hidden: true` above, and add the {% content-ref %} entry to
       mariadb-cloud-release-notes/README.md (newest first). The card is held
       back until then: that README is live, so a card here would surface an
       unreleased feature.

  Cross-space links are already expanded to app.gitbook.com URLs (matching the
  two published Cloud RNs) because this lands as a direct commit to main and
  expand-gitbook-aliases only runs on PRs.
-->

# Multiple MariaDB Server Versions on Serverless

**Release Date:** _TBD_

## New Features

### Multiple MariaDB Server versions on Serverless

A Serverless database can now be created on any MariaDB Server version that MariaDB Cloud offers for provisioned single-node databases. Previously, a Serverless database could only be created on the current default version.

Choose the version with the **MariaDB Version** picker when you launch the database.

Availability and behavior:

* **Default version** — MariaDB Cloud keeps pre-provisioned instances on the default version, so a database created on it is ready in milliseconds. The picker pre-selects this version.
* **Any other available version** — the database is built on demand when you create it, so it takes longer to launch than the instant start. In every other respect it is a Serverless database: it scales to zero when idle, resumes on connection, and is billed by MCU-hour.
* Selecting a version other than the default requires a paid plan. On a trial with no payment method on file — including the Free Developer Tier database — the version picker offers the default version only.
* MariaDB Community Server versions are available on all service tiers. MariaDB Enterprise Server versions are available on the **Power** and **PowerPlus** tiers, in addition to the default Community version.

For details, see [MariaDB Cloud Serverless](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/readme/serverless) and [MariaDB Server Version Support](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/reference/mariadb-server-versions).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
