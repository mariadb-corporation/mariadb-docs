---
description: >-
  Connecting to a GridGain 8 cluster from the Java, .NET, C++, Python, and
  Node.js thin clients, JDBC, ODBC, the Java thick client, and the REST API.
---

# Connecting to Your Cluster

You can connect to your cluster by using the following clients:

- [Java Thin Client](#java-thin-client)
- [.NET Thin Client](#net-thin-client)
- [C++ Thin Client](#c-thin-client)
- [Python Thin Client](#python-thin-client)
- [Node.js Thin Client](#nodejs-thin-client)
- [JDBC](#jdbc)
- [ODBC](#odbc)
- [Java Thick Client](#java-thick-client)
- [REST API](#rest-api)

## Connection URI

All examples below contain the `{connectionUri}` value. You can get it from the template at the end of provisioning wizard, or

## Java Thin Client

Java thin client is a lightweight client that connects to the cluster via a standard socket connection. It does not become a part of the cluster topology, never holds any data, and is not used as a destination for compute calculations. The thin client simply establishes a socket connection to a standard node​ and performs all operations through that node.

1. Add the following dependencies to your Maven project:

   ```xml
   <repositories>
       <repository>
           <id>GridGain External Repository</id>
           <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
       </repository>
   </repositories>

   <dependencies>
       <dependency>
           <groupId>org.gridgain</groupId>
           <artifactId>ignite-core</artifactId>
           <version>8.9.20</version>
       </dependency>
   </dependencies>
   ```
2. Create a client configuration. Replace the `USER_NAME` placeholder with your cluster URL. Replace the `USER_NAME` and `PASSWORD` placeholders with your cluster credentials.

   ```java
   ClientConfiguration cfg = new ClientConfiguration()
           .setAddresses("CONNECTION_URL")
           .setUserName("USER_NAME")
           .setUserPassword("PASSWORD")
           .setSslMode(SslMode.REQUIRED);
   ```
3. Connect to the cluster.

   ```java
   try (IgniteClient client = Ignition.startClient(cfg)) {
       // Use the API.
       ClientCache<Integer, String> cache =  client.getOrCreateCache(new ClientCacheConfiguration()
               .setName("Test")
               .setBackups(1)
       );
       cache.put(1, "foo");
       System.out.println(">>>    " + cache.get(1));
   }
   ```

For more information on thin clients, please see [this article](https://www.gridgain.com/docs/latest/installation-guide/deployment-modes#thick-vs-thin-clients).

## .NET Thin Client

Prerequisites:

- Supported runtimes: .NET 4.0+, .NET Core 2.0+
- Supported OS: Windows, Linux, macOS (any OS supported by .NET Core 2.0+)

1. Install the GridGain package:

   ```bash
   dotnet add package GridGain --version 8.9.120
   ```
2. Create client configuration: Replace the `${HIDDEN_LOGIN}` and `${HIDDEN_PASSWORD}` with your cluster credentials.

   ```csharp
   var cfg = new IgniteClientConfiguration
   {
       Endpoints = new[] { "${connectionInfo?.urls[0]}:10800" },
       UserName = "${HIDDEN_LOGIN}",
       Password = "${HIDDEN_PASSWORD}",
       SslStreamFactory = new SslStreamFactory()
   };
   ```
3. Connect to the cluster.

   ```csharp
   using (var client = Ignition.StartClient(cfg))
   {
       // Use the API.
       var cache = client.GetOrCreateCache<int, string>(new CacheClientConfiguration("test") { Backups = 1 });
       cache.Put(1, "foo");
       Console.Out.WriteLine(">>>    " + cache.Get(1));
   }
   ```

For more information on .NET Thin Client, please see [this article](https://www.gridgain.com/docs/latest/developers-guide/net-specific/net-configuration-options).

## Python Thin Client

Please note the following client prerequisites: Python 3.4 or above.

### Setting Up

You can install the Python thin client either using `pip` or from a zip archive.

#### Using PIP

The python thin client package is called `pygridgain`. You can install it using the following command:

{% tabs %}
{% tab title="pip3" %}
```bash
pip3 install pygridgain
```
{% endtab %}

{% tab title="pip" %}
```bash
pip install pygridgain
```
{% endtab %}
{% endtabs %}

#### Using ZIP Archive

The thin client can be installed from the zip archive available for download from the GridGain website:

- Go to the website and download the [GridGain Python Thin Client](https://www.gridgain.com/tryfree#thinClients) archive.
- Unpack the archive and navigate to the root folder.
- Install the client using the command below.

{% tabs %}
{% tab title="pip3" %}
```bash
pip3 install .
```
{% endtab %}

{% tab title="pip" %}
```bash
pip install .
```
{% endtab %}
{% endtabs %}

This will install `pygridgain` in your environment in the so-called "develop" or "editable" mode. Learn more about the mode from the [official documentation](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

After that, import the GridGain Python thin client:

```python
from pygridgain import Client
```

### Connecting to the Cluster

1. Create client configuration: Replace the `{login}` and `{password}` with your cluster credentials.

   ```python
   client = Client(username='{login}', password='{password}', use_ssl=True)
   ```
2. Connect to the cluster.

   ```python
   client.connect('${connectionInfo.urls?.[0]}', 10800)
   ```
3. Use the API.

   ```python
   my_cache = client.get_or_create_cache('test')
   my_cache.put(1, 'foo')
   result = my_cache.get(1)
   print(result)
   ```

For more information on Python Thin Client, please see [this article](https://www.gridgain.com/docs/latest/developers-guide/thin-clients/python/1.4.0/python-thin-client).

## C++ Thin Client

GridGain on-premise comes with a C++ thin client that you can use to work with GridGain clusters.

### Setting Up

The source code of the C++ thin clien is available with the GridGain distribution package in the `{GRIDGAIN_HOME}/platforms/cpp` directory. To start working with it, install the client on your system:

```bash
mkdir cmake-build-release

cd cmake-build-release

cmake -DCMAKE_BUILD_TYPE=Release -DWITH_THIN_CLIENT=ON -DWITH_CORE=OFF -DWITH_ODBC=OFF ..

# The following installs Ignite on your system.
make install
```

### Creating a Client Instance

```cpp
#include <ignite/thin/ignite_client.h>

using namespace ignite::thin;

void main()
{
    // Create a client configuration.
    // Replace {login} and {password} values with cluster credentials.
    IgniteClientConfiguration cfg;
    cfg.SetEndPoints("your-cluster.example.com:10800");
    cfg.SetUser("{login}");
    cfg.SetPassword("{password}");
    cfg.SetSslMode(SslMode::REQUIRE);

    try
    {
        // Connect to the cluster.
        IgniteClient client = IgniteClient::Start(cfg);

        // Create the cache and put data into it.
        cache::CacheClient<int32_t, std::string> cache = client.GetOrCreateCache<int32_t, std::string>("test");
        cache.Put(1, "foo");
        std::cout << ">>>    " << cache.Get(1) << std::endl;
    }
    catch (const ignite::IgniteError& err)
    {
        std::cerr << err.GetText() << std::endl;
    }
}
```

For additional information on using C++ thin client, read the [extended article](https://www.gridgain.com/docs/8.8.13/developers-guide/thin-clients/cpp-thin-client) in GridGain documentation.

## Node.js Thin Client

Prerequisites: Node.js version 8 or higher.

1. Install the GridGain package: `npm install -g @gridgain/thin-client`:

   ```javascript
   const IgniteClient = require('@gridgain/thin-client');
   const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;
   const ObjectType = IgniteClient.ObjectType;
   async function performCacheKeyValueOperations() {
   ```
2. Create client configuration: Replace the `${HIDDEN_LOGIN}` and `${HIDDEN_PASSWORD}` with your cluster credentials.

   ```javascript
   const igniteClientConfiguration = new IgniteClientConfiguration('${connectionInfo?.urls[0]}:10800').
       setUserName('${HIDDEN_LOGIN}').
       setPassword('${HIDDEN_PASSWORD}').
       setConnectionOptions(true);
     // Connect to the cluster.
     const igniteClient = new IgniteClient();
     try {
       await igniteClient.connect(igniteClientConfiguration);
       // Use the API.
       const cache = (await igniteClient.getOrCreateCache('test')).
                 setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER);
       await cache.put(1, 'foo');
       const value = await cache.get(1);
       console.log(value);
     }
     catch (err) {
       console.log(err.message);
     }
     finally {
       igniteClient.disconnect();
     }
   }
   ```

For more information on Node.js Thin Client, please see [this article](https://www.gridgain.com/docs/latest/developers-guide/thin-clients/nodejs-thin-client).

## JDBC

GridGain is shipped with JDBC drivers that allow processing of distributed data using standard SQL statements like `SELECT`, `INSERT`, `UPDATE` or `DELETE` directly from the JDBC side.

1. Open a JDBC connection: Replace the `${HIDDEN_LOGIN}` and `${HIDDEN_PASSWORD}` with your cluster credentials.

   ```java
   try (Connection connection = DriverManager
       .getConnection("jdbc:ignite:thin://${connectionInfo?.urls[0]}:10800" +
       "?user=${HIDDEN_LOGIN}&password=${HIDDEN_PASSWORD}&sslMode=require")) {
   ```
2. Use the API:

   ```java
   try (Statement stmt = connection.createStatement()) {
       stmt.executeUpdate("CREATE TABLE IF NOT EXISTS person (id LONG PRIMARY KEY, name VARCHAR) WITH \"backups=1\"");
       stmt.execute("INSERT INTO person (id, name) VALUES (1, 'John Doe')");
       stmt.execute("INSERT INTO person (id, name) VALUES (2, 'Jane Doe')")

       try (ResultSet rs = stmt.executeQuery("SELECT id, name FROM person")) {
           while (rs.next())
               System.out.println(">>>    " + rs.getString(1) + ", " + rs.getString(2));
       }
   }
   ```

For more information on JDBC driver, please see [this article](https://www.gridgain.com/docs/latest/developers-guide/SQL/JDBC/jdbc-driver).

## ODBC

GridGain includes an ODBC driver that allows you both to select and to modify data stored in a distributed cache using standard SQL queries and native ODBC API.

### Installation

GridGain comes with an ODBC driver. If you use Windows, you can install it immediately. On Linux you will need to build it first. You can find installation and build instructions in [GridGain documentation](https://www.gridgain.com/docs/8.8.13/developers-guide/SQL/ODBC/odbc-driver#building-odbc-driver).

### Connecting to Cluster

To connect to cluster, use the following connection template. Below we will walk through the template step by step:

- Make sure to include the required dependencies in your code:

  ```cpp
  #include <sql.h>
  #include <sqlext.h>

  #include <stdio.h>
  #include <string.h>
  ```
- We will be using the following code to handle possible issues:

  ```cpp
  void PrintOdbcErrorStack(SQLSMALLINT handleType, SQLHANDLE handle)
  {
      SQLCHAR sqlState[7] = "";

      SQLCHAR message[1024];
      SQLSMALLINT messageLen = 0;

      SQLSMALLINT idx = 1;
      while (true)
      {
          memset(message, 0, sizeof(message));
          memset(sqlState, 0, sizeof(sqlState));

          SQLRETURN ret = SQLGetDiagRec(handleType, handle, idx, sqlState, NULL, message, sizeof(message), &messageLen);

          if (!SQL_SUCCEEDED(ret))
              break;

          printf("[ERROR] %s: %s\n", sqlState, message);
          ++idx;
      }
  }
  ```
- Allocate environment and connection handles:

  ```cpp
  // Allocates an environment handle.
  SQLHENV env;
  SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &env);
  if (env == NULL)
  {
      printf("Can not allocate environment handle\n");
      return;
  }

  // Allocates a connection handle.
  SQLHDBC conn;
  SQLAllocHandle(SQL_HANDLE_DBC, env, &conn);
  if (conn == NULL)
  {
      printf("Can not allocate connection handle\n");
      PrintOdbcErrorStack(SQL_HANDLE_ENV, env);
      return;
  }
  ```
- Specify that ODBC 3 will be used to connect to the cluster:

  ```cpp
  // Enables support for ODBC 3.
  SQLSetEnvAttr(env, SQL_ATTR_ODBC_VERSION, (void*)(SQL_OV_ODBC3), 0);
  ```
- Connect to the server:

  ```cpp
  // Creates a connection string.
  SQLCHAR connectStr[] =
      "DRIVER={Apache Ignite};"
      "ADDRESS=your-cluster.example.com:10800;"
      "SSL_MODE=REQUIRE;"
      "SCHEMA=PUBLIC;"
      "USER={login};"
      "PASSWORD={password}";

  // Connects to ODBC server.
  SQLRETURN ret = SQLDriverConnect(conn, NULL, connectStr, SQL_NTS, NULL, 0, NULL, SQL_DRIVER_COMPLETE);
  if (!SQL_SUCCEEDED(ret))
  {
      PrintOdbcErrorStack(SQL_HANDLE_DBC, conn);
      return;
  }
  ```
- Allocate a statement handle:

  ```cpp
  // Allocates a statement handle.
  SQLHSTMT statement;
  SQLAllocHandle(SQL_HANDLE_STMT, conn, &statement);
  if (statement == NULL)
  {
      printf("Can not allocate statement handle\n");
      PrintOdbcErrorStack(SQL_HANDLE_DBC, conn);
      return;
  }
  ```
- Create a table in the cluster:

  ```cpp
  // Creates a table.
  SQLCHAR createTableReq[] =
      "CREATE TABLE IF NOT EXISTS TEST "
      "(ID INTEGER PRIMARY KEY, VALUE VARCHAR) "
      "WITH "template=partitioned, cache_name=Test";";

  ret = SQLExecDirect(statement, createTableReq, SQL_NTS);
  if (!SQL_SUCCEEDED(ret))
  {
      PrintOdbcErrorStack(SQL_HANDLE_STMT, statement);
      return;
  }
  ```

You can find more information on working with ODBC driver in [GridGain Documentation](https://www.gridgain.com/docs/8.8.13/developers-guide/SQL/ODBC/querying-modifying-data).

## Java Thick Client

Java thick client (client node) joins the cluster via an internal protocol, receives all of the cluster-wide updates such as topology changes, is aware of data distribution, and can direct a query/operation to a server node that owns a required data set. Plus, Java thick client supports all of the GridGain APIs.

1. Add the following dependencies to your Maven project:

   ```xml
   <repositories>
       <repository>
           <id>GridGain External Repository</id>
           <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
       </repository>
   </repositories>

   <dependencies>
       <dependency>
           <groupId>org.gridgain</groupId>
           <artifactId>gridgain-core</artifactId>
           <version>8.8.10</version>
       </dependency>
       <dependency>
           <groupId>org.gridgain</groupId>
           <artifactId>ignite-indexing</artifactId>
               <version>8.9.20</version>
           </dependency>
   </dependencies>
   ```
2. Create client configuration: Replace the `{login}` and `{password}` with your cluster credentials.

   ```java
   System.setProperty("IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED", "true");
   SecurityCredentials clientCredentials = new SecurityCredentials("{login}", "{password}");
   IgniteConfiguration cfg = new IgniteConfiguration()
           .setClientMode(true)
           .setDiscoverySpi(new TcpDiscoverySpi()
                   .setIpFinder(new TcpDiscoveryVmIpFinder()
                           .setAddresses(Collections.singleton(
                                   "${connectionInfo?.urls[0]}:47500"))))
           .setCommunicationSpi(new TcpCommunicationSpi()
                   .setForceClientToServerConnections(true))
           .setPluginConfigurations(new GridGainConfiguration()
                   .setSecurityCredentialsProvider(new SecurityCredentialsBasicProvider(clientCredentials))
                   .setRollingUpdatesEnabled(true))
           .setSslContextFactory(new SslContextFactory());
   ```
3. Connect to the cluster.

   ```java
   try (Ignite client = Ignition.start(cfg)) {
       // Use the API.
       IgniteCache<Integer, String> cache =  client.getOrCreateCache(new CacheConfiguration<Integer, String>()
           .setName("Test")
           .setBackups(1)
       );
       cache.put(1, "foo");
       System.out.println(">>>    " + cache.get(1));
   }
   ```

## REST API

GridGain provides an HTTP REST client that gives you the ability to communicate with the grid over HTTP and HTTPS protocols using the REST approach.

Run the following to test your connection:

1. Replace the `{login}` and `{password}` with your cluster credentials. The response will contain a `sessionToken`.

   ```bash
   curl "https://${connectionInfo.urls[0]}:8080/ignite?cmd=authenticate&ignite.login={login}&ignite.password={password}"
   ```
2. Use the `sessionToken` in subsequent requests to avoid authenticating every time.

   ```bash
   curl "https://${connectionInfo.urls[0]}:8080/ignite?cmd=currentState&sessionToken={sessionToken}"
   ```
