---
description: >-
  Package shell extensions as plugins that load at startup, write them with
  the plugin decorators, and manage plugins from repositories with the
  plugins global object.
---

# Plugins

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

A plugin is a directory of Python code that MariaDB Shell loads at startup. Plugins typically add global objects with documented functions, [reports](reports.md), or [SQL handlers](sql-handlers.md). The built-in `sandbox` and `plugins` globals and the `util.debug` functions are themselves plugins.

## Plugin Layout

Each plugin is a directory that contains an `init.py` file. The shell runs `init.py` at startup; it can import further modules from the same directory.

```text
~/.mariadb-shell/plugins/
└── schema_tools/
    ├── init.py
    └── queries.py
```

The shell searches two locations:

| Location | Contents | Disable with |
| --- | --- | --- |
| `lib/mariadb-shell/plugins/` in the installation directory | The built-in plugins. | `--disable-builtin-plugins` |
| `plugins/` in the user configuration directory: `~/.mariadb-shell/plugins/` on Linux and macOS, `%AppData%\MariaDB\mariadb-shell\plugins\` on Windows | Your plugins, and plugins installed with `plugins.install()`. | `--disable-plugins` |

The rules for a plugin directory:

* The directory name must be a valid Python package name, because the shell imports it as a package. Use letters, digits, and underscores.
* Directories whose names start with a dot are skipped.
* A directory without `init.py` is ignored, unless it's a plugin group.
* While `init.py` runs, the parent of the plugin directory is on `sys.path`, so `init.py` imports helper modules by package name, for example `from schema_tools.queries import find_columns_sql`. The shell restores `sys.path` after the plugin has loaded.
* Each plugin runs in its own namespace. Names it defines don't leak into the interactive Python session; only what it registers, such as global objects, becomes visible.

{% hint style="info" %}
The startup files in the `init.d` directory of the user configuration directory still load when you start the shell with `--disable-plugins`. Only plugin directories are skipped.
{% endhint %}

If a plugin fails to load, the shell prints `Found errors loading plugins, for more details look at the log at: <path>` and continues. The [log file](../logging-and-debugging.md) contains the Python traceback.

### Plugin Groups

A directory without `init.py` can hold several plugins, one level deep. This is useful to keep related plugins, for example the plugins of one team, under one directory:

```text
~/.mariadb-shell/plugins/
└── acme/
    ├── audit/
    │   └── init.py
    └── capacity/
        └── init.py
```

For plugins in a group, the plugins directory itself is on `sys.path` during loading, so modules are imported with the group name as prefix, for example `from acme.audit.checks import run_checks`.

## Built-in Plugins

| Plugin | What it provides |
| --- | --- |
| `sandbox` | The `sandbox` global object for local test servers. See [Sandbox Instances](../sandbox-instances.md). |
| `plugins_plugin` | The `plugins` global object, described [below](#managing-plugins-from-repositories). |
| `debug` | The `util.debug` functions. See [Diagnostics Utilities](../utilities/diagnostics-utilities.md). |
| `util` | `util.change_password()`. See [Password Change Utility](../utilities/password-change-utility.md). |

If you start the shell with `--disable-builtin-plugins`, these objects and functions are missing.

## The Plugin Decorators

The `mysqlsh.plugin_manager` module provides decorators that register global objects and functions and build the help text from your docstrings. They call the lower-level [extension object](extension-objects.md) API for you. Use that API directly only when you need full control over the members of an object.

```python
from mysqlsh.plugin_manager import plugin, plugin_function
```

The module keeps the name `mysqlsh` from MySQL Shell, so plugins written for MySQL Shell import it unchanged.

### @plugin

`@plugin` registers a class as a global object. The class name becomes the object name, and the class docstring becomes its help: the first paragraph is the brief description, and the rest is the details. Inner classes become nested objects.

```python
@plugin
class schemaTools:
    """Helpers for exploring the schemas of a MariaDB server.

    The functions use the active global session.
    """

    class report:
        """Reporting helpers: schemaTools.report."""
```

| Argument | Description |
| --- | --- |
| `parent` | The name of an existing object to attach the new object to, instead of registering a global. For example, `@plugin(parent="util")` on a class named `audit` creates `util.audit`. |
| `shell_version_min`, `shell_version_max` | The range of MariaDB Shell versions the plugin supports, such as `"26.9.0"`. Outside the range, registration fails with an error that names the required version. |

### @plugin_function

`@plugin_function` registers a function as a member of an object:

```python
@plugin_function("schemaTools.findColumns", cli=True)
def find_columns(pattern, **options):
    ...
```

| Argument | Description |
| --- | --- |
| `fully_qualified_name` | Required. The object path and the function name in camelCase, such as `schemaTools.findColumns`. Python callers use the snake_case form, `schemaTools.find_columns()`. If the object doesn't exist yet, pass its help in `plugin_docs`, or declare it first with `@plugin`. |
| `plugin_docs` | A dictionary with `brief` and `details` for an object that the decorator has to create. |
| `shell` | Whether the function is available in the shell. The default is `True`. |
| `cli` | Whether the function is also available through [command line integration](../using-mariadb-shell/command-line-integration.md). The default is `False`, and `cli=True` requires `shell=True`. |

The decorator wraps your function: if it raises an exception, the shell shows the message to the user and writes the traceback to the log at `debug` level. Raise `mysqlsh.Error("message")` for errors that the user should act on.

### Docstring Format

The decorators parse the docstring of each function and refuse to register it when the documentation doesn't match the signature. Follow these rules:

* The first paragraph is the brief description. Further paragraphs become the details. A line that ends with a colon, such as `Returns:`, starts a section.
* An `Args:` section must document every parameter, and only real parameters, one per line in the form `name (type): description`. Continuation lines are indented further.
* Types are Python names that map to shell types: `str` to string, `int` to integer, `bool`, `float`, `dict` to dictionary, `list` to array, and `object` for sessions and other objects. Omit the type to accept any value.
* A parameter with a default value is optional. A parameter declared with `=None` receives `None` when the caller omits it, from the command line too, and callers can pass `None` for it explicitly. Write `(type,required)` only for options inside a dictionary that callers must pass.
* Document the keys of `**options` in a `Keyword Args:` section. For a named dictionary parameter `cfg`, use a section called `Allowed options for cfg:`.
* Lines that start with `* ` become bullet points in the help.

## Example: A Schema Explorer Plugin

The following plugin adds a `schemaTools` global with a `find_columns()` function that searches all user schemas for columns by name. The SQL lives in a helper module.

{% code title="~/.mariadb-shell/plugins/schema_tools/init.py" %}
```python
"""schema_tools: helpers for exploring schemas."""

from mysqlsh.plugin_manager import plugin, plugin_function
from mysqlsh import globals, Error

from schema_tools.queries import find_columns_sql


@plugin
class schemaTools:
    """Helpers for exploring the schemas of a MariaDB server.

    The functions use the active global session.
    """


def _session():
    session = globals.shell.get_session()
    if session is None:
        raise Error("Connect to a server first, for example with \\connect.")
    return session


@plugin_function("schemaTools.findColumns", cli=True)
def find_columns(pattern, **options):
    """Finds columns whose name matches a LIKE pattern.

    Prints one row per matching column and returns the number of matches.

    Args:
        pattern (str): A LIKE pattern for the column name, such as '%email%'.
        **options (dict): Optional arguments.

    Keyword Args:
        schema (str): Search only this schema. By default, all user schemas
            are searched.
        dataType (str): Return only columns of this data type, such as
            'varchar'.

    Returns:
        The number of matching columns.
    """
    sql, args = find_columns_sql(pattern, options.get("schema"),
                                 options.get("dataType"))
    return globals.shell.dump_rows(_session().run_sql(sql, args))
```
{% endcode %}

{% code title="~/.mariadb-shell/plugins/schema_tools/queries.py" %}
```python
SYSTEM_SCHEMAS = ("mysql", "sys", "information_schema", "performance_schema")


def find_columns_sql(pattern, schema=None, data_type=None):
    sql = ("SELECT table_schema, table_name, column_name, column_type "
           "FROM information_schema.columns "
           "WHERE column_name LIKE ? AND table_schema NOT IN (?, ?, ?, ?)")
    args = [pattern, *SYSTEM_SCHEMAS]
    if schema:
        sql += " AND table_schema = ?"
        args.append(schema)
    if data_type:
        sql += " AND data_type = ?"
        args.append(data_type)
    return sql + " ORDER BY 1, 2, 3", args
```
{% endcode %}

Restart the shell and use the plugin. You can pass the options as keyword arguments or as a dictionary:

```text
MariaDB localhost:3306 ssl  Py > schemaTools.find_columns("%email%", schema="shop")
+--------------+------------+--------------+--------------+
| table_schema | table_name | column_name  | column_type  |
+--------------+------------+--------------+--------------+
| shop         | customers  | backup_email | varchar(200) |
| shop         | customers  | email        | varchar(200) |
+--------------+------------+--------------+--------------+
2
```

`\? schemaTools.find_columns` shows the help built from the docstring. Because the function is registered with `cli=True`, it also runs from the operating system shell. Use the object name as registered and the function name in kebab-case or camelCase:

```sh
mariadb-shell root@localhost -- schemaTools find-columns %email% --schema=shop --data-type=varchar
```

## Managing Plugins from Repositories

The `plugins` global object installs plugins that are published in a plugin repository: a JSON manifest that lists plugins, their versions, and download URLs. MariaDB Shell doesn't register any repository by default, so `plugins.list()` shows nothing until you add one.

| Function | Description |
| --- | --- |
| `plugins.repositories.add([url])` | Adds a repository after showing its plugins and asking for confirmation. Without a URL, it prompts for one. |
| `plugins.repositories.list()` | Lists the registered repositories. |
| `plugins.repositories.remove([url=...])` | Removes a repository. Without `url`, it prompts for the repository to remove. |
| `plugins.list()` | Lists the plugins in all registered repositories, with their installation and update status. |
| `plugins.details([name])` | Shows details about a plugin. |
| `plugins.install([name])` | Downloads a plugin and extracts it into the user `plugins` directory. Restart the shell to load it. |
| `plugins.update([name])` | Updates one plugin, or all installed plugins that have a newer version. |
| `plugins.uninstall([name])` | Removes an installed plugin. |
| `plugins.info()`, `plugins.version()` | Show the version of the plugin manager. |
| `plugins.about()` | Prints an overview of plugin support. |

Without a name, the functions that act on one plugin prompt you to choose. They also accept keyword arguments; for example, `plugins.install("myplugin", version="1.2.0", force_install=True)` installs a specific version over an existing copy. Run `\? plugins.install` for the full list.

`plugins.repositories.add()` expands short forms of the URL:

| You enter | Manifest URL |
| --- | --- |
| `example.com` | `https://example.com/mariadb-shell-plugins-manifest.json` |
| `example.com/plugins` | `https://example.com/plugins/mariadb-shell-plugins-manifest.json` |
| `github/<user>` | `https://raw.githubusercontent.com/<user>/mariadb-shell-plugins/master/mariadb-shell-plugins-manifest.json` |
| `github/<user>/<repo>` | `https://raw.githubusercontent.com/<user>/<repo>/master/mariadb-shell-plugins-manifest.json` |

The registered repositories are stored in `plugin-repositories.json` in the user configuration directory.

{% hint style="warning" %}
A plugin runs with your operating system permissions and has access to every session you open in the shell. Add repositories and install plugins only from sources you trust.
{% endhint %}

The plugin manager considers a plugin installed when a global object with the plugin's name exists. To let it detect updates, give the plugin object a `version()` function that returns the version string.

<sub>_This page is licensed: GPLv2_</sub>
