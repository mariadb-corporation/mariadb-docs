---
description: >-
  Work with MariaDB Shell day to day: shell commands, SQL and Python modes,
  completion, history, batch runs, result formats, command line integration,
  and the pager.
icon: terminal
---

# Using MariaDB Shell

MariaDB Shell is an interactive client and a scripting environment at the same time. You type SQL or Python at the prompt, control the shell itself with backslash commands such as `\use` or `\option`, and run the same work unattended from scripts, cron jobs, or CI pipelines.

The pages in this section describe how to work with the shell once it's installed and connected. To install it, see [Installation](../installation/). To open a connection, see [Connecting to a Server](../connecting/).

{% columns %}
{% column %}
{% content-ref url="shell-commands.md" %}
[shell-commands.md](shell-commands.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The built-in backslash commands, their aliases and syntax, with details on the ones that need explanation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-and-python-modes.md" %}
[sql-and-python-modes.md](sql-and-python-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to switch between SQL and Python, enter multi-line statements, and run SQL from Python code.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="autocompletion.md" %}
[autocompletion.md](autocompletion.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tab completion for SQL keywords, database object names, Python objects, and shell commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="editing-and-history.md" %}
[editing-and-history.md](editing-and-history.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Line-editing keys, editing statements in an external editor, and the command history.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="batch-execution.md" %}
[batch-execution.md](batch-execution.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to run SQL and Python scripts non-interactively, pass arguments to them, and evaluate exit codes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="output-formats.md" %}
[output-formats.md](output-formats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Table, tabbed, vertical, and JSON result formats, column metadata, and formatting results from Python.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="command-line-integration.md" %}
[command-line-integration.md](command-line-integration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to call `util`, `shell`, and `sandbox` operations directly from the operating system shell.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pager.md" %}
[pager.md](pager.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to page long results through `less`, `more`, or another program.
{% endcolumn %}
{% endcolumns %}
