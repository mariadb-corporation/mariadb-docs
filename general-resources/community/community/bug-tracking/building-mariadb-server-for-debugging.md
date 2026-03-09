# Building MariaDB Server for Debugging

Instructions on how to build a mysqld that contains all the information we need to fix problems you encounter. (A more detailed explanation can be found [here](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-fault-finding/how-to-produce-a-full-stack-trace-for-mariadbd).)

* Add the [--core-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) option to your /.my.cnf or /etc/my.cnf file under the \[mysqld] tag.
* Get the latest [MariaDB code from GitHub](../../contributing-participating/contributing-code.md).
* Compile MariaDB with the -g compiler flag (Unix).
* Optionally: with more checking [Compile MariaDB for debugging](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-fault-finding/compiling-mariadb-for-debugging) - will cause slowdown.
* Shut down your old mysqld server.
* Install the new compiled `mysqld` binary. Note that if you are compiling same version of MariaDB that you have already installed it's enough to just copy this one binary!
* Restart mysqld.

Compiling with **-g** should not cause any notable slowdown of the server.

You can of course also do **make install**, but the above way allows\
you to go back to your old binary if needed.

If you get any errors about a wrong number of error messages, you can\
fix that by copying the corresponding language file from **sql/share**\
over your old ones (this should be reasonably safe to do).

```
cp sql/share/english/* mariadb-install-dir/share/mysql/english
```

## What to Do When You Get a Crash After Installing a Debug Binary

Now when you get a crash do the following:

* Create a README file that describes the problem. You can use the mysqlbug script to generate a template for this.
* Create a tar file containing the core, the mysqld binary and README. If possible, also add any database files that could help us repeat the problem!

```
sh> tar cvfz /tmp/mariadb-bug-'short-description'.tgz mariadb-data-dir/core* mariadb-install-dir/libexec/mysqld README
```

* Send it to our secure ftp server:

```
sh> ftp -a ftp.askmonty.org
ftp> cd private
ftp> binary 
ftp> put /tmp/mariadb-bug-'short-description'.tgz
ftp> quit
```

* To be able to follow the progress, create a bug report in [JIRA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/server-development/tools/jira) about this. This should be easy to do based on the information you have in your README file.

## See Also

* [Compiling MariaDB from Source](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source)
* [Compiling MariaDB for debugging](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-fault-finding/compiling-mariadb-for-debugging)
* [How to produce a stack trace from a core file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-fault-finding/how-to-produce-a-full-stack-trace-for-mariadbd)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
