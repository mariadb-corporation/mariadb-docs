---
description: >-
  XML functions in MariaDB Server: EXTRACTVALUE() reads text from an XML
  fragment with an XPath expression, and UPDATEXML() replaces part of it.
---

# XML Functions

MariaDB Server provides two functions for working with XML fragments stored as strings. Both take an XPath expression that selects the part of the fragment to work on.

* [EXTRACTVALUE](extractvalue.md) returns the text content of the elements that an XPath expression matches.
* [UPDATEXML](updatexml.md) replaces the element that an XPath expression matches with a new XML fragment, and returns the changed fragment.

```sql
SELECT ExtractValue('<a><b>x</b><b>y</b></a>', '/a/b[2]') AS extracted,
       UpdateXML('<a><b>x</b></a>', '/a/b', '<c>z</c>') AS updated;
```

```
+-----------+-----------------+
| extracted | updated         |
+-----------+-----------------+
| y         | <a><c>z</c></a> |
+-----------+-----------------+
```

The [Feature\_xml](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#feature_xml) status variable counts how often these functions have been used.

## Other XML Features

* [XMLTYPE](../../../data-types/string-data-types/xmltype.md) is a data type for storing XML data, available from MariaDB 12.3.
* [LOAD XML](../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-xml.md) reads data from an XML file into a table.
* The [CONNECT XML table type](../../../../server-usage/storage-engines/connect/connect-table-types/connect-xml-table-type.md) accesses an XML file as a table.
* The `--xml` option of the [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#x-xml) client and of [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#x-xml) produces XML output.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
