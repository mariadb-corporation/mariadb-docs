# Cookbook: the MaxScale settings reference

`maxscale/reference/maxscale-configuration-settings.md` lists every MaxScale configuration
setting on one page. **It is generated** by `maxscale/gen_settings_reference`, a Python script
owned by Johan Wikman (MaxScale), from the module pages that document each setting. Don't edit
the page by hand, in Git or in the GitBook editor: the next run overwrites every hand edit
(DOCS-6943).

## Where each part of an entry comes from

An entry looks like this on the reference page:

```markdown
[**match**](maxscale-filters/maxscale-binlog-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Includes only events that match the given regular expression.
```

Every line of it comes from the module page:

| Part | Source |
|------|--------|
| The name and its link | The heading above the `* Type` bullet, or a bold paragraph such as ``**`vault.host`**`` directly above it. With a bold paragraph, the link points at the heading above it. |
| The bullets | Every `* ` line from `* Type` to the first line that isn't a bullet, copied as they are. Links in them are rewritten to be relative to the reference page. |
| The description | The `* Description:` bullet. It is one of the bullets, so it is copied the same way. |
| The group | The heading one level above the setting, for example `Settings` or ``storage_redis``. For a bold-paragraph name, the heading directly above it. |

To change what the reference page says about a setting, edit its module page and regenerate.

### Module pages split into a folder

A long module page can be split into a folder (DOCS-6367): `maxscale-readwritesplit.md` became
`maxscale-readwritesplit/README.md`, which keeps the URL, plus `readwritesplit-settings.md`,
which holds the settings. The script treats a folder that has a `README.md`, has no subfolders,
and sits at least two levels below `reference/` as **one** module page. Its settings stay under the page's old
heading (`[maxscale-readwritesplit](…/README.md)`), and each entry links to the file that holds
it. The group is still the heading one level up, which in a settings child page is its H1 (for
example "MaxScale Readwritesplit Settings").

Category folders such as `reference/maxscale-routers/` also have a `README.md`, but they sit only
one level below `reference/`, so they are scanned as before.

The MaxScale Configuration Guide is split the same way, into
`maxscale-configuration-guide/README.md` plus `global-settings.md` and `service-settings.md`.
It isn't under `reference/`: it's the script's first default argument, and the argument is the
folder. A split-page folder (a flat folder with a `README.md`) given as an argument is grouped like a single file, under its
top-level directory, so its settings stay under **General** > **MaxScale**. If a split page moves
or a new top-level page is added, update the default arguments in `main()`.

## Writing a description

Put a `* Description:` bullet after the other bullets of every setting:

```markdown
### `match`

* Type: [regex](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Includes only events that match the given regular expression.
```

Keep it to one sentence that says what the setting does. The longer explanation stays in the
prose below the bullets.

## Regenerating the page

From the `maxscale` directory:

```bash
./gen_settings_reference > reference/maxscale-configuration-settings.md
```

The script prints to stderr every setting that has no `* Description:` bullet. Add the
missing descriptions to the module pages and run it again.

Before you commit:

- Read the diff of the reference page. Every change in it should come from a module-page change
  you can name.
- Run the gates on the reference page and on every module page you changed: `docs-check`, or
  `.claude/hooks/doc-lint.sh <files>`. The links use the GitBook slug rules of
  `.claude/hooks/fragcheck.py`, which the script imports, so fragcheck should report no dead
  anchors.

## What the script treats as a setting

A setting is a `* Type` bullet under a name that is an identifier: a lowercase letter, then
letters, digits, `_` or `.` (`threads`, `vault.host`, `matchXY`). The REST API resource pages
and the telemetry metrics also have `* Type` bullets, under headings such as "Create a filter"
or "General Metrics". The identifier rule leaves those out.

The `debug` parameter's options (`disable-module-unloading`, `gdb-stacktrace` and so on) are not
settings. They are documented in a list under the `debug` setting in the MaxScale configuration
guide.
