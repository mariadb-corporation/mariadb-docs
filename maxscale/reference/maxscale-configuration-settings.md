---
description: >-
  Browse the comprehensive list of MariaDB MaxScale configuration parameters.
  This reference details valid values, default settings, and dynamic
  capabilities for servers, services, and monitors.
---

# MaxScale Configuration Settings

## General

### [MaxScale](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md)

#### Filter

[**module**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#module)

* Type: filter
* Mandatory: Yes
* Dynamic: No
* Description: The module parameter specifies the name of the filter module that is included in the routing chain.

#### Global Settings

[**admin\_audit**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables the logging of incoming REST API requests for auditing and monitoring purposes.

[**admin\_audit\_exclude\_methods**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit_exclude_methods)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions
* Description: Provides a list of HTTP methods to be excluded from REST API audit logging, separated by commas.

[**admin\_audit\_file**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`&#x20;
* Description: Defines the location of the REST API audit logs.

[**admin\_auth**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_auth)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Allows HTTP Basic authentication for the REST API.

[**admin\_enabled**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Enables or disables the MaxScale admin interface.

[**admin\_gui**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_gui)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Enables or disables the graphical user interface (GUI) for the admin interface.

[**admin\_host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_host)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`&#x20;
* Description: Provides the network interface address that the REST API is listening to.

[**admin\_jwt\_algorithm**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_algorithm)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`&#x20;
* Description: Specifies the algorithm for signing JSON Web Tokens (JWTs) for the REST API.

[**admin\_jwt\_issuer**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_issuer)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`&#x20;
* Description: Specifies the issuer ("iss") claim in the REST API-generated JSON Web Tokens.&#x20;

[**admin\_jwt\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_key)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Identifies the encryption key that is used to sign JSON Web Tokens.

[**admin\_jwt\_max\_age**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_max_age)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `24h`&#x20;
* Description: Specifies the maximum duration of JWTs issued by the REST API.

[**admin\_log\_auth\_failures**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_log_auth_failures)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Enables logging of authentication failures for the admin interface.

[**admin\_oidc\_client\_id**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_id)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the client ID for OpenID Connect (OIDC) login authentication requests.

[**admin\_oidc\_client\_secret**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_secret)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the client secret used for OIDC authentication requests.

[**admin\_oidc\_extra\_options**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_extra_options)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""` &#x20;
* Description: Defines additional parameters that should be included in authorization requests for OIDC. &#x20;

[**admin\_oidc\_flow**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_flow)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `auto`, `implicit`, `code`
* Default: `auto`&#x20;
* Description: Describes the OIDC authentication flow used for SSO.

[**admin\_oidc\_ssl\_insecure**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_ssl_insecure)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Disables TLS certificate validation while retrieving OIDC certificates.

[**admin\_oidc\_url**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_url)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the OIDC provider's URL, which is needed to validate JWT.

[**admin\_pam\_readonly\_service**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_pam_readonly_service)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines the PAM service that is used to verify read-only REST API users.

[**admin\_pam\_readwrite\_service**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_pam_readwrite_service)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the PAM service used for authentication REST API users with read and write access.

[**admin\_port**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_port)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`&#x20;
* Description: Defines the port at which the REST API waits for incoming connections.

[**admin\_readwrite\_hosts**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_readwrite_hosts)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`

[**admin\_secure\_gui**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_secure_gui)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cipher**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cipher)

* Type: string
* Mandatory: No
* Dynamic: No

[**admin\_ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_passphrase**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_passphrase)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**admin\_ssl\_version**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_version)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

[**admin\_verify\_url**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_verify_url)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;

**allow\_duplicate\_servers**

* Type: boolean
* Default: false
* Description: Allows multiple server definitions to use the same IP address and port combination.

[**auth\_connect\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_connect_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**auto\_tune**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No

[**config\_sync\_cluster**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_cluster)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_db**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_db)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`

[**config\_sync\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`

[**config\_sync\_password**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_password)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**config\_sync\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connector\_plugindir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connector_plugindir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**core\_file**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#core_file)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No

**cors\_allow\_origin**

* Type: string
* Default: N/A
* Description: Enables CORS and sets the `Access-Control-Allow-Origin` header to the specified value.

[**datadir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#datadir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`

[**debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#debug)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;

**disable\_fcrdns**

* Type: boolean
* Default: false
* Description: Disables Forward-Confirmed Reverse DNS (fcRDNS) lookups for client connections.

**disable\_module\_unloading**

* Type: boolean
* Default: false
* Description: Disables the unloading of modules at exit. This provides more accurate Valgrind leak reports when memory is allocated within shared libraries.

**disable\_statement\_logging**

* Type: boolean
* Default: true
* Description: Disables the logging of SQL statements sent by MaxScale to backend servers.

[**dump\_last\_statements**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#dump_last_statements)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`&#x20;

**dump\_network\_traffic**

* Type: boolean
* Default: false
* Description: Dumps all raw network traffic to the log as `info` level messages.&#x20;

**enable\_cors**

* Type: boolean
* Default: false
* Description: Enables Cross-Origin Resource Sharing (CORS) support for the MaxScale REST API.

**enable\_module\_unloading**

* Type: boolean
* Default: true
* Description: Re-enables module unloading at exit (overrides `disable-module-unloading`)

**enable\_statement\_logging**

* Type: boolean
* Default: false
* Description: Enables logging of all SQL statements sent by MaxScale monitors and authenticators to the backend servers.

**exception\_frequency**

* Type: integer
* Default: true
* Description: Defines the frequency of generated API exceptions.

**gdb\_stacktrace**

* Type: boolean
* Default: true
* Description: When enabled, MaxScale attempts to use GDB to generate detailed stack traces during a crash. Can be disabled with `gdb-stacktrace=false`.

[**host\_cache\_size**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#host_cache_size)

* Type: integer
* Default: 128
* Dynamic: Yes

[**key\_manager**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#key_manager)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`

[**libdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#libdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**load\_persisted\_configs**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#load_persisted_configs)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**local\_address**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#local_address)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**log\_augmentation**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_augmentation)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**log\_debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_throttling**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_throttling)

* Type: number, [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations), [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`

[**log\_warn\_super\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warn_super_user)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**log\_warning**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**logdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#logdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`

[**max\_auth\_errors\_until\_block**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_auth_errors_until_block)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**maxlog**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#maxlog)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**module\_configdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#module_configdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`

[**ms\_timestamp**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ms_timestamp)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**passive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**persist\_runtime\_changes**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persist_runtime_changes)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: No

[**persistdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persistdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`

[**piddir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#piddir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`

[**query\_classifier\_cache\_size**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_classifier_cache_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent

[**query\_retries**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retries)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**query\_retry\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retry_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**rebalance\_period**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_period)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**rebalance\_threshold**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_threshold)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`

[**rebalance\_window**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_window)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`&#x20;

**redirect\_output\_to\_file**

* Type: boolean
* Default: false
* Description: Redirects `stdout` and `stderr` to the specified file path.

[**require\_secure\_transport**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#require_secure_transport)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No

[**retain\_last\_statements**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**secretsdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#secretsdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**session\_trace**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**session\_trace\_match**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sharedir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sharedir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`

[**skip\_name\_resolve**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#skip_name_resolve)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**sql\_mode**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sql_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`&#x20;

**sql\_batch\_size**

* Type: size
* Default: 10MiB
* Description: Sets the maximum batch size for REST API SQL statement processing.

[**substitute\_variables**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#substitute_variables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**syslog**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#syslog)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**telemetry**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**telemetry\_attributes**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_attributes)

* Type: stringlist
* Default: empty
* Dynamic: Yes
* Mandatory: No

[**telemetry\_ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**telemetry\_ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**telemetry\_ssl\_insecure**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_insecure)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**telemetry\_ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**telemetry\_update\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_update_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

[**telemetry\_url**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_url)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `http://localhost:4318/v1/metrics`

[**threads**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads)

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`

[**threads\_max**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads_max)

* Type: positive integer
* Default: 256
* Dynamic: No

[**trace\_file\_dir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_dir)

* Type: path
* Mandatory: No
* Dynamic: No

[**trace\_file\_size**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes

[**users\_refresh\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**users\_refresh\_time**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`

[**writeq\_high\_water**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_high_water)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`

[**writeq\_low\_water**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_low_water)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`

#### Service

[**auth\_all\_servers**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_all_servers)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**cluster**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#cluster)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connection\_keepalive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connection_keepalive)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)

[**disable\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#disable_sescmd_history)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enable\_root\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enable_root_user)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**filters**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#filters)

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**force\_connection\_keepalive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#force_connection_keepalive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**idle\_session\_pool\_time**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#idle_session_pool_time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`

[**log\_auth\_warnings**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_auth_warnings)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_warning**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**max\_connections**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_connections)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.

[**max\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_sescmd_history)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`

[**multiplex\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#multiplex_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

[**net\_write\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#net_write_timeout)

* Type: [durations](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory No
* Dynamic: Yes
* Default: `0s`

[**password**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**prune\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#prune_sescmd_history)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_last\_statements**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**role**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#role)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**router**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#router)

* Type: router
* Mandatory: Yes
* Dynamic: No

[**servers**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#servers)

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**session\_track\_trx\_state**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_track_trx_state)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**strip\_db\_esc**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#strip_db_esc)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**targets**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#targets)

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user\_accounts\_file**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**user\_accounts\_file\_usage**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file_usage)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`

[**version\_string**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#version_string)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None

[**wait\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#wait_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s` (>= MaxScale 24.02.5, 25.01.2), `0s` (<= MaxScale 24.02.4, 25.01.1)
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)

#### Settings for File-based Key Manager

[**file.keyfile**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#file.keyfile)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

#### Settings for HashiCorp Vault Key Manager

[**vault.ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.ca)

* Type: path
* Default: `""`
* Dynamic: Yes

[**vault.host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.host)

* Type: string
* Default: `localhost`
* Dynamic: Yes

[**vault.mount**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.mount)

* Type: string
* Default: `secret`
* Dynamic: Yes

[**vault.port**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.port)

* Type: integer
* Default: `8200`
* Dynamic: Yes

[**vault.timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 30s
* Dynamic: Yes

[**vault.tls**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.tls)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: Yes

[**vault.token**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.token)

* Type: password
* Mandatory: Yes
* Dynamic: Yes

#### Settings for KMIP Key Manager

[**kmip.ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.ca)

* Type: path
* Default: `""`
* Dynamic: Yes

[**kmip.cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.cert)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.host)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**kmip.key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.key)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.port**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.port)

* Type: integer
* Mandatory: Yes
* Dynamic: Yes

#### Settings for TLS/SSL Encryption

[**ssl**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert\_verify\_depth**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert_verify_depth)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`

[**ssl\_cipher**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cipher)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_crl**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_crl)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_key)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_passphrase**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_passphrase)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_verify\_peer\_certificate**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_certificate)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ssl\_verify\_peer\_host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_host)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**ssl\_version**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_version)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

## reference

### [maxscale-listeners](maxscale-listeners.md)

#### Settings

[**address**](maxscale-listeners.md#address)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

[**authenticator**](maxscale-listeners.md#authenticator)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**authenticator\_options**](maxscale-listeners.md#authenticator_options)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**connection\_init\_sql\_file**](maxscale-listeners.md#connection_init_sql_file)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**connection\_metadata**](maxscale-listeners.md#connection_metadata)

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

[**port**](maxscale-listeners.md#port)

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

[**protocol**](maxscale-listeners.md#protocol)

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

[**redirect\_url**](maxscale-listeners.md#redirect_url)

* Type: URL
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**service**](maxscale-listeners.md#service)

* Type: service
* Mandatory: Yes
* Dynamic: No

[**socket**](maxscale-listeners.md#socket)

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

[**sql\_mode**](maxscale-listeners.md#sql_mode)

* Type: [enum](maxscale-listeners.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

[**user\_mapping\_file**](maxscale-listeners.md#user_mapping_file)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

### [maxscale-servers](maxscale-servers.md)

#### Settings

[**address**](maxscale-servers.md#address)

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

[**disk\_space\_threshold**](maxscale-servers.md#disk_space_threshold)

* Type: Custom
* Mandatory: No
* Dynamic: Yes
* Default: None

[**extra\_port**](maxscale-servers.md#extra_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**initial\_status**](maxscale-servers.md#initial_status)

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `down`, `up`, `read`, `write`
* Default: `down`

[**labels**](maxscale-servers.md#labels)

* Type: string list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**max\_routing\_connections**](maxscale-servers.md#max_routing_connections)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.

[**monitorpw**](maxscale-servers.md#monitorpw)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**monitoruser**](maxscale-servers.md#monitoruser)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**persistmaxtime**](maxscale-servers.md#persistmaxtime)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**persistpoolmax**](maxscale-servers.md#persistpoolmax)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**port**](maxscale-servers.md#port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

[**priority**](maxscale-servers.md#priority)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**private\_address**](maxscale-servers.md#private_address)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**proxy\_protocol**](maxscale-servers.md#proxy_protocol)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**rank**](maxscale-servers.md#rank)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

[**replication\_custom\_options**](maxscale-servers.md#replication_custom_options)

* Type: string
* Default: None
* Dynamic: Yes

[**socket**](maxscale-servers.md#socket)

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

[**use\_service\_credentials**](maxscale-servers.md#use_service_credentials)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

### reference/maxscale-authenticators

#### [maxscale-gssapi-client-authenticator](maxscale-authenticators/maxscale-gssapi-client-authenticator.md)

**Settings**

[**gssapi\_keytab\_path**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md#gssapi_keytab_path)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

[**principal\_name**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md#principal_name)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`

#### [maxscale-mariadb-mysql-authenticator](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)

**Settings**

[**log\_password\_mismatch**](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md#log_password_mismatch)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [maxscale-pam-authenticator](maxscale-authenticators/maxscale-pam-authenticator.md)

**Settings**

[**pam\_backend\_mapping**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_backend_mapping)

* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`

[**pam\_mapped\_pw\_file**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_mapped_pw_file)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: None

[**pam\_mode**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_mode)

* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`

[**pam\_use\_cleartext\_plugin**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_use_cleartext_plugin)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

### reference/maxscale-filters

#### [maxscale-binlog-filter](maxscale-filters/maxscale-binlog-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-binlog-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-binlog-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_dest**](maxscale-filters/maxscale-binlog-filter.md#rewrite_dest)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_src**](maxscale-filters/maxscale-binlog-filter.md#rewrite_src)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [maxscale-cache](maxscale-filters/maxscale-cache.md)

**Settings**

[**cache\_in\_transactions**](maxscale-filters/maxscale-cache.md#cache_in_transactions)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`

[**cached\_data**](maxscale-filters/maxscale-cache.md#cached_data)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`

[**clear\_cache\_on\_parse\_errors**](maxscale-filters/maxscale-cache.md#clear_cache_on_parse_errors)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**debug**](maxscale-filters/maxscale-cache.md#debug)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**enabled**](maxscale-filters/maxscale-cache.md#enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**hard\_ttl**](maxscale-filters/maxscale-cache.md#hard_ttl)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**invalidate**](maxscale-filters/maxscale-cache.md#invalidate)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`

[**max\_count**](maxscale-filters/maxscale-cache.md#max_count)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_rows**](maxscale-filters/maxscale-cache.md#max_resultset_rows)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_size**](maxscale-filters/maxscale-cache.md#max_resultset_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_size**](maxscale-filters/maxscale-cache.md#max_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**rules**](maxscale-filters/maxscale-cache.md#rules)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)

[**selects**](maxscale-filters/maxscale-cache.md#selects)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`

[**soft\_ttl**](maxscale-filters/maxscale-cache.md#soft_ttl)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**storage**](maxscale-filters/maxscale-cache.md#storage)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`

[**storage\_options**](maxscale-filters/maxscale-cache.md#storage_options)

* Type: string
* Mandatory: No
* Dynamic: No
* Default:

[**timeout**](maxscale-filters/maxscale-cache.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `5s`

[**users**](maxscale-filters/maxscale-cache.md#users)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`

**`storage_memcached`**

[**max\_value\_size**](maxscale-filters/maxscale-cache.md#max_value_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi

[**server**](maxscale-filters/maxscale-cache.md#server)

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

**`storage_redis`**

[**password**](maxscale-filters/maxscale-cache.md#password)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server**](maxscale-filters/maxscale-cache.md#server)

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

[**ssl**](maxscale-filters/maxscale-cache.md#ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**ssl\_ca**](maxscale-filters/maxscale-cache.md#ssl_ca)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_cert**](maxscale-filters/maxscale-cache.md#ssl_cert)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_key**](maxscale-filters/maxscale-cache.md#ssl_key)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**username**](maxscale-filters/maxscale-cache.md#username)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

#### [maxscale-comment-filter](maxscale-filters/maxscale-comment-filter.md)

**Settings**

[**inject**](maxscale-filters/maxscale-comment-filter.md#inject)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

#### [maxscale-consistent-critical-read-filter](maxscale-filters/maxscale-consistent-critical-read-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-consistent-critical-read-filter.md#count)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**global**](maxscale-filters/maxscale-consistent-critical-read-filter.md#global)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ignore**](maxscale-filters/maxscale-consistent-critical-read-filter.md#ignore)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](maxscale-filters/maxscale-consistent-critical-read-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**options**](maxscale-filters/maxscale-consistent-critical-read-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**time**](maxscale-filters/maxscale-consistent-critical-read-filter.md#time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

#### [maxscale-ldi-filter](maxscale-filters/maxscale-ldi-filter.md)

**Settings**

[**host**](maxscale-filters/maxscale-ldi-filter.md#host)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`

[**key**](maxscale-filters/maxscale-ldi-filter.md#key)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**no\_verify**](maxscale-filters/maxscale-ldi-filter.md#no_verify)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**port**](maxscale-filters/maxscale-ldi-filter.md#port)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**protocol\_version**](maxscale-filters/maxscale-ldi-filter.md#protocol_version)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2

[**region**](maxscale-filters/maxscale-ldi-filter.md#region)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`

[**secret**](maxscale-filters/maxscale-ldi-filter.md#secret)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**use\_http**](maxscale-filters/maxscale-ldi-filter.md#use_http)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

#### [maxscale-masking-filter](maxscale-filters/maxscale-masking-filter.md)

**Settings**

[**check\_subqueries**](maxscale-filters/maxscale-masking-filter.md#check_subqueries)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_unions**](maxscale-filters/maxscale-masking-filter.md#check_unions)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_user\_variables**](maxscale-filters/maxscale-masking-filter.md#check_user_variables)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**large\_payload**](maxscale-filters/maxscale-masking-filter.md#large_payload)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`

[**prevent\_function\_usage**](maxscale-filters/maxscale-masking-filter.md#prevent_function_usage)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**require\_fully\_parsed**](maxscale-filters/maxscale-masking-filter.md#require_fully_parsed)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**rules**](maxscale-filters/maxscale-masking-filter.md#rules)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**treat\_string\_arg\_as\_field**](maxscale-filters/maxscale-masking-filter.md#treat_string_arg_as_field)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**warn\_type\_mismatch**](maxscale-filters/maxscale-masking-filter.md#warn_type_mismatch)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`

#### [maxscale-maxrows-filter](maxscale-filters/maxscale-maxrows-filter.md)

**Settings**

[**debug**](maxscale-filters/maxscale-maxrows-filter.md#debug)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_resultset\_return**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_return)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`

[**max\_resultset\_rows**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_rows)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)

[**max\_resultset\_size**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`

#### [maxscale-named-server-filter](maxscale-filters/maxscale-named-server-filter.md)

**Settings**

[**matchXY**](maxscale-filters/maxscale-named-server-filter.md#matchXY)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-named-server-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**source**](maxscale-filters/maxscale-named-server-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**targetXY**](maxscale-filters/maxscale-named-server-filter.md#targetXY)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-named-server-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [maxscale-query-log-all-filter](maxscale-filters/maxscale-query-log-all-filter.md)

**Settings**

[**append**](maxscale-filters/maxscale-query-log-all-filter.md#append)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**duration\_unit**](maxscale-filters/maxscale-query-log-all-filter.md#duration_unit)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

[**exclude**](maxscale-filters/maxscale-query-log-all-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](maxscale-filters/maxscale-query-log-all-filter.md#filebase)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**flush**](maxscale-filters/maxscale-query-log-all-filter.md#flush)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_data**](maxscale-filters/maxscale-query-log-all-filter.md#log_data)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

[**log\_type**](maxscale-filters/maxscale-query-log-all-filter.md#log_type)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

[**match**](maxscale-filters/maxscale-query-log-all-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**newline\_replacement**](maxscale-filters/maxscale-query-log-all-filter.md#newline_replacement)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

[**options**](maxscale-filters/maxscale-query-log-all-filter.md#options)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

[**separator**](maxscale-filters/maxscale-query-log-all-filter.md#separator)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

[**source**](maxscale-filters/maxscale-query-log-all-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**source\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md#source_exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**source\_match**](maxscale-filters/maxscale-query-log-all-filter.md#source_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**use\_canonical\_form**](maxscale-filters/maxscale-query-log-all-filter.md#use_canonical_form)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**user**](maxscale-filters/maxscale-query-log-all-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**user\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md#user_exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**user\_match**](maxscale-filters/maxscale-query-log-all-filter.md#user_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

#### [maxscale-regex-filter](maxscale-filters/maxscale-regex-filter.md)

**Settings**

[**log\_file**](maxscale-filters/maxscale-regex-filter.md#log_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**log\_trace**](maxscale-filters/maxscale-regex-filter.md#log_trace)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-regex-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: Yes
* Dynamic: Yes

[**options**](maxscale-filters/maxscale-regex-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**replace**](maxscale-filters/maxscale-regex-filter.md#replace)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**source**](maxscale-filters/maxscale-regex-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-regex-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [maxscale-rewrite-filter](maxscale-filters/maxscale-rewrite-filter.md)

**Settings**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**log\_replacement**](maxscale-filters/maxscale-rewrite-filter.md#log_replacement)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`

[**template\_file**](maxscale-filters/maxscale-rewrite-filter.md#template_file)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value

**Settings per template in the template file**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: From maxscale.cnf

[**continue\_if\_matched**](maxscale-filters/maxscale-rewrite-filter.md#continue_if_matched)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false

[**ignore\_whitespace**](maxscale-filters/maxscale-rewrite-filter.md#ignore_whitespace)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)

* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf

[**what\_if**](maxscale-filters/maxscale-rewrite-filter.md#what_if)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false

#### [maxscale-tee-filter](maxscale-filters/maxscale-tee-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-tee-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-tee-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-tee-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**service**](maxscale-filters/maxscale-tee-filter.md#service)

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none

[**source**](maxscale-filters/maxscale-tee-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sync**](maxscale-filters/maxscale-tee-filter.md#sync)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**target**](maxscale-filters/maxscale-tee-filter.md#target)

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none

[**user**](maxscale-filters/maxscale-tee-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [maxscale-throttle-filter](maxscale-filters/maxscale-throttle-filter.md)

**Settings**

[**continuous\_duration**](maxscale-filters/maxscale-throttle-filter.md#continuous_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 2s

[**max\_qps**](maxscale-filters/maxscale-throttle-filter.md#max_qps)

* Type: number
* Mandatory: Yes
* Dynamic: Yes

[**sampling\_duration**](maxscale-filters/maxscale-throttle-filter.md#sampling_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms

[**throttling\_duration**](maxscale-filters/maxscale-throttle-filter.md#throttling_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: Yes
* Dynamic: Yes

#### [maxscale-top-filter](maxscale-filters/maxscale-top-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-top-filter.md#count)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**exclude**](maxscale-filters/maxscale-top-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](maxscale-filters/maxscale-top-filter.md#filebase)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**match**](maxscale-filters/maxscale-top-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-top-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`

[**source**](maxscale-filters/maxscale-top-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-top-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [maxscale-workload-capture-and-replay](maxscale-filters/maxscale-workload-capture-and-replay.md)

**Settings**

[**capture\_dir**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_dir)

* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No

[**capture\_duration**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 0s
* Maximum: Unlimited in MaxScale, 5min in MaxScale Lite.
* Mandatory: No
* Dynamic: No

[**capture\_size**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Default: 0
* Maximum: Unlimited in MaxScale, 10MB in MaxScale Lite.
* Mandatory: No
* Dynamic: No

[**start\_capture**](maxscale-filters/maxscale-workload-capture-and-replay.md#start_capture)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Mandatory: No
* Dynamic: No

### reference/maxscale-monitors

#### [common-monitor-parameters](maxscale-monitors/common-monitor-parameters.md)

**Settings**

[**backend\_connect\_attempts**](maxscale-monitors/common-monitor-parameters.md#backend_connect_attempts)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

[**backend\_connect\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_connect_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_read\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_read_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_write\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_write_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**disk\_space\_check\_interval**](maxscale-monitors/common-monitor-parameters.md#disk_space_check_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**disk\_space\_threshold**](maxscale-monitors/common-monitor-parameters.md#disk_space_threshold)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**events**](maxscale-monitors/common-monitor-parameters.md#events)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

[**journal\_max\_age**](maxscale-monitors/common-monitor-parameters.md#journal_max_age)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

[**module**](maxscale-monitors/common-monitor-parameters.md#module)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**monitor\_interval**](maxscale-monitors/common-monitor-parameters.md#monitor_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

[**password**](maxscale-monitors/common-monitor-parameters.md#password)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**primary\_state\_sql**](maxscale-monitors/common-monitor-parameters.md#primary_state_sql)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replica\_state\_sql**](maxscale-monitors/common-monitor-parameters.md#replica_state_sql)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**role**](maxscale-monitors/common-monitor-parameters.md#role)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**script**](maxscale-monitors/common-monitor-parameters.md#script)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**script\_timeout**](maxscale-monitors/common-monitor-parameters.md#script_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**servers**](maxscale-monitors/common-monitor-parameters.md#servers)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user**](maxscale-monitors/common-monitor-parameters.md#user)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

#### [galera-monitor](maxscale-monitors/galera-monitor.md)

**Settings**

[**available\_when\_donor**](maxscale-monitors/galera-monitor.md#available_when_donor)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**disable\_master\_failback**](maxscale-monitors/galera-monitor.md#disable_master_failback)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**disable\_master\_role\_setting**](maxscale-monitors/galera-monitor.md#disable_master_role_setting)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**root\_node\_as\_master**](maxscale-monitors/galera-monitor.md#root_node_as_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**set\_donor\_nodes**](maxscale-monitors/galera-monitor.md#set_donor_nodes)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**use\_priority**](maxscale-monitors/galera-monitor.md#use_priority)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

#### [mariadb-monitor](maxscale-monitors/mariadb-monitor.md)

**Settings**

[**assume\_unique\_hostnames**](maxscale-monitors/mariadb-monitor.md#assume_unique_hostnames)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**cooperative\_monitoring\_locks**](maxscale-monitors/mariadb-monitor.md#cooperative_monitoring_locks)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`

[**enforce\_read\_only\_servers**](maxscale-monitors/mariadb-monitor.md#enforce_read_only_servers)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_read\_only\_slaves**](maxscale-monitors/mariadb-monitor.md#enforce_read_only_slaves)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_writable\_master**](maxscale-monitors/mariadb-monitor.md#enforce_writable_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failcount**](maxscale-monitors/mariadb-monitor.md#failcount)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`

[**maintenance\_on\_low\_disk\_space**](maxscale-monitors/mariadb-monitor.md#maintenance_on_low_disk_space)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_conditions**](maxscale-monitors/mariadb-monitor.md#master_conditions)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`

[**script\_max\_replication\_lag**](maxscale-monitors/mariadb-monitor.md#script_max_replication_lag)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**slave\_conditions**](maxscale-monitors/mariadb-monitor.md#slave_conditions)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`

**Settings for Backup operations**

[**backup\_storage\_address**](maxscale-monitors/mariadb-monitor.md#backup_storage_address)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**backup\_storage\_path**](maxscale-monitors/mariadb-monitor.md#backup_storage_path)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**mariadb\_backup\_parallel**](maxscale-monitors/mariadb-monitor.md#mariadb_backup_parallel)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

[**mariadb\_backup\_use\_memory**](maxscale-monitors/mariadb-monitor.md#mariadb_backup_use_memory)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `1G`

[**rebuild\_port**](maxscale-monitors/mariadb-monitor.md#rebuild_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`

[**ssh\_check\_host\_key**](maxscale-monitors/mariadb-monitor.md#ssh_check_host_key)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**ssh\_keyfile**](maxscale-monitors/mariadb-monitor.md#ssh_keyfile)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**ssh\_port**](maxscale-monitors/mariadb-monitor.md#ssh_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`

[**ssh\_timeout**](maxscale-monitors/mariadb-monitor.md#ssh_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**ssh\_user**](maxscale-monitors/mariadb-monitor.md#ssh_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**Settings for Cluster manipulation operations**

[**auto\_failover**](maxscale-monitors/mariadb-monitor.md#auto_failover)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`

[**auto\_rejoin**](maxscale-monitors/mariadb-monitor.md#auto_rejoin)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**demotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md#demotion_sql_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**enforce\_simple\_topology**](maxscale-monitors/mariadb-monitor.md#enforce_simple_topology)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failover\_timeout**](maxscale-monitors/mariadb-monitor.md#failover_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**handle\_events**](maxscale-monitors/mariadb-monitor.md#handle_events)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_failure\_timeout**](maxscale-monitors/mariadb-monitor.md#master_failure_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**promotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md#promotion_sql_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_master\_ssl**](maxscale-monitors/mariadb-monitor.md#replication_master_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**replication\_password**](maxscale-monitors/mariadb-monitor.md#replication_password)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_user**](maxscale-monitors/mariadb-monitor.md#replication_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**servers\_no\_promotion**](maxscale-monitors/mariadb-monitor.md#servers_no_promotion)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**\[switchover\_on\_low\_disk\_space`\*\*](../reference/maxscale-monitors/mariadb-monitor.md#switchover_on_low_disk_space`\*\*)**

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**switchover\_timeout**](maxscale-monitors/mariadb-monitor.md#switchover_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**verify\_master\_failure**](maxscale-monitors/mariadb-monitor.md#verify_master_failure)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

**Settings for Primary server write test**

[**write\_test\_fail\_action**](maxscale-monitors/mariadb-monitor.md#write_test_fail_action)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes

[**write\_test\_interval**](maxscale-monitors/mariadb-monitor.md#write_test_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Dynamic: Yes
* Default: 0s

[**write\_test\_table**](maxscale-monitors/mariadb-monitor.md#write_test_table)

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`

### reference/maxscale-protocols

#### [maxscale-mariadb-protocol-module](maxscale-protocols/maxscale-mariadb-protocol-module.md)

**Settings**

[**allow\_replication**](maxscale-protocols/maxscale-mariadb-protocol-module.md#allow_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

#### [maxscale-nosql-protocol-module](maxscale-protocols/maxscale-nosql-protocol-module.md)

**Settings**

[**authentication\_db**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_db)

* Type: string
* Mandatory: No
* Default: `"NoSQL"`

[**authentication\_key\_id**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_key_id)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_password**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_password)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_required**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_required)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**authentication\_shared**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_shared)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**authentication\_user**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_user)

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.

[**authorization\_enabled**](maxscale-protocols/maxscale-nosql-protocol-module.md#authorization_enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**auto\_create\_databases**](maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_databases)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

[**auto\_create\_tables**](maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_tables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

[**cursor\_timeout**](maxscale-protocols/maxscale-nosql-protocol-module.md#cursor_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Default: `60s`

[**debug**](maxscale-protocols/maxscale-nosql-protocol-module.md#debug)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`

[**host**](maxscale-protocols/maxscale-nosql-protocol-module.md#host)

* Type: string
* Mandatory: No
* Default: `"%"`

[**id\_length**](maxscale-protocols/maxscale-nosql-protocol-module.md#id_length)

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`

[**internal\_cache**](maxscale-protocols/maxscale-nosql-protocol-module.md#internal_cache)

* Type: string
* Mandatory: No
* Default: ''

[**log\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md#log_unknown_command)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**on\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md#on_unknown_command)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`

[**ordered\_insert\_behavior**](maxscale-protocols/maxscale-nosql-protocol-module.md#ordered_insert_behavior)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`

[**password**](maxscale-protocols/maxscale-nosql-protocol-module.md#password)

* Type: string
* Mandatory: No
* Default: `""`

[**user**](maxscale-protocols/maxscale-nosql-protocol-module.md#user)

* Type: string
* Mandatory: No
* Default: `""`

### reference/maxscale-rest-api

#### [maxscale-filter-resource](maxscale-rest-api/maxscale-filter-resource.md)

**Resource Operations**

**\[Create a filter]\(../reference/maxscale-rest-api/maxscale-filter-resource.md#Create a filter)**

* Type of the object, must be `filters`
* `data.attributes.module`
* The filter module to use

#### [maxscale-listener-resource](maxscale-rest-api/maxscale-listener-resource.md)

**Resource Operations**

**\[Create a new listener]\(../reference/maxscale-rest-api/maxscale-listener-resource.md#Create a new listener)**

* Type of the object, must be `listeners`
* `data.attributes.parameters.port` OR `data.attributes.parameters.socket`
* The TCP port or UNIX Domain Socket the listener listens on. Only one of the fields can be defined.
* `data.relationships.services.data`
* The service relationships data, must define a JSON object with an `id` value that defines the service to use and a `type` value set to `services`.

#### [maxscale-monitor-resource](maxscale-rest-api/maxscale-monitor-resource.md)

**Resource Operations**

**\[Create a monitor]\(../reference/maxscale-rest-api/maxscale-monitor-resource.md#Create a monitor)**

* Type of the object, must be `monitors`
* `data.attributes.module`
* The monitor module to use
* `data.attributes.parameters.user`
* The [`user`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user) to use
* `data.attributes.parameters.password`
* The [password](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password) to use

#### [maxscale-server-resource](maxscale-rest-api/maxscale-server-resource.md)

**Resource Operations**

**\[Create a server]\(../reference/maxscale-rest-api/maxscale-server-resource.md#Create a server)**

* Type of the object, must be `servers`
* `data.attributes.parameters.address` OR `data.attributes.parameters.socket`
* The [`address`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#address) or [`socket`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#socket) to use. Only one of the fields can be defined.
* `data.attributes.parameters.port`
* The [`port`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#port) to use. Needs to be defined if the `address` field is defined.

#### [maxscale-service-resource](maxscale-rest-api/maxscale-service-resource.md)

**Resource Operations**

**\[Create a service]\(../reference/maxscale-rest-api/maxscale-service-resource.md#Create a service)**

* Type of the object, must be `services`
* `data.attributes.router`
* The router module to use
* `data.attributes.parameters.user`
* The [`user`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user) to use
* `data.attributes.parameters.password`
* The [`password`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password) to use

### reference/maxscale-routers

#### [maxscale-binlogrouter](maxscale-routers/maxscale-binlogrouter.md)

**Settings**

[**archivedir**](maxscale-routers/maxscale-binlogrouter.md#archivedir)

* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No

[**compression\_algorithm**](maxscale-routers/maxscale-binlogrouter.md#compression_algorithm)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`

[**datadir**](maxscale-routers/maxscale-binlogrouter.md#datadir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`

[**ddl\_only**](maxscale-routers/maxscale-binlogrouter.md#ddl_only)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: false

[**encryption\_cipher**](maxscale-routers/maxscale-binlogrouter.md#encryption_cipher)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`

[**encryption\_key\_id**](maxscale-routers/maxscale-binlogrouter.md#encryption_key_id)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**expiration\_mode**](maxscale-routers/maxscale-binlogrouter.md#expiration_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`

[**expire\_log\_duration**](maxscale-routers/maxscale-binlogrouter.md#expire_log_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s`

[**expire\_log\_minimum\_files**](maxscale-routers/maxscale-binlogrouter.md#expire_log_minimum_files)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`

[**net\_timeout**](maxscale-routers/maxscale-binlogrouter.md#net_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `10s`

[**number\_of\_noncompressed\_files**](maxscale-routers/maxscale-binlogrouter.md#number_of_noncompressed_files)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`

[**rpl\_semi\_sync\_slave\_enabled**](maxscale-routers/maxscale-binlogrouter.md#rpl_semi_sync_slave_enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: false
* Dynamic: Yes

[**select\_master**](maxscale-routers/maxscale-binlogrouter.md#select_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**server\_id**](maxscale-routers/maxscale-binlogrouter.md#server_id)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`

#### [maxscale-diff](maxscale-routers/maxscale-diff.md)

**Settings**

[**explain**](maxscale-routers/maxscale-diff.md#explain)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

[**explain\_entries**](maxscale-routers/maxscale-diff.md#explain_entries)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

[**explain\_period**](maxscale-routers/maxscale-diff.md#explain_period)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

[**main**](maxscale-routers/maxscale-diff.md#main)

* Type: server
* Mandatory: Yes
* Dynamic: No

[**max\_request\_lag**](maxscale-routers/maxscale-diff.md#max_request_lag)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

[**on\_error**](maxscale-routers/maxscale-diff.md#on_error)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

[**percentile**](maxscale-routers/maxscale-diff.md#percentile)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

[**qps\_window**](maxscale-routers/maxscale-diff.md#qps_window)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 15m

[**report**](maxscale-routers/maxscale-diff.md#report)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

[**reset\_replication**](maxscale-routers/maxscale-diff.md#reset_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_faster\_statements**](maxscale-routers/maxscale-diff.md#retain_faster_statements)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**retain\_slower\_statements**](maxscale-routers/maxscale-diff.md#retain_slower_statements)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**samples**](maxscale-routers/maxscale-diff.md#samples)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

[**service**](maxscale-routers/maxscale-diff.md#service)

* Type: service
* Mandatory: Yes
* Dynamic: No

#### [maxscale-exasolrouter](maxscale-routers/maxscale-exasolrouter.md)

**Settings**

[**appearance**](maxscale-routers/maxscale-exasolrouter.md#appearance)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`

[**connection\_string**](maxscale-routers/maxscale-exasolrouter.md#connection_string)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**preprocessor**](maxscale-routers/maxscale-exasolrouter.md#preprocessor)

* Type: String
* Mandatory: No
* Dynamic: No
* Values: `auto`, `activate-only`, `custom:<path>`, `disabled`
* Default: `auto`

[**preprocessor\_script**](maxscale-routers/maxscale-exasolrouter.md#preprocessor_script)

* Type: String
* Mandatory: No
* Dynamic: No
* Default: "UTIL.maria\_preprocessor"

#### [maxscale-kafkacdc](maxscale-routers/maxscale-kafkacdc.md)

**Settings**

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkacdc.md#bootstrap_servers)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**cooperative\_replication**](maxscale-routers/maxscale-kafkacdc.md#cooperative_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**enable\_idempotence**](maxscale-routers/maxscale-kafkacdc.md#enable_idempotence)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](maxscale-routers/maxscale-kafkacdc.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**gtid**](maxscale-routers/maxscale-kafkacdc.md#gtid)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_mechanism)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_password)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_user)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](maxscale-routers/maxscale-kafkacdc.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**read\_gtid\_from\_kafka**](maxscale-routers/maxscale-kafkacdc.md#read_gtid_from_kafka)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**send\_schema**](maxscale-routers/maxscale-kafkacdc.md#send_schema)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**server\_id**](maxscale-routers/maxscale-kafkacdc.md#server_id)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**timeout**](maxscale-routers/maxscale-kafkacdc.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**topic**](maxscale-routers/maxscale-kafkacdc.md#topic)

* Type: string
* Mandatory: Yes
* Dynamic: No

#### [maxscale-kafkaimporter](maxscale-routers/maxscale-kafkaimporter.md)

**Settings**

[**batch\_size**](maxscale-routers/maxscale-kafkaimporter.md#batch_size)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkaimporter.md#bootstrap_servers)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**engine**](maxscale-routers/maxscale-kafkaimporter.md#engine)

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_mechanism)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_password)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**table\_name\_in**](maxscale-routers/maxscale-kafkaimporter.md#table_name_in)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

[**timeout**](maxscale-routers/maxscale-kafkaimporter.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

[**topics**](maxscale-routers/maxscale-kafkaimporter.md#topics)

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes

#### [maxscale-mirror](maxscale-routers/maxscale-mirror.md)

**Settings**

[**exporter**](maxscale-routers/maxscale-mirror.md#exporter)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`

[**file**](maxscale-routers/maxscale-mirror.md#file)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_broker**](maxscale-routers/maxscale-mirror.md#kafka_broker)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_topic**](maxscale-routers/maxscale-mirror.md#kafka_topic)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**main**](maxscale-routers/maxscale-mirror.md#main)

* Type: target
* Mandatory: Yes
* Dynamic: Yes

[**on\_error**](maxscale-routers/maxscale-mirror.md#on_error)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`

[**report**](maxscale-routers/maxscale-mirror.md#report)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`

#### [maxscale-readconnroute](maxscale-routers/maxscale-readconnroute.md)

**Settings**

[**master\_accept\_reads**](maxscale-routers/maxscale-readconnroute.md#master_accept_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**max\_replication\_lag**](maxscale-routers/maxscale-readconnroute.md#max_replication_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**router\_options**](maxscale-routers/maxscale-readconnroute.md#router_options)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`

#### [maxscale-readwritesplit](maxscale-routers/maxscale-readwritesplit.md)

**Settings**

[**causal\_reads**](maxscale-routers/maxscale-readwritesplit.md#causal_reads)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`

[**causal\_reads\_timeout**](maxscale-routers/maxscale-readwritesplit.md#causal_reads_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**delayed\_retry**](maxscale-routers/maxscale-readwritesplit.md#delayed_retry)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**delayed\_retry\_timeout**](maxscale-routers/maxscale-readwritesplit.md#delayed_retry_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**lazy\_connect**](maxscale-routers/maxscale-readwritesplit.md#lazy_connect)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_accept\_reads**](maxscale-routers/maxscale-readwritesplit.md#master_accept_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_failure\_mode**](maxscale-routers/maxscale-readwritesplit.md#master_failure_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)

[**master\_reconnection**](maxscale-routers/maxscale-readwritesplit.md#master_reconnection)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)

[**max\_replication\_lag**](maxscale-routers/maxscale-readwritesplit.md#max_replication_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**max\_slave\_connections**](maxscale-routers/maxscale-readwritesplit.md#max_slave_connections)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 0
* Max: 255
* Default: 255

[**retry\_failed\_reads**](maxscale-routers/maxscale-readwritesplit.md#retry_failed_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**slave\_connections**](maxscale-routers/maxscale-readwritesplit.md#slave_connections)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**slave\_selection\_criteria**](maxscale-routers/maxscale-readwritesplit.md#slave_selection_criteria)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`

[**strict\_multi\_stmt**](maxscale-routers/maxscale-readwritesplit.md#strict_multi_stmt)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_sp\_calls**](maxscale-routers/maxscale-readwritesplit.md#strict_sp_calls)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_tmp\_tables**](maxscale-routers/maxscale-readwritesplit.md#strict_tmp_tables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)

[**sync\_transaction**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `soft`, `hard`
* Default: `none`

[**sync\_transaction\_count**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_count)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 255
* Default: 1

[**sync\_transaction\_max\_lag**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_max_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**sync\_transaction\_timeout**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**transaction\_replay**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_attempts**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_attempts)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**transaction\_replay\_checksum**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_checksum)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`

[**transaction\_replay\_max\_size**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_max_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB

[**transaction\_replay\_retry\_on\_deadlock**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_retry_on_deadlock)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_retry\_on\_mismatch**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_retry_on_mismatch)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_safe\_commit**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_safe_commit)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**transaction\_replay\_timeout**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)

[**use\_sql\_variables\_in**](maxscale-routers/maxscale-readwritesplit.md#use_sql_variables_in)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`

#### [maxscale-schemarouter](maxscale-routers/maxscale-schemarouter.md)

**Settings**

[**allow\_duplicates**](maxscale-routers/maxscale-schemarouter.md#allow_duplicates)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ignore\_tables**](maxscale-routers/maxscale-schemarouter.md#ignore_tables)

* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ignore\_tables\_regex**](maxscale-routers/maxscale-schemarouter.md#ignore_tables_regex)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**max\_staleness**](maxscale-routers/maxscale-schemarouter.md#max_staleness)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 150s

[**refresh\_databases**](maxscale-routers/maxscale-schemarouter.md#refresh_databases)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**refresh\_interval**](maxscale-routers/maxscale-schemarouter.md#refresh_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`

#### [maxscale-smartrouter](maxscale-routers/maxscale-smartrouter.md)

**Settings**

[**master**](maxscale-routers/maxscale-smartrouter.md#master)

* Type: target
* Mandatory: Yes
* Dynamic: No

***

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
