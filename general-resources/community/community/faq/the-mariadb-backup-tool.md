# The mariadb-backup Tool

* Q: What is mariadb-backup and its primary use?\
  A: mariadb-backup is a command-line utility included with MariaDB Community Server. Its primary use is to perform physical "hot" backups of MariaDB database instances, especially those utilizing transactional storage engines like InnoDB and XtraDB. This tool is based on the well-regarded Percona XtraBackup technology.
* Q: What are the main advantages of using mariadb-backup for database backups?\
  A: The main advantages of mariadb-backup are its ability to perform online (hot) backups with minimal locking. This means your MariaDB database remains largely available for both read and write operations during the backup process. For large databases, mariadb-backup is generally much faster than logical backup methods (like mariadb-dump) and, when used in conjunction with MariaDB's binary logs, it enables precise point-in-time recovery (PITR).
* Q: How does the mariadb-backup utility work to create backups?\
  A: mariadb-backup works by copying the physical data files from the MariaDB data directory while the server is running. It continuously monitors for changes made to these files during the backup operation and records these modifications in a separate log file. In a subsequent "prepare" phase, these logged changes are applied to the copied data files to ensure they are brought to a transactionally consistent state, ready for restoration.
* Q: Is mariadb-backup a suitable backup solution for all MariaDB storage engines?\
  A: mariadb-backup is primarily designed for, and works most effectively with, transactional storage engines such as InnoDB and XtraDB, for which it can guarantee consistency and perform online backups. While it might be able to copy data files for other storage engines like Aria or MyISAM, it cannot ensure the same level of transactional consistency or perform true online backups for them. For non-transactional engines, mariadb-dump or filesystem-level snapshots might be more appropriate choices.
* Q: Is the mariadb-backup tool free to use?\
  A: Yes, mariadb-backup is an open-source tool that is included as a standard utility with MariaDB Community Server and is completely free to use.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
