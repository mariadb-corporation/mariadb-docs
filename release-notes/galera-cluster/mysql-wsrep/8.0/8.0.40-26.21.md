# MySQL-wsrep 8.0.40-26.21 Release Notes

Changes in MySQL-wsrep 8.0.40-26.21 (2024-12-03)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.40 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.40.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.39-26.20:

* `wsrep_ready` is now atomic
* foreign key checks are skipped in applying during IST, controlled by new `wsrep_mode APPLIER_SKIP_FK_CHECKS_IN_IST` (not on by default)
* node crashes if TOI fails during IST while executing CREATE TABLE due to an unpopped `Strict_error_handler`, fixed by ensuring `thd->pop_internal_handler()` is called before returning
* ALTER TABLE RENAME caused BF ABORT on two nodes due to transactional MDL-locks not being released after an implicit commit failure from a certification error, fixed by ensuring locks are released even when the commit fails
* the SKIP LOCKED option in SELECT FOR UPDATE caused an assertion failure when attempting to lock a supremum record already held by a high-priority transaction, fixed by handling unexpected `DB_SKIP_LOCKED` return codes as `DB_DEADLOCK` to abort the operation
* fix `wsrep_cluster_conf_id` to show correct value (which is not -1 the default, 18446744073709551615)
* fix an assert in SELECT FOR UPDATE SKIP LOCKED
* `wsrep_diag.sql` script was updated to filter out MDL locks on `performance_schema` tables caused by querying the `metadata_locks` table itself
* fix issue of continuing to check multiple foreign key constraints despite an error is resolved by ensuring that `wsrep_row_upd_check_foreign_constraints()` stops further checks and errors out immediately if the error state is not `DB_SUCCESS`.
* watchdog moved into a separate thread to avoid blocking the InnoDB monitor
* fix DROP TABlE IF EXISTS could still be missing certification keys from referenced tables
* refactor Galera MDL-conflict handling by introducing `wsrep_bf_info` to securely store conflict logging data and holding appropriate locks during MDL-conflict logging to ensure thread safety and prevent data changes
* ensure fail-silent semantics during crashes by shutting down Galera networking and suppressing Galera/wsrep logging upon fatal signals, preventing interference with stack traces and core dumping

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
