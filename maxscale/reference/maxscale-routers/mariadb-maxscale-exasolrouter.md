---
description: >-
  Learn how to configure the Exasolrouter in MariaDB MaxScale to route
  analytical queries to Exasol while maintaining transactional workloads in
  MariaDB
---

# MariaDB MaxScale Exasolrouter

{% hint style="info" %}
This functionality is available from MaxScale 25.10.1.
{% endhint %}

> In MaxScale configuration, this module is referred to as `exasolrouter`. For documentation purposes, it is styled as `Exasolrouter` to enhance readability.

## Description

The [Exasolrouter](maxscale-exasolrouter.md) module is primarily intended to be used in combination with SmartRouter within hybrid transactional/analytical processing (HTAP) environments, where:

* **Write queries** are routed to MariaDB
* **Read queries** are routed to either MariaDB or Exasol, based on runtime performance measurements

The Exasolrouter module can also be used in standalone mode to expose Exasol through a MariaDB client protocol listener. In this configuration, MaxScale acts as a protocol bridge between MariaDB clients and the Exasol ODBC driver. This mode is primarily designed for debugging or specialized deployments.

SmartRouter measures query performance using canonical query forms (with constants replaced by placeholders). When a new canonical query is encountered, the preferred backend is based on measured response times and periodically reevaluates its decision.

For a detailed explanation of the routing algorithm, see [SmartRouter](maxscale-smartrouter.md#cluster-selection-how-queries-are-routed).

This architecture allows applications to use a single connection endpoint for both Online Transactional Processing (OLTP) and analytics workloads without application-level routing logic.

## Prerequisites

* MariaDB MaxScale **25.10.1 or later** must be installed. \
  See the [installation guide](../../maxscale-quickstart-guides/mariadb-maxscale-installation-guide.md) if required.
* MaxScale running on x86\_64 architecture
  * The Exasolrouter module uses the Exasol ODBC driver to establish communication with Exasol.
  * The Exasol ODBC driver currently requires x86\_64.
  * So, MaxScale must run on x86\_64 when using `exasolrouter`.&#x20;
* Operational MariaDB deployment
* Operational Exasol deployment
* Network connectivity between MaxScale, MariaDB, and Exasol

Default ports:

* MariaDB: 3306
* MaxScale: 3306
* Exasol: 8563

## Configuring the Exasolrouter in MariaDB MaxScale

#### Step 1. Install the Exasol ODBC driver on the MaxScale host.

The `Exasolrouter` leverages Exasol’s native ODBC connector to deliver optimal performance and full functionality.<br>

* Go to the [Exasol ODBC download page](https://downloads.exasol.com/clients-and-drivers/odbc) and select the driver version that matches the operating system of the MaxScale host.
* Download the appropriate Exasol ODBC driver for your operating system (x86\_64 architecture is required).&#x20;
* Install the downloaded driver according to the platform-specific installation instructions.

&#x20;      Replace the version number in the commands below with the version you downloaded:&#x20;

```
curl https://x-up.s3.amazonaws.com/7.x/26.2.6/Exasol_ODBC-26.2.6-Linux_x86_64.tar.gz \
-o Exasol_ODBC-26.2.6-Linux_x86_64.tar.gz
tar -xvf Exasol_ODBC-26.2.6-Linux_x86_64.tar.gz
chmod -R 755 Exasol_ODBC-26.2.6-Linux_x86_64
```

#### Step 2. Create the required users in both MariaDB and Exasol.

**MariaDB User**\
\
If you do not already have a MaxScale monitor and service user, create one using the following commands. These grants allow MaxScale to monitor the health of the MariaDB node and handle user authentication.

```
mariadb -e "DROP USER IF EXISTS maxuser@'%'"
mariadb -e "CREATE USER maxuser@'%' IDENTIFIED BY 'aBcd123%'"
mariadb -e "GRANT SUPER, RELOAD, REPLICATION CLIENT, REPLICATION SLAVE, SHOW DATABASES ON *.* TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.db TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.user TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.roles_mapping TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.tables_priv TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.columns_priv TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.proxies_priv TO maxuser@'%'"
mariadb -e "GRANT SELECT ON mysql.procs_priv TO maxuser@'%'"

```

&#x20;**Exasol User**\
\
It is considered best practice to avoid using the `sys` user for application access. Instead, create a dedicated user with the appropriate privileges.\
\
If `exaplus` utility is not available in your PATH or if you are not confirm where this utility is located on your system, you can locate it using the following command:

```
sudo su
find / -name exaplus
```

This command searches your entire system and suppresses permission-denied errors. A typical path looks like:&#x20;

```
/home/mariadbexa/.ccc/x/u/branchr/db+Titzi90-patch-2-e01f9219-64r/install/opt/exasol/db-2025.2.0/bin/Console/exaplus
```

Replace the IP address, port, and passwords to match your environment:

```
exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p syspassword \
--sql "CREATE USER admin_user IDENTIFIED BY \"aBc123%%\";"

exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p syspassword \
--sql "GRANT CREATE SESSION, CREATE TABLE, SELECT ANY TABLE, \
INSERT ANY TABLE, UPDATE ANY TABLE, DELETE ANY TABLE TO admin_user;"
```

**Important**: For all connections to Exasol, the Exasolrouter uses a **single service user**. Exasol does not currently receive user‑level authentication from MariaDB clients.

#### Step 3. Configure the MaxScale server and monitor.

Define the MariaDB server that will handle primary OLTP workloads. Replace the IP address and password to match your environment:

```
maxctrl create server mariadb1 address=127.0.0.1 port=3306 protocol=MariaDBBackend;
maxctrl create monitor mariadb_monitor mariadbmon \
  servers=mariadb1 \
  user=maxuser \
  password=aBcd123% \
  monitor_interval=1s ;
```

#### Step 4. Configure the MaxScale Exasolrouter.

Create the Exasolrouter service. This service contains the connection information for Exasol, including the ODBC driver path and credentials.<br>

```
maxctrl create service mariadb_exasolrouter exasolrouter \
user=maxuser \
password=aBcd123% p \
reprocessor=auto  ' \
connection_string=DRIVER=/home/rocky/Exasol_ODBC-26.2.6-Linux_x86_64/lib/libexaodbc.so;
EXAHOST=102.22.2.22:8563;UID=admin_user;PWD=aBc123%%;FINGERPRINT=NOCERTCHECK' 
```

Replace the following placeholders with values that match your actual environment:

* `DRIVER`: Full path to the `libexaodbc.so` file from Step 1
* `EXAHOST`: Your Exasol host and port
* `UID` and `PWD`: The Exasol user credentials created in Step 2

#### Step 5. Configure the MaxScale SmartRouter.

The SmartRouter integrates the MariaDB server with the Exasolrouter and is responsible for distributing queries between the two backends.\
\
Replace the password to match your environment:

```
maxctrl create service mariadb_smartrouter smartrouter \
  user=maxuser \
  password='aBcd123%' \
  targets=mariadb1,mariadb_exasolrouter \
  master=mariadb1
```

\
The `master` parameter designates the cluster that receives all write operations. In this configuration, all writes are directed to MariaDB.

#### Step 6: Configure the MaxScale service and listeners.

Create a listener that defines the port on which MaxScale will accept client connections for the SmartRouter service.\
\
Replace the port number if a different port is required:

```
maxctrl create listener mariadb_smartrouter mariadb_smartrouter_listener 3306
```

#### Step 7: Test and verify the configuration.

This step provides guidance on verifying whether the Exasol and SmartRouter components are connected and functioning correctly. It also explains how to enable logging for verification purposes and outlines data synchronization requirements.

*   Connecting to the service.



    First, verify that you can connect to MaxScale on the configured listener port:<br>

    <pre><code><strong>mariadb \
    </strong>  -h &#x3C;maxscale-ip> \
      -P &#x3C;mariadb exa port> \
      -u &#x3C;user> \
      -p 
    </code></pre>

    \
    Replace:

    * `<maxscale-ip>` with the IP address of your MaxScale host.
    * `<exa-listener-port>` with the port you configured for the `exasolrouter` listener.
    * `<username>` with a valid MariaDB username that MaxScale can authenticate. <br>

    To perform a very basic connectivity test:<br>

    ```
    mariadb \
    -h <maxscale-ip> \
    -P <mariadb exa port> \
    -u <user> \
    -p -e “select 1 as connected”
    ```

    \
    If the connection is established successfully, the result will return as `connected = 1`. This confirms that the client can reach MaxScale and that the router is actively listening.
*   Enabling debug logs for verification\
    \
    To verify which backend (MariaDB or Exasol) executed a query and inspect routing decisions, enable debug and info logging in MaxScale, and then tail the main logs:<br>

    ```
    maxctrl alter maxscale log_debug true
    maxctrl alter maxscale log_info true
    ```

    &#x20;\
    Then, monitor the MaxScale log:<br>

    ```
    tail -f /var/log/maxscale/maxscale.log
    ```

    \
    When SmartRouter re-measures a query, you will see log output messages similar to:<br>

    ```
    2026-02-13 18:14:49   info   : (3) [smartrouter] (mariadb_smartrouter); Trigger re-measure, schedule 2min, perf: mariadb1, 15.2181s, SELECT DISTINCT( IF( domain_new IS NOT NULL, domain_new, IF( username ...
    2026-02-13 18:15:04   info   : (3) [smartrouter] (mariadb_smartrouter); Update perf: from mariadb1, 15.2181s to mariadb1, 14.5416s, SELECT DISTINCT( IF( domain_new IS NOT NULL, domain_new, IF( username ...
    ```

    \
    These messages indicate which backend is being evaluated. \
    \
    Another way to determine how a query was executed is by using the [Hint Filter](../maxscale-filters/maxscale-hintfilter.md). You can force routing to a specific backend by adding a SQL comment.
* Data synchronizing requirements

The Exasolrouter does not automatically synchronize data between MariaDB and Exasol.&#x20;

In the event that [Change Data Capture](../../maxscale-archive/archive/mariadb-maxscale-23-02/mariadb-maxscale-23-02-protocols/mariadb-maxscale-2302-change-data-capture-cdc-users.md) (CDC) is not set up:

* Data inserted into MariaDB will not automatically appear in Exasol.
* Unless the same dataset is present in both systems, queries sent to Exasol may result in empty results.

In order to conduct relevant query testing:

* Put the same datasets into Exasol and MariaDB, or
* Set up CDC to copy data to Exasol from MariaDB.

## Behavior during Backend Unavailability

SmartRouter automatically connects to the designated master (MariaDB) in the event that Exasol is unavailable (for example, due to a network outage or unavailability). To maintain availability for OLTP activities, all reads and writes will only be sent to MariaDB.

## Known Limitations

The MariaDB MaxScale–Exasol integration includes some limitations. It includes:

* Exasol access is limited to a single service user (unlike MariaDB, which required per user authentication)
* The SQL preparser does not support all MariaDB functions.
* The following function mappings are necessary:
  * `FROM_UNIXTIME()` → `FROM_POSIX_TIME()`
  * `DATE_FORMAT` → `TO_CHAR`
* The following interactive statements are not the primary focus and may not behave as expected:
  * `SHOW TABLES`
  * `Use database`
  * `DESCRIBE table`
  * DDL statements&#x20;

## See Also

* [MaxScale Exasolrouter](maxscale-exasolrouter.md)
* [MaxScale SmartRouter](maxscale-smartrouter.md)
* [Hint Filter](../maxscale-filters/maxscale-hintfilter.md)
