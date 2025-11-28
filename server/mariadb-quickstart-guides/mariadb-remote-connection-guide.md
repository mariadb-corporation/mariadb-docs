---
description: Remote Access Configuration Guide
---

# Configuring MariaDB for Remote Client Access Guide

This guide explains how to configure your MariaDB server to accept connections from remote hosts. Learn to adjust crucial network settings like `bind-address`, grant appropriate user privileges for remote connections, and configure essential firewall rules.

### Understanding Key Network Directives

Two main configuration directives control MariaDB's network accessibility:

* **`skip-networking`**: If this directive is enabled, MariaDB will not listen for TCP/IP connections at all. All interaction must be through local mechanisms like Unix sockets or named pipes.
* **`bind-address`**: This directive specifies the IP address the server listens on.
  * By default, for security, many MariaDB packages bind to `127.0.0.1` (localhost). This means the server will only accept connections originating from the server machine itself via the loopback interface. Remote connections will fail.
  *   If `bind-address` is set to `127.0.0.1`, attempting to connect from another host, or even from the same host using a non-loopback IP address, will result in errors like:

      ```sql
      ERROR 2002 (HY000): Can't connect to MySQL server on 'myhost' (115)
      ```

      A `telnet myhost 3306` test would likely show "Connection refused."
  * To allow connections from other hosts, you must either comment out the `bind-address` directive (making MariaDB listen on all available network interfaces, i.e., `0.0.0.0` for IPv4), or set it to a specific public IP address of the server.
  * **MariaDB 10.11 and later:** `bind-address` can accept multiple comma-separated IP addresses, allowing the server to listen on specific interfaces while excluding others.

Connecting via `localhost` typically works even if `bind-address` is `127.0.0.1` (using the loopback interface):

```bash
./client/mariadb --host=localhost --protocol=tcp --port=3306 test
```

Locating the MariaDB Configuration File

To change these network settings, you need to edit MariaDB's configuration file (often named `my.cnf` or `my.ini`).

* See [Configuring MariaDB with my.cnf](../ha-and-performance/optimization-and-tuning/system-variables/sample-mycnf-files.md) for comprehensive details.
* **Common Locations:**
  * `/etc/my.cnf` (Unix/Linux/BSD)
  * `/etc/mysql/my.cnf` (Common on Debian/Ubuntu)
  * `$MYSQL_HOME/my.cnf` (Unix/Linux/BSD, where `$MYSQL_HOME` is MariaDB's base directory)
  * `SYSCONFDIR/my.cnf` (Compile-time specified system configuration directory)
  * `DATADIR\my.ini` (Windows, in the data directory)
  * `~/.my.cnf` (User-specific configuration file)
*   **Identifying Loaded Files:** To see which configuration files your `mariadbd` server instance reads and in what order, execute:

    Bash

    ```bash
    mariadbd --help --verbose
    ```

    Look for a line similar to: `Default options are read from the following files in the given order: /etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf`

### Modifying the Configuration File for Remote Access

1. **Open the File:** Use a text editor to open the primary configuration file identified (e.g., `/etc/mysql/my.cnf`).
2. **Locate `[mysqld]` Section:** Find the section starting with `[mysqld]`.
3. **Adjust Directives:**
   *   If `skip-networking` is present and enabled (not commented out with `#`), comment it out or set it to `0`:Ini, TOML

       ```toml
       #skip-networking
       ```

       orIni, TOML

       ```toml
       skip-networking=0
       ```
   *   If `bind-address = 127.0.0.1` (or another loopback/specific IP that's too restrictive) is present:

       * To listen on all available IPv4 interfaces: Comment it out entirely (`#bind-address = 127.0.0.1`) or set `bind-address = 0.0.0.0`.
       * To listen on a specific public IP address of your server: `bind-address = <your_server_public_ip>`.
       * Alternatively, to effectively disable binding to a specific address and listen on all, you can add `skip-bind-address`. Example changes:

       ```toml
       [mysqld]
       ...
       #skip-networking
       #bind-address = 127.0.0.1
       ...
       ```

       Or, to be explicit for listening on all interfaces if `bind-address` was previously restrictive:

       ```toml
       [mysqld]
       bind-address = 0.0.0.0
       ```
4. **Save and Restart:** Save the configuration file and restart the MariaDB server service.
   * See [Starting and Stopping MariaDB](../server-management/starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md) for instructions.
5.  **Verify Settings (Optional):** You can check the options `mariadbd` is effectively using by running:

    ```bash
    ./sql/mariadbd --print-defaults  # Adjust path to mariadbd if necessary
    ```

    Look for the effective `bind-address` value or the absence of `skip-networking`. If multiple `[mysqld]` sections or `skip-bind-address` are used, the last specified prevailing value is typically what counts.

### Granting User Privileges for Remote Connections

Configuring the server to listen for remote connections is only the first step. You must also grant privileges to user accounts to connect from specific remote hosts. MariaDB user accounts are defined as `'username'@'hostname'`.

1.  **Connect to MariaDB:**

    ```bash
    mariadb -u root -p
    ```
2.  **View Existing Remote Users (Optional):**SQL

    ```sql
    SELECT User, Host FROM mysql.user 
    WHERE Host <> 'localhost' AND Host <> '127.0.0.1' AND Host <> '::1';
    ```
3. **Grant Privileges:** Use the `GRANT` statement to allow a user to connect from a remote host or a range of hosts.
   * **Syntax Elements:**
     * Privileges (e.g., `ALL PRIVILEGES`, `SELECT, INSERT, UPDATE`)
     * Database/tables (e.g., `database_name.*` for all tables in a database, `*.*` for all databases)
     * Username
     * Host (IP address, hostname, or subnet with wildcards like `%`)
     * Password (using `IDENTIFIED BY 'password'`)
   *   **Example: Grant `root`-like access from a specific LAN subnet:** It's highly discouraged to allow `root` access from all hosts (`'root'@'%'`) directly to the internet. Instead, restrict it to trusted networks if necessary.

       SQL

       ```sql
       GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.100.%'
         IDENTIFIED BY 'my-very-strong-password' WITH GRANT OPTION;
       FLUSH PRIVILEGES;
       ```

       This allows the `root` user to connect from any IP address in the `192.168.100.x` subnet. Replace `'my-very-strong-password'` with a strong, unique password.
   * For creating less privileged users or more granular permissions, see the [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md) documentation.

### Configuring Your Firewall

Even if MariaDB is configured for remote access, a firewall on the server (software or hardware) might block incoming connections on MariaDB's port (default is `3306`).

*   **RHEL/CentOS 7 Example (using `firewall-cmd`):**

    ```bash
    sudo firewall-cmd --add-port=3306/tcp --permanent
    sudo firewall-cmd --reload
    ```

    The first command adds the rule, the second makes it persist after reboots and applies the changes. Consult your OS/firewall documentation for specific commands.

### Important Considerations and Reverting Changes

* **Security:** Opening MariaDB to remote connections, especially to the internet, increases security risks. Always use strong passwords, grant minimal necessary privileges, and restrict host access as much as possible. Consider using TLS/SSL for encrypted connections (see [Secure Connections Overview](../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md)).
* **Reverting:** To disable remote access and revert to a more secure local-only setup:
  1. Edit your MariaDB configuration file.
  2. Ensure `skip-networking` is not enabled (or is `0`).
  3. Set `bind-address = 127.0.0.1` explicitly, or remove any `skip-bind-address` directive if you previously added it to listen on all interfaces. The goal is to have `bind-address=127.0.0.1` as the effective setting.
  4. Restart the MariaDB server.
  5. Review and revoke any unnecessary remote `GRANT` privileges.

_The initial version of this article was copied, with permission, from_ [_Remote\_Clients\_Cannot\_Connect_](https://hashmysql.org/wiki/Remote_Clients_Cannot_Connect) _on 2012-10-30._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
