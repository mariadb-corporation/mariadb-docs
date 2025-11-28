# CONNECT XML Table Type

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

## Overview

CONNECT supports tables represented by XML files. For these tables, the\
standard input/output functions of the operating system are not used but the\
parsing and processing of the file is delegated to a specialized library.\
Currently two such systems are supported: libxml2, a part of the GNOME\
framework, but which does not require GNOME and, on Windows, MS-DOM (DOMDOC), the Microsoft standard support of XML documents.

DOMDOC is the default for the Windows version of CONNECT and libxml2 is always\
used on other systems. On Windows the choice can be specified using the XMLSUP [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) list option, for instance specifying`option_list='xmlsup=libxml2'`.

## Creating XML tables

First of all, it must be understood that XML is a very general language used to\
encode data having any structure. In particular, the tag hierarchy in an XML\
file describes a tree structure of the data. For instance, consider the file:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<BIBLIO SUBJECT="XML">
   <BOOK ISBN="9782212090819" LANG="fr" SUBJECT="applications">
      <AUTHOR>
         <FIRSTNAME>Jean-Christophe</FIRSTNAME>
         <LASTNAME>Bernadac</LASTNAME>
      </AUTHOR>
      <AUTHOR>
         <FIRSTNAME>François</FIRSTNAME>
         <LASTNAME>Knab</LASTNAME>
      </AUTHOR>
      <TITLE>Construire une application XML</TITLE>
      <PUBLISHER>
         <NAME>Eyrolles</NAME>
         <PLACE>Paris</PLACE>
      </PUBLISHER>
      <DATEPUB>1999</DATEPUB>
   </BOOK>
   <BOOK ISBN="9782840825685" LANG="fr" SUBJECT="applications">
      <AUTHOR>
         <FIRSTNAME>William J.</FIRSTNAME>
         <LASTNAME>Pardi</LASTNAME>
      </AUTHOR>
      <TRANSLATOR PREFIX="adapté de l'anglais par">
         <FIRSTNAME>James</FIRSTNAME>
         <LASTNAME>Guerin</LASTNAME>
      </TRANSLATOR>
      <TITLE>XML en Action</TITLE>
      <PUBLISHER>
         <NAME>Microsoft Press</NAME>
         <PLACE>Paris</PLACE>
      </PUBLISHER>
      <DATEPUB>1999</DATEPUB>
   </BOOK>
</BIBLIO>
```

It represents data having the structure:

```
<BIBLIO>
                        __________|_________
                       |                    |
            <BOOK:ISBN,LANG,SUBJECT>        |
         ______________|_______________     |
        |        |         |           |    |
     <AUTHOR> <TITLE> <PUBLISHER> <DATEPUB> |
    ____|____            ___|____           |
   |    |    |          |        |          |
<FIRST> | <LAST>     <NAME>   <PLACE>       |
        |                                   |
     <AUTHOR>                   <BOOK:ISBN,LANG,SUBJECT>
    ____|____         ______________________|__________________
   |         |       |            |         |        |         |
<FIRST>   <LAST>  <AUTHOR> <TRANSLATOR> <TITLE> <PUBLISHER> <DATEPUB>
                _____|_        ___|___            ___|____
               |       |      |       |          |        |
            <FIRST> <LAST> <FIRST> <LAST>     <NAME>   <PLACE>
```

This structure seems at first view far from being tabular. However, modern\
database management systems, including MariaDB, implement something close to the\
relational model and work on tables that are structurally not hierarchical but\
tabular with rows and columns.

Nevertheless, CONNECT can do it. Of course, it cannot guess what you want to\
extract from the XML structure, but gives you the possibility to specify it\
when you create the table\[[1](connect-xml-table-type.md#_note-0)].

Let us take a first example. Suppose you want to make a table from the above\
document, displaying the node contents.

For this, you can define a table _xsamptag_ as:

```
CREATE TABLE xsamptag (
  AUTHOR CHAR(50),
  TITLE CHAR(32),
  TRANSLATOR CHAR(40),
  PUBLISHER CHAR(40),
  DATEPUB INT(4))
ENGINE=CONNECT table_type=XML file_name='Xsample.xml';
```

It are displayed as:

| AUTHOR                   | TITLE                          | TRANSLATOR   | PUBLISHER             | DATEPUB |
| ------------------------ | ------------------------------ | ------------ | --------------------- | ------- |
| Jean-Christophe Bernadac | Construire une application XML |              | Eyrolles Paris        | 1999    |
| William J. Pardi         | XML en Action                  | James Guerin | Microsoft Press Paris | 1999    |

Let us try to understand what happened. By default the column names correspond\
to tag names. Because this file is rather simple, CONNECT was able to default\
the top tag of the table as the root node `<BIBLIO>` of the file, and the row\
tags as the `<BOOK>` children of the table tag. In a more complex file, this\
should have been specified, as we will see later. Note that we didn't have to worry\
about the sub-tags such as `<FIRSTNAME>` or `<LASTNAME>` because CONNECT\
automatically retrieves the entire text contained in a tag and its\
sub-tags\[[2](connect-xml-table-type.md#_note-1)].

Only the first author of the first book appears. This is because only the first\
occurrence of a column tag has been retrieved so the result has a proper\
tabular structure. We will see later what we can do about that.

How can we retrieve the values specified by attributes? By using a _Coltype_\
table option to specify the default column type. The value ‘@’ means that\
column names match attribute names. Therefore, we can retrieve them by creating\
a table such as:

```
CREATE TABLE xsampattr (
  ISBN CHAR(15),
  LANG CHAR(2),
  SUBJECT CHAR(32))
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
option_list='Coltype=@';
```

This table returns the following:

| ISBN          | LANG | SUBJECT      |
| ------------- | ---- | ------------ |
| 9782212090819 | fr   | applications |
| 9782840825685 | fr   | applications |

Now to define a table that will give us all the previous information, we must\
specify the column type for each column. Because in the next statement the\
column type defaults to Node, the _field\_format_ column parameter was used to\
indicate which columns are attributes:

From Connect 1.7.0002

```
CREATE TABLE xsamp (
ISBN CHAR(15) xpath='@',
LANG CHAR(2) xpath='@',
SUBJECT CHAR(32) xpath='@',
AUTHOR CHAR(50),
TITLE CHAR(32),
TRANSLATOR CHAR(40),
PUBLISHER CHAR(40),
DATEPUB INT(4))
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK';
```

Before Connect 1.7.0002

```
CREATE TABLE xsamp (
  ISBN CHAR(15) field_format='@',
  LANG CHAR(2) field_format='@',
  SUBJECT CHAR(32) field_format='@',
  AUTHOR CHAR(50),
  TITLE CHAR(32),
  TRANSLATOR CHAR(40),
  PUBLISHER CHAR(40),
  DATEPUB INT(4))
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK';
```

Once done, we can enter the query:

```
SELECT subject, lang, title, author FROM xsamp;
```

This will return the following result:

| SUBJECT      | LANG | TITLE                          | AUTHOR                   |
| ------------ | ---- | ------------------------------ | ------------------------ |
| applications | fr   | Construire une application XML | Jean-Christophe Bernadac |
| applications | fr   | XML en Action                  | William J. Pardi         |

Note that we have been lucky. Because unlike SQL, XML is case sensitive and the\
column names have matched the node names only because the column names were given\
in upper case. Note also that the order of the columns in the table could have\
been different from the order in which the nodes appear in the XML file.

## Using Xpaths with XML tables

Xpath is used by XML to locate and retrieve nodes. The table's main node Xpath is specified by the `tabname` option. If just the node name is given, CONNECT constructs an Xpath such as `‘BIBLIO’` in the example above that should retrieve the `BIBLIO` node wherever it is within the XML file.

The row nodes are by default the children of the table node. However, for instance to eliminate some children nodes that are not real row nodes, the row node name can be specified using the `rownode` sub-option of the `option_list` option.

The field\_format options we used above can be specified to locate more\
precisely where and what information to retrieve using an Xpath-like\
syntax. For instance:

From Connect 1.7.0002

```
CREATE TABLE xsampall (
isbn CHAR(15) xpath='@ISBN',
LANGUAGE CHAR(2) xpath='@LANG',
subject CHAR(32) xpath='@SUBJECT',
authorfn CHAR(20) xpath='AUTHOR/FIRSTNAME',
authorln CHAR(20) xpath='AUTHOR/LASTNAME',
title CHAR(32) xpath='TITLE',
translated CHAR(32) xpath='TRANSLATOR/@PREFIX',
tranfn CHAR(20) xpath='TRANSLATOR/FIRSTNAME',
tranln CHAR(20) xpath='TRANSLATOR/LASTNAME',
publisher CHAR(20) xpath='PUBLISHER/NAME',
LOCATION CHAR(20) xpath='PUBLISHER/PLACE',
YEAR INT(4) xpath='DATEPUB')
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK';
```

Before Connect 1.7.0002

```
CREATE TABLE xsampall (
  isbn CHAR(15) field_format='@ISBN',
  LANGUAGE CHAR(2) field_format='@LANG',
  subject CHAR(32) field_format='@SUBJECT',
  authorfn CHAR(20) field_format='AUTHOR/FIRSTNAME',
  authorln CHAR(20) field_format='AUTHOR/LASTNAME',
  title CHAR(32) field_format='TITLE',
  translated CHAR(32) field_format='TRANSLATOR/@PREFIX',
  tranfn CHAR(20) field_format='TRANSLATOR/FIRSTNAME',
  tranln CHAR(20) field_format='TRANSLATOR/LASTNAME',
  publisher CHAR(20) field_format='PUBLISHER/NAME',
  LOCATION CHAR(20) field_format='PUBLISHER/PLACE',
  YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK';
```

This very flexible column parameter serves several purposes:

* To specify the tag name, or the attribute name if different from the column\
  name.
* To specify the type (tag or attribute) by a prefix of '@' for attributes.
* To specify the path for sub-tags using the '/' character.

This path is always relative to the current context (the column top node) and\
cannot be specified as an absolute path from the document root, therefore a\
leading '/' cannot be used. The path cannot be variable in node names or depth,\
therefore using '`//`' is not allowed.

The query:

```
SELECT isbn, title, translated, tranfn, tranln, LOCATION FROM
    xsampall WHERE translated IS NOT NULL;
```

replies:

| ISBN          | TITLE         | TRANSLATED              | TRANFN | TRANLN | LOCATION |
| ------------- | ------------- | ----------------------- | ------ | ------ | -------- |
| 9782840825685 | XML en Action | adapté de l'anglais par | James  | Guerin | Paris    |

### Libxml2 default name space issue

An issue with libxml2 is that some files can declare a default name space in their root node. Because Xpath only searches in that name space, the nodes will not be found if they are not prefixed. If this happens, specify the tabname option as an Xpath ignoring the current name space:

```
TABNAME="//*[local-name()='BIBLIO']"
```

This must also be done for the default of specified Xpath of the not attribute columns. For instance:

```
title char(32) field_format="*[local-name()='TITLE']",
```

Note: This raises an error (and is useless anyway) with DOMDOC.

### Direct access on XML tables

Direct access is available on XML tables. This means that XML tables can be\
sorted and used in joins, even in the one-side of the join.

However, building a permanent index is not yet implemented. It is unclear whether this can be useful. Indeed, the DOM implementation that is used to access these tables firstly parses the whole file and constructs a node tree in memory. This may often be the longest part of the process, so the use of an index would not be of great value. Note also that this limits the XML files to a reasonable size. Anyway, when speed is important, this table type is not the best to use. Therefore, in these cases, it is probably better to convert the file to another type by inserting the XML table into another table of a more appropriate type for performance.

### Accessing tags with namespaces

With the Windows DOMDOC support, this can be done using the prefix in the tabname column option and/or xpath column option. For instance, given the file gns.xml:

```
<?xml version="1.0" encoding="UTF-8"?>
<gpx xmlns:gns="http:dummy">
<gns:trkseg>
<trkpt lon="-121.9822235107421875" lat="37.3884925842285156">
<gns:ele>6.610851287841797</gns:ele>
<time>2014-04-01T14:54:05.000Z</time>
</trkpt>
<trkpt lon="-121.9821929931640625" lat="37.3885803222656250">
<ele>6.787827968597412</ele>
<time>2014-04-01T14:54:08.000Z</time>
</trkpt>
<trkpt lon="-121.9821624755859375" lat="37.3886299133300781">
<ele>6.771987438201904</ele>
<time>2014-04-01T14:54:10.000Z</time>
</trkpt>
</gns:trkseg>
</gpx>
```

and the defined CONNECT table:

```
CREATE TABLE xgns (
`lon` DOUBLE(21,16) NOT NULL `xpath`='@',
`lat` DOUBLE(20,16) NOT NULL `xpath`='@',
`ele` DOUBLE(21,16) NOT NULL `xpath`='gns:ele',
`time` DATETIME date_format="YYYY-MM-DD 'T' hh:mm:ss '.000Z'"
) 
  ENGINE=CONNECT DEFAULT CHARSET=latin1 `table_type`=XML 
  `file_name`='gns.xml' tabname='gns:trkseg' option_list='xmlsup=domdoc';
```

```
SELECT * FROM xgns;
```

Displays:

| lon               | lat              | ele             | time                |
| ----------------- | ---------------- | --------------- | ------------------- |
| -121,982223510742 | 37,3884925842285 | 6,6108512878418 | 01/04/2014 14:54:05 |
| -121,982192993164 | 37,3885803222656 | 0               | 01/04/2014 14:54:08 |
| -121,982162475586 | 37,3886299133301 | 0               | 01/04/2014 14:54:10 |

Only the prefixed ‘ele’ tag is recognized.

However, this does not work with the libxml2 support. The solution is then to use a function ignoring the name space:

```
CREATE TABLE xgns2 (
`lon` DOUBLE(21,16) NOT NULL `xpath`='@',
`lat` DOUBLE(20,16) NOT NULL `xpath`='@',
`ele` DOUBLE(21,16) NOT NULL `xpath`="*[local-name()='ele']",
`time` DATETIME date_format="YYYY-MM-DD 'T' hh:mm:ss '.000Z'"
) 
  ENGINE=CONNECT DEFAULT CHARSET=latin1 `table_type`=XML 
  `file_name`='gns.xml' tabname="*[local-name()='trkseg']" option_list='xmlsup=libxml2';
```

Then :

```
SELECT * FROM xgns2;
```

Displays:

| lon               | lat              | ele             | time                |
| ----------------- | ---------------- | --------------- | ------------------- |
| -121,982223510742 | 37,3884925842285 | 6,6108512878418 | 01/04/2014 14:54:05 |
| -121,982192993164 | 37,3885803222656 | 6.7878279685974 | 01/04/2014 14:54:08 |
| -121,982162475586 | 37,3886299133301 | 6.7719874382019 | 01/04/2014 14:54:10 |

This time, all ‘ele\` tags are recognized. This solution does not work with DOMDOC.

## Having Columns defined by Discovery

It is possible to let the MariaDB discovery process do the job of column specification. When columns are not defined in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement, CONNECT endeavours to analyze the XML file and to provide the column specifications. This is possible only for true XML tables, but not for HTML tables.

For instance, the _xsamp_ table could have been created specifying:

```
CREATE TABLE xsamp
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK';
```

Let’s check how it was actually specified using the SHOW CREATE TABLE statement:

```
CREATE TABLE `xsamp` (
  `ISBN` CHAR(13) NOT NULL `FIELD_FORMAT`='@',
  `LANG` CHAR(2) NOT NULL `FIELD_FORMAT`='@',
  `SUBJECT` CHAR(12) NOT NULL `FIELD_FORMAT`='@',
  `AUTHOR` CHAR(24) NOT NULL,
  `TRANSLATOR` CHAR(12) DEFAULT NULL,
  `TITLE` CHAR(30) NOT NULL,
  `PUBLISHER` CHAR(21) NOT NULL,
  `DATEPUB` CHAR(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='XML' 
  `FILE_NAME`='E:/Data/Xml/Xsample.xml' `TABNAME`='BIBLIO' `OPTION_LIST`='rownode=BOOK';
```

It is equivalent except for the column sizes that have been calculated from the file as the maximum length of the corresponding column when it was a normal value. Also, all columns are specified as type [CHAR](../../../../reference/data-types/string-data-types/char.md) because XML does not provide information about the node content data type. Nullable is set to true if the column is missing in some rows.

If a more complex definition is desired, you can ask CONNECT to analyse the XPATH up to a given level using the level option in the option list. The level value is the number of nodes that are taken in the XPATH. For instance:

```
CREATE TABLE xsampall
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK,Level=1';
```

This will define the table as:

From Connect 1.7.0002

```
CREATE TABLE `xsampall` (
  `ISBN` CHAR(13) NOT NULL `XPATH`='@',
  `LANG` CHAR(2) NOT NULL `XPATH`='@',
  `SUBJECT` CHAR(12) NOT NULL `XPATH`='@',
  `AUTHOR_FIRSTNAME` CHAR(15) NOT NULL `XPATH`='AUTHOR/FIRSTNAME',
  `AUTHOR_LASTNAME` CHAR(8) NOT NULL `XPATH`='AUTHOR/LASTNAME',
  `TRANSLATOR_PREFIX` CHAR(24) DEFAULT NULL `XPATH`='TRANSLATOR/@PREFIX',
  `TRANSLATOR_FIRSTNAME` CHAR(7) DEFAULT NULL `XPATH`='TRANSLATOR/FIRSTNAME',
  `TRANSLATOR_LASTNAME` CHAR(6) DEFAULT NULL `XPATH`='TRANSLATOR/LASTNAME',
  `TITLE` CHAR(30) NOT NULL,
  `PUBLISHER_NAME` CHAR(15) NOT NULL `XPATH`='PUBLISHER/NAME',
  `PUBLISHER_PLACE` CHAR(5) NOT NULL `XPATH`='PUBLISHER/PLACE',
  `DATEPUB` CHAR(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='XML' `FILE_NAME`='Xsample.xml' `TABNAME`='BIBLIO' `OPTION_LIST`='rownode=BOOK,Depth=1';
<</SQL>>


BEFORE CONNECT 1.7.0002
<<SQL>>
CREATE TABLE `xsampall` (
  `ISBN` CHAR(13) NOT NULL `FIELD_FORMAT`='@',
  `LANG` CHAR(2) NOT NULL `FIELD_FORMAT`='@',
  `SUBJECT` CHAR(12) NOT NULL `FIELD_FORMAT`='@',
  `AUTHOR_FIRSTNAME` CHAR(15) NOT NULL `FIELD_FORMAT`='AUTHOR/FIRSTNAME',
  `AUTHOR_LASTNAME` CHAR(8) NOT NULL `FIELD_FORMAT`='AUTHOR/LASTNAME',
  `TRANSLATOR_PREFIX` CHAR(24) DEFAULT NULL `FIELD_FORMAT`='TRANSLATOR/@PREFIX',
  `TRANSLATOR_FIRSTNAME` CHAR(7) DEFAULT NULL `FIELD_FORMAT`='TRANSLATOR/FIRSTNAME',
  `TRANSLATOR_LASTNAME` CHAR(6) DEFAULT NULL `FIELD_FORMAT`='TRANSLATOR/LASTNAME',
  `TITLE` CHAR(30) NOT NULL,
  `PUBLISHER_NAME` CHAR(15) NOT NULL `FIELD_FORMAT`='PUBLISHER/NAME',
  `PUBLISHER_PLACE` CHAR(5) NOT NULL `FIELD_FORMAT`='PUBLISHER/PLACE',
  `DATEPUB` CHAR(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='XML' `FILE_NAME`='Xsample.xml' 
  `TABNAME`='BIBLIO' `OPTION_LIST`='rownode=BOOK,Level=1';
<</SQL>>

This METHOD can be used AS a quick way TO make a “TEMPLATE” TABLE definition that can later be edited TO make the desired definition. IN particular, COLUMN NAMES ARE constructed FROM ALL the nodes OF their PATH IN ORDER TO have DISTINCT COLUMN names. This can be manually edited TO have the desired NAMES, provided their XPATH IS NOT modified.

TO have a preview OF how columns are DEFINED, you can USE a CATALOG TABLE like this:

<<SQL>>
CREATE TABLE xsacol
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK,Level=1' catfunc=col;
<</SQL>>

AND WHEN asking:

<<SQL>>
SELECT COLUMN_NAME Name, type_name TYPE, column_size SIZE, NULLABLE, xpath FROM xsacol;
<</SQL>>

You GET the description OF what the TABLE columns are:

<<style CLASS="darkheader-nospace-borders">>
|= Name |= TYPE |= SIZE |= NULLABLE |= xpath |
| ISBN | CHAR | 13 | 0 | @ | 
| LANG | CHAR | 2 | 0 | @ |
| SUBJECT | CHAR | 12 | 0 | @ |
| AUTHOR_FIRSTNAME | CHAR | 15 | 0 | AUTHOR/FIRSTNAME | 
| AUTHOR_LASTNAME | CHAR | 8 | 0 | AUTHOR/LASTNAME | 
| TRANSLATOR_PREFIX | CHAR | 24 | 1 | TRANSLATOR/@PREFIX | 
| TRANSLATOR_FIRSTNAME | CHAR | 7 | 1 | TRANSLATOR/FIRSTNAME |
| TRANSLATOR_LASTNAME | CHAR | 6 | 1 | TRANSLATOR/LASTNAME | 
| TITLE | CHAR | 30 | 0 |  | 
| PUBLISHER_NAME | CHAR | 15 | 0 | PUBLISHER/NAME |
| PUBLISHER_PLACE | CHAR | 5 | 0 | PUBLISHER/PLACE |
| DATEPUB | CHAR | 4 | 0 | |
<</style>>

== WRITE operations ON XML TABLES
You can freely USE the UPDATE, DELETE AND INSERT commands WITH XML tables.
However, you must understand that the format OF the updated OR inserted DATA
follows the specifications OF the TABLE you created, NOT the ones OF the
original SOURCE file. FOR INSTANCE, let us suppose we INSERT a NEW book USING
the //xsamp// TABLE (NOT the //xsampall// TABLE) WITH the command:

<<code lang=mysql INLINE=FALSE>>
INSERT INTO xsamp
  (isbn, lang, subject, author, title, publisher,datepub)
  VALUES ('9782212090529','fr','général','Alain Michard',
         'XML, Langage et Applications','Eyrolles Paris',1998);
```

Then if we ask:

```
SELECT subject, author, title, translator, publisher FROM xsamp;
```

Everything seems correct when we get the result:

| SUBJECT      | AUTHOR                   | TITLE                          | TRANSLATOR   | PUBLISHER             |
| ------------ | ------------------------ | ------------------------------ | ------------ | --------------------- |
| applications | Jean-Christophe Bernadac | Construire une application XML |              | Eyrolles Paris        |
| applications | William J. Pardi         | XML en Action                  | James Guerin | Microsoft Press Paris |
| général      | Alain Michard            | XML, Langage et Applications   |              | Eyrolles Paris        |

However if we enter the apparently equivalent query on the _xsampall_ table,\
based on the same file:

```
SELECT subject,
concat(authorfn, ' ', authorln) author , title,
concat(tranfn, ' ', tranln) translator,
concat(publisher, ' ', LOCATION) publisher FROM xsampall;
```

this returns an apparently wrong answer:

| SUBJECT      | AUTHOR                   | TITLE                          | TRANSLATOR   | PUBLISHER             |
| ------------ | ------------------------ | ------------------------------ | ------------ | --------------------- |
| applications | Jean-Christophe Bernadac | Construire une application XML |              | Eyrolles Paris        |
| applications | William J. Pardi         | XML en Action                  | James Guerin | Microsoft Press Paris |
| général      |                          | XML, Langage et Applications   |              |                       |

What happened here? Simply, because we used the _xsamp_ table to do the\
Insert, what has been inserted within the XML file had the structure described\
for _xsamp_:

```
<BOOK ISBN="9782212090529" LANG="fr" SUBJECT="général">
      <AUTHOR>Alain Michard</AUTHOR>
      <TITLE>XML, Langage et Applications</TITLE>
      <TRANSLATOR></TRANSLATOR>
      <PUBLISHER>Eyrolles Paris</PUBLISHER>
      <DATEPUB>1998</DATEPUB>
   </BOOK>
```

CONNECT cannot "invent" sub-tags that are not part of the _xsamp_ table.\
Because these sub-tags do not exist, the _xsampall_ table cannot retrieve the\
information that should be attached to them. If we want to be able to query the\
XML file by all the defined tables, the correct way to insert a new book to the\
file is to use the _xsampall_ table, the only one that addresses all the\
components of the original document:

```
DELETE FROM xsamp WHERE isbn = '9782212090529';

INSERT INTO xsampall (isbn, LANGUAGE, subject, authorfn, authorln,
      title, publisher, LOCATION, YEAR)
   VALUES('9782212090529','fr','général','Alain','Michard',
      'XML, Langage et Applications','Eyrolles','Paris',1998);
```

Now the added book, in the XML file, will have the required structure:

```
<BOOK ISBN="9782212090529" LANG="fr" SUBJECT="général">
      <AUTHOR>
         <FIRSTNAME>Alain</FIRSTNAME>
         <LASTNAME>Michard</LASTNAME>
      </AUTHOR>
      <TITLE>XML, Langage et Applications</TITLE>
      <PUBLISHER>
         <NAME>Eyrolles</NAME>
         <PLACE>Paris</PLACE>
      </PUBLISHER>
      <DATEPUB>1998</DATEPUB>
   </BOOK>
```

**Note:** We used a column list in the Insert statements when creating the table to avoid generating a `<TRANSLATOR>`\
node with sub-nodes, all containing null values (this works on Windows only).

## Multiple nodes in the XML document

Let us come back to the above example XML file. We have seen that the author\
node can be "multiple" meaning that there can be more than one author of a\
book. What can we do to get the complete information fitting the relational\
model? CONNECT provides you with two possibilities, but is restricted to only one\
such multiple node per table.

The first and most challenging one is to return as many rows than there are\
authors, the other columns being repeated as if we had make a join between the\
author column and the rest of the table. To achieve this, simply specify the\
“multiple” node name and the “expand” option when creating the table. For\
instance, we can create the _xsamp2_ table like this:

```
CREATE TABLE xsamp2 (
  ISBN CHAR(15) field_format='@',
  LANG CHAR(2) field_format='@',
  SUBJECT CHAR(32) field_format='@',
  AUTHOR CHAR(40),
  TITLE CHAR(32),
  TRANSLATOR CHAR(32),
  PUBLISHER CHAR(32),
  DATEPUB INT(4))
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO'
option_list='rownode=BOOK,Expand=1,Mulnode=AUTHOR,Limit=2';
```

In this statement, the Limit option specifies the maximum number of values that are expanded. If not specified, it defaults to `10`. Any values above the limit are ignored and a warning message issued\[[3](connect-xml-table-type.md#_note-2)]. Now you can enter a query such as:

```
SELECT isbn, subject, author, title FROM xsamp2;
```

This will retrieve and display the following result:

| ISBN          | SUBJECT      | AUTHOR                   | TITLE                          |
| ------------- | ------------ | ------------------------ | ------------------------------ |
| 9782212090819 | applications | Jean-Christophe Bernadac | Construire une application XML |
| 9782212090819 | applications | François Knab            | Construire une application XML |
| 9782840825685 | applications | William J. Pardi         | XML en Action                  |
| 9782212090529 | général      | Alain Michard            | XML, Langage et Applications   |

In this case, this is as if the table had four rows. However if we enter the query:

```
SELECT isbn, subject, title, publisher FROM xsamp2;
```

this time the result are:

| ISBN          | SUBJECT      | TITLE                          | PUBLISHER             |
| ------------- | ------------ | ------------------------------ | --------------------- |
| 9782212090819 | applications | Construire une application XML | Eyrolles Paris        |
| 9782840825685 | applications | XML en Action                  | Microsoft Press Paris |
| 9782212090529 | général      | XML, Langage et Applications   | Eyrolles Paris        |

Because the author column does not appear in the query, the corresponding row\
was not expanded. This is somewhat strange because this would have been\
different if we had been working on a table of a different type. However, it is\
closer to the relational model for which there should not be two identical rows\
(tuples) in a table. Nevertheless, you should be aware of this somewhat erratic\
behavior. For instance:

```
SELECT COUNT(*) FROM xsamp2;                /* Replies 3 */
SELECT COUNT(author) FROM xsamp2;           /* Replies 4 */
SELECT COUNT(isbn) FROM xsamp2;             /* Replies 3 */
SELECT isbn, subject, title, publisher FROM xsamp2 WHERE author <> '';
```

This last query replies:

| ISBN          | SUBJECT      | TITLE                          | PUBLISHER             |
| ------------- | ------------ | ------------------------------ | --------------------- |
| 9782212090819 | applications | Construire une application XML | Eyrolles Paris        |
| 9782212090819 | applications | Construire une application XML | Eyrolles Paris        |
| 9782840825685 | applications | XML en Action                  | Microsoft Press Paris |
| 9782212090529 | général      | XML, Langage et Applications   | Eyrolles Paris        |

Even though the author column does not appear in the result, the corresponding row was\
expanded because the multiple column was used in the where clause.

## Intermediate multiple node

The "multiple" node can be an intermediate node. If we want to do the same\
expanding with the _xsampall_ table, there are nothing more to do. The_xsampall2_ table can be created with:

From Connect 1.7.0002

```
CREATE TABLE xsampall2 (
isbn CHAR(15) xpath='@ISBN',
LANGUAGE CHAR(2) xpath='@LANG',
subject CHAR(32) xpath='@SUBJECT',
authorfn CHAR(20) xpath='AUTHOR/FIRSTNAME',
authorln CHAR(20) xpath='AUTHOR/LASTNAME',
title CHAR(32) xpath='TITLE',
translated CHAR(32) xpath='TRANSLATOR/@PREFIX',
tranfn CHAR(20) xpath='TRANSLATOR/FIRSTNAME',
tranln CHAR(20) xpath='TRANSLATOR/LASTNAME',
publisher CHAR(20) xpath='PUBLISHER/NAME',
LOCATION CHAR(20) xpath='PUBLISHER/PLACE',
YEAR INT(4) xpath='DATEPUB')
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO' option_list='rownode=BOOK,Expand=1,Mulnode=AUTHOR,Limit=2';
```

Before Connect 1.7.0002

```
CREATE TABLE xsampall2 (
  isbn CHAR(15) field_format='@ISBN',
  LANGUAGE CHAR(2) field_format='@LANG',
  subject CHAR(32) field_format='@SUBJECT',
  authorfn CHAR(20) field_format='AUTHOR/FIRSTNAME',
  authorln CHAR(20) field_format='AUTHOR/LASTNAME',
  title CHAR(32) field_format='TITLE',
  translated CHAR(32) field_format='TRANSLATOR/@PREFIX',
  tranfn CHAR(20) field_format='TRANSLATOR/FIRSTNAME',
  tranln CHAR(20) field_format='TRANSLATOR/LASTNAME',
  publisher CHAR(20) field_format='PUBLISHER/NAME',
  LOCATION CHAR(20) field_format='PUBLISHER/PLACE',
  YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=XML file_name='Xsample.xml'
tabname='BIBLIO'
option_list='rownode=BOOK,Expand=1,Mulnode=AUTHOR,Limit=2';
```

The only difference is that the "multiple" node is an intermediate node in the\
path. The resulting table can be seen with a query such as:

```
SELECT subject, LANGUAGE lang, title, authorfn FIRST, authorln
    LAST, YEAR FROM xsampall2;
```

This query displays:

| SUBJECT      | LANG | TITLE                          | FIRST           | LAST     | YEAR |
| ------------ | ---- | ------------------------------ | --------------- | -------- | ---- |
| applications | fr   | Construire une application XML | Jean-Christophe | Bernadac | 1999 |
| applications | fr   | Construire une application XML | François        | Knab     | 1999 |
| applications | fr   | XML en Action                  | William J.      | Pardi    | 1999 |
| général      | fr   | XML, Langage et Applications   | Alain           | Michard  | 1998 |

These composite tables, half array half tree, reserve some surprises for us when\
updating, deleting from or inserting into them. Insert just cannot generate\
this structure; if two rows are inserted with just a different author, two book\
nodes are generated in the XML file. Delete always deletes one book node\
and all its children nodes even if specified against only one author. Update is\
more complicated:

```
UPDATE xsampall2 SET authorfn = 'Simon' WHERE authorln = 'Knab';
UPDATE xsampall2 SET YEAR = 2002 WHERE authorln = 'Bernadac';
UPDATE xsampall2 SET authorln = 'Mercier' WHERE YEAR = 2002;
```

After these three updates, the first two responding "Affected rows: 1" and the\
last one responding "Affected rows: 2", the last query answers:

| subject      | lang | title                          | first           | last    | year |
| ------------ | ---- | ------------------------------ | --------------- | ------- | ---- |
| applications | fr   | Construire une application XML | Jean-Christophe | Mercier | 2002 |
| applications | fr   | Construire une application XML | François        | Knab    | 2002 |
| applications | fr   | XML en Action                  | William J.      | Pardi   | 1999 |
| général      | fr   | XML, Langage et Applications   | Alain           | Michard | 1998 |

What must be understood here is that the Update modifies node values in the XML file, not cell values in the relational table. The first update worked normally. The second update changed the year value of the book and this shows for the two expanded rows because there is only one DATEPUB node for that book. Because the third update applies to a row having a certain date value, both author names were updated.

## Making a List of Multiple Values

Another way to see multiple values is to ask CONNECT to make a comma separated\
list of the multiple node values. This time, it can only be done if the\
"multiple" node is not intermediate. For example, we can modify the _xsamp2_\
table definition by:

```
ALTER TABLE xsamp2 option_list='rownode=BOOK,Mulnode=AUTHOR,Limit=3';
```

This time 'Expand' is not specified, and Limit gives the maximum number of\
items in the list. Now if we enter the query:

```
SELECT isbn, subject, author "AUTHOR(S)", title FROM xsamp2;
```

We will get the following result:

| ISBN          | SUBJECT      | AUTHOR(S)                               | TITLE                          |
| ------------- | ------------ | --------------------------------------- | ------------------------------ |
| 9782212090819 | applications | Jean-Christophe Bernadac, François Knab | Construire une application XML |
| 9782840825685 | applications | William J. Pardi                        | XML en Action                  |
| 9782212090529 | général      | Alain Michard                           | XML, Langage et Applications   |

Note that updating the "multiple" column is not possible because CONNECT does\
not know which of the nodes to update.

This could not have been done with the _xsampall2_ table because the author\
node is intermediate in the path, and making two lists, one of first names and\
another one of last names would not make sense anyway.

### What if a table contains several multiple nodes

This can be handled by creating several tables on the same file, each\
containing only one multiple node and constructing the desired result using\
joins.

## Support of HTML Tables

Most tables included in HTML documents cannot be processed by CONNECT because the HTML\
language is often not compatible with the syntax of XML. In particular, XML\
requires all open tags to be matched by a closing tag while it is sometimes\
optional in HTML. This is often the case concerning column tags.

However, you can meet tables that respect the XML syntax but have some of the\
features of HTML tables. For instance:

```
<?xml version="1.0"?>
<Beers>
  <table>
    <th><td>Name</td><td>Origin</td><td>Description</td></th>
    <tr>
      <td><brandName>Huntsman</brandName></td>
      <td><origin>Bath, UK</origin></td>
      <td><details>Wonderful hop, light alcohol</details></td>
    </tr>
    <tr>
      <td><brandName>Tuborg</brandName></td>
      <td><origin>Danmark</origin></td>
      <td><details>In small bottles</details></td>
    </tr>
  </table>
</Beers>
```

Here the different column tags are included in `<td></td>` tags as for HTML\
tables. You cannot just add this tag in the Xpath of the columns, because the\
search is done on the first occurrence of each tag, and this would cause this\
search to fail for all columns except the first one. This case is handled by\
specifying the _Colnode_ table option that gives the name of these column\
tags, for example:

From Connect 1.7.0002

```
CREATE TABLE beers (
`Name` CHAR(16) xpath='brandName',
`Origin` CHAR(16) xpath='origin',
`Description` CHAR(32) xpath='details')
ENGINE=CONNECT table_type=XML file_name='beers.xml'
tabname='table' option_list='rownode=tr,colnode=td';
```

Before Connect 1.7.0002

```
CREATE TABLE beers (
  `Name` CHAR(16) field_format='brandName',
  `Origin` CHAR(16) field_format='origin',
  `Description` CHAR(32) field_format='details')
ENGINE=CONNECT table_type=XML file_name='beers.xml'
tabname='table' option_list='rownode=tr,colnode=td';
```

The table are displayed as:

| Name     | Origin   | Description                  |
| -------- | -------- | ---------------------------- |
| Huntsman | Bath, UK | Wonderful hop, light alcohol |
| Tuborg   | Danmark  | In small bottles             |

However, you can deal with tables even closer to the HTML model. For example\
the _coffee.htm_ file:

```
<TABLE summary="This table charts the number of cups of coffe
                consumed by each senator, the type of coffee (decaf
                or regular), and whether taken with sugar.">
  <CAPTION>Cups of coffee consumed by each senator</CAPTION>
  <TR>
    <TH>Name</TH>
    <TH>Cups</TH>
    <TH>Type of Coffee</TH>
    <TH>Sugar?</TH>
  </TR>
  <TR>
    <TD>T. Sexton</TD>
    <TD>10</TD>
    <TD>Espresso</TD>
    <TD>No</TD>
  </TR>
  <TR>
    <TD>J. Dinnen</TD>
    <TD>5</TD>
    <TD>Decaf</TD>
    <TD>Yes</TD>
  </TR>
</TABLE>
```

Here column values are directly represented by the TD tag text. You cannot\
declare them as tags nor as attributes. In addition, they are not located using\
their name but by their position within the row. Here is how to declare such a\
table to CONNECT:

```
CREATE TABLE coffee (
  `Name` CHAR(16),
  `Cups` INT(8),
  `Type` CHAR(16),
  `Sugar` CHAR(4))
ENGINE=CONNECT table_type=XML file_name='coffee.htm'
tabname='TABLE' header=1 option_list='Coltype=HTML';
```

You specify the fact that columns are located by position by setting the_Coltype_ option to 'HTML'. Each column position (0 based) are the value\
of the _flag_ column parameter that is set by default in sequence. Now we are\
able to display the table:

| Name      | Cups | Type     | Sugar |
| --------- | ---- | -------- | ----- |
| T. Sexton | 10   | Espresso | No    |
| J. Dinnen | 5    | Decaf    | Yes   |

**Note 1:** We specified '`header=n`' in the create statement to indicate\
that the first n rows of the table are not data rows and should be skipped.

**Note 2:** In this last example, we did not specify the node names using the\
Rownode and Colnode options because when _Coltype_ is set to 'HTML' they\
default to '`Rownode=TR`' and '`Colnode=TD`'.

**Note 3:** The _Coltype_ option is a word only the first character of which\
is significant. Recognized values are:

|                          |                                              |
| ------------------------ | -------------------------------------------- |
| T(ag) or N(ode)          | Column names match a tag name (the default). |
| A(ttribute) or @         | Column names match an attribute name.        |
| H(tml) or C(ol) or P(os) | Column are retrieved by their position.      |

### New file setting

Some create options are used only when creating a table on a new file, i. e.\
when inserting into a file that does not exist yet. When specified, the\
'Header' option will create a header row with the name of the table columns.\
This is chiefly useful for HTML tables to be displayed on a web browser.

Some new list-options are used in this context:

|           |                                                                         |
| --------- | ----------------------------------------------------------------------- |
| Encoding  | The encoding of the new document, defaulting to UTF-8.                  |
| Attribute | A list of 'attname=attvalue' separated by ';' to add to the table node. |
| HeadAttr  | An attribute list to be added to the header row node.                   |

Let us see for instance, the following create statement:

```
CREATE TABLE handlers (
  handler CHAR(64),
  VERSION CHAR(20),
  author CHAR(64),
  description CHAR(255),
  maturity CHAR(12))
ENGINE=CONNECT table_type=XML file_name='handlers.htm'
tabname='TABLE' header=yes
option_list='coltype=HTML,encoding=ISO-8859-1,
attribute=border=1;cellpadding=5,headattr=bgcolor=yellow';
```

Supposing the table file does not exist yet, the first insert into that table,\
for instance by the following statement:

```
INSERT INTO handlers SELECT plugin_name, plugin_version,
  plugin_author, plugin_description, plugin_maturity FROM
  information_schema.plugins WHERE plugin_type = 'DAEMON';
```

will generate the following file:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- Created by CONNECT Version 3.05.0005 August 17, 2012 -->
<TABLE border="1" cellpadding="5">
  <TR bgcolor="yellow">
    <TH>handler</TH>
    <TH>version</TH>
    <TH>author</TH>
    <TH>description</TH>
    <TH>maturity</TH>
  </TR>
  <TR>
    <TD>Maria</TD>
    <TD>1.5</TD>
    <TD>Monty Program Ab</TD>
    <TD>Compatibility aliases for the Aria engine</TD>
    <TD>Gamma</TD>
  </TR>
</TABLE>
```

This file can be used to display the table on a web browser (encoding should be`ISO-8859-x`)

| handler | version | author           | description                               | maturity |
| ------- | ------- | ---------------- | ----------------------------------------- | -------- |
| Maria   | 1.5     | Monty Program Ab | Compatibility aliases for the Aria engine | Gamma    |

**Note:** The XML document encoding is generally specified in the XML header\
node and can be different from the DATA\_CHARSET, which is always UTF-8 for XML\
tables. Therefore the table DATA\_CHARSET character set should be unspecified,\
or specified as UTF8. The Encoding specification is useful only for new XML\
files and ignored for existing files having their encoding already specified in\
the header node.

## Notes

1. [↑](connect-xml-table-type.md#_ref-0) CONNECT does not claim to be able to deal with\
   any XML document. Besides, those that can usefully be processed for data\
   analysis are likely to have a structure that can easily be transformed into a\
   table.
2. [↑](connect-xml-table-type.md#_ref-1) With libxml2, sub tags text can be separated by 0 or several\
   blanks depending on the structure and indentation of the data file.
3. [↑](connect-xml-table-type.md#_ref-2) This may cause some rows to be lost because an eventual where clause on the “multiple” column is applied only on the limited number of retrieved rows.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
