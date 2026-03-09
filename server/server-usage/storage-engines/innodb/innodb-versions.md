---
description: >-
  This page is outdated. It's left in place because release notes for old
  MariaDB versions refer to it (MariaDB < 10.3).
---

# InnoDB Versions

{% hint style="warning" %}
This page is outdated. It's left in place because release notes for old MariaDB versions refer to it (MariaDB < 10.3).
{% endhint %}

The InnoDB implementation has diverged substantially from the InnoDB in MySQL. Therefore, in these versions, the InnoDB version is no longer associated with a MySQL release version.

The default InnoDB implementation is based on InnoDB from MySQL 5.7. See [Why MariaDB uses InnoDB instead of XtraDB from MariaDB 10.2](innodb-unmaintained/using-innodb-instead-of-xtradb.md) for more information.

#### Note

XtraDB is a performance enhanced fork of InnoDB. For compatibility reasons, the [system variables](innodb-system-variables.md) still retain their original `innodb` prefixes. If the documentation says that something applies to InnoDB, then it usually also applies to the XtraDB fork, unless explicitly stated otherwise. In these versions, it is still possible to use InnoDB instead of XtraDB. See [Using InnoDB instead of XtraDB](innodb-unmaintained/using-innodb-instead-of-xtradb.md) for more information.

## Divergences

Some examples of divergences between MariaDB's InnoDB and MySQL's InnoDB are:

* [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) (which is based on MySQL 5.6) included encryption and\
  variable-size page compression before MySQL 5.7 introduced them.
* [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) (based on MySQL 5.7) introduced persistent AUTO\_INCREMENT ([MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076)) in a GA release before MySQL 8.0.
* [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) (based on MySQL 5.7) introduced instant ADD COLUMN ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)) before MySQL.

## InnoDB Versions Included in MariaDB Releases

### [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)

| InnoDB Version     | Introduced                                                                                                 |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| No longer reported | [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7) |
| InnoDB 5.7.20      | [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3) |
| InnoDB 5.7.19      | [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.1) |
| InnoDB 5.7.14      | [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.0) |

### [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

| InnoDB Version | Introduced                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| InnoDB 5.7.29  | [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.33) |
| InnoDB 5.7.23  | [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.17) |
| InnoDB 5.7.22  | [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15) |
| InnoDB 5.7.21  | [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.13) |
| InnoDB 5.7.20  | [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.10) |
| InnoDB 5.7.19  | [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.8)   |
| InnoDB 5.7.18  | [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.7)   |
| InnoDB 5.7.14  | [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2)   |

### [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1)

| InnoDB Version | Introduced                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| InnoDB 5.6.49  | [MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.46) |
| InnoDB 5.6.47  | [MariaDB 10.1.44](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.44) |
| InnoDB 5.6.44  | [MariaDB 10.1.39](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.39) |
| InnoDB 5.6.42  | [MariaDB 10.1.37](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.37) |
| InnoDB 5.6.39  | [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.31) |
| InnoDB 5.6.37  | [MariaDB 10.1.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.26) |
| InnoDB 5.6.36  | [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.24) |
| InnoDB 5.6.35  | [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.21) |
| InnoDB 5.6.33  | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.18) |
| InnoDB 5.6.32  | [MariaDB 10.1.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.17) |
| InnoDB 5.6.31  | [MariaDB 10.1.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.16) |
| InnoDB 5.6.30  | [MariaDB 10.1.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.14) |
| InnoDB 5.6.29  | [MariaDB 10.1.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.12) |

### [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

| InnoDB Version | Introduced                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| InnoDB 5.6.43  | [MariaDB 10.0.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.38) |
| InnoDB 5.6.42  | [MariaDB 10.0.37](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.37) |
| InnoDB 5.6.40  | [MariaDB 10.0.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.35) |
| InnoDB 5.6.39  | [MariaDB 10.0.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.34) |
| InnoDB 5.6.38  | [MariaDB 10.0.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.33) |
| InnoDB 5.6.37  | [MariaDB 10.0.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.32) |
| InnoDB 5.6.36  | [MariaDB 10.0.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.31) |
| InnoDB 5.6.35  | [MariaDB 10.0.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.29) |
| InnoDB 5.6.33  | [MariaDB 10.0.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.28) |
| InnoDB 5.6.32  | [MariaDB 10.0.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.27) |
| InnoDB 5.6.31  | [MariaDB 10.0.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.26) |
| InnoDB 5.6.30  | [MariaDB 10.0.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.25) |
| InnoDB 5.6.29  | [MariaDB 10.0.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.24) |
| InnoDB 5.6.28  | [MariaDB 10.0.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.23) |
| InnoDB 5.6.27  | [MariaDB 10.0.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.22) |
| InnoDB 5.6.26  | [MariaDB 10.0.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.21) |
| InnoDB 5.6.25  | [MariaDB 10.0.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.20) |
| InnoDB 5.6.24  | [MariaDB 10.0.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.18) |
| InnoDB 5.6.23  | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.17) |
| InnoDB 5.6.22  | [MariaDB 10.0.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.16) |
| InnoDB 5.6.21  | [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) |
| InnoDB 5.6.20  | [MariaDB 10.0.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.14) |
| InnoDB 5.6.19  | [MariaDB 10.0.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.13) |
| InnoDB 5.6.17  | [MariaDB 10.0.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.11) |
| InnoDB 5.6.15  | [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.9)   |
| InnoDB 5.6.14  | [MariaDB 10.0.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.8)   |

## See Also

* [Why MariaDB uses InnoDB instead of XtraDB from MariaDB 10.2](innodb-unmaintained/using-innodb-instead-of-xtradb.md)
* [XtraDB Versions](innodb-unmaintained/about-xtradb.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
