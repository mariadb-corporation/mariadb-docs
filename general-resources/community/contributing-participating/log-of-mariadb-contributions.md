# Log of MariaDB Contributions

### How to Document Contributions

Add the following in the global comment for each contribution:

```bash
Patch: Name, url or where we got patch
Author:   ....
License:  MCA or BSD
Reviewer: ....
```

For those cases this is not done, please add to this page a short line for each\
push into MariaDB that includes code from contributors not employed by the MariaDB Foundation or the MariaDB Corporation. The purpose of this is to properly track that all such patches are submitted either under [MCA](../community/legal-documents/mca.md) or BSD-new and to ensure that the developer gets credit for his work.

Example:

```bash
Feature/Patch name
* Author(s)
* Author has signed MCA on "date" | Patch was licensed under BSD
```

(Please enhance the example with anything that makes sense.)

### [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/what-is-mariadb-117) Log of Contributions

* [MariaDB 11.7.1 contributors](https://mariadb.org/mariadb-11-6-2-and-mariadb-11-7-1-now-available/)

### [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/what-is-mariadb-116) Log of Contributions

* [MariaDB 11.6.2 contributors](https://mariadb.org/mariadb-11-6-2-and-mariadb-11-7-1-now-available/)
* [MariaDB 11.6.1 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)

### [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) Log of Contributions

* [MariaDB 11.5.2 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 11.5.1 contributors](https://mariadb.org/mariadb-11-4-2-and-mariadb-11-5-1-now-available/)

### [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114) Log of Contributions

* [MariaDB 11.4.5 contributors](https://mariadb.org/mariadb-11-4-5-10-11-11-10-6-21-and-10-5-28-now-available/)
* [MariaDB 11.4.4 contributors](https://mariadb.org/mariadb-11-4-4-11-2-6-10-11-10-10-6-20-and-10-5-27-now-available/)
* [MariaDB 11.4.3 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 11.4.2 contributors](https://mariadb.org/mariadb-11-4-2-and-mariadb-11-5-1-now-available/)
* [MariaDB 11.4.1 contributors](https://mariadb.org/mariadb-11-4-1-11-3-2-now-available/)
* [Binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) writing speed was improved by moving checksum calculations out of the global binlog mutex. This is a contribution by Kristian Nielsen ([MDEV-31273](https://jira.mariadb.org/browse/MDEV-31273))
* New system variable [max\_binlog\_total\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#max_binlog_total_size) enables binary log purging when the total size of all binary logs exceeds the specified threshold. The implementation is based on the patch from Percona ([MDEV-31404](https://jira.mariadb.org/browse/MDEV-31404))
* FULL\_NODUP is a new value for the [binlog\_row\_image system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_image). It essentially works like FULL, that is all columns are included in the event, but it takes less space, because the after image omits columns that were not changed by the UPDATE statement, and have same values as in the before image. This is a contribution from Alibaba ([MDEV-32589](https://jira.mariadb.org/browse/MDEV-32589))

### [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/what-is-mariadb-113) Log of Contributions

* [MariaDB 11.3.2 contributors](https://mariadb.org/mariadb-11-4-1-11-3-2-now-available/)
* [MariaDB 11.3.1 contributors](https://mariadb.org/mariadb-11-3-1-11-2-2-now-available/)

### [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/what-is-mariadb-112) Log of Contributions

* [MariaDB 11.2.6 contributors](https://mariadb.org/mariadb-11-4-4-11-2-6-10-11-10-10-6-20-and-10-5-27-now-available/)
* [MariaDB 11.2.5 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 11.2.4 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 11.2.3 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 11.2.2 contributors](https://mariadb.org/mariadb-11-3-1-11-2-2-now-available/)
* [MariaDB 11.2.1 contributors](https://mariadb.org/mariadb-11-2-1-11-1-2-now-available/)

### [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111) Log of Contributions

* [MariaDB 11.1.6 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 11.1.5 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 11.1.4 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 11.1.3 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 11.1.2 contributors](https://mariadb.org/mariadb-11-2-1-11-1-2-now-available/)
* [MariaDB 11.1.1 contributors](https://mariadb.org/mariadb-11-1-1-11-0-2-now-available/)

### [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) Log of Contributions

* [MariaDB 11.0.6 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 11.0.5 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 11.0.4 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 11.0.3 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 11.0.2 contributors](https://mariadb.org/mariadb-11-1-1-11-0-2-now-available/)
* [MariaDB 11.0.1 contributors](https://mariadb.org/mariadb-11-0-1-rc-short-term-support-now-available/)

### [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011) Log of Contributions

* [MariaDB 10.11.11 contributors](https://mariadb.org/mariadb-11-4-5-10-11-11-10-6-21-and-10-5-28-now-available/)
* [MariaDB 10.11.10 contributors](https://mariadb.org/mariadb-11-4-4-11-2-6-10-11-10-10-6-20-and-10-5-27-now-available/)
* [MariaDB 10.11.9 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 10.11.8 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 10.11.7 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 10.11.6 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 10.11.5 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.11.4 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.11.3 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.11.2 contributors](https://mariadb.org/mariadb-10-11-2-ga-now-available/)
* [MariaDB 10.11.1 contributors](https://mariadb.org/mariadb-10-11-1-rc-and-10-10-2-ga-now-available/)

### [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010) Log of Contributions

* [MariaDB 10.10.7 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 10.10.6 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.10.5 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.10.4 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.10.2 contributors](https://mariadb.org/mariadb-10-11-1-rc-and-10-10-2-ga-now-available/)
* [MariaDB 10.10.3 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.10.1 contributors](https://mariadb.org/mariadb-10-10-1-rc-and-10-9-2-ga-now-available/)

### [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109) Log of Contributions

* [MariaDB 10.9.8 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.9.7 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.9.6 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.9.5 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.9.4 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.9.3 contributors](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/)
* [MariaDB 10.9.2 contributors](https://mariadb.org/mariadb-10-10-1-rc-and-10-9-2-ga-now-available/)
* [MariaDB 10.9.1 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)

### [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108) Log of Contributions

* [MariaDB 10.8.8 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.8.7 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.8.6 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.8.5 contributors](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/)
* [MariaDB 10.8.4 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.8.3 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.8.2 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.8.1 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)

### [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107) Log of Contributions

* [MariaDB 10.7.8 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.7.7 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.7.6 contributors](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/)
* [MariaDB 10.7.5 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.7.4 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.7.3 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.7.2 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.7.1 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)

### [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106) Log of Contributions

* [MariaDB 10.6.21 contributors](https://mariadb.org/mariadb-11-4-5-10-11-11-10-6-21-and-10-5-28-now-available/)
* [MariaDB 10.6.20 contributors](https://mariadb.org/mariadb-11-4-4-11-2-6-10-11-10-10-6-20-and-10-5-27-now-available/)
* [MariaDB 10.6.19 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 10.6.18 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 10.6.17 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 10.6.16 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 10.6.15 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.6.14 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.6.13 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.6.12 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.6.11 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.6.10 contributors](https://mariadb.org/mariadb-10-9-3-10-8-5-10-7-6-and-10-6-10-now-available/)
* [MariaDB 10.6.9 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.6.8 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.6.7 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.6.6 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.6.5 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)
* [MariaDB 10.6.4 contributors](https://mariadb.org/mariadb-10-6-4-10-5-12-10-4-21-10-3-31-and-10-2-40-now-available/)
* [MariaDB 10.6.3 contributors](https://mariadb.org/mariadb-10-6-3-ga-now-available/)
* [MariaDB 10.6.2 contributors](https://mariadb.org/mariadb-10-6-2-now-available/)
* [MariaDB 10.6.1 contributors](https://mariadb.org/mariadb-10-6-1-now-available/)
* [MariaDB 10.6.0 contributors](https://mariadb.org/mariadb-10-6-0-now-available/)

### [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) Log of Contributions

* [MariaDB 10.5.28 contributors](https://mariadb.org/mariadb-11-4-5-10-11-11-10-6-21-and-10-5-28-now-available/)
* [MariaDB 10.5.27 contributors](https://mariadb.org/mariadb-11-4-4-11-2-6-10-11-10-10-6-20-and-10-5-27-now-available/)
* [MariaDB 10.5.26 contributors](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/)
* [MariaDB 10.5.25 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 10.5.24 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 10.5.23 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 10.5.22 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.5.21 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.5.20 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.5.19 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.5.18 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.5.17 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.5.16 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.5.15 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.5.14 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.5.13 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)
* [MariaDB 10.5.12 contributors](https://mariadb.org/mariadb-10-6-4-10-5-12-10-4-21-10-3-31-and-10-2-40-now-available/)
* [MariaDB 10.5.11 contributors](https://mariadb.org/mariadb-10-5-11-10-4-20-10-3-30-and-10-2-39-now-available/)
* [MariaDB 10.5.10 contributors](https://mariadb.org/mariadb-10-5-10-10-4-19-10-3-29-and-10-2-38-now-available/)
* [MariaDB 10.5.9 contributors](https://mariadb.org/mariadb-10-5-9-10-4-18-10-3-28-and-10-2-37-now-available/)
* [MariaDB 10.5.8 contributors](https://mariadb.org/mariadb-10-5-8-10-4-17-10-3-27-and-10-2-36-now-available/)
* [MariaDB 10.5.7 contributors](https://mariadb.org/mariadb-10-5-7-10-4-16-10-3-26-10-2-35-and-10-1-48-now-available/)
* [MariaDB 10.5.6 contributors](https://mariadb.org/mariadb-10-5-6-10-4-15-10-3-25-10-2-34-and-10-1-47-now-available/)
* [MariaDB 10.5.5 contributors](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/)
* [MariaDB 10.5.4 contributors](https://mariadb.org/mariadb-10-5-4-now-available/)
* [MariaDB 10.5.3 contributors](https://mariadb.org/mariadb-10-5-3-release-candidate-now-available/)
* [MariaDB 10.5.2 contributors](https://mariadb.org/mariadb-10-5-2-now-available/)
* [MariaDB 10.5.1 contributors](https://mariadb.org/mariadb-10-5-1-now-available/)
* [MariaDB 10.5.0 contributors](https://mariadb.org/mariadb-10-5-0-now-available/)

### [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) Log of Contributions

* [MariaDB 10.4.34 contributors](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/)
* [MariaDB 10.4.33 contributors](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/)
* [MariaDB 10.4.32 contributors](https://mariadb.org/mariadb-11-1-3-11-0-4-10-11-6-10-10-7-10-6-16-10-5-23-10-4-32-now-available/)
* [MariaDB 10.4.31 contributors](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/)
* [MariaDB 10.4.30 contributors](https://mariadb.org/mariadb-10-11-4-10-10-5-10-9-7-10-6-14-10-5-21-10-4-30-now-available/).
* [MariaDB 10.4.29 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.4.28 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.4.27 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.4.26 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.4.25 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.4.24 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.4.23 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.4.23 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.4.22 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)
* [MariaDB 10.4.21 contributors](https://mariadb.org/mariadb-10-6-4-10-5-12-10-4-21-10-3-31-and-10-2-40-now-available/)
* [MariaDB 10.4.20 contributors](https://mariadb.org/mariadb-10-5-11-10-4-20-10-3-30-and-10-2-39-now-available/)
* [MariaDB 10.4.19 contributors](https://mariadb.org/mariadb-10-5-10-10-4-19-10-3-29-and-10-2-38-now-available/)
* [MariaDB 10.4.18 contributors](https://mariadb.org/mariadb-10-5-9-10-4-18-10-3-28-and-10-2-37-now-available/)
* [MariaDB 10.4.17 contributors](https://mariadb.org/mariadb-10-5-8-10-4-17-10-3-27-and-10-2-36-now-available/)
* [MariaDB 10.4.16 contributors](https://mariadb.org/mariadb-10-5-7-10-4-16-10-3-26-10-2-35-and-10-1-48-now-available/)
* [MariaDB 10.4.15 contributors](https://mariadb.org/mariadb-10-5-6-10-4-15-10-3-25-10-2-34-and-10-1-47-now-available/)
* [MariaDB 10.4.14 contributors](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/)
* [MariaDB 10.4.13 contributors](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available)
* [MariaDB 10.4.12 contributors](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/)
* [MariaDB 10.4.11 contributors](https://mariadb.org/mariadb-10-4-11-10-3-21-and-10-2-30-now-available/)
* [MariaDB 10.4.10 contributors](https://mariadb.org/mariadb-10-4-10-10-3-20-10-2-29-and-10-1-43-now-available/)
* [MariaDB 10.4.9 contributors](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/)
* [MariaDB 10.4.8 contributors](https://mariadb.org/mariadb-10-4-8-10-3-18-and-10-2-27-now-available/)
* [MariaDB 10.4.7 contributors](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/)
* [MariaDB 10.4.6 contributors](https://mariadb.org/mariadb-10-4-6-first-stable-10-4-release-and-mariadb-connector-j-2-4-2-now-available/)
* [MariaDB 10.4.5 contributors](https://mariadb.org/mariadb-10-4-5-now-available/)
* [MariaDB 10.4.4 contributors](https://mariadb.org/mariadb-10-4-4-now-available/)
* [MariaDB 10.4.3 contributors](https://mariadb.org/mariadb-10-4-3-now-available/)
* [MariaDB 10.4.2 contributors](https://mariadb.org/mariadb-10-4-2-now-available/)
* [MariaDB 10.4.1 contributors](https://mariadb.org/mariadb-10-4-1-and-mariadb-connector-node-js-2-0-2-now-available/)
* [MariaDB 10.4.0 contributors](https://mariadb.org/first-mariadb-10-4-alpha-release/)

### [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) Log of Contributions

[Instant ADD COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb) ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369))

* Tencent Game DBA Team, developed by vinchen.

[UPDATE statements with the same source and target](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update#update-statements-with-the-same-source-and-target) ([MDEV-12874](https://jira.mariadb.org/browse/MDEV-12874))

* Jerome Brauge.

Per-engine mysql.gtid\_slave\_pos tables ([MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179))

* Kristian Nielsen funded by Booking.com.

The MariaDB Foundation website provides a more detailed list of contributors by release, starting from [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.5)

* [MariaDB 10.3.39 contributors](https://mariadb.org/mariadb-10-11-3-10-10-4-10-9-6-10-8-8-10-6-13-10-5-20-10-4-29-and-10-3-39-now-available/)
* [MariaDB 10.3.38 contributors](https://mariadb.org/mariadb-10-10-3-10-9-5-10-8-7-10-7-8-10-6-12-10-5-19-10-4-28-and-10-3-38-now-available/)
* [MariaDB 10.3.37 contributors](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/)
* [MariaDB 10.3.36 contributors](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/)
* [MariaDB 10.3.35 contributors](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/)
* [MariaDB 10.3.34 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.3.33 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.3.32 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)
* [MariaDB 10.3.31 contributors](https://mariadb.org/mariadb-10-6-4-10-5-12-10-4-21-10-3-31-and-10-2-40-now-available/)
* [MariaDB 10.3.30 contributors](https://mariadb.org/mariadb-10-5-11-10-4-20-10-3-30-and-10-2-39-now-available/)
* [MariaDB 10.3.29 contributors](https://mariadb.org/mariadb-10-5-10-10-4-19-10-3-29-and-10-2-38-now-available/)
* [MariaDB 10.3.28 contributors](https://mariadb.org/mariadb-10-5-9-10-4-18-10-3-28-and-10-2-37-now-available/)
* [MariaDB 10.3.27 contributors](https://mariadb.org/mariadb-10-5-8-10-4-17-10-3-27-and-10-2-36-now-available/)
* [MariaDB 10.3.26 contributors](https://mariadb.org/mariadb-10-5-7-10-4-16-10-3-26-10-2-35-and-10-1-48-now-available/)
* [MariaDB 10.3.25 contributors](https://mariadb.org/mariadb-10-5-6-10-4-15-10-3-25-10-2-34-and-10-1-47-now-available/)
* [MariaDB 10.3.24 contributors](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/)
* [MariaDB 10.3.23 contributors](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available)
* [MariaDB 10.3.22 contributors](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/)
* [MariaDB 10.3.21 contributors](https://mariadb.org/mariadb-10-4-11-10-3-21-and-10-2-30-now-available/)
* [MariaDB 10.3.20 contributors](https://mariadb.org/mariadb-10-4-10-10-3-20-10-2-29-and-10-1-43-now-available/)
* [MariaDB 10.3.19 contributors](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/)
* [MariaDB 10.3.18 contributors](https://mariadb.org/mariadb-10-4-8-10-3-18-and-10-2-27-now-available/)
* [MariaDB 10.3.17 contributors](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/)
* [MariaDB 10.3.16 contributors](https://mariadb.org/mariadb-10-3-16-and-mariadb-10-2-25-now-available/)
* [MariaDB 10.3.15 contributors](https://mariadb.org/mariadb-10-3-15-mariadb-connector-c-3-0-10-mariadb-connector-node-js-2-0-5-and-mariadb-connector-odbc-3-1-1-now-available/)
* [MariaDB 10.3.14 contributors](https://mariadb.org/mariadb-10-3-14-now-available/)
* [MariaDB 10.3.13 contributors](https://mariadb.org/mariadb-10-3-13-and-mariadb-connector-c-3-0-9-now-available/)
* [MariaDB 10.3.12 contributors](https://mariadb.org/mariadb-10-3-12-and-mariadb-connector-c-3-0-8-now-available/)
* [MariaDB 10.3.11 contributors](https://mariadb.org/mariadb-10-3-11-and-mariadb-connector-c-3-0-7-connector-odbc-3-0-7-and-connector-node-js-2-0-1-now-available/)
* [MariaDB 10.3.10 contributors](https://mariadb.org/mariadb-10-3-10-now-available/)
* [MariaDB 10.3.9 contributors](https://mariadb.org/mariadb-10-3-9-now-available/)
* [MariaDB 10.3.8 contributors](https://mariadb.org/mariadb-10-3-8-now-available/)
* [MariaDB 10.3.7 contributors](https://mariadb.org/mariadb-10-3-7-now-available/)
* [MariaDB 10.3.6 contributors](https://mariadb.org/mariadb-10-3-6-now-available/)
* [MariaDB 10.3.5 contributors](https://mariadb.org/mariadb-10-3-5-mariadb-connector-j-2-2-2-1-7-2-now-available/)

### [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) Log of Contributions

New variable [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) permits restricting the speed at which the slave reads the binlog from the master ([MDEV-11064](https://jira.mariadb.org/browse/MDEV-11064))

* Tencent Game DBA Team, developed by chouryzhou.

[Compression of events in the binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log) ([MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065))

* Tencent Game DBA Team, developed by vinchen.

[No Pad collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) ([MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711))

* Daniil Medvedev

[Flashback](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/flashback)

* Lixun Peng, Alibaba

Implement non-recursive common table expressions ([MDEV-8789](https://jira.mariadb.org/browse/MDEV-8789))\
Implement recursive common table expressions ([MDEV-9864](https://jira.mariadb.org/browse/MDEV-9864))\
Pushdown conditions into non-mergeable views/derived tables ([MDEV-9197](https://jira.mariadb.org/browse/MDEV-9197))

* Galina Shalygina

Backporting Delayed replication ([MDEV-7145](https://jira.mariadb.org/browse/MDEV-7145)) from MySQL 5.6

* Kristian Nielsen funded by Booking.com

The MariaDB Foundation website provides a more detailed list of contributors by release, starting from [MariaDB 10.2.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.14)

* [MariaDB 10.2.43 contributors](https://mariadb.org/mariadb-10-8-2-rc-and-mariadb-10-7-3-10-6-7-10-5-15-10-4-24-10-3-34-and-10-2-43-now-available/)
* [MariaDB 10.2.42 contributors](https://mariadb.org/mariadb-10-8-1-rc-and-mariadb-10-7-2-10-6-6-10-5-14-10-4-23-10-3-33-and-10-2-42-now-available/)
* [MariaDB 10.2.41 contributors](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/)
* [MariaDB 10.2.40 contributors](https://mariadb.org/mariadb-10-6-4-10-5-12-10-4-21-10-3-31-and-10-2-40-now-available/)
* [MariaDB 10.2.39 contributors](https://mariadb.org/mariadb-10-5-11-10-4-20-10-3-30-and-10-2-39-now-available/)
* [MariaDB 10.2.38 contributors](https://mariadb.org/mariadb-10-5-10-10-4-19-10-3-29-and-10-2-38-now-available/)
* [MariaDB 10.2.37 contributors](https://mariadb.org/mariadb-10-5-9-10-4-18-10-3-28-and-10-2-37-now-available/)
* [MariaDB 10.2.36 contributors](https://mariadb.org/mariadb-10-5-8-10-4-17-10-3-27-and-10-2-36-now-available/)
* [MariaDB 10.2.35 contributors](https://mariadb.org/mariadb-10-5-7-10-4-16-10-3-26-10-2-35-and-10-1-48-now-available/)
* [MariaDB 10.2.34 contributors](https://mariadb.org/mariadb-10-5-6-10-4-15-10-3-25-10-2-34-and-10-1-47-now-available/)
* [MariaDB 10.2.33 contributors](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/)
* [MariaDB 10.2.32 contributors](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available)
* [MariaDB 10.2.31 contributors](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/)
* [MariaDB 10.2.30 contributors](https://mariadb.org/mariadb-10-4-11-10-3-21-and-10-2-30-now-available/)
* [MariaDB 10.2.29 contributors](https://mariadb.org/mariadb-10-4-10-10-3-20-10-2-29-and-10-1-43-now-available/)
* [MariaDB 10.2.28 contributors](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/)
* [MariaDB 10.2.27 contributors](https://mariadb.org/mariadb-10-4-8-10-3-18-and-10-2-27-now-available/)
* [MariaDB 10.2.26 contributors](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/)
* [MariaDB 10.2.25 contributors](https://mariadb.org/mariadb-10-3-16-and-mariadb-10-2-25-now-available/)
* [MariaDB 10.2.24 contributors](https://mariadb.org/mariadb-10-2-24-now-available/)
* [MariaDB 10.2.23 contributors](https://mariadb.org/mariadb-10-2-23-and-mariadb-connector-j-2-4-1-now-available/)
* [MariaDB 10.2.22 contributors](https://mariadb.org/mariadb-10-2-22-now-available/)
* [MariaDB 10.2.21 contributors](https://mariadb.org/mariadb-10-2-21-now-available/)
* [MariaDB 10.2.20 contributors](https://mariadb.org/mariadb-10-2-20-and-mariadb-connector-c-3-0-8-now-available/)
* [MariaDB 10.2.19 contributors](https://mariadb.org/mariadb-10-2-19-now-available)
* [MariaDB 10.2.18 contributors](https://mariadb.org/mariadb-10-2-18-and-mariadb-connector-node-js-2-0-0-now-available/)
* [MariaDB 10.2.17 contributors](https://mariadb.org/mariadb-10-2-17-now-available/)
* [MariaDB 10.2.16 contributors](https://mariadb.org/mariadb-10-2-16-now-available/)
* [MariaDB 10.2.15 contributors](https://mariadb.org/mariadb-10-2-15-and-mariadb-connector-j-2-2-4-now-available/)
* [MariaDB 10.2.14 contributors](https://mariadb.org/mariadb-10-2-14-mariadb-10-1-32-and-mariadb-connector-j-2-2-3-and-1-7-3-now-available/)

### [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) Log of Contributions

[Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), optimizer, security, speed enhancements, bug fixing, etc

* [MariaDB Corporation](https://mariadb.com)

Power8 optimization

* [MariaDB Foundation](https://mariadb.org)
* Stewart Smith
* In cooperation with IBM

[Documentation](https://mariadb.com/kb)

* [MariaDB Foundation](https://mariadb.org)

[Query timeouts](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/query-limits-and-timeouts)

* [MariaDB Foundation](https://mariadb.org)

[Character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/setting-character-sets-and-collations) enhancements and speedups

* [MariaDB Foundation](https://mariadb.org)

[Upgraded regexp library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre)

* [MariaDB Foundation](https://mariadb.org)

Reviews for [replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption), compression, [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/), [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) storage engine, [Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) storage engine, [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider), [OR REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create) etc.

* [MariaDB Foundation](https://mariadb.org)

[Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption), scrubbing, enhanced semisync, dump thread enhancements, thd\_specifics plugin service

* Google

Table level [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption), [plugin for secure encryption](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/encryption-plugins)

* [Eperi GmbH](https://eperi.de/)

[Defragmentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces), online alter progress monitoring

* [Kakao Inc](https://www.kakao.com)

[Galera (wsrep patches)](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/)

* [Codership](https://galeracluster.com/)

[Compound statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements)

* Antony Curtis

[CREATE OR REPLACE/IF NOT EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create)

* Sriram Patil

New [status variables for replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables)

* Daniel Black

[RESET MASTER TO #](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master)

* Daniël van Eeden

Atomic writes, page compression, trim, multi-threaded flush for XtraDB/InnoDB

* In cooperation with FusionIO

The MariaDB Foundation website provides a more detailed list of contributors by release, starting from [MariaDB 10.1.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.32)

* [MariaDB 10.1.48 contributors](https://mariadb.org/mariadb-10-5-7-10-4-16-10-3-26-10-2-35-and-10-1-48-now-available/)
* [MariaDB 10.1.47 contributors](https://mariadb.org/mariadb-10-5-6-10-4-15-10-3-25-10-2-34-and-10-1-47-now-available/)
* [MariaDB 10.1.46 contributors](https://mariadb.org/mariadb-10-5-5-10-4-14-10-3-24-10-2-33-and-10-1-46-now-available/)
* [MariaDB 10.1.45 contributors](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available)
* [MariaDB 10.1.44 contributors](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/)
* [MariaDB 10.1.43 contributors](https://mariadb.org/mariadb-10-4-10-10-3-20-10-2-29-and-10-1-43-now-available/)
* [MariaDB 10.1.42 contributors](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/)
* [MariaDB 10.1.41 contributors](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/)
* [MariaDB 10.1.40 contributors](https://mariadb.org/mariadb-10-1-40-now-available/)
* [MariaDB 10.1.39 contributors](https://mariadb.org/mariadb-10-1-39-now-available/)
* [MariaDB 10.1.38 contributors](https://mariadb.org/mariadb-10-1-38-now-available/)
* [MariaDB 10.1.37 contributors](https://mariadb.org/mariadb-10-1-37-now-available/)
* [MariaDB 10.1.36 contributors](https://mariadb.org/mariadb-10-1-36-and-mariadb-connector-c-2-3-7-connector-j-2-3-0-and-connector-odbc-2-0-18-now-available/)
* [MariaDB 10.1.35 contributors](https://mariadb.org/mariadb-10-1-35-and-mariadb-galera-cluster-10-0-36-now-available/)
* [MariaDB 10.1.34 contributors](https://mariadb.org/mariadb-10-1-34-and-latest-mariadb-connectors-now-available/)
* [MariaDB 10.1.33 contributors](https://mariadb.org/mariadb-10-1-33-and-mariadb-galera-cluster-10-0-35-now-available/)
* [MariaDB 10.1.32 contributors](https://mariadb.org/mariadb-10-2-14-mariadb-10-1-32-and-mariadb-connector-j-2-2-3-and-1-7-3-now-available/)

#### Also Used Code Snippets by

Facebook

* Defragmentation, prefix index queries optimization, lazy flushing, buffer pool list scan optimization, configurable long semaphore wait timeout

Percona

* [SET STATEMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-statement), [enforce\_storage\_engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#enforce_storage_engine)

Oracle

* [UNION ALL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/union) optimization, [default\_tmp\_storage\_engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#default_tmp_storage_engine)

### [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0) Log of Contributions

Per thread memory counting and usage

* Base code and idea by Lixun Peng, Taobao
* License: BSD

[Multi-source replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication)

* Base code by Lixun Peng, Taobao
* License: BSD

[GET\_LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/get_lock)

* Code by Konstantin "Kostja" Osipov, mail.ru
* License: BSD

[CONNECT storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect)

* Code by Olivier Bertrand
* License: GPL

[Spider storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)[metadata\_lock\_info Information schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table)

* Code by Kentoku Shiba, Spiral Arms
* License: GPL

[Roles](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/roles/roles_overview)

* Code by Vicentiu Ciorbaru, Google Summer of Code 2013
* License: BSD

[PCRE Regular Expressions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre)

* Code by Sudheera Palihakkara, Google Summer of Code 2013
* License: BSD

[Global Transaction IDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)

* Some patches by Pavel Ivanov, Google

The MariaDB Foundation website provides a more detailed list of contributors by release, starting from [MariaDB 10.0.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.35)

* [MariaDB Galera Cluster 10.0.38 contributors](https://mariadb.org/mariadb-galera-cluster-10-0-38-now-available/)
* [MariaDB 10.0.38 contributors](https://mariadb.org/mariadb-10-0-38-mariadb-connector-j-2-4-0-and-mariadb-connector-node-js-2-0-3-now-available/)
* [MariaDB Galera Cluster 10.0.37 contributors](https://mariadb.org/mariadb-galera-cluster-10-0-37-now-available/)
* [MariaDB 10.0.37 contributors](https://mariadb.org/mariadb-10-0-37-now-available/)
* [MariaDB Galera Cluster 10.0.36 contributors](https://mariadb.org/mariadb-10-1-35-and-mariadb-galera-cluster-10-0-36-now-available/)
* [MariaDB 10.0.36 contributors](https://mariadb.org/mariadb-10-0-36-now-available/)
* [MariaDB Galera Cluster 10.0.35 contributors](https://mariadb.org/mariadb-10-1-33-and-mariadb-galera-cluster-10-0-35-now-available/)
* [MariaDB 10.0.35 contributors](https://mariadb.org/mariadb-10-0-35-mariadb-galera-cluster-5-5-60-and-mariadb-connector-c-3-0-4-now-available/)

### [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) Log of Contributions

Function last\_value() which returns the last value but evaluates all arguments as a side effect.

* Original patch by Eric Herman, Booking.com
* License: BSD

nowatch option for mysqld\_safe (allow systemd)

* Based on code from Maarten Vanraes
* License: BSD

Security fixes, patches

* Work by Honza Horak, Red Hat

Coverity scans

* Work by Christian Convey

The MariaDB Foundation website provides a more detailed list of contributors by release, starting from [MariaDB 5.5.60](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/5.5.60)

* [MariaDB 5.5.68 contributors](https://mariadb.org/mariadb-10-4-13-10-3-23-10-2-32-10-1-45-and-5-5-68-now-available)
* [MariaDB 5.5.67 contributors](https://mariadb.org/mariadb-10-4-12-10-3-22-and-10-2-31-10-1-44-and-5-5-67-now-available/)
* [MariaDB 5.5.66 contributors](https://mariadb.org/mariadb-10-4-9-10-3-19-and-10-2-28-10-1-42-and-5-5-66-now-available/)
* [MariaDB 5.5.65 contributors](https://mariadb.org/mariadb-10-4-7-10-3-17-10-2-26-10-1-41-and-5-5-65-now-available/)
* [MariaDB 5.5.64 contributors](https://mariadb.org/mariadb-5-5-64-now-available/)
* [MariaDB Galera Cluster 5.5.63 contributors](https://mariadb.org/mariadb-galera-cluster-5-5-63-now-available/)
* [MariaDB 5.5.63 contributors](https://mariadb.org/mariadb-5-5-63-now-available/)
* [MariaDB Galera Cluster 5.5.62 contributors](https://mariadb.org/mariadb-galera-cluster-5-5-62-now-available/)
* [MariaDB 5.5.62 contributors](https://mariadb.org/mariadb-5-5-62-now-available/)
* [MariaDB Galera Cluster 5.5.61 contributors](https://mariadb.org/mariadb-galera-cluster-5-5-61-mariadb-connector-c-3-0-6-and-mariadb-connector-odbc-3-0-6-now-available/)
* [MariaDB 5.5.61 contributors](https://mariadb.org/mariadb-5-5-61-mariadb-connector-node-js-0-7-0-and-mariadb-connector-j-2-2-6-now-available/)
* [MariaDB Galera Cluster 5.5.60 contributors](https://mariadb.org/mariadb-10-0-35-mariadb-galera-cluster-5-5-60-and-mariadb-connector-c-3-0-4-now-available/)
* [MariaDB 5.5.60 contributors](https://mariadb.org/mariadb-5-5-60-now-available/)

### [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.2/changes-improvements-in-mariadb-5-2) Log of Contributions

Virtual Columns

* [MySQL\_virtual\_columns\_ref\_manual](https://forge.mysql.com/wiki/MySQL_virtual_columns_ref_manual)
* [mysql-6.0-wl1075-wl411](https://code.launchpad.net/~andrey-zhakov/mysql-server/mysql-6.0-wl1075-wl411)
* Andrey Zhakov (modified by Sanja and Igor)
* Author has [signed MCA](https://lists.askmonty.org/pipermailp/dev/2009-October/000079.html)

Declaring many CHARSET objects as const.

* Antony T Curtis (LinkedIn)
* License: BSD

[Extended user statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics)

* Authors: People at Google, Facebook and Percona. This code owes a special thanks to Mark Callaghan!
* License: BSD

[Segmented MyISAM Key Cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache)

* Fredrik Nylander from Stardoll.com
* License: MCA

The [OQGRAPH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine/installing-oqgraph) storage engine

* [doc](https://openquery.com/graph/doc)
* Created by Arjen Lenz, Open Query
* License GPL

The [Sphinx](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sphinx-storage-engine) storage engine

* [current.html](https://sphinxsearch.com/docs/current.html)
* Created by Andrew Aksyonoff.
* License: GPL

Pluggable Authentication

* RJ Silk\
  License: MCA

Various bug fixes

* Stewart Smith, Percona

### [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/changes-improvements-in-mariadb-5-1) Log of Contributions (Outside of Monty Program Ab)

Microsecond precision in process list

* [microsec\_process.patch](https://www.percona.com/mysql/5.0.77-b13/patches/microsec_process.patch)
* Percona Inc
* Patch was [licensed to Monty Program under BSD (new)](https://lists.askmonty.org/pipermailp/dev/2009-October/000075.html).

Slow Query Log Extened Statistics

* [microslow.patch](https://www.percona.com/mysql/5.1.26/patches/microslow.patch)
* Percona Inc
* Patch was [licensed to Monty Program under BSD (new)](https://lists.askmonty.org/pipermailp/dev/2009-October/000075.html).

The [PBXT storage engine](https://kb.askmonty.org/v/about-pbxt)

*
* Created by Paul McCullagh
* License: GPL

The FederatedX storage engine

* [project.php?id=265](https://forge.mysql.com/projects/project.php?id=265)
* All changes are made by Patrik Galbraith and Antony Curtis and are given to us under BSD-new.
* In addition we are allowed to promote FederatedX.

Windows enhancements and various bug fixes

* Alex Budovski, under MCA

Creating of MariaDB packages

* Arjen Lenz, Open Query

Various bug fixes

* Stewart Smith, Percona

### Sponsored Features

Google has sponsored:

* [Parallel Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication)
* Google tests GTID, parallel replication and lots more on the mailing list

Facebook has sponsored many features, including:

* [LIMIT ROWS EXAMINED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/limit-rows-examined)
* The [non-blocking client library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api/non-blocking-client-library)
* Facebook employees do frequent the mailing list

### See Also

* [SHOW CONTRIBUTORS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-contributors) lists [all members and sponsors of the MariaDB Foundation](https://mariadb.org/en/supporters) and other sponsors.
* [SHOW AUTHORS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-authors) lists the authors of MariaDB (including documentation, QA etc.).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
