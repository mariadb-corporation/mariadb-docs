# Fixing Connection Issues

If you are completely new to MariaDB and relational databases, you may want to start with the [MariaDB Primer](../../mariadb-quickstart-guides/mariadb-usage-guide.md). Also, make sure you understand the connection parameters discussed in the [Connecting to MariaDB](../../mariadb-quickstart-guides/mariadb-connecting-guide.md) article.

There are a number of common problems that can occur when connecting to MariaDB.

### Server Not Running in Specified Location

If the error you get is something like:

```bash
mariadb -uname -p -uname -p
ERROR 2002 (HY000): Can't connect to local MySQL server through 
  socket '/var/run/mysqld/mysqld.sock' (2 "No such file or directory")
```

or

```bash
mariadb -uname -p --port=3307 --protocol=tcp
ERROR 2003 (HY000): Can't connect to MySQL server on  'localhost' 
  (111 "Connection refused")
```

the server is either not running, or not running on the specified port, socket or pipe. Make sure you are using the correct host, port, pipe, socket and protocol options, or alternatively, see [Getting, Installing and Upgrading MariaDB](../../server-management/install-and-upgrade-mariadb/), [Starting and Stopping MariaDB](../../server-management/starting-and-stopping-mariadb/) or [Troubleshooting Installation Issues](../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/).

The socket file can be in a non-standard path. In this case, the `socket` option is probably written in the my.cnf file. Check that its value is identical in the \[mysqld] and \[client] sections; if not, the client will look for a socket in a wrong place.

If unsure where the Unix socket file is running, it's possible to find this out, for example:

```bash
netstat -ln | grep mysqld
unix  2      [ ACC ]     STREAM     LISTENING     33209505 /var/run/mysqld/mysqld.sock
```

### Unable to Connect from a Remote Location

Usually, the MariaDB server does not by default accept connections from a remote client or connecting with tcp and a hostname and has to be configured to permit these.

```bash
(/my/maria-10.4) ./client/mysql --host=myhost --protocol=tcp --port=3306 test
ERROR 2002 (HY000): Can't connect to MySQL server on 'myhost' (115)
(/my/maria-10.4) telnet myhost 3306
Trying 192.168.0.11...
telnet: connect to address 192.168.0.11: Connection refused
(/my/maria-10.4) perror 115
OS error code 115:  Operation now in progress
```

To solve this, see [Configuring MariaDB for Remote Client Access](../../mariadb-quickstart-guides/mariadb-remote-connection-guide.md)

### Authentication Problems

The [unix\_socket authentication plugin](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is enabled by default on Unix-like systems. This uses operating system credentials when connecting to MariaDB via the local Unix socket file. See [unix\_socket authentication plugin](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) for instructions on connecting and on switching to password-based authentication as well as [Authentication](../../security/user-account-management/authentication-from-mariadb-10-4.md) for an overview.

Authentication is granted to a particular username/host combination. `user1'@'localhost'`, for example, is not the same as `user1'@'166.78.144.191'`. See the [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md) article for details on granting permissions.

Passwords are hashed with [PASSWORD](../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. If you have set a password with the [SET PASSWORD](../../reference/sql-statements/account-management-sql-statements/set-password.md) statement, the `PASSWORD` function must be used at the same time. For example, `SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass')` rather than just `SET PASSWORD FOR 'bob'@'%.loc.gov' = 'newpass'` .

#### Problems Exporting Query Results

If you can run regular queries but get an authentication error when running the [SELECT ... INTO OUTFILE](../../reference/sql-statements/data-manipulation/selecting-data/select-into-outfile.md), [SELECT ... INTO DUMPFILE](../../reference/sql-statements/data-manipulation/selecting-data/select-into-dumpfile.md) or [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statements, you do not have permission to write files to the server. This requires the FILE privilege. See the [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md) article.

#### Access to the Server, but not to a Database

If you can connect to the server, but not to a database, for example:

```sql
USE test;
ERROR 1044 (42000): Access denied for user 'ian'@'localhost' to database 'test'
```

or can connect to a particular database, but not another, for example`mariadb -uname -p -u name db1` works but not `mariadb -uname -p -u name db2`, you have not been granted permission for the particular database. See the [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md) article.

#### Option Files and Environment Variables

It's possible that option files or environment variables may be providing incorrect connection parameters. Check the values provided in any option files read by the client you are using (see [mariadbd Configuration Files and Groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) and the documentation for the particular client you're using - see [Clients and Utilities](../../clients-and-utilities/)).

Option files can usually be suppressed with `no-defaults` option, for example:

```bash
mariadb-import --no-defaults ...
```

#### Unable to Connect to a Running Server / Lost root Password

If you are unable to connect to a server, for example because you have lost the root password, you can start the server without using the privilege tables by running the [--skip-grant-tables](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#skip-grant-tables) option, which gives users full access to all tables. You can then run [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to resume using the grant tables, followed by [SET PASSWORD](../../reference/sql-statements/account-management-sql-statements/set-password.md) to change the password for an account.

#### localhost and %

You may have created a user with something like:

```sql
CREATE USER melisa IDENTIFIED BY 'password';
```

This creates a user with the '%' wildcard host.

```sql
SELECT user,host FROM mysql.user WHERE user='melisa';
+--------+------+
| user   | host |
+--------+------+
| melisa | %    |
+--------+------+
```

However, you may still be failing to login from localhost. Some setups create anonymous users, including localhost. So, the following records exist in the user table:

```sql
SELECT user,host FROM mysql.user WHERE user='melisa' OR user='';
+--------+-----------+
| user   | host      |
+--------+-----------+
| melisa | %         |
|        | localhost |
+--------+-----------+
```

Since you are connecting from localhost, the anonymous credentials, rather than those for the 'melisa' user, are used. The solution is either to add a new user specific to localhost, or to remove the anonymous localhost user.

### See Also

* [CREATE USER](../../reference/sql-statements/account-management-sql-statements/create-user.md)
* [GRANT](../../reference/sql-statements/account-management-sql-statements/grant.md)
* [Authentication](../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [Authentication from MariaDB 10 4 video tutorial](https://www.youtube.com/watch?v=aWFG4uLbimM)
* [Error 1698: Access denied for user](../../reference/error-codes/mariadb-error-codes-1600-to-1699/e1698.md)

CC BY-SA / Gnu FDL
