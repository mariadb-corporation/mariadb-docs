---
description: >-
  MariaDB functions evaluated as post-processing after MariaDB ColumnStore
  returns data, supported in SELECT projection and ORDER BY only — not
  distributed across PrimProc nodes.
---

# ColumnStore Non-Distributed Post-Processed Functions

## Overview

ColumnStore supports all MariaDB functions that can be used in a post-processing manner where data is returned by ColumnStore first and then MariaDB executes the function on the data returned. The functions are currently supported only in the projection (`SELECT`) and `ORDER BY` portions of the SQL statement.

## See Also

* [ColumnStore Distributed Functions](columnstore-distributed-functions.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
