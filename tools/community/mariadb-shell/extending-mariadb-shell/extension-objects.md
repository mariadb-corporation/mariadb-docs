---
description: >-
  Build your own global objects with shell.create_extension_object(),
  add_extension_object_member(), and register_global(), including the help
  text and parameter validation.
---

# Extension Objects

An extension object is a container for functions, properties, and nested objects that you define in Python and register as a global object. Once registered, it behaves like the built-in globals: it's available in Python mode without an import, `\?` documents it, the shell validates the arguments of its functions, and it can expose functions to [command line integration](../using-mariadb-shell/command-line-integration.md).

This page describes the low-level API. When you write a [plugin](plugins.md), the `@plugin` and `@plugin_function` decorators call this API for you and build the member definitions from your docstrings, which is usually less work. Use the API directly when you want full control, or for a few helpers in your [startup script](../customizing/startup-scripts.md).

## How It Works

Building an extension object takes three steps:

1. Create an empty object with `shell.create_extension_object()`.
2. Add functions, properties, and child objects with `shell.add_extension_object_member()`.
3. Register the top-level object with `shell.register_global()`.

```python
greeter = shell.create_extension_object()

def hello(name):
    return f"Hello, {name}!"

shell.add_extension_object_member(greeter, "hello", hello, {
    "brief": "Returns a greeting.",
    "parameters": [{"name": "name", "type": "string", "brief": "Who to greet."}]
})

shell.register_global("greeter", greeter, {"brief": "A minimal extension object."})
```

```text
MariaDB localhost:3306 ssl  Py > greeter.hello("world")
Hello, world!
```

The members of an object become usable only when the object is registered as a global, or added to another object that is registered. You can add members before or after registration.

## shell.create_extension_object()

```python
shell.create_extension_object()
```

Returns a new, empty extension object. It takes no arguments.

## shell.add_extension_object_member()

```python
shell.add_extension_object_member(object, name, member[, definition])
```

| Parameter | Description |
| --- | --- |
| `object` | The extension object to add the member to. |
| `name` | The member name. It must match `[_a-zA-Z][_a-zA-Z0-9]*`. |
| `member` | The member: a function, another extension object, or a value. |
| `definition` | Optional. A dictionary with the help text and, for functions, the parameter definitions. |

The kind of member determines how it behaves:

| Member | Behavior |
| --- | --- |
| Function | A method of the object. It can't be replaced after it's added. |
| Extension object | A read-only property that holds a nested object, such as `dbtools.sessions`. |
| Boolean, integer, float, string, list, dictionary, or `None` | A read-write property. Code can assign a new value at any time. |

Write member names in camelCase. In Python mode, the shell exposes them in snake_case: a member added as `tableCount` is called as `dbtools.table_count()`, and a property added as `maxRows` is read as `dbtools.max_rows`. Option names inside dictionary parameters keep the spelling you define.

### Member Definition

| Key | Type | Applies to | Description |
| --- | --- | --- | --- |
| `brief` | string | All members | A one-line description for the help. |
| `details` | list of strings | All members | Paragraphs of detailed help. |
| `parameters` | list of dictionaries | Functions | The parameters of the function, in order. |
| `cli` | bool | Functions | When `True`, the function is also available through command line integration. The default is `False`. |

### Parameter Definition

Each entry of `parameters` describes one positional parameter:

| Key | Type | Description |
| --- | --- | --- |
| `name` | string | Required. The parameter name, a valid identifier. It appears in the help. |
| `type` | string | The type the shell enforces: `string`, `integer`, `float`, `bool`, `array`, `dictionary`, or `object`. Without `type`, the parameter accepts any value. |
| `required` | bool | Whether the caller must pass the parameter. Parameters are required by default. List required parameters before optional ones. |
| `default` | any | The value the function receives when the caller omits an optional parameter. |
| `brief` | string | A one-line description. |
| `details` | list of strings | Additional help paragraphs. |
| `values` | list of strings | For `string` parameters, the only values allowed. |
| `class`, `classes` | string, list of strings | For `object` parameters, the class or classes of object allowed, for example `ClassicSession`. To find the class name of an object, print it: `print(session)` shows `<ClassicSession:...>`. |
| `options` | list of dictionaries | For `dictionary` parameters, the keys the dictionary accepts. |

An option definition, an entry of `options`, takes the same keys as a parameter definition. Options are optional unless you set `"required": True`, and they can appear in any order. When a caller passes a key that isn't defined, the shell rejects the call with `Invalid options at Argument #n`.

The shell checks the arguments against the definitions before it calls your function, and reports a mismatch as an error such as `Argument #1 is expected to be a string`.

## shell.register_global()

```python
shell.register_global(name, object[, definition])
```

| Parameter | Description |
| --- | --- |
| `name` | The name of the global object. It must be a valid identifier and can't be the name of a built-in global or of an object that is already registered. The name is used exactly as given, with no snake_case conversion. |
| `object` | The extension object to register. |
| `definition` | Optional. A dictionary with `brief` and `details` for the help. |

## Example: A DBA Toolbox

The following script defines a `dbtools` global with a function, a nested object, and a property. Save it in the `init.d` directory of the user configuration directory, for example `~/.mariadb-shell/init.d/dbtools.py`, so it loads at every start.

{% code title="~/.mariadb-shell/init.d/dbtools.py" %}
```python
def _require_session():
    session = shell.get_session()
    if session is None:
        raise Exception("Connect to a server first.")
    return session


def table_count(schema):
    result = _require_session().run_sql(
        "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = ?",
        [schema])
    return result.fetch_one()[0]


def kill_idle(min_seconds, options=None):
    options = options or {}
    session = _require_session()
    sql = ("SELECT id FROM information_schema.processlist "
           "WHERE command = 'Sleep' AND time >= ? AND id <> CONNECTION_ID()")
    args = [min_seconds]
    if options.get("user"):
        sql += " AND user = ?"
        args.append(options["user"])
    ids = [row[0] for row in session.run_sql(sql, args).fetch_all()]
    if not options.get("dryRun", False):
        for connection_id in ids:
            session.run_sql("KILL CONNECTION ?", [connection_id])
    return ids


dbtools = shell.create_extension_object()
sessions = shell.create_extension_object()

shell.add_extension_object_member(dbtools, "tableCount", table_count, {
    "brief": "Returns the number of tables in a schema.",
    "cli": True,
    "parameters": [
        {"name": "schema", "type": "string", "brief": "Name of the schema."}
    ]})

shell.add_extension_object_member(sessions, "killIdle", kill_idle, {
    "brief": "Kills connections that have been idle for a while.",
    "details": ["Returns the IDs of the affected connections."],
    "parameters": [
        {"name": "minSeconds", "type": "integer",
         "brief": "Minimum idle time in seconds."},
        {"name": "options", "type": "dictionary", "required": False,
         "brief": "Additional options.",
         "options": [
             {"name": "user", "type": "string",
              "brief": "Only connections of this user."},
             {"name": "dryRun", "type": "bool",
              "brief": "List the connections without killing them."}
         ]}
    ]})

shell.add_extension_object_member(dbtools, "sessions", sessions,
                                  {"brief": "Connection management helpers."})
shell.add_extension_object_member(dbtools, "version", "1.0",
                                  {"brief": "Version of the toolbox."})

shell.register_global("dbtools", dbtools, {
    "brief": "Small DBA helpers.",
    "details": ["Defined in init.d/dbtools.py."]})
```
{% endcode %}

After a restart, the object is documented and ready:

```text
MariaDB localhost:3306 ssl  Py > \? dbtools.sessions.kill_idle
NAME
      kill_idle - Kills connections that have been idle for a while.

SYNTAX
      dbtools.sessions.kill_idle(minSeconds[, options])

WHERE
      minSeconds: Integer - Minimum idle time in seconds.
      options: Dictionary - Additional options.

DESCRIPTION
      Returns the IDs of the affected connections.

      The options parameter accepts the following options:

      - user: String - Only connections of this user.
      - dryRun: Bool - List the connections without killing them.

MariaDB localhost:3306 ssl  Py > dbtools.table_count("sakila")
23
MariaDB localhost:3306 ssl  Py > dbtools.sessions.kill_idle(600, {"user": "app", "dryRun": True})
[
    118,
    131
]
```

Because `tableCount` sets `"cli": True`, you can also call it from the operating system shell. Give the connection before the `--` separator:

```sh
mariadb-shell root@localhost -- dbtools table-count sakila
```
