# Galera 26.4.6 Release Notes

Codership is pleased to announce the release of Galera Replication library 4.6, implementing wsrep API version 26.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera replication since last binary release by Codership (4.5):

* The in-memory GCache index implementation was reworked to use sorted std::deque instead of std::map, leading to eightfold reduction in GCache memory footprint.
* CRC32C implementation was reworked. Hardware CRC32C is now supported on x86\_64 and ARM64 platforms.
* Bus error due to unaligned access on Sparc64 platform was fixed.
* Three new status variables were added: `wsrep_flow_control_active`, `wsrep_flow_control_requested` and `wsrep_gmcast_segment`.
* Prevent GCache rollover on Donor during IST.
* Binary tarball package was added in this release.

Other changes:

* Unit tests were reworked to replace deprecated Check library API calls with supported ones (codership/galera#577).

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.

End of Life Notice:

This is the last release for openSUSE 15.0.
