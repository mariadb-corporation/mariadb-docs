# MySQL-wsrep 8.0.21-26.4 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.21 and Galera 4.6, wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.21 and numerous fixes and enhancements specific to Galera replication.

New features in MySQL-wsrep since latest release 8.0.19-26.3.

* Audit log plugin was merged from Percona XTraDB Cluster.

Notable fixes in MySQL-wsrep since latest release 8.0.19-26.3.

* Wsrep patch was reworked to work with CATS InnoDB transaction scheduling algorithm.
* Deadlock between DDL and applying transaction was fixed.
* Server crash when starting transaction with `wsrep_on` disabled was fixed.
* Several memory leaks and memory access errors reported by AddressSanitizer were fixed.
* Generic binary tarball package was included in this release.
* Fix for vulnerability CVE-2020-15180.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* RedHat 8 and 8
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

End of life notice:

This is the last release for openSUSE 15.0.

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
