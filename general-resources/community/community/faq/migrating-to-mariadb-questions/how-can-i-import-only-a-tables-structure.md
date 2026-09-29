# How can I Import Only a Table's Structure?

The easiest way to import only the structure of databases and tables is to export only that, and not the data. Use [mariadb-dump]({server}/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) with the `--no-data` option to export your database without its rows, then import the resulting file as usual. Many GUI clients have similar options.

Importing a schema from other database systems is more difficult, and may not be possible.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
