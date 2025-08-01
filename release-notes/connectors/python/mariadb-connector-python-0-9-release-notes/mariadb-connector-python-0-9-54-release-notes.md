# Connector/Python 0.9.54-beta Release Notes

{% include "../../../.gitbook/includes/latest-python.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/python-connector/" class="button primary">Download</a> <a href="mariadb-connector-python-0-9-54-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0954-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-python-guide" class="button secondary">Connector/Python Overview</a>

**Release date:** 18 Feb 2020

This is a [_**beta**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/Python and not intended for production use.

{% hint style="danger" %}
**Do not use&#x20;**_**beta**_**&#x20;releases in production!**
{% endhint %}

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C client library for client server communication.

## Notable Updates

* Fixed parameter sequence when creating a xid object
* Added ssl\_capath in connect() method
* [CONPY-40](https://jira.mariadb.org/browse/CONPY-40): ConnectionPool.\_setconfig now accepts only DSN parameters
* [CONPY-35](https://jira.mariadb.org/browse/CONPY-35): Close and reinitialize statement if the cursor was reused with a different SQL statement
* [CONPY-34](https://jira.mariadb.org/browse/CONPY-34): If a python object can't be converted to a corresponding data type, an exception will be raised.
* [CONPY-39](https://jira.mariadb.org/browse/CONPY-39): If no pool\_name was provided, an exception will be raised.
* [CONPY-33](https://jira.mariadb.org/browse/CONPY-33): Segfault when using auto completion in python shell
* [CONPY-37](https://jira.mariadb.org/browse/CONPY-37): Corrected option name: named\_tuple
* [CONPY-36](https://jira.mariadb.org/browse/CONPY-36): connection key word socket was renamed to unix\_socket

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-python-09-changelogs/mariadb-connector-python-0954-changelog.md).

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
