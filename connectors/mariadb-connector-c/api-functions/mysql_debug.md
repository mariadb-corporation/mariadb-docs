---
description: >-
  mysql_debug enables debug output for a MariaDB Connector/C client using the
  DBUG library, accepting a colon-separated control string to configure trace
  and logging options.
---

# mysql\_debug

## Syntax

```c
void mysql_debug(const char * debug);
```

* `debug` - a string representing the debug operation to perform. See description below.

## Description

Enables debug output for development and debug purposes by using Fred Fish's DBUG library. For using this function the mariadb-client library must be compiled with debug support.

Almost all MariaDB binaries use the DBUG library and one can get a trace of the program execution by using the [--debug](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#debug) command line option with the binary. This will only work if the binary is compiled for debugging (compiler option `-DDBUG_ON`).

Returns void.

The debug control string is a sequence of colon separated fields as follows:

```c
field_1:field_2:field_n
```

Each field consists of a mandatory flag character followed by an optional "," and comma separated list of modifiers:

```c
flag[,modifier,modifier,...,modifier]
```

The currently recognized flag characters are:

| Option | Description                                                                                                                                                                                                                                                                  |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| d      | Enable output from DBUG\_ macros for the current state. May be followed by a list of keywords which selects output only for the DBUG macros with that keyword. A null list of keywords implies output for all macros.                                                        |
| D      | Delay after each debugger output line. The argument is the number of tenths of seconds to delay, subject to machine capabilities. I.E. -#D,20 is delay two seconds.                                                                                                          |
| f      | Limit debugging and/or tracing, and profiling to the list of named functions. Note that a null list will disable all functions. The appropriate "d" or "t" flags must still be given, this flag only limits their actions if they are enabled.                               |
| F      | Identify the source file name for each line of debug or trace output.                                                                                                                                                                                                        |
| i      | Identify the process with the pid for each line of debug or trace output.                                                                                                                                                                                                    |
| g      | Enable profiling. Create a file called 'dbugmon.out' containing information that can be used to profile the program. May be followed by a list of keywords that select profiling only for the functions in that list. A null list implies that all functions are considered. |
| L      | Identify the source file line number for each line of debug or trace output.                                                                                                                                                                                                 |
| n      | Print the current function nesting depth for each line of debug or trace output.                                                                                                                                                                                             |
| N      | Number each line of dbug output.                                                                                                                                                                                                                                             |
| o      | Redirect the debugger output stream to the specified file. The default output is stderr.                                                                                                                                                                                     |
| O      | As o but the file is really flushed between each write. When needed the file is closed and reopened between each write.                                                                                                                                                      |
| a      | Like o, but opens for append.                                                                                                                                                                                                                                                |
| A      | Like O, but opens for append.                                                                                                                                                                                                                                                |
| p      | Limit debugger actions to specified processes. A process must be identified with the DBUG\_PROCESS macro and match one in the list for debugger actions to occur.                                                                                                            |
| P      | Print the current process name for each line of debug or trace output.                                                                                                                                                                                                       |
| r      | When pushing a new state, do not inherit the previous state's function nesting level. Useful when the output is to start at the left margin.                                                                                                                                 |
| S      | Do function \_sanity(_file_,_line_) at each debugged function until \_sanity() returns something that differs from 0. (Mostly used with safemalloc)                                                                                                                          |
| t      | Enable function call/exit trace lines. May be followed by a list (containing only one modifier) giving a numeric maximum trace level, beyond which no output will occur for either debugging or tracing macros. The default is a compile time option.                        |

{% hint style="info" %}
Instead of using the mysql\_debug() function you also can set the environment variable MYSQL\_DEBUG\\

Enabling generation of debug information slows down the overall performance and generates huge files. In case you need debug information only for special places you can disable the generation of debug information by using mysql\_debug\_end().
{% endhint %}

{% hint style="info" %}
This function is deprecated and not supported anymore.
{% endhint %}

## See Also

* mysql\_debug\_end()
* [mysql\_dump\_debug\_info()](mysql_dump_debug_info.md)

{% @marketo/form formId="4316" %}
