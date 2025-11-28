# String Literals

Strings are sequences of characters and enclosed with quotes.

The syntax is:

```sql
[_charset_name]'string' [COLLATE collation_name]
```

For example:

```sql
'The MariaDB Foundation'
_utf8 'Foundation' COLLATE utf8_unicode_ci;
```

Strings can either be enclosed in single quotes or in double quotes (the same character must be used to both open and close the string).

The ANSI SQL-standard does not permit double quotes for enclosing strings, and although MariaDB does by default, if the MariaDB server has enabled the [ANSI\_QUOTES\_SQL](../../../server-management/variables-and-modes/sql_mode.md#ansi_quotes) [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md), double quotes will be treated as being used for [identifiers](identifier-names.md) instead of strings.

Strings that are next to each other are automatically concatenated. The following are equivalent:

```
'The ' 'MariaDB ' 'Foundation'
```

```
'The MariaDB Foundation'
```

The `\` (backslash character) is used to escape characters (unless the [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) hasn't been set to [NO\_BACKSLASH\_ESCAPES](../../../server-management/variables-and-modes/sql_mode.md#no_backslash_escapes)):

```
'MariaDB's new features'
```

That is not a valid string because of the single quote in the middle of the string, which is treated as if it closes the string, but is actually meant as part of the string, an apostrophe. The backslash character helps in situations like this:

```
'MariaDB\'s new features'
```

That is now a valid string, and if displayed, will appear without the backslash.

```sql
SELECT 'MariaDB\'s new features';
+------------------------+
| MariaDB's new features |
+------------------------+
| MariaDB's new features |
+------------------------+
```

Another way to escape the quoting character is repeating it twice:

```sql
SELECT 'I''m here', """Double""";
+----------+----------+
| I'm here | "Double" |
+----------+----------+
| I'm here | "Double" |
+----------+----------+
```

## Escape Sequences

There are other escape sequences:

| Escape sequence | Character                                           |
| --------------- | --------------------------------------------------- |
| \0              | ASCII NUL (0x00).                                   |
| '               | Single quote (“'”).                                 |
| "               | Double quote (“"”).                                 |
| \b              | Backspace.                                          |
|                 | Newline, or linefeed,.                              |
|                 | Carriage return.                                    |
|                 | Tab.                                                |
| \Z              | ASCII 26 (Control+Z). See note following the table. |
| \\              | Backslash (“\”).                                    |
| %               | “%” character. See note following the table.        |
| \_              | A “\_” character. See note following the table.     |

Escaping the `%` and `_` characters can be necessary when using the [LIKE](../../sql-functions/string-functions/like.md) operator, which treats them as special characters.

The ASCII 26 character (`\Z`) needs to be escaped when included in a batch file which needs to be executed in Windows. The reason is that ASCII 26, in Windows, is the end of file (EOF).

Backslash (`\`), if not used as an escape character, must always be escaped. When followed by a character that is not in the above table, backslashes will simply be ignored.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
