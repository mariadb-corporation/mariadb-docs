---
description: >-
  Add your own reports, global objects, plugins, and SQL statements to
  MariaDB Shell with Python.
icon: puzzle-piece
---

# Extending MariaDB Shell

MariaDB Shell runs an embedded Python interpreter, and the same Python APIs that the built-in features use are open to you. With a few lines of Python you can add a report that `\show` and `\watch` display, a global object with documented functions, or a handler that answers an SQL statement the server doesn't know.

The extension mechanisms build on each other:

* A **report** is a Python function registered with `shell.register_report()`. It returns rows or a structured document, and the shell formats the output.
* A **plugin** is a directory with an `init.py` file that the shell loads at startup. Plugins add global objects with documented functions, which appear next to `shell` and `util` and are documented by `\?`, and they register reports and SQL handlers. The plugin decorators generate the help text from your docstrings.
* An **SQL handler** intercepts SQL statements that start with a given prefix and returns a result that the shell displays like a server result.

To load your code automatically, put it in a plugin directory, in the `init.d` directory of the user configuration directory, or in the [startup script](../customizing/startup-scripts.md).

{% columns %}
{% column %}
{% content-ref url="reports.md" %}
[reports.md](reports.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The built-in `query`, `thread`, and `threads` reports, the `\show` and `\watch` commands, and how to write your own reports.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="plugins.md" %}
[plugins.md](plugins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The plugin directory layout, the plugin decorators, the built-in plugins, the `plugins` global object, and the extension object API that the decorators build on.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-handlers.md" %}
[sql-handlers.md](sql-handlers.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to intercept SQL statements by prefix and return custom results built with `shell.create_result()`.
{% endcolumn %}
{% endcolumns %}
