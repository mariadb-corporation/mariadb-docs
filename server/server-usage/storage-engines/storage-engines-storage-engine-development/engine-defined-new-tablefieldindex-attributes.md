# Engine-defined New Table/Field/Index Attributes

In MariaDB, a storage engine can allow the user to specify additional attributes per index, field, or table. The engine needs to declare what attributes it introduces.

## API

There are three new members in the `handlerton` structure, they can be set in the engine's initialization function as follows:

```
example_hton->table_options= example_table_option_array;
example_hton->field_options= example_field_option_array;
example_hton->index_options= example_index_option_array;
```

The arrays are declared statically, as in the following example:

```
static MYSQL_THDVAR_ULONG(varopt_default, PLUGIN_VAR_RQCMDARG,
  "default value of the VAROPT table option", NULL, NULL, 5, 0, 100, 0);

struct ha_table_option_struct
{
  char *strparam;
  ulonglong ullparam;
  uint enumparam;
  bool boolparam;
  ulonglong varparam;
};

ha_create_table_option example_table_option_list[]=
{
  HA_TOPTION_NUMBER("NUMBER", ullparam, UINT_MAX32, 0, UINT_MAX32, 10),
  HA_TOPTION_STRING("STR", strparam),
  HA_TOPTION_ENUM("ONE_OR_TWO", enumparam, "one,two", 0),
  HA_TOPTION_BOOL("YESNO", boolparam, 1),
  HA_TOPTION_SYSVAR("VAROPT", varopt, varparam),
  HA_TOPTION_END
};
```

The engine declares a structure`ha_table_option_struct`\
that will hold values of these new attributes.

And it describes these attributes to MySQL by creating an array of`HA_TOPTION_*` macros. Note a detail: these macros expect a structure called`ha_table_option_struct`, if the structure is called differently, a`#define` are needed.

There are five supported kinds of attributes:

| macro name          | attribure value type                    | corresponding C type           | additional parameters of a macro                                                                                   |
| ------------------- | --------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| macro name          | attribure value type                    | corresponding C type           | additional parameters of a macro                                                                                   |
| HA\_TOPTION\_NUMBER | an integer number                       | unsigned long long             | a default value, minimal allowed value, maximal allowed value, a factor, that any allowed should be a multiple of. |
| HA\_TOPTION\_STRING | a string                                | char \*                        | none. The default value is a null pointer.                                                                         |
| HA\_TOPTION\_ENUM   | one value from a list of allowed values | unsigned int                   | a string with a comma-separated list of allowed values, and a default value as a number, starting from 0.          |
| HA\_TOPTION\_BOOL   | a boolean                               | bool                           | a default value                                                                                                    |
| HA\_TOPTION\_SYSVAR | defined by the system variable          | defined by the system variable | system variable name                                                                                               |

_Do not use_ `enum` _for your_ `HA_TOPTION_ENUM` _C structure members, the size of the_ `enum` _depends on the compiler, and even on the compilation options, and the plugin API uses only types with known storage sizes._

In all macros the first two parameters are name of the attribute as should be used in SQL in the `CREATE TABLE` statement, and the name of the corresponding member of the `ha_table_option_struct` structure.

The `HA_TOPTION_SYSVAR` stands aside a bit. It does not specify the attribute type or the default value, instead it binds the attribute to a system variable. The attribute type and the range of allowed values are the same as of the corresponding system variable. The attribute **default value** are the **current value** of its system variable. And unlike other attribute types that are only stored in the `.frm` file if explicitly set in the `CREATE TABLE` statement, the `HA_TOPTION_SYSVAR` attributes are always stored. If the system variable value is changed, it will not affect existing tables. Note that for this very reason, if a table was created in the old version of a storage engine, and a new version has introduced a `HA_TOPTION_SYSVAR` attribute, the attribute value in the old tables are the **default** value of the system variable, not its **current** value.

The array ends with a `HA_TOPTION_END` macro.

Field and index (key) attributes are declared similarly using `HA_FOPTION_*` and `HA_IOPTION_*` macros.

When in a `CREATE TABLE` statement, the `::create()` handler method is called, the table attributes are available in the `table_arg->s->option_struct`, field attributes - in the `option_struct` member of the individual fields (objects of the `Field` class), index attributes - in the `option_struct` member of the individual keys (objects of the `KEY` class).

Additionally, they are available in most other handler methods: the attributes are stored in the `.frm` file and on every open MySQL makes them available to the engine by filling the corresponding `option_struct` members of the table, fields, and keys.

The `ALTER TABLE` needs a special support from the engine. MySQL compares old and new table definitions to decide whether it needs to rebuild the table or not. As the semantics of the engine declared attributes is unknown, MySQL cannot make this decision by analyzing attribute values - this is delegated to the engine. The `HA_CREATE_INFO` structure has three new members:

```
ha_table_option_struct *option_struct;           ///< structure with parsed table options
ha_field_option_struct **fields_option_struct;   ///< array of field option structures
ha_index_option_struct **indexes_option_struct;  ///< array of index option structures
```

The engine (in the `::check_if_incompatible_data()` method) is responsible for comparing new values of the attributes from the `HA_CREATE_INFO` structure with the old values from the table and returning `COMPATIBLE_DATA_NO` if they were changed in such a way that requires the table to be rebuild.

The example of declaring the attributes and comparing the values for the `ALTER TABLE` can be found in the EXAMPLE engine.

## SQL

The engine declared attributes can be specified per field, index, or table in the `CREATE TABLE` or `ALTER TABLE`. The syntax is the conventional:

```
CREATE TABLE ... (
  field ... [attribute=value [attribute=value ...]],
  ...
  index ... [attribute=value [attribute=value ...]],
  ...
) ...  [attribute=value [attribute=value ...]]
```

All values must be specified as literals, not expressions. The value of a boolean option may be specified as one of YES, NO, ON, OFF, 1, or 0. A string value may be specified either quoted or not, as an identifier (if it is a valid identifier, of course). Compare with the old behavior:

```
CREATE TABLE ... ENGINE=FEDERATED CONNECTION='mysql://root@127.0.0.1';
```

where the value of the ENGINE attribute is specified not quoted, while the value of the CONNECTION is quoted.

When an attribute is set, it are stored with the table definition and shown in the `SHOW CREATE TABLE;`. To remove an attribute from a table definition use `ALTER TABLE` to set its value to a `DEFAULT`.

The values of unknown attributes or attributes with the illegal values cause an error by default. But with [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) one can change the storage engine and some previously valid attributes may become unknown — to the new engine. They are not removed automatically, though, because the table might be altered back to the first engine, and these attributes are valid again. Still [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) will comment these unknown attributes out in the output, otherwise they would make a generated [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement invalid.

With the `IGNORE_BAD_TABLE_OPTIONS` [sql mode](../../../server-management/variables-and-modes/sql_mode.md) this behavior changes. Unknown attributes do not cause an error, they only result in a warning. And [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) will not comment them out. This mode is implicitly enabled in the replication slave thread.

## See Also

* [Writing Plugins for MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/development-writing-plugins-for-mariadb)
* [Storage Engines](../)
* [Storage Engine Development](./)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
