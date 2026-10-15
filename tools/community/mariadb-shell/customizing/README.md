---
description: >-
  Tailor MariaDB Shell to the way you work: startup scripts, the prompt,
  persistent configuration options, and the Python module search path.
icon: sliders
---

# Customizing MariaDB Shell

MariaDB Shell keeps its per-user settings in the user configuration directory, `~/.mariadb-shell` on Linux and macOS and `%AppData%\MariaDB\mariadb-shell` on Windows. You can point the shell to another directory with the `MARIADB_SHELL_USER_CONFIG_HOME` environment variable. For a complete list of the files the shell reads, see [Files and Environment Variables](../files-and-environment-variables.md).

The pages in this section describe the files and settings that change how the shell behaves for you.

{% columns %}
{% column %}
{% content-ref url="startup-scripts.md" %}
[startup-scripts.md](startup-scripts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Where the shell looks for `mariadb-shellrc.py`, when the script runs, and what to put in it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="prompt.md" %}
[prompt.md](prompt.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The shipped prompt themes, including the Nerd Fonts themes, the prompt variables, and how to write your own theme.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-options.md" %}
[configuration-options.md](configuration-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Every shell option, how to change it for a session or permanently, and which setting wins when several sources set it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="python-module-search-paths.md" %}
[python-module-search-paths.md](python-module-search-paths.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the bundled Python interpreter finds modules, and how to add your own modules and third-party packages.
{% endcolumn %}
{% endcolumns %}
