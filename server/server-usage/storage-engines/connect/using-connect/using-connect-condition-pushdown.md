---
description: The CONNECT storage engine.
---

# Using CONNECT - Condition Pushdown

The [ODBC](../connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md), [JDBC](../connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md), [MYSQL](../connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md), [TBL](../connect-table-types/connect-tbl-table-type-table-list.md) and WMI table types use engine condition pushdown in order to restrict the number of rows returned by the RDBS source or the WMI component.

The CONDITION\_PUSHDOWN argument used in old versions of CONNECT is no longer needed because CONNECT uses condition pushdown unconditionally.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
