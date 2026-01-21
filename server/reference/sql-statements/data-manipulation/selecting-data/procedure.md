---
description: >-
  Pass query results to a C procedure. This clause allows processing the result
  set on the server side before returning it to the client.
---

# PROCEDURE

The `PROCEDURE` clause of [SELECT](select.md) passes the whole result set to a Procedure which will process it. These Procedures are not [Stored Procedures](../../../../server-usage/stored-routines/stored-procedures/), and can only be written in the C language, so it is necessary to recompile the server.

Currently, the only available procedure is [ANALYSE](../../../sql-functions/secondary-functions/information-functions/procedure-analyse.md), which examines the resultset and suggests the optimal datatypes for each column. It is defined in the `sql/sql_analyse.cc` file, and can be used as an example to create more Procedures.

This clause cannot be used in a [view](../../../../server-usage/views/) definition.

## See Also

* [SELECT](select.md)
* [Stored Procedures](../../../../server-usage/stored-routines/stored-procedures/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
