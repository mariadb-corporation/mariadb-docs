---
description: >-
  The util global object of MariaDB Shell: dump, load, and copy utilities,
  table export and import, password changes, and diagnostics collectors.
icon: toolbox
---

# Utilities

The `util` global object groups the administrative utilities of MariaDB Shell. It is available in Python mode as soon as the shell starts. Most utilities work on the global session, so you connect to a server first and then call the utility.

In Python, you call the functions in snake case and pass options as a dictionary with camelCase keys:

```text
MariaDB localhost:3306 ssl  Py > util.export_table("shop.orders", "/exports/orders.tsv", {"where": "status = 'open'"})
```

Most utilities can also run from the operating system shell through [command line integration](../using-mariadb-shell/command-line-integration.md), where function and option names may be written in camelCase or kebab-case:

```sh
mariadb-shell root@localhost -- util export-table shop.orders /exports/orders.tsv --where="status = 'open'"
```

To list the utilities that your build provides, run `\? util` in the shell. For the options of one function, run `\? util.<function>`, for example `\? util.import_table`.

{% columns %}
{% column %}
{% content-ref url="dump-and-load/" %}
[dump-and-load](dump-and-load/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Parallel logical backup, restore, and server-to-server copy with `util.dump_instance()`, `util.dump_schemas()`, `util.dump_tables()`, `util.load_dump()`, and the copy utilities.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-export-and-import.md" %}
[table-export-and-import.md](table-export-and-import.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Export one table to a delimited text file with `util.export_table()`, and load delimited or JSON files into a table in parallel with `util.import_table()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="password-change-utility.md" %}
[password-change-utility.md](password-change-utility.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Change the password of your own account or of another account with `util.change_password()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="diagnostics-utilities.md" %}
[diagnostics-utilities.md](diagnostics-utilities.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `util.debug` collectors that package server, shell, and host information into a ZIP file for troubleshooting and support requests.
{% endcolumn %}
{% endcolumns %}
