---
description: >-
  The Information Schema MROONGA_STATS table provides statistical information
  specific to the Mroonga full-text search storage engine.
---

# Information Schema MROONGA\_STATS Table

The [Information Schema](../) `MROONGA_STATS` table only exists if the [Mroonga](../../../../server-usage/storage-engines/mroonga/) storage engine is installed, and contains information about its activities.

| Column        | Description                                  |
| ------------- | -------------------------------------------- |
| VERSION       | Mroonga version.                             |
| rows\_written | Number of rows written into Mroonga tables.  |
| rows\_read    | Number of rows read from all Mroonga tables. |

This table always contains 1 row.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
