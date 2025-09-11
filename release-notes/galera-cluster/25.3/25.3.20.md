# Galera 25.3.20 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.20, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE, SLES and FreeBSD. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.19):

* Galera can now be compiled with OpenSSL 1.1.0 (GAL-445, codership/galera#407)
* Included asio library would fail to compile with some compilers (GAL-445, codership/galera#407)
* Compilation could fail when compiling on FreeBSD (GAL-476)
* An assertion could happen with two consecutive DDLs run under RSU (GAL-480)
* A scons option, `system_asio=0` is now available to prevent using the system asio library when compiling Galera
* Compilation could fail if attempting to compile Galera with GCC 6 (GAL-484)
* An scons option, `deterministic_tests=1`, is now available to disable non-deterministic Galera unit tests (GAL-470, codership/galera#432)
