# MySQL-wsrep 8.4.2-26.20 Release Notes

Changes in MySQL-wsrep 8.4.2-26.20 (2024-08-02)

Codership is pleased to announce the first beta release of Galera Cluster for MySQL 8.4, consisting of MySQL-wsrep 8.4.2 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.4.2.

Galera Cluster 8.4 is available as targeted packages and package repositories for Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 22.04 LTS (Jammy), and 24.04 LTS (Noble), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep in 8.4.2-26.20:

* `wsrep_provider_options` is now implemented as a plugin, meaning system variables are generated dynamically from options read from the provider. Options can be dynamic or readonly.
* the default SST method is now switched to using the CLONE plugin (other methods, like rsync, are still available).
* the wsrep allowlist allows you to add IPs for Galera Cluster node addresses that can make SST/IST requests.

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
