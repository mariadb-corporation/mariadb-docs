---
description: >-
  Plugin API reference: Plugin Services. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin Services

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md)

A set of services provided by the server to plugins. **See also**: [Plugin Services Implementation](page-implementation.md#plugin-services-implementation)

## Groups

| Name | Description |
|------|-------------|
| [`Base64 Service`](plugin_api_service_base64.md) | Base64 service |
| [`Debug Sync Service`](plugin_api_service_debug_sync.md) | Debug Sync service. |
| [`Encryption Service`](plugin_api_service_encryption.md) | Functions to support data encryption and encryption key management. |
| [`Encryption Scheme Service`](plugin_api_service_encryption_scheme.md) | A higher-level access to encryption service. |
| [`JSON Service`](plugin_api_service_json.md) | Exports JSON parsing methods for plugins to use. |
| [`KILL Statement Service`](plugin_api_service_kill_statement.md) | This service provides functions that allow plugins to support the KILL statement. |
| [`Log Warnings Service`](plugin_api_service_log_warnings.md) | This service provides access to the log warning level for the current session. |
| [`Logger Service`](plugin_api_service_logger.md) | Log file with rotation implementation. |
| [`MD5 Service`](plugin_api_service_md5.md) | Functions to calculate MD5 hash from a memory buffer |
| [`My Crypt Service`](plugin_api_service_my_crypt.md) | AES encryption functions, and a function to generate random bytes. |
| [`My Print Error Service`](plugin_api_service_my_print_error.md) | This service provides functions for plugins to report errors to client (without client, the errors are written to the error log). |
| [`my_snprintf Service`](plugin_api_service_my_snprintf.md) | Portable and limited vsnprintf() implementation. |
| [`Print Check Msg Service`](plugin_api_service_print_check_msg.md) | This service provides functions to write messages for check or repair |
| [`Progress Report Service`](plugin_api_service_progress_report.md) | Allows plugins to report progress of long running operations to the server. |
| [`SHA1 Service`](plugin_api_service_sha1.md) | my sha1 service |
| [`SHA2 Service`](plugin_api_service_sha2.md) | my sha2 service |
| [`SQL Service`](plugin_api_service_sql.md) | SQL Service |
| [`THD Service`](plugin_api_service_thd.md) | Access to the current thd |
| [`THD Alloc Service`](plugin_api_service_thd_alloc.md) | This service provides functions to allocate memory in a connection local memory pool |
| [`THD Autoinc Service`](plugin_api_service_thd_autoinc.md) | Access to the auto_increment related system variables. |
| [`THD Error Context Service`](plugin_api_service_thd_error_context.md) | Error context service to access the statement diagnostics area. |
| [`THD MDL Service`](plugin_api_service_thd_mdl.md) | Access to the metadata locks. |
| [`THD RND Service`](plugin_api_service_thd_rnd.md) | Access to the thd-local random number generator. |
| [`THD Specifics Service`](plugin_api_service_thd_specifics.md) | THD specific for plugin(s) |
| [`THD Timezone Service`](plugin_api_service_thd_timezone.md) | THD timezone handling for plugin(s) |
| [`THD Wait Service`](plugin_api_service_thd_wait.md) | This service provides functions for plugins and storage engines to report when they are going to sleep/stall. |

