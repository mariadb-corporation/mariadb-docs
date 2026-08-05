---
title: backports-11.8.6-3-and-11.4.10-7
---

* [CHECK TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) and [mariadb-check](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check) now support [sequences](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/), backported from MariaDB Community Server 12.0 ([MDEV-22491](https://jira.mariadb.org/browse/MDEV-22491))
  * Previously, checking a sequence returned the note `The storage engine for the table doesn't support check`
  * The check first runs the underlying storage engine's own check, then validates the sequence: the table must hold exactly one row, the sequence options must be in range, and the sequence must not be exhausted
  * A sequence table with no rows reports the error `Fewer than one row in the table` and is flagged as corrupt; a table with more than one row reports the warning `More than one row in the table`
  * Sequence options that are out of range report the error `Sequence 'db.name' has out of range value for options` and flag the table as corrupt
  * An exhausted sequence reports the warning `Sequence 'db.name' has run out`, raised only when `SELECT NEXTVAL` would fail for the same reason
  * The sequence-level checks ignore the `CHECK TABLE` options, so `EXTENDED` and `FOR UPGRADE` validate the sequence exactly as a plain `CHECK TABLE` does
