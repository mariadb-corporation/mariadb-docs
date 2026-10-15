---
description: >-
  Complete SQL keywords, database object names, Python objects, and shell
  commands with the Tab key, and control the name cache that SQL completion
  uses.
---

# Autocompletion

Press **Tab** at the prompt to complete the word under the cursor. If exactly one completion fits, the shell inserts it. If several fit, press **Tab** a second time to list them.

Completion is available in interactive sessions only. It works in both modes and for shell commands:

| What you type | What completes |
| --- | --- |
| A backslash or slash at the start of the line | Shell commands, such as `\rehash` or `/history`, and their arguments. See [The Slash Prefix](shell-commands.md#the-slash-prefix). |
| SQL, in SQL mode | SQL keywords and built-in functions, plus database object names from the name cache. |
| Python, in Python mode | Global objects such as `util`, `shell`, `session`, and `sandbox`, their methods and properties, and Python names in scope. |

## SQL Mode

SQL completion is context-aware: the shell parses the statement up to the cursor and offers only what fits at that position. After `FROM`, it offers schema, table, and view names. In a select list, it offers the columns of the tables named in the statement. After `CALL`, it offers stored procedures. Keywords complete in uppercase, whatever case you type.

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT * FROM pro<Tab>
MariaDB localhost:3306 ssl  shop  SQL > SELECT * FROM product
```

Names that need quoting, such as names with spaces or names that are reserved words, are inserted with backticks. If you start a name with a backtick, the completion keeps it.

## Python Mode

In Python mode, **Tab** completes global objects and the members of any object that the shell knows, following the chain of names you typed:

```text
MariaDB localhost:3306 ssl  shop  Py > util.dump_s<Tab>
MariaDB localhost:3306 ssl  shop  Py > util.dump_schemas()
```

Methods complete with their parentheses. Shell API methods complete in snake_case, which is the naming style of the Python API.

## Name Cache

SQL completion of object names doesn't query the server on each **Tab**. Instead, the shell keeps a cache of names and fills it at these moments:

* When the global session opens in an interactive shell.
* When you change the default schema with `\use` or with the SQL statement `USE`.
* When you run `\rehash`.

When the cache is filled, the shell prints a line such as the following. Press **Ctrl+C** to stop the load if it takes too long:

```text
Fetching global names, object names from `shop` for auto-completion... Press ^C to stop.
```

The cache holds two kinds of names:

* **Global names**: schemas, storage engines, character sets, collations, system variables, user-defined functions, plugins, and accounts the session can read.
* **Objects of the default schema**: tables, views, their columns, stored functions and procedures, events, and triggers.

Objects in other schemas aren't loaded, so after `FROM sakila.` table names of `sakila` complete only after you make `sakila` the default schema. The cache also doesn't follow changes made by you or others: after `CREATE TABLE` or `DROP TABLE`, run `\rehash` to update it.

{% hint style="info" %}
Loading the cache runs queries against `INFORMATION_SCHEMA`. On a server with tens of thousands of tables in the default schema, this takes noticeable time on each connect and each `\use`. In that case, turn automatic loading off and run `\rehash` when you need it.
{% endhint %}

### Turning Automatic Loading Off

| Method | Effect |
| --- | --- |
| `-A` or `--no-name-cache` | Starts the shell without automatic cache loading. Keywords still complete, and `\rehash` loads the names on demand. |
| `--name-cache` | Turns automatic loading on. Use it to override `autocomplete.nameCache` set to `false` in the configuration. |
| `autocomplete.nameCache` option | `true` loads the cache automatically, `false` doesn't. Persist it with `\option --persist autocomplete.nameCache false`. |

```sh
mariadb-shell -A mariadb://dba@db1.example.com/warehouse
```

When standard input or standard output isn't a terminal, such as in batch mode or when you pipe the output into another program, completion can't be used and the shell doesn't load the cache, unless you request it explicitly with `--name-cache`.

### Refreshing the Cache

`\rehash` reloads the global names and the objects of the current default schema. It works whether automatic loading is on or off:

```text
MariaDB localhost:3306 ssl  shop  SQL > CREATE TABLE supplier (id INT PRIMARY KEY, name VARCHAR(80));
MariaDB localhost:3306 ssl  shop  SQL > \rehash
Fetching global names, object names from `shop` for auto-completion... Press ^C to stop.
```

In Python mode, `\rehash` loads only the schema names.
