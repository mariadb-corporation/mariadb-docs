---
description: >-
  Obtain a MariaDB MaxScale license key from the MariaDB License Portal, install it in
  maxscale.cnf, and understand what MaxScale does when the license expires.
hidden: true
---

# Install a MaxScale License Key

MariaDB MaxScale requires a license key to start. The key is issued by MariaDB, installed in the
MaxScale configuration file, and validated every time MaxScale starts.

This page covers Enterprise Platform license keys.
[MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) uses the same mechanism and the same
`license_key` parameter. The two differ only in what the license grants. To evaluate MaxScale,
follow the trial page instead.

For the full list of MariaDB products that use a license key, see
[Install a MariaDB Enterprise License](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/enterprise-license-install).

## Before You Begin

Do these steps before you install the license key:

1. Download MaxScale.
   * If you have an Enterprise Platform subscription, sign in with your
     customer account. Then download MaxScale from
     [Download MariaDB](https://mariadb.com/downloads/enterprise/enterprise-maxscale/).
   * If you want to evaluate MaxScale, use the
     [MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) page instead.
2. Install MaxScale. For instructions, see the
   [MaxScale Installation Guide](maxscale-installation-guide.md).
   The installation creates the file `/etc/maxscale.cnf`. You add the license
   key to this file in a later step.
3. Get a license key from the MariaDB License Portal. The License Portal is
   not the same site as the download site. For instructions, see
   [Get Your License Key](#get-your-license-key).

## Get Your License Key

1. Go to the [MariaDB License Portal](https://customers.mariadb.com/license/).
2. Sign in with your MariaDB ID. If you do not have an account, create one with your email
   address or with your Google, GitHub, or LinkedIn account.
3. Select the Enterprise Platform card. Then follow the instructions on the page to generate
   your key. One Enterprise Platform key is valid for all MariaDB products that use a license key.
4. Copy or download the key. You add it to the configuration file in
   [Install the Key](#install-the-key).

{% hint style="info" %}
If you do not see a card for your subscription, contact
[MariaDB](https://mariadb.com/maxscale-contact/). MariaDB then sends you the key directly.
{% endhint %}

<!-- TODO (DOCS-6634): confirm with Allen Herrera that the Enterprise Platform card is live on
     customers.mariadb.com/license/ and whether it has a deep link, as the trial does at
     /license/maxscale-trial/. Adjust step 3 and the hint accordingly before publishing. -->

## Install the Key

Open `/etc/maxscale.cnf` and add a `license_key` entry to the `[maxscale]` section:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
license_key=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6...
```
{% endcode %}

The value of `license_key` can be the license key itself or the **absolute** path to a file that
contains the key:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
license_key=/etc/maxscale-license.key
```
{% endcode %}

{% hint style="warning" %}
MaxScale reads the value as a file path only if the path is absolute and the file exists.
Otherwise, MaxScale reads the value as the license key itself, cannot parse it, and does not
start.
{% endhint %}

{% hint style="info" %}
If the key is in a file, the `maxscale` user must be able to read the file.
{% endhint %}

Then start MaxScale:

```bash
sudo systemctl start maxscale.service
```

### Change the Key on a Running MaxScale

You can change `license_key` at runtime. To install a renewed license without a restart, run:

```bash
maxctrl alter maxscale license_key=<new-key>
```

## System and Configuration Feedback

By default, MaxScale sends feedback to MariaDB. The feedback contains the contract ID of the
license key and the system information that `maxctrl show maxscale` shows in the `System` row.
It does not contain user data or SQL.

MaxScale sends the feedback to `customers.mariadb.com` 30 seconds after it starts. It skips
sending if the data is the same as the last time, or if it already sent feedback in the last 24
hours.

Example of the `System` row:

```
├──────────────┼──────────────────────────────────────────────────────────────────────────┤
│ System       │ {                                                                        │
│              │     "databases": {                                                       │
│              │         "10.11.16-MariaDB-log": 4                                        │
│              │     },                                                                   │
│              │     "machine": {                                                         │
│              │         "cores_available": 8,                                            │
│              │         "cores_physical": 8,                                             │
│              │         "cores_virtual": 8.0,                                            │
│              │         "memory_available": 33345155072,                                 │
│              │         "memory_physical": 33345155072                                   │
│              │     },                                                                   │
│              │     "maxscale": {                                                        │
│              │         "query_classifier_cache_size": 5001773260,                       │
│              │         "threads": 4                                                     │
│              │     },                                                                   │
│              │     "modules": {                                                         │
│              │         "mariadbmon": 1,                                                 │
│              │         "readconnroute": 2,                                              │
│              │         "readwritesplit": 1                                              │
│              │     },                                                                   │
│              │     "os": {                                                              │
│              │         "machine": "x86_64",                                             │
│              │         "os_type": "rocky",                                              │
│              │         "os_version": "8",                                               │
│              │         "release": "7.2.7-100.fc43.x86_64",                              │
│              │         "sysname": "Linux",                                              │
│              │         "version": "#1 SMP PREEMPT_DYNAMIC Mon Sep 21 19:33:15 UTC 2026" │
│              │     }                                                                    │
│              │ }                                                                        │
└──────────────┴──────────────────────────────────────────────────────────────────────────┘
```

After MaxScale sends the feedback, it saves a copy of the data in the file `feedback.json` in
the data directory. By default, this is `/var/lib/maxscale/feedback.json`.

To disable the feedback, add `enable_feedback=false` to the `[maxscale]` section and restart
MaxScale:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
enable_feedback=false
```
{% endcode %}

## Expiry and Renewal

* **At startup:** if the license is expired, not valid, or missing, MaxScale does not start.
  The MaxScale log gives the reason.
* **While MaxScale runs:** when the license expires, MaxScale logs
  `The license has expired, please contact MariaDB: https://mariadb.com/maxscale-contact/`
  and stops.

To renew the license, generate a new key in the
[MariaDB License Portal](https://customers.mariadb.com/license/). Then install the new key as
described in [Install the Key](#install-the-key), or
[change it on the running MaxScale](#change-the-key-on-a-running-maxscale).

## Troubleshoot

Look in the MaxScale log first:

```bash
sudo cat /var/log/maxscale/maxscale.log
```

| Log message | Cause and action |
| ----------- | ---------------- |
| `Invalid license key.` | MaxScale cannot parse the key, or MariaDB did not sign it. Usually, the key was not copied completely. Copy the full key again. |
| `License key is not valid.` | The signature or the issuer of the key is not correct, for example because the key was changed after MariaDB issued it. MaxScale then also logs `Invalid license key.` Copy the full key again, or generate a new key. |
| `Invalid license key. If the license key refers to a file, use an absolute path and make sure the file exists.` | The value of `license_key` contains a `/`, but MaxScale cannot use it as a file. The path is relative, or the file does not exist. Use the absolute path to a file that exists. |
| `Invalid license key file: <error>` | MaxScale cannot read the license key file. Make sure that the `maxscale` user can read the file. |
| `The MaxScale license period of <duration> has ended. Please renew your MaxScale license: https://mariadb.com/maxscale-contact/` | The license has expired. Generate a new key. |
| `The MaxScale license is not yet valid. Validity starts after <duration>.` | The start date of the license is in the future, or the clock of the host is wrong. Wait until the start date, or correct the clock. |
| `License key does not have any valid entitlements for MaxScale.` | The license is valid, but it is not for MaxScale. Contact MariaDB. |
| `License key contains only expired entitlements for MaxScale.` | The license was for MaxScale, but the MaxScale entitlement has expired. Generate a new key. |
| `The license key has no entitlements.` | The key is valid, but it does not give access to any product. Contact MariaDB. |

## See Also

* [Install a MariaDB Enterprise License](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/enterprise-license-install) — license
  installation across MariaDB products
* [MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) — evaluating MaxScale
* [MaxScale Installation Guide](maxscale-installation-guide.md)
* [MaxScale Configuration Guide](../deployment/installation-and-configuration/maxscale-configuration-guide.md)
* [Setting up MariaDB MaxScale](../../mariadb-maxscale-tutorials/setting-up-mariadb-maxscale.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
