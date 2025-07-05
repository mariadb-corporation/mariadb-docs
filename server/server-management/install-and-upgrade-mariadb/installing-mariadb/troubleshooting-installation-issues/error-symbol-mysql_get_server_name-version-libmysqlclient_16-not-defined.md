# Error: symbol mysql\_get\_server\_name, version libmysqlclient\_16 not defined

If you see the error message:

```
symbol mysql_get_server_name, version libmysqlclient_16 not defined in file libmysqlclient.so.16 with link time reference
```

...then you are probably trying to use the mysql command-line client from\
MariaDB with libmysqlclient.so from MySQL.

The symbol `mysql_get_server_name()` is something present in the MariaDB\
source tree and not in the MySQL tree.

If you have both the MariaDB client package and the MySQL client packages\
installed this error will happen if your system finds the MySQL version of`libmysqlclient.so` first.

To figure out which library is being linked in dynamically (ie, the\
wrong one) use the 'ldd' tool.

```
ldd $(which mysql) | grep mysql
```

or

```
ldd /path/to/the/binary | grep mysql
```

For example:

```
me@mybox:~$ ldd $(which mysql)|grep mysql
        libmysqlclient.so.16 => /usr/lib/libmysqlclient.so.16 (0xb74df000)
```

You can then use your package manager's tools to find out which package the library belongs to.

On CentOS the command to find out which package installed a specific file is:

```
rpm -qf /path/to/file
```

On Debian-based systems, the command is:

```
dpkg -S /path/to/file
```

Here's an example of locating the library and finding out which package it belongs to on an Ubuntu system:

```
me@mybox:~$ ldd $(which mysql)|grep mysql
	libmysqlclient.so.16 => /usr/lib/libmysqlclient.so.16 (0xb75f8000)
me@mybox:~$ dpkg -S /usr/lib/libmysqlclient.so.16
libmariadbclient16: /usr/lib/libmysqlclient.so.16
```

The above shows that the mysql command-line client is using the library`/usr/lib/libmysqlclient.so.16` and that library is part of\
the `libmariadbclient16` Ubuntu package. Unsurprisingly, the\
mysql command-line client works perfectly on this system.

If the answer that came back had been something other than a MariaDB package,\
then it is likely there would have been issues with running the MariaDB mysql client\
application.

If the library that the system tries to use is not from a MariaDB\
package, the remedy is to remove the offending package (and possibly install or re-install\
the correct package) so that the correct library can be used.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
