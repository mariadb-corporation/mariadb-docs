---
description: >-
  Plugin API reference: Plugin API Concepts . Generated from the MariaDB server headers by doxygen and moxygen.
---

# Plugin API Concepts 

## The Big Picture: The Server, Plugins and Interfaces
The server does, at certain stages of its execution, call plugin APIs when it needs certain operation performed: e.g. authenticate a user, log a message, read and write from/to a database table etc.

These API are like written functionality contracts. They allow separating the server functionality from the actual API implementations themselves. And, since the API implementations are a dynamic set, adding new implementations extends the server functionality (e.g. adds new ways a user can be authenticated or message be logged) without having to re-compile and even re-start the server itself.

The MariaDB server plugin infrastructure uses the following logical terms:

## Plugin API
A well defined, versioned and stable interface specification. It's also abstract, as it's not tied to any one specific implementation.

## Plugin
A named and versioned implementation of a specific [Plugin API](#plugin-api).

**See also**: [Plugin Types](plugin_types.md) for a list of the available plugin types and what they do

## Plugin Library
(habitually abbreviated as a plugin) An executable binary that contains one or more [Plugin](#plugin) that can be accessed by the server when it needs to call plugin API implementations.

## Plugin Services
Sometimes plugin code needs to call back into the server.

The plugin is running into the same process and the server symbols are not hidden. So it can just reference a server symbol: e.g. call a server function or read a server variable. These will get resolved by the OS's dynamic linker (for dynamic plugins) or static linker (for static plugins).

But this is considered **bad** since there's no guarantee that the plugin's snapshot of what the server symbol is captured during plugin compilation matches the actual server symbol definition inside the running server.

This is why the plugin infrastructure provides a more controlled way for a plugin to call server code.

It's called a plugin service.

Plugin services are a finite set determined at server's and plugin's compile time.

They guarantee that the service is present, matches the definition and is callable after plugin load. They also provide platform independence as they operate the same on all OSes and architectures.

## Plugin System Variables
Plugins can provide their own configuration variables. These become regular server system variables when the plugin is loaded: their values can be stored in config files or passed on the server's command line or via the SET command. When the plugin is unloaded the variables go away with it.

The variable names known to the server are prefixed with the plugin name so that they do not pollute the namespace. E.g. the variable `foo` becomes known to the server as `bar_plugin_foo` when exported by the plugin `bar_plugin`.

Each variable has a declared data type.

Plugin authors must decide if they want to keep a single global value or a per-session value + global value for each variable.

Plugin authors must also decide if they will allow setting the value at runtime or not. And make sure the plugin code is built to handle value changes mid-flight if they allow it.

## Plugin Status Variables
Plugins can also provide their own status variables. Think of status variables as read-only [Plugin System Variables](#plugin-system-variables) that the plugin authors can use to expose volatile data of the plugin state, like e.g. counters, on/off indicators, gauges, progress bars, state names etc.

Status variables are also lighter weight compared to [Plugin System Variables](#plugin-system-variables) : knowing that they're read-only allows better optimization and less locking when handling them. So, if plugin authors can use status variables, it's advisable that they should.

Similarly to system variables, the status variables become known to the server when the plugin is loaded and go away when it's unloaded.

> [!WARNING]
> Status variables are not automatically prefixed with the plugin name! You will need to prefix your status variables with the plugin name. See [Array Status Variables](page-implementation.md#array-status-variables) for a convenient way to do this.

The status variables also have a declared data type.

**See also**: [Plugin API Implementation](page-implementation.md) on how the above concepts are implemented.

