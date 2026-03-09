---
description: The CONNECT storage engine.
---

# CONNECT PROXY Table Type

A `PROXY` table is a table that accesses and reads the data of another table or view. To create a table based on the boys `FIX` table:

```sql
CREATE TABLE xboy ENGINE=CONNECT 
  table_type=PROXY tabname=boys;
```

Simply, `PROXY` being the default type when `TABNAME` is specified:

```sql
CREATE TABLE xboy ENGINE=CONNECT tabname=boys;
```

Because the boys table can be directly used, what can be the use of a proxy table? Well, its main use is to be internally used by other table types such as [TBL](connect-tbl-table-type-table-list.md), [XCOL](connect-xcol-table-type.md), [OCCUR](connect-occur-table-type.md), or [PIVOT](connect-pivot-table-type.md). Sure enough, PROXY tables are CONNECT tables, meaning that they can be based on tables of any engines and accessed by table types that need to access CONNECT tables.

## Proxy on non-CONNECT Tables

When the sub-table is a view or not a CONNECT table, CONNECT internally creates a temporary CONNECT table of [MYSQL](connect-mysql-table-type-accessing-mysqlmariadb-tables.md) type to access it. This connection uses the same default parameters as for a `MYSQL` table. It is also possible to specify them to the `PROXY` table using in the `PROXY` declaration the same`OPTION_LIST` options as for a `MYSQL` table. Of course, it is simpler and more natural to use directly the MYSQL type in this case.

Normally, the default parameters should enable the `PROXY` table to reconnect the server. However, an issue is when the current user was logged using a password. The security protocol prevents CONNECT to retrieve this password and requires it to be given in the `PROXY` table create statement. For instance adding to it:

```
... option_list='Password=mypass';
```

However, it is often not advisable to write in clear a password that can be seen by all user able to see the table declaration by show create table, in particular, if the table is used when the current user is root. To avoid this, a specific user should be created on the local host that are used by proxy tables to retrieve local tables. This user can have minimum grant options, for instance `SELECT` on desired directories, and needs no password. Supposing ‘proxy’ is such a user, the option list to add are:

```
... option_list='user=proxy';
```

## Using a PROXY Table as a View

A `PROXY` table can also be used by itself to modify the way a table is viewed. For instance, a proxy table does not use the indexes of the object table. It is also possible to define its columns with different names or type, to use only some of them or to changes their order. For instance:

```sql
CREATE TABLE city (
  city VARCHAR(11),
  boy CHAR(12) flag=1,
  birth DATE)
ENGINE=CONNECT tabname=boys;
SELECT * FROM city;
```

This displays:

| city     | boy    | birth      |
| -------- | ------ | ---------- |
| Boston   | John   | 1986-01-25 |
| Boston   | Henry  | 1987-06-07 |
| San Jose | George | 1981-08-10 |
| Chicago  | Sam    | 1979-11-22 |
| Dallas   | James  | 1992-05-13 |
| Boston   | Bill   | 1986-09-11 |

Here we did not have to specify column format or offset because data are retrieved from the boys table, not directly from the boys.txt file. The flag option of the _boy_ column indicates that it correspond to the first column of the boys table, the _name_ column.

## Avoiding PROXY Table Loop

CONNECT is able to test whether a `PROXY`, or `PROXY`-based, table refers directly or indirectly to itself. If a direct reference can tested at table creation, an indirect reference can only be tested when executing a query on the table. However, this is possible only for local tables. When using remote\
tables or views, a problem can occur if the remote table or the view refers back to one of the local tables of the chain. The same caution should be used than when using [FEDERATEDX](../../federatedx-storage-engine/) tables.

**Note:** All `PROXY` or `PROXY`-based tables are read-only in this version.

## Modifying Operations

All [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) / [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) / [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) operations can be used with proxy tables. However, the same restrictions applying to the source table also apply to the proxy table.

Note: All PROXY and PROXY-based table types are not indexable.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
