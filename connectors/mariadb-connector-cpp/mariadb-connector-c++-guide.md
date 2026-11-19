---
description: Quickstart Guide for Connector/C++
---

# MariaDB Connector/C++ Overview

MariaDB Connector/C++ enables C++ applications to establish client connections to MariaDB database products over TLS.

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/0sZptD6VDS0ZF1tsWwKB/" %}

C++ applications can connect to MariaDB database products either with MariaDB Connector/C++ or [MariaDB Connector/C](../mariadb-connector-c/).

Using MariaDB Connector/C++ in C++ applications enables design with an object-oriented model and enables efficient dynamic memory allocation/de-allocation with smart pointers.

| Feature             | Connector/C++ | [Connector/C](../mariadb-connector-c/) |
| ------------------- | ------------- | -------------------------------------- |
| Executes SQL        | Yes           | Yes                                    |
| Object-Oriented     | Yes           | No                                     |
| Smart Pointers      | Yes           | No                                     |
| Implements JDBC API | Yes           | No                                     |

## Supported Versions

### Server Compatibility

MariaDB Connector/C++ connects to MariaDB database products. Individual server-side features may require a minimum server version; those requirements are noted with the feature.

### Supported Release Series

The following MariaDB Connector/C++ release series are supported:

| Release Series | Stable (GA) Date |
| -------------- | ---------------- |
| 1.1            | February 2024    |
| 1.0            | March 2021       |

1.1 is the current stable release series. The 1.0 series has passed End of Standard Support and remains available under extended support only.

For End of Standard Support and End of Life dates, along with the supported operating systems for each series, see the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/).

### Requirements

To build MariaDB Connector/C++ from source, you need:

| Requirement  | Minimum                                                           |
| ------------ | ----------------------------------------------------------------- |
| C++ standard | C++11                                                             |
| CMake        | 3.10 (3.23 on macOS)                                              |
| GCC          | 4.8, when building with GCC                                       |

The source tree includes MariaDB Connector/C, which Connector/C++ uses for client/server communication.

### Checking Your Installed Version

At runtime, retrieve the connector version from the connection's `DatabaseMetaData` object:

```cpp
std::unique_ptr<sql::Connection> conn(sql::DriverManager::getConnection(url, properties));
sql::DatabaseMetaData* metadata= conn->getMetaData();

std::cout << metadata->getDriverVersion() << std::endl;       // for example, 1.1.9
std::cout << metadata->getDriverMajorVersion() << std::endl;  // for example, 1
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
