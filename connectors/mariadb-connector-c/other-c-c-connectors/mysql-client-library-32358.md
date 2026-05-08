---
description: >-
  MySQL client library 3.23.58 is an archived LGPL release for non-GPL
  distribution use cases, with known limitations including no prepared
  statements and deprecated password authentication.
---

# MySQL Client Library 3.23.58

[Download](https://askmonty.org/wiki/MariaDB:Download:LGPL_MySQL_Client_Library_3.23.58) | **Release Notes**

**Release date:** 30 Aug 2010

**Note that this library is superseded by the new** [**MariaDB Client Library for C**](../)**, which is also LGPL.**

This is the LGPL MySQL client library version 3.23.58. This library can be used to connect to MySQL or MariaDB.

Normally, you should use the standard libmysql client library to connect to MariaDB/MySQL. The main reason for wanting to use this one is if you want to distribute your non-GPL application with MySQL support (to provide some optional feature), but don't want to change the license of your application to\
GPL.

This code is based on the LGPL libmysql client library from MySQL 3.23.

The following are the main known limitations:

* You have to compile your application(s) to use this library (as the structures used by the C API are a bit different)
* You have to use the `--old-password` option in MySQL (as the old client library only supports the old authentication)
* You can't use prepared statements (as the old client library doesn't have support for these)
* Not all client character sets are supported.
* It doesn't compile on Windows (should not be hard to fix; It's mainly the compiler environment files that are missing)
* It's not as secure as the standard libmysql as it uses the old password protocol.

This library could be used as the basis for a full, up-to-date LGPL MariaDB client library that is a binary drop-in replacement for the current MySQL /MariaDB GPL library.

Besides using this library as the basis, the other options are:

* Use the new [MariaDB Client Library for C](../), which is also LGPL.
* Write a new client library from scratch.
* Use the Drizzle client library as the base for a new client library.

Monty Program AB is about to start a project for creating a new free client library that is binary compatible with the old client library. See [Monty's blog](https://monty-says.blogspot.com/2010/12/in-search-of-bsdlgplapache-licensed.html) about this for more information.

If you want to be part of this development effort, you can discuss this on the [maria-developers mailing list](https://launchpad.net/~maria-developers).

If you are interested in sponsoring this effort, you can [contact Monty Program](https://montyprogram.com/contact).

## See also:

* The new [MariaDB Client Library for C](../) is also LGPL.
* [Worklog for the MySQL 3.23 client library](https://askmonty.org/worklog/Client-Sprint/index.pl?tid=134)
* [Worklog for a new free MariaDB client library](https://askmonty.org/worklog/Client-Sprint/index.pl?tid=171)

{% hint style="info" %}
Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announcement 'at lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified of all new releases, security issues, and low-traffic critical bug fixes for all MariaDB plc products, thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
Information can be found on the [Distributions Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.
{% endhint %}

{% @marketo/form formId="4316" %}
