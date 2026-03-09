---
description: The CONNECT storage engine.
---

# CONNECT PIVOT Table Type

This table type can be used to transform the result of another table or view (called the source table) into a pivoted table along “pivot” and “facts” columns. A pivot table is a great reporting tool that sorts and sums (by default) independent of the original data layout in the source table.

For example, let us suppose you have the following “Expenses” table:

| Who   | Week | What | Amount |
| ----- | ---- | ---- | ------ |
| Joe   | 3    | Beer | 18.00  |
| Beth  | 4    | Food | 17.00  |
| Janet | 5    | Beer | 14.00  |
| Joe   | 3    | Food | 12.00  |
| Joe   | 4    | Beer | 19.00  |
| Janet | 5    | Car  | 12.00  |
| Joe   | 3    | Food | 19.00  |
| Beth  | 4    | Beer | 15.00  |
| Janet | 5    | Beer | 19.00  |
| Joe   | 3    | Car  | 20.00  |
| Joe   | 4    | Beer | 16.00  |
| Beth  | 5    | Food | 12.00  |
| Beth  | 3    | Beer | 16.00  |
| Joe   | 4    | Food | 17.00  |
| Joe   | 5    | Beer | 14.00  |
| Janet | 3    | Car  | 19.00  |
| Joe   | 4    | Food | 17.00  |
| Beth  | 5    | Beer | 20.00  |
| Janet | 3    | Food | 18.00  |
| Joe   | 4    | Beer | 14.00  |
| Joe   | 5    | Food | 12.00  |
| Janet | 3    | Beer | 18.00  |
| Janet | 4    | Car  | 17.00  |
| Janet | 5    | Food | 12.00  |

Pivoting the table contents using the 'Who' and 'Week' fields for the left\
columns, and the 'What' field for the top heading and summing the 'Amount'\
fields for each cell in the new table, gives the following desired result:

| Who   | Week | Beer  | Car   | Food  |
| ----- | ---- | ----- | ----- | ----- |
| Beth  | 3    | 16.00 | 0.00  | 0.00  |
| Beth  | 4    | 15.00 | 0.00  | 17.00 |
| Beth  | 5    | 20.00 | 0.00  | 12.00 |
| Janet | 3    | 18.00 | 19.00 | 18.00 |
| Janet | 4    | 0.00  | 17.00 | 0.00  |
| Janet | 5    | 33.00 | 12.00 | 12.00 |
| Joe   | 3    | 18.00 | 20.00 | 31.00 |
| Joe   | 4    | 49.00 | 0.00  | 34.00 |
| Joe   | 5    | 14.00 | 0.00  | 12.00 |

Note that SQL enables you to get the same result presented differently by using\
the “group by” clause, namely:

```sql
SELECT who, week, what, SUM(amount) FROM expenses
       GROUP BY who, week, what;
```

However there is no way to get the pivoted layout shown above just using SQL.\
Even using embedded SQL programming for some DBMS is not quite simple and\
automatic.

The Pivot table type of CONNECT makes doing this much simpler.

## Using the PIVOT Tables Type

To get the result shown in the example above, just define it as a new table\
with the statement:

```sql
CREATE TABLE pivex
ENGINE=connect table_type=pivot tabname=expenses;
```

You can now use it as any other table, for instance to display the result shown\
above, just say:

```sql
SELECT * FROM pivex;
```

The CONNECT implementation of the PIVOT table type does much of the work\
required to transform the source table:

1. Finding the “Facts” column, by default the last column of the source table. Finding “Facts” or “Pivot” columns work only for table based pivot tables. They do not for view or srcdef based pivot tables, for which they must be explicitly specified.
2. Finding the “Pivot” column, by default the last remaining column.
3. Choosing the aggregate function to use, “SUM” by default.
4. Constructing and executing the “Group By” on the “Facts” column, getting its\
   result in memory.
5. Getting all the distinct values in the “Pivot” column and defining a “Data”\
   column for each.
6. Spreading the result of the intermediate memory table into the final table.

The source table “Pivot” column must not be nullable (there are no such things as a “null”\
column) The creation are refused even is this nullable column actually does not contain null values.

If a different result is desired, Create Table options are available to change\
the defaults used by Pivot. For instance if we want to display the average\
expense for each person and product, spread in columns for each week, use the\
following statement:

```sql
CREATE TABLE pivex2
ENGINE=connect table_type=pivot tabname=expenses
option_list='PivotCol=Week,Function=AVG';
```

Now saying:

```sql
SELECT * FROM pivex2;
```

Will display the resulting table:

| Who   | What | 3     | 4     | 5     |
| ----- | ---- | ----- | ----- | ----- |
| Beth  | Beer | 16.00 | 15.00 | 20.00 |
| Beth  | Food | 0.00  | 17.00 | 12.00 |
| Janet | Beer | 18.00 | 0.00  | 16.50 |
| Janet | Car  | 19.00 | 17.00 | 12.00 |
| Janet | Food | 18.00 | 0.00  | 12.00 |
| Joe   | Beer | 18.00 | 16.33 | 14.00 |
| Joe   | Car  | 20.00 | 0.00  | 0.00  |
| Joe   | Food | 15.50 | 17.00 | 12.00 |

## Restricting the Columns in a Pivot Table

Let us suppose that we want a Pivot table from expenses summing the expenses\
for all people and products whatever week it was bought. We can do this just by\
removing from the pivex table the week column from the column list.

```sql
ALTER TABLE pivex DROP COLUMN week;
```

The result we get from the new table is:

| Who   | Beer  | Car   | Food  |
| ----- | ----- | ----- | ----- |
| Beth  | 51.00 | 0.00  | 29.00 |
| Janet | 51.00 | 48.00 | 30.00 |
| Joe   | 81.00 | 20.00 | 77.00 |

Note: Restricting columns is also needed when the source table contains extra columns that should not be part of the pivot table. This is true in particular for key columns that prevent a proper grouping.

## PIVOT Create Table Syntax

The Create Table statement for PIVOT tables uses the following syntax:

```sql
CREATE TABLE pivot_table_name
[(column_definition)]
ENGINE=CONNECT table_type=PIVOT
{tabname='source_table_name' | srcdef='source_table_def'}
[option_list='pivot_table_option_list'];
```

The column definition has two sets of columns:

1. A set of columns belonging to the source table, not including the “facts” and\
   “pivot” columns.
2. “Data” columns receiving the values of the aggregated “facts” columns named\
   from the values of the “pivot” column. They are indicated by the “flag”\
   option.

The **options** and **sub-options** available for Pivot tables are:

| Option     | Type             | Description                                                                                                                |
| ---------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Tabname    | \[DB.]Name       | The name of the table to “pivot”. If not set SrcDef must be specified.                                                     |
| SrcDef     | SQL\_statement   | The statement used to generate the intermediate mysql table.                                                               |
| DBname     | name             | The name of the database containing the source table. Defaults to the current database.                                    |
| Function\* | name             | The name of the aggregate function used for the data columns, SUM by default.                                              |
| PivotCol\* | name             | Specifies the name of the Pivot column whose values are used to fill the “data” columns having the flag option.            |
| FncCol\*   | \[func(]name\[)] | Specifies the name of the data “Facts” column. If the form func(name) is used, the aggregate function name is set to func. |
| Groupby\*  | Boolean          | Set it to True (1 or Yes) if the table already has a GROUP BY format.                                                      |
| Accept\*   | Boolean          | To accept non matching Pivot column values.                                                                                |

* : These options must be specified in the OPTION\_LIST.

### Additional Access Options

There are four cases where pivot must call the server containing the source table or on which the SrcDef statement must be executed:

1. The source table is not a CONNECT table.
2. The SrcDef option is specified.
3. The source table is on another server.
4. The columns are not specified.

By default, pivot tries to call the currently used server using host=localhost, user=root not using password, and port=3306. However, this may not be what is needed, in particular if the local root user has a password in which case you can get an “access denied” error message when creating or using the pivot table.

Specify the host, user, password and/or port options in the option\_list to override the default connection options used to access the source table, get column specifications, execute the generated group by or SrcDef query.

## Defining a Pivot Table

There are principally two ways to define a PIVOT table:

1. From an existing table or view.
2. Directly giving the SQL statement returning the result to pivot.

### Defining a Pivot Table from a Source Table

The **tabname** standard table option is used to give the name of the source table or view.

For tables, the internal Group By are internally generated, except when the `GROUP BY` option is specified as true. Do it only when the table or view has a valid `GROUP BY` format.

### Directly Defining the Source of a Pivot Table in SQL

Alternatively, the internal source can be directly defined using the **SrcDef** option that must have the proper group by format.

As we have seen above, a proper Pivot Table is made from an internal intermediate table resulting from the execution of a `GROUP BY` statement. In many cases, it is simpler or desirable to directly specify this when creating the pivot table. This may be because the source is the result of a complex\
process including filtering and/or joining tables.

To do this, use the **SrcDef** option, often replacing all other options. For instance, suppose that in the first example we are only interested in weeks 4 and 5. We could of course display it by:

```sql
SELECT * FROM pivex WHERE week IN (4,5);
```

However, what if this table is a huge table? In this case, the correct way to do it is to define the pivot table as this:

```sql
CREATE TABLE pivex4
ENGINE=connect table_type=pivot
option_list='PivotCol=what,FncCol=amount'
SrcDef='select who, week, what, sum(amount) from expenses
where week in (4,5) group by who, week, what';
```

If your source table has millions of records and you plan to pivot only a small subset of it, doing so will make a lot of a difference performance wise. In addition, you have entire liberty to use expressions, scalar functions, aliases, join, where and having clauses in your SQL statement. The only constraint is that you are responsible for the result of this statement to have the correct format for the pivot processing.

Using SrcDef also permits to use expressions and/or scalar functions. For instance:

```sql
CREATE TABLE xpivot (
Who CHAR(10) NOT NULL,
What CHAR(12) NOT NULL,
First DOUBLE(8,2) flag=1,
Middle DOUBLE(8,2) flag=1,
Last DOUBLE(8,2) flag=1)
ENGINE=connect table_type=PIVOT
option_list='PivotCol=wk,FncCol=amnt'
Srcdef='select who, what, case when week=3 then ''First'' when
week=5 then ''Last'' else ''Middle'' end as wk, sum(amount) *
6.56 as amnt from expenses group by who, what, wk';
```

Now the statement:

```sql
SELECT * FROM xpivot;
```

Will display the result:

| Who   | What | First  | Middle | Last   |
| ----- | ---- | ------ | ------ | ------ |
| Beth  | Beer | 104.96 | 98.40  | 131.20 |
| Beth  | Food | 0.00   | 111.52 | 78.72  |
| Janet | Beer | 118.08 | 0.00   | 216.48 |
| Janet | Car  | 124.64 | 111.52 | 78.72  |
| Janet | Food | 118.08 | 0.00   | 78.72  |
| Joe   | Beer | 118.08 | 321.44 | 91.84  |
| Joe   | Car  | 131.20 | 0.00   | 0.00   |
| Joe   | Food | 203.36 | 223.04 | 78.72  |

**Note 1:** to avoid multiple lines having the same fixed column values, it is mandatory in **SrcDef** to place the pivot column at the end of the group by\
list.

**Note 2:** in the create statement **SrcDef**, it is mandatory to give aliases **to** the columns containing expressions so they are recognized by the other options.

**Note 3:** in the **SrcDef** select statement, quotes must be escaped because the entire statement is passed to MariaDB between quotes. Alternatively, specify it between double quotes.

**Note 4:** We could have left CONNECT do the column definitions. However, because they are defined from the sorted names, the Middle column had been placed at the end of them.

## Specifying the Columns Corresponding to the Pivot Column

These columns must be named from the values existing in the “pivot” column. For instance, supposing we have the following _pet_ table:

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

Pivoting it using _race_ as the pivot column is done with:

```sql
CREATE TABLE pivet
ENGINE=connect table_type=pivot tabname=pet
option_list='PivotCol=race,groupby=1';
```

This gives the result:

| name    | dog | cat | rabbit | bird | fish |
| ------- | --- | --- | ------ | ---- | ---- |
| John    | 2   | 0   | 0      | 0    | 0    |
| Bill    | 0   | 1   | 0      | 0    | 0    |
| Mary    | 1   | 1   | 0      | 0    | 0    |
| Lisbeth | 0   | 0   | 2      | 0    | 0    |
| Kevin   | 0   | 2   | 0      | 6    | 0    |
| Donald  | 1   | 0   | 0      | 0    | 3    |

By the way, does this ring a bell? It shows that in a way PIVOT tables are doing the opposite of what OCCUR tables do.

We can alternatively define specifically the table columns but what happens if the Pivot column contains values that is not matching a “data” column? There are three cases depending on the specified options and flags.

**First case:** If no specific options are specified, this is an error an when trying to display the table. The query will abort with an error message stating that a non-matching value was met. Note that because the column list is established when creating the table, this is prone to occur if some rows containing new values for the pivot column are inserted in the source table. If this happens, you should re-create the table or manually add the new columns to the pivot table.

**Second case:** The accept option was specified. For instance:

```sql
CREATE TABLE xpivet2 (
name VARCHAR(12) NOT NULL,
dog INT NOT NULL DEFAULT 0 flag=1,
cat INT NOT NULL DEFAULT 0 flag=1)
ENGINE=connect table_type=pivot tabname=pet
option_list='PivotCol=race,groupby=1,Accept=1';
```

No error are raised and the non-matching values are ignored. This table are displayed as:

| name    | dog | cat |
| ------- | --- | --- |
| John    | 2   | 0   |
| Bill    | 0   | 1   |
| Mary    | 1   | 1   |
| Lisbeth | 0   | 0   |
| Kevin   | 0   | 2   |
| Donald  | 1   | 0   |

**Third case:** A “dump” column was specified with the flag value equal to 2. All non-matching values are added in this column. For instance:

```sql
CREATE TABLE xpivet (
name VARCHAR(12) NOT NULL,
dog INT NOT NULL DEFAULT 0 flag=1,
cat INT NOT NULL DEFAULT 0 flag=1,
other INT NOT NULL DEFAULT 0 flag=2)
ENGINE=connect table_type=pivot tabname=pet
option_list='PivotCol=race,groupby=1';
```

This table are displayed as:

| name    | dog | cat | other |
| ------- | --- | --- | ----- |
| John    | 2   | 0   | 0     |
| Bill    | 0   | 1   | 0     |
| Mary    | 1   | 1   | 0     |
| Lisbeth | 0   | 0   | 2     |
| Kevin   | 0   | 2   | 6     |
| Donald  | 1   | 0   | 3     |

It is a good idea to provide such a “dump” column if the source table is prone to be inserted new\
rows that can have a value for the pivot column that did not exist when the pivot table was created.

## Pivoting Big Source Tables

This may sometimes be risky. If the pivot column contains too many distinct values, the resulting table may have too many columns. In all cases the process involved, finding distinct values when creating the table or doing the group by when using it, can be very long and sometimes can fail because of exhausted memory.

Restrictions by a where clause should be applied to the source table when creating the pivot table rather than to the pivot table itself. This can be done by creating an intermediate table or using as source a view or a srcdef option.

All PIVOT tables are read only.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
