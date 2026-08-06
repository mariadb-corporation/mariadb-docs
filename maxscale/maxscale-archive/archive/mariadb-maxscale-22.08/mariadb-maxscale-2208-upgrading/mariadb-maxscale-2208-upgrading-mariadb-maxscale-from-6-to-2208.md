# Upgrading MariaDB MaxScale From 6 to 22.08

## Upgrading MariaDB MaxScale from 6 to 22.08

## Upgrading MariaDB MaxScale from 6 to 22.08

This document describes possible issues when upgrading MariaDB MaxScale from
version 6 to 22.08.

For more information about MaxScale 22.08, refer to the [ChangeLog](../../../../../en/mariadb-maxscale-2208-maxscale-2208-changelog/).

Before starting the upgrade, any existing configuration files should be backed
up.

## Removed Features

* The support for legacy encryption keys generated with `maxkeys` from pre-2.5
  versions has been removed. This feature was deprecated in MaxScale 2.5 when
  the new key storage format was introduced. To migrate to the new key storage
  format, create a new key file with `maxkeys` and re-encrypt the passwords with`maxpasswd`.
* The deprecated Database Firewall filter has been removed.

CC BY-SA / Gnu FDL
