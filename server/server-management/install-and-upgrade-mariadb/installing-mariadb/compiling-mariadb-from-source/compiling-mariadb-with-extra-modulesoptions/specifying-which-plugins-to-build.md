---
description: >-
  Explains how to use CMake options like `PLUGIN_xxx` to control which plugins
  are built statically, dynamically, or not at all during compilation.
---

# Specifying Which Plugins to Build

By default all plugins are enabled and built as dynamic `.so` (or `.dll`) modules. If a plugin does not support dynamic builds, it is not built at all.

Use `PLUGIN_xxx` cmake variables. They can be set on the command line with `-DPLUGIN_xxx=value` or in the cmake gui. Supported values are

| Value     | Effect                                                                                                                                              |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NO`      | the plugin will be not compiled at all                                                                                                              |
| `STATIC`  | the plugin will be compiled statically, if supported. Otherwise it will be not compiled.                                                            |
| `DYNAMIC` | the plugin will be compiled dynamically, if supported. Otherwise it will be not compiled. This is the default behavior.                             |
| `AUTO`    | the plugin will be compiled statically, if supported. Otherwise it will be compiled dynamically.                                                    |
| `YES`     | same as AUTO, but if plugin prerequisites (for example, specific libraries) are missing, it will not be skipped, it will abort cmake with an error. |

Note that unlike autotools, cmake tries to configure and build incrementally. You can modify one configuration option and cmake will only rebuild the part of the tree affected by it. For example, when you do `cmake -DWITH_EMBEDDED_SERVER=1` in the already-built tree, it will make libmysqld to be built, but no other configuration options will be changed or reset to their default values.

In particular this means that if you have run, for example`cmake -DPLUGIN_OQGRAPH=NO`\
and later you want to restore the default behavior (with OQGraph being built) in the same build tree, you would need to run`cmake -DPLUGIN_OQGRAPH=DYNAMIC`

Alternatively, you might simply delete the `CMakeCache.txt` file — this is the file where cmake stores current build configuration — and rebuild everything from scratch.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
