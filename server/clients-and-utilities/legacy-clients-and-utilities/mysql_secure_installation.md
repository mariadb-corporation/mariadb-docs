---
description: >-
  Complete mysql_secure_installation guide: renamed to
  mariadb-secure-installation in 10.5, Linux symlink access, Windows alternate
  binary, security setup.
---

# mysql\_secure\_installation

{% hint style="info" %}
Note that many of the reasons for the existence of this script no longer apply. In particular, from [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), [Unix socket authentication](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is applied by default, and there is usually no need to create a root password. See [Authentication from MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md).
{% endhint %}

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), the client is called `mariadb-secure-installation`. It can still be accessed under its original `mysql_secure_installation` name via a symlink in Linux, or an alternate binary in Windows.

See [mariadb-secure-installation](../deployment-tools/mariadb-secure-installation.md) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
