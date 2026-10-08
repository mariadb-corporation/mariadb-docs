---
description: >-
  The replace utility changes strings in place in files or on standard input.
---

# replace

## Description

The `replace` utility program changes strings in place in files or on the standard input. Invoke replace in one of the following ways:

```bash
shell> replace from to [from to] ... -- file_name [file_name] ...
shell> replace from to [from to] ... < file_name
```

`from` represents a string to look for, and `to` represents its replacement. There can be one or more pairs of strings.

A from-string can contain these special characters:

| Character | Description                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ^         | Match start of line.                                                                                                                                                                            |
| $         | Match end of line.                                                                                                                                                                              |
| \b        | Match space-character, start of line or end of line. For an end `\b` , the next replace starts looking at the end space character ( ). A `\b` alone in a string matches only a space character. |

Use the `--` option to indicate where the string-replacement list ends and the file names begin. Any file named on the command line is modified in place, so you may want to make a copy of the original before
converting it. `replace` prints a message indicating which of the input files it actually modifies.

If the `--` option is not given, `replace` reads standard input and writes to `stdout` (standard output).

`replace` uses a finite state machine to match longer strings first. It can be used to swap strings. For example, the following command swaps "a" and "b" in the given files, _file1_ _and file2_:

```bash
shell> replace a b b a -- file1 file2 ...
```

## Options

`replace` supports the following options:

| Option           | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| -?, -I           | Display a help message and exit.                                  |
| -#debug\_options | Enable debugging.                                                 |
| -s               | Silent mode. Print less information about what the program does.  |
| -v               | Verbose mode. Print more information about what the program does. |
| -V               | Display version information and exit.                             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
