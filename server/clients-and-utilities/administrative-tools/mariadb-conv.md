---
description: >-
  mariadb-conv is a character set conversion utility for MariaDB, available
  from MariaDB 10.5.
---

# mariadb-conv

{% hint style="info" %}
This tool is available from MariaDB 10.5.
{% endhint %}

`mariadb-conv` is a character set conversion utility for MariaDB.

## Usage

```bash
mariadb-conv [OPTION...] [FILE...]
```

## Options

`mariadb-conv` supports the following options:

| Option           | Description                                   |
| ---------------- | --------------------------------------------- |
| -f, --from=name  | Specifies the encoding of the input.          |
| -t, --to=name    | Specifies the encoding of the output.         |
| -c, --continue   | Silently ignore conversion errors.            |
| --delimiter=name | Treat the specified characters as delimiters. |

By default, `mariadb-conv` exits whenever it encounters any conversion problems, like

* the input byte sequence is not valid in the source character set;
* the character cannot be converted to the target character set.

The `-c` option makes `mariadb-conv` ignore such errors and use the question mark (`?`) to replace bytes in bad input sequences, or unconvertible characters.

The `--delimiter=...` option makes `mariadb-conv` treat the specified characters as delimiters rather than data to convert, so the input is treated as a combination of

* data chunks, which are converted according to the `-f` and `-t` options;
* delimiters, which are not converted and are copied from the input to the output as is.

## Examples

Convert the file `file.latin1.txt` from `latin1` to `utf8` :

```bash
mariadb-conv -f latin1 -t utf8 file.latin1.txt
```

Convert the file `file.latin1.txt` from `latin1` to `utf8`, reading the input data from `stdin`:

```bash
mariadb-conv -f latin1 -t utf8 < file.latin1.txt
```

Using `mariadb-conv` in a pipe:

```bash
echo test | ./mariadb-conv -f utf8 -t ucs2 >file.ucs2.txt
```

As a side effect, `mariadb-conv` can be used to list MariaDB data directories in a human readable form. Suppose you create the following tables:

```sql
SET NAMES utf8;
CREATE OR REPLACE TABLE t1 (a INT);
CREATE OR REPLACE TABLE ß (a INT);
CREATE OR REPLACE TABLE абв (a INT);
CREATE OR REPLACE TABLE 桌子 (a INT);
```

This statement creates the following files in the MariaDB data directory:

```
@1j.frm
@1j.ibd
@684c@5b50.frm
@684c@5b50.ibd
@g0@h0@i0.frm
@g0@h0@i0.ibd
t1.frm
t1.ibd
```

It's not precisely clear which file stores which table, because MariaDB uses a special table-name-to-file-name encoding.

This command on Linux (assuming an utf-8 console) can print the table list in a readable way:

```bash
ls | mariadb-conv -f filename -t utf8 --delimiter=".\n"

ß.frm
ß.ibd
桌子.frm
桌子.ibd
абв.frm
абв.ibd
t1.frm
t1.ibd
```

{% hint style="info" %}
The `--delimiter=".\n"` option is needed to make `mariadb-conv` treat the dot character (delimiting the encoded table name from the file extension) and the newline character (delimiting separate lines) as delimiters, rather than as the data to convert (otherwise the conversion would fail).
{% endhint %}

Windows users can use the following command to list the data directory in the ANSI text console:

```bash
dir /b | mariadb-conv -c -f filename -t cp850 --delimiter=".\r\n"
```

Note:

* The `-t` options assume a Western machine.
* The `-c` option is needed to ignore conversion errors for Cyrillic and CJK characters.
* `--delimiter=` additionally needs the carriage return character.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
