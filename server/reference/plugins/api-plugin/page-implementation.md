---
description: >-
  Plugin API reference: Plugin API Implementation . Generated from the MariaDB server headers by doxygen and moxygen.
---

# Plugin API Implementation 

This is how the individual abstract concepts are implemented and interact with each other.

## The Server Plugin API implementation
The server is the bedrock of the plugin infrastructure and contains the base implementation to enable plugin usage. Plugins can theoretically be loaded into other binaries, but chances are that they won't operate all that well (if at all) in this case since they heavily depend on server's infrastructure.

Here's what the server implements to support plugins:

### The Global Plugin List
The server maintains a global in-memory list of all available plugins (plugin_array), mirrored into a set of hash tables (plugin_hash) and guarded by LOCK_plugin.

The plugin libraries containing the available plugins can be:

* statically linked into the server binary
* dynamically loaded at startup via the &ndash;plugin-load... command line arguments
* dynamically loaded just prior to the server's commencement of normal operations from the mysql.plugin table.
* dynamically loaded at runtime via the INSTALL PLUGIN SQL command.
* unloaded at runtime via the UNINSTALL PLUGIN SQL command
* unloaded at server shutdown

The server implements all of the above possibilities in its code.

It also implements and provides a list of interfaces the plugins can use to call back and interact with the server. These are called [Plugin Services Implementation](#plugin-services-implementation).

The list and some basic attributes for each plugin in it are visible via the INFORMATION_SCHEMA.plugins table.

### How Does The Server Call a Plugin API.
At certain opportune stages of server's normal operation the server might decide to "reach out" to a plugin by calling a plugin API. Since the plugins are named it can call any individual plugin by name. E.g. when executing `CREATE TABLE engine=foo`, the server will:

* look "foo" into the cache of plugin "references" (plugin_ref) for that plugin type, if available.
* If no cached reference is found:
  * Take LOCK_plugin
  * Look "foo" up into the global plugin_array for implementations of the specific plugin API (storage engine in this case)
  * If found, create a reference (plugin_ref) to the plugin.
* call API "method" (function pointers) through the plugin_ref, if found.
* when done, either store the plugin_ref into a cache for reuse or release it.

## Plugin Services Implementation
Every dynamic plugin exposes one symbol for every service it knows about. These are implemented by the `libservices` static library that is linked into every plugin.

Initially, these global pointers are not valid pointers: when the plugin is compiled, they are set to the service version (e.g. VERSION_base64) that the plugin expects. The service header also contains a definition of a more concrete data structure (e.g. [base64_service_st](plugin_api_service_base64.md#base64_service_st)) that this global pointer should be pointing to.

The server maintains a global named list of plugin service API implementations. Every time a [Plugin Library](page-concepts.md#plugin-library) is initialized, the server gets its global service API implementation list, looks up all the symbols exported by the [Plugin Library](page-concepts.md#plugin-library), and, for each symbol:

* checks the versions by comparing the symbol's value to the server version.
* sets [Plugin Library](page-concepts.md#plugin-library) 's symbol value to the actual server service pointer.

Each service header also contains "syntax sugar" macros, e.g.

```cpp
#define my_base64_encode(A,B,C) base64_service->base64_encode_ptr(A,B,C)
```

that allow successful compilation of

```cpp
my_base64_encode(x,y,z)
```
 as a function pointer call through the [Plugin Library](page-concepts.md#plugin-library) 's service pointer.

**See also**: [Plugin Services](plugin_api_services.md) for a list of the services provided by the server.

## The Plugin library Implementation
A [Plugin Library](page-concepts.md#plugin-library) is executable code, either a part of the server itself or bundled as a shared library.

Each plugin library implements the plugin library API. It exposes that implementation via a set of dynamic library symbols.

### Statically Linked Plugin Libraries.
Plugins linked statically to the server are collected into a global server "plugin library" and "installed" (and initialized) at server startup.

### Dynamic Plugin Libraries
A [Plugin Library](page-concepts.md#plugin-library) is usually compiled as OS dynamic library: DLLs on MS Windows, .so on Unixes. What differentiates a [Plugin Library](page-concepts.md#plugin-library) from a regular OS shared library is that it exposes a specific public symbol *maria_plugin_declarations* that the server recognizes. In fact it also exposes *maria_plugin_interface_version* and *maria_sizeof_struct_st_plugin*, but these are auxiliary.

See [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin) for details on how this is implemented.

### The Lifecycle Of a Plugin Library
A plugin library always provides an array of [st_maria_plugin](plugin_declaration.md#st_maria_plugin) structures, each describing a [Plugin](page-concepts.md#plugin) this [Plugin Library](page-concepts.md#plugin-library) provides. This contains everything that goes between [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin) and [maria_declare_plugin_end](plugin_declaration.md#maria_declare_plugin_end) in plugin declaration.

When the [Plugin Library](page-concepts.md#plugin-library) is loaded into the server:

* the library is version and maturity checked. **See also**: [Plugin Verification](page-plugin_verification.md)

* for each [Plugin](page-concepts.md#plugin) contained
  * plugin API version check is performed
  * the plugin system variables are added the variable global lists
  * the plugin is initialized
  * the status variables are added to the variable global lists
  * the plugin is added into the global plugin_array.

At unload time the effect of plugin library load above is reversed.

## Plugin implementation
A MariaDB plugin is a logical, versioned implementation of exactly two interfaces:

* The base, house-keeping [st_maria_plugin](plugin_declaration.md#st_maria_plugin) plugin management interface
* A specific plugin interface, one of [Plugin Types](plugin_types.md). This is referenced by the [st_maria_plugin::info](plugin_declaration.md#info-1) pointer of the [st_maria_plugin](plugin_declaration.md#st_maria_plugin) structure.

## Plugin System Variables Implementation
Broadly speaking the [Plugin System Variables](page-concepts.md#plugin-system-variables) are a property of the [st_maria_plugin](plugin_declaration.md#st_maria_plugin) interface that every plugin exposes. They are assigned to the [st_maria_plugin::system_vars](plugin_declaration.md#system_vars-1) member. When the plugin is loaded the data in that NULL-terminated C++ array are used to register the system variables into the server. And also to unregister them at plugin unload time.

The plugin macros [Plugin System Variable Macros](plugin_sysvar_macros.md), [Plugin Session-Local System Variable Macros](plugin_thdvar_macros.md) and [MYSQL_SYSVAR](implementation_only_plugin_vars.md#mysql_sysvar) facilitate defining an array of `st_mysql_sys_var` system variable definitions that is then passed as a value initializer to [st_maria_plugin::system_vars](plugin_declaration.md#system_vars-1) member when defining the plugin.

But before we can examine more practical examples, there are some important decisions to make about each system variable: its type and settability cases.

### Decide on Data Type and Settability.

#### Pick a Data Type
The data types available are listed in the [Plugin System Variable Types](plugin_sysvar_types.md) group. Pick the one that matches your configuration option best.

#### Pick Settability
You need to decide if the system variable should just be a global variable or if it also should have a per-session value.

The global variable represents a single variable instance, containing a single value, shared across all worker threads inside the server. Think global scope C/C++ variables.

The per-session variable, in addition to what the global variable does, will also allow:

* lock-free access to the session value.
* Every session having a different value for this variable, that is defaulted to the current value of the global variable at session creation time.

See the corresponding server reference manual chapter on system variables for more details on this.

### Check and Update Callbacks

#### The Check Callback
This callback (if non-`NULL`) is called by the server **before** the variable value is set. See [mysql_var_check_func](plugin_sys_vars.md#mysql_var_check_func) for the parameters of the callback. This is the plugin author's chance to check the new value and return an error if it cannot or should not be set.

This callback is expected to:

* inspect the value passed to it
* apply validity constraints (e.g. limits), if any to the value.
* convert it to the correct native C type (see [Plugin System Variable Types](plugin_sysvar_types.md)) for the destination value.
* store it (in native C format) into the temp storage the save pointer points to

If no callback is supplied the server adds its own for each system variable type supported.

A very simple check function for the [PLUGIN_VAR_DOUBLE](plugin_sysvar_types.md#plugin_var_double) type is shown below:

```cpp
static int check_func_double(THD *thd, struct st_mysql_sys_var *var,
                             void *save, st_mysql_value *value)
{
  double v;
  const double v_max = 100.0, v_min=-100.0;

  if (value->val_real(value, &v))
    return 1;
  if (v < v_min || v > v_max)
    return 1;
  *(double *) save= v;

  return 0;
}
```

#### The Update Callback
This callback (if non-`NULL`) is called by the server to set the new value into the variable. See [mysql_var_update_func](plugin_sys_vars.md#mysql_var_update_func) for the parameters to the callback.

The plugin author should implement that if they want to have more control over how the variable is set. E.g. if they want to store the value into an atomic variable they will need the update callback.

Another reason to implement is to invoke any side effects on setting the variable. E.g. if a new value for a temp cache size is set, the code would need to actually resize the global cache list to the new size in addition to storing the new size value.

This callback is expected to:

* fetch the value to be set stored by [The Check Callback](#the-check-callback)
* store it into the variable pointed to by the `var_ptr` pointer argument

If no callback is supplied the server adds its own for each system variable type supported.

A very simple update function for the [PLUGIN_VAR_DOUBLE](plugin_sysvar_types.md#plugin_var_double) type is shown below:

```cpp
static void update_func_double(THD *thd, struct st_mysql_sys_var *var,
                               void *tgt, const void *save)
{
  *(double *) tgt= *(double *) save;
}
```

### Define a Global Variable
To define a global only variable, do as follows:

* Define the C++ global variable. Use the variable type for your selected type mentioned in [Plugin System Variable Types](plugin_sysvar_types.md), e.g. 
```cpp
char *var1_var;
char default_var1_var[]= "var1 default";
...
```
* Use one of the [Plugin System Variable Macros](plugin_sysvar_macros.md) to declare the variable, e.g. 
```cpp
static MYSQL_SYSVAR_STR(var1, var1_var, PLUGIN_VAR_RQCMDARG,
 "Variable 1", NULL, NULL, default_var1_var);
```
* Add the variable to a global per-plugin NULL terminated C++ array using [MYSQL_SYSVAR](implementation_only_plugin_vars.md#mysql_sysvar), e.g. 
```cpp
 static struct st_mysql_sys_var* vars[] = {
...
MYSQL_SYSVAR(var1),
...
NULL
 };
```
* Pass the array to [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin), e.g. 
```cpp
maria_declare_plugin(innobase)
{
  MYSQL_STORAGE_ENGINE_PLUGIN,
  &innobase_storage_engine,
  innobase_hton_name,
  plugin_author,
  "Supports transactions, row-level locking, foreign keys and encryption for tables",
  PLUGIN_LICENSE_GPL,
  innodb_init, // Plugin Init
  NULL, // Plugin Deinit
  MYSQL_VERSION_MAJOR << 8 | MYSQL_VERSION_MINOR,
  innodb_status_variables_export, // status variables
  vars,   // system variables
  PACKAGE_VERSION,
  MariaDB_PLUGIN_MATURITY_STABLE // maturity
}
```

### Define a Session Variable
Unlike the global ones, session variables do not need a C++ placeholder variable. The global value is stored within a global server data structure. And the values for each session are stored into a per-session data structure, owned by the [MYSQL_THD](plugin_api.md#mysql_thd) structure.

This also means that you will need to use the [THDVAR](plugin_sys_vars.md#thdvar) macro to access both the global (pass `NULL` to the first [MYSQL_THD](plugin_api.md#mysql_thd) argument) and the per-session values.

Example:

```cpp
static MYSQL_THDVAR_INT(tvar, ...);
...
// Get and set the global value
int val = THDVAR(NULL, tvar);
THDVAR(NULL, tvar)= 12;
...
// Get and set the per-thread value
MYSQL_THD thd = ...
int val = THDVAR(thd, tvar);
THDVAR(thd, tvar)= 42;
...
```

To define a global+session variable do as follows:

* Define the variable using one of the [Plugin Session-Local System Variable Macros](plugin_thdvar_macros.md), e.g.: 
```cpp
static MYSQL_THDVAR_INT(tvar,
  PLUGIN_VAR_RQCMDARG, // flags
  "Default depth used by Json, XML and Mongo discovery", // comment
  NULL, // check
  NULL, // update
  5, // default
  -1, // min
  16, // max
  1); // block.
```
* Add the variable to a global per-plugin NULL terminated C++ array using [MYSQL_SYSVAR](implementation_only_plugin_vars.md#mysql_sysvar), e.g. 
```cpp
static struct st_mysql_sys_var* vars[] = {
   ...
   MYSQL_SYSVAR(tvar),
   ...
   NULL
};
```
* Pass the array to [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin), e.g. 
```cpp
maria_declare_plugin(innobase)
{
  MYSQL_STORAGE_ENGINE_PLUGIN,
  &innobase_storage_engine,
  innobase_hton_name,
  plugin_author,
  "Supports transactions, row-level locking, foreign keys and encryption for tables",
  PLUGIN_LICENSE_GPL,
  innodb_init, // Plugin Init
  NULL, // Plugin Deinit
  MYSQL_VERSION_MAJOR << 8 | MYSQL_VERSION_MINOR,
  innodb_status_variables_export, // status variables
  vars,   // system variables
  PACKAGE_VERSION,
  MariaDB_PLUGIN_MATURITY_STABLE // maturity
}
```

  > [!NOTE]
  > You can mix global and session variables into a single array.

## Plugin Status Variables Implementation
[Plugin Status Variables](page-concepts.md#plugin-status-variables) are defined similarly to [Plugin System Variables](page-concepts.md#plugin-system-variables) by creating a per-plugin `NULL` terminated array of [st_mysql_show_var](plugin_status_vars.md#st_mysql_show_var) structures and passing it down to [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin).

Unlike the system variables, the status variables are read-only, i.e. only the plugin code can manipulate the status variable's value.

Each status variable has a type: one of the [enum_mysql_show_type](plugin_status_vars.md#enum_mysql_show_type) types. In practice try to restrict your variables to use either [SHOW_LONG](plugin_status_vars.md#show_long) or [SHOW_LONGLONG](plugin_status_vars.md#show_longlong). These are typically counters and these two types get reset by the server when you reset status. Plus, they are typically accessed atomically by modern CPUs so you can skip doing locking.

The scope for the status variables is handled by the server as follows: Plugin status variables are global: the server reads the variable the pointer refers to. If you need per-session values, use a [SHOW_FUNC](plugin_status_vars.md#enum_mysql_show_type) or [SHOW_SIMPLE_FUNC](plugin_status_vars.md#enum_mysql_show_type) variable and compute the value from the THD.

Status variables can be scalar or functional.

### Scalar Status Variables
For "scalar" status variables the data is kept into a C/C++ variable and a pointer to that is passed to the infrastructure. When the server needs to read the value it just de-references the pointer and reads the value.

To implement a scalar status variable do as follows:

* Define the global counter variable 
```cpp
unsigned long long stat_var_buffer;
```
* Add it to a global per-plugin NULL-element terminated array: 
```cpp
static struct st_mysql_show_var status_variables[]= {
  ...
  {"stat_var", (char *) &stat_var_buffer, SHOW_LONGLONG},
  ...
  {NullS, NullS, SHOW_LONG}};
```
* Pass the global array to [maria_declare_plugin](plugin_declaration.md#maria_declare_plugin) : 
```cpp
maria_declare_plugin(innobase)
{
  MYSQL_STORAGE_ENGINE_PLUGIN,
  &innobase_storage_engine,
  innobase_hton_name,
  plugin_author,
  "Supports transactions, row-level locking, foreign keys and encryption for tables",
  PLUGIN_LICENSE_GPL,
  innodb_init, // Plugin Init
  NULL, // Plugin Deinit
  MYSQL_VERSION_MAJOR << 8 | MYSQL_VERSION_MINOR,
  status_variables, // status variables
  vars,   // system variables
  PACKAGE_VERSION,
  MariaDB_PLUGIN_MATURITY_STABLE // maturity
}
```
* Manipulate the global counter variable 
```cpp
stat_var_buffer++;
```

### Functional Status Variables
For functional status variables instead of dereferencing a pointer, the server takes a function pointer of the type [mysql_show_var_func](plugin_status_vars.md#mysql_show_var_func) and is calling the function when it needs the value.

The function can also change the type for the variable.

A typical [SHOW_SIMPLE_FUNC](plugin_status_vars.md#enum_mysql_show_type) variable looks like this: 
```cpp
static int show_func_example(MYSQL_THD thd, struct st_mysql_show_var *var,
                         void *buf, system_status_var *, enum_var_type)
{
  var->type= SHOW_CHAR;
  var->value= buf; // it's of SHOW_VAR_FUNC_BUFF_SIZE bytes
  my_snprintf((char*) buf, SHOW_VAR_FUNC_BUFF_SIZE,
          ...);
  return 0;
}
...
static struct st_mysql_show_var func_status[]=
{
  {"func_example",  (char *)show_func_example, SHOW_SIMPLE_FUNC},
  {0,0,SHOW_UNDEF}
};
```

There's also [SHOW_FUNC](plugin_status_vars.md#enum_mysql_show_type), which you can use through the SHOW_FUNC_ENTRY macro as follows: 
```cpp
static int show_value(THD *thd, SHOW_VAR *var, void *buff,
                       system_status_var *, enum_var_type scope)
{
  var->type= SHOW_ULONGLONG;
  var->value= buff;
  *(ulonglong*) buff= 0;
  return 0;
}
...
static struct st_mysql_show_var func_status[]=
{
  SHOW_FUNC_ENTRY("show_value", &show_value),
  {0,0,SHOW_UNDEF}
};
```

### Array Status Variables
Sometimes you want a group of status variables to have a custom prefix.

One approach is to copy that prefix to all the variables in the list, e.g. 
```cpp
struct st_mysql_show_var status_variables[] = {
  {"prefix_var1", (char *) &var1, SHOW_LONGLONG},
  {"prefix_var2", (char *) &var2, SHOW_LONGLONG},
  {NullS, NullS, SHOW_LONG}
};
```

This can be tedious, so MariaDB supports a trick to specify the prefix just once:

```cpp
struct st_mysql_show_var plugin_variables[] = {
  {"var1", (char *) &var1, SHOW_LONGLONG},
  {"var2", (char *) &var2, SHOW_LONGLONG},
  {NullS, NullS, SHOW_LONG}
};

static int show_plugin_vars(THD *thd, SHOW_VAR *var, void *buff,
                         struct system_status_var *,
                         enum enum_var_type) {
  var->type = SHOW_ARRAY;
  var->value = reinterpret_cast<char *>(&plugin_variables);
  return 0;
}

struct st_mysql_show_var status_variables[] = {
  SHOW_FUNC_ENTRY("prefix", &show_plugin_vars),
  {NullS, NullS, SHOW_LONG}
};
```

Here the [SHOW_FUNC](plugin_status_vars.md#enum_mysql_show_type) entry returns a [SHOW_ARRAY](plugin_status_vars.md#enum_mysql_show_type), and the server prefixes the names of the array's variables with the entry's name.

