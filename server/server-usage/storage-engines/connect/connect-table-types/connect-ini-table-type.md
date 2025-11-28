# CONNECT INI Table Type

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

## Overview

The INI type is one of the configuration or initialization files often found on\
Windows machines. For instance, let us suppose you have the following contact\
file _contact.ini_:

```
[BER]
name=Bertrand
forename=Olivier
address=21 rue Ferdinand Buisson
city=Issy-les-Mlx
zipcode=92130
tel=09.54.36.29.60
cell=06.70.06.04.16

[WEL]
name=Schmitt
forename=Bernard
hired=19/02/1985
address=64 tiergarten strasse
city=Berlin
zipcode=95013
tel=03.43.377.360

[UK1]
name=Smith
forename=Henry
hired=08/11/2003
address=143 Blum Rd.
city=London
zipcode=NW1 2BP
```

CONNECT lets you view it as a table in two different ways.

## Column layout

The first way is to regard it as a table having one line per section, the\
columns being the keys you want to display. In this case, the CREATE statement\
could be:

```
CREATE TABLE contact (
  contact CHAR(16) flag=1,
  name CHAR(20),
  forename CHAR(32),
  hired DATE date_format='DD/MM/YYYY',
  address CHAR(64),
  city CHAR(20),
  zipcode CHAR(8),
  tel CHAR(16))
ENGINE=CONNECT table_type=INI file_name='contact.ini';
```

The column that will contain the section name can have any name but must\
specify `flag=1`. All other columns must have the names of the keys we want to\
display (case insensitive). The type can be character or numeric depending on\
the key value type, and the length is the maximum expected length for the key\
value. Once done, the statement:

```
SELECT contact, name, hired, city, tel FROM contact;
```

This statement will display the file in tabular format.

| contact | name     | hired      | city         | tel            |
| ------- | -------- | ---------- | ------------ | -------------- |
| BER     | Bertrand | 1970-01-01 | Issy-les-Mlx | 09.54.36.29.60 |
| WEL     | Schmitt  | 1985-02-19 | Berlin       | 03.43.377.360  |
| UK1     | Smith    | 2003-11-08 | London       | NULL           |

Only the keys defined in the create statements are visible; keys that do not\
exist in a section are displayed as null or pseudo null (blank for character,\
1/1/70 for dates, and 0 for numeric) for columns declared NOT NULL.

All relational operations can be applied to this table. The table (and the\
file) can be updated, inserted and conditionally deleted. The only constraint\
is that when inserting values, the section name must be the first in the list\
of values.

**Note 1:** When inserting, if a section already exists, no new section are\
created but the new values are added or replace those of the existing\
section. Thus, the following two commands are equivalent:

```
UPDATE contact SET forename = 'Harry' WHERE contact = 'UK1';
INSERT INTO contact (contact,forename) VALUES('UK1','Harry');
```

**Note 2:** Because sections represent one line, a DELETE statement on a\
section key will delete the whole section.

## Row layout

To be a good candidate for tabular representation, an INI file should have\
often the same keys in all sections. In practice, many files commonly found on\
computers, such as the _win.ini_ file of the Windows directory or the_&#x6D;y.ini_ file cannot be viewed that way because each section has different\
keys. In this case, a second way is to regard the file as a table having one\
row per section key and whose columns can be the section name, the key name,\
and the key value.

For instance, let us define the table:

```
create table xcont (
  section char(16) flag=1,
  keyname char(16) flag=2,
  value char(32))
engine=CONNECT table_type=INI file_name='contact.ini'
option_list='Layout=Row';
```

In this statement, the "Layout" option sets the display format, Column by\
default or anything else not beginning by 'C' for row layout display. The names\
of the three columns can be freely chosen. The Flag option gives the meaning of\
the column. Specify `flag=1` for the section name and `flag=2` for the key\
name. Otherwise, the column will contain the key value.

Once done, the command:

```
SELECT * FROM xcont;
```

Will display the following result:

| section | keyname  | value                    |
| ------- | -------- | ------------------------ |
| BER     | name     | Bertrand                 |
| BER     | forename | Olivier                  |
| BER     | address  | 21 rue Ferdinand Buisson |
| BER     | city     | Issy-les-Mlx             |
| BER     | zipcode  | 92130                    |
| BER     | tel      | 09.54.36.29.60           |
| BER     | cell     | 06.70.06.04.16           |
| WEL     | name     | Schmitt                  |
| WEL     | forename | Bernard                  |
| WEL     | hired    | 19/02/1985               |
| WEL     | address  | 64 tiergarten strasse    |
| WEL     | city     | Berlin                   |
| WEL     | zipcode  | 95013                    |
| WEL     | tel      | 03.43.377.360            |
| UK1     | name     | Smith                    |
| UK1     | forename | Henry                    |
| UK1     | hired    | 08/11/2003               |
| UK1     | address  | 143 Blum Rd.             |
| UK1     | city     | London                   |
| UK1     | zipcode  | NW1 2BP                  |

**Note:** When processing an INI table, all section names are retrieved in a\
buffer of 8K bytes (2048 bytes before 10.0.17). For a big file having many sections, this size can be\
increased using for example:

```
option_list='seclen=16K';
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
