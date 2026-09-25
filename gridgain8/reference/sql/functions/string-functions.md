---
description: >-
  Reference of the SQL string functions supported by GridGain — length,
  case, padding, trimming, search/replace, regular-expression, and XML functions.
---

# String Functions

## ASCII

### Description

Returns the ASCII value of the first character in the string as an `int`.

```sql
ASCII(string)
```

### Parameters

`string` - the argument

### Example

Return the ASCII for the first character in the Players' names:

```sql
select ASCII(name) FROM Players;
```

## BIT_LENGTH

### Description

Returns the number of bits in a string as a `long`. For `BLOB`, `CLOB`, `BYTES`, and `JAVA_OBJECT`, the object's specified precision is used. Each character needs 16 bits.

```sql
BIT_LENGTH(string)
```

### Parameters

`string` - the argument

### Example

Return the bit length for Players' names:

```sql
select BIT_LENGTH(name) FROM Players;
```

## LENGTH

### Description

Returns the number of characters in a string as a `long`. For `BLOB`, `CLOB`, `BYTES`, and `JAVA_OBJECT`, the object's specified precision is used.

```sql
{LENGTH | CHAR_LENGTH | CHARACTER_LENGTH} (string)
```

### Parameters

`string` - the argument

### Example

Return the length of Players' names:

```sql
SELECT LENGTH(name) FROM Players;
```

## OCTET_LENGTH

### Description

Returns the number of bytes in a string as a `long`. For `BLOB`, `CLOB`, `BYTES` and `JAVA_OBJECT`, the object's specified precision is used. Each character needs 2 bytes.

```sql
OCTET_LENGTH(string)
```

### Parameters

`string` - the argument

### Example

Return the number of bytes in Players' names:

```sql
SELECT OCTET_LENGTH(name) FROM Players;
```

## CHAR

### Description

Returns the character that represents the ASCII value of an integer as a `string`.

```sql
{CHAR | CHR} (int)
```

### Parameters

`int` - the argument

### Example

Return the ASCII representation from Players' names:

```sql
SELECT CHAR(65)||name FROM Players;
```

## CONCAT

### Description

Concatenates strings. Unlike with the `||` operator, NULL parameters are ignored and do not cause the result to become NULL. This function returns a `string`.

```sql
CONCAT(string, string [,...])
```

### Parameters

`string` - the argument

### Example

Concatenate Players' names:

```sql
SELECT CONCAT(NAME, '!') FROM Players;
```

## CONCAT_WS

### Description

Concatenates strings and inserts a separator. Unlike with the `||` operator, NUL parameters are ignored, and do not cause the result to become NULL. This function returns a `string`.

```sql
CONCAT_WS(separatorString, string, string [,...])
```

### Parameters

- `separatorString` - the separator to insert
- `string` - the argument

### Example

Concatenate Players' names with comma as a separator:

```sql
SELECT CONCAT_WS(',', NAME, '!') FROM Players;
```

## DIFFERENCE

### Description

Returns the difference between the `SOUNDEX()` values of two strings as an`int`.

```sql
DIFFERENCE(X, Y)
```

### Parameters

`X` and `Y` - strings to compare

### Example

Calculate the SOUNDEX() difference for two Players' names:

```sql
select DIFFERENCE(T1.NAME, T2.NAME) FROM players T1, players T2
   WHERE T1.ID = 10 AND T2.ID = 11;
```

## HEXTORAW

### Description

Converts a hex representation of a string to a `string`. Uses 4 hex characters per string character.

```sql
HEXTORAW(string)
```

### Parameters

`string` - a hex string to convert

### Example

Return a string representation of Players' names:

```sql
SELECT HEXTORAW(DATA) FROM Players;
```

## RAWTOHEX

### Description

Converts a string to the hex representation. Uses 4 hex characters per string character. Returns a `string`.

```sql
RAWTOHEX(string)
```

### Parameters

`string` - a string to convert

### Example

Return hex representations of Players' names:

```sql
SELECT RAWTOHEX(DATA) FROM Players;
```

## INSTR

### Description

Returns the location of a search string in a string. If a start position is used, the characters before it are ignored. If the position is negative, the rightmost location is returned. Zero (0) is returned if the search string is not found.

{% hint style="info" %}
This function is case sensitive even if the parameters are not.
{% endhint %}

```sql
INSTR(string, searchString, [, startInt])
```

### Parameters

- `string` - the string to search in
- `searchString` - the string to search for
- `startInt` - start position for the search

### Example

Check if a string includes "@":

```sql
SELECT INSTR(EMAIL,'@') FROM Players;
```

## INSERT

### Description

Inserts an additional string into the original string at a specified start position, returns a `string`.

```sql
INSERT(originalString, startInt, lengthInt, addString)
```

### Parameters

- `originalString` - the original string
- `startInt` - the start position
- `lengthInt` - the number of characters to remove at the start position in the original string
- `addString` - the string to insert

### Example

Insert a blank space at the beginning of Players' names.

```sql
SELECT INSERT(NAME, 1, 1, ' ') FROM Players;
```

## LOWER

### Description

Converts a string to lowercase.

```sql
{LOWER | LCASE} (string)
```

### Parameters

`string` - the string to convert

### Example

Convert to lower case Players' names:

```sql
SELECT LOWER(NAME) FROM Players;
```

## UPPER

### Description

Converts a string to uppercase.

```sql
{UPPER | UCASE} (string)
```

### Parameters

`string` - the string to convert

### Example

Return the last name for each Player in uppercase:

```sql
SELECT UPPER(last_name) "LastNameUpperCase" FROM Players;
```

## LEFT

### Description

Returns the specified number of leftmost characters in a string.

```sql
LEFT(string, int)
```

### Parameters

- `string` - the string to extract the characters from
- `int` - the number of characters to extract

### Example

Extract the first 3 letters from Players' names:

```sql
SELECT LEFT(NAME, 3) FROM Players;
```

## RIGHT

Returns the specified number of rightmost characters in a string.

```sql
RIGHT(string, int)
```

### Parameters

- `string` - the string to extract the characters from
- `int` - the number of characters to extract

### Example

Extract the first 3 letters from Players' names:

```sql
SELECT RIGHT(NAME, 3) FROM Players;
```

## LOCATE

### Description

Returns the location of a search string in a string. If a start position is used, the characters before it are ignored. If the position is negative, the rightmost location is returned. Zero (0) is returned if the search string is not found.

```sql
LOCATE(searchString, string [, startInt])
```

### Parameters

- `searchString` - the string to search for
- `string` - the string to search in
- `startInt` - start position for the search

### Example

Search for period (.) in Players' names:

```sql
SELECT LOCATE('.', NAME) FROM Players;
```

## POSITION

### Description

Returns the location of a search string in a string. A simplified version of [LOCATE](#locate).

```sql
POSITION(searchString, string)
```

### Parameters

- `searchString` - the string to search for
- `string` - the string to search in

### Example

Search for period (.) in Players' names:

```sql
SELECT POSITION('.', NAME) FROM Players;
```

## LPAD

### Description

Left-pads the string to the specified length. If the length is shorter than the string, the string is truncated at the end. If the padding string is not set, spaces are used.

```sql
LPAD(string, int[, paddingString])
```

### Parameters

- `string` - the string to pad
- `int` - the length to pad to
- `paddingString` - the string to pad with

### Example

Left-pad Players' amount with asterisks to the length of 10:

```sql
SELECT LPAD(AMOUNT, 10, '*') FROM Players;
```

## RPAD

### Description

Right-pad the string to the specified length. If the length is shorter than the string, the string is truncated. If the padding string is not set, spaces are used.

```sql
RPAD(string, int[, paddingString])
```

### Parameters

- `string` - the string to pad
- `int` - the length to pad to
- `paddingString` - the string to pad with

### Example

Right-pad Players' text with dashed to the length of 10:

```sql
SELECT RPAD(TEXT, 10, '-') FROM Players;
```

## LTRIM

### Description

Removes all leading spaces from a string.

```sql
LTRIM(string)
```

### Parameters

`string` - the string to left-trim

### Example

Remove leading spaces from Players' names:

```sql
SELECT LTRIM(NAME) FROM Players;
```

## RTRIM

### Description

Removes all trailing spaces from a string.

```sql
RTRIM(string)
```

### Parameters

`string` - the string to right-trim

### Example

Remove trailing spaces from Players' names:

```sql
SELECT RTRIM(NAME) FROM Players;
```

## TRIM

### Description

Removes all leading spaces, trailing spaces, or spaces at both ends, from a string. Other characters can be removed as well.

```sql
TRIM ([{LEADING | TRAILING | BOTH} [string] FROM] string)
```

### Parameters

- `LEADING | TRAILING | BOTH` - indicates where to trim
- `[string]` - (optional) what character(s)/string to trim
- `string` - the string to trim

### Example

Trim underscore characters on both ends of Players' names:

```sql
SELECT TRIM(BOTH '_' FROM NAME) FROM Players;
```

## REGEXP_REPLACE

### Description

Replaces each substring that matches a regular expression. For details, see the [Java String.replaceAll() method](https://www.javatpoint.com/java-string-replaceall). If any parameter is `NULL` (except the optional `flagsString` parameter), the result is `NULL`.

```sql
REGEXP_REPLACE(inputString, regexString, replacementString [, flagsString])
```

### Parameters

- `inputString` - the string to replace substrings in
- `regexString` - the regular expression to match
- `replacementString` - the string to replace the matching substrings with
- `flagString` - possible values are:
  - 'i' enables case insensitive matching (Pattern.CASE_INSENSITIVE)
  - 'c' disables case insensitive matching (Pattern.CASE_INSENSITIVE)
  - 'n' allows the period to match the newline character (Pattern.DOTALL)
  - 'm' enables multiline mode (Pattern.MULTILINE)

  Other symbols cause an exception. Multiple symbols can be used in the `flagsString` parameter; for example, 'im'. Later flags override former ones; for example, 'ic' is equivalent to case sensitive, matching 'c'.

### Example

Returns the names from the Players table with 'w' replaced by 'W':

```sql
SELECT REGEXP_REPLACE(name, 'w+', 'W', 'i') FROM Players;
```

## REGEXP_LIKE

### Description

Matches string to a regular expression. For details, see the [Java Matcher.find() method](https://www.javatpoint.com/post/java-matcher-find-method). If any parameter is `NULL` (except the optional `flagsString` parameter), the result is `NULL`.

```sql
REGEXP_LIKE(inputString, regexString [, flagsString])
```

### Parameters

- `inputString` - the string to match regular expression
- `regexString` - the regular expression to match
- `flagString` - possible values are:
  - 'i' enables case insensitive matching (Pattern.CASE_INSENSITIVE)
  - 'c' disables case insensitive matching (Pattern.CASE_INSENSITIVE)
  - 'n' allows the period to match the newline character (Pattern.DOTALL)
  - 'm' enables multiline mode (Pattern.MULTILINE)

  Other symbols cause an exception. Multiple symbols can be used in the `flagsString` parameter; for example, 'im'. Later flags override former ones; for example, 'ic' is equivalent to case sensitive, matching 'c'.

### Example

Returns Players whose names match 'A-M':

```sql
SELECT REGEXP_LIKE(name, '[A-M ]*', 'i') FROM Players;
```

## REPEAT

### Description

Returns a string repeated the specified number of times.

```sql
REPEAT(string, int)
```

### Parameters

- `string` - the string to repeat
- `int` - the number of times to repeat the string

### Example

Repeat Players' names 10 times:

```sql
SELECT REPEAT(NAME || ' ', 10) FROM Players;
```

## REPLACE

### Description

Replaces all occurrences of a search string in the specified text with another string. If no replacement is specified, the search string is removed from the text. If any parameter is `NULL`, the result is `NULL`.

```sql
REPLACE(string, searchString [, replacementString])
```

### Parameters

- `string` - the text to replace the string in
- `searchString` - the string to replace
- `replacementString` - the string to replace with

### Example

Remove spaces from Players' names:

```sql
SELECT REPLACE(NAME, ' ') FROM Players;
```

## SOUNDEX

### Description

Returns a four-character code representing the `SOUNDEX` of a string. For details, see [http://www.archives.gov/genealogy/census/soundex.html](http://www.archives.gov/genealogy/census/soundex.html). Returns a `string`.

```sql
SOUNDEX(string)
```

### Parameters

`string` - the SOUNDEX source string

### Example

Return the four-character code representing the `SOUNDEX` of Players' names:

```sql
SELECT SOUNDEX(NAME) FROM Players;
```

## SPACE

### Description

Returns a `string` consisting of the specified number of spaces.

```sql
SPACE(int)
```

### Parameters

`int` - the number of spaces in the string to return

### Example

Return two columns: Players' names in one, 80 spaces in the other:

```sql
SELECT name, SPACE(80) FROM Players;
```

## STRINGDECODE

### Description

Converts an encoded string using the Java string literal encoding format. Special characters are `\b`, `\t`, `\n`, `\f`, `\r`, `\"`, `\`, `\<octal>`, `\u<unicode>`. Returns a `string`.

```sql
STRINGDECODE(string)
```

### Parameters

`string` - the string that contains the special characters

### Example

Convert the line break symbol (\n) to a format Java can work with:

```sql
STRINGDECODE('Lines 1\nLine 2');
```

## STRINGENCODE

### Description

Encodes special characters in a string using the Java string literal encoding format. Special characters are `\b`, `\t`, `\n`, `\f`, `\r`, `\"`, `\`, `\<octal>`, `\u<unicode>`. Returns a `string`.

```sql
STRINGENCODE(string)
```

### Parameters

`string` - the string that contains the special characters

### Example

Encode the previously converted line break symbol (\n):

```sql
STRINGENCODE(STRINGDECODE('Lines 1\nLine 2'))
```

## STRINGTOUTF8

### Description

Encodes a string to a byte array using the UTF8 encoding format. Returns `bytes`.

```sql
STRINGTOUTF8(string)
```

### Parameters

`string` - the string to encode

### Example

Encode Players' names:

```sql
SELECT STRINGTOUTF8(name) FROM Players;
```

## SUBSTRING

### Description

Returns a substring of a string starting at the specified position. Also supported is: `SUBSTRING(string [FROM start] [FOR length])`.

```sql
{SUBSTRING | SUBSTR} (string, startInt [, lengthInt])
SUBSTRING(string [FROM start] [FOR length])
```

### Parameters

- `string` - the string to extract the substring from
- `startInt` | `start` - the starting position for the substring to extract; if negative, the start index is relative to the end of the string
- `lengthInt` | `length` - (optional) the length of the substring to extract

### Example

From Players names, extract a 5-character long substring that starts at the second position:

```sql
SELECT SUBSTR(name, 2, 5) FROM Players;
```

## TO_CHAR

### Description

Formats a timestamp, number, or text.

```sql
TO_CHAR(value [, formatString[, nlsParamString]])
```

### Parameters

- `formatString` - the string to be formatted
- `nlsParamString` - the format to use

### Example

Format the '2010-01-01 00:00:00' timestamp to 'DD MON, YYYY':

```sql
TO_CHAR(TIMESTAMP '2010-01-01 00:00:00', 'DD MON, YYYY')
```

## TRANSLATE

### Description

Replaces a sequence of characters in a string with another set of characters.

```sql
TRANSLATE(value , searchString, replacementString]])
```

### Parameters

- `value` - the string that contains the character sequence(s)
- `searchString` - the sequence of characters to replace
- `replacementString` - the string to replace the sequence of characters with

### Example

Replace 'el' from 'Hello world!' with 'EL':

```sql
TRANSLATE('Hello world', 'el', 'EL')
```

## UTF8TOSTRING

### Description

Decodes a byte array in the UTF8 format to a string.

```sql
UTF8TOSTRING(bytes)
```

### Parameters

`bytes` - the array to decode

### Example

Decode byte array derived from Players' names:

```sql
SELECT UTF8TOSTRING(name) FROM Players;
```

## XMLATTR

### Description

Creates an XML attribute element in the `name=value` form. The value is encoded as XML text. Returns a `string`.

```sql
XMLATTR(nameString, valueString)
```

### Parameters

- `nameString` - the 'name' part of the element
- `valueString` - the 'value' part of the element

### Example

Create the 'href=http://h2database.com' XML element:

```sql
XMLNODE('a', XMLATTR('href', 'http://h2database.com'))
```

## XMLNODE

### Description

Creates an XML node element. An empty or null attribute string means no attributes are set. An empty or null content string means the node is empty. The content is indented by default if it contains a newline. This function returns a `string`.

```sql
XMLNODE(elementString [, attributesString [, contentString [, indentBoolean]]])
```

### Parameters

- `elementString` - the name of the element/node to create
- `attributeString` - the list of attributes for the element/node to create
- `contentString` - the element/node content
- `indentBoolean` - 'yes' to indent the node element, 'no' otherwise

### Example

Create 'a' XML node element at the H2 indentation level:

```sql
XMLNODE('a', XMLATTR('href', 'http://h2database.com'), 'H2')
```

## XMLCOMMENT

### Description

Creates an XML comment. Two dashes (`--`) are converted to `- -`. This function returns a `string`.

```sql
XMLCOMMENT(commentString)
```

### Parameters

`commentString` - the comment content

### Example

Create the 'Test' comment:

```sql
XMLCOMMENT('Test')
```

## XMLCDATA

### Description

Creates an XML CDATA element. If the value contains `]]>`, an XML text element is created instead. This function returns a `string`.

```sql
XMLCDATA(valueString)
```

### Parameters

`valueString` - the CDATA/text element's content

### Example

Create the 'data' CDATA element:

```sql
XMLCDATA('data')
```

## XMLSTARTDOC

### Description

Returns the XML declaration. The result is always `<?xml version=1.0?>`.

```sql
XMLSTARTDOC()
```

### Example

```sql
XMLSTARTDOC()
```

## XMLTEXT

### Description

Creates an XML text element, returns a `string`.

```sql
XMLTEXT(valueString [, escapeNewlineBoolean])
```

### Parameters

- `valueString` - the text element's content
- `escapeNewlineBoolean` - if 'yes', newline and linefeed are converted to an XML entity (`&#`)

### Example

Create the 'data' XML text element:

```sql
XMLTEXT(('data'))
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
