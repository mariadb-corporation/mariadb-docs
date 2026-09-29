---
description: >-
  GridGain 8 thin clients are lightweight clients that connect to a cluster over
  a socket connection, available for Java, .NET/C#, C++, Python, Node.js, and PHP.
---

# Thin Clients

A thin client is a lightweight GridGain client that connects to the cluster via a standard socket connection. It does not become a part of the cluster topology, never holds any data, and is not used as a destination for compute calculations. It simply establishes a socket connection to a standard GridGain node and performs all operations through that node.

GridGain provides the following thin clients:

- [Java Thin Client](java-thin-client.md)
- [.NET/C# Thin Client](dotnet-thin-client.md)
- [C++ Thin Client](cpp-thin-client.md)
- [Python Thin Client](python-thin-client.md)
- [Node.js Thin Client](nodejs-thin-client.md)
- [PHP Thin Client](php-thin-client.md)

For a feature comparison of the clients and details on connection failover, partition awareness, and authentication, see [Thin Clients Overview](getting-started-with-thin-clients.md). For details on authorizing thin client connections, see [Client Authorization](authorization.md).
