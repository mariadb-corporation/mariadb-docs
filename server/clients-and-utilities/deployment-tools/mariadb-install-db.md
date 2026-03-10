---
description: >-
  Definitive mariadb-install-db guide: initialize data directory,
  --user/--datadir syntax, --auth-root-authentication-method=socket, and
  --skip-test-db.
---

# mariadb-install-db

{% hint style="warning" %}
**This page is for the `mariadb-install-db` script for Linux/Unix only.**

For the Windows specific tool of similar name and purpose see [mysql\_install\_db.exe](../legacy-clients-and-utilities/mysql_install_db.md).

The Windows version shares the common theme (creating system tables), yet has a lot of functionality specific to Windows systems, for example creating a Windows service. The Windows version does _not_ share command line parameters with the Unix shell script.
{% endhint %}

`mariadb-install-db` initializes the MariaDB data directory and creates the [system tables](../../reference/system-tables/) in the [mysql](../../reference/system-tables/the-mysql-database-tables/) database, if they do not exist.

{% hint style="info" %}
Previously, the client was called `mysql_install_db`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

MariaDB uses these tables to manage [privileges](../../reference/sql-statements/account-management-sql-statements/grant.md#privilege-levels), [roles](../../security/user-account-management/roles/), and [plugins](../../reference/plugins/). It also uses them to provide the data for the [help](../../reference/sql-statements/administrative-sql-statements/help-command.md) command in the [mariadb](../mariadb-client/) client.

`mariadb-install-db` works by starting MariaDB Server's `mariadbd` process in [--bootstrap](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#bootstrap) mode and sending commands to create the [system tables](../../reference/system-tables/) and their content.

## Usage

Invoke `mariadb-install-db` using the following syntax:

```bash
$ mariadb-install-db [options]
```

Because the MariaDB server (`mariadbd`) needs to access the data directory when it runs, you should either run `mariadb-install-db` from the same account that is used for running `mariadbd`, or run it as `root` and use the `--user` option to indicate the username that `mariadbd` runs as. It might be necessary to specify other options such as `--basedir` or `--datadir` if `mariadb-install-db` does not use the correct locations for the installation directory or data directory. Here is a typical invocation:

```bash
$ scripts/mariadb-install-db --user=mysql \
   --basedir=/opt/mysql/mysql \
   --datadir=/opt/mysql/mysql/data
```

## Options

`mariadb-install-db` supports the following options:

#### --auth-root-authentication-method={`normal`|`socket`}

If set to `normal`, it creates a `root@localhost` account that authenticates with the [`mysql_native_password`](../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin and that has no initial password set, which can be insecure. If set to `socket`, it creates a `root@localhost` account that authenticates with the [`unix_socket`](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin. Set to `socket` by default.

#### --auth-root-socket-user=_username_

Used with `--auth-root-authentication-method=`_`socket`_. It specifies the name of the second account to create with [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) privileges in addition to root, as well as of the system account allowed to access it. Defaults to the value of `--user`.

#### --basedir=_path_

The _path_ to the MariaDB installation directory.

#### --builddir=_directory_

If using `--srcdir` with out-of-directory builds, you will need to set this to the location of the _build directory_ where built files reside.

#### --catalogs=\["_list_"]

Initialize MariaDB for [catalogs](../../security/user-account-management/catalogs/). Argument is a _list of the catalogs to create_, separated with space or comma. The def catalog is created automatically. This option is available from MariaDB 11.7.

#### --catalog-user=_username_

_User_ when adding catalogs to running server. This option is available from MariaDB 11.7.

#### --catalog-password\[=_password_]

_Password_ for [catalog-user](../../security/user-account-management/catalogs/). This option is available from MariaDB 11.7.

#### --catalog-client-arg=_argument_

Other _arguments_ to `mariadb` when adding new [catalogs](https://github.com/mariadb-corporation/docs-server/blob/test/server/clients-and-utilities/security/user-account-management/catalogs/README.md). This option is available from MariaDB 11.7.

#### --cross-bootstrap

For internal use. Used when building the MariaDB system tables on a different host than the target.

#### --datadir=_path_, --ldata=_path_

The _path_ to the MariaDB data directory.

#### --client-debug

Write commands to-be executed in `/tmp/mariadb_install_db.log`. This option is available from MariaDB 11.6.

#### --server-debug

Start mariadbd (server) with `--debug`.

#### --defaults-extra-file=_file_

Read this _file_ after the global files are read. Must be given as the first option.

#### --defaults-file=_file_

Only read default options from the given _file_ name. Must be given as the first option.

#### --defaults-group-suffix=_suffix_

In addition to the given groups, read also groups with this _suffix_.

#### --force

Causes mariadb-install-db to run even if DNS does not work. In that case, grant table entries that normally use host names will use IP addresses.

#### --no-defaults

Don't read default options from any option file. Must be given as the first option.

#### --print-defaults

Print the program argument list and exit. Must be given as the first option.

#### --rpm

For internal use. This option is used by RPM files during the MariaDB installation process.

#### --skip-name-resolve

Uses IP addresses rather than host names when creating grant table entries. This option can be useful if your DNS does not work.

#### --skip-test-db

Don't install the test database.

#### --srcdir=_path_

For internal use. The _path_ to the MariaDB source directory. This option uses the compiled binaries and support files within the source tree, useful for if you don't want to install MariaDB yet and just want to create the system tables. The directory under which mariadb-install-db looks for support files such as the error message file and the file for populating the help tables.

#### --user=_username_

The login _username_ to use for running mariadbd. Files and directories created by mariadbd is owned by this user. You must be root to use this option. By default, mariadbd runs using your current login name and files and directories that it creates is owned by you.

#### --verbose

Verbose mode. Print more information about what the program does.

#### --windows

For internal use. This option is used for creating Windows distributions.

### Option Files

In addition to reading options from the command line, `mariadb-install-db` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-install-db` in an option file, then it is ignored.

The following options relate to how MariaDB command line tools handles option files. They must be given as the first argument on the command line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

### Option Groups

`mariadb-install-db` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group                 | Description                                                                        |
| --------------------- | ---------------------------------------------------------------------------------- |
| \[mysql\_install\_db] | Options read by mysqld\_safe, which includes both MariaDB Server and MySQL Server. |

`mariadb-install-db` also reads options from the following server [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group            | Description                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqld]        | Options read by mysqld, which includes both MariaDB Server and MySQL Server.                                                                                                                   |
| \[server]        | Options read by MariaDB Server.                                                                                                                                                                |
| \[mysqld-X.Y]    | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, \[mysqld-5.5].                                                                 |
| \[mariadb]       | Options read by MariaDB Server.                                                                                                                                                                |
| \[mariadb-X.Y]   | Options read by a specific version of MariaDB Server.                                                                                                                                          |
| \[client-server] | Options read by all MariaDB [client programs](../mariadb-client/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[galera]        | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support.                                                                                            |

## Installing System Tables

### Installing System Tables From a Source Tree

If you have just [compiled MariaDB from source](../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/), and if you want to use `mariadb-install-db` from your source tree, then that can be done without having to actually install MariaDB. This is very useful if you want to test your changes to MariaDB without disturbing any existing installations of MariaDB.

To do so, you would have to provide the `--srcdir` option. For example:

```bash
./scripts/mariadb-install-db --srcdir=. --datadir=path-to-temporary-data-dir
```

### Installing System Tables From a Binary Tarball

If you install a [binary tarball](../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) package in a non standard path, like your home directory, and if you already have a MariaDB / MySQL package installed, then you may get conflicts\
with the default `/etc/my.cnf`. This often results in permissions\
errors.

One possible solution is to use the `--no-defaults` option, so that it does not read any [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
./scripts/mariadb-install-db --no-defaults --basedir=. --datadir=data
```

Another possible solution is to use the `defaults-file` option, so that you can specify your own [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
./scripts/mariadb-install-db --defaults-file=~/.my.cnf
```

## User Accounts Created by Default

`mariadb-install-db` sets `--auth-root-authentication-method=socket` by default. When this is set, the default `root@localhost` user account is created with the ability to use two [authentication plugins](../../reference/plugins/authentication-plugins/):

* First, it is configured to try to use the [unix\_socket](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin. This allows the `root@localhost` user to login without a password via the local Unix socket file defined by the [socket](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#socket) system variable, as long as the login is attempted from a process owned by the operating system `root` user account.
* Second, if authentication fails with the [unix\_socket](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin, then it is configured to try to use the [mysql\_native\_password](../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin.

The definition of the default `root@localhost` user account is:

```
CREATE USER 'root'@'localhost' IDENTIFIED VIA unix_socket 
  OR mysql_native_password USING 'invalid';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION;
```

Since `mariadb-install-db` sets `--auth-root-authentication-method=socket` by default, the following additional user accounts are **not** created by default:

* `root@127.0.0.1`
* `root@::1`
* `root@${current_hostname}`

However, an additional user account that is defined by the `--auth-root-socket-user` option is created. If this option is not set, then the value defaults to the value of the `--user` option. On most systems, the `--user` option will use the value of `mysql` by default, so this additional user account would be called `mysql@localhost`.

The definition of this `mysql@localhost` user account is similar to the `root@localhost` user account:

```
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket 
  OR mysql_native_password USING 'invalid';
GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'localhost' WITH GRANT OPTION;
```

An invalid password is initially set for both of these user accounts. This means that before a password can be used to authenticate as either of these user accounts, the accounts must first be given a valid password by executing the [SET PASSWORD](../../reference/sql-statements/account-management-sql-statements/set-password.md) statement.

For example, here is an example of setting the password for the `root@localhost` user account immediately after installation:

```bash
$ sudo yum install MariaDB-server
$ sudo systemctl start mariadb
$ sudo mariadb
...
MariaDB> SET PASSWORD = PASSWORD('XH4VmT3_jt');
```

You may notice in the above example that the [mariadb](../mariadb-client/mariadb-command-line-client.md) command-line client is executed via [sudo](https://linux.die.net/man/8/sudo). This allows the `root@localhost` user account to successfully authenticate via the [unix\_socket](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin.

## Troubleshooting Issues

### Checking the Error Log

If `mariadb-install-db` fails, you should examine the [error log](../../server-management/server-monitoring-logs/error-log.md) in the data directory, which is the directory specified with `--datadir` option. This should provide a clue about what went wrong.

### Testing With mariadbd

You can also test that this is not a general fault of MariaDB Server by trying to start the `mariadbd` process. The [-skip-grant-tables](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#skip-grant-tables) option will tell it to ignore the [system tables](../../reference/system-tables/). Enabling the [general query log](../../server-management/server-monitoring-logs/general-query-log.md) can help you determine what queries are being run on the server. For example:

```bash
mariadbd --skip-grant-tables --general-log
```

At this point, you can use the [mariadb](../mariadb-client/) client to connect to the [mysql](../../reference/system-tables/the-mysql-database-tables/) database and look at the [system tables](../../reference/system-tables/). For example:

```bash
$ /usr/local/mysql/bin/mysql -u root mysql
MariaDB [mysql]> show tables
```

## Using a Server Compiled With --disable-grant-options

The following only apply in the exceptional case that you are using a mariadbd server which is configured with the `--disable-grant-options` option:

`mariadb-install-db` needs to invoke `mariadbd` with the`--bootstrap` and `--skip-grant-tables` options.\
A MariaDB configured with the `--disable-grant-options`\
option has `--bootstrap` and `--skip-grant-tables`\
disabled. To handle this case, set the `MYSQLD_BOOTSTRAP` environment\
variable to the full path name of a mariadbd server that is configured without `--disable-grant-options`. `mariadb-install-db` will use that server.

## The test and test\_% Databases

When calling the `mariadb-install-db` script, a new folder called `test` is created in the data directory.\
It only has the single `db.opt` file, which sets the client options `default-character-set` and `default-collation` only.

If you run `mysql` as an anonymous user, `mysql -u''@localhost`, and look for the grants and databases you are able to work with, you will get the following:

```sql
SELECT current_user;
+--------------+
| current_user |
+--------------+
| @localhost   |
+--------------+

SHOW GRANTS FOR current_user;
+--------------------------------------+
| Grants for @localhost                |
+--------------------------------------+
| GRANT USAGE ON *.* TO ``@`localhost` |
+--------------------------------------+

SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
+--------------------+
```

Shown are the `information_schema` as well as `test` databases that are built in databases.\
But looking from [SHOW GRANTS](../../reference/sql-statements/administrative-sql-statements/show/show-grants.md) appears to be a paradox; how can the current user see something if they don't have privileges for that?

Let's go a step further.\
Now, use the `root`/`unix` user, which has all rights, in order to create a new database with the prefix `test_` , something like:

```sql
CREATE DATABASE test_electricity;
```

With the above change, a new directory is created in the data directory.\
Now login again with the anonymous user and run [SHOW DATABASES](../../reference/sql-statements/administrative-sql-statements/show/show-databases.md):

```sql
SHOW DATABASES
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
| test_electricity   |
+--------------------+
```

Again we are able to see the newly created database, without any rights?\
We have an anonymous user that has no privileges, but still can see the `test` and `test_electricity` databases. Where does this come from?

Log in with the `root`/`unix` user to find out all privileges that the anonymous user has:

```sql
SELECT * FROM mysql.user WHERE user='' AND host='localhost'\G
*************************** 1. row ***************************
                  Host: localhost
                  User: 
              Password: 
           Select_priv: N
           Insert_priv: N
           Update_priv: N
           Delete_priv: N
           Create_priv: N
             Drop_priv: N
           Reload_priv: N
         Shutdown_priv: N
          Process_priv: N
             File_priv: N
            Grant_priv: N
       References_priv: N
            Index_priv: N
            Alter_priv: N
          Show_db_priv: N
            Super_priv: N
 Create_tmp_table_priv: N
      Lock_tables_priv: N
          Execute_priv: N
       Repl_slave_priv: N
      Repl_client_priv: N
      Create_view_priv: N
        Show_view_priv: N
   Create_routine_priv: N
    Alter_routine_priv: N
      Create_user_priv: N
            Event_priv: N
          Trigger_priv: N
Create_tablespace_priv: N
   Delete_history_priv: N
              ssl_type: 
            ssl_cipher: 
           x509_issuer: 
          x509_subject: 
         max_questions: 0
           max_updates: 0
       max_connections: 0
  max_user_connections: 0
                plugin: 
 authentication_string: 
      password_expired: N
               is_role: N
          default_role: 
    max_statement_time: 0.000000
```

As seen above from the [mysql.user](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md) table, the anonymous user doesn't have any global privileges.\
Still, the anonymous user can see databases, so there must be a way so that anonymous user can see the `test` and `test_electricity` databases.

Let's check for grants on the database level. That information can be found in the [mysql.db](../../reference/system-tables/the-mysql-database-tables/mysql-db-table.md) table.\
Looking at the `mysql.db` table, it already contains 2 rows created when the `mariadb-install-db` script was invoked.

The anonymous user has database privileges (without `grant`, `alter_routine` and `execute`) on `test` and `test_%` databases:

```sql
SELECT * FROM mysql.db\G
*************************** 1. row ***************************
                 Host: %
                   Db: test
                 User: 
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: Y
           Grant_priv: N
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: N
         Execute_priv: N
           Event_priv: Y
         Trigger_priv: Y
  Delete_history_priv: Y
*************************** 2. row ***************************
                 Host: %
                   Db: test\_%
                 User: 
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: Y
           Grant_priv: N
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: N
         Execute_priv: N
           Event_priv: Y
         Trigger_priv: Y
  Delete_history_priv: Y
```

The first row is reserved for explicit usage for the `test` database, which is automatically created with `mariadb-install-db`.

Since database `test_electricity` satisfies the `test_%` pattern where `test_` is a prefix, we can understand why the user has the right to work with the newly-created database.

As long as records in `mysql.db` for the anonymous user exists, each new user created will have the privileges for the `test` and `test_%` databases.

Other databases privileges **are not automatically granted** for the newly created user. We have to grant privileges, which is visible in `mysql.db` table.

### Not Creating the test Database and Anonymous User

If you run `mariadb-install-db` with the `--skip-test-db` option, no `test` database is created, which we can see as follows:

```sql
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+

SELECT * FROM mysql.db;
Empty set (0.001 sec)
```

Also, no anonymous user is created (only `unix`/`mariadb.sys`/`root` users):

```sql
SELECT user,host FROM mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| anel        | localhost |
| mariadb.sys | localhost |
| root        | localhost |
+-------------+-----------+
```

## See Also

* [Configure MariaDB with catalog support](../../security/user-account-management/catalogs/starting-with-catalogs.md)
* [Installing system tables (mariadb-install-db)](mariadb-install-db.md)
* The Windows version of `mariadb-install-db`: [mysql\_install\_db.exe](../legacy-clients-and-utilities/mysql_install_db.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
