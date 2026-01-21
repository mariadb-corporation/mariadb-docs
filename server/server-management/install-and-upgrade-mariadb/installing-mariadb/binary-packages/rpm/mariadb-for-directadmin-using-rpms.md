---
description: >-
  Specific instructions for installing MariaDB RPMs on servers running the
  DirectAdmin control panel, including necessary configuration edits to prevent
  conflicts.
---

# MariaDB for DirectAdmin Using RPMs

If you are using DirectAdmin and you encounter any issues with [Installing MariaDB with YUM](yum.md), then the directions below may help. The process is very straightforward.

{% hint style="info" %}
Installing with YUM is preferable to installing the MariaDB RPM packages manually, so only do this if you are having issues such as:\
Starting httpd:

{% code overflow="wrap" %}
```
  httpd:
    Syntax error on line 18 of /etc/httpd/conf/httpd.conf:
    Syntax error on line 1 of /etc/httpd/conf/extra/httpd-phpmodules.conf:
      Cannot load /usr/lib/apache/libphp5.so into server:
        libmysqlclient.so.18: cannot open shared object file: No such file or directory
```
{% endcode %}
{% endhint %}

Or:

{% code overflow="wrap" %}
```
Starting httpd:
  httpd:
    Syntax error on line 18 of /etc/httpd/conf/httpd.conf:
    Syntax error on line 1 of /etc/httpd/conf/extra/httpd-phpmodules.conf:
      Cannot load /usr/lib/apache/libphp5.so into server:
        /usr/lib/apache/libphp5.so: undefined symbol: client_errors
```
{% endcode %}

## RPM Installation

To install the RPMs, there is a quick and easy guide to [Installing MariaDB with the RPM Tool](installing-mariadb-with-the-rpm-tool.md). Follow the instructions there.

## Necessary Edits

We do not want DirectAdmin's custombuild to remove/overwrite our MariaDB\
installation whenever an update is performed. To rectify this, disable automatic MySQL installation.

Edit `/usr/local/directadmin/custombuild/options.conf` and replace `mysql_inst=yes` with `mysql_inst=no`

```bash
sudo sed -i 's/^mysql_inst=yes/mysql_inst=no/' /usr/local/directadmin/custombuild/options.conf
```

{% hint style="warning" %}
When MariaDB is installed manually (i.e. not using YUM), updates are not\
automatic. You will need to update the RPMs yourself.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
