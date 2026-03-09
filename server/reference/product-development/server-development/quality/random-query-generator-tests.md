---
description: >-
  Explains how to use the Random Query Generator (RQG) to find edge-case bugs by
  executing automatically generated SQL queries.
---

# Random Query Generator Tests

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

[PQuery](https://github.com/mariadb-corporation/mariadb-qa/tree/master/pquery) is currently in development to perform random query generation.

The documentation for the Random Query Generator is available [here](http://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator).

The latest RQG used by MariaDB can be found at:

* [https://github.com/elenst/rqg/tree/master](https://github.com/elenst/rqg/tree/master)
* [https://github.com/MariaDB/randgen/tree/master](https://github.com/MariaDB/randgen/tree/master)

The list of automatic tests is located in the `buildbot.conf` file in the [`mariadb.org-tools`](benchmarks-and-long-running-tests/benchmarks/mariadb-tools.md) repository.

## See Also <a href="#see-also" id="see-also"></a>

* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [Optimizer Quality](optimizer-quality.md)
* [QA Tools](qa-tools.md)
* [Worklog Quality Checklist Template](worklog-quality-checklist-template.md)
