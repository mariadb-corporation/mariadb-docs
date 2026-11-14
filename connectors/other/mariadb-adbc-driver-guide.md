---
description: >-
  The ADBC driver for MariaDB connects applications to MariaDB through Arrow
  Database Connectivity (ADBC), returning query results as Apache Arrow data.
icon: link
---

# ADBC

## Overview

[ADBC (Arrow Database Connectivity)](https://arrow.apache.org/adbc/) is an Apache Arrow API standard for database access. Unlike row-oriented APIs such as ODBC and JDBC, ADBC exchanges data in the columnar Apache Arrow format, so query results load directly into Arrow-native tools.

The [ADBC driver for MariaDB](https://adbc-drivers.org/drivers/mariadb/) is an open-source driver maintained by the [ADBC Driver Foundry](https://github.com/adbc-drivers). It supports queries, prepared statements, bulk ingestion, transactions, and catalog metadata, as well as MariaDB-specific data types such as `UUID`, `INET4`, `INET6`, and `VECTOR`.

## Installation

Install the driver with [dbc](https://docs.columnar.tech/dbc/):

```bash
dbc install mariadb
```

For connection options, data type mappings, and usage examples, see the [ADBC driver for MariaDB documentation](https://adbc-drivers.org/drivers/mariadb/).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
