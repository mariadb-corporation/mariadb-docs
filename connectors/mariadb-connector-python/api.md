---
description: >-
  MariaDB Connector/Python API reference covers the module, connection
  class, cursor class, async/await support, connection pooling, and
  constants used in Python database applications.
---

# API Reference

{% columns %}
{% column %}
{% content-ref url="module.md" %}
[module.md](module.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Connector/Python module provides `connect`, `asyncConnect`, `create_pool`, and `create_async_pool` constructors, DB API 2.0 type objects, and the exception hierarchy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connection.md" %}
[connection.md](connection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python Connection class reference covers parameters, methods for commit and rollback, and read-only attributes for server version and TLS state.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cursor.md" %}
[cursor.md](cursor.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python Cursor class documents parameters, execute and fetch methods, and attributes such as `rowcount`, `description`, and `sp_outparams` for stored procedures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pool.md" %}
[pool.md](pool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python ConnectionPool manages a fixed-size pool with methods to add, retrieve, and close connections, plus attributes reporting pool size and connection state.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="constants.md" %}
[constants.md](constants.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python constants module defines groups: CAPABILITY, CLIENT, CURSOR, FIELD_TYPE, FIELD_FLAG, INDICATOR, STATUS, and EXT_FIELD_TYPE.
{% endcolumn %}
{% endcolumns %}

{% @marketo/form formId="4316" %}
