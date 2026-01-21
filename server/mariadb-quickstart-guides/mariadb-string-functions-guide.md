---
description: >-
  This guide goes through several built-in string functions in MariaDB, grouping
  them by similar features, and providing examples of how they might be used.
---

# MariaDB String Functions Guide

This guide explores a variety of MariaDB's built-in string functions essential for effective data manipulation. Learn how to format text for display, extract specific substrings, replace content, and utilize various expression aids to enhance your string operations in SQL queries.

### Formatting Strings

Several functions are available for formatting text and numbers for display or processing.

**Concatenating Strings:**

*   `CONCAT(str1, str2, ...)`: Joins two or more strings together.

    SQL

    ```sql
    SELECT CONCAT(name_first, ' ', name_last) AS Name FROM contacts;
    ```

    This displays a full name by combining `name_first`, a space, and `name_last`.
*   `CONCAT_WS(separator, str1, str2, ...)`: Joins strings with a specified separator between each.

    SQL

    ```sql
    SELECT CONCAT_WS('|', col1, col2, col3) FROM table1;
    ```

    This creates a pipe-delimited string from `col1`, `col2`, and `col3`.

**Formatting Numbers:**

*   `FORMAT(number, decimal_places)`: Formats a number with commas every three digits and a specified number of decimal places.SQL

    ```sql
    SELECT CONCAT('$', FORMAT(col5, 2)) AS Price FROM table3;
    ```

    This prepends a dollar sign to a number formatted with commas and two decimal places (e.g., `$100,000.00`).

**Changing Case:**

* `UCASE(str)` or `UPPER(str)`: Converts a string to all upper-case letters.
*   `LCASE(str)` or `LOWER(str)`: Converts a string to all lower-case letters.SQL

    ```sql
    SELECT UCASE(col1) AS Upper_Col1, LCASE(col2) AS Lower_Col2 FROM table4;
    ```

**Padding Strings:**

* `LPAD(str, len, padstr)`: Left-pads `str` with `padstr` until it is `len` characters long.
*   `RPAD(str, len, padstr)`: Right-pads `str` with `padstr` until it is `len` characters long.SQL

    ```sql
    SELECT RPAD(part_nbr, 8, '.') AS 'Part Nbr.', LPAD(description, 15, '_') AS Description FROM catalog;
    ```

    Example: `RPAD('H200', 8, '.')` might produce `H200....`. `LPAD('hinge', 15, '_')` might produce `__________hinge`.

**Trimming Strings:**

* `LTRIM(str)`: Removes leading spaces.
* `RTRIM(str)`: Removes trailing spaces.
*   `TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)`: Removes leading, trailing, or both occurrences of `remstr` (or spaces if `remstr` is not given). `BOTH` is the default if no specifier is given before `remstr`. If only `str` is provided, trims leading and trailing spaces.

    ```sql
    SELECT
        TRIM(LEADING '.' FROM col1) AS Trimmed_Leading_Dots,
        TRIM(TRAILING FROM col2) AS Trimmed_Trailing_Spaces, -- Trims spaces
        TRIM(BOTH '_' FROM col3) AS Trimmed_Both_Underscores,
        TRIM(col4) AS Trimmed_Spaces -- Trims leading and trailing spaces
    FROM table5;
    ```

### Extracting Substrings

These functions help extract specific parts of a string.

* `LEFT(str, len)`: Returns the leftmost `len` characters from `str`.
*   `RIGHT(str, len)`: Returns the rightmost `len` characters from `str`.

    ```sql
    SELECT LEFT(telephone, 3) AS area_code, RIGHT(telephone, 7) AS tel_nbr
    FROM contacts
    ORDER BY area_code;
    ```

    This extracts the first 3 characters as `area_code` and the last 7 as `tel_nbr`.
*   `SUBSTRING(str, pos, [len])` or `MID(str, pos, [len])`: Returns a substring `len` characters long from `str`, starting at position `pos`. `MID()` is a synonym for `SUBSTRING()`. If `len` is omitted, returns the rest of the string from `pos`.

    ```sql
    SELECT CONCAT('(', LEFT(telephone, 3), ') ',
                  SUBSTRING(telephone, 4, 3), '-',
                  MID(telephone, 7)) AS 'Telephone Number'
    FROM contacts
    ORDER BY LEFT(telephone, 3);
    ```

    This formats a 10-digit phone number like `(504) 555-1234`.

### Manipulating Strings

Functions for changing or generating strings.

*   `REPLACE(str, from_str, to_str)`: Replaces all occurrences of `from_str` within `str` with `to_str`.

    ```sql
    SELECT CONCAT(REPLACE(title, 'Mrs.', 'Ms.'), ' ', name_first, ' ', name_last) AS Name
    FROM contacts;
    ```

    This replaces "Mrs." with "Ms." in the `title` column.
* `INSERT(str, pos, len, newstr)`: Replaces the substring in `str` starting at `pos` and `len` characters long with `newstr`. If `len` is 0, `newstr` is inserted at `pos` without overwriting.
*   `LOCATE(substr, str, [pos])`: Returns the starting position of the first occurrence of `substr` within `str`. An optional `pos` specifies where to start searching. Returns 0 if `substr` is not found.

    ```sql
    -- Example: Change 'Mrs.' to 'Ms.' where title is embedded in a 'name' column
    SELECT INSERT(name, LOCATE('Mrs.', name), LENGTH('Mrs.'), 'Ms.')
    FROM contacts
    WHERE name LIKE '%Mrs.%';
    ```

    This finds 'Mrs.' in the `name` string, and replaces it with 'Ms.'. `LENGTH('Mrs.')` (which is 4) is used for `len`. If `LOCATE()` returns 0, `INSERT()` with a position of 0 typically returns the original string unchanged.
*   `REVERSE(str)`: Reverses the characters in `str`.

    ```sql
    SELECT REVERSE('MariaDB'); -- Output: BDeiraM
    ```
*   `REPEAT(str, count)`: Repeats `str` `count` times.

    ```sql
    SELECT REPEAT('Ha', 3); -- Output: HaHaHa
    ```

### String Expression Aids

Functions that provide information about strings or assist in specific comparisons/conversions.

*   `CHAR_LENGTH(str)` or `CHARACTER_LENGTH(str)`: Returns the length of `str` in characters.

    ```sql
    SELECT COUNT(school_id) AS 'Number of Students'
    FROM table8
    WHERE CHAR_LENGTH(school_id) = 8;
    ```

    This counts rows where `school_id` has exactly 8 characters.
* `INET_ATON(ip_address_str)`: Converts an IPv4 address string (e.g., '10.0.1.1') into a numeric representation suitable for numeric sorting.
*   INET\_NTOA(numeric\_ip\_representation): Converts the numeric representation back to an IPv4 address string.

    To correctly sort IP addresses numerically instead of lexically:

    ```sql
    SELECT ip_address
    FROM computers
    WHERE server = 'Y'
    ORDER BY INET_ATON(ip_address)
    LIMIT 3;
    ```

    Lexical sort of 10.0.1.1, 10.0.11.1, 10.0.2.1 might be 10.0.1.1, 10.0.11.1, 10.0.2.1.

    Numeric sort (using INET\_ATON) would correctly be 10.0.1.1, 10.0.2.1, 10.0.11.1.
*   `STRCMP(str1, str2)`: Performs a case-sensitive comparison of `str1` and `str2`.

    * Returns `0` if strings are identical.
    * Returns `-1` if `str1` is alphabetically before `str2`.
    * Returns `1` if `str1` is alphabetically after `str2`.

    ```sql
    SELECT col1, col2
    FROM table6
    WHERE STRCMP(col3, 'text') = 0; -- Finds exact case-sensitive match for 'text'
    ```
*   `SUBSTRING_INDEX(str, delim, count)`: Returns a substring from `str` before or after `count` occurrences of the delimiter `delim`.

    * If `count` is positive, returns everything to the left of the `count`-th delimiter (from the left).
    * If `count` is negative, returns everything to the right of the `abs(count)`-th delimiter (from the right).

    ```sql
    -- Get the first two elements from a pipe-delimited string
    SELECT SUBSTRING_INDEX('elem1|elem2|elem3|elem4', '|', 2); -- Output: elem1|elem2

    -- Get the last two elements
    SELECT SUBSTRING_INDEX('elem1|elem2|elem3|elem4', '|', -2); -- Output: elem3|elem4
    ```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
