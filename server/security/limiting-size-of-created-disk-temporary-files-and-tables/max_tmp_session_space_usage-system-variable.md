---
description: >-
  Documentation for the system variable that limits the total size of temporary
  files and temporary tables that a single connection can use.
---

# max\_tmp\_session\_space\_usage System Variable

#### `max_tmp_session_space_usage`

* Description: The maximum total size in bytes of temporary file and temporary table usage for a single connection. Each connection is limited independently: this is not a server-wide limit, and it is not aggregated across the connections of one user account. To cap the total across all connections, use [max\_tmp\_total\_space\_usage](max_tmp_total_space_usage-system-variable.md). A statement that would exceed this limit fails with `Local temporary space limit reached`. A value of 0 disables this feature. Set in blocks of 65536, rounded down if not a multiple of 65536. See [Limiting Size of Created Disk Temporary Files and Tables Overview](limiting-size-of-created-disk-temporary-files-and-tables-overview.md) for details. Named max\_tmp\_space\_usage in [MariaDB 11.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/11.5.0) only.
* Commandline: `--max-tmp-session-space-usage=num`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric` (bigint unsigned)
* Default Value: `1099511627776`
* Range: `0` to `18446744073709551615` (blocks of `65536`)
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
