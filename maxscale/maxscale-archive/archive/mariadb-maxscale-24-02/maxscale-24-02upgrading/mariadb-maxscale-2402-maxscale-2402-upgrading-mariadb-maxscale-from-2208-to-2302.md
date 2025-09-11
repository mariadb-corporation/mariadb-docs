# Upgrading MariaDB MaxScale from 22.08 to 23.02

This document describes possible issues when upgrading MariaDB MaxScale from
version 22.08 to 23.02.

For more information about what has changed, please refer to the [ChangeLog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/maxscale) and to the [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/maxscale).

Before starting the upgrade, any existing configuration files should be backed
up.

## Removed Features

* The `csmon` and `auroramon` monitors have been removed.
* The obsolete `maxctrl drain` command has been removed.
* The `maxctrl cluster` commands have been removed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
