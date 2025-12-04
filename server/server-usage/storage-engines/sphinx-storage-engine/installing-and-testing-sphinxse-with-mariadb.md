# Installing and Testing SphinxSE with MariaDB

To use [SphinxSE](./) with MariaDB you need to first [download and install Sphinx](installing-sphinx.md).

Complete Sphinx documentation is available on the [Sphinx website](https://sphinxsearch.com/docs/).

## Tips for Installing Sphinx

### libexpat

One library we know you will need on Linux before you can install Sphinx is `libexpat`. If it is not installed, you will get the\
warning `checking for libexpat... not found`.\
On Suse the package is called `libexpat-devel`,\
on Ubuntu the package is called `libexpat1-dev`.

### MariaDB detection

If you run into problems with MariaDB not being detected, use the\
following options:

```
--with-mysql            compile with MySQL support (default is enabled)
 --with-mysql-includes   path to MySQL header files
 --with-mysql-libs       path to MySQL libraries
```

The above will tell the `configure` script where your MySQL/MariaDB\
installation is.

## Testing Sphinx

After installing Sphinx, you can check that things are working in MariaDB by\
doing the following:

```bash
cd installation-dir/mysql-test
./mysql-test-run --suite=sphinx
```

If the above test doesn't pass, check the logs in the `'var'` directory.\
If there is a problem with the sphinx installation, the reason can probably\
be found in the log file at: `var/log/sphinx.sphinx/searchd/sphinx.log`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
