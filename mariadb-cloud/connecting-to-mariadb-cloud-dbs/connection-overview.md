# Connection Overview

This page describes connecting to a MariaDB Cloud database using the following options:

* MariaDB-compatible client
* From your application
* Through SQL tools
  * GUI Clients

{% hint style="info" %}
**Whitelist IP Address**\
Access to all services is by default protected by a firewall. You need to whitelist your client’s (your desktop, laptop or server) IP address before connecting. Select ‘Manage —> Security Access’ and then click ‘Add my current IP’ to add the IP of your current workstation (laptop, desktop).
{% endhint %}

{% hint style="danger" %}
**Warning**: Using `0.0.0.0/0` will disable the firewall. Never do this for production databases.\
For more details, go to the [Firewall](<../Security/Configuring Firewall.md>) settings page.
{% endhint %}

## Connecting Using the MariaDB Client

Once your DB service is launched, click on the ‘Connect’ option for your service on the dashboard. This pops up all the required attributes to connect from any SQL client.

Connection parameters include:

* Default username
* Default password
* Hostname (Fully Qualified Domain Name)
* TCP port (3306 or 3307)
* ssl-verify-server-cert (if SSL is ON)

{% hint style="info" %}
Unlike previous MariaDB Cloud versions, the current version no longer requires clients to supply the Server SSL Certificate for SSL connections. Customers who migrated from MariaDB corporation to MariaDB Cloud Inc can continue to use provided certificates (when using the previous MariaDB Cloud method for connecting). But we strongly recommend moving to the connection properties as shown in the Connect window for your service.
{% endhint %}

<figure><img src="../.gitbook/assets/connect_window.png" alt=""><figcaption></figcaption></figure>

## Connecting From Your Application

Applications can connect to MariaDB Cloud using any of the below MariaDB supported connectors. There are several other connectors from the community too.

* [C](connect-from-c-app.md)
* [C++](connect-from-c++-app.md)
* [Java](connect-from-java-app.md)
* [Java R2DBC](connect-using-connector-r2dbc.md)
* [Node.js (JavaScript)](connect-from-node-js-app.md)
* [ODBC API](connect-using-odbc.md)
* [Python](connect-from-python-app.md)
* [MongoDB Client](connect-from-mongodb-clients.md)

{% hint style="info" %}
For Server with Replicas, you can also use any MongoDB client and use the [NoSQL Interface](connect-from-mongodb-clients.md).
{% endhint %}

## Connecting From SQL Tools

Clients listed here have been tested to properly connect with MariaDB Cloud and execute queries.

Most of the SQL clients and editors natively support MariaDB. Most often you can also just select 'MySQL' and connect to your MariaDB Cloud DB service.

* [Connecting using Java clients like Squirrel SQL](https://squirrel-sql.sourceforge.io/)
  * All you need to do is to make sure the "useSsl" property is set to 'true' if SSL is ON.
* MariaDB CLI
* [Sequel Ace](https://sequel-ace.com/) - Connect to MariaDB from MacOS
  * In the connection window, you should select 'Require SSL' if your MariaDB Cloud database has SSL turned ON (the default).

### Graphical User Interfaces (GUIs)

The following GUI clients have been tested to properly connect with MariaDB Cloud and execute queries. Most SQL clients and editors natively support MariaDB. You can often select 'MySQL' as the connection type to connect to your MariaDB Cloud DB service.

* [Connect using DBeaver](database-tools/dbeaver.md) (CloudDBA recommended)
* [Connect using DBGate](database-tools/dbgate.md)
* [Connect using HeidiSQL](database-tools/heidisql.md)
* [Connect using TablePlus](database-tools/tableplus.md)

