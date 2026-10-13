---
description: >-
  MariaDB Cloud 2026.10.12 is a Public Preview release, released on
  2026-10-12. It adds self-service account linking for Bring Your Own Cloud
  (BYOC) on AWS, Google Cloud, and Microsoft Azure.
icon: rocket-launch
hidden: true
---

# MariaDB Cloud 2026.10.12 Release Notes: BYOC Onboarding

**Release Date:** 12 October 2026

Release 2026.10.12 is a Public Preview release.

## New Features

### Self-service BYOC onboarding (Public Preview)

{% hint style="info" %}
BYOC is in **Public Preview**. Features and behavior may change before general availability.
{% endhint %}

Bring Your Own Cloud (BYOC) deploys the MariaDB Cloud data plane inside your own cloud account, while the control plane (Portal, API, and monitoring) remains in MariaDB Cloud. Until this release, MariaDB staff linked each customer account manually. You can now link your own AWS, Google Cloud, or Microsoft Azure account from the Cloud Portal.

After MariaDB approves your BYOC request, you select a cloud, enter your account details and regions, run a MariaDB-provided template in your own cloud console, and verify the link.

* The templates are in the public `mariadb-byoc-onboarding` repository: CloudFormation or Terraform for AWS, an ARM template or Terraform for Azure, and a guided Cloud Shell tutorial that runs Terraform for Google Cloud.
* After you select **Verify**, the account status changes from **Pending** to **Verification: Running**, **Verification: Passed**, and **Ready**. If verification fails, the page shows the reason, and you can retry.
* **Settings** → **BYOC** lists your linked accounts, with each account's provider, account ID, label, status, enabled regions, template version, and link date. Each row has an actions menu.
* You can edit the enabled regions of an AWS account, and unlink an account.
* A service that you create on a linked cloud deploys into your account, in one of the regions that you enabled.

Availability and limitations:

* Requires the **Power** or **Power Plus** service tier, and MariaDB must enable BYOC for your organization.
* You can link one account for each cloud.
* You can edit regions for AWS accounts only. For Azure and Google Cloud, adding a region requires running the template again.
* You cannot unlink an account while services still run in it. Unlinking does not delete the resources that the template created in your cloud account.
* Supports **Provisioned** databases only. Serverless is not available with BYOC.

For details, see [Bring Your Own Cloud (BYOC)](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/bring-your-own-cloud-byoc).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
