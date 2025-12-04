---
description: >-
  A detailed reference list of specific schema change operations (like adding
  columns or indexes) and their compatibility with INSTANT, INPLACE, and NOCOPY
  algorithms.
---

# InnoDB Schema Changes

## MariaDB Enterprise Server InnoDB Schema Changes with the INPLACE Algorithm

Changes in enterprise databases and applications are inevitable. Schema changes often block other workloads, incur unique production situations that cannot be fully simulated for testing, and may have unpredictable execution times.

MariaDB Enterprise Server includes the In-place `ALTER` functionality for the InnoDB storage engine, such that:

When possible, schema change operations are performed `INPLACE`, minimizing impact on other workloads.

When the `alter_algorithm` system variable is set to `INPLACE`, schema change operations will not run unless they can be performed `INPLACE`, minimizing the risk of unpredictable behavior.

Additional information is available [here](../../innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md).

## MariaDB Enterprise Server InnoDB Schema Changes with the INSTANT Algorithm

Changes in enterprise databases and applications are inevitable. Schema changes often block other workloads, incur unique production situations that cannot be fully simulated for testing, and may have unpredictable execution times.

MariaDB Enterprise Server includes the Instant `ALTER` functionality for the InnoDB storage engine, such that:

When possible, schema change operations are performed `INSTANT`, minimizing impact on other workloads.

When the `alter_algorithm` system variable is set to `INSTANT`, schema change operations will not run unless they can be performed `INSTANT`, minimizing the risk of unpredictable behavior.

Additional information is available [here](../../innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm.md).

## MariaDB Enterprise Server InnoDB Schema Changes with the NOCOPY Algorithm

Changes in enterprise databases and applications are inevitable. Schema changes often block other workloads, incur unique production situations that cannot be fully simulated for testing, and may have unpredictable execution times.

MariaDB Enterprise Server includes the No-copy `ALTER` functionality for the InnoDB storage engine, such that:

When possible, schema change operations are performed `NOCOPY`, minimizing impact on other workloads.

When the alter\_algorithm system variable is set to `NOCOPY`, schema change operations will not run unless they can be performed `NOCOPY`, minimizing the risk of unpredictable behavior.

Additional information is available [here](../../innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
