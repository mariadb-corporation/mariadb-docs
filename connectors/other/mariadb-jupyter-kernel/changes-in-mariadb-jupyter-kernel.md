---
description: >-
  Release history for the MariaDB Jupyter Kernel, covering SQL
  autocompletion, code introspection, multi-notebook server management, and
  other fixes from v0.1.0 onward.
---

# Changes in MariaDB Jupyter Kernel

## \[v0.2.0] 02 November 2021

### Features and improvements

* SQL code autocompletion ( [GSoC](https://summerofcode.withgoogle.com/archive/2021/projects/6374646231859200/) project 2021 by Xing-Zhi Jiang)
* Code Introspection ( [GSoC](https://summerofcode.withgoogle.com/archive/2021/projects/6374646231859200/) project 2021 by Xing-Zhi Jiang)
* Add `debug` option in ClientConfig
* The MyBinder configurations are switched to Dockerfile to achieve more flexibility
* The kernel is now able to start its own MariaDB Server instance, run `mariadb-install-db` to create a datadir and pass the right options to client and server so that first-time users only need to have the `mariadb-server` package installed (Contribution by Jonas Karlsson).

### Bug fixes

* Progress reporting for commands such as `LOAD DATA` is disabled
* In multiple running notebooks with multiple MariaDB kernels, only the last alive notebook kills the MariaDB server (Contribution by Jonas Karlsson)

## \[v0.1.1] 29 March 2021

### Features and improvements

* Add pre-commit support in the GitHub Actions CI
* Add two new example notebooks (contribution from Daniel Black)
* Add more tests
* Queries such as INSERT that don't return any result set should show a "Query OK" confirmation message (Contribution by XING-ZHI JIANG)
* Add %%delimiter cell magic command to run a query under a different SQL delimiter
* SQL error messages should only contain the relevant part of the error without the MariaDB error number

### Bug fixes

* Refactor CodeParser to address a number of bugs related to how the MariaDB kernel was parsing multi-line queries
* Fixed bugs in MariaDB client that were leading to wrong multi-line outputs from functions such as JSON\_DETAILED

## \[v0.1.0] 11 January 2021

First release!


{% @marketo/form formId="4316" %}
