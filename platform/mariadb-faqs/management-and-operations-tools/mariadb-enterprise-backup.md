# MariaDB Enterprise Backup

* Q: What is MariaDB Enterprise Backup and how does it differ from community tools?\
  A: MariaDB Enterprise Backup is an enhanced version of the physical backup utility, specifically included with MariaDB Enterprise Server subscriptions. It is designed for performing robust, non-blocking backups in demanding production environments, particularly for very large databases and mission-critical systems.
* Q: How does MariaDB Enterprise Backup improve upon the community mariadb-backup utility?\
  A: MariaDB Enterprise Backup incorporates several enterprise-only optimizations. A key enhancement is its improved Data Definition Language (DDL) statement tracking during backup operations. This significantly reduces the duration of locks required, thereby minimizing the impact on write-intensive applications and allowing for smoother operations during the backup window. It's engineered for superior consistency and reduced operational interruption in enterprise scenarios.
* Q: What are the general benefits of physical backups, such as those performed by MariaDB Enterprise Backup?\
  A: Physical backups, by copying the actual data files, are generally much faster than logical backups (which reconstruct SQL statements) for large datasets. They also tend to impose lower CPU and I/O overhead on the database server during the backup process and can often be restored more quickly. MariaDB Enterprise Backup aims to make this inherently efficient process even smoother and more reliable for critical enterprise systems.
* Q: Is MariaDB Enterprise Backup a free tool?\
  A: No, MariaDB Enterprise Backup is a commercial feature and tool. It is available as part of a MariaDB Enterprise subscription from MariaDB plc.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
