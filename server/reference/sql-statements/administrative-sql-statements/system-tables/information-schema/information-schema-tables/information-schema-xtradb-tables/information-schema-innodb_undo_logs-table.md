# Information Schema INNODB\_UNDO\_LOGS Table

**MariaDB** [**5.5.27**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5527-release-notes) **-** [**10.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

The `INNODB_UNDO_LOGS` are a Percona enhancement, introduced in version [MariaDB 5.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5527-release-notes) and removed in 10.0.

The [Information Schema](../../) `INNODB_UNDO_LOGS` table is a Percona enchancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](../../../../../../../server-usage/storage-engines/innodb/)). It contains information about the InnoDB [undo log](../../../../../../../server-usage/storage-engines/innodb/innodb-undo-log.md), with each record being an undo log segment. It was removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).

It has the following columns:

| Column        | Description                                                                                                                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column        | Description                                                                                                                                                                                                                                                                 |
| TRX\_ID       | Unique transaction ID number, matching the value from the [information\_schema.INNODB\_TRX](../information-schema-innodb-tables/information-schema-innodb_trx-table.md) table.                                                                                              |
| RSEG\_ID      | Rollback segment ID, matching the value from the information\_schema.INNODB\_RSEG table.                                                                                                                                                                                    |
| USEG\_ID      | Undo segment ID.                                                                                                                                                                                                                                                            |
| SEGMENT\_TYPE | Indicates the operation type, for example INSERT or UPDATE.                                                                                                                                                                                                                 |
| STATE         | Segment state; one of ACTIVE (contains active transaction undo log), CACHED, TO\_FREE (insert undo segment can be freed), TO\_PURGE (update undo segment won't be re-used and can be purged when all undo data is removed) or PREPARED (segment of a prepared transaction). |
| SIZE          | Size in pages of the segment.                                                                                                                                                                                                                                               |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
