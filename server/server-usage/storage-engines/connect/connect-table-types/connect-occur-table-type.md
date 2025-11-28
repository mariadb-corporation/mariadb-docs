# CONNECT OCCUR Table Type

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Similarly to the [XCOL](connect-xcol-table-type.md) table type, `OCCUR` is an extension to the [PROXY](connect-proxy-table-type.md) type when\
referring to a table or view having several columns containing the same kind of\
data. It enables having a different view of the table where the data from\
these columns are put in a single column, eventually causing several rows to be\
generated from one row of the object table. For example, supposing we have a_pets_ table:

| name    | dog | cat | rabbit | bird | fish |
| ------- | --- | --- | ------ | ---- | ---- |
| John    | 2   | 0   | 0      | 0    | 0    |
| Bill    | 0   | 1   | 0      | 0    | 0    |
| Mary    | 1   | 1   | 0      | 0    | 0    |
| Lisbeth | 0   | 0   | 2      | 0    | 0    |
| Kevin   | 0   | 2   | 0      | 6    | 0    |
| Donald  | 1   | 0   | 0      | 0    | 3    |

We can create an occur table by:

```
CREATE TABLE xpet (
  name VARCHAR(12) NOT NULL,
  race CHAR(6) NOT NULL,
  NUMBER INT NOT NULL)
ENGINE=CONNECT table_type=occur tabname=pets
option_list='OccurCol=number,RankCol=race'
Colist='dog,cat,rabbit,bird,fish';
```

When displaying it by

```
SELECT * FROM xpet;
```

We will get the result:

| name    | race   | number |
| ------- | ------ | ------ |
| John    | dog    | 2      |
| Bill    | cat    | 1      |
| Mary    | dog    | 1      |
| Mary    | cat    | 1      |
| Lisbeth | rabbit | 2      |
| Kevin   | cat    | 2      |
| Kevin   | bird   | 6      |
| Donald  | dog    | 1      |
| Donald  | fish   | 3      |

First of all, the values of the column listed in the Colist option have been\
put in a unique column whose name is given by the OccurCol option. When several\
columns have non null (or pseudo-null) values, several rows are generated, with\
the other normal columns values repeated.

In addition, an optional special column was added whose name is given by the\
RankCol option. This column contains the name of the source column from which\
the value of the OccurCol column comes from. It permits here to know the race\
of the pets whose number is given in _number_.

This table type permit to make queries that would be more complicated to make\
on the original tables. For instance to know who as more than 1 pet of a kind,\
you can simply ask:

```
SELECT * FROM xpet WHERE NUMBER > 1;
```

You will get the result:

| name    | race   | number |
| ------- | ------ | ------ |
| John    | dog    | 2      |
| Lisbeth | rabbit | 2      |
| Kevin   | cat    | 2      |
| Kevin   | bird   | 6      |
| Donald  | fish   | 3      |

**Note 1:** Like for [XCOL tables](connect-xcol-table-type.md), no\
row multiplication for queries not implying the Occur column.

**Note 2:** Because the OccurCol was declared "not null" no rows were generated\
for null or pseudo-null values of the column list. If the OccurCol is declared\
as nullable, rows are also generated for columns containing null or pseudo-null\
values.

Occur tables can be also defined from views or source definition. Also, CONNECT\
is able to generate the column definitions if not specified:

```
CREATE TABLE ocsrc ENGINE=CONNECT table_type=occur
colist='january,february,march,april,may,june,july,august,september,
october,november,december' option_list='rankcol=month,occurcol=day'
srcdef='select ''Foo'' name, 8 january, 7 february, 2 march, 1 april,
  8 may, 14 june, 25 july, 10 august, 13 september, 22 october, 28
  november, 14 december';
```

This table is displayed as:

| name | month     | day |
| ---- | --------- | --- |
| Foo  | january   | 8   |
| Foo  | february  | 7   |
| Foo  | march     | 2   |
| Foo  | april     | 1   |
| Foo  | may       | 8   |
| Foo  | june      | 14  |
| Foo  | july      | 25  |
| Foo  | august    | 10  |
| Foo  | september | 13  |
| Foo  | october   | 22  |
| Foo  | november  | 28  |
| Foo  | december  | 14  |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
