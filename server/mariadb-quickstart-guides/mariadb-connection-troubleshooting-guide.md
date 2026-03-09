---
description: >-
  Complete Troubleshooting Connection Issues Guide guide for MariaDB. Complete
  resource with setup instructions, configuration, usage examples, and best
  practices.
---

# Troubleshooting Connection Issues Guide

The guide helps diagnose and resolve common issues encountered when connecting to a MariaDB server. Identify causes for errors like 'Can't connect to local server' or access denied messages, and learn steps to effectively troubleshoot these connection problems.

If you are completely new to MariaDB and relational databases, you may want to start with [A MariaDB Primer](../server-usage/basics/mariadb-usage-guide-1.md). Also, ensure you understand the connection parameters discussed in the [Connection Parameters Guide](mariadb-connecting-guide.md).

## Server Not Running or Incorrect Location

### Symptoms

You receive errors like [client error](#user-content-fn-1)[^1] 2002 or client error 2003:

```sql
ERROR 2002 (HY000): Can't connect to local MySQL server through
  socket '/var/run/mysqld/mysqld.sock' (2 "No such file or directory")
```

```sql
mariadb -u someuser -p --port=3307 --protocol=tcp
ERROR 2003 (HY000): Can't connect to MySQL server on 'localhost'
  (111 "Connection refused")
```

### Causes & Solutions

#### Server Not Running

The MariaDB server process may not be running. Verify with `mariadb-admin`:

```bash
$ mariadb-admin status      
mariadb-admin: connect to server at 'localhost' failed
error: 'Can't connect to local server through socket '/tmp/mysql.sock' (2)'
Check that mariadbd is running and that the socket: '/tmp/mysql.sock' exists!
```

If the server isn't running, [start it using the method applicable to your environment](../server-management/starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).

#### Incorrect Parameters

The server is running, but not on the specified host, port, socket, pipe, or protocol. Verify your connection parameters.

* **Socket File Mismatch (Unix):** The socket file path might be non-standard or inconsistent between server and client configurations.
  * Check your [configuration file](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#server-option-groups). Ensure the `socket` option has the identical value for both server and client.
  *   To find the running Unix socket file, try this command:

      ```bash
      $ netstat -ln | grep mysqld
      ```

      Example output:

      ```bash
      unix  2      [ ACC ]     STREAM     LISTENING     33209505 /var/run/mysqld/mysqld.sock
      ```
* See also: [Troubleshooting Installation Issues](../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/).

## Unable to Connect from a Remote Location

### Symptoms

You can connect locally, but not from a remote machine, possibly seeing errors like this:

```bash
$ mariadb --host=myhost --protocol=tcp --port=3306 test
ERROR 2002 (HY000): Can't connect to MySQL server on 'myhost' (115)
```

You can use `telnet` (if available) to test basic network connectivity to the port:

```bash
$ telnet myhost 3306
```

A "Connection refused" message from `telnet` indicates a network or firewall issue, or that MariaDB is not listening for TCP/IP connections or on that specific interface/port.

The `perror` utility can interpret OS[^2] error codes:

```bash
$ perror 115
```

Example output:

```bash
OS error code 115: Operation now in progress
```

### Causes & Solutions

By default, MariaDB often does not accept remote TCP/IP connections, or is bound only to `localhost` (`127.0.0.1`).

**Solution:** See [Configuring MariaDB for Remote Client Access](../server-usage/connecting/mariadb-remote-connection-guide-1.md) for detailed instructions on how to enable remote connections by adjusting the `bind-address` server variable and ensuring user accounts are configured correctly for remote hosts.

## Authentication Problems

### Symptoms

Connection is established, but authentication fails (for instance, "Access denied for user...").

### Causes & Solutions

* **Unix Socket Authentication:** On Unix-like systems, the `unix_socket` authentication plugin is enabled by default for local connections via the Unix socket file. This plugin uses operating system user credentials.
  * See the [`unix_socket` authentication plugin documentation](../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) for connection instructions and how to switch to password-based authentication if needed.
  * For an overview of authentication changes in MariaDB 10.4, see [Authentication from MariaDB 10.4](../security/user-account-management/authentication-from-mariadb-10-4.md).
* **Incorrect Username/Host Combination:** Authentication is specific to a `username@host` combination. For example, `'user1'@'localhost'` is distinct from `'user1'@'166.78.144.191'`. Ensure the user account exists for the host from which you are connecting.
  * See [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md) for details on granting permissions.
* **Password Hashing:** When setting or changing passwords using `SET PASSWORD`, ensure the `PASSWORD()` function is used if the server expects hashed passwords.
  * Example: `SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass');`
  * Rather than: `SET PASSWORD FOR 'bob'@'%.loc.gov' = 'newpass';` (which might store the password as plain text, potentially leading to issues depending on the authentication plugin).

## Problems Exporting Query Results or Loading Data

### Symptoms

You can run regular queries, but get authentication or permission errors when using `SELECT ... INTO OUTFILE`, `SELECT ... INTO DUMPFILE`, or `LOAD DATA INFILE`.

### Causes & Solutions

* These operations require the `FILE` privilege on the server.
* **Solution:** Grant the necessary `FILE` privilege to the user. See the [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md) article.

## Access Denied to a Specific Database

### Symptoms

You can connect to the MariaDB server, but attempting to issue the `USE` command or query a specific database results in an error:

```sql
USE test;
ERROR 1044 (42000): Access denied for user 'youruser'@'yourhost' to database 'test'
```

Or, connecting with `mariadb -u user -p db1` works, but `mariadb -u user -p db2` fails for `db2`.

### Causes & Solutions

* The user account has not been granted sufficient privileges for that particular database.
* **Solution:** Grant the required privileges (e.g., `SELECT`, `INSERT`, etc.) on the specific database to the user. See [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md).

## Issues Due to Option Files or Environment Variables

### Symptoms

Unexpected connection behavior, or parameter usage that you didn't explicitly provide on the command line.

### Causes & Solutions

* Option files (for instance, `my.cnf`, `.my.ini`) or environment variables (for instance, `MYSQL_HOST`) might be supplying incorrect parameters, or overriding connection parameters.
* **Troubleshooting:**
  * Check the values in any option files read by your client. See [Configuring MariaDB with Option Files](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) and the documentation for the specific client you are using (listed under [Clients and Utilities](../clients-and-utilities/)).
  *   You can often suppress the reading of default option files by using a `--no-defaults` option (if supported by the client):

      ```bash
      $ mariadb --no-defaults ...
      ```

## Unable to Connect / Lost Root Password

### Symptoms

You cannot connect to a running server because the root (or other administrative) password is lost or unknown.

### Causes & Solutions

* **Solution:** You can start the MariaDB server with the `--skip-grant-tables` option. This bypasses the privilege system, granting full access. **Use this with extreme caution and only temporarily.**
  1. Stop the MariaDB server.
  2. Restart the server manually from the command line, adding the `--skip-grant-tables` option.
  3. Connect to the server (no password is required for `root@localhost`).
  4. Execute `FLUSH PRIVILEGES;` to reload the grant tables (they are now active again).
  5.  Change the password for the account you're connecting with (for example, `root`):

      ```sql
      SET PASSWORD FOR 'root'@'localhost' = PASSWORD('your_new_strong_password');
      ```
  6. Stop the server, and restart it normally (without `--skip-grant-tables`).

{% hint style="info" %}
Before doing this, particularly if you cannot connect to a freshly installed MariaDB server, see if the next solution can solve your problem.
{% endhint %}

#### Quick Fix: Access Denied for 'root'@'localhost'?

Starting with MariaDB 10.4, the default security model for Linux installations uses the `unix_socket` authentication plugin. This means the MariaDB `root` user is tied to your system's `root` user.

* **The Problem:** If you try to connect using `mariadb -u root -p`, the server may reject you because it is looking for your operating system identity, not a password.
*   **The Solution:** Instead of a password, use `sudo`:

    ```bash
    sudo mariadb
    ```
* **Why this works:** The server recognizes you have `sudo` (administrative) privileges on the machine and automatically logs you into the MariaDB `root` account without requiring a separate database password.

{% hint style="warning" %}
Do not use this as a permanent solution.

Rather than that, use it as a one-off, to be able to connect to the MariaDB Server at all. Once logged in, create a proper user, like `'myuser'@'localhost'`, or even `'myadmin'@'localhost'`. Then, [grant](../reference/sql-statements/account-management-sql-statements/grant.md) the necessary privileges to that user. An administrative user, comparable to `root`, should have privileges to access every object in your database, by running this query:

`GRANT ALL ON *.* to 'myadmin'@'localhost' IDENTIFIED BY '(your_password)' WITH GRANT OPTION`

When done, log out, then log in again, using your newly created user. This is now possible without using the `sudo` workaround:

`mariadb --user myadmin --password` (specify _your\_password_ when prompted)
{% endhint %}

## `localhost` vs. `%` Wildcard Host Issues

### Symptoms

You've created a user like `'melisa'@'%'` but cannot log in as melisa when connecting from `localhost`.

```sql
-- User created with '%' host
CREATE USER 'melisa'@'%' IDENTIFIED BY 'password';

-- Checking users in mysql.user table
SELECT user, host FROM mysql.user WHERE user='melisa' OR user='';
```

Example output showing the problem:

```sql
+--------+-----------+
| user   | host      |
+--------+-----------+
| melisa | %         |
|        | localhost | -- An anonymous user for localhost
+--------+-----------+
```

### Causes & Solutions

* The MariaDB user authentication prioritizes more specific host matches. If an anonymous user (`''@'localhost'`) exists, it can take precedence over `'melisa'@'%'` when connecting from `localhost`.
* **Solutions:**
  1.  Create a specific user for localhost:

      ```sql
      CREATE USER 'melisa'@'localhost' IDENTIFIED BY 'password_for_melisa_localhost';
      GRANT ALL PRIVILEGES ON yourdatabase.* TO 'melisa'@'localhost'; -- Grant necessary privileges
      FLUSH PRIVILEGES;
      ```
  2.  Remove the anonymous user for localhost (use with caution):

      ```sql
      DROP USER ''@'localhost';
      FLUSH PRIVILEGES;
      ```

      Ensure this doesn't break other intended anonymous access, if any.

## MariaDB Authentication Tutorial <a href="#see-also" id="see-also"></a>

{% columns %}
{% column %}
{% embed url="https://www.youtube.com/watch?v=aWFG4uLbimM" %}
MariaDB authentication from MariaDB 10.4
{% endembed %}
{% endcolumn %}

{% column %}
In this video tutorial, the MariaDB team explains the fundamental changes to the security model introduced in version 10.4, specifically regarding how the `root` user and local connections are handled.

#### Core Topics Covered:

* The "No Password" Default: Explains why, in MariaDB 10.4 and later, the `root` user does not have a password by default on many Linux distributions.
* Unix Socket Authentication: A walkthrough of the `unix_socket` plugin. This plugin allows the OS-level `root` user to log in to the MariaDB `root` account without a password, as security is verified by the operating system identity.
* The `mysql.global_priv` table: Introduction of the new table that replaces the old `mysql.user` table for storing privileges, and how this change simplifies managing multiple authentication methods for a single user.
* Switching Authentication Methods: Practical steps on how to move from socket-based authentication back to traditional password-based authentication (using the `mysql_native_password` plugin) if your environment requires it.

#### Key Takeaway for Troubleshooting:

If you are receiving an Access Denied error while trying to log in as `root` despite using a password you believe is correct, the video demonstrates that your server is likely expecting Unix Socket authentication. In this case, you should use `sudo mariadb` rather than `mariadb -u root -p`.
{% endcolumn %}
{% endcolumns %}

## See Also <a href="#see-also" id="see-also"></a>

* [CREATE USER](../reference/sql-statements/account-management-sql-statements/create-user.md)
* [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md)
* [Authentication](../security/user-account-management/authentication-from-mariadb-10-4.md)
* [Authentication from MariaDB 10 4](https://www.youtube.com/watch?v=aWFG4uLbimM) (video • 20 minutes • 2020)
* [Error 1698: Access denied for user](../reference/error-codes/mariadb-error-codes-1600-to-1699/e1698.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: Client errors are errors issued by the client, rather than the server. A typical client that issues such errors is the MariaDB command-line client, mariadb.

[^2]: Operating system
