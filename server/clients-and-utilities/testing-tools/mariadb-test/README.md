---
description: >-
  MariaDB uses mariadb-test to test functionality. It is an all-in-one test
  framework doing unit, regression, and conformance testing
---

# mariadb-test

{% columns %}
{% column %}
{% content-ref url="mariadb-test-overview.md" %}
[mariadb-test-overview.md](mariadb-test-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How mariadb-test runs a test file and compares its output against a result file to decide pass or fail.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-minio-for-usage-with-mariadb-test-run.md" %}
[installing-minio-for-usage-with-mariadb-test-run.md](installing-minio-for-usage-with-mariadb-test-run.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MinIO to provide S3-compatible storage for testing the S3 storage engine with mariadb-test-run.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-test-auxiliary-files.md" %}
[mariadb-test-auxiliary-files.md](mariadb-test-auxiliary-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The auxiliary files the mariadb-test framework uses to control test runs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-test-run-pl-options.md" %}
[mariadb-test-run-pl-options.md](mariadb-test-run-pl-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Command-line options for the mariadb-test-run.pl test-runner script.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="new-features-for-mysqltest-in-mariadb.md" %}
[new-features-for-mysqltest-in-mariadb.md](new-features-for-mysqltest-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB enhancements to the mariadb-test (mysqltest) framework.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pausing-mariadb-test-run-pl.md" %}
[pausing-mariadb-test-run-pl.md](pausing-mariadb-test-run-pl.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to pause and resume mariadb-test-run.pl while a test run is in progress.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="the-debug-sync-facility.md" %}
[the-debug-sync-facility.md](the-debug-sync-facility.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Debug Sync facility for placing synchronization points to coordinate tests.
{% endcolumn %}
{% endcolumns %}
