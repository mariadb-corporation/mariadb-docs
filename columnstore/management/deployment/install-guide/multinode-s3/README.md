---
description: >-
  Multi-node MariaDB ColumnStore deployment with S3 object storage:
  HA topology with three or more nodes, MaxScale routing, CMAPI cluster
  management, and bulk data import.

---

# Multi-Node S3

This procedure describes the deployment of a Multi-Node ColumnStore topology with Object Storage (S3). This High Availability (HA) configuration delivers production-grade analytics with fault tolerance and scalable storage by leveraging S3-compatible object storage for data and a distributed proxy layer.

The topology consists of:

* One or more MariaDB MaxScale nodes to monitor health and route queries.
* An odd number of ColumnStore nodes (minimum of 3) running MariaDB Enterprise Server, ColumnStore, and the Cluster Management API (CMAPI).
* S3-compatible object storage for data.
* Shared local storage (e.g., NFS, EBS Multi-Attach) for the Storage Manager metadata directory.

{% include "../../../../.gitbook/includes/the-instructions-were-teste....md" %}

## Procedure

The procedure has 5 steps, each on its own page. Follow them in order:

1. [Step 1: Prepare Systems for ColumnStore Nodes](step-1-prepare-systems-for-enterprise-columnstore-nodes.md)
2. [Step 2: Install ColumnStore](step-2-install-enterprise-columnstore.md)
3. [Step 3: Start and Configure ColumnStore](step-3-start-and-configure-enterprise-columnstore.md)
4. [Step 4: Test ColumnStore](step-4-test-enterprise-columnstore.md)
5. [Step 5: Bulk Import of Data](step-5-bulk-import-of-data.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
