---
description: The CONNECT storage engine has been deprecated.
---

# Using CONNECT - Importing File Data Into MariaDB Tables

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Directly using external (file) data has many advantages, such as to work on “fresh” data produced for instance by cash registers, telephone switches, or scientific apparatus. However, you may want in some case to import external data into your MariaDB database. This is extremely simple and flexible using the CONNECT handler. For instance, let us suppose you want to import the data of the xsample.xml XML file previously given in example into a [MyISAM](../../myisam-storage-engine/) table called _biblio_ belonging to the connect database. All you have to do is to create it by:

```
CREATE TABLE biblio ENGINE=myisam SELECT * FROM xsampall2;
```

This last statement creates the [MyISAM](../../myisam-storage-engine/) table and inserts the original XML data, translated to tabular format by the _xsampall2_ CONNECT table, into the MariaDB _biblio_ table. Note that further transformation on the data could have been achieved by using a more elaborate Select statement in the Create statement, for instance using filters, alias or applying functions to the data. However, because the Create Table process copies table data, later modifications of the _xsample.xml_ file will not change the _biblio_ table and changes to the _biblio_ table will not modify the _xsample.xml_ file.

All these can be combined or transformed by further SQL operations. This makes working with\
CONNECT much more flexible than just using the [LOAD](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/) statement.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
