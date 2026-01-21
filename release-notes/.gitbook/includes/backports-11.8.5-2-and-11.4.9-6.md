---
title: backports-11.8.5-2-and-11.4.9-6
---

* Log write buffering added to the [SERVER\_AUDIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) and [SERVER\_AUDIT2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit) plugins ([MENT-2438](https://jira.mariadb.org/browse/MENT-2438))
  * The buffering is controlled by the added variables:
    * `server_audit_file_buffer_size` - defines the size of the buffer. The default value is 0 meaning there's no buffering at all. Setting non-zero value enables the buffering with the buffer of the specified size aligned by 8192. The maximum value is 65536.
    * `server_audit_sync_log_file` - flushes the buffer to the log file. While the log record is in the buffer, it cannot be seen in the log file. And if there are not many events to log, the time before records can be observed can be significant. So user can do `SET GLOBAL server_audit_log_file=1` to this variable to force write the buffer to the file, to make sure he doesn't miss the recent records.
* Two new fields are available via `SHOW REPLICA STATUS` ([MENT-2129](https://jira.mariadb.org/browse/MENT-2129))
  1. `Connects_Tried`, which provides the number of attempts the replica has made to connect to the primary, and
  2. `Master_Retry_Count`, which provides the number of times the replica will attempt to connect to a primary before giving up.
* The authentication plugin `caching_sha2_password` has been added, not loaded by default ([MDEV-37600](https://jira.mariadb.org/browse/MDEV-37600))
