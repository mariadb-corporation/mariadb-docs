---
description: >-
  Integrate MariaDB Server with Sphinx for advanced full-text search. The Sphinx
  storage engine allows you to query external Sphinx indexes directly from your
  database.
---

# SphinxSE

{% columns %}
{% column %}
{% content-ref url="about-sphinxse.md" %}
[about-sphinxse.md](about-sphinxse.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SphinxSE is a storage engine that connects MariaDB to the Sphinx search daemon, enabling advanced full-text search capabilities within MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-sphinx.md" %}
[installing-sphinx.md](installing-sphinx.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for installing the standalone Sphinx search server on various operating systems, a prerequisite for using the SphinxSE storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-and-testing-sphinxse-with-mariadb.md" %}
[installing-and-testing-sphinxse-with-mariadb.md](installing-and-testing-sphinxse-with-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to install the SphinxSE plugin in MariaDB and run tests to verify the connection between the database and the Sphinx daemon.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-sphinx.md" %}
[configuring-sphinx.md](configuring-sphinx.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to configuring the Sphinx daemon (`searchd`) to index data from MariaDB, including setting up `sphinx.conf` and creating necessary users.
{% endcolumn %}
{% endcolumns %}
