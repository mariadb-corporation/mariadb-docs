---
description: >-
  Line-editing keys at the MariaDB Shell prompt, editing statements in an
  external editor, and the per-mode command history with its options and
  filters.
---

# Editing and History

The MariaDB Shell prompt has Emacs-style line editing, a searchable command history, and a shortcut that opens the current statement in your text editor. These features are available in interactive sessions.

## Line-Editing Keys

In the following table, **Meta** is the **Alt** key on most keyboards. On macOS terminals, set the **Option** key to act as Meta, or press **Esc** and then the letter.

### Moving the Cursor

| Keys | Action |
| --- | --- |
| **Ctrl+A**, **Home** | Moves to the start of the line. |
| **Ctrl+E**, **End** | Moves to the end of the line. |
| **Ctrl+B**, **Left** | Moves one character left. |
| **Ctrl+F**, **Right** | Moves one character right. |
| **Meta+B**, **Ctrl+Left** | Moves one word left. |
| **Meta+F**, **Ctrl+Right** | Moves one word right. |

### Deleting and Pasting

| Keys | Action |
| --- | --- |
| **Backspace**, **Ctrl+H** | Deletes the character left of the cursor. |
| **Delete** | Deletes the character under the cursor. |
| **Ctrl+D** | Deletes the character under the cursor. On an empty line, exits the shell. |
| **Ctrl+K** | Cuts from the cursor to the end of the line. |
| **Ctrl+U** | Cuts from the start of the line to the cursor. |
| **Ctrl+W** | Cuts the text left of the cursor up to the previous space. |
| **Meta+D** | Cuts the word right of the cursor. |
| **Meta+Backspace** | Cuts the word left of the cursor. |
| **Ctrl+Y** | Pastes the most recently cut text. |
| **Meta+Y** | After **Ctrl+Y**, replaces the pasted text with the previously cut text. |

### Changing Text

| Keys | Action |
| --- | --- |
| **Ctrl+T** | Swaps the character under the cursor with the one before it. |
| **Meta+U** | Converts the word to uppercase. |
| **Meta+L** | Converts the word to lowercase. |
| **Meta+C** | Capitalizes the word. |
| **Tab** | Completes the word under the cursor. See [Autocompletion](autocompletion.md). |

### History and Control

| Keys | Action |
| --- | --- |
| **Up**, **Ctrl+P** | Shows the previous history entry. |
| **Down**, **Ctrl+N** | Shows the next history entry. |
| **Page Up**, **Meta+<** | Jumps to the oldest history entry. |
| **Page Down**, **Meta+>** | Jumps back to the line you are typing. |
| **Ctrl+R** | Searches the history backward. Type part of an entry; press **Ctrl+R** again for older matches. |
| **Ctrl+S** | Searches the history forward. |
| **Ctrl+X Ctrl+E** | Opens the last history entry in the external editor. See [External Editor](#external-editor). |
| **Ctrl+L** | Clears the screen and redraws the current line. |
| **Ctrl+C** | Discards the current line or the pending multi-line statement. While a statement runs, cancels it. |
| **Ctrl+Z** | Suspends the shell (Linux and macOS). Resume it with `fg`. |

## External Editor

For long statements, an editor is more comfortable than the prompt. `\edit` (or `\e`) writes text to a temporary file and opens it in an editor:

* `\edit` without an argument opens the most recent history entry.
* `\edit <text>` opens the given text, for example `\e SELECT * FROM product`.
* **Ctrl+X Ctrl+E** works like `\edit` without an argument.

When you save and quit the editor, the edited text is placed at the prompt. Review it and press **Enter** to run it. If you quit without saving, the original text comes back.

The shell starts the program named in the `EDITOR` environment variable, or in `VISUAL` if `EDITOR` isn't set. Without either, it uses `vi` on Linux and macOS and `notepad.exe` on Windows. The variable can include options, such as `code --wait` for Visual Studio Code, which needs `--wait` so that the shell waits until you close the file.

```sh
export EDITOR="nano"
```

## Command History

The shell records each statement and command you run at the prompt. Up and Down arrows, **Ctrl+R**, and `\history` work with these entries. A statement that you typed over several lines is stored as one entry.

### History Files

SQL mode and Python mode keep separate histories, so the Up arrow in SQL mode doesn't bring back Python code. When you switch modes with `\sql` or `\py`, the shell saves the history of the old mode and loads the history of the new one.

The histories are saved in the shell's configuration directory when the shell exits:

| Mode | Linux and macOS | Windows |
| --- | --- | --- |
| SQL | `~/.mariadb-shell/history.sql` | `%APPDATA%\MariaDB\mariadb-shell\history.sql` |
| Python | `~/.mariadb-shell/history.py` | `%APPDATA%\MariaDB\mariadb-shell\history.py` |

If `MARIADB_SHELL_USER_CONFIG_HOME` is set, the files are in that directory instead. The files are created with permissions that only the owner can read.

Statements that run from a script, with `\source` or `-f`, aren't added to the history.

### The \history Command

`\history` without arguments lists the entries of the current mode with their numbers:

```text
MariaDB localhost:3306 ssl  shop  SQL > \history
    1  SELECT * FROM product;
    2  SELECT * FROM product WHERE id=1\G
    3  \use sakila
    4  SELECT COUNT(*) FROM rental;
```

| Command | Effect |
| --- | --- |
| `\history del <n>` | Deletes entry *n*. |
| `\history del <n>-<m>` | Deletes entries *n* through *m*. |
| `\history del <n>-` | Deletes entry *n* and all later entries. |
| `\history del -<n>` | Deletes the last *n* entries. |
| `\history clear` | Deletes all entries of the current mode. |
| `\history save` | Writes the history of the current mode to its file now, without waiting for the shell to exit. |

`delete` is a synonym for `del`. Use `\history del` to remove an entry that contains something you don't want to keep, such as a password that you typed in a statement the ignore filter didn't catch.

### History Options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `history.autoSave` | Boolean | `true` | Saves the history to the history files when the shell exits. With `false`, the history lasts only for the session, unless you run `\history save`. |
| `history.maxSize` | Integer | `1000` | The number of entries to keep per mode. The oldest entries are dropped first. |
| `history.sql.ignorePattern` | String | `*IDENTIFIED*:*PASSWORD*` | A colon-separated list of glob patterns. SQL statements that match one aren't saved. |
| `history.sql.syslog` | Boolean | `false` | Also writes SQL statements that pass the ignore filter to the system log. Same as the `--syslog` command line option. |

Set the options with `\option` or `shell.options`, and add `--persist` to keep the setting:

```text
MariaDB localhost:3306 ssl  SQL > \option --persist history.maxSize 10000
MariaDB localhost:3306 ssl  SQL > \option --persist history.autoSave false
```

### Keeping Secrets Out of the History

`history.sql.ignorePattern` keeps statements with sensitive content out of the history files. The patterns use `*` for any sequence of characters and `?` for one character, they must match the whole statement, and matching ignores case. The default value `*IDENTIFIED*:*PASSWORD*` catches statements such as `CREATE USER ... IDENTIFIED BY '...'` and `SET PASSWORD`.

A statement that matches a pattern is still available with the Up arrow for the next command, so you can correct a typo in it. After the next command, it's removed and never written to disk.

To extend the list for one session, use `--histignore` on the command line. The value replaces the default, so repeat the default patterns if you want to keep them:

```sh
mariadb-shell --histignore='*IDENTIFIED*:*PASSWORD*:*AES_ENCRYPT*' mariadb://dba@localhost
```

To change the list permanently, persist the option:

```text
MariaDB localhost:3306 ssl  SQL > \option --persist history.sql.ignorePattern *IDENTIFIED*:*PASSWORD*:*AES_ENCRYPT*
```

The filter applies to SQL statements only: lines that you type in SQL mode, statements that you run with `\sql` (or `/sql`) from Python mode, and the arguments of `\show` and `\watch`, which a report such as `query` runs as SQL. In SQL mode it also applies to `\source` lines, which the system log records. Other shell commands aren't SQL and aren't filtered.

A `\connect` (or `\c`, `/connect`) line is saved without its password, in any mode: `\connect root:secret@localhost` is saved as `\connect root@localhost`, and `--password=secret` as `--password`, so running the entry again prompts for the password. A password in an `--ssh` URI is removed too, and the rest of a URI is kept as typed; an empty password, as in `root:@localhost`, isn't a secret and stays. A shell command line that the shell rejects, such as a `\connect` with an error in its options or a command with a misplaced quote, is kept only until the next command, as a filtered statement is.

Python code isn't filtered: avoid literal passwords in Python lines, and use the credential store or `shell.prompt()` instead. See [Credential Store](../connecting/credential-store.md).
