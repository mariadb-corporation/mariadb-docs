# Galera 25.3.13 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.13, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable fixes in Galera replication since last binary release by Codership (3.12):

* the 'could not find key from cert index' warning will no longer be printed in certain situations (codership/galera#361)
* fix compilation on the latest Debian release (codership/galera#321)
* fix compilation on FreeBSD
* several fixes to the build scripts to support various distros and architectures (codership/galera#321)
