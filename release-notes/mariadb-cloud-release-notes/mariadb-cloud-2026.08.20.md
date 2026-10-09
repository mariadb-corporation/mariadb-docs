---
description: >-
  MariaDB Cloud 2026.08.20 is a Tech Preview release, released on 2026-08-20.
  It introduces Bring Your Own Cloud (BYOC) on Google Cloud.
icon: rocket-launch
---

# MariaDB Cloud 2026.08.20 Release Notes: BYOC

**Release Date:** 20 August 2026

Release 2026.08.20 is a Tech Preview release.

## New Features

### Bring Your Own Cloud (BYOC) on Google Cloud (Tech Preview)

{% hint style="info" %}
BYOC on Google Cloud is a **Tech Preview**. Features and behavior may change before general availability.
{% endhint %}

Bring Your Own Cloud (BYOC) deploys the MariaDB Cloud data plane inside your own Google Cloud account, while the control plane (Portal, API, and monitoring) remains in MariaDB Cloud. BYOC databases are managed with the same Cloud Portal, APIs, and Terraform provider. This release extends BYOC to Google Cloud.

Because the data plane runs in your account, database nodes and data remain within your own VPC and cloud environment.

Availability and limitations:

* Requires the **Power** or **Power Plus** service tier.
* Supports **Provisioned** databases only; Serverless is not available with BYOC.
* Database services connect privately by default using Google Cloud Private Service Connect.
* Regions are enabled per account rather than from a fixed list. See the available regions on the service launch page in the Cloud Portal, or [MariaDB Cloud Region Choices](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/reference/region-choices).

For details, see [Bring Your Own Cloud (BYOC)](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/bring-your-own-cloud-byoc).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
