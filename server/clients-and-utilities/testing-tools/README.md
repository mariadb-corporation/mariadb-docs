---
description: >-
  Explore testing tools for MariaDB Server. This section introduces utilities
  that help you validate server functionality, test configurations, and ensure
  the reliability of your database deployments.
---

# Testing Tools

{% columns %}
{% column %}
{% content-ref url="mariadb-slap.md" %}
[mariadb-slap.md](mariadb-slap.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load-test MariaDB with mariadb-slap by emulating many concurrent clients running a set of queries repeatedly (formerly mysqlslap).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-stress-test.md" %}
[mariadb-stress-test.md](mariadb-stress-test.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Stress-test a MariaDB server by running test scenarios repeatedly with mariadb-stress-test (a symlink to mysql-stress-test).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-test/" %}
[mariadb-test](mariadb-test/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB uses mariadb-test to test functionality. It is an all-in-one test framework doing unit, regression, and conformance testing
{% endcolumn %}
{% endcolumns %}
