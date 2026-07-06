---
description: >-
  Extend MariaDB Server's capabilities with user-defined functions (UDFs). Learn
  how to create and implement custom functions to perform specialized operations
  directly within your SQL queries.
---

# User-Defined Functions

{% columns %}
{% column %}
{% content-ref url="user-defined-functions-overview.md" %}
[user-defined-functions-overview.md](user-defined-functions-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to User-Defined Functions (UDFs) in MariaDB, explaining how they extend the server's functionality by adding new native-like functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="creating-user-defined-functions.md" %}
[creating-user-defined-functions.md](creating-user-defined-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide for developers on writing UDFs in C/C++, covering the required interface functions, memory allocation, and thread safety.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-function-udf.md" %}
[create-function-udf.md](create-function-udf.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install a user-defined function from a shared library. This command loads an external compiled function into the server for extended capabilities.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-function-udf.md" %}
[drop-function-udf.md](drop-function-udf.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the DROP FUNCTION statement, which uninstalls a UDF and removes its entry from the system table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-defined-functions-calling-sequences.md" %}
[user-defined-functions-calling-sequences.md](user-defined-functions-calling-sequences.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Technical details on the execution flow of UDFs, explaining the sequence in which initialization, processing, and de-initialization functions are called.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-defined-functions-security.md" %}
[user-defined-functions-security.md](user-defined-functions-security.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of security measures for UDFs, including file location restrictions, required privileges, and system variable configurations.
{% endcolumn %}
{% endcolumns %}
