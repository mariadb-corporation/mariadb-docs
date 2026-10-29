---
description: >-
  Plugin API reference: How to make a plugin . Generated from the MariaDB server headers by doxygen and moxygen.
---

# How to make a plugin 

This is a tutorial and a walk-through on how to bootstrap, implement, compile, test and distribute a MariaDB [Plugin Library](page-concepts.md#plugin-library).

## Architecture and Design Decisions.
The most important architectural decision is to decide what [Plugin API](page-concepts.md#plugin-api) to implement. To make that determination you need to understand when your plugin needs to be called by the server and with what parameters.

Sometimes just the base [st_maria_plugin](plugin_declaration.md#st_maria_plugin) API is good enough. [st_maria_plugin::init](plugin_declaration.md#init-1) is called when the plugin is loaded and [st_maria_plugin::deinit](plugin_declaration.md#deinit-1) is called when the plugin is unloaded. This will suffice if you are after implementing e.g. a network listener: you can start a background thread that listens for connections and processes connects, disconnects and commands in [st_maria_plugin::init](plugin_declaration.md#init-1). And then signal to it to shut down gracefully from [st_maria_plugin::deinit](plugin_declaration.md#deinit-1).

In this case you implement the so called [Daemon Plugin](daemon_plugin_data.md). This has no API whatsoever. Just a version.

But, in general, you need to understand the available [Plugin Types](plugin_types.md) and decide on implementing the one that suits your needs best.

Do you want to provide a better password validation method? Look into [Password Validation Plugin](password_validation_plugin_data.md). Need to expose data in tabular format to server? Do a [Information Schema Plugin](information_schema_plugin_data.md).

The good part is that you can actually combine multiple [Plugin](page-concepts.md#plugin) into a single [Plugin Library](page-concepts.md#plugin-library).

So, back to the example above, if you need to implement a network listener, but also return the current connection table as an INFORMATION_SCHEMA table you can define the two [Plugin](page-concepts.md#plugin) implementations into your single [Plugin Library](page-concepts.md#plugin-library).

## Code your plugin library
It's easiest to just take one of the existing plugins and copy its code.

But, in case you want to start afresh, here's a very minimal boilerplate to copy from 
```cpp
#include <mysql/plugin.h>
/* TODO: if needed: #include <mysql/specific plugin type, e.g. plugin_audit.h> */

static int plugin_one_init(void *)
{
  /* TODO: code here */
  return 0; /* success */
}

static int plugin_one_deinit(void *)
{
  /* TODO: code here */
  return 0; /* success */
}

static struct st_mysql_daemon plugin_one =
{ MYSQL_DAEMON_INTERFACE_VERSION  };

maria_declare_plugin(plugin_one)
{
  MYSQL_DAEMON_PLUGIN,
  &plugin_one,
  "plugin example",
  "You",
  "A boilerplate plugin code",
  PLUGIN_LICENSE_GPL,
  plugin_one_init,            /* Plugin Init */
  plugin_one_deinit,          /* Plugin Deinit */
  0x0100,                     /* 1.0 */
  NULL,                       /* status variables */
  NULL,                       /* system variables */
  "1.0",                      /* string version */
  MariaDB_PLUGIN_MATURITY_EXPERIMENTAL /* maturity */
}
maria_declare_plugin_end;
```

**See also**: [maria_declare_plugin](api.md#maria_declare_plugin), [maria_declare_plugin_end](api.md#maria_declare_plugin_end), [MYSQL_DAEMON_PLUGIN](api.md#mysql_daemon_plugin), [MYSQL_DAEMON_INTERFACE_VERSION](api.md#mysql_daemon_interface_version), [PLUGIN_LICENSE_GPL](api.md#plugin_license_gpl), [MariaDB_PLUGIN_MATURITY_EXPERIMENTAL](api.md#mariadb_plugin_maturity_experimental)

If you need to add system variables, you can add the following to the above:

```cpp
 static unsigned int v1;

 static int
 v1_check_function(MYSQL_THD thd,
                   struct st_mysql_sys_var *var,
                   void *save, struct st_mysql_value *value) {
   /* TODO: code here, enhance the below */
   long long v;
   if (value->val_int(value, &v))
     return 1; /* FAILURE */
   *(unsigned int*) save= (unsigned int) v;
   return 0; /* OK */
 }
 static void
 v1_update_function(MYSQL_THD thd,
                    struct st_mysql_sys_var *var,
                    void *var_ptr, const void *save) {
   /* TODO: code here */
 }

 static MYSQL_SYSVAR_UINT(
  v1,           /* SQL variable name */
  v1,           /* local C variable reference */
  PLUGIN_VAR_RQCMDARG,    /* flags: An argument is required */
      "gizmo variable", /* SQL visible description */
  v1_check_function,
  v1_update_function,
      0,                      /* default value */
  0,                      /* minimal value */
  365*100,                /* maximum value */
  1         /* increase step */
);

static struct st_mysql_sys_var* sysvars[]= {
  MYSQL_SYSVAR(v1),   /* variable reference */
  NULL                /* terminator. keep */
};
```

And then pass on the `sysvars` to the [maria_declare_plugin](api.md#maria_declare_plugin) 's system variable placeholder.

**See also**: [MYSQL_SYSVAR_UINT](api.md#mysql_sysvar_uint), [mysql_var_check_func](api.md#mysql_var_check_func), [mysql_var_update_func](api.md#mysql_var_update_func), [MYSQL_SYSVAR](api.md#mysql_sysvar)

Similarly, if you need status variables, you can add the following:

```cpp
static volatile int var_s1;
static struct st_mysql_show_var status_vars[]=
{
  {
    "s1",               /* status variable SQL name */
    (char *) &var_s1,   /* reference to the C variable */
    SHOW_INT            /* type */
  },
  { 0, 0, SHOW_UNDEF}   /* terminator. keep */
};
```

And then pass on the `status_vars` to the [maria_declare_plugin](api.md#maria_declare_plugin) 's status variable placeholder.

**See also**: [st_mysql_show_var](plugin_status_vars.md#st_mysql_show_var), [SHOW_INT](api.md#show_int)

