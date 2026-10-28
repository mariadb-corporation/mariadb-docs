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

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
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

## Writing a description

Put a `* Description:` bullet after the other bullets of every setting:

```markdown
### `match`

* Type: [regex](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
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
