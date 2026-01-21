---
description: >-
  Get an overview of regex usage. This page introduces the pattern matching
  capabilities and common metacharacters used in MariaDB regular expressions.
---

# Regular Expressions Overview

Regular Expressions allow MariaDB to perform complex pattern matching on a string. In many cases, the simple pattern matching provided by [LIKE](../like.md) is sufficient. `LIKE` performs two kinds of matches:

* `_` - the underscore, matching a single character
* `%` - the percentage sign, matching any number of characters.

In other cases you may need more control over the returned matches, and will need to use regular expressions.

Regular expression matches are performed with the [REGEXP](regexp.md) function. `RLIKE` is a synonym for `REGEXP`.

Comparisons are performed on the byte value, so characters that are treated as equivalent by a collation, but do not have the same byte-value, such as accented characters, could evaluate as unequal.

Without any special characters, a regular expression match is true if the characters match. The match is case-insensitive, except in the case of BINARY strings.

```sql
SELECT 'Maria' REGEXP 'Maria';
+------------------------+
| 'Maria' REGEXP 'Maria' |
+------------------------+
|                      1 |
+------------------------+

SELECT 'Maria' REGEXP 'maria';
+------------------------+
| 'Maria' REGEXP 'maria' |
+------------------------+
|                      1 |
+------------------------+

SELECT BINARY 'Maria' REGEXP 'maria';
+-------------------------------+
| BINARY 'Maria' REGEXP 'maria' |
+-------------------------------+
|                             0 |
+-------------------------------+
```

Note that the word being matched must match the whole pattern:

```sql
SELECT 'Maria' REGEXP 'Mari';
+-----------------------+
| 'Maria' REGEXP 'Mari' |
+-----------------------+
|                     1 |
+-----------------------+

SELECT 'Mari' REGEXP 'Maria';
+-----------------------+
| 'Mari' REGEXP 'Maria' |
+-----------------------+
|                     0 |
+-----------------------+
```

The first returns true because the pattern "Mari" exists in the expression "Maria". When the order is reversed, the result is false, as the pattern "Maria" does not exist in the expression "Mari"

A match can be performed against more than one word with the `|` character. For example:

```sql
SELECT 'Maria' REGEXP 'Monty|Maria';
+------------------------------+
| 'Maria' REGEXP 'Monty|Maria' |
+------------------------------+
|                            1 |
+------------------------------+
```

## Special Characters

The above examples introduce the syntax, but are not very useful on their own. It's the special characters that give regular expressions their power.

#### ^

`^` matches the beginning of a string (inside square brackets it can also mean `NOT` - see below):

```sql
SELECT 'Maria' REGEXP '^Ma';
+----------------------+
| 'Maria' REGEXP '^Ma' |
+----------------------+
|                    1 |
+----------------------+
```

#### $

`$` matches the end of a string:

```sql
SELECT 'Maria' REGEXP 'ia$';
+----------------------+
| 'Maria' REGEXP 'ia$' |
+----------------------+
|                    1 |
+----------------------+
```

#### .

`.` matches any single character:

```sql
SELECT 'Maria' REGEXP 'Ma.ia';
+------------------------+
| 'Maria' REGEXP 'Ma.ia' |
+------------------------+
|                      1 |
+------------------------+

SELECT 'Maria' REGEXP 'Ma..ia';
+-------------------------+
| 'Maria' REGEXP 'Ma..ia' |
+-------------------------+
|                       0 |
+-------------------------+
```

#### \*

`x*` matches zero or more of a character `x`. In the examples below, it's the `r` character.

```sql
SELECT 'Maria' REGEXP 'Mar*ia';
+-------------------------+
| 'Maria' REGEXP 'Mar*ia' |
+-------------------------+
|                       1 |
+-------------------------+

SELECT 'Maia' REGEXP 'Mar*ia';
+------------------------+
| 'Maia' REGEXP 'Mar*ia' |
+------------------------+
|                      1 |
+------------------------+

SELECT 'Marrria' REGEXP 'Mar*ia';
+---------------------------+
| 'Marrria' REGEXP 'Mar*ia' |
+---------------------------+
|                         1 |
+---------------------------+
```

#### +

`x+` matches one or more of a character `x`. In the examples below, it's the `r` character.

```sql
SELECT 'Maria' REGEXP 'Mar+ia';
+-------------------------+
| 'Maria' REGEXP 'Mar+ia' |
+-------------------------+
|                       1 |
+-------------------------+

SELECT 'Maia' REGEXP 'Mar+ia';
+------------------------+
| 'Maia' REGEXP 'Mar+ia' |
+------------------------+
|                      0 |
+------------------------+

SELECT 'Marrria' REGEXP 'Mar+ia';
+---------------------------+
| 'Marrria' REGEXP 'Mar+ia' |
+---------------------------+
|                         1 |
+---------------------------+
```

#### ?

`x?` matches zero or one of a character `x`. In the examples below, it's the `r` character.

```sql
SELECT 'Maria' REGEXP 'Mar?ia';
+-------------------------+
| 'Maria' REGEXP 'Mar?ia' |
+-------------------------+
|                       1 |
+-------------------------+

SELECT 'Maia' REGEXP 'Mar?ia';
+------------------------+
| 'Maia' REGEXP 'Mar?ia' |
+------------------------+
|                      1 |
+------------------------+

SELECT 'Marrria' REGEXP 'Mar?ia';
+---------------------------+
| 'Marrria' REGEXP 'Mar?ia' |
+---------------------------+
|                         0 |
+---------------------------+
```

#### ()

`(xyz)` - combine a sequence, for example `(xyz)+` or `(xyz)*`

```sql
SELECT 'Maria' REGEXP '(ari)+';
+-------------------------+
| 'Maria' REGEXP '(ari)+' |
+-------------------------+
|                       1 |
+-------------------------+
```

#### {}

`x{n}` and `x{m,n}`\
This notation is used to match many instances of the `x`. In the case of `x{n}` the match must be exactly that many times. In the case of `x{m,n}`, the match can occur from `m` to `n` times. For example, to match zero or one instance of the string `ari` (which is identical to `(ari)?`), the following can be used:

```sql
SELECT 'Maria' REGEXP '(ari){0,1}';
+-----------------------------+
| 'Maria' REGEXP '(ari){0,1}' |
+-----------------------------+
|                           1 |
+-----------------------------+
```

#### \[]

`[xy]` groups characters for matching purposes. For example, to match either the `p` or the `r` character:

```sql
SELECT 'Maria' REGEXP 'Ma[pr]ia';
+---------------------------+
| 'Maria' REGEXP 'Ma[pr]ia' |
+---------------------------+
|                         1 |
+---------------------------+
```

The square brackets also permit a range match, for example, to match any character from a-z, `[a-z]` is used. Numeric ranges are also permitted.

```sql
SELECT 'Maria' REGEXP 'Ma[a-z]ia';
+----------------------------+
| 'Maria' REGEXP 'Ma[a-z]ia' |
+----------------------------+
|                          1 |
+----------------------------+
```

The following does not match, as `r` falls outside of the range `a-p`.

```sql
SELECT 'Maria' REGEXP 'Ma[a-p]ia';
+----------------------------+
| 'Maria' REGEXP 'Ma[a-p]ia' |
+----------------------------+
|                          0 |
+----------------------------+
```

**^**

The `^` character means does `NOT` match, for example:

```sql
SELECT 'Maria' REGEXP 'Ma[^p]ia';
+---------------------------+
| 'Maria' REGEXP 'Ma[^p]ia' |
+---------------------------+
|                         1 |
+---------------------------+

SELECT 'Maria' REGEXP 'Ma[^r]ia';
+---------------------------+
| 'Maria' REGEXP 'Ma[^r]ia' |
+---------------------------+
|                         0 |
+---------------------------+
```

The `[` and `]` characters on their own can be literally matched inside a `[]` block, without escaping, as long as they immediately match the opening bracket:

```sql
SELECT '[Maria' REGEXP '[[]';
+-----------------------+
| '[Maria' REGEXP '[[]' |
+-----------------------+
|                     1 |
+-----------------------+

SELECT '[Maria' REGEXP '[]]';
+-----------------------+
| '[Maria' REGEXP '[]]' |
+-----------------------+
|                     0 |
+-----------------------+

SELECT ']Maria' REGEXP '[]]';
+-----------------------+
| ']Maria' REGEXP '[]]' |
+-----------------------+
|                     1 |
+-----------------------+

SELECT ']Maria' REGEXP '[]a]';
+------------------------+
| ']Maria' REGEXP '[]a]' |
+------------------------+
|                      1 |
+------------------------+
```

Incorrect order, so no match:

```sql
SELECT ']Maria' REGEXP '[a]]';
+------------------------+
| ']Maria' REGEXP '[a]]' |
+------------------------+
|                      0 |
+------------------------+
```

The `-` character can also be matched in the same way:

```sql
SELECT '-Maria' REGEXP '[1-10]';
+--------------------------+
| '-Maria' REGEXP '[1-10]' |
+--------------------------+
|                        0 |
+--------------------------+

SELECT '-Maria' REGEXP '[-1-10]';
+---------------------------+
| '-Maria' REGEXP '[-1-10]' |
+---------------------------+
|                         1 |
+---------------------------+
```

#### Word boundaries

The :<: and :>: patterns match the beginning and the end of a word respectively. For example:

```sql
SELECT 'How do I upgrade MariaDB?' REGEXP '[[:<:]]MariaDB[[:>:]]';
+------------------------------------------------------------+
| 'How do I upgrade MariaDB?' REGEXP '[[:<:]]MariaDB[[:>:]]' |
+------------------------------------------------------------+
|                                                          1 |
+------------------------------------------------------------+

SELECT 'How do I upgrade MariaDB?' REGEXP '[[:<:]]Maria[[:>:]]';
+----------------------------------------------------------+
| 'How do I upgrade MariaDB?' REGEXP '[[:<:]]Maria[[:>:]]' |
+----------------------------------------------------------+
|                                                        0 |
+----------------------------------------------------------+
```

#### Character Classes

There are a number of shortcuts to match particular preset character classes. These are matched with the `[:character_class:]` pattern (inside a `[]` set). The following character classes exist:

| Character Class | Description                              |
| --------------- | ---------------------------------------- |
| alnum           | Alphanumeric                             |
| alpha           | Alphabetic                               |
| blank           | Whitespace                               |
| cntrl           | Control characters                       |
| digit           | Digits                                   |
| graph           | Graphic characters                       |
| lower           | Lowercase alphabetic                     |
| print           | Graphic or space characters              |
| punct           | Punctuation                              |
| space           | Space, tab, newline, and carriage return |
| upper           | Uppercase alphabetic                     |
| xdigit          | Hexadecimal digit                        |

For example:

```sql
SELECT 'Maria' REGEXP 'Mar[[:alnum:]]*';
+--------------------------------+
| 'Maria' REGEXP 'Mar[:alnum:]*' |
+--------------------------------+
|                              1 |
+--------------------------------+
```

Remember that matches are by default case-insensitive, unless a binary string is used, so the following example, specifically looking for an uppercase, counter-intuitively matches a lowercase character:

```sql
SELECT 'Mari' REGEXP 'Mar[[:upper:]]+';
+---------------------------------+
| 'Mari' REGEXP 'Mar[[:upper:]]+' |
+---------------------------------+
|                               1 |
+---------------------------------+

SELECT BINARY 'Mari' REGEXP 'Mar[[:upper:]]+';
+----------------------------------------+
| BINARY 'Mari' REGEXP 'Mar[[:upper:]]+' |
+----------------------------------------+
|                                      0 |
+----------------------------------------+
```

#### Character Names

There are also number of shortcuts to match particular preset character names. These are matched with the `[.character.]` pattern (inside a `[]` set). The following character classes exist:

| Name                 | Character |
| -------------------- | --------- |
| NUL                  | 0         |
| SOH                  | 001       |
| STX                  | 002       |
| ETX                  | 003       |
| EOT                  | 004       |
| ENQ                  | 005       |
| ACK                  | 006       |
| BEL                  | 007       |
| alert                | 007       |
| BS                   | 010       |
| backspace            | '\b'      |
| HT                   | 011       |
| tab                  | '\t'      |
| LF                   | 012       |
| newline              | '\n'      |
| VT                   | 013       |
| vertical-tab         | '\v'      |
| FF                   | 014       |
| form-feed            | '\f'      |
| CR                   | 015       |
| carriage-return      | '\r'      |
| SO                   | 016       |
| SI                   | 017       |
| DLE                  | 020       |
| DC1                  | 021       |
| DC2                  | 022       |
| DC3                  | 023       |
| DC4                  | 024       |
| NAK                  | 025       |
| SYN                  | 026       |
| ETB                  | 027       |
| CAN                  | 030       |
| EM                   | 031       |
| SUB                  | 032       |
| ESC                  | 033       |
| IS4                  | 034       |
| FS                   | 034       |
| IS3                  | 035       |
| GS                   | 035       |
| IS2                  | 036       |
| RS                   | 036       |
| IS1                  | 037       |
| US                   | 037       |
| space                | ' '       |
| exclamation-mark     | '!'       |
| quotation-mark       | '"'       |
| number-sign          | '#'       |
| dollar-sign          | '$'       |
| percent-sign         | '%'       |
| ampersand            | '&'       |
| apostrophe           | '''       |
| left-parenthesis     | '('       |
| right-parenthesis    | ')'       |
| asterisk             | '\*'      |
| plus-sign            | '+'       |
| comma                | ','       |
| hyphen               | '-'       |
| hyphen-minus         | '-'       |
| period               | '.'       |
| full-stop            | '.'       |
| slash                | '/'       |
| solidus              | '/'       |
| zero                 | '0'       |
| one                  | '1'       |
| two                  | '2'       |
| three                | '3'       |
| four                 | '4'       |
| five                 | '5'       |
| six                  | '6'       |
| seven                | '7'       |
| eight                | '8'       |
| nine                 | '9'       |
| colon                | ':'       |
| semicolon            | ';'       |
| less-than-sign       | '<'       |
| equals-sign          | '='       |
| greater-than-sign    | '>'       |
| question-mark        | '?'       |
| commercial-at        | '@'       |
| left-square-bracket  | '\['      |
| backslash            | ''        |
| reverse-solidus      | ''        |
| right-square-bracket | ']'       |
| circumflex           | '^'       |
| circumflex-accent    | '^'       |
| underscore           | '\_'      |
| low-line             | '\_'      |
| grave-accent         | '\`'      |
| left-brace           | '{'       |
| left-curly-bracket   | '{'       |
| vertical-line        | '         |
| right-brace          | '}'       |
| right-curly-bracket  | '}'       |
| tilde                | ''        |
| DEL                  | 177       |

For example:

```sql
SELECT '|' REGEXP '[[.vertical-line.]]';
+----------------------------------+
| '|' REGEXP '[[.vertical-line.]]' |
+----------------------------------+
|                                1 |
+----------------------------------+
```

### Combining

The true power of regular expressions is unleashed when the above is combined, to form more complex examples. Regular expression's reputation for complexity stems from the seeming complexity of multiple combined regular expressions, when in reality, it's simply a matter of understanding the characters and how they apply:

The first example fails to match, as while the `Ma` matches, either `i` or `r` only matches once before the `ia` characters at the end.

```sql
SELECT 'Maria' REGEXP 'Ma[ir]{2}ia';
+------------------------------+
| 'Maria' REGEXP 'Ma[ir]{2}ia' |
+------------------------------+
|                            0 |
+------------------------------+
```

This example matches, as either `i` or `r` match exactly twice after the `Ma`, in this case one `r` and one `i`.

```sql
SELECT 'Maria' REGEXP 'Ma[ir]{2}';
+----------------------------+
| 'Maria' REGEXP 'Ma[ir]{2}' |
+----------------------------+
|                          1 |
+----------------------------+
```

### Escaping

With the large number of special characters, care needs to be taken to properly escape characters. Two backslash characters, \`\` (one for the MariaDB parser, one for the regex library), are required to properly escape a character. For example:

To match the literal `(Ma`:

```sql
SELECT '(Maria)' REGEXP '(Ma';
ERROR 1139 (42000): Got error 'parentheses not balanced' from regexp

SELECT '(Maria)' REGEXP '\(Ma';
ERROR 1139 (42000): Got error 'parentheses not balanced' from regexp

SELECT '(Maria)' REGEXP '\\(Ma';
+--------------------------+
| '(Maria)' REGEXP '\\(Ma' |
+--------------------------+
|                        1 |
+--------------------------+
```

To match `r+`: The first two examples are incorrect, as they match `r` one or more times, not `r+`:

```sql
SELECT 'Mar+ia' REGEXP 'r+';
+----------------------+
| 'Mar+ia' REGEXP 'r+' |
+----------------------+
|                    1 |
+----------------------+

SELECT 'Maria' REGEXP 'r+';
+---------------------+
| 'Maria' REGEXP 'r+' |
+---------------------+
|                   1 |
+---------------------+

SELECT 'Maria' REGEXP 'r\\+';
+-----------------------+
| 'Maria' REGEXP 'r\\+' |
+-----------------------+
|                     0 |
+-----------------------+

SELECT 'Maria' REGEXP 'r+';
+---------------------+
| 'Maria' REGEXP 'r+' |
+---------------------+
|                   1 |
+---------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
