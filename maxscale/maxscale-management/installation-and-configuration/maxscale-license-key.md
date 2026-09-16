---
description: >-
  Obtain a MariaDB MaxScale license key from the MariaDB License Portal, install it in
  maxscale.cnf, and understand how MaxScale validates and renews it.
hidden: true
---

# Install a MaxScale License Key

MariaDB MaxScale requires a license key to start. The key is issued by MariaDB, installed in the
MaxScale configuration file, and validated every time MaxScale starts.

This page covers enterprise license keys. The mechanism is the same one used by
[MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) — the same `license_key` parameter,
in the same place — and the two differ only in what the license itself grants. If you are
evaluating MaxScale rather than running it in production, follow the trial page instead.

For the full list of MariaDB products that use a license key, see
[Install a MariaDB Enterprise License]({platform}/enterprise-license-install).

## Before you begin

Downloading MaxScale and licensing it are two separate steps, in two different places.

* **Download MaxScale** from
  [Download MariaDB](https://mariadb.com/downloads/enterprise/enterprise-maxscale/). An
  enterprise subscription is required, so sign in with your customer account first. To evaluate
  MaxScale instead, take the free evaluation build from the **Trials** section of
  [Download MariaDB](https://mariadb.com/downloads/) and follow
  [MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md).
* **Generate a license key** in the MariaDB License Portal, as described below.

Install MaxScale before adding the key — the configuration file you edit is created by the
package. See the [MaxScale Installation Guide](maxscale-installation-guide.md).

## Get your license key

License keys are issued through the MariaDB License Portal, which is separate from the download
site.

1. Navigate to the [MariaDB License Portal](https://customers.mariadb.com/license/).
2. Sign in with your MariaDB ID. If you do not have an account, you can create one using your
   email, Google, GitHub, or LinkedIn credentials.
3. Select the MaxScale card and follow the on-screen instructions to generate your key.
4. Copy or download the generated key. You need it to complete the steps below.

{% hint style="info" %}
If you do not see a card for your subscription, contact
[MariaDB](https://mariadb.com/maxscale-contact/) and your key will be provided to you directly.
{% endhint %}

<!-- TODO (DOCS-6634): confirm with Allen Herrera that the enterprise MaxScale card is live on
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

## How MaxScale validates the key

A license key is a JSON Web Token (JWT) signed by MariaDB. MaxScale validates it in two stages.

**Locally.** MaxScale verifies the token's signature against a set of MariaDB public keys built
into the MaxScale package, then checks that the license grants a MaxScale entitlement that has not
expired.

**Online.** MaxScale then contacts `https://customers.mariadb.com/license/activated/` to confirm
that the license is still active, and uses the response in preference to the local copy. If that
request fails — for example on a host with no outbound internet access — MaxScale falls back to the
locally verified license and starts normally.

{% hint style="info" %}
Allow outbound HTTPS to `customers.mariadb.com` where you can. Without it MaxScale still starts,
but it cannot see license changes made after the key was issued.
{% endhint %}

## Expiry and renewal

MaxScale checks the license when it starts, and every three hours after that.

* **At startup**, an expired, invalid, or missing license stops MaxScale from starting. The error
  log explains which of the three it was.
* **While running**, a license that lapses does not stop MaxScale. It logs
  `License is no longer valid.` as a warning at the next three-hourly check and keeps serving
  traffic.

MaxScale logs the remaining lifetime on every check, in the form
`License expires in 27 days at <date>`. The severity escalates as the expiry approaches:

| Remaining lifetime | Log level |
| ------------------ | --------- |
| More than 30 days  | Notice    |
| Less than 30 days  | Warning   |
| Expired            | Error     |

The warning threshold applies only to licenses issued for longer than 30 days, so a short-term
license does not spend its whole life logging warnings.

To renew, generate a new key in the [MariaDB License Portal](https://customers.mariadb.com/license/)
and install it as described above.

## Troubleshoot

Check the MaxScale error log first:

```bash
sudo cat /var/log/maxscale/maxscale.log
```

| Log message | Cause |
| ----------- | ----- |
| `Invalid license key.` | The key is malformed, was not signed by MariaDB, or was truncated when copied. |
| `Invalid license key. If the license key refers to a file, use an absolute path and make sure the file exists.` | The value looks like a path but is relative, or points to a file that does not exist or cannot be read. |
| `The MaxScale license period of <duration> has ended. Please renew your MaxScale license` | The license has expired. Generate a new key. |
| `The MaxScale license is not yet valid. Validity starts after <duration>.` | The license has a future start date, or the host clock is wrong. |
| `License key does not have any valid entitlements for MaxScale.` | The license is valid but was issued for a different product. |
| `License key contains only expired entitlements for MaxScale.` | The license covered MaxScale, but that entitlement has expired. |
| `The license key has no entitlements.` | The token is well-formed but carries no entitlement list. Contact MariaDB. |

## See also

* [Install a MariaDB Enterprise License]({platform}/enterprise-license-install) — license
  installation across MariaDB products
* [MaxScale Trial](../../maxscale-use-cases/maxscale-trial.md) — evaluating MaxScale
* [MaxScale Installation Guide](maxscale-installation-guide.md)
* [MaxScale Configuration Guide](../deployment/installation-and-configuration/maxscale-configuration-guide.md)
* [Setting up MariaDB MaxScale](../../mariadb-maxscale-tutorials/setting-up-mariadb-maxscale.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
