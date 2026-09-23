---
description: >-
  Learn about special module-specific commands in MaxScale. This guide explains
  how to list and execute commands using MaxCtrl for modules like
  authenticators, filters, and monitors.
---

# MaxScale Module Commands

## Module commands

Introduced in MaxScale 2.1, the module commands are special, module-specific commands. They allow the modules to expand beyond the capabilities of the module API. Currently, only MaxCtrl implements an interface to the module commands.

All registered module commands can be shown with `maxctrl list commands`. They can be executed with `maxctrl call command <module> <name> ARGS...`, where `<module>` is the name of the module and `<name>` is the name of the command. `ARGS` is a command-specific list of arguments, separated by spaces.

{% hint style="info" %}
From MaxScale 25.10, the name of a service, filter, or monitor can be used in place of the module name. MaxScale then resolves the module from that object and passes the object as the command's first argument automatically, so the usage is `call command <module|object> <command> [params...]`.

For example, to call the `switchover` command of a `mariadbmon` monitor named `MariaDB-Monitor`:

```bash
maxctrl call command MariaDB-Monitor switchover
```

This is equivalent to the older form, which names the module explicitly and passes the monitor as an argument:

```bash
maxctrl call command mariadbmon switchover MariaDB-Monitor
```

Both forms are supported. The older form is required on MaxScale 25.01 and earlier.
{% endhint %}

### Developer reference

The module command API is defined in the _modulecmd.h_ header. It consists of various functions to register and call module commands. Read the function documentation in the header for more details.

The following example registers the module command _my\_command_ for module\_my\_module\_.

```
#include <maxscale/modulecmd.hh>

bool my_simple_cmd(const MODULECMD_ARG *argv)
{
    printf("%d arguments given\n", argv->argc);
}

int main(int argc, char **argv)
{
    modulecmd_arg_type_t my_args[] =
    {
        {MODULECMD_ARG_BOOLEAN, "This is a boolean parameter"},
        {MODULECMD_ARG_STRING | MODULECMD_ARG_OPTIONAL, "This is an optional string parameter"}
    };

    // Register the command
    modulecmd_register_command("my_module", "my_command", my_simple_cmd, 2, my_args);

    // Find the registered command
    const MODULECMD *cmd = modulecmd_find_command("my_module", "my_command");

    // Parse the arguments for the command
    const void *arglist[] = {"true", "optional string"};
    MODULECMD_ARG *arg = modulecmd_arg_parse(cmd, arglist, 2);

    // Call the module command
    modulecmd_call_command(cmd, arg);

    // Free the parsed arguments
    modulecmd_arg_free(arg);
    return 0;
}
```

The array _my\_args_ of type _modulecmd\_arg\_type\_t_ is used to tell what kinds of arguments the command expects. The first argument is a boolean and the second argument is an optional string.

Arguments are passed to the parsing function as an array of void pointers. They are interpreted as the types the command expects.

When the module command is executed, the _argv_ parameter for the\_my\_simple\_cmd\_ contains the parsed arguments received from the caller of the command.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
