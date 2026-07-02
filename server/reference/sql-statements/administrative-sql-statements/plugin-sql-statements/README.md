---
ayout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
description: >-
  Manage server plugins. This section covers INSTALL PLUGIN, UNINSTALL PLUGIN,
  and SHOW PLUGINS for extending server functionality.
---

# Plugin Statements

{% columns %}
{% column %}
{% content-ref url="install-plugin.md" %}
[install-plugin.md](install-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install a specific plugin from a shared library. This statement adds the plugin to the mysql.plugin table and loads its code into the server memory.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install-soname.md" %}
[install-soname.md](install-soname.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load all plugins contained within a shared library file. This statement automatically discovers and installs every valid plugin found in the specified library.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="uninstall-plugin.md" %}
[uninstall-plugin.md](uninstall-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a specific plugin from the server. This statement unloads the plugin code and deletes its entry from the mysql.plugin table to prevent reloading.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="uninstall-soname.md" %}
[uninstall-soname.md](uninstall-soname.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Uninstall all plugins loaded from a specific library. This statement removes every plugin associated with the library file and unloads the library itself.
{% endcolumn %}
{% endcolumns %}
