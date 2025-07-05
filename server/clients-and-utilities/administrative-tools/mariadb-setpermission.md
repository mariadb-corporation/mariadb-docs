# mariadb-setpermission

## Syntax

```
mariadb-setpermission [options]
```

## Description

`mariadb-setpermission` is a Perl script that was originally written and contributed by Luuk de Boer. It requires the DBI and DBD::mysql Perl modules to be installed.`mariadb-setpermission` can help you add users or databases or change passwords in MariaDB.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysql_setpermission`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It interactively sets permissions in the MariaDB grant tables, but does not check permissions which have already been set in MariaDB. So if you can't connect to MariaDB using the permission you just added, take a look at the permissions which have already been set in MariaDB.

The account used when you connect determines which permissions you have when attempting to modify existing permissions in the grant tables.

`mariadb-setpermission` also reads options from the \[client] and \[perl] groups in the .my.cnf file in your home directory, if the file exists.

The following options are available:

## Options

| Option | Description |
| ------ | ----------- |
| Option | Description |

|                     |                                                                                                                                                                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --help              | Display a help message and exit.                                                                                                                                                                                                                                                                         |
| --host=host\_name   | Connect to the MariaDB server on the given host.                                                                                                                                                                                                                                                         |
| --password=password | The password to use when connecting to the server. Note that the password value is not optional for this option, unlike for other MariaDB programs Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line. |
| --port=port\_num    | The TCP/IP port number to use for the connection.                                                                                                                                                                                                                                                        |
| --socket=path       | For connections to localhost, the Unix socket file to use.                                                                                                                                                                                                                                               |
| --user=user\_name   | The MariaDB user name to use when connecting to the server.                                                                                                                                                                                                                                              |

## Example

```
./mariadb-setpermission --user=msandbox --password=msandbox --host=127.0.0.1 --port=11200
######################################################################
## Welcome to the permission setter 1.4 for MariaDB.
## made by Luuk de Boer
######################################################################
What would you like to do:
  1. Set password for an existing user.
  2. Create a database + user privilege for that database
     and host combination (user can only do SELECT)
  3. Create/append user privilege for an existing database
     and host combination (user can only do SELECT)
  4. Create/append broader user privileges for an existing
     database and host combination
     (user can do SELECT,INSERT,UPDATE,DELETE)
  5. Create/append quite extended user privileges for an
     existing database and host combination (user can do
     SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,
     LOCK TABLES,CREATE TEMPORARY TABLES)
  6. Create/append full privileges for an existing database
     and host combination (user has FULL privilege)
  7. Remove all privileges for an existing database and
     host combination.
     (user will have all permission fields set to N)
  0. exit this program
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
