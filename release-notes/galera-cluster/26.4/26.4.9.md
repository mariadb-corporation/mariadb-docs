# Galera 26.4.9 Release Notes

Changes in Galera 4.9 (2021-07-26)

Codership is pleased to announce the release of Galera Replication library 4.9, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.8:

* Networking code was fixed to handle address already in use in graceful manner.
* Applying of streaming replication write sets was made to respect applying order more reliably.
* Too early transaction replay was fixed.
* IST failure handling was improved to allow resuming IST after process restart.
* A new status variable `wsrep_apply_waits` was introduced to count the number of times an applier thread had to wait for its turn to apply a write set.
* An issue of having incorrect certification results right after SST was fixed.
* Occasional excessive GCache CPU consumption during IST was fixed.
* GCS flow control now allows write set replication more reliably when the node is in Donor state.
* Gcache recovery reliability was improved.
* Wsrep provider option `socket.ssl_reload` is now exposed when SSL is enabled.

Build fixes:

* CRC32C detection was improved to work correctly with GCC 4.8.
* `CK_TIMEOUT_MULTIPLER` was restored in Debian build scripts to reduce unit test timeouts during builds (codership/galera#558).
* Tests which rely on the availability of UDP multicast were disabled by default (codership/galera#595).

End of life notices:

* Due to little usage pattern we plan to discontinue building Galera 4 packages for SUSE Linux Enterprise Server 15 after this release.

The users still running above discontinued platforms are adviced to use the binary tarball package.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
