---
description: The CONNECT storage engine has been deprecated.
---

# Using CONNECT - Exporting Data From MariaDB

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Exporting data from MariaDB is obviously possible with CONNECT in particular for all formats not supported by the [SELECT INTO OUTFILE](../../../../reference/sql-statements/data-manipulation/selecting-data/select-into-outfile.md) statement. Let us consider the query:

```sql
SELECT
    plugin_name AS handler,
    plugin_version AS version,
    plugin_author AS author,
    plugin_description AS description,
    plugin_maturity AS maturity
FROM
    information_schema.plugins
WHERE
    plugin_type = 'STORAGE ENGINE';
```

Supposing you want to get the result of this query into a file handlers.htm in XML/HTML format, allowing displaying it on an Internet browser, this is how you can do it:

Just create the CONNECT table that are used to make the file:

```sql
CREATE TABLE handout
ENGINE=CONNECT
table_type=XML
file_name='handout.htm'
header=yes
option_list='name=TABLE,coltype=HTML,attribute=border=1;cellpadding=5,headattr=bgcolor=yellow'
AS
SELECT
    plugin_name AS handler,
    plugin_version AS version,
    plugin_author AS author,
    plugin_description AS description,
    plugin_maturity AS maturity
FROM
    information_schema.plugins
WHERE
    plugin_type = 'STORAGE ENGINE';
```

Here the column definition is not given and will come from the Select statement following the Create. The CONNECT options are the same we have seen previously. This will do both actions, creating the matching _handlers_ CONNECT table and 'filling' it with the query result.

**Note 1:** This could not be done in only one statement if the table type had required using explicit CONNECT column options. In this case, firstly create the table, and then populate it with an Insert statement.

**Note 2:** The source “plugins” table column “description” is a long text column, data type not supported for CONNECT tables. It has been silently internally replaced by varchar(256).

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
