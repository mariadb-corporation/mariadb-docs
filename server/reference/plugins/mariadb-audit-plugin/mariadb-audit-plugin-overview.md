---
description: >-
  The MariaDB Audit Plugin records server activity, including connections,
  queries, and table access, to help meet organizational auditing and compliance
  regulations.
---

# Audit Plugin Overview

MariaDB and MySQL are used in a broad range of environments, but if you needed to record user access to be in compliance with auditing regulations for your organization, you would previously have had to use other database solutions. To meet this need, though, MariaDB has developed the MariaDB Audit Plugin. Although the MariaDB Audit Plugin has some unique features available only for MariaDB, it can be used also with MySQL.

Basically, the purpose of the MariaDB Audit Plugin is to log the server's activity. For each client session, it records who connected to the server (i.e., user name and host), what queries were executed, and which tables were accessed and server variables that were changed. This information is stored in a rotating log file or it may be sent to the local `syslogd`.

Review these pages for detailed documentation:

* [Installation](mariadb-audit-plugin-installation.md)
* [Configuration](mariadb-audit-plugin-configuration.md)
* [Log Settings](mariadb-audit-plugin-log-settings.md)
* [Log Location & Rotation](mariadb-audit-plugin-location-and-rotation-of-logs.md)
* [Log Format](mariadb-audit-plugin-log-format.md)
* [Status Variables](mariadb-audit-plugin-status-variables.md)
* [System Variables](mariadb-audit-plugin-options-and-system-variables.md)

## Tutorials

* [Activating MariaDB Audit Log](https://tunnelix.com/activating-mariadb-audit-log/)\
  by Jaykishan Mutkawoa, May 30, 2016
* [Installing MariaDB Audit Plugin on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html)\
  Amazon RDS supports using the MariaDB Audit Plugin on MySQL and MariaDB database instances.

## Blog Posts

* [MySQL Auditing with MariaDB Auditing Plugin](https://planet.mysql.com/entry/?id=5994184)\
  by Peter Zaitsev, February 15, 2016
