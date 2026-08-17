# Licensing FAQ

In this article we will explain how the MariaDB and MySQL server and client library licenses affect other applications and what steps you can take to comply with the GPL or avoid having to change your applications to GPL.

In the following text we talk about MariaDB. The guidelines also apply to MySQL in general, at least up to 5.1.55 which was the latest stable release at the time of writing.

## Licenses Used by MariaDB

MariaDB is distributed under the [GPL license](mariadb-licenses.md), version 2.

The [MariaDB client libraries]({server}/clients-and-utilities/server-client-software/client-libraries) for [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) and [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc) are distributed under the LGPL license, version 2.1 or later. The LGPL license allows you to distribute these MariaDB client libraries freely with any application.

The MariaDB client library included with the MariaDB server is also GPL version 2, but has a [FLOSS exception](mariadb-licenses.md) that allows you to combine it with most other open source software, without conflicting with their license, even if that license is incompatible with the GPL. We do however recommend you to use the new [client libraries]({server}/clients-and-utilities/server-client-software/client-libraries) for any non-GPL application.

## Internal Usage is Free

The GPL license only affects code that you distribute to other parties.

Internal usage within an organization is totally free and not subject to any conditions. There is no such thing as 'internal distribution' that would restrict the usage of your code by requiring it to be GPLed.

Connecting to a remote service that runs MariaDB (or any other GPL software) in the background is also free.

For internal programs for which you own all the copyright(s), there is essentially no risk in using GPL software. The argument you can use in your defense is that if the software became GPL as part of the distribution, you as the copyright holder could immediately revert your part back to its original copyright. No one has the right to require you to reveal or redistribute your code to the outside of your organization even if you would have distributed it internally linked with GPL software!

If your lawyers are concerned about distributions of software linked with GPL libraries between different legal entities within your organization, you can solve this by distributing your components and the GPL software separately, and have your other entity combining them. You can also switch to use the new [LGPL client libraries]({server}/clients-and-utilities/server-client-software/client-libraries).

## Distributing an Application with a MariaDB Connector/Client

This section is for those that want to distribute the MariaDB client library code, but not the server, with their applications.

### Free Software/Open-Source Applications

If your application is Free software/open source and uses one of the licenses listed in the [FLOSS exception](mariadb-licenses.md), the GPL in the client library does not affect your application.

In other cases we recommend you to use the new [LGPL client libraries]({server}/clients-and-utilities/server-client-software/client-libraries).

### Using a Connector That is not GPL

If you are using a connector that is not GPL, you are only bound by the license of that connector. Some examples are:

* [MySQL native driver for PHP - mysqlnd](https://php.net/manual/en/book.mysqlnd.php)
* ruby-mysql
* [LGPL client libraries or C, Java and ODBC]({server}/clients-and-utilities/server-client-software/client-libraries).

The above have licenses that allow you to use them freely, without you being bound by the GPL.

### Using a Database-Source-Independent Framework

If you are using a framework that allows you to connect dynamically to different RDBMS systems, any GPL licensed module loaded by the framework will not affect the
application. Such frameworks are

* ODBC (Open Database Connectivity)
* JDBC (Java Database connectivity)
* Perl
* [PHP PDO MySQL driver](https://php.net/manual/en/ref.pdo-mysql.php)

The reason the GPL in the MySQL client library would not affect your application in this case is that the GPL client is supporting a standard interface and is thus merely an optional component among many. Your application could just as easily use the framework to connect to a RDBMS other than MariaDB or MySQL.

Any software can be connected to the GPL v2 licensed MySQL Connector/ODBC, without the need for that software to be GPLed. This is because there is a piece of general management software, the ODBC manager, between the GPLed MySQL Connector/ODBC and your software. If any logic would require the software which interfaces with MySQL Connector/ODBC to be GPL, then that would apply also to the ODBC manager itself. Yet, the ODBC manager is not GPL, neither on Windows nor on Linux. By consequence, no one would be allowed to use MySQL ODBC driver for anything.

### Using the MariaDB Client Library for C

If your application is using a license that is not covered by the [FLOSS exception](mariadb-licenses.md), you
should use the new [LGPL client libraries or C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c).

The LGPL license allows you to distribute these MariaDB client library freely with any application. If you modify the client library, you need to publish the new source code.

## Distributing a Proprietary Application With the MariaDB / MySQL Server

When you are distributing your application together with MariaDB or MySQL, you are bound by the GPL if some of the following statements apply:

* You are using GPL code from MySQL linked directly to your application. (Like the MySQL GPL client library).
* Your application requires the MariaDB server to work and without the MariaDB server it doesn't start or it has very limited functionality.

The problem with the client library can be avoided by using one of the solutions mentioned before on this page.

If your application works with many databases, either natively or by using one of the [database-source-independent frameworks](licensing-faq.md#using-a-database-source-independent-framework), then you can freely distribute the MariaDB server with your application without being affected by the GPL. The reason for this is that MariaDB would only be an optional, independent component in your software distribution and section 2 of the GPL explicitly allows this:

```
"In addition, mere aggregation of another work not based on
the Program with the Program (or with a work based on the Program) on
a volume of a storage or distribution medium does not bring the other
work under the scope of this License."
```

You also have the option to buy licenses for MySQL from Oracle to get MySQL under other copyright terms. If you would like to later be able to use MariaDB instead of MySQL, please ensure that your license agreement allows you to make changes to the MySQL code! (This is something that you should ensure in all cases as otherwise you may run into bugs that Oracle will not fix, you are not allowed to fix and could make MySQL software unusable for you!)

The rights to use the MariaDB code changes in your application can be requested.

## Legal Notice

The text above is written by Michael "Monty" Widenius, who is not a lawyer and you should not regard any statements of the above as 'ultimate truth' in all scenarios. On the other hand, it was David and Monty who together decided to make MySQL GPL and also decided and openly declared the intentions behind this license change, so there is some merit to information in this article.

If you want a second opinion of how GPL works in this case, you can contact [Software Freedom Law Center](https://www.softwarefreedom.org) or [Free Software Foundation](https://www.fsf.org) about this. Neither part has had anything to do with this KB article but they are the default authorities to turn to when you want to know more about the GPL or LGPL.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
