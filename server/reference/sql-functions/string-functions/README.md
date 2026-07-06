---
description: >-
  Learn about string functions in MariaDB Server. This section details SQL
  functions for manipulating, searching, and formatting text strings, essential
  for data cleansing and presentation.
---

# String Functions

{% columns %}
{% column %}
{% content-ref url="ascii.md" %}
[ascii.md](ascii.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the ASCII value of the first character. This function returns the numeric ASCII code for the leftmost character of the input string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bin.md" %}
[bin.md](bin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the binary representation of a number. This function converts a number to its binary string equivalent.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-operator.md" %}
[binary-operator.md](binary-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Cast a string to a binary string. This operator converts a character string to a binary string, often used for case-sensitive comparisons.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bit_length.md" %}
[bit_length.md](bit_length.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the length of a string in bits. This function calculates the size of the string in bits (length in bytes multiplied by 8).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cast.md" %}
[cast.md](cast.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete CAST reference for MariaDB. Complete function guide with syntax, parameters, return values, and usage examples with comprehensive examples and best.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="char-function.md" %}
[char-function.md](char-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the character for each integer passed. This function interprets arguments as integer ASCII values and returns a string of those characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="char_length.md" %}
[char_length.md](char_length.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the length of a string in characters. This function counts the number of characters in the string, treating multi-byte characters as single units.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="character_length.md" %}
[character_length.md](character_length.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for CHAR_LENGTH(). Returns the number of characters in the string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="chr.md" %}
[chr.md](chr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the character for a specific ASCII value. This function is similar to CHAR() but accepts a single integer argument.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="concat.md" %}
[concat.md](concat.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete CONCAT reference for MariaDB. Complete function guide with syntax, parameters, return values, and usage examples with comprehensive examples and.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="concat_ws.md" %}
[concat_ws.md](concat_ws.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Concatenate with separator. This function joins strings with a specified separator. It skips NULL values during concatenation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="convert.md" %}
[convert.md](convert.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete CONVERT() reference: CONVERT(expr,type) and CONVERT(expr USING charset) syntax, SIGNED/UNSIGNED/BINARY/CHAR types, and CAST() differences.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="elt.md" %}
[elt.md](elt.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the string at a specific index. This function returns the N-th string from a list of arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="export_set.md" %}
[export_set.md](export_set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a string representation of bits. This function generates a string based on the bits set in a number, using specified 'on' and 'off' strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="extractvalue.md" %}
[extractvalue.md](extractvalue.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract a value from XML. This function returns the text content of an XML fragment matching a given XPath expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="field.md" %}
[field.md](field.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the index of a string in a list. This function returns the position of the first argument within the subsequent list of arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="find_in_set.md" %}
[find_in_set.md](find_in_set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the index of a string in a comma-separated list. This function finds the position of a string within a list of strings separated by commas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="format.md" %}
[format.md](format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Format a number. This function formats a number to a format like '#,###,###.##', rounded to a specified number of decimal places.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="from_base64.md" %}
[from_base64.md](from_base64.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Decode a base-64 encoded string. This function takes a base-64 string and returns the decoded binary result.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hex.md" %}
[hex.md](hex.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the hexadecimal representation. This function converts a number or string to its hexadecimal string equivalent.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="insert-function.md" %}
[insert-function.md](insert-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert a substring into a string. This function inserts a string within another string at a specified position and length, replacing existing characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="instr.md" %}
[instr.md](instr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the position of the first occurrence of a substring. This function locates a substring within a string and returns its index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lcase.md" %}
[lcase.md](lcase.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for LOWER(). Converts a string to lowercase characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="left.md" %}
[left.md](left.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the leftmost characters. This function returns the specified number of characters from the beginning (left) of a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="length.md" %}
[length.md](length.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the length of a string in bytes. This function counts the number of bytes in the string, which may differ from character count for multi-byte strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lengthb.md" %}
[lengthb.md](lengthb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the length of a string in bytes. This function is a synonym for LENGTH() in default mode, returning the byte count.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="like.md" %}
[like.md](like.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete LIKE operator reference: LIKE/NOT LIKE pattern matching syntax, % and _ wildcards, ESCAPE clause, NULL behavior, and collation case-sensitivity.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load_file.md" %}
[load_file.md](load_file.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Read a file from the server. This function reads the content of a file located on the server host and returns it as a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="locate.md" %}
[locate.md](locate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the position of the first occurrence of a substring. This function finds the starting position of a substring within a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lower.md" %}
[lower.md](lower.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a string to lowercase. This function returns the string with all characters converted to lowercase.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lpad.md" %}
[lpad.md](lpad.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Left-pad a string. This function pads a string on the left side with a specified string until it reaches a certain length.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ltrim.md" %}
[ltrim.md](ltrim.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove leading spaces. This function returns the string with any leading whitespace characters removed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="make_set.md" %}
[make_set.md](make_set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a set of comma-separated strings. This function returns a string consisting of substrings corresponding to the set bits in a given number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="match-against.md" %}
[match-against.md](match-against.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform a full-text search. This construct searches for a text query against a set of columns indexed with a FULLTEXT index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mid.md" %}
[mid.md](mid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for SUBSTRING(). Returns a substring starting at a specified position for a given length.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="natural_sort_key.md" %}
[natural_sort_key.md](natural_sort_key.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Generate a sort key for natural ordering. This function produces a key that allows strings containing numbers to be sorted in a human-readable order.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="not-like.md" %}
[not-like.md](not-like.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Negated pattern matching. This operator tests whether a string does NOT match a specified SQL pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="not-regexp.md" %}
[not-regexp.md](not-regexp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Negated regular expression matching. This operator tests whether a string does NOT match a specified regular expression pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="octet_length.md" %}
[octet_length.md](octet_length.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the length of a string in bytes. This function is a synonym for LENGTH() and returns the number of bytes in the string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ord.md" %}
[ord.md](ord.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the numeric value of the first character. This function returns the code for the leftmost character, supporting multi-byte characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="position.md" %}
[position.md](position.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for LOCATE(). Returns the position of the first occurrence of a substring within a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="quote.md" %}
[quote.md](quote.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Quote a string for SQL usage. This function produces a string ready for use as a data value in an SQL statement, escaping special characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repeat-function.md" %}
[repeat-function.md](repeat-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Repeat a string. This function returns a string consisting of the input string repeated a specified number of times.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replace-function.md" %}
[replace-function.md](replace-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete REPLACE Function reference for MariaDB. Complete function guide with syntax, parameters, return values, and usage examples for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="reverse.md" %}
[reverse.md](reverse.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reverse a string. This function returns the string with the order of its characters reversed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="right.md" %}
[right.md](right.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the rightmost characters. This function returns the specified number of characters from the end (right) of a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rpad.md" %}
[rpad.md](rpad.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Right-pad a string. This function pads a string on the right side with a specified string until it reaches a certain length.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rtrim.md" %}
[rtrim.md](rtrim.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove trailing spaces. This function returns the string with any trailing whitespace characters removed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sformat.md" %}
[sformat.md](sformat.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Format strings with arbitrary patterns. This function allows complex string formatting using a pattern string and arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="soundex.md" %}
[soundex.md](soundex.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the Soundex string. This function calculates the Soundex key for a string, allowing comparison of words that sound similar.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sounds-like.md" %}
[sounds-like.md](sounds-like.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare strings by sound. This operator tests if two strings have the same Soundex value, useful for fuzzy matching.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="space.md" %}
[space.md](space.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a string of spaces. This function returns a string consisting of a specified number of space characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="strcmp.md" %}
[strcmp.md](strcmp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare two strings. This function returns 0 if strings are equal, -1 if the first is smaller, and 1 if the first is larger.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="substr.md" %}
[substr.md](substr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SUBSTR() is a synonym for SUBSTRING(), returning a substring from a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="substring.md" %}
[substring.md](substring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete SUBSTRING() reference: syntax forms (pos,len, FROM/FOR), negative position from end, NULL handling, and Oracle sql_mode position 0 behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="substring_index.md" %}
[substring_index.md](substring_index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete SUBSTRING_INDEX() reference: SUBSTRING_INDEX(str,delim,count) syntax, positive/negative count, case-sensitive delimiter, NULL rules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_base64.md" %}
[to_base64.md](to_base64.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Encode a string to base-64. This function converts a string argument to its base-64 encoded form.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_char.md" %}
[to_char.md](to_char.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert to string. This function converts a value (often date/time) to a string, potentially using a format mask.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="trim.md" %}
[trim.md](trim.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove spaces from both ends. This function removes leading and trailing whitespace (or other specified characters) from a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="trim_oracle.md" %}
[trim_oracle.md](trim_oracle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Oracle-compatible TRIM function. This version of TRIM provides compatibility with Oracle's syntax for removing characters from a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="type-conversion.md" %}
[type-conversion.md](type-conversion.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand Type Conversion in MariaDB. Learn the rules for implicit conversion during comparisons and arithmetic, and how to use CAST for predictable results.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ucase.md" %}
[ucase.md](ucase.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for UPPER(). Converts a string to uppercase characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="unhex.md" %}
[unhex.md](unhex.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert hexadecimal to string. This function interprets pairs of hexadecimal digits as numbers and converts them to the characters they represent.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="updatexml.md" %}
[updatexml.md](updatexml.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replace a portion of XML. This function replaces a section of XML markup matching an XPath expression with a new XML fragment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="upper.md" %}
[upper.md](upper.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a string to uppercase. This function returns the string with all characters converted to uppercase.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="weight_string.md" %}
[weight_string.md](weight_string.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the weight string. This function returns the binary string that represents the sorting and comparison value of the input string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="regular-expressions-functions/" %}
[regular-expressions-functions](regular-expressions-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about regular expression functions in MariaDB Server. This section details SQL functions for powerful pattern matching and manipulation of string data using regular expressions.
{% endcolumn %}
{% endcolumns %}
