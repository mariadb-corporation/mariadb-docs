# Upgrading MariaDB MaxScale from 6 to 22.08

This document describes possible issues when upgrading MariaDB MaxScale from
version 6 to 22.08.

For more information about what has changed, please refer to the [ChangeLog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/maxscale) and to the [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/maxscale).

Before starting the upgrade, any existing configuration files should be backed
up.

## Removed Features

* The support for legacy encryption keys generated with `maxkeys` from pre-2.5
  versions has been removed. This feature was deprecated in MaxScale 2.5 when
  the new key storage format was introduced. To migrate to the new key storage
  format, create a new key file with `maxkeys` and re-encrypt the passwords with`maxpasswd`.
* The deprecated Database Firewall filter has been removed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
