---
name: mariadb-string-functions
description: "MariaDB string functions — extraction (SUBSTRING/SUBSTR, LEFT, RIGHT, MID, SUBSTRING_INDEX); length in bytes (LENGTH/OCTET_LENGTH/LENGTHB) vs characters (CHAR_LENGTH/CHARACTER_LENGTH); search (LOCATE, INSTR, POSITION, FIND_IN_SET, FIELD); concatenation (CONCAT, CONCAT_WS); modification (REPLACE, INSERT, REVERSE, REPEAT, SPACE, LPAD/RPAD, TRIM/LTRIM/RTRIM); case (LOWER/UPPER); PCRE2 regular expressions (REGEXP/RLIKE, REGEXP_REPLACE, REGEXP_INSTR, REGEXP_SUBSTR); formatting (FORMAT, SFORMAT); encoding (HEX/UNHEX, TO_BASE64/FROM_BASE64, ASCII, CHAR, ORD); plus the LIKE, REGEXP, SOUNDS LIKE, and BINARY operators. Use when writing SQL that searches, slices, pads, concatenates, case-folds, or pattern-matches string data in MariaDB."
---

# MariaDB String Functions

*Last updated: 2026-06-24*

Catalog of every built-in string function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at <https://mariadb.com/docs/server/reference/sql-functions/string-functions> (PCRE2 regex syntax: <https://mariadb.com/docs/server/reference/sql-functions/string-functions/regular-expressions-functions>).

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `LENGTH(str)` to count characters | `LENGTH()` returns **bytes**, not characters. Under the default `utf8mb4`, a 5-emoji string returns 20, not 5. Use `CHAR_LENGTH()` / `CHARACTER_LENGTH()` for a character count; `OCTET_LENGTH()` / `LENGTHB()` are the explicit byte forms |
| `CONCAT(a, b, c)` and expecting `NULL` arguments to be skipped | `CONCAT()` returns `NULL` if **any** argument is `NULL` — one `NULL` wipes the whole result. Use `CONCAT_WS(sep, …)` (skips `NULL`s), or wrap args in `IFNULL(x, '')` |
| `SUBSTRING(str, 0, n)` to take from the start | String positions are **1-indexed**; `pos = 0` returns an **empty string**. Use `SUBSTRING(str, 1, n)`. A negative `pos` counts from the end (`SUBSTRING(str, -4)` → last 4 chars) |
| `LOCATE(str, substr)` / `INSTR(substr, str)` — guessing the argument order | The two take **reversed** orders: `LOCATE(substr, str)` (needle first) but `INSTR(str, substr)` (haystack first). `POSITION(substr IN str)` is a synonym for `LOCATE`. All are 1-based, `0` if not found |
| `str REGEXP '…'` expecting POSIX ERE semantics | MariaDB's `REGEXP`/`RLIKE` and the `REGEXP_*` functions use **PCRE2** — inline flags `(?i)`/`(?m)`, lazy quantifiers `.+?`, backreferences. Treat the dialect as PCRE, not classic POSIX ERE |
| Case-sensitivity of `LIKE`, `REGEXP`, `=` is fixed | It depends on the operand **collation**. With the default `utf8mb4_uca1400_ai_ci` they are **case-insensitive**. Force case-sensitive matching with a `_bin`/`_cs` collation (`COLLATE utf8mb4_bin`), the `BINARY` operator, or a PCRE `(?-i)` flag. (`REPLACE()` is always case-sensitive regardless of collation) |
| `REGEXP_REPLACE(…)` with `$1`-style replacement backreferences | Replacement backreferences use `\N` (`\\1`…`\\9` in a SQL string literal), not `$1`. Inline flags like `(?i)` go inside the **pattern** |
| `TRIM(str)` to strip an arbitrary character | Bare `TRIM` removes **spaces** from both ends. Use `TRIM(LEADING | TRAILING | BOTH remstr FROM str)` for other characters or one side (`remstr` is a full string, not a char set). `LTRIM`/`RTRIM` are space-only |
| `a || b` for string concatenation | By default `||` is **logical OR**, not concatenation — use `CONCAT()`. `||` concatenates only when `sql_mode` includes `PIPES_AS_CONCAT` (or `ORACLE`) |
| `LPAD(str, len)` / `RPAD(str, len)` only lengthens | If `str` is **longer** than `len`, the result is **truncated** to `len`. `len` counts characters; the pad string defaults to a single space |
| `'a' = 'a '` is false (trailing spaces significant) | `CHAR`/`VARCHAR` comparison **ignores trailing spaces** by default, so `'a' = 'a '` is true. Use the `BINARY` operator (or a `NO PAD` collation) to make trailing spaces and case significant |
| `printf`-style `%s` formatting in SQL | Use `SFORMAT(fmt, …)` for Python/fmtlib-style `{}` placeholders *(since 10.7)*. Note it has no native temporal/decimal handling (`TIME`→string, `DECIMAL`→real) |

## Related operators

Pattern-matching and comparison are **operators**, not functions, so they aren't in the catalog below:

- **`LIKE` / `NOT LIKE`** — wildcard match (`%`, `_`) with an optional `ESCAPE` clause; collation-dependent case-sensitivity; index-usable when the pattern doesn't start with `%`/`_`.
- **`REGEXP` / `RLIKE` / `NOT REGEXP`** — PCRE2 pattern match returning 1/0/`NULL`; session `default_regex_flags` sets default modifiers.
- **`BINARY`** — forces a byte-wise (case- and trailing-space-sensitive) comparison; the canonical way to make a comparison case-sensitive.
- **`SOUNDS LIKE`** — shorthand for `SOUNDEX(a) = SOUNDEX(b)`.

To join multiple rows into one string, see `GROUP_CONCAT` in **`mariadb-aggregate-functions`**.

## Functions

Auto-generated from the canonical `server/reference/sql-functions/string-functions/` pages by `agent-skills/extractor/extract_function_category.py`; regenerate when the doc tree changes. Do not hand-edit between the markers.

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/string-functions -->
<!-- 58 functions, 8 pages skipped on extraction failure -->

### ASCII
`ASCII(str)`  
Returns the numeric ASCII value of the leftmost character of the string argument.

### BIN
`BIN(N)`  
Returns a string representation of the binary value of the given longlong (that is, BIGINT) number.

### BIT_LENGTH
`BIT_LENGTH(str)`  
Returns the length of the given string argument in bits.

### CAST
`CAST(expr AS type)`  
The `CAST()` function takes a value of one data type and produces a value of another data type, similar to the CONVERT() function.

### CHAR
`CHAR(N,... [USING charset_name])`  
`CHAR()` interprets each argument as an INT and returns a string consisting of the characters given by the code values of those integers.

### CHARACTER_LENGTH
`CHARACTER_LENGTH(str)`  
`CHARACTER_LENGTH()` is a synonym for CHAR_LENGTH().

### CHAR_LENGTH
`CHAR_LENGTH(str)`  
Returns the length of the given string argument, measured in characters.

### CHR
`CHR(N)`  
`CHR()` interprets each argument N as an integer and returns a VARCHAR(1) string consisting of the character given by the code values of the integer.

### CONCAT
`CONCAT(str1,str2,...)`  
Returns the string that results from concatenating the arguments.

### CONCAT_WS
`CONCAT_WS(separator,str1,str2,...)`  
`CONCAT_WS()` stands for Concatenate With Separator and is a special form of CONCAT().

### CONVERT
`CONVERT(expr,type), CONVERT(expr USING transcoding_name)`  
The `CONVERT()` and CAST() functions take a value of one type and produce a value of another type.

### ELT
`ELT(N, str1[, str2, str3,...])`  
Takes a numeric argument and a series of string arguments.

### EXPORT_SET
`EXPORT_SET(bits, on, off[, separator[, number_of_bits]])`  
Takes a minimum of three arguments.

### EXTRACTVALUE
`EXTRACTVALUE(xml_frag, xpath_expr)`  
The `EXTRACTVALUE()` function takes two string arguments: a fragment of XML markup and an XPath expression, (also known as a locator).

### FIELD
`FIELD(pattern, str1[,str2,...])`  
Returns the index position of the string or number matching the given pattern.

### FIND_IN_SET
`FIND_IN_SET(pattern, strlist)`  
Returns the index position where the given pattern occurs in a string list.

### FORMAT
`FORMAT(num, decimal_position[, locale])`  
Formats the given number for display as a string, adding separators to appropriate position and rounding the results to the given decimal position.

### FROM_BASE64
`FROM_BASE64(str)`  
Decodes the given base-64 encode string, returning the result as a binary string.

### HEX
`HEX(N_or_S)`  
If `N_or_S` is a number, returns a string representation of the hexadecimal value of `N`, where `N` is a `longlong` (BIGINT) number.

### INSERT
`INSERT(str,pos,len,newstr)`  
Returns the string `str`, with the substring beginning at position `pos` and `len` characters long replaced by the string `newstr`.

### INSTR
`INSTR(str,substr)`  
Returns the position of the first occurrence of substring _substr_ in string _str_.

### LCASE
`LCASE(str)`  
`LCASE()` is a synonym for LOWER().

### LEFT
`LEFT(str,len)`  
Returns the leftmost `len` characters from the string `str`, or `NULL` if any argument is `NULL`.

### LENGTH
`LENGTH(str)`  
Returns the length of the string `str`.

### LENGTHB
`LENGTHB(str)`  
`LENGTHB()` returns the length of the given string, in bytes.

### LIKE
`expr LIKE pat [ESCAPE 'escape_char']`  
Tests whether _expr_ matches the pattern _pat_.

### LOAD_FILE
`LOAD_FILE(file_name)`  
Reads the file and returns the file contents as a string.

### LOCATE
`LOCATE(substr,str), LOCATE(substr,str,pos)`  
The first syntax returns the position of the first occurrence of substring `substr` in string `str`.

### LOWER
`LOWER(str)`  
Returns the string `str` with all characters changed to lowercase according to the current character set mapping.

### LPAD
`LPAD(str, len [,padstr])`  
Returns the string `str`, left-padded with the string `padstr` to a length of `len` characters.

### LTRIM
`LTRIM(str)`  
Returns the string `str` with leading space characters removed.

### MAKE_SET
`MAKE_SET(bits,str1,str2,...)`  
Returns a set value (a string containing substrings separated by "," characters) consisting of the strings that have the corresponding bit in bits set.

### MID
`MID(str,pos,len)`  
MID(str,pos,len) is a synonym for SUBSTRING(str,pos,len)!

### NATURAL_SORT_KEY
`NATURAL_SORT_KEY(str)`  
The `NATURAL_SORT_KEY` function is used for sorting that is closer to natural sorting. *(since 10.7)*

### OCTET_LENGTH
`OCTET_LENGTH(str)`  
`OCTET_LENGTH()` returns the length of the given string, in octets (bytes).

### ORD
`ORD(str)`  
If the leftmost character of the string `str` is a multi-byte character, returns the code for that character, calculated from the numeric values of its constituent bytes using this formula:

### POSITION
`POSITION(substr IN str)`  
`POSITION(substr IN str)` is a synonym for LOCATE(substr,str).

### QUOTE
`QUOTE(str)`  
Quotes a string to produce a result that can be used as a properly escaped data value in an SQL statement.

### REPEAT
`REPEAT(str,count)`  
Returns a string consisting of the string `str` repeated `count` times.

### REPLACE
`REPLACE(str,from_str,to_str)`  
Returns the string `str` with all occurrences of the string `from_str` replaced by the string `to_str`.

### REVERSE
`REVERSE(str)`  
Returns the string `str` with the order of the characters reversed.

### RIGHT
`RIGHT(str,len)`  
Returns the rightmost _`len`_ characters from the string _`str`_, or `NULL` if any argument is `NULL`.

### RPAD
`RPAD(str, len [, padstr])`  
Returns the string `str`, right-padded with the string `padstr` to a length of `len` characters.

### RTRIM
`RTRIM(str)`  
Returns the string `str` with trailing space characters removed.

### SOUNDEX
`SOUNDEX(str)`  
Returns a soundex string from _`str`_.

### SPACE
`SPACE(N)`  
Returns a string consisting of _`N`_ space characters.

### STRCMP
`STRCMP(expr1,expr2)`  
`STRCMP()` returns `0` if the strings are the same, `-1` if the first argument is smaller than the second according to the current sort order, and `1` if the strings are otherwise not the same.

### SUBSTR
Alias for `SUBSTRING`.

### SUBSTRING
`SUBSTRING(str,pos),`  
The forms without a _`len`_ argument return a substring from string _`str`_ starting at position _`pos`_.

### SUBSTRING_INDEX
`SUBSTRING_INDEX(str,delim,count)`  
Returns the substring from string _`str`_ before count occurrences of the delimiter _`delim`_.

### TO_BASE64
`TO_BASE64(str)`  
Converts the string argument `str` to its base-64 encoded form, returning the result as a character string in the connection character set and collation.

### TO_CHAR
`TO_CHAR(expr[, fmt])`  
{% tabs %} {% tab title="Current" %} The `TO_CHAR` function converts an _expr_ of type date, datetime, time or timestamp to a string.

### TRIM
`TRIM_ORACLE([{BOTH | LEADING | TRAILING} [remstr] FROM] str), TRIM([remstr FROM] str)`  
Returns the string `str` with all `remstr` prefixes or suffixes removed.

### UCASE
`UCASE(str)`  
`UCASE()` is a synonym for UPPER().

### UNHEX
`UNHEX(str)`  
Performs the inverse operation of HEX(str).

### UPDATEXML
`UpdateXML(xml_target, xpath_expr, new_xml)`  
This function replaces a single portion of a given fragment of XML markup`xml_target` with a new XML fragment `new_xml`, and then returns the changed XML.

### UPPER
`UPPER(str)`  
Returns the string `str` with all characters changed to uppercase according to the current character set mapping.

### WEIGHT_STRING
`WEIGHT_STRING(str [AS {CHAR|BINARY}(N)] [LEVEL levels] [flags])`  
Returns a binary string representing the string's sorting and comparison value.
<!-- END GENERATED -->

## See Also

- **`mariadb-features`** (topical) — the `latin1` → `utf8mb4` default-charset (since 11.6) and `uca1400_ai_ci` default-collation (since 11.5) changes that drive every case-sensitivity row
- **`mysql-to-mariadb`** (topical) — the `||`-as-OR default and collation-alias behavior
- **`mariadb-aggregate-functions`** — `GROUP_CONCAT` for joining rows into a string
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/string-functions>
