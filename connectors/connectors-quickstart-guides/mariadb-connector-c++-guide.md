---
description: Quickstart Guide for Connector/C++
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# MariaDB Connector/C++ Guide

## MariaDB Connector/C++ Quickstart Guide

**MariaDB Connector/C++** allows your C++ applications to connect to MariaDB databases, including support for TLS encryption. It provides an object-oriented design and leverages smart pointers for efficient memory management.

{% hint style="info" %}
The most recent **Stable (GA) release is MariaDB Connector/C++ 1.1.6**.
{% endhint %}

### Why Choose Connector/C++?

While you can use MariaDB Connector/C for C++ applications, Connector/C++ offers specific advantages for C++ development:

| **Feature**         | **Connector/C++** | **Connector/C** |
| ------------------- | ----------------- | --------------- |
| Executes SQL        | Yes               | Yes             |
| Object-Oriented     | Yes               | No              |
| Smart Pointers      | Yes               | No              |
| Implements JDBC API | Yes               | No              |

### Next Steps

To get started with MariaDB Connector/C++, you'll typically need to:

1. **Download the Connector/C++ library.** Look for the appropriate package for your operating system and development environment.
2. **Integrate the library into your C++ project.** This usually involves including header files and linking against the library during compilation.
3. **Write C++ code** to establish a connection, execute SQL queries, and process results using the object-oriented API.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
