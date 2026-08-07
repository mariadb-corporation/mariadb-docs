---
description: >-
  Connecting to a GridGain 9 cluster from the Java, .NET, .NET LINQ, C++, and
  Python clients, and via the Python DB API.
---

# Connecting to Your Cluster

You can connect to your cluster by using the following clients:

- [Java client](#java-client)
- [.NET client](#net-client)
- [.NET LINQ client](#net-linq-client)
- [C++ client](#c-client)
- [Python client](#python-client)
- [Python DB API](#python-db-api)

## Connection URI and API credentials

All examples below use the following values:

- `{connectionUri}` -- obtain from the [Connections widget](my-cluster.md)
- `{login}` and `{password}` -- obtain from the [My cluster tab](my-cluster.md).

## Java client

The Java thin client connects to the cluster via a standard socket connection. It does not become a part of the cluster topology, never holds any data, and is not used as a destination for compute calculations. The thin client simply establishes a socket connection to a standard node​ and performs all operations through that node.

1. Add the following dependencies to your Maven project:

   {% hint style="info" %}
   The `{gg.version}` parameter should match the version of the managed cluster. You can find this information on the [Cluster Management screen](../../cluster-management.md) or on the [My cluster tab](my-cluster.md).
   {% endhint %}

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
           <version>${gg.version}</version>
       </dependency>
   </dependencies>
   ```
2. Create a client configuration and replace the `{login}` and `{password}` placeholders with your cluster credentials. Replace the `{connectionUri}` with the connection URI from the **Connections** widget.

   ```java
       public static void main(String[] args) {
           SslConfiguration sslConfiguration = new SslConfigurationBuilder()
                   .enabled(true)
                   .build();
           IgniteClientAuthenticator auth = BasicAuthenticator.builder()
                   .username("{login}")
                   .password("{password}")
                   .build();
           // Connect to the cluster.
           try (IgniteClient client = IgniteClient.builder()
                   .addresses("{connectionUri}:10800")
                   .authenticator(auth)
                   .ssl(sslConfiguration)
                   .build()) {
           // Query the table using SQL.
               client.sql().execute(null, "CREATE TABLE IF NOT EXISTS Person (id VARCHAR PRIMARY KEY, name VARCHAR)");

           }
       }
   ```

For more information on Java client, see [this article](https://www.gridgain.com/docs/gridgain9/latest/developers-guide/clients/java#java-client).

## C++ client

1. Add the GridGain C++ client library to your project. Include the following headers:
   - `ignite/client/ignite_client.h`
   - `ignite/client/basic_authenticator.h`
2. Create a client configuration and replace the `{login}` and `{password}` placeholders with your cluster credentials. Replace the `{connectionUri}` with the connection URI from the **Connections** widget.

   ```cpp
   #include <chrono>
   #include <iostream>

   #include "ignite/client/ignite_client.h"
   #include <ignite/client/basic_authenticator.h>

   using namespace ignite;
   using namespace std::chrono_literals;

   void main()
   {
   try {
   auto auth = std::make_shared<basic_authenticator>("{login}", "{password}");
   ignite_client_configuration cfg{"{connectionUri}:10800"};
   cfg.set_authenticator(std::move(auth));
   cfg.set_ssl_mode(ssl_mode::REQUIRE);

       // Connect to the cluster.
       auto client = ignite_client::start(std::move(cfg), 5s);
       auto sql = client.get_sql();

       // Query the table using SQL.
       sql.execute(nullptr, {"CREATE TABLE Person(ID INT PRIMARY KEY, VAL VARCHAR)"}, {});
     } catch (std::exception &e) {
       std::cout << e.what() << std::endl;
       return 1;
     }
   }
   ```

For more information on C++ client, see [this article](https://www.gridgain.com/docs/gridgain9/latest/developers-guide/clients/cpp).

## .NET client

Supported runtimes: .NET 8.0+

1. Install [.NET SDK](https://dotnet.microsoft.com/en-us/download)
2. Copy the Program and dependency example files to an empty folder.
3. Replace `{gg.version}` with the version of the managed cluster.
4. Replace the `{login}` and `{password}` placeholders with your cluster API credentials.
5. Execute `dotnet run` in that folder.

For more information on .NET client, see [this article](https://gridgain.com/docs/gridgain9/latest/developers-guide/clients/dotnet#net-client).

## .NET LINQ client

Supported runtimes: .NET 8.0+

1. Install [.NET SDK](https://dotnet.microsoft.com/en-us/download)
2. Copy the Program and dependency example files to an empty folder.
3. Replace `{gg.version}` with the version of the managed cluster.
4. Replace the `{login}` and `{password}` placeholders with your cluster API credentials.
5. Execute `dotnet run` in that folder.

For more information on .NET LINQ client, see [this article](https://gridgain.com/docs/gridgain9/latest/developers-guide/clients/linq#net-linq-queries).

## Python client

1. Install the pygridgain package:

   ```bash
   pip install pygridgain>=9
   ```
2. Create a client configuration and replace the `{login}` and `{password}` placeholders with your cluster credentials. Replace the `{connectionUri}` with the connection URI from the **Connections** widget.

   ```python
   import asyncio
   import ssl
   from pygridgain import AsyncClient, EndPoint, BasicAuthenticator, SSLConfig
   async def main():
   # Client configuration.
   # Replace the {login} and {password} with your cluster credentials.
   address = EndPoint("{connectionUri}", 10800)
   auth = BasicAuthenticator(username="{login}", password="{password}")
   ssl_cfg = SSLConfig(cert_reqs=ssl.CERT_NONE)
   # Connect to the cluster.
   async with AsyncClient(
       address,
       authenticator=auth,
       ssl_config=ssl_cfg,
   ) as client:
       # Get or create a BinaryMap (cache-like key/value structure).
       my_map = await client.structures().get_or_create_binary_map("MyTestMap")
       # Put/get example.
       await my_map.put(b"1", b"foo")
       result = await my_map.get(b"1")
       # Print the decoded result.
       print(result.decode("utf-8"))
       # Optional checks.
       exists = await my_map.contains(b"1")
       print("Key exists:", exists)
   ```

For more information on Python client, see [this article](https://gridgain.com/docs/gridgain9/latest/developers-guide/clients/python-client).

## Python DB API

1. Install the pygridgain_dbapi package:

   ```bash
   pip install pygridgain_dbapi
   ```

   {% hint style="info" %}
   On macOS, if you encounter SSL-related build errors, set the `OPENSSL_HOME` environment variable to your OpenSSL installation path. To find your OpenSSL path, run `openssl version -a`.
   {% endhint %}
2. Create a connection and replace the `{login}` and `{password}` placeholders with your cluster credentials. Replace the `{connectionUri}` with the connection URI from the **Connections** widget.

   ```python
   import pygridgain_dbapi
   HOST = "{connectionUri}"
   PORT = 10800
   IDENTITY = "{login}"
   SECRET = "{password}"
   # SQL object name.
   TABLE = "Person"
   def connect():
   return pygridgain_dbapi.connect(
   address=f"{HOST}:{PORT}",
   identity=IDENTITY,
   secret=SECRET,
   use_ssl=True,
   )
   def main():
   # Connect to the cluster.
   conn = connect()
   try:
   cur = conn.cursor()

       # Create table.
       cur.execute(
           f"CREATE TABLE IF NOT EXISTS {TABLE} ("
           f"  id INTEGER PRIMARY KEY, "
           f"  name VARCHAR"
           f")"
       )

       # Insert values into the table.
       cur.execute(
           f"INSERT INTO {TABLE}(id, name) VALUES "
           f"(1, 'Ed'), (2, 'Ann'), (3, 'Emma')"
       )
       # Count.
       cur.execute(f"SELECT COUNT(*) FROM {TABLE}")
       count = cur.fetchone()[0]
       print(f"COUNT(*) FROM {TABLE} = {count}")
       # Commit is recommended for DDL/DML in DB-API usage.
       conn.commit()
   finally:
   # Close the connection.
   conn.close()
   ```

For more information on Python DB API, see [this article](https://gridgain.com/docs/gridgain9/latest/developers-guide/clients/python).
