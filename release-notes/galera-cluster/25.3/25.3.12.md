# Galera 25.3.12 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.12, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable fixes in Galera replication since last binary release by Codership (3.10):

* Support for Debian Jessie (codership/galera#264)
* Galera will abort gracefully if there is no disk space to write the required gcache files (codership/galera#324)
* Gcache files are removed faster than before in order to reduce Galera disk usage (codership/galera#317)
* Better error logging in case of SSL errors or misconfiguration (codership/galera#290)
* The configuration in /etc/sysconfig/garb is now properly honored by the garbd systemd service (codership/galera#267)
* Arbitrator service no longer starts automatically on package installation, giving the user the opportunity to configure it first (codership/galera#266)
* Miscellaneous fixes in the garb startup script (codership/galera#186)
