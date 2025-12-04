# FEDERATED Storage Engine

The FEDERATED Storage Engine is a legacy storage engine no longer being supported. A fork, [FederatedX](../federatedx-storage-engine/) is being actively maintained. Since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), the [CONNECT](../connect/) storage engine also permits accessing a remote database via MySQL or ODBC connection (table types: [MYSQL](../connect/connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md), [ODBC](../connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md)).

The FEDERATED Storage Engine was originally designed to let one access data remotely without using clustering or replication, and perform local queries that automatically access the remote data.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
