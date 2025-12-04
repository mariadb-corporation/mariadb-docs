---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT Table Types - OEM: Implemented in an External LIB

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Although CONNECT provides a rich set of table types, specific applications may need to access data organized in a way that is not handled by its existing foreign data wrappers (FDW). To handle these cases, CONNECT features an interface that enables developers to implement in C++ the required table wrapper and use it as if it were part of the standard CONNECT table type list. CONNECT can use these additional handlers providing the corresponding external module (dll or shared lib) be available.

To create such a table on an existing handler, use a Create Table statement as shown below.

```
CREATE TABLE xtab (COLUMN definitions)
ENGINE=CONNECT table_type=OEM MODULE='libname'
subtype='MYTYPE' [standard table options]
Option_list='Myopt=foo';
```

The option module gives the name of the DLL or shared library implementing the OEM wrapper for the table type. This library must be located in the plugin directory like all other plugins or UDF’s.

This library must export a function _GetMYTYPE_. The option subtype enables CONNECT to have the name of the exported function and to use the new table type. Other options are interpreted by the OEM type and can also be specified within the _option\_list_ option.

Column definitions can be unspecified only if the external wrapper is able to return this information. For this it must export a function ColMYTYPE returning these definitions in a format acceptable by the CONNECT discovery function.

Which and how options must be specified and the way columns must be defined may vary depending on the OEM type used and should be documented by the OEM type implementer(s).

## An OEM Table Example

The OEM table REST described in [Adding the REST Feature as a Library Called by an OEM Table](../connect-adding-the-rest-feature-as-a-library-called-by-an-oem-table.md) permits using REST-like tables with MariaDB binary distributions containing but not enabling the [REST table type](connect-files-retrieved-using-rest-queries.md)

Of course, the mongo (dll or so) exporting the GetREST and colREST functions must be available in the plugin directory for all this to work.

### Some Currently Available OEM Table Modules and Subtypes

| Module   | Subtype | Description                                                           |
| -------- | ------- | --------------------------------------------------------------------- |
| libhello | HELLO   | A sample OEM wrapper displaying a one line table saying “Hello world” |
| mongo    | MONGO   | Enables using tables based on MongoDB collections.                    |
| Tabfic   | FIC     | Handles files having the Windev HyperFile format.                     |
| Tabofx   | OFC     | Handles Open Financial Connectivity files.                            |
| Tabofx   | QIF     | Handles Quicken Interchange Format files.                             |
| Cirpack  | CRPK    | Handles CDR's from Cirpack UTP's.                                     |
| Tabplg   | PLG     | Access tables from the PlugDB DBMS.                                   |

How to implement an OEM handler is out of the scope of this document.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
