---
description: >-
  wsrep_certificate_expiration_hours_warning configures Galera Cluster to log a
  warning when the node's wsrep X.509 certificate expires within the given
  number of hours; 0 disables warnings.
---

# wsrep\_certificate\_expiration\_hours\_warning

## Overview <a href="#overview_h2" id="overview_h2"></a>

Print warning about certificate expiration if the X509 certificate used for wsrep connections is about to expire in hours given as an argument. If the value is 0, warnings are not printed.

## Usage

The `wsrep_certificate_expiration_hours_warning` system variable can be set in a configuration file:

```ini
[mariadb]
...
# warn 3 days before certificate expiration
wsrep_certificate_expiration_hours_warning=72
```

The global value of the `wsrep_certificate_expiration_hours_warning` system variable can also be set dynamically at runtime by executing [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session):

```sql
SET GLOBAL wsrep_certificate_expiration_hours_warning=72;
```

When the `wsrep_certificate_expiration_hours_warning` system variable is set dynamically at runtime, its value will be reset the next time the server restarts. To make the value persist on restart, set it in a configuration file too.

## Details

The `wsrep_certificate_expiration_hours_warning` system variable can be used to configure certificate expiration warnings for MariaDB Enterprise Cluster, powered by Galera:

* When the `wsrep_certificate_expiration_hours_warning` system variable is set to `0`, certificate expiration warnings are not printed to the [MariaDB Error Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log).
* When the `wsrep_certificate_expiration_hours_warning` system variable is set to a value `N`, which is greater than `0`, certificate expiration warnings are printed to the MariaDB Error Log when the node's certificate expires in `N` hours or less.

### Parameters

| Command-line          | --wsrep\_certificate\_expiration\_hours\_warning=# |
| --------------------- | -------------------------------------------------- |
| Configuration file    | Supported                                          |
| Dynamic               | Yes                                                |
| Scope                 | Global                                             |
| Data Type             | BIGINT UNSIGNED                                    |
| Minimum Value         | 0                                                  |
| Maximum Value         | 18446744073709551615                               |
| Product Default Value | 0                                                  |
