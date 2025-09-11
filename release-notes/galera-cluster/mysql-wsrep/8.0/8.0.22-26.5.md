# MySQL-wsrep 8.0.22-26.5 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.22 and Galera 4.7, wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.22 and numerous fixes and enhancements specific to Galera replication.

Notable new features in MySQL-wsrep 8.0 since latest release 8.0.21-26.4.

* A new SST method based on Clone plugin was added.
* A new variable `wsrep_mode` was introduced to wsrep behavior. The first application of the variable is to allow ignoring native replication filter rules if configured with `replicate-do-db` (codership/mysql-wsrep#372).
* Logging was improved to display the origin of wsrep-lib and Galera related messages. Log messages prefixed with `P` come from Galera library, messages prefixed with `L` come from wsrep-lib.

Notable fixes in MySQL-wsrep since latest release 8.0.21-26.4.

* Load data failure with foreign keys was fixed (codership/mysql-wsrep#375).
* PS protocol compatibility with MySQL-wsrep was improved.
* FreeBSD compatibility for Xtrabackup v2 SST script was improved (codership/mysql-wsrep#379).
* BF-BF conflicts between OPTIMIZE/REPAIR/ALTER TABLE and DML in precense of foreign key constraints were suppressed (MDEV-21577).
* Due to regression in `mysqld_safe` script recovery step was skipped when starting MySQL server, causing full SST to be donated when IST should have taken place. This issue affected systems which do not use systemd. This has now been fixed.

XtraBackup compatibility:

* Percona XtraBackup version 8.0.22-15.0 or higher is required to perform XtraBackup based SSTs.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* RedHat 7 and 8
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
*   When installing software in Ubuntu 20.04, in order to select correct versions of mysql-common and mysql-client packages, the following must be run before installing mysql-wsrep-8.0 package

    ```bash
    common_version=$(apt-cache policy mysql-common | \
                     grep Candidate | \
                     awk -F ':' '{print $2}' | \
                     tr -d ' ' | grep 8.0)
    apt-get install -y mysql-common=${common_version} mysql-client=${common_version}
    ```
