---
description: >-
  MariaDB Enterprise Server 10.6.28-24 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 10.6, released on TBD
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.28-24

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="10.6.28-24.md" class="button secondary">Release Notes</a> <a class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of Enterprise Server 10.6</a>

<!-- TODO(DOCS-6574): set the release date at publish time. TODO-6192's stated dates
     (internal 30 Jul 2026, public 3 Aug 2026) have both passed; the working date is
     "ASAP". Update here AND in the frontmatter description. -->
**Release date:** TBD

## Issues Fixed

* Hashicorp Key Management plugin improved performance by avoiding calling expensive time retrieval functions ([MENT-2764](https://jira.mariadb.org/browse/MENT-2764))
* A large number of joins in a SELECT can crash the server ([MENT-2788](https://jira.mariadb.org/browse/MENT-2788))
* Backport MDEV-40413 - ALTER TABLE ... CONVERT ... PARTITION doesn't encode partition names ([MENT-2799](https://jira.mariadb.org/browse/MENT-2799))
* Backport MDEV-40058 - cached_sha2_password crashes on zero-length password ([MENT-2804](https://jira.mariadb.org/browse/MENT-2804))
* Backport MDEV-40365 - OOB read for common_header_len & post_header_len on malformed Format_description_log_event ([MENT-2840](https://jira.mariadb.org/browse/MENT-2840))
* Backport MDEV-40366 - OOB read for used_checksum_alg on malformed Format_description_log_event ([MENT-2841](https://jira.mariadb.org/browse/MENT-2841))
* Backport MDEV-39485 - Heap-buffer-overflow in mariadb-binlog upon read in Rows_log_event constructor in sql/log_event.cc ([MENT-2842](https://jira.mariadb.org/browse/MENT-2842))
* A replica could crash when a heartbeat or other event from its master arrived truncated, which can happen when the replication stream is corrupted in transit; the replica trusted the size the truncated event declared and tried to read and allocate far more data than the event held, in some builds nearly 4GB; such an event now stops the replica's IO thread with an error identifying the bad event length ([MENT-2846](https://jira.mariadb.org/browse/MENT-2846))
* Cherry pick MDEV-40645 - Slave Crash on Malformed User_var_log_event ([MENT-2847](https://jira.mariadb.org/browse/MENT-2847))
* Backport MDEV-40647 - Replication Breaks from Mal-copied Binlog Name on Malformed Format_description Event ([MENT-2848](https://jira.mariadb.org/browse/MENT-2848))
* A master could cause a replica to apply the same statement twice and end up with data the master's binary log never contained, by sending an event whose declared size disagrees with the amount of data actually sent; the replica stored such an event in its relay log as received, and a hidden second event in the surplus bytes was later applied as though the master had sent it; the replica now compares the two sizes on arrival, so a mismatched event stops the IO thread with an error and never reaches the relay log; this closes a gap that made a replica's data unverifiable against its master's binary log ([MENT-2849](https://jira.mariadb.org/browse/MENT-2849))
* mariadb_upgrade running when upgrading from community server to same major version of enterprise server ([MENT-1712](https://jira.mariadb.org/browse/MENT-1712))

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
