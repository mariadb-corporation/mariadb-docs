---
description: Quickstart guide for MariaDB Connector/ODBC
---

# Connector/ODBC Guide

### Quickstart Guide: MariaDB Connector/ODBC

MariaDB Connector/ODBC is a database driver that allows applications to connect to MariaDB and MySQL databases using the Open Database Connectivity (ODBC) API. It's fully compliant with the ODBC 3.5 standard, open-source (LGPL), and can serve as a drop-in replacement for MySQL Connector/ODBC. It supports both Unicode and ANSI modes and communicates primarily using the MariaDB/MySQL binary protocol.

#### 1. What is ODBC?

ODBC (Open Database Connectivity) is a standard API for accessing database management systems (DBMS). It provides a common way for applications to communicate with different databases, abstracting away the specifics of each database's native communication protocol. MariaDB Connector/ODBC acts as the specific bridge for MariaDB.

#### 2. Installation

Installation typically involves downloading the appropriate driver package for your operating system and configuring a Data Source Name (DSN).

**a. Windows:**

1. **Download:** Go to the [MariaDB Connector/ODBC Downloads page](https://mariadb.com/downloads/#connectors) and download the appropriate `.msi` installer for your Windows version (32-bit or 64-bit).
2. **Run Installer:** Execute the downloaded `.msi` file and follow the on-screen instructions. This will install the necessary driver files.
3. **Configure DSN:**
   * Open the ODBC Data Source Administrator:
     * For 64-bit systems, search for "ODBC Data Sources (64-bit)".
     * For 32-bit systems, search for "ODBC Data Sources (32-bit)".
   * Go to the "User DSN" or "System DSN" tab (System DSN is generally preferred for broader application access).
   * Click "Add...".
   * Select "MariaDB ODBC Driver" (or "MariaDB ODBC 3.1 Driver" depending on the version) from the list and click "Finish".
   * A configuration dialog will appear. Fill in the details:
     * **Data Source Name:** A descriptive name for your DSN (e.g., `MyMariaDBDSN`).
     * **TCP/IP Server:** `localhost` or the IP address/hostname of your MariaDB server.
     * **Port:** `3306` (default MariaDB port).
     * **User:** Your database username.
     * **Password:** Your database password.
     * **Database:** The specific database you want to connect to.
   * Click "Test" to verify the connection. Click "OK" to save the DSN.

**b. Linux / macOS:**

1. **Download:** Download the appropriate `.deb`, `.rpm`, or `.pkg` package from the [MariaDB Connector/ODBC Downloads page](https://mariadb.com/downloads/#connectors).
2. **Install Package:**
   * **Debian/Ubuntu:** `sudo dpkg -i mariadb-connector-odbc_X.Y.Z.deb`
   * **Red Hat/CentOS:** `sudo rpm -i mariadb-connector-odbc-X.Y.Z.rpm`
   * **macOS:** Run the `.pkg` installer.
3.  **Configure `odbcinst.ini` and `odbc.ini`:**

    * The installer usually places the driver definition in `/etc/odbcinst.ini` (or a similar location).
    * You need to create or modify `~/.odbc.ini` (for user DSNs) or `/etc/odbc.ini` (for system DSNs) to define your data source.

    **Example `odbcinst.ini` (Driver Definition - usually installed automatically):**

    ```toml
    [MariaDB ODBC Driver]
    Description = MariaDB Connector/ODBC
    Driver = /usr/lib/x86_64-linux-gnu/odbc/libmaodbc.so # Adjust path for your system
    Setup = /usr/lib/x86_64-linux-gnu/odbc/libmaodbc.so # Adjust path for your system
    UsageCount = 1
    FileUsage = 1
    CPTimeout =
    CPReconnect =
    ```

    **Example `odbc.ini` (DSN Definition):**

    ```toml
    [MyMariaDBDSN]
    Description = My MariaDB Database
    Driver = MariaDB ODBC Driver # Matches the name from odbcinst.ini
    SERVER = localhost
    PORT = 3306
    DATABASE = your_database_name
    UID = your_username
    PASSWORD = your_password
    OPTION =
    ```
4.  **Test DSN (Optional):** You can use `isql` (from `unixodbc-dev` or `unixodbc` package) to test your DSN:

    ```bash
    isql MyMariaDBDSN your_username your_password
    ```

#### 3. Basic Usage (Connecting from Applications)

Once the MariaDB ODBC driver is installed and a DSN is configured, applications can connect to your MariaDB database using the standard ODBC API. The exact code will vary depending on the programming language and framework you are using (e.g., C++, Java with JDBC-ODBC Bridge, Python with `pyodbc`, PHP with `odbc` extension).

**a. Connecting via DSN (Common for many applications):**

Many applications and tools (like Microsoft Excel, reporting tools, or C++ applications using ODBC) will allow you to select a configured DSN directly.

**b. Connecting via DSN-less Connection String:**

You can also provide a full connection string directly in your application without pre-configuring a DSN. This is often used in scripting languages or when you need more dynamic control.

```
Driver={MariaDB ODBC Driver};Server=localhost;Port=3306;Database=your_database_name;Uid=your_username;Pwd=your_password;
```

Replace `{MariaDB ODBC Driver}` with the exact driver name from your `odbcinst.ini` if different.

#### Further Resources:

* [MariaDB Connector/ODBC Documentation](../mariadb-connector-odbc/)
* [MariaDB Connector/ODBC Downloads](https://mariadb.com/downloads/#connectors)
