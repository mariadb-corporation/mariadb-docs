# MariaDB MaxScale 23.08.2 Release Notes

## MaxScale 23.08 MariaDB MaxScale 23.08.2 Release Notes -- 2023-10-30

## MariaDB MaxScale 23.08.2 Release Notes -- 2023-10-30

Release 23.08.2 is a GA release.

This document describes the changes in release 23.08.2, when compared to the\
previous release in the same series.

If you are upgrading from an older major version of MaxScale, please read the [upgrading document](https://mariadb.com/docs/maxscale/maxscale-versions/mariadb-maxscale-24-02/maxscale-24-02upgrading/mariadb-maxscale-2402-maxscale-2402-upgrading-mariadb-maxscale-from-2302-to-2308) for\
this MaxScale version.

For any problems you encounter, please consider submitting a bug\
report on [our Jira](https://jira.mariadb.org/projects/MXS).

### External CVEs resolved.

* [CVE-2022-1586](https://www.cve.org/CVERecord?id=CVE-2022-1586) Fixed by [MXS-4806](https://jira.mariadb.org/browse/MXS-4806) Update pcre2 to 10.42
* [CVE-2022-1587](https://www.cve.org/CVERecord?id=CVE-2022-1587) Fixed by [MXS-4806](https://jira.mariadb.org/browse/MXS-4806) Update pcre2 to 10.42
* [CVE-2022-41409](https://www.cve.org/CVERecord?id=CVE-2022-41409) Fixed by [MXS-4806](https://jira.mariadb.org/browse/MXS-4806) Update pcre2 to 10.42

### New Features

* [MXS-4759](https://jira.mariadb.org/browse/MXS-4759) Force failover flag

### Bug fixes

* [MXS-4831](https://jira.mariadb.org/browse/MXS-4831) Missing SQL error in server state change messages
* [MXS-4829](https://jira.mariadb.org/browse/MXS-4829) Query Editor doesn't assign active database to existing query tabs
* [MXS-4822](https://jira.mariadb.org/browse/MXS-4822) Chart pane width issue in Query Editor
* [MXS-4821](https://jira.mariadb.org/browse/MXS-4821) Multi-statement detection works differently on non-AVX2 CPUs
* [MXS-4817](https://jira.mariadb.org/browse/MXS-4817) maxscale crashes on maxsimd::generic::is\_multi\_stmt\_imp
* [MXS-4815](https://jira.mariadb.org/browse/MXS-4815) @@last\_gtid and @@last\_insert\_id are treated differently
* [MXS-4814](https://jira.mariadb.org/browse/MXS-4814) GTIDs used by causal\_reads=global cannot be reset without restarting MaxScale
* [MXS-4812](https://jira.mariadb.org/browse/MXS-4812) More than one primary database in a monitor results in errors in MaxScale GUI
* [MXS-4811](https://jira.mariadb.org/browse/MXS-4811) Error handling differences between running maxctrl directly or in a subshell
* [MXS-4810](https://jira.mariadb.org/browse/MXS-4810) --timeout doesn't work with multiple values in --hosts
* [MXS-4808](https://jira.mariadb.org/browse/MXS-4808) connection\_metadata checks for the wrong capability bit
* [MXS-4807](https://jira.mariadb.org/browse/MXS-4807) MaxScale does not always report the OS version correctly
* [MXS-4799](https://jira.mariadb.org/browse/MXS-4799) ConfigManager may spam the log with warnings
* [MXS-4797](https://jira.mariadb.org/browse/MXS-4797) NullFilter has not been extended to support all routing enumeration values.
* [MXS-4792](https://jira.mariadb.org/browse/MXS-4792) Semi-sync replication through MaxScale causes errors on STOP SLAVE
* [MXS-4790](https://jira.mariadb.org/browse/MXS-4790) Log version after log rotation
* [MXS-4788](https://jira.mariadb.org/browse/MXS-4788) Galeramon should use gtid\_binlog\_pos if gtid\_current\_pos is empty
* [MXS-4782](https://jira.mariadb.org/browse/MXS-4782) Kafkacdc logs warnings about the configuration
* [MXS-4781](https://jira.mariadb.org/browse/MXS-4781) cooperative\_replication works even if cluster parameter is not used
* [MXS-4780](https://jira.mariadb.org/browse/MXS-4780) Shutdown may hang if cooperative\_replication is used
* [MXS-4778](https://jira.mariadb.org/browse/MXS-4778) Aborts due to SystemD watchdog should tell if a DNS lookup was in progress
* [MXS-4777](https://jira.mariadb.org/browse/MXS-4777) Maxscale crash due to systemd timeout
* [MXS-4776](https://jira.mariadb.org/browse/MXS-4776) Sescmd target selection is sub-optimal with lazy\_connect
* [MXS-4775](https://jira.mariadb.org/browse/MXS-4775) KafkaCDC: current\_gtid.txt is moving but is behind
* [MXS-4772](https://jira.mariadb.org/browse/MXS-4772) Config sync status leaves origin field empty on restart
* [MXS-4771](https://jira.mariadb.org/browse/MXS-4771) Problem while linking libnosqlprotocol.so
* [MXS-4750](https://jira.mariadb.org/browse/MXS-4750) dynamic\_node\_detection=false does not work with server hostname, needs IP
* [MXS-4743](https://jira.mariadb.org/browse/MXS-4743) switchover-force should ignore replication delay
* [MXS-4718](https://jira.mariadb.org/browse/MXS-4718) Add replication\_custom\_options to enable replication TLS certification check
* [MXS-4686](https://jira.mariadb.org/browse/MXS-4686) Undefined behavior in ed25519 plugin
* [MXS-4604](https://jira.mariadb.org/browse/MXS-4604) Qlafilter doesn't handle pipelined queries correctly
* [MXS-4562](https://jira.mariadb.org/browse/MXS-4562) When MaxScalle is installed from tarball and starded without -d option --basedir=. is not parsed properly and full directory needs to be specified
* [MXS-4538](https://jira.mariadb.org/browse/MXS-4538) No valid servers in cluster 'MariaDB-Monitor'
* [MXS-4457](https://jira.mariadb.org/browse/MXS-4457) Duplicate values in `servers` are silently ignored

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../mariadb-maxscale-23-08-about/mariadb-maxscale-2308-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the supported Linux distributions.

Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is `maxscale-X.Y.Z`. Further, the default branch is always the latest GA version\
of MaxScale.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

CC BY-SA / Gnu FDL
