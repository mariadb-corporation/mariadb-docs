---
title: backports-10.6.24-20
---

* Two new fields are available via `SHOW REPLICA STATUS` ([MENT-2129](https://jira.mariadb.org/browse/MENT-2129))
  1. `Connects_Tried`, which provides the number of attempts the replica has made to connect to the primary, and
  2. `Master_Retry_Count`, which provides the number of times the replica will attempt to connect to a primary before giving up.
* Add the server option `--replicate-rewrite-db` to system variables and SHOW REPLICA STATUS (backport of MDEV-15530) ([MENT-2421](https://jira.mariadb.org/browse/MENT-2421))
* The authentication plugin `caching_sha2_password` has been added, not loaded by default ([MDEV-37600](https://jira.mariadb.org/browse/MDEV-37600))
