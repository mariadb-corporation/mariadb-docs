---
description: >-
  Obtain a MariaDB MaxScale license key from the MariaDB License Portal, install it in
  maxscale.cnf, and understand what MaxScale does when the license expires.
hidden: true
---

# Install a MaxScale License Key

MariaDB MaxScale requires a license key to start. The key is issued by MariaDB, installed in the
MaxScale configuration file, and validated every time MaxScale starts.

This page covers Enterprise Platform license keys. The mechanism is the same one used by
[MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) — the same `license_key` parameter,
in the same place — and the two differ only in what the license itself grants. If you are
evaluating MaxScale rather than running it in production, follow the trial page instead.

For the full list of MariaDB products that use a license key, see
[Install a MariaDB Enterprise Platform License](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/enterprise-license-install).

## Before you begin

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
   [Get your license key](#get-your-license-key).

## Get your license key

License keys are issued through the MariaDB License Portal, which is separate from the download
site.

1. Navigate to the [MariaDB License Portal](https://customers.mariadb.com/license/).
2. Sign in with your MariaDB ID. If you do not have an account, you can create one using your
   email, Google, GitHub, or LinkedIn credentials.
3. Select the Enterprise Platform card. Then follow the instructions on the page to generate
   your key. One Enterprise Platform key is valid for all MariaDB products that use a license key.
4. Copy or download the generated key. You need it to complete the steps below.

{% hint style="info" %}
If you do not see a card for your subscription, contact
[MariaDB](https://mariadb.com/maxscale-contact/) and your key will be provided to you directly.
{% endhint %}

<!-- TODO (DOCS-6634): confirm with Allen Herrera that the Enterprise Platform card is live on
     customers.mariadb.com/license/ and whether it has a deep link, as the trial does at
     /license/maxscale-trial/. Adjust step 3 and the hint accordingly before publishing. -->

## Install the key

Open `/etc/maxscale.cnf` and add a `license_key` entry to the `[maxscale]` section:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
license_key=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6...
```
{% endcode %}

The value of `license_key` can either be the license key itself or the **absolute** path to a file
containing the key:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
license_key=/etc/maxscale-license.key
```
{% endcode %}

{% hint style="warning" %}
A relative path is not treated as a file. If the path is not absolute, MaxScale interprets the
value as a license key, fails to parse it, and refuses to start.
{% endhint %}

{% hint style="info" %}
If the license is read from a file, the file must be readable by the `maxscale` user.
{% endhint %}

Start MaxScale once the key is in place:

```bash
sudo systemctl start maxscale.service
```

### Change the key on a running MaxScale

`license_key` can be changed at runtime, so a renewed license can be installed without a restart:

```bash
maxctrl alter maxscale license_key=<new-key>
```

## System and configuration feedback

By default, MaxScale sends feedback to MariaDB. The feedback contains the contract ID of the
license key and the system information that `maxctrl show maxscale` shows in the `System` row.
It does not contain user data or SQL.

MaxScale sends the feedback to `customers.mariadb.com` 30 seconds after it starts. MaxScale
does not send the feedback again if the data did not change, or if it sent feedback in the
last 24 hours.

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

After MaxScale sends the feedback, it saves a copy of the data in the file `feedback.json`
in the data directory. The default location is `/var/lib/maxscale/feedback.json`.

To disable the feedback, add `enable_feedback=false` to the `[maxscale]` section and restart
MaxScale:

{% code title="/etc/maxscale.cnf" %}
```ini
[maxscale]
enable_feedback=false
```
{% endcode %}

## Expiry and renewal

* **At startup:** if the license is expired, not valid, or missing, MaxScale does not start.
  The error log gives the reason.
* **While MaxScale runs:** when the license expires, MaxScale logs
  `The license has expired, please contact MariaDB: https://mariadb.com/maxscale-contact/`
  and stops.

To renew the license, generate a new key in the
[MariaDB License Portal](https://customers.mariadb.com/license/). Then install the new key as
described in [Install the key](#install-the-key).

## Troubleshoot

Look in the MaxScale log first:

```bash
sudo cat /var/log/maxscale/maxscale.log
```

| Log message | Cause and action |
| ----------- | ---------------- |
| `Invalid license key.` | The key is not correct. Possible causes: the key is incomplete because it was not fully copied, or MariaDB did not sign it. Copy the full key again. |
| `Invalid license key. If the license key refers to a file, use an absolute path and make sure the file exists.` | The value of `license_key` contains a `/`, but MaxScale cannot use it as a file. The path is relative, or the file does not exist. Use an absolute path to a file that exists. |
| `Invalid license key file: <error>` | MaxScale cannot read the license key file. Make sure that the `maxscale` user can read the file. |
| `The MaxScale license period of <duration> has ended. Please renew your MaxScale license: https://mariadb.com/maxscale-contact/` | The license has expired. Generate a new key. |
| `The MaxScale license is not yet valid. Validity starts after <duration>.` | The start date of the license is in the future, or the clock of the host is wrong. Wait until the start date, or correct the clock. |
| `License key does not have any valid entitlements for MaxScale.` | The license is valid, but it is not for MaxScale. Contact MariaDB. |
| `License key contains only expired entitlements for MaxScale.` | The license was for MaxScale, but the MaxScale entitlement has expired. Generate a new key. |
| `The license key has no entitlements.` | The key has the correct format, but it does not give access to a product. Contact MariaDB. |

## See also

* [Install a MariaDB Enterprise Platform License](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/enterprise-license-install) — license
  installation across MariaDB products
* [MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) — evaluating MaxScale
* [MaxScale Installation Guide](maxscale-installation-guide.md)
* [MaxScale Configuration Guide](../deployment/installation-and-configuration/maxscale-configuration-guide.md)
* [Setting up MariaDB MaxScale](../../mariadb-maxscale-tutorials/setting-up-mariadb-maxscale.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
