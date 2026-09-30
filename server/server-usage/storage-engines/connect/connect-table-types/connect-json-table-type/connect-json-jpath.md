---
description: >-
  How CONNECT JSON columns address JSON data with Jpath: path syntax, array operators and expansion, calculated values, and handling of NULL values.
---

# CONNECT JSON Jpath Specification

From Connect 1.6, the Jpath specification has changed to be the one of the native JSON functions and more compatible with what is generally used. It is close to the standard definition and compatible to what MongoDB and other products do. The ‘:’ separator is replaced by ‘.’. Position in array is accepted MongoDB style with no square brackets. Array specification specific to CONNECT are still accepted but \[\*] is used for expanding and \[x] for multiply. However, tables created with the previous syntax can still be used by adding SEP\_CHAR=’:’ (can be done with alter table). Also, it can be now specified as JPATH (was FIELD\_FORMAT) but FIELD\_FORMAT is still accepted.

Until Connect 1.5, it is the description of the path to follow to reach the required item. Each step is the key name (case sensitive) of the pair when crossing an object, and the number of the value between square brackets when crossing an array. Each specification is separated by a ‘:’ character.

From Connect 1.6, It is the description of the path to follow to reach the required item. Each step is the key name (case sensitive) of the pair when crossing an object, and the position number of the value when crossing an array. Key specifications are separated by a ‘.’ character.

For instance, in the above file, the last name of the second author of a book is reached by:

$.AUTHOR\[1].LASTNAME _standard style$AUTHOR.1.LASTNAME_ MongoDB style\
AUTHOR:\[1]:LASTNAME _old style when SEP\_CHAR=’:’ or until Connect 1.5_

The ‘$’ or “$.” prefix specifies the root of the path and can be omitted with CONNECT.

The array specification can also indicate how it must be processed:

For instance, in the above file, the last name of the second author of a book is reached by:

```
AUTHOR:[1]:LASTNAME
```

The array specification can also indicate how it must be processed:

| Specification                                                        | Array Type | Limit | Description                                                                                               |
| -------------------------------------------------------------------- | ---------- | ----- | --------------------------------------------------------------------------------------------------------- |
| n (Connect >= 1.6) or \[n]\[1] | All        | N.A   | Take the nth value of the array.                                                                          |
| \[\*] (Connect >= 1.6), \[X] or \[x] (Connect <= 1.5)                | All        |       | Expand. Generate one row for each array value.                                                            |
| \["string"]                                                          | String     |       | Concatenate all values separated by the specified string.                                                 |
| \[+]                                                                 | Numeric    |       | Make the sum of all the non-null array values.                                                            |
| \[x] (Connect >= 1.6), \[\*] (Connect <= 1.5)                        | Numeric    |       | Make the product of all non-null array values.                                                            |
| \[!]                                                                 | Numeric    |       | Make the average of all the non-null array values.                                                        |
| \[>] or \[<]                                                         | All        |       | Return the greatest or least non-null value of the array.                                                 |
| \[#]                                                                 | All        | N.A   | Return the number of values in the array.                                                                 |
| \[]                                                                  | All        |       | Expand if under an expanded object. Otherwise sum if numeric, else concatenation separated by “, “.       |
|                                                                      | All        |       | Between two separators, if an array, expand it if under an expanded object or take the first value of it. |

Note 1: When the LIMIT restriction is applicable, only the first _m_ array items are used, _m_ being the value of the LIMIT option (to be specified in option\_list). The LIMIT default value is 10.

Note 2: An alternative way to indicate what is to be expanded is to use the expand option in the option list, for instance:

```
OPTION_LIST='Expand=AUTHOR'
```

`AUTHOR` is here the key of the pair that has the array as a value (case sensitive). Expand is limited to only one branch (expanded arrays must be under the same object).

Let us take as an example the file `expense.json` ([found here](../../json-sample-files.md)).\
The table jexpall expands all under and including the week array:

From Connect 1.07.0002

```sql
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) jpath='$.WEEK[*].NUMBER',
WHAT CHAR(32) jpath='$.WEEK[*].EXPENSE[*].WHAT',
AMOUNT DOUBLE(8,2) jpath='$.WEEK[*].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect.1.6

```
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) field_format='$.WEEK[*].NUMBER',
WHAT CHAR(32) field_format='$.WEEK[*].EXPENSE[*].WHAT',
AMOUNT DOUBLE(8,2) field_format='$.WEEK[*].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) field_format='WEEK:[x]:NUMBER',
WHAT CHAR(32) field_format='WEEK:[x]:EXPENSE:[x]:WHAT',
AMOUNT DOUBLE(8,2) field_format='WEEK:[x]:EXPENSE:[x]:AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

| WHO   | WEEK | WHAT | AMOUNT |
| ----- | ---- | ---- | ------ |
| Joe   | 3    | Beer | 18.00  |
| Joe   | 3    | Food | 12.00  |
| Joe   | 3    | Food | 19.00  |
| Joe   | 3    | Car  | 20.00  |
| Joe   | 4    | Beer | 19.00  |
| Joe   | 4    | Beer | 16.00  |
| Joe   | 4    | Food | 17.00  |
| Joe   | 4    | Food | 17.00  |
| Joe   | 4    | Beer | 14.00  |
| Joe   | 5    | Beer | 14.00  |
| Joe   | 5    | Food | 12.00  |
| Beth  | 3    | Beer | 16.00  |
| Beth  | 4    | Food | 17.00  |
| Beth  | 4    | Beer | 15.00  |
| Beth  | 5    | Food | 12.00  |
| Beth  | 5    | Beer | 20.00  |
| Janet | 3    | Car  | 19.00  |
| Janet | 3    | Food | 18.00  |
| Janet | 3    | Beer | 18.00  |
| Janet | 4    | Car  | 17.00  |
| Janet | 5    | Beer | 14.00  |
| Janet | 5    | Car  | 12.00  |
| Janet | 5    | Beer | 19.00  |
| Janet | 5    | Food | 12.00  |

The table `jexpw` shows what was bought and the sum and average of amounts for each person and week:

From Connect 1.07.0002

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL jpath='$.WEEK[*].NUMBER',
WHAT CHAR(32) NOT NULL jpath='$.WEEK[].EXPENSE[", "].WHAT',
SUM DOUBLE(8,2) NOT NULL jpath='$.WEEK[].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL jpath='$.WEEK[].EXPENSE[!].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect 1.6:

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL field_format='$.WEEK[*].NUMBER',
WHAT CHAR(32) NOT NULL field_format='$.WEEK[].EXPENSE[", "].WHAT',
SUM DOUBLE(8,2) NOT NULL field_format='$.WEEK[].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='$.WEEK[].EXPENSE[!].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL field_format='WEEK:[x]:NUMBER',
WHAT CHAR(32) NOT NULL field_format='WEEK::EXPENSE:[", "]:WHAT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK::EXPENSE:[+]:AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK::EXPENSE:[!]:AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

| WHO   | WEEK | WHAT                         | SUM   | AVERAGE |
| ----- | ---- | ---------------------------- | ----- | ------- |
| Joe   | 3    | Beer, Food, Food, Car        | 69.00 | 17.25   |
| Joe   | 4    | Beer, Beer, Food, Food, Beer | 83.00 | 16.60   |
| Joe   | 5    | Beer, Food                   | 26.00 | 13.00   |
| Beth  | 3    | Beer                         | 16.00 | 16.00   |
| Beth  | 4    | Food, Beer                   | 32.00 | 16.00   |
| Beth  | 5    | Food, Beer                   | 32.00 | 16.00   |
| Janet | 3    | Car, Food, Beer              | 55.00 | 18.33   |
| Janet | 4    | Car                          | 17.00 | 17.00   |
| Janet | 5    | Beer, Car, Beer, Food        | 57.00 | 14.25   |

Let us see what the table `jexpz` does:

From Connect 1.6:

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL field_format='WEEK[", "].NUMBER',
SUMS CHAR(64) NOT NULL field_format='WEEK["+"].EXPENSE[+].AMOUNT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK[+].EXPENSE[+].AMOUNT',
AVGS CHAR(64) NOT NULL field_format='WEEK["+"].EXPENSE[!].AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL field_format='WEEK[+].EXPENSE[!].AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL field_format='WEEK[!].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK[!].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect 1.07.0002

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL jpath='WEEK[", "].NUMBER',
SUMS CHAR(64) NOT NULL jpath='WEEK["+"].EXPENSE[+].AMOUNT',
SUM DOUBLE(8,2) NOT NULL jpath='WEEK[+].EXPENSE[+].AMOUNT',
AVGS CHAR(64) NOT NULL jpath='WEEK["+"].EXPENSE[!].AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL jpath='WEEK[+].EXPENSE[!].AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL jpath='WEEK[!].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL jpath='WEEK[!].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL field_format='WEEK:[", "]:NUMBER',
SUMS CHAR(64) NOT NULL field_format='WEEK:["+"]:EXPENSE:[+]:AMOUNT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK:[+]:EXPENSE:[+]:AMOUNT',
AVGS CHAR(64) NOT NULL field_format='WEEK:["+"]:EXPENSE:[!]:AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL field_format='WEEK:[+]:EXPENSE:[!]:AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL field_format='WEEK:[!]:EXPENSE:[+]:AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK:[!]:EXPENSE:[x]:AMOUNT')
ENGINE=CONNECT table_type=JSON
File_name='E:/Data/Json/expense2.json';
```

| WHO   | WEEKS   | SUMS              | SUM    | AVGS              | SUMAVG | AVGSUM | AVERAGE |
| ----- | ------- | ----------------- | ------ | ----------------- | ------ | ------ | ------- |
| Joe   | 3, 4, 5 | 69.00+83.00+26.00 | 178.00 | 17.25+16.60+13.00 | 46.85  | 59.33  | 16.18   |
| Beth  | 3, 4, 5 | 16.00+32.00+32.00 | 80.00  | 16.00+16.00+16.00 | 48.00  | 26.67  | 16.00   |
| Janet | 3, 4, 5 | 55.00+17.00+57.00 | 129.00 | 18.33+17.00+14.25 | 49.58  | 43.00  | 16.12   |

For all persons:

* Column 1 show the person name.
* Column 2 shows the weeks for which values are calculated.
* Column 3 lists the sums of expenses for each week.
* Column 4 calculates the sum of all expenses by person.
* Column 5 shows the week’s expense averages.
* Column 6 calculates the sum of these averages.
* Column 7 calculates the average of the week’s sum of expenses.
* Column 8 calculates the average expense by person.

It would be very difficult, if even possible, to obtain this result from table `jexpall` using an SQL query.

## Handling of NULL Values

Json has a null explicit value that can be met in arrays or object key values. When regarding json as a relational table, a column value can be null because the corresponding json item is explicitly null, or implicitly because the corresponding item is missing in an array or object. CONNECT does not make any distinction between explicit and implicit nulls.

However, it is possible to specify how nulls are handled and represented. This is done by setting the string session variable [connect\_json\_null](../../connect-system-variables.md#connect_json_null). The default value of connect\_json\_null is “”; it can be changed, for instance, by:

```
SET connect_json_null='NULL';
```

This changes its representation when a column displays the text of an object or the concatenation of the values of an array.

It is also possible to tell CONNECT to ignore nulls by:

```
SET connect_json_null=NULL;
```

When doing so, nulls do not appear in object text or array lists. However, this does not change the behavior of array calculation nor the result of array count.

## Notes

1. The value n can be 0 based or 1 based depending on the base table option. The default is 0 to match what is the current usage in the Json world but it can be set to 1 for tables created in old versions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
