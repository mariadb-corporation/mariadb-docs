# Remote Client Access

Some MariaDB packages bind MariaDB to 127.0.0.1 (the loopback IP address) by default\
as a security measure using the [bind-address](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#bind_address) configuration directive. Old MySQL packages sometimes disabled TCP/IP networking altogether using the [skip-networking](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking) directive. Before going in to how to configure these, let's\
explain what each of them actually does:

* [skip-networking](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_networking) is fairly simple. It just tells MariaDB to run without any of the TCP/IP networking options.
* [bind-address](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#bind_address) requires a little bit of background information. A given\
  server usually has at least two networking interfaces (although this is not\
  required) and can easily have more. The two most common are a Loopback\
  network device and a physical Network Interface Card (NIC) which allows\
  you to communicate with the network. MariaDB is bound to the loopback\
  interface by default because it makes it impossible to connect to the TCP\
  port on the server from a remote host (the bind-address must refer to a local\
  IP address, or you will receive a fatal error and MariaDB will not start).\
  This of course is not desirable if you want to use the TCP port from a remote\
  host, so you must remove this bind-address directive or replace it either 0.0.0.0\
  to listen on all interfaces, or the address of a specific public interface.

**MariaDB starting with** [**10.11**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011)

Multiple comma-separated addresses can now be given to `bind_address` to allow the server to listen on more than one specific interface while not listening on others.

If [bind-address](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#bind_address) is bound to 127.0.0.1 (localhost), one can't connect to the MariaDB server from other hosts or from the same host over TCP/IP on a different interface than the loopback (127.0.0.1). This for example will not work (connecting with a hostname that points to a local IP of the host):

```bash
(/my/maria-10.11) ./client/mariadb --host=myhost --protocol=tcp --port=3306 test
ERROR 2002 (HY000): Can't connect to MySQL server on 'myhost' (115)
(/my/maria-10.11) telnet myhost 3306
Trying 192.168.0.11...
telnet: connect to address 192.168.0.11: Connection refused
```

Using 'localhost' works when binding with `bind_address`:

```bash
(my/maria-10.11) ./client/mariadb --host=localhost --protocol=tcp --port=3306 test
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
...
```

## Finding the Defaults File

To enable MariaDB to listen to remote connections, you need to edit your defaults\
file. See [Configuring MariaDB with my.cnf](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for more detail.

Common locations for defaults files:

```bash
* /etc/my.cnf                              (*nix/BSD)
  * $MYSQL_HOME/my.cnf                       (*nix/BSD) *Most Notably /etc/mysql/my.cnf
  * SYSCONFDIR/my.cnf                        (*nix/BSD)
  * DATADIR\my.ini                           (Windows)
```

You can see which defaults files are read and in which order by executing:

```bash
shell> mariadbd --help --verbose
mariadbd  Ver 10.11.5-MariaDB for linux-systemd on x86_64 (MariaDB Server)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Starts the MariaDB database server.

Usage: ./mariadbd [OPTIONS]

Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf
```

The last line shows which defaults files are read.

## Editing the Defaults File

Once you have located the defaults file, use a text editor to open the file and\
try to find lines like this under the \[mysqld] section:

```bash
[mysqld]
    ...
    skip-networking
    ...
    bind-address = <some ip-address>
    ...
```

(The lines may not be in this order, and the order doesn't matter.)

If you are able to locate these lines, make sure they are both commented out\
(prefaced with hash (#) characters), so that they look like this:

```bash
[mysqld]
    ...
    #skip-networking
    ...
    #bind-address = <some ip-address>
    ...
```

(Again, the order of these lines don't matter)

Alternatively, just add the following lines **at the end** of your .my.cnf (notice that the file name starts with a dot) file in your home directory or alternative **last** in your /etc/my.cnf file.

```bash
[mysqld]
skip-networking=0
skip-bind-address
```

This works as one can have any number of \[mysqld] sections.

Save the file and restart the mariadbd daemon or service (see [Starting and Stopping MariaDB](../server-management/starting-and-stopping-mariadb/)).

You can check the options mariadbd is using by executing:

```bash
shell> ./sql/mariadbd --print-defaults
./sql/mariadbd would have been started with the following arguments:
--bind-address=127.0.0.1 --innodb_file_per_table=ON --server-id=1 --skip-bind-address ...
```

It doesn't matter if you have the original --bind-address left as the later --skip-bind-address will overwrite it.

## Granting User Connections From Remote Hosts

Now that your MariaDB server installation is setup to accept connections from\
remote hosts, we have to add a user that is allowed to connect from something\
other than 'localhost' (Users in MariaDB are defined as 'user'@'host', so\
'chadmaynard'@'localhost' and 'chadmaynard'@'1.1.1.1' (or\
'chadmaynard'@'server.domain.local') are different users that can have\
completely different permissions and/or passwords.

To create a new user:

* log into the [mariadb command line client](../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) (or your favorite graphical client if you wish)

```bash
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 36
Server version: 5.5.28-MariaDB-mariadb1~lucid mariadb.org binary distribution

Copyright (c) 2000, 2012, Oracle, Monty Program Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

* if you are interested in viewing any existing remote users, issue the following SQL statement on the [mysql.user](../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table:

```sql
SELECT User, Host FROM mysql.user WHERE Host <> 'localhost';
+--------+-----------+
| User   | Host      |
+--------+-----------+
| daniel | %         |
| root   | 127.0.0.1 |
| root   | ::1       |
| root   | gandalf   |
+--------+-----------+
4 rows in set (0.00 sec)
```

(If you have a fresh install, it is normal for no rows to be returned)

Now you have some decisions to make. At the heart of every grant statement you have these things:

* list of allowed privileges
* what database/tables these privileges apply to
* username
* host this user can connect from
* and optionally a password

It is common for people to want to create a "root" user that can connect from anywhere, so as an example, we'll do just that, but to improve on it we'll create\
a root user that can connect from anywhere on my local area network (LAN), which\
has addresses in the subnet 192.168.100.0/24. This is an improvement because\
opening a MariaDB server up to the Internet and granting access to all\
hosts is bad practice.

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.100.%' 
  IDENTIFIED BY 'my-new-password' WITH GRANT OPTION;
```

(% is a wildcard)

For more information about how to use GRANT, please see the [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md)\
page.

At this point we have accomplished our goal and we have a user 'root' that can\
connect from anywhere on the 192.168.100.0/24 LAN.

## Port 3306 is Configured in Firewall

One more point to consider whether the firewall is configured to allow incoming request from remote clients:

On RHEL and CentOS 7, it may be necessary to configure the firewall to allow TCP access to MariaDB from remote hosts. To do so, execute both of these commands:

```bash
firewall-cmd --add-port=3306/tcp 
firewall-cmd --permanent --add-port=3306/tcp
```

## Caveats

* If your system is running a software firewall (or behind a hardware firewall\
  or NAT) you must allow connections destined to TCP port that MariaDB runs on (by\
  default and almost always 3306).
* To undo this change and not allow remote access anymore, simply remove the `skip-bind-address` line or uncomment the [bind-address](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#bind_address) line in your defaults file. The end result should be that you should have in the output from `./sql/mariadbd --print-defaults` the option `--bind-address=127.0.0.1` and no `--skip-bind-address`.

_The initial version of this article was copied, with permission, from_ [_Remote\_Clients\_Cannot\_Connect_](https://hashmysql.org/wiki/Remote_Clients_Cannot_Connect) _on 2012-10-30._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
