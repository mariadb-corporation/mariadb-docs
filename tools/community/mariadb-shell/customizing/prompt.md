---
description: >-
  Choose one of the shipped prompt themes, including the Nerd Fonts themes,
  or write your own prompt.json with segments, classes, and prompt variables
  such as %vendor%.
---

# Prompt

The MariaDB Shell prompt is built from a theme: a JSON file that arranges segments of text, such as the server vendor, the host and port, the default schema, and the current mode, each with its own colors. A typical prompt with the default theme looks like this:

```text
 MariaDB  localhost:3306 ssl  sakila  SQL >
```

The shell ships a set of themes and picks one automatically. You can select a different shipped theme or write your own.

## How the Shell Selects a Theme

At startup, the shell uses the first of the following that applies:

1. The `MARIADB_SHELL_PROMPT_THEME` environment variable, if it's set. Its value is the path to a theme file. If the file doesn't exist, the shell prints a note and uses its plain built-in prompt. An empty value also selects the plain built-in prompt, which shows the mode and the default schema without colors.
2. `prompt.json` in the user configuration directory: `~/.mariadb-shell/prompt.json` on Linux and macOS, `%AppData%\MariaDB\mariadb-shell\prompt.json` on Windows.
3. A shipped theme that matches the color capability of the terminal: `prompt_256.json` for terminals with 256 or more colors, `prompt_16.json` for 16-color terminals, and `prompt_nocolor.json` for terminals without color.

The shell never selects a theme that needs a patched font on its own. To use one, copy it to `prompt.json` or point `MARIADB_SHELL_PROMPT_THEME` to it.

### Terminal Color Capability

On Linux and macOS, the shell assumes 256 colors unless the `TERM` environment variable is unset, in which case it assumes 16 colors. On Windows, it uses 24-bit color when the console supports virtual terminal sequences, and no color otherwise.

To override the detection, set `MARIADB_SHELL_TERM_COLOR_MODE`:

| Value | Meaning |
| --- | --- |
| `rgb` | 24-bit color. Theme colors written as `#rrggbb` are used as is. |
| `256` | 256 indexed colors. |
| `16` | The 16 basic ANSI colors. |
| `nocolor` | No colors or text attributes. |

With any other non-empty value, the shell prints a note and falls back to its plain built-in prompt.

```sh
MARIADB_SHELL_TERM_COLOR_MODE=16 mariadb-shell root@localhost
```

## Shipped Themes

The themes are in the `share/mariadb-shell/prompt/` directory of the installation, together with a `README.prompt` file that summarizes the format.

| Theme | Description |
| --- | --- |
| `prompt_256.json` | The default for color terminals. Colored blocks for the vendor, the host and port with an `ssl` marker, the default schema, the transaction state, and the mode. |
| `prompt_256inv.json` | Like `prompt_256.json`, with colored text instead of colored blocks. |
| `prompt_dbl_256.json` | Like `prompt_256.json`, with the information on one line and the input prompt on the next, which leaves more room for typing. |
| `prompt_16.json` | For terminals with 16 colors. |
| `prompt_nocolor.json` | No colors or attributes, for example `MariaDB [localhost:3306 ssl/sakila] SQL>`. |
| `prompt_classic.json` | A short prompt such as `mariadb-sql>`. It shows neither the vendor nor connection details. |
| `prompt_256_nerd-fonts.json`, `prompt_dbl_256_nerd-fonts.json` | One-line and two-line themes with arrow-shaped segment separators and icons. They need a font from the [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) project, such as JetBrainsMono Nerd Font, set as your terminal font. |
| `prompt_256pl.json`, `prompt_dbl_256pl.json` | Themes with arrow-shaped separators that need a font patched for Powerline. |
| `prompt_256pl+aw.json`, `prompt_dbl_256pl+aw.json` | Powerline themes that also use icon characters from fonts patched with the awesome-terminal-fonts symbols. |

The Nerd Fonts themes are specific to MariaDB Shell. Nerd Fonts bundles the Powerline glyphs and is actively maintained, so prefer these themes over the `pl` and `pl+aw` themes if you want separators and icons. Without a suitable font, the special characters appear as boxes.

Every theme except `prompt_classic.json` starts with the vendor of the connected server, through the `%vendor%` variable: `MariaDB` or `MySQL`. While the shell isn't connected, the segment shows `MariaDB`.

All themes except `prompt_classic.json` also show a ` PRODUCTION ` marker, red in the color themes, when the host of the current connection is listed in the `PRODUCTION_SERVERS` environment variable. Separate several hosts with semicolons:

```sh
export PRODUCTION_SERVERS="db1.example.com;db2.example.com"
```

To use a shipped theme permanently, copy it to your user configuration directory:

{% tabs %}
{% tab title="Linux and macOS" %}
```sh
cp "$(dirname "$(command -v mariadb-shell)")/../share/mariadb-shell/prompt/prompt_256_nerd-fonts.json" ~/.mariadb-shell/prompt.json
```
{% endtab %}

{% tab title="Windows" %}
```powershell
$share = Join-Path (Split-Path (Get-Command mariadb-shell).Source) "..\share\mariadb-shell\prompt"
Copy-Item "$share\prompt_256_nerd-fonts.json" "$env:APPDATA\MariaDB\mariadb-shell\prompt.json"
```
{% endtab %}
{% endtabs %}

## Theme File Format

A theme is a JSON object with these top-level keys:

| Key | Description |
| --- | --- |
| `segments` | Required. The list of segments, displayed from left to right. |
| `classes` | Named sets of segment attributes that segments can select dynamically. |
| `variables` | Custom variables computed from other variables. |
| `prompt` | The text and attributes of the final input prompt. |
| `symbols` | The default separator and ellipsis characters. |
| `desc` | A free-text description of the theme. The shell ignores it. |

### Segments

Each segment is a JSON object with any of these attributes:

| Attribute | Description |
| --- | --- |
| `text` | The text to display. It can contain [variables](#prompt-variables). |
| `fg`, `bg` | The foreground and background color. See [Colors](#colors). |
| `bold`, `underline` | `true` to make the text bold or underlined. |
| `padding` | The number of spaces around the text. |
| `separator` | The separator after this segment, instead of the default from `symbols`. |
| `shrink` | How to shorten the text when the line is too narrow: `none`, `truncate_on_dot` (cut a host name at a dot), or `ellipsize` (cut the end and add the ellipsis). |
| `min_width` | The minimum width to which the segment can shrink. |
| `weight` | The priority for hiding segments when the terminal is too narrow. Segments with higher weights are hidden first. |
| `classes` | A list of class names. The first name that exists in `classes` supplies attributes for the segment. Names can contain variables. |

A segment `{"break": true}` starts a new line, which is how the two-line themes put the input prompt on its own line.

### Classes

The `classes` object maps a class name to a set of segment attributes. Because class names in a segment can contain variables, a segment can change its look depending on the connection state. The shipped themes use this pattern often:

```json
{ "classes": ["noschema%schema%", "schema"] }
```

When no default schema is selected, `%schema%` is empty, the first name becomes `noschema`, and that class applies. When a schema is selected, the first name becomes something like `noschemasakila`, which isn't defined, so the shell falls through to the `schema` class. In the same way, `%Mode%` as a class name selects the class `SQL` or `Py`, so each mode can have its own colors.

### Custom Variables

Under `variables`, you can define a variable whose value depends on a pattern match:

```json
"variables": {
  "is_production": {
    "match": { "pattern": "*;%host%;*", "value": ";%env:PRODUCTION_SERVERS%;" },
    "if_true": "production",
    "if_false": ""
  }
}
```

The shell expands the variables in `value` and `pattern`, matches the value against the pattern, where `*` and `?` are wildcards, and sets the variable to `if_true` or `if_false`. Use the variable like any other, as `%is_production%`. Custom variables are evaluated when the shell connects, and the result is cached for the connection.

### Prompt and Symbols

```json
"prompt": { "text": "> ", "cont_text": "%linectx%> ", "fg": "32" },
"symbols": { "separator": " ", "separator2": " ", "ellipsis": "..." }
```

* `prompt.text` is shown where you type. `prompt.cont_text` replaces it on continuation lines of a statement that isn't complete yet. The prompt also accepts the color and attribute keys of a segment.
* `symbols.separator` is the default separator between segments, `symbols.separator2` an alternative separator that some themes use between segments of the same color, and `symbols.ellipsis` the text appended to a shortened segment.

### Colors

A color value is a color name, a color index from 0 to 255, or a `#rrggbb` value. You can give several, separated by semicolons, and the shell picks the one that matches the terminal: for example, `"red;160;#d70000"` uses `#d70000` on 24-bit terminals, index 160 on 256-color terminals, and `red` on 16-color terminals. The color names are `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, and `white`.

## Prompt Variables

| Variable | Value |
| --- | --- |
| `%vendor%` | The vendor of the connected server, `MariaDB` or `MySQL`. While not connected, `MariaDB`. |
| `%mode%`, `%Mode%` | The current mode: `sql` or `py`, or capitalized as `SQL` or `Py`. |
| `%uri%` | The URI of the current connection, without the password. |
| `%user%` | The user name of the current connection. |
| `%host%` | The host of the current connection. |
| `%port%` | The TCP port, or empty for socket connections. |
| `%socket%` | The socket path or named pipe, `default` for the default socket, or empty for TCP connections. |
| `%ssh_host%` | The SSH server of a [tunneled](../connecting/ssh-tunnels.md) connection, or empty. |
| `%ssl%` | `SSL` when the connection is encrypted, otherwise empty. |
| `%session%` | `c` while connected, otherwise empty. |
| `%connection_id%` | The connection ID of the current connection. |
| `%schema%` | The default schema. |
| `%trx%` | `*` inside a transaction, `^` inside a read-only transaction, otherwise empty. |
| `%autocommit%` | `.` when autocommit is off, otherwise empty. |
| `%slow_query%` | `&` when the server flagged the last statement as slow. |
| `%linectx%` | On continuation lines, what is still open: `-` for an unfinished statement, or `'`, `"`, `` ` ``, or `/*` for an open string, quoted identifier, or comment. Empty otherwise. |
| `%system_user%` | The operating system user who runs the shell. |
| `%time%`, `%date%` | The current time (`HH:MM:SS`) and date (`YYYY-MM-DD`). |
| `%env:NAME%` | The value of the environment variable `NAME`. |
| `%sysvar:name%` | The value of the global system variable `name`. |
| `%sessvar:name%` | The value of the session system variable `name`. |
| `%status:name%` | The value of the global status variable `name`. |
| `%sessstatus:name%` | The value of the session status variable `name`. |

The connection variables are read once per connection. The values of `%sysvar:…%`, `%sessvar:…%`, `%status:…%`, and `%sessstatus:…%` are also cached; to read the current value each time the prompt is drawn, capitalize the prefix, for example `%Sessvar:sql_mode%` or `%Status:Threads_connected%`. Each uncached variable sends a query to the server before every prompt.

## Example: A Custom Theme

The following theme shows a red `PROD` marker for hosts listed in a `PROD_HOSTS` environment variable, the vendor, `user@host:port` or `not connected`, the default schema, a `*` inside transactions, and the mode in a mode-specific color.

{% code title="~/.mariadb-shell/prompt.json" %}
```json
{
  "desc": "Vendor, user@host:port, schema, transaction state and mode, with a PROD marker.",
  "symbols": { "separator": " ", "separator2": " ", "ellipsis": "~" },
  "variables": {
    "env_label": {
      "match": { "pattern": "*;%host%;*", "value": ";%env:PROD_HOSTS%;" },
      "if_true": "prod",
      "if_false": "dev"
    }
  },
  "classes": {
    "prod":     { "text": " PROD ", "bg": "red;160;#d70000", "fg": "white", "bold": true },
    "dev":      { "text": "" },
    "online":   { "text": "%user%@%host%:%port%" },
    "offline":  { "text": "not connected", "fg": "white;245" },
    "schema":   { "text": "%schema%", "fg": "green;71" },
    "noschema": { "text": "" },
    "intrx":    { "text": "*", "fg": "red;196" },
    "notrx":    { "text": "" },
    "SQL":      { "fg": "yellow;214" },
    "Py":       { "fg": "cyan;39" }
  },
  "segments": [
    { "classes": ["dev%host%", "%env_label%"] },
    { "text": "%vendor%", "fg": "blue;31", "bold": true },
    { "classes": ["offline%host%", "online"], "shrink": "truncate_on_dot", "weight": 10 },
    { "classes": ["noschema%schema%", "schema"], "shrink": "ellipsize", "min_width": 8, "weight": 5 },
    { "classes": ["notrx%trx%", "intrx"] },
    { "classes": ["%Mode%"], "text": "%Mode%" }
  ],
  "prompt": { "text": "> ", "cont_text": "%linectx%> " }
}
```
{% endcode %}

The first segment uses `dev%host%` so that the marker disappears while the shell isn't connected, when `%host%` is empty. Without colors, the prompt reads:

```text
MariaDB root@localhost:3306 sakila SQL> BEGIN;
Query OK, 0 rows affected (0.0001 sec)
MariaDB root@localhost:3306 sakila * SQL> \disconnect
MariaDB not connected SQL>
```

To try a theme before you install it, point `MARIADB_SHELL_PROMPT_THEME` to the file for one run:

```sh
MARIADB_SHELL_PROMPT_THEME=./my-theme.json mariadb-shell root@localhost
```

If the file isn't valid JSON, the shell prints `Error loading prompt theme` with the reason and uses its plain built-in prompt.
