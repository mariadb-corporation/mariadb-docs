---
description: >-
  MariaDB Shell is an interactive SQL and Python client for MariaDB Server, with
  parallel dump, load, and copy utilities, SSH tunnels, and local sandboxes.
icon: terminal
---

# MariaDB Shell

MariaDB Shell is a client for MariaDB Server that combines an interactive SQL console with a Python scripting environment. Besides running queries, it backs up, restores, and copies databases in parallel, connects through SSH tunnels, deploys local sandbox servers, and lets you automate and extend all of this in Python.

```text
$ mariadb-shell mariadb://root@localhost:3306
MariaDB localhost:3306 ssl  SQL > SELECT VERSION();
```

{% hint style="info" %}
To install MariaDB Shell, run the install script for your platform as described in [Installation](installation/README.md). The executable is `mariadb-shell`, with `msh` as a short alias.
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="about-mariadb-shell.md" %}
[about-mariadb-shell.md](about-mariadb-shell.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
What MariaDB Shell is, its main features, the platforms it runs on, and the servers it connects to.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installation/" %}
[installation](installation/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install, upgrade, and remove MariaDB Shell on Linux, macOS, and Windows with the install scripts or from a release package.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="getting-started/" %}
[getting-started](getting-started/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to start the shell, open a session, use the global objects, and what differs from MySQL Shell.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connecting/" %}
[connecting](connecting/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Connection URIs including `mariadb://` and `mariadb+ssh://`, option files, TLS, SSH tunnels, compression, and stored credentials.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-mariadb-shell/" %}
[using-mariadb-shell](using-mariadb-shell/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Shell commands, SQL and Python modes, editing and history, batch scripts, output formats, and calling the API from the command line.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="utilities/" %}
[utilities](utilities/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Parallel dump, load, and copy, table export and import, password changes, and diagnostics collection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sandbox-instances.md" %}
[sandbox-instances.md](sandbox-instances.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy and manage local MariaDB and MySQL servers for testing and development.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="schema-management/" %}
[schema-management](schema-management/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to develop, release, and deploy a versioned database schema with MariaDB Schema Management.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mcp-server/" %}
[mcp-server](mcp-server/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure, start, and secure the MCP server that gives AI agents access to your MariaDB servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="extending-mariadb-shell/" %}
[extending-mariadb-shell](extending-mariadb-shell/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reports, extension objects, plugins, and SQL handlers written in Python.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="customizing/" %}
[customizing](customizing/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Startup scripts, prompt themes, configuration options, and Python module search paths.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="logging-and-debugging.md" %}
[logging-and-debugging.md](logging-and-debugging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The application log, log levels, verbose output, and SQL logging.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cli-reference.md" %}
[cli-reference.md](cli-reference.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Every command-line option of `mariadb-shell`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="files-and-environment-variables.md" %}
[files-and-environment-variables.md](files-and-environment-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The files MariaDB Shell reads and writes, and the environment variables it recognizes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="appendix/" %}
[appendix](appendix/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Background on how parts of MariaDB Shell work, such as the credential helpers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="license.md" %}
[license.md](license.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The license that MariaDB Shell is distributed under.
{% endcolumn %}
{% endcolumns %}
