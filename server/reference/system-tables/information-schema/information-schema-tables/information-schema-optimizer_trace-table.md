---
description: >-
  The Information Schema OPTIMIZER_TRACE table contains details about the
  optimizer's decision-making process for the last executed query.
---

# Information Schema OPTIMIZER\_TRACE Table

## Description

The [Information Schema](../) `OPTIMIZER_TRACE` table contains [Optimizer Trace](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/wIjY1kOpUvbr3Rbr8GXl) information.

It contains the following columns:

| Column                                 | Description                                                                                                                                                    |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QUERY                                  | Displays the query that was asked to be traced.                                                                                                                |
| TRACE                                  | A JSON document displaying the stats we collected when the query was run.                                                                                      |
| MISSING\_BYTES\_BEYOND\_MAX\_MEM\_SIZE | For huge trace, where the trace is truncated due to the optimizer\_trace\_max\_mem\_size limit being reached, displays the bytes that are missing in the trace |
| INSUFFICENT\_PRIVILEGES                | Set to 1 if the user running the trace does not have the privileges to see the trace.                                                                          |

Structure:

```sql
SHOW CREATE TABLE INFORMATION_SCHEMA.OPTIMIZER_TRACE \G
*************************** 1. row ***************************
       Table: OPTIMIZER_TRACE
Create Table: CREATE TEMPORARY TABLE `OPTIMIZER_TRACE` (
  `QUERY` longtext NOT NULL DEFAULT '',
  `TRACE` longtext NOT NULL DEFAULT '',
  `MISSING_BYTES_BEYOND_MAX_MEM_SIZE` int(20) NOT NULL DEFAULT 0,
  `INSUFFICIENT_PRIVILEGES` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=Aria DEFAULT CHARSET=utf8 PAGE_CHECKSUM=0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
