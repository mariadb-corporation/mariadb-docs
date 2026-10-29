---
description: >-
  Plugin API reference: Plugin Verification . Generated from the MariaDB server headers by doxygen and moxygen.
---

# Plugin Verification 

When a dynamically-loaded [Plugin Library](page-concepts.md#plugin-library) is loaded into the server, the server will verify if it is compatible with it before proceeding any further. This is important since the plugin API expects certain data structures to be laid out in a certain way so that the plugin can function correctly.

## Plugin Version Verification
The server will read plugin's symbol `_maria_plugin_interface_version_` (as defined by [maria_declare_plugin](api.md#maria_declare_plugin)) and compare that with its own plugin API version. Loading is refused if the plugin's interface version is older than the minimum the server supports, or if its major version is newer than the server's. If the version differs but is accepted, the server also reads `_maria_sizeof_struct_st_plugin_` to handle the older [st_maria_plugin](plugin_declaration.md#st_maria_plugin) layout.

