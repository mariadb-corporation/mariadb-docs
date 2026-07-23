---
description: >-
  Backup and restore overview for MariaDB ColumnStore:
  system-of-record planning, full and incremental backup strategies, and the
  components that must be backed up together.
---

# Backup and Restore Overview

## Overview

MariaDB ColumnStore supports backup and restore.

## System of Record

Before you determine a backup strategy for your ColumnStore deployment, it is a good idea to determine the **system of record** for your ColumnStore data.

A system of record is the authoritative data source for a given piece of information. Organizations often store duplicate information in several systems, but only a single system can be the authoritative data source.

ColumnStore is designed to handle analytical processing for OLAP, data warehousing, DSS, and hybrid workloads on very large data sets. Analytical processing does not generally happen on the system of record. Instead, analytical processing generally occurs on a specialized database that is loaded with data from the separate system of record. Additionally, very large data sets can be difficult to back up. Therefore, it may be beneficial to only backup the system of record.

If ColumnStore is not acting as the system of record for your data, you should determine how the system of record affects your backup plan:

* If your system of record is another database server, you should ensure that the other database server is properly backed up and that your organization has procedures to reload ColumnStore from the other database server.
* If your system of record is a set of data files, you should ensure that the set of data files is properly backed up and that your organization has procedures to reload ColumnStore from the set of data files.

## Full Backup and Restore

MariaDB ColumnStore supports full backup and restore for all storage types. A full backup includes:

* ColumnStore's data and metadata

With S3: an S3 snapshot of the [S3-compatible object storage](../../architecture/columnstore-architectural-overview.md#s3-compatible-object-storage-1) and a file system snapshot or copy of the [Storage Manager directory](../../architecture/columnstore-storage-architecture.md#storage-manager-directory) Without S3: a file system snapshot or copy of the [DB Root directories](../../architecture/columnstore-storage-architecture.md#db-root-directories).

* The MariaDB data directory from the primary node

To see the procedure to perform a full backup and restore, choose the storage type:

**[ColumnStore with Object Storage](mariadb-enterprise-columnstore-backup-and-restore-with-object-storage.md)**

```mermaid
flowchart TD
    accTitle: MaxScale routing to a three-node ColumnStore cluster on S3 storage
    accDescr {
        A MaxScale proxy routes client connections to three MariaDB Enterprise
        Server and ColumnStore nodes: one read-write route and two read-only
        routes. All three nodes use a shared S3-compatible object storage
        backend for their table data.
    }
    MX["MariaDB MaxScale"]
    N1[("ES + ColumnStore")]
    N2[("ES + ColumnStore")]
    N3[("ES + ColumnStore")]
    S3[("S3-compatible object storage")]
    MX -->|ro| N1
    MX -->|rw| N2
    MX -->|ro| N3
    S3 -.-> N1
    S3 -.-> N2
    S3 -.-> N3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    class MX,N1,N2,N3,S3 node
```

_MaxScale routes read/write traffic to three ES + ColumnStore nodes backed by S3-compatible object storage._

**[ColumnStore with Shared Local Storage](../../architecture/columnstore-architectural-overview.md#enterprise-columnstore-with-shared-local-storage)**

```mermaid
flowchart TD
    accTitle: MaxScale routing to a three-node ColumnStore cluster on NFS shared storage
    accDescr {
        A MaxScale proxy routes client connections to three MariaDB Enterprise
        Server and ColumnStore nodes: one read-write route and two read-only
        routes. All three nodes share their table data over an NFS shared
        storage backend.
    }
    MX["MariaDB MaxScale"]
    N1[("ES + ColumnStore")]
    N2[("ES + ColumnStore")]
    N3[("ES + ColumnStore")]
    NFS[("NFS shared storage")]
    MX -->|ro| N1
    MX -->|rw| N2
    MX -->|ro| N3
    NFS -.-> N1
    NFS -.-> N2
    NFS -.-> N3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    class MX,N1,N2,N3,NFS node
```

_MaxScale routes read/write traffic to three ES + ColumnStore nodes backed by NFS shared storage._

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
