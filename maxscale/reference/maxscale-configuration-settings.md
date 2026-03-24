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
* Default: `%`&#x20;
* Description: Hosts can perform any REST API operation with read and write access.

[**admin\_secure\_gui**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_secure_gui)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Manages whether the GUI are accessible only over secure HTTPS.

[**admin\_ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Path to the CA sertificate for outgoing HTTPS requests.

[**admin\_ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Provides the path of the TLS public certificate in PEM format used by the REST API.

[**admin\_ssl\_cipher**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cipher)

* Type: string
* Mandatory: No
* Dynamic: No
* Description: Defines additional TLS cipher configuration for the REST API.

[**admin\_ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Indicates the location of the TLS private key in PEM format that the admin interface uses.

[**admin\_ssl\_passphrase**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_passphrase)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Provides the passphrase needed to decrypt the admin interface's TLS private key.

[**admin\_ssl\_version**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_version)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`&#x20;
* Description: Specifies the allowed TLS protocol versions for the REST API.

[**admin\_verify\_url**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_verify_url)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Delegate the validation of tokens to an external server.

**allow\_duplicate\_servers**

* Type: boolean
* Default: false
* Description: Allows multiple server definitions to use the same IP address and port combination.

[**auth\_connect\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_connect_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Sets the connection timeout for retrieving user authentication data from backend servers.

[**auto\_tune**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No
* Description: Allows automatic tuning of specified configuration parameters based on backend server values.

[**config\_sync\_cluster**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_cluster)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Monitor name used for configuration synchronization&#x20;

[**config\_sync\_db**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_db)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`&#x20;
* Description: Identifies the database that contains the `maxscale_config` table, which is used to synchronize configurations.

[**config\_sync\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`&#x20;
* Description: Specifies how often MaxScale synchronizes configuration changes with the cluster.

[**config\_sync\_password**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_password)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description:&#x20;

[**config\_sync\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Timeout for config sync SQL operations.

[**config\_sync\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Username used for configuration sync database access across MaxScale instances.

[**connector\_plugindir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connector_plugindir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent
* Description: Specifies the ditrectory that contains MaxScale's MariaDB Connector-C authentication plugins.

[**core\_file**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#core_file)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No
* Description: Specifies whether a core dump file is generated in the event that MaxScale crashes.

**cors\_allow\_origin**

* Type: string
* Default: N/A
* Description: Enables CORS and sets the `Access-Control-Allow-Origin` header to the specified value.

[**datadir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#datadir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`&#x20;
* Description: Specifies the location of MaxScale's data files directory.

[**debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#debug)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines debug options equivalent to the `--debug` command line argument.

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
* Description: Manages when MaxScale logs the last statements executed by a client session.

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
* Description: Sets the number of entries in the reverse DNS lookup cache for client hostnames.

[**key\_manager**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#key_manager)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`&#x20;
* Description: Defines the encrytion key manager that MaxScale uses.

[**libdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#libdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent
* Description: Specifies the directory that MaxScale uses to locate modules.

[**load\_persisted\_configs**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#load_persisted_configs)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* &#x20;Description: Loads saved runtime changes at startup.

[**local\_address**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#local_address)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines what specific local interface to use when connecting to servers.

[**log\_augmentation**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_augmentation)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Includes function names to logged messages.

[**log\_debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Log debug messages when enabled.

[**log\_info**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Log detailed info messages when enabled.

[**log\_notice**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Log notice level messages when enabled.

[**log\_throttling**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_throttling)

* Type: number, [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations), [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`&#x20;
* Description: Manages how frequently repeated errors or warnings are logged.

[**log\_warn\_super\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warn_super_user)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Log warning when a client with SUPER privilege connects.

[**log\_warning**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Enable service-level warning logging.

[**logdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#logdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`&#x20;
* Description: Defines the directory where log files are stored.

[**max\_auth\_errors\_until\_block**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_auth_errors_until_block)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`&#x20;
* Description: Maximum number of authentication failures before temprarily blocking a host.

[**maxlog**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#maxlog)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Enables logging of messages to the MaxScale log file.

[**module\_configdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#module_configdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`&#x20;
* Description: Directory for module-specific configuration files.

[**ms\_timestamp**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ms_timestamp)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Adds millisecond precision to logfile timestamps.

[**passive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Deprecated - use [cooperative monitoring](maxscale-monitors/mariadb-monitor.md#cooperative-monitoring) instead.&#x20;

[**persist\_runtime\_changes**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persist_runtime_changes)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: No
* Description: Save runtime configuration changes to disk.

[**persistdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persistdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`&#x20;
* Description: Directory where runtime configuration changes are stored.

[**piddir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#piddir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`&#x20;
* Description: Specifies the directory containing the MaxScale process ID (PID) file.

[**query\_classifier\_cache\_size**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_classifier_cache_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent
* Description: Sets the maximum size of the query classifier cache.

[**query\_retries**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retries)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`&#x20;
* Description: Deprecated and ignored.

[**query\_retry\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retry_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Deprecated and ignored.

[**rebalance\_period**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_period)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`&#x20;
* Description: Defines the interval for monitoring and rebalancing worker thread load. A value of `0` disables this function.

[**rebalance\_threshold**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_threshold)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`&#x20;
* Description: Load difference percentage that triggers thread rebalancing.

[**rebalance\_window**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_window)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`&#x20;
* Description: Manages how many seconds of load to consider for rebalancing.

**redirect\_output\_to\_file**

* Type: boolean
* Default: false
* Description: Redirects `stdout` and `stderr` to the specified file path.

[**require\_secure\_transport**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#require_secure_transport)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No
* Description: Requires SSL for all listeners, servers, and the REST API.

[**retain\_last\_statements**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Specifies how many statements MaxScale can store per session.

[**secretsdir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#secretsdir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Location of the .secrets file for password encryption.

[**session\_trace**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Defines how many log entries are stored in the session trace log.

[**session\_trace\_match**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a refular expression pattern used to filter session trace logs.

[**sharedir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sharedir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`&#x20;
* Description: Defines the directory where static data assests are loaded.

[**skip\_name\_resolve**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#skip_name_resolve)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Disables reverse DNS lookups of client IP addresses.

[**sql\_mode**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sql_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`&#x20;
* Description: Defines which SQL language mode the query classifier should ex&#x70;_&#x65;ct._

**sql\_batch\_size**

* Type: size
* Default: 10MiB
* Description: Sets the maximum batch size for REST API SQL statement processing.

[**substitute\_variables**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#substitute_variables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Allows use of environment variables within MaxScale configuration files.

[**syslog**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#syslog)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Writes log messages to the system journal via the system logging interface.

[**telemetry**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables sending metrics to OpenTelemetry Collector.

[**telemetry\_attributes**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_attributes)

* Type: stringlist
* Default: empty
* Dynamic: Yes
* Mandatory: No
* Description: Global attributes to send with every metric.

[**telemetry\_ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Path to trusted CA certificate (PEM) used for validating TLS connections in telemetry.

[**telemetry\_ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the file path to the TLS public certificate in PEM format for telemetry.

[**telemetry\_ssl\_insecure**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_insecure)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Disable TLS certificate validation for telemetry.

[**telemetry\_ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: TLS private key for encrypted telemetry.

[**telemetry\_update\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_update_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`&#x20;
* Description: Defines the minimum interval between sending metrics to the telemetry collector.

[**telemetry\_url**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_url)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `http://localhost:4318/v1/metrics`&#x20;
* Description: Defines the OpenTelemetry endpoint where MaxScale pushes metrics.

[**threads**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads)

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`&#x20;
* Description: Manages the number of worker threads for routing client traffic.

[**threads\_max**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads_max)

* Type: positive integer
* Default: 256
* Dynamic: No
* Description: Hard limit for the number of worker threads.

[**trace\_file\_dir**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_dir)

* Type: path
* Mandatory: No
* Dynamic: No
* Description: Directory for low-overhead trace log files.

[**trace\_file\_size**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Description: Amount of log data to keep in trace files.

[**users\_refresh\_interval**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`&#x20;
* Description: Defines the interval for automatically refreshing user accounts from backend servers.

[**users\_refresh\_time**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`&#x20;
* Description: Maximum frequency for refreshing user accounts from backend servers after authentication failures.

[**writeq\_high\_water**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_high_water)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`&#x20;
* Description: High water mark for network write buffer throttling.

[**writeq\_low\_water**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_low_water)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`&#x20;
* Description: Low water mark to disable network write throttling.

#### Service

[**auth\_all\_servers**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_all_servers)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Manages whether authentication data is loaded from one server or aggregated from all servers.

[**cluster**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#cluster)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Monitor that defines servers for this service.

[**connection\_keepalive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connection_keepalive)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)
* Description: Send pings to keep idle backend connections alive.

[**disable\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#disable_sescmd_history)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Disable session command history entirely.

[**enable\_root\_user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enable_root_user)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Controls whether the root user is allowed to connect through MaxScale to backend servers.&#x20;

[**filters**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#filters)

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a list of filters applied to client requests before routing to backend servers.

[**force\_connection\_keepalive**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#force_connection_keepalive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Send keepalive pings to any backends even when client is idle.

[**idle\_session\_pool\_time**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#idle_session_pool_time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`&#x20;
* Description: Time idle before pooling backend connections.

[**log\_auth\_warnings**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_auth_warnings)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Log authentication failures and warnings.

[**log\_debug**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enable service-level debug logging.

[**log\_info**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enable service-level info logging.

[**log\_notice**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enable service-level notice logging.

[**log\_warning**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enable service-level warning logging.

[**max\_connections**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_connections)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.
* Description: Maximum number of simultaneous connections allowed to this service.

[**max\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_sescmd_history)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`&#x20;
* Description: Maximum session commands to store for replay.

[**multiplex\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#multiplex_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`&#x20;
* Description: Maximum wait time for backend connection.

[**net\_write\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#net_write_timeout)

* Type: [durations](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory No
* Dynamic: Yes
* Default: `0s`&#x20;
* Description: Disconnects connection if data buffered longer than this duration.

[**password**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the password the service uses to retrieve user accounts from backends.

[**prune\_sescmd\_history**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#prune_sescmd_history)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Prune old session commands when limit exceeded the configured value.

[**retain\_last\_statements**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`&#x20;
* Description: Defines the number of statements MaxScale stores per session.

[**role**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#role)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Role to activate after connecting to a server.

[**router**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#router)

* Type: router
* Mandatory: Yes
* Dynamic: No
* Description: Defines the router module that a service uses to direct client connections to backend servers.

[**servers**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#servers)

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the backend servers associated with the service.

[**session\_track\_trx\_state**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_track_trx_state)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Improves accuracy by enabling backend-based transaction state tracking.

[**strip\_db\_esc**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#strip_db_esc)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Remove escape characters from database names when loading users grants from a backend server.

[**targets**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#targets)

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Nested services or servers for multi-level routing.

[**user**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Username for retrieving user account information from backends.

[**user\_accounts\_file**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the path to a JSON file containing additional user accounts for client authentication.

[**user\_accounts\_file\_usage**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file_usage)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`&#x20;
* Description: Specifies when the user accounts file is read instead of or alongside server data.

[**version\_string**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#version_string)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None
* Description: Custom version string sent in MySQL handshake.

[**wait\_timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#wait_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s` (>= MaxScale 24.02.5, 25.01.2), `0s` (<= MaxScale 24.02.4, 25.01.1)
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)
* Description: Specifies the idle timeout for client sessions before terminatio&#x6E;**.**

#### Settings for File-based Key Manager

[**file.keyfile**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#file.keyfile)

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Path to file containing encryption keys.

#### Settings for HashiCorp Vault Key Manager

[**vault.ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.ca)

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: Defines the CA certificate used for validating Vault server connections.

[**vault.host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.host)

* Type: string
* Default: `localhost`
* Dynamic: Yes
* Description: Specifies the hostname of the Vault server.

[**vault.mount**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.mount)

* Type: string
* Default: `secret`
* Dynamic: Yes
* Description: Provides the Key-Value mount path in Vault where secrets are stored.

[**vault.port**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.port)

* Type: integer
* Default: `8200`
* Dynamic: Yes
* Description: Defines the port on which the Vault server listens.

[**vault.timeout**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 30s
* Dynamic: Yes
* Description: Sets the timeout for requests and connections to the Vault server.

[**vault.tls**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.tls)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: Yes
* Description: Manages whether encrypted (HTTPS) or unencrypted (HTTP) connections are used when communicating with the Vault server.

[**vault.token**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.token)

* Type: password
* Mandatory: Yes
* Dynamic: Yes
* Description: Provides the authentication token to access the Vault server.

#### Settings for KMIP Key Manager

[**kmip.ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.ca)

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: CA ceritficate for KMIP server.

[**kmip.cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.cert)

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Client certificate for KMIP authentication.

[**kmip.host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.host)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**kmip.key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.key)

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the client private key used for connecting to the KMIP serve&#x72;**.**

[**kmip.port**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.port)

* Type: integer
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the port on which the KMIP server listens.

#### Settings for TLS/SSL Encryption

[**ssl**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables SSL encryption for connections when set to true.

[**ssl\_ca**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the CA certificate used to validate the peer’s certificate.

[**ssl\_cert**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Deprecated - use [ssl\_ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_ca) instead.

[**ssl\_cert\_verify\_depth**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert_verify_depth)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`&#x20;
* Description: Specifies the maximum depth of the CA chain during verification.

[**ssl\_cipher**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cipher)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Provides the list of TLS ciphers to use for SSL connections.

[**ssl\_crl**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_crl)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the CRL file used to validate revoked SSL certificates.

[**ssl\_key**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_key)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the path to the SSL/TLS private key that is used for secure connections.

[**ssl\_passphrase**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_passphrase)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Defines the passphrase used to decrypt the SSL/TLS private key.

[**ssl\_verify\_peer\_certificate**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_certificate)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Verifies the peer's SSL/TLS certificate against a trusted CA.

[**ssl\_verify\_peer\_host**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_host)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Verifies the peer's hostname or IP address using its SSL/TLS certificate.

[**ssl\_version**](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_version)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`&#x20;
* Description: Lists the TLS protocol versions that are allowed for SSL/TLS connections.

## reference

### [maxscale-listeners](maxscale-listeners.md)

#### Settings

[**address**](maxscale-listeners.md#address)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`&#x20;
* Description: Indicates the hostname or address that the listener binds to when a connection is made.

[**authenticator**](maxscale-listeners.md#authenticator)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the authenticator module used for client authentication.

[**authenticator\_options**](maxscale-listeners.md#authenticator_options)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Provides additional configuration settings for the authenticator module.

[**connection\_init\_sql\_file**](maxscale-listeners.md#connection_init_sql_file)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies a file containing SQL statements executed on backend connections after authentication.

[**connection\_metadata**](maxscale-listeners.md#connection_metadata)

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No
* Description: Provides the metadata that is given to clients upon connection as a list of key-value pairs separated by commas.

[**port**](maxscale-listeners.md#port)

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`&#x20;
* Description: Specifies the port on which the listener accepts connections.

[**protocol**](maxscale-listeners.md#protocol)

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`&#x20;
* Description: Defines the protocol module that clients and MaxScale use to communicate.

[**redirect\_url**](maxscale-listeners.md#redirect_url)

* Type: URL
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the database URL that clients are sent to following authentication.

[**service**](maxscale-listeners.md#service)

* Type: service
* Mandatory: Yes
* Dynamic: No
* Description: Identifies the service that the listener is connected to.

[**socket**](maxscale-listeners.md#socket)

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines the Unix domain socket that the listener uses to receive inbound connections.

[**sql\_mode**](maxscale-listeners.md#sql_mode)

* Type: [enum](maxscale-listeners.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`&#x20;
* Description: Specifies the listener's SQL mode, overriding the global `sql_mode` setting if it is set.

[**user\_mapping\_file**](maxscale-listeners.md#user_mapping_file)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Provides optional backend credentials for MariaDB protocol connections, as well as a JSON file that specifies user and group mappings.

### [maxscale-servers](maxscale-servers.md)

#### Settings

[**address**](maxscale-servers.md#address)

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the hostname or IP address of the backend server to which MaxScale connects.

[**disk\_space\_threshold**](maxscale-servers.md#disk_space_threshold)

* Type: Custom
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines disk usage threshold that triggers warnings or actions when exceeded.

[**extra\_port**](maxscale-servers.md#extra_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Specifies an alternative port that MaxScale uses for administrative connections to the backend server.

[**initial\_status**](maxscale-servers.md#initial_status)

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `down`, `up`, `read`, `write`
* Default: `down`&#x20;
* Description: Provides the initial status of the server when it starts or its reconfigured.

[**labels**](maxscale-servers.md#labels)

* Type: string list
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a comma-separated list of user-defined labels assigned to the server.

[**max\_routing\_connections**](maxscale-servers.md#max_routing_connections)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.
* Description: Provides the maximum number of routing connections to the server.

[**monitorpw**](maxscale-servers.md#monitorpw)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the password that is needed to authenticate server-specific monitoring.

[**monitoruser**](maxscale-servers.md#monitoruser)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the username used for authentication in server‑specific monitorin&#x67;**.**

[**persistmaxtime**](maxscale-servers.md#persistmaxtime)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`&#x20;
* Description: Shows how long a connection can stay in the persistent pool before being discarded.

[**persistpoolmax**](maxscale-servers.md#persistpoolmax)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Defines the server connection pool's maximum size.

[**port**](maxscale-servers.md#port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`&#x20;
* Description: Identifies the port that connections are accepted by the backend server.

[**priority**](maxscale-servers.md#priority)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Description: Sets the server's priority for selecting the main node.

[**private\_address**](maxscale-servers.md#private_address)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: An alternate hostname or IP address is used for internal communications.

[**proxy\_protocol**](maxscale-servers.md#proxy_protocol)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Allows the original client IP address and port to be forwarded to backend servers using PROXY protocol headers.

[**rank**](maxscale-servers.md#rank)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`&#x20;
* Description: Specifies the server's priority when making routing decisions.

[**replication\_custom\_options**](maxscale-servers.md#replication_custom_options)

* Type: string
* Default: None
* Dynamic: Yes
* Description: Defines custom options added to replication commands for server.

[**socket**](maxscale-servers.md#socket)

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the Unix domain socket route that is used to establish a connection with the backend server.

[**use\_service\_credentials**](maxscale-servers.md#use_service_credentials)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether service credentials are used for backend authentication before switching to the client user.

### reference/maxscale-authenticators

#### [maxscale-gssapi-client-authenticator](maxscale-authenticators/maxscale-gssapi-client-authenticator.md)

**Settings**

[**gssapi\_keytab\_path**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md#gssapi_keytab_path)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default
* Description: Specifies the location of the GSSAPI authentication-related Kerberos keytab file.&#x20;

[**principal\_name**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md#principal_name)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`&#x20;
* Description: Defines the service principal name used in GSSAPI authentication.

#### [maxscale-mariadb-mysql-authenticator](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)

**Settings**

[**log\_password\_mismatch**](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md#log_password_mismatch)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Allows tracking of password hash mismatches during authentication.

#### [maxscale-pam-authenticator](maxscale-authenticators/maxscale-pam-authenticator.md)

**Settings**

[**pam\_backend\_mapping**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_backend_mapping)

* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`&#x20;
* Description: Manages the mapping of PAM-authenticated users to backend authentication.

[**pam\_mapped\_pw\_file**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_mapped_pw_file)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: None
* Description: Specifies a JSON file containing passwords for PAM-mapped users.

[**pam\_mode**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_mode)

* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`&#x20;
* Description: Defines the PAM authentication mode for client login.

[**pam\_use\_cleartext\_plugin**](maxscale-authenticators/maxscale-pam-authenticator.md#pam_use_cleartext_plugin)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Enables cleartext password authentication between the client and MaxScale when using PAM.

### reference/maxscale-filters

#### [maxscale-binlog-filter](maxscale-filters/maxscale-binlog-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-binlog-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Excludes events, which match the specified regular expression.

[**match**](maxscale-filters/maxscale-binlog-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Includes only events that match the given regular expression.

[**rewrite\_dest**](maxscale-filters/maxscale-binlog-filter.md#rewrite_dest)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the replacement pattern that replication events use to rewrite statements.

[**rewrite\_src**](maxscale-filters/maxscale-binlog-filter.md#rewrite_src)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Describes the pattern that is used to match statements in replication events for rewriting.

#### [maxscale-cache](maxscale-filters/maxscale-cache.md)

**Settings**

[**cache\_in\_transactions**](maxscale-filters/maxscale-cache.md#cache_in_transactions)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`&#x20;
* Description: Manages how the cache is used and updated during transactions.

[**cached\_data**](maxscale-filters/maxscale-cache.md#cached_data)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`&#x20;
* Description: Determines whether cached data remains thread-specific or shared across threads.

[**clear\_cache\_on\_parse\_errors**](maxscale-filters/maxscale-cache.md#clear_cache_on_parse_errors)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Controls whether the cache is cleared when modifying statements are not parsed correctly.

[**debug**](maxscale-filters/maxscale-cache.md#debug)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Uses a bitmask value to control the cache's debug logging level.

[**enabled**](maxscale-filters/maxscale-cache.md#enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Manages whether the cache is enabled or disabled at startup.

[**hard\_ttl**](maxscale-filters/maxscale-cache.md#hard_ttl)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)
* Description: Specifies how long cached data can last before being deleted and reloaded.

[**invalidate**](maxscale-filters/maxscale-cache.md#invalidate)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`&#x20;
* Description: Manages how cached data is invalidated when changes occur.

[**max\_count**](maxscale-filters/maxscale-cache.md#max_count)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Specifies the maximum amount of data that cache can store.

[**max\_resultset\_rows**](maxscale-filters/maxscale-cache.md#max_resultset_rows)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Defines the maximum number of rows in a result set that can be cached.

[**max\_resultset\_size**](maxscale-filters/maxscale-cache.md#max_resultset_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Specifies the maximum result set size that can be cached.

[**max\_size**](maxscale-filters/maxscale-cache.md#max_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Defines the maximum total size of the cache.

[**rules**](maxscale-filters/maxscale-cache.md#rules)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)
* Description: Specifies the file path containing caching rules.

[**selects**](maxscale-filters/maxscale-cache.md#selects)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`&#x20;
* Description: Controls whether SELECT statements are considered to be cacheable or validated before caching.

[**soft\_ttl**](maxscale-filters/maxscale-cache.md#soft_ttl)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)
* Description: Determines how long cached data is used before being refreshed from the backend.

[**storage**](maxscale-filters/maxscale-cache.md#storage)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`&#x20;
* Description: Defines the storage module used by the cache.

[**storage\_options**](maxscale-filters/maxscale-cache.md#storage_options)

* Type: string
* Mandatory: No
* Dynamic: No
* Default:
* Description: Deprecated. Previously used to pass configuration options to the storage module.

[**timeout**](maxscale-filters/maxscale-cache.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `5s`&#x20;
* Description: Specifies the timeout for processes involving external storage backends.

[**users**](maxscale-filters/maxscale-cache.md#users)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`&#x20;
* Description: Manages whether cached data is stored separately for each user or shared between users.

**`storage_memcached`**

[**max\_value\_size**](maxscale-filters/maxscale-cache.md#max_value_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi
* Description: Defines the maximum size of a value that can be stored in the cache.

[**server**](maxscale-filters/maxscale-cache.md#server)

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the Memcached server address. The default port is 11211 is used when no port is provided.

**`storage_redis`**

[**password**](maxscale-filters/maxscale-cache.md#password)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Password used for authentication.

[**server**](maxscale-filters/maxscale-cache.md#server)

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No
* Description: Defines the Redis server address. The default port is 6379 is used when no port is provided.

[**ssl**](maxscale-filters/maxscale-cache.md#ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Enable SSL when connectign to the Redis server.

[**ssl\_ca**](maxscale-filters/maxscale-cache.md#ssl_ca)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the CA certificate used to verify the Redis server certificate.

[**ssl\_cert**](maxscale-filters/maxscale-cache.md#ssl_cert)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines the SSL client certificate used when connecting to the Redis server.

[**ssl\_key**](maxscale-filters/maxscale-cache.md#ssl_key)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the private key for the SSL client that is used to connect to the Redis server.&#x20;

[**username**](maxscale-filters/maxscale-cache.md#username)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Username used for authentication.

#### [maxscale-comment-filter](maxscale-filters/maxscale-comment-filter.md)

**Settings**

[**inject**](maxscale-filters/maxscale-comment-filter.md#inject)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the comment injected before statements.

#### [maxscale-consistent-critical-read-filter](maxscale-filters/maxscale-consistent-critical-read-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-consistent-critical-read-filter.md#count)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Defines the number of statements that are sent to the primary following a data-modifying statement.

[**global**](maxscale-filters/maxscale-consistent-critical-read-filter.md#global)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Manages whether write activity from a single connection affects routing behavior for all connections.

[**ignore**](maxscale-filters/maxscale-consistent-critical-read-filter.md#ignore)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines a pattern for queries that should be ignored.

[**match**](maxscale-filters/maxscale-consistent-critical-read-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies a pattern for statements that cause re-routing of statements.

[**options**](maxscale-filters/maxscale-consistent-critical-read-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`&#x20;
* Description: Defines regular expression options used with match and ignore.

[**time**](maxscale-filters/maxscale-consistent-critical-read-filter.md#time)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`&#x20;
* Description: Determines the time range during which statements are directed to the primary following a data-modifying statement.

#### [maxscale-ldi-filter](maxscale-filters/maxscale-ldi-filter.md)

**Settings**

[**host**](maxscale-filters/maxscale-ldi-filter.md#host)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`&#x20;
* Description: Specifies the S3 object storage host.

[**key**](maxscale-filters/maxscale-ldi-filter.md#key)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Description: Defines the S3 access key used for authentication.

[**no\_verify**](maxscale-filters/maxscale-ldi-filter.md#no_verify)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: TLS certificate verification is disabled for object storage when enabled.

[**port**](maxscale-filters/maxscale-ldi-filter.md#port)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Description: Defines the port used to connect to the S3 object storage.

[**protocol\_version**](maxscale-filters/maxscale-ldi-filter.md#protocol_version)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2
* Description: Specifies the protocol version used to communicate with object storage.

[**region**](maxscale-filters/maxscale-ldi-filter.md#region)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`&#x20;
* Description: Defines the S3 region that contains the data.

[**secret**](maxscale-filters/maxscale-ldi-filter.md#secret)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Description: Describes the S3 secret key that is used for verification.

[**use\_http**](maxscale-filters/maxscale-ldi-filter.md#use_http)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables unencrypted HTTP communication with the object storage when set to true.

#### [maxscale-masking-filter](maxscale-filters/maxscale-masking-filter.md)

**Settings**

[**check\_subqueries**](maxscale-filters/maxscale-masking-filter.md#check_subqueries)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether masking rules are applied to subqueries.

[**check\_unions**](maxscale-filters/maxscale-masking-filter.md#check_unions)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Controls whether masking rules are applied to the UNION queries.

[**check\_user\_variables**](maxscale-filters/maxscale-masking-filter.md#check_user_variables)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether user variables are applied to user variables.

[**large\_payload**](maxscale-filters/maxscale-masking-filter.md#large_payload)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`&#x20;
* Description: Controls how payloads larger than 16MB are managed by the masking filter.

[**prevent\_function\_usage**](maxscale-filters/maxscale-masking-filter.md#prevent_function_usage)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether queries using functions on masked columns are rejected.

[**require\_fully\_parsed**](maxscale-filters/maxscale-masking-filter.md#require_fully_parsed)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Determines whether statements that cannot be fully parsed are rejected.

[**rules**](maxscale-filters/maxscale-masking-filter.md#rules)

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Determines the path to the file containing masking rules.

[**treat\_string\_arg\_as\_field**](maxscale-filters/maxscale-masking-filter.md#treat_string_arg_as_field)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages if functions' string parameters are managed as fields for masking.

[**warn\_type\_mismatch**](maxscale-filters/maxscale-masking-filter.md#warn_type_mismatch)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`&#x20;
* Description: Controls whether a column with an unsupported type is matched by a masking rule and whether a warning is logged.

#### [maxscale-maxrows-filter](maxscale-filters/maxscale-maxrows-filter.md)

**Settings**

[**debug**](maxscale-filters/maxscale-maxrows-filter.md#debug)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`&#x20;
* Description: Manages the level of debug logging for the MaxRows filter.

[**max\_resultset\_return**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_return)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`&#x20;
* Description: Regulates the response that is sent to the client when the limitations defined by the results are exceeded.

[**max\_resultset\_rows**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_rows)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)
* Description: Specifies the maximum number of rows allowed in a result set returned to the client.

[**max\_resultset\_size**](maxscale-filters/maxscale-maxrows-filter.md#max_resultset_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`&#x20;
* Description: Restricts the size of a resultset that can be returned to the client; larger resultsets are replaced with an empty result.

#### [maxscale-named-server-filter](maxscale-filters/maxscale-named-server-filter.md)

**Settings**

[**matchXY**](maxscale-filters/maxscale-named-server-filter.md#matchXY)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a numbered regex pattern to match SQL queries and apply a corresponding routing target when the pattern is matched.

[**options**](maxscale-filters/maxscale-named-server-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`&#x20;
* Description: Describes the collection and matching process for the matchXY regular expressions (e.g., case sensitivity or extended syntax).

[**source**](maxscale-filters/maxscale-named-server-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits the filter to client connections from particular IP addresses or patterns; the regex rules will only be applied to sessions that match.

[**targetXY**](maxscale-filters/maxscale-named-server-filter.md#targetXY)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines the routing hint used to direct queries that match the corresponding matchXY pattern to specific server or roles.

[**user**](maxscale-filters/maxscale-named-server-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limit the filters to sessions authenticated with a specific username; the routing hints and regex rules will only be applied to matching users.

#### [maxscale-query-log-all-filter](maxscale-filters/maxscale-query-log-all-filter.md)

**Settings**

[**append**](maxscale-filters/maxscale-query-log-all-filter.md#append)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Defines whether a new routing hint is added to existing ones or replaces them when applied to matching queries.

[**duration\_unit**](maxscale-filters/maxscale-query-log-all-filter.md#duration_unit)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`&#x20;
* Description: Defines the time unit used for logging durations.

[**exclude**](maxscale-filters/maxscale-query-log-all-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern to exclude queries from matching and filtering.

[**filebase**](maxscale-filters/maxscale-query-log-all-filter.md#filebase)

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the base filename for session log files with unique session identifiers appended to create individual output files.

[**flush**](maxscale-filters/maxscale-query-log-all-filter.md#flush)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Manages whether log files are immediately flushed to disk after each write operation.

[**log\_data**](maxscale-filters/maxscale-query-log-all-filter.md#log_data)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`&#x20;
* Description: Specifies the fields, such as query details, user, timing, and execution metadata, that are present in each log entry.

[**log\_type**](maxscale-filters/maxscale-query-log-all-filter.md#log_type)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`&#x20;
* Description: Defines the logging output type, such as per-session files, a unified log file, or standard output.

[**match**](maxscale-filters/maxscale-query-log-all-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a regex pattern for queries ti include and process by the filter.

[**newline\_replacement**](maxscale-filters/maxscale-query-log-all-filter.md#newline_replacement)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`&#x20;
* Description: Specifies the string that is used to substitute newline characters in logged queries so that the log output is consistent and readable.

[**options**](maxscale-filters/maxscale-query-log-all-filter.md#options)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`&#x20;
* Description: Defines the regex matching behavior (case sensitivity and extended syntax) for filter queries.

[**separator**](maxscale-filters/maxscale-query-log-all-filter.md#separator)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`&#x20;
* Description: Specifies the string used to separate fields within each log entry.

[**source**](maxscale-filters/maxscale-query-log-all-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Limits logging to sessions that originate from specific client source addresses.

[**source\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md#source_exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Description: Defines a regex pattern for excluding requests from specified client IP addresses or hosts from logging.

[**source\_match**](maxscale-filters/maxscale-query-log-all-filter.md#source_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Description: Defines a regex pattern to include only queries from specific client IP addresses or hosts from logging.

[**use\_canonical\_form**](maxscale-filters/maxscale-query-log-all-filter.md#use_canonical_form)

* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Log queries in canonical format,replacing user-defined constants with placeholders to ensure consistent and secure output.

[**user**](maxscale-filters/maxscale-query-log-all-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Limits logging to sessions initiated by a specific username.

[**user\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md#user_exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Description: Defines a regex pattern that prevent requests from specific users from being logged.

[**user\_match**](maxscale-filters/maxscale-query-log-all-filter.md#user_match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Description: Specifies a regex pattern to include queries only from specific users for logging.

#### [maxscale-regex-filter](maxscale-filters/maxscale-regex-filter.md)

**Settings**

[**log\_file**](maxscale-filters/maxscale-regex-filter.md#log_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Identifies a file where all queries, matched and unmatched, are logged, mainly for diagnostic purposes.

[**log\_trace**](maxscale-filters/maxscale-regex-filter.md#log_trace)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Allows runtime logging of matched and unmatched queries with replacements at the info level for diagnostic purposes.

[**match**](maxscale-filters/maxscale-regex-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the regex pattern in SQL statements that filter should identify and replace.

[**options**](maxscale-filters/maxscale-regex-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`&#x20;
* Description: Determines how the match regex pattern is compiled, including case sensitivity and extended syntax.

[**replace**](maxscale-filters/maxscale-regex-filter.md#replace)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the string that will replace SQL query parts that `match` the specific pattern.

[**source**](maxscale-filters/maxscale-regex-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Restricts the match-and-replace filter to client connections originating from a specified address.

[**user**](maxscale-filters/maxscale-regex-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits the match-and-replace filter to sessions initiated by a specific username.

#### [maxscale-rewrite-filter](maxscale-filters/maxscale-rewrite-filter.md)

**Settings**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Defines whether template matching is case-sensitive by default.

[**log\_replacement**](maxscale-filters/maxscale-rewrite-filter.md#log_replacement)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Allows logging of query replacements at the NOTICE level for monitoring and debugging.

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`&#x20;
* Description: Overrides the template's default regex grammar, allowing it to be used with alternative regex engines such as `ECMAScript` or `Posix`.

[**template\_file**](maxscale-filters/maxscale-rewrite-filter.md#template_file)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value
* Description: Specifies the file path to the template used by the filter.

**Settings per template in the template file**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: From maxscale.cnf
* Description: Overrides the global template configuration to specify whether pattern matching is case-sensitive.

[**continue\_if\_matched**](maxscale-filters/maxscale-rewrite-filter.md#continue_if_matched)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Description: Identifies whether to use subsequent templates on a query once the previous template has been matched and replaced.

[**ignore\_whitespace**](maxscale-filters/maxscale-rewrite-filter.md#ignore_whitespace)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Description: Specifies whether whitespace differences between the template and SQL inout should be ignored during matching.&#x20;

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)

* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf
* Description: Defines the default tes such as `Native`, `ECMAScript`, and `POSIX`.

[**what\_if**](maxscale-filters/maxscale-rewrite-filter.md#what_if)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Description: Simulates replacements without affecting queries and logs any possible changes to the NOTICE level.

#### [maxscale-tee-filter](maxscale-filters/maxscale-tee-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-tee-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern to exclude queries from processing or matching.

[**match**](maxscale-filters/maxscale-tee-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern to include only queries that match it for processing or filtering.

[**options**](maxscale-filters/maxscale-tee-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`&#x20;
* Description: Determines how regular expressions are parsed, including case sensitivity and extended syntax.

[**service**](maxscale-filters/maxscale-tee-filter.md#service)

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none
* Description: Specifies the service for which queries are replicated; deprecated in favor of the target parameter.

[**source**](maxscale-filters/maxscale-tee-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits query replication to sessions that start from a specific client IP address.

[**sync**](maxscale-filters/maxscale-tee-filter.md#sync)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Allows synchronous routing, ensuring queries are executed on both the main and branch targets before continuing; branch failures close the client connection.

[**target**](maxscale-filters/maxscale-tee-filter.md#target)

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none
* Description: Specifies the branch target, which is the service or server where queries will be replicated.

[**user**](maxscale-filters/maxscale-tee-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Restricts query replication to sessions initiated by a specific username.

#### [maxscale-throttle-filter](maxscale-filters/maxscale-throttle-filter.md)

**Settings**

[**continuous\_duration**](maxscale-filters/maxscale-throttle-filter.md#continuous_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 2s
* Description: Specifies the time interval used to decide when continuous throttling begins and finishes.

[**max\_qps**](maxscale-filters/maxscale-throttle-filter.md#max_qps)

* Type: number
* Mandatory: Yes
* Dynamic: Yes
* Description: Sets the maximum number of requests per second allowed for a session during the specific sample period.

[**sampling\_duration**](maxscale-filters/maxscale-throttle-filter.md#sampling_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms
* Description: Defines the time interval during which queries per second (QPS) are mesaured for throttling purposes.

[**throttling\_duration**](maxscale-filters/maxscale-throttle-filter.md#throttling_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies how long a session can be throttled before being disconnected by MaxScale.

#### [maxscale-top-filter](maxscale-filters/maxscale-top-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-top-filter.md#count)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`&#x20;
* Description: Sets the number of SQL statements to store and include in the report.

[**exclude**](maxscale-filters/maxscale-top-filter.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern that prevents the filter from logging specific queries.

[**filebase**](maxscale-filters/maxscale-top-filter.md#filebase)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the base name for session log files, followed by the session ID to generate unique output files.

[**match**](maxscale-filters/maxscale-top-filter.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regex pattern that only logs requests that match it, while ignoring others.

[**options**](maxscale-filters/maxscale-top-filter.md#options)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`&#x20;
* Description: Determines how the `match` and `exlcude` regex patterns are handled, including case sensitivity and extended syntax.

[**source**](maxscale-filters/maxscale-top-filter.md#source)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits logging to sessions that start from a specific client IP address.

[**user**](maxscale-filters/maxscale-top-filter.md#user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Limits logging to sessions initiated by a specific username.

#### [maxscale-workload-capture-and-replay](maxscale-filters/maxscale-workload-capture-and-replay.md)

**Settings**

[**capture\_dir**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_dir)

* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No
* Description: Specifies the directory in which session capture subdirectories are kept for each filter.

[**capture\_duration**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 0s
* Maximum: Unlimited in MaxScale, 5min in MaxScale Lite.
* Mandatory: No
* Dynamic: No
* Description: Determines how long a session capture can run; a value of `0` indicates an infinite duration.

[**capture\_size**](maxscale-filters/maxscale-workload-capture-and-replay.md#capture_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Default: 0
* Maximum: Unlimited in MaxScale, 10MB in MaxScale Lite.
* Mandatory: No
* Dynamic: No
* Description: Specifies the maximum session capture size in bytes; a value of 0 indicates no size restriction.

[**start\_capture**](maxscale-filters/maxscale-workload-capture-and-replay.md#start_capture)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Mandatory: No
* Dynamic: No
* Description: Determines whether session capture starts automatically when MaxScale starts.

### reference/maxscale-monitors

#### [common-monitor-parameters](maxscale-monitors/common-monitor-parameters.md)

**Settings**

[**backend\_connect\_attempts**](maxscale-monitors/common-monitor-parameters.md#backend_connect_attempts)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`&#x20;
* Description: Specifies the maximum number of times MaxScale attempts to connect to a backend during each monitoring cycle.

[**backend\_connect\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_connect_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`&#x20;
* Description: Sets the maximum amount of time allowed to connect to a backend server; deprecated in favor of backend timeout.

[**backend\_read\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_read_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`&#x20;
* Description: Specifies the timeout for reading query resuts from a backend server. Deprecated and ignored since MaxScale 25.08.0.&#x20;

[**backend\_write\_timeout**](maxscale-monitors/common-monitor-parameters.md#backend_write_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`&#x20;
* Description: Deprecated and ignored since MaxScale 25.10.0.&#x20;

[**disk\_space\_check\_interval**](maxscale-monitors/common-monitor-parameters.md#disk_space_check_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`&#x20;
* Description: Sets the minimum interval between disk space checks; a value of `0` disables automatic checks.

[**disk\_space\_threshold**](maxscale-monitors/common-monitor-parameters.md#disk_space_threshold)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines the disk usage limit (per path) that creates alerts. It can be set globally in the monitor or individually per server if disk configurations differ.

[**events**](maxscale-monitors/common-monitor-parameters.md#events)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events
* Description: Specifies which server events cause a script to execute; if not provided, it defaults to all events.&#x20;

[**journal\_max\_age**](maxscale-monitors/common-monitor-parameters.md#journal_max_age)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`&#x20;
* Description: Sets the maximum age of journal files; older files are deleted when the monitor starts.

[**module**](maxscale-monitors/common-monitor-parameters.md#module)

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies which monitor module will be used, such as `mariadbmon` or `orgaleramon`.

[**monitor\_interval**](maxscale-monitors/common-monitor-parameters.md#monitor_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`&#x20;
* Description: Determines how often the monitor checks and updates the status of servers; shorter intervals result in more frequent checks.

[**password**](maxscale-monitors/common-monitor-parameters.md#password)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the password for the user defined in the user parameter; overrides older `passwd` settings.

[**primary\_state\_sql**](maxscale-monitors/common-monitor-parameters.md#primary_state_sql)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies custom SQL commands to be executed on a primary (Master) server when it achieves Master status or when the monitor starts, allowing for role-based configuration changes.

[**replica\_state\_sql**](maxscale-monitors/common-monitor-parameters.md#replica_state_sql)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies custom SQL commands to run on a replica (Slave) server when they get Slave status or when the monitor starts, allowing role-based configuration changes.

[**role**](maxscale-monitors/common-monitor-parameters.md#role)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a user role to activate when the monitor connects to a server, providing privilege separation between monitoring and service operations.

[**script**](maxscale-monitors/common-monitor-parameters.md#script)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a command to execute when the server status changes, with the help of placeholders (such as `$INITIATOR`, `$EVENT`, and `$MASTERLIST`) that MaxScale replaces with relevant server information; script output is reported based on message prefixes.

[**script\_timeout**](maxscale-monitors/common-monitor-parameters.md#script_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`&#x20;
* Description: Sets a maximum period of time a script can execute; if this limit exceeds the allowed duration, the script is issued `SIGTERM`, followed by `SIGKILL` if it does not stop.

[**servers**](maxscale-monitors/common-monitor-parameters.md#servers)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Provides a comma-separated list of servers that the monitor will track and manage.

[**user**](maxscale-monitors/common-monitor-parameters.md#user)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the monitor's username for connecting to backend servers; if defined, this overrides the server's `monitoruser`. &#x20;

#### [galera-monitor](maxscale-monitors/galera-monitor.md)

**Settings**

[**available\_when\_donor**](maxscale-monitors/galera-monitor.md#available_when_donor)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description: Allows Galera nodes to continue performing normal operations while acting as donors during non-blocking SST methods, preventing them from losing synchronized or read/write state.

[**disable\_master\_failback**](maxscale-monitors/galera-monitor.md#disable_master_failback)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description: Prevents MaxScale from restoring the original node to primary status after a failover; the new primary retains the role while running.

[**disable\_master\_role\_setting**](maxscale-monitors/galera-monitor.md#disable_master_role_setting)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description: Disables automatic primary and replica role assignment in a Galera cluster; when enabled, only the Synced status is assigned.

[**root\_node\_as\_master**](maxscale-monitors/galera-monitor.md#root_node_as_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description: Ensures that only the Galera node with `wsrep_local_index = 0` can be chosen as the primary for writes, enabling many MaxScale instances to use the same primary node.

[**set\_donor\_nodes**](maxscale-monitors/galera-monitor.md#set_donor_nodes)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description:  Controls whether the `wsrep_sst_donor` global variable is set on each replica node, listing eligible donor nodes for SST in a sorted order based on priority or `wsrep_local_index`. &#x20;

[**use\_priority**](maxscale-monitors/galera-monitor.md#use_priority)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes
* Description: Allows the monitor to automatically select the writing node and manage controlled node replacements in a Galera cluster while keeping server priorities into account.

#### [mariadb-monitor](maxscale-monitors/mariadb-monitor.md)

**Settings**

[**assume\_unique\_hostnames**](maxscale-monitors/mariadb-monitor.md#assume_unique_hostnames)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: When enabled, the monitor assumes that the server hostnames and ports in the configuration match those provided by the servers, resulting in accurate topology identification and support for cluster actions such as failover and switching.

[**cooperative\_monitoring\_locks**](maxscale-monitors/mariadb-monitor.md#cooperative_monitoring_locks)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`&#x20;
* Description: Controls how a monitor achieves exclusive locks in multi-MaxScale configurations; decides whether a monitor becomes primary based on the majority of all servers, only running servers, or none at all.

[**enforce\_read\_only\_servers**](maxscale-monitors/mariadb-monitor.md#enforce_read_only_servers)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Automatically sets `read_only` on any writable servers that are not the primary and are not under maintenance, ensuring that non-primary servers remain read-only.

[**enforce\_read\_only\_slaves**](maxscale-monitors/mariadb-monitor.md#enforce_read_only_slaves)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Automatically sets `read_only` flag on writable replica servers, allowing only privileged users to write; the primary server is unaffected.

[**enforce\_writable\_master**](maxscale-monitors/mariadb-monitor.md#enforce_writable_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Ensures that the primary server is always writable by automatically disabling read-only mode during monitoring.

[**failcount**](maxscale-monitors/mariadb-monitor.md#failcount)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`&#x20;
* Description: Specifies how many consecutive monitor cycles a primary must fail before being considered down and requiring failover or primary reselection.

[**maintenance\_on\_low\_disk\_space**](maxscale-monitors/mariadb-monitor.md#maintenance_on_low_disk_space)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: When disk space is low, non-primary servers are automatically put into maintenance mode, which stops them from being used for sessions or failover unless they are manually removed.

[**master\_conditions**](maxscale-monitors/mariadb-monitor.md#master_conditions)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`&#x20;
* Description: Specifies additional requirements for a server to be considered primary, such as the availability of connected or running replicas, sufficient disk space, or agreement with supporting monitors.

[**script\_max\_replication\_lag**](maxscale-monitors/mariadb-monitor.md#script_max_replication_lag)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`&#x20;
* Description: Sets a replication lag threshold (in seconds) that executes the monitor script when exceeded (`rlag_above`) or returned below (`rlag_below`); negative values disable this feature.

[**slave\_conditions**](maxscale-monitors/mariadb-monitor.md#slave_conditions)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`&#x20;
* Description: Specifies additional requirements for a server to be identified as a Slave, such as being connected to a running or writable primary; several conditions can be coupled using an `enum` mask.

**Settings for Backup operations**

[**backup\_storage\_address**](maxscale-monitors/mariadb-monitor.md#backup_storage_address)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Provides the backup storage server's hostname or IP address. The server does not have to run MariaDB or be monitored by MaxScale. MaxScale connects via SSH, and the storage must have enough disk space to accommodate all backups.

[**backup\_storage\_path**](maxscale-monitors/mariadb-monitor.md#backup_storage_path)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the path to the backup storage host where backups will be saved. The SSH user specified in `ssh_user` must have full read and write access to this directory.

[**mariadb\_backup\_parallel**](maxscale-monitors/mariadb-monitor.md#mariadb_backup_parallel)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`&#x20;
* Description: Defines the number of parallel threads to use while running `mariadb-backup`. This value is used as the `--parallel=<val>` for `mariadb-backup --backup`. Increasing this value can accelerate backups on systems with multiple CPUs and fast I/O.

[**mariadb\_backup\_use\_memory**](maxscale-monitors/mariadb-monitor.md#mariadb_backup_use_memory)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `1G`&#x20;
* Description: Specifies how much memory `mariadb-backup` should use during the `--prepare` phase. This value is specified with the `--use-memory=<val>`. Setting it to an empty string disables the option and allows `mariadb-backup` to utilize the internal default. Increasing RAM can accelerate backup preparation, especially for large datasets.

[**rebuild\_port**](maxscale-monitors/mariadb-monitor.md#rebuild_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`&#x20;
* Description: Specifies the TCP port on which the source server will listen for the rebuild (SST) connection during a state transfer. This port must be open (not blocked by firewalls) and free (not in use by another process). If another process uses the port when the rebuild begins, MaxScale will attempt to terminate it to free up the port.

[**ssh\_check\_host\_key**](maxscale-monitors/mariadb-monitor.md#ssh_check_host_key)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether MaxScale verifies the SSH host key when connecting to a backend server.  When set to `true`, MaxScale requires that the backend server’s host key is already present in the `known_hosts` file of the user running MaxScale. This ensures the authenticity of the server during SSH connections. &#x20;

[**ssh\_keyfile**](maxscale-monitors/mariadb-monitor.md#ssh_keyfile)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the SSH private key file used by MaxScale to authenticate when connecting to backend servers.

[**ssh\_port**](maxscale-monitors/mariadb-monitor.md#ssh_port)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`&#x20;
* Description: Uses port for SSH connections when executing remote commands on backend servers.

[**ssh\_timeout**](maxscale-monitors/mariadb-monitor.md#ssh_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Specifies the maximum duration allowed for SSH commands during a rebuild before timing out.

[**ssh\_user**](maxscale-monitors/mariadb-monitor.md#ssh_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the SSH username for logging in to backend servers to execute commands.

**Settings for Cluster manipulation operations**

[**auto\_failover**](maxscale-monitors/mariadb-monitor.md#auto_failover)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`&#x20;
* Description: Enables or disables automated primary failover, which allows MaxScale to select a new primary if the current one fails.

[**auto\_rejoin**](maxscale-monitors/mariadb-monitor.md#auto_rejoin)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Allows automatic redirection of servers to duplicate from the current primary, resulting in a 1-primary-N-replicas architecture.

[**demotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md#demotion_sql_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a SQL file to execute when a server is downgraded; equivalent to `promotion_sql_file`.

[**enforce\_simple\_topology**](maxscale-monitors/mariadb-monitor.md#enforce_simple_topology)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Promotes a 1-primary-N-replicas cluster configuration, automatically reconnecting servers and deleting unnecessary replication sources to maintain a simple topology.

[**failover\_timeout**](maxscale-monitors/mariadb-monitor.md#failover_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`&#x20;
* Description: Sets the maximum time allowed for a failover operation before it is terminated and automatic failover is disabled.

[**handle\_events**](maxscale-monitors/mariadb-monitor.md#handle_events)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Manages whether the monitor tracks and updates scheduled events on servers during offers, demotions, and rejoins.

[**master\_failure\_timeout**](maxscale-monitors/mariadb-monitor.md#master_failure_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Specifies the duration MaxScale waits before considering a primary server as failed.

[**promotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md#promotion_sql_file)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a file of SQL statements to execute on a server during promotion to primary.

[**replication\_master\_ssl**](maxscale-monitors/mariadb-monitor.md#replication_master_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enables SSL encryption for replication by configuring generated replication commands to use secure connections.

[**replication\_password**](maxscale-monitors/mariadb-monitor.md#replication_password)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the password used by the replication user for authentication.

[**replication\_user**](maxscale-monitors/mariadb-monitor.md#replication_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the username used for replication authentication when configuring replica connections.

[**servers\_no\_promotion**](maxscale-monitors/mariadb-monitor.md#servers_no_promotion)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**\[switchover\_on\_low\_disk\_space`\*\*](../reference/maxscale-monitors/mariadb-monitor.md#switchover_on_low_disk_space`\*\*)**

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Lists the servers that are excluded from being promoted to primary during failover or automatic selection.

[**switchover\_timeout**](maxscale-monitors/mariadb-monitor.md#switchover_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`&#x20;
* Description: Defines the maximum time allowed for switchover and rejoin operations before timing out.

[**verify\_master\_failure**](maxscale-monitors/mariadb-monitor.md#verify_master_failure)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Enables verification of primary server failure using replica status before triggering automatic failover.

**Settings for Primary server write test**

[**write\_test\_fail\_action**](maxscale-monitors/mariadb-monitor.md#write_test_fail_action)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes
* Description: Defines the action to consider when the primary fails a write text, either logging the failure or triggering a failover.

[**write\_test\_interval**](maxscale-monitors/mariadb-monitor.md#write_test_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Dynamic: Yes
* Default: 0s
* Description: Sets the interval after which a write test is performed on the primary if no changes are detected.

[**write\_test\_table**](maxscale-monitors/mariadb-monitor.md#write_test_table)

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`&#x20;
* Description: Specifies the fully qualified table used by the monitor to perform primary server write tests.

### reference/maxscale-protocols

#### [maxscale-mariadb-protocol-module](maxscale-protocols/maxscale-mariadb-protocol-module.md)

**Settings**

[**allow\_replication**](maxscale-protocols/maxscale-mariadb-protocol-module.md#allow_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Manages whether the replication protocol is permitted through this listener.

#### [maxscale-nosql-protocol-module](maxscale-protocols/maxscale-nosql-protocol-module.md)

**Settings**

[**authentication\_db**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_db)

* Type: string
* Mandatory: No
* Default: `"NoSQL"`&#x20;
* Description: Specifies the database that stores NoSQL account information for authentication.

[**authentication\_key\_id**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_key_id)

* Type: string
* Mandatory: No
* Default: `""`&#x20;
* Description: Specifies the encryption key ID used to encrypt NoSQL account information in the database.

[**authentication\_password**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_password)

* Type: string
* Mandatory: No
* Default: `""`&#x20;
* Description: Specifies the password for the NoSQL authentication user.

[**authentication\_required**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_required)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`&#x20;
* Description: Determines whether clients are required to authenticate before accessing the service.

[**authentication\_shared**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_shared)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`&#x20;
* Description: Controls whether NoSQL account information is stored in a shared or private manner.

[**authentication\_user**](maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_user)

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.
* Description: Specifies the user used to access and manage shared NoSQL account information.

[**authorization\_enabled**](maxscale-protocols/maxscale-nosql-protocol-module.md#authorization_enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`&#x20;
* Description: Enables or disables NoSQL protocol–level authorization for user management commands.

[**auto\_create\_databases**](maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_databases)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`&#x20;
* Description: Controls whether databases are automatically created when required.

[**auto\_create\_tables**](maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_tables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`&#x20;
* Description: Controls whether tables are automatically created within existing databases when required.

[**cursor\_timeout**](maxscale-protocols/maxscale-nosql-protocol-module.md#cursor_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Default: `60s`&#x20;
* Description: Sets the maximum idle time before an inactive cursor is automatically closed.

[**debug**](maxscale-protocols/maxscale-nosql-protocol-module.md#debug)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`&#x20;
* Description: Manages which protocol events are logged, including incoming commands, backend SQL, and client responses.

[**host**](maxscale-protocols/maxscale-nosql-protocol-module.md#host)

* Type: string
* Mandatory: No
* Default: `"%"`&#x20;
* Description: Specifies the host portion of the MariaDB user account created via the NoSQL protocol.

[**id\_length**](maxscale-protocols/maxscale-nosql-protocol-module.md#id_length)

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`&#x20;
* Description: Sets the length of the `id` column for automatically created tables.

[**internal\_cache**](maxscale-protocols/maxscale-nosql-protocol-module.md#internal_cache)

* Type: string
* Mandatory: No
* Default: ''
* Description: Specifies the internal cache to use, currently supporting only the `cache` filter. &#x20;

[**log\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md#log_unknown_command)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`&#x20;
* Description: Determines whether unsupported or unknown client commands are logged for debugging.

[**on\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md#on_unknown_command)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`&#x20;
* Description: Defines how the system responds to unrecognized client commands, either with an error or an empty result.

[**ordered\_insert\_behavior**](maxscale-protocols/maxscale-nosql-protocol-module.md#ordered_insert_behavior)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`&#x20;
* Description:  Controls whether multi-document inserts are performed completely or individually based on the `ordered` setting. &#x20;

[**password**](maxscale-protocols/maxscale-nosql-protocol-module.md#password)

* Type: string
* Mandatory: No
* Default: `""`&#x20;
* Description: Specifies the password used for backend connections when the MongoDB client is unauthenticated.

[**user**](maxscale-protocols/maxscale-nosql-protocol-module.md#user)

* Type: string
* Mandatory: No
* Default: `""`&#x20;
* Description: Specifies the username used for backend connections when the MongoDB client is unauthenticated.

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
* Description: Specifies the directory where files are archived when `expiration_mode` is set to `archive`. &#x20;

[**compression\_algorithm**](maxscale-routers/maxscale-binlogrouter.md#compression_algorithm)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`&#x20;
* Description: Defines the compression algorithm to use for archived files.

[**datadir**](maxscale-routers/maxscale-binlogrouter.md#datadir)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`&#x20;
* Description: Shows the directory where binary log files are stored.

[**ddl\_only**](maxscale-routers/maxscale-binlogrouter.md#ddl_only)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: false
* Description: When enabled, only DDL events (CREATE, ALTER, DROP) are logged, excluding data changes.

[**encryption\_cipher**](maxscale-routers/maxscale-binlogrouter.md#encryption_cipher)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`&#x20;
* Description: Defines the AES encryption mode used for securing data, such as GCM, CBC, or CTR.

[**encryption\_key\_id**](maxscale-routers/maxscale-binlogrouter.md#encryption_key_id)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the encryption key ID used to encrypt binary logs, requiring a configured key manager.

[**expiration\_mode**](maxscale-routers/maxscale-binlogrouter.md#expiration_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`&#x20;
* Description: Indicates whether expired logs are automatically deleted or archived.

[**expire\_log\_duration**](maxscale-routers/maxscale-binlogrouter.md#expire_log_duration)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s`&#x20;
* Description: Sets the duration after which binary log files expire and are eligible for purge or archiving.&#x20;

[**expire\_log\_minimum\_files**](maxscale-routers/maxscale-binlogrouter.md#expire_log_minimum_files)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`&#x20;
* Description: Determines the minimum number of binary log files to keep during automatic purging.&#x20;

[**net\_timeout**](maxscale-routers/maxscale-binlogrouter.md#net_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `10s`&#x20;
* Description: Sets the network connection and read timeout for the primary server connection.

[**number\_of\_noncompressed\_files**](maxscale-routers/maxscale-binlogrouter.md#number_of_noncompressed_files)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`&#x20;
* Description: Specifies the minimum number of binary log files to keep up uncompressed.

[**rpl\_semi\_sync\_slave\_enabled**](maxscale-routers/maxscale-binlogrouter.md#rpl_semi_sync_slave_enabled)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: false
* Dynamic: Yes
* Description: Enables semi-synchronous replication from a MariaDB server by sending acknowledgements for received events.

[**select\_master**](maxscale-routers/maxscale-binlogrouter.md#select_master)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Selects a primary server for replication automatically from a list of servers that are monitored and have Master status.

[**server\_id**](maxscale-routers/maxscale-binlogrouter.md#server_id)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`&#x20;
* Description: Mentions the server ID used by MaxScale for replication and serving binary logs to replicas.

#### [maxscale-diff](maxscale-routers/maxscale-diff.md)

**Settings**

[**explain**](maxscale-routers/maxscale-diff.md#explain)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`&#x20;
* Description: Determines whether queries are EXPLAINed on the main server, other servers, or both.

[**explain\_entries**](maxscale-routers/maxscale-diff.md#explain_entries)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2
* Description: Sets the maximum number of times a canonical statement is EXPLAINed throughout the explain period.

[**explain\_period**](maxscale-routers/maxscale-diff.md#explain_period)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 15m
* Description: Defines the time window over which the `explain_entries` limit applies for EXPLAIN operations.

[**main**](maxscale-routers/maxscale-diff.md#main)

* Type: server
* Mandatory: Yes
* Dynamic: No
* Description: Specifes the primary server from which query results are returned to the client.

[**max\_request\_lag**](maxscale-routers/maxscale-diff.md#max_request_lag)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10
* Description: Sets the maximum allowed request la on replica servers before SELECTs are skipped to connect with the primary server.

[**on\_error**](maxscale-routers/maxscale-diff.md#on_error)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`&#x20;
* Description: Determines whether errors from replica servers close the session or are are ignored.

[**percentile**](maxscale-routers/maxscale-diff.md#percentile)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99
* Description: Defines the percentile of samples used to calculate histogram width and bin count.

[**qps\_window**](maxscale-routers/maxscale-diff.md#qps_window)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 15m
* Description: Specifies the time window over which queries per second (QPS) are calculated and logged.&#x20;

[**report**](maxscale-routers/maxscale-diff.md#report)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`&#x20;
* Description: Defines when results from main and other executions are logged: always, on discrepancy, or never.

[**reset\_replication**](maxscale-routers/maxscale-diff.md#reset_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`&#x20;
* Description: Controls whether replication on other is reset and restarted after a read-write Diff session completes.

[**retain\_faster\_statements**](maxscale-routers/maxscale-diff.md#retain_faster_statements)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5
* Description: Sets how many of the fastest statements are kept in memory for summary reporting.

[**retain\_slower\_statements**](maxscale-routers/maxscale-diff.md#retain_slower_statements)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5
* Description: Sets how many of the slowest statements are kept in memory for summary reporting.

[**samples**](maxscale-routers/maxscale-diff.md#samples)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000
* Description: Defines the number of samples collected to determine histrogram bin edges and counts.

[**service**](maxscale-routers/maxscale-diff.md#service)

* Type: service
* Mandatory: Yes
* Dynamic: No
* Description: Defines the service that Diff will operate on.

#### [maxscale-exasolrouter](maxscale-routers/maxscale-exasolrouter.md)

**Settings**

[**appearance**](maxscale-routers/maxscale-exasolrouter.md#appearance)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`&#x20;
* Description: Determines whether the Exasolrouter appears as read-only or read-write to other MaxScale components.

[**connection\_string**](maxscale-routers/maxscale-exasolrouter.md#connection_string)

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the Exasol ODBC connection string used to connect to the database.

[**preprocessor**](maxscale-routers/maxscale-exasolrouter.md#preprocessor)

* Type: String
* Mandatory: No
* Dynamic: No
* Values: `auto`, `activate-only`, `custom:<path>`, `disabled`
* Default: `auto`&#x20;
* Description: Defines how the Exasol preprocesser script is managed: auto-installed, activate-only, custom path, or disabled.

[**preprocessor\_script**](maxscale-routers/maxscale-exasolrouter.md#preprocessor_script)

* Type: String
* Mandatory: No
* Dynamic: No
* Default: "UTIL.maria\_preprocessor"
* Description: Specifies the name of a custom Exasol preprocessor script when using a custom preprocessor path.

#### [maxscale-kafkacdc](maxscale-routers/maxscale-kafkacdc.md)

**Settings**

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkacdc.md#bootstrap_servers)

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the list of Kafka brokers in `host:port` format for connecting to the cluster. &#x20;

[**cooperative\_replication**](maxscale-routers/maxscale-kafkacdc.md#cooperative_replication)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Enables coperative replication, allowing multiple MaxScale instances to replicate from the same cluster while ensuring each event is processed only once.

[**enable\_idempotence**](maxscale-routers/maxscale-kafkacdc.md#enable_idempotence)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Enables idempotent Kafka producer mode to reduce duplicate message delivery and preserve message order.

[**exclude**](maxscale-routers/maxscale-kafkacdc.md#exclude)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Excludes tables matching a specified pattern from being sent to Kafka.

[**gtid**](maxscale-routers/maxscale-kafkacdc.md#gtid)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the initial GTID position for replication; supports `newest` and `oldest` special values. &#x20;

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_mechanism)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`&#x20;
* Description: Specifies the SASL authentication mechanism for connecting to Kafka, such as `PLAIN` or `SCRAM-SHA` variants.

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_password)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the password used for SASL authentication with Kafka.

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_user)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the username used for SASL authentication with Kafka.

[**kafka\_ssl**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Enables SSL encryption for Kafka connections.

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the path to the CA certificate file for SSL Kafka connections.

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the path to the client SSL certificate file for Kafka connections.

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Specifies the path to the client SSL private key for Kafka connections.

[**match**](maxscale-routers/maxscale-kafkacdc.md#match)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Includes only tables whose combined database and table names match the specified pattern for Kafka replication.

[**read\_gtid\_from\_kafka**](maxscale-routers/maxscale-kafkacdc.md#read_gtid_from_kafka)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`&#x20;
* Description: Determines whether to read the latest GTID from Kafka on startup to resume replication.

[**send\_schema**](maxscale-routers/maxscale-kafkacdc.md#send_schema)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Controls whether table schema change events are sent as JSON objects into the Kafka stream.

[**server\_id**](maxscale-routers/maxscale-kafkacdc.md#server_id)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`&#x20;
* Description: Specifies the server ID used when connecting to the primary for replication.

[**timeout**](maxscale-routers/maxscale-kafkacdc.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`&#x20;
* Description: Defines the timeout for establishing and reading from the replication stream connection.

[**topic**](maxscale-routers/maxscale-kafkacdc.md#topic)

* Type: string
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the Kafka topic where replicated events are published.

#### [maxscale-kafkaimporter](maxscale-routers/maxscale-kafkaimporter.md)

**Settings**

[**batch\_size**](maxscale-routers/maxscale-kafkaimporter.md#batch_size)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`&#x20;
* Description: Defines the maximum number of records to buffer before committing a batch of imported data.

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkaimporter.md#bootstrap_servers)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the comma-separated list of Kafka broker addresses used to establish connections.

[**engine**](maxscale-routers/maxscale-kafkaimporter.md#engine)

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes
* Description: Specifies the storage engine used when creating tables for imported Kafka data.

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_mechanism)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`&#x20;
* Description: Specifies the SASL authentication mechanism used for Kafka connections.

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_password)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the SASL password for Kafka authentication, requiring a corresponding username.

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_user)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the SASL username for Kafka authentication, requiring a corresponding password.

[**kafka\_ssl**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`&#x20;
* Description: Enables or disables SSL encryption for Kafka connections.

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_ca)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the CA certificate file used to verify Kafka SSL connections, or defaults to the system CA.

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_cert)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Defines the SSL certificate file for Kafka connections, requiring a corresponding private key.

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_key)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies the SSL private key file for Kafka connections, requiring a corresponding certificate.

[**table\_name\_in**](maxscale-routers/maxscale-kafkaimporter.md#table_name_in)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`&#x20;
* Description: Defines whether the Kafka topic or message key is used to determine the target table for data insertion.

[**timeout**](maxscale-routers/maxscale-kafkaimporter.md#timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`&#x20;
* Description: Sets the timeout for network communication with both Kafka and MariaDB.

[**topics**](maxscale-routers/maxscale-kafkaimporter.md#topics)

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the comma-separated list of topics to subscribe to.

#### [maxscale-mirror](maxscale-routers/maxscale-mirror.md)

**Settings**

[**exporter**](maxscale-routers/maxscale-mirror.md#exporter)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`&#x20;
* Description: Specifies the destination where metrics are exported, such as log, file, or Kafka.

[**file**](maxscale-routers/maxscale-mirror.md#file)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes
* Description: Specifies the file path where metrics are written when the file exporter is enabled.

[**kafka\_broker**](maxscale-routers/maxscale-mirror.md#kafka_broker)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes
* Description: Specifies the list of Kafka brokers used to send metrics when the Kafka exporter is enabled.

[**kafka\_topic**](maxscale-routers/maxscale-mirror.md#kafka_topic)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes
* Description: Specifies the Kafka topic used to publish metrics when the Kafka exporter is enabled.

[**main**](maxscale-routers/maxscale-mirror.md#main)

* Type: target
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the primary target server whose results are returned to the client and whose availability is required for the session.

[**on\_error**](maxscale-routers/maxscale-mirror.md#on_error)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`&#x20;
* Description: Defines how backend connection failures are handled, either by ignoring them or closing the client connection.

[**report**](maxscale-routers/maxscale-mirror.md#report)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`&#x20;
* Description: Determines when query results are reported to the client, either always or only on conflicts.

#### [maxscale-readconnroute](maxscale-routers/maxscale-readconnroute.md)

**Settings**

[**master\_accept\_reads**](maxscale-routers/maxscale-readconnroute.md#master_accept_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Determines whether read queries are routed to the primary server when selecting servers.

[**max\_replication\_lag**](maxscale-routers/maxscale-readconnroute.md#max_replication_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s
* Description: Sets the maximum allowed replication lag for a server to be used for routing.

[**router\_options**](maxscale-routers/maxscale-readconnroute.md#router_options)

* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`&#x20;
* Description: Specifies which server roles are eligible for connections when establishing new router sessions.

#### [maxscale-readwritesplit](maxscale-routers/maxscale-readwritesplit.md)

**Settings**

[**causal\_reads**](maxscale-routers/maxscale-readwritesplit.md#causal_reads)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`&#x20;
* Description: Controls causal read behavior to ensure reads reflect prior writes despite replication lag.

[**causal\_reads\_timeout**](maxscale-routers/maxscale-readwritesplit.md#causal_reads_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s
* Description: Defines how long to wait for replica synchronization when using causal reads before timing out.

[**delayed\_retry**](maxscale-routers/maxscale-readwritesplit.md#delayed_retry)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables retrying failed queries for a limited time before returning an error if no server becomes available.

[**delayed\_retry\_timeout**](maxscale-routers/maxscale-readwritesplit.md#delayed_retry_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s
* Description: Specifies how long to wait before returning an error to the client when delayed retries are enabled.

[**lazy\_connect**](maxscale-routers/maxscale-readwritesplit.md#lazy_connect)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables on-demand creation of backend connections instead of opening all connections at session start.

[**master\_accept\_reads**](maxscale-routers/maxscale-readwritesplit.md#master_accept_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Determines whether the primary server can be used to handle read queries alongside replicas.

[**master\_failure\_mode**](maxscale-routers/maxscale-readwritesplit.md#master_failure_mode)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)
* Description: Defines how the router handles primary server failure and client behavior during write operations.

[**master\_reconnection**](maxscale-routers/maxscale-readwritesplit.md#master_reconnection)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)
* Description: Controls whether a session can reconnect to a new primary server if the current one becomes unavailable.

[**max\_replication\_lag**](maxscale-routers/maxscale-readwritesplit.md#max_replication_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s
* Description: Sets the maximum allowed replication lag for replicas to be eligible for routing read queries.

[**max\_slave\_connections**](maxscale-routers/maxscale-readwritesplit.md#max_slave_connections)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 0
* Max: 255
* Default: 255
* Description: Limits the maximum number of replica connections a session can use simultaneously.

[**retry\_failed\_reads**](maxscale-routers/maxscale-readwritesplit.md#retry_failed_reads)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Determines whether failed autocommit read queries are retried on another replica.

[**slave\_connections**](maxscale-routers/maxscale-readwritesplit.md#slave_connections)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255
* Description: Specifies the initial number of replica connections a session creates for routing read queries.

[**slave\_selection\_criteria**](maxscale-routers/maxscale-readwritesplit.md#slave_selection_criteria)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`&#x20;
* Description: Defines the criteria used to select replica servers for routing read queries and balancing load.

[**strict\_multi\_stmt**](maxscale-routers/maxscale-readwritesplit.md#strict_multi_stmt)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Ensures that all queries after a multi-statement query are routed to the primary to maintain session consistency.

[**strict\_sp\_calls**](maxscale-routers/maxscale-readwritesplit.md#strict_sp_calls)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Ensures that queries following a stored procedure call are routed to the primary to maintain consistency.

[**strict\_tmp\_tables**](maxscale-routers/maxscale-readwritesplit.md#strict_tmp_tables)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)
* Description: Controls whether temporary tables block reconnections, ensuring they are not lost during primary node failovers.

[**sync\_transaction**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `soft`, `hard`
* Default: `none`&#x20;
* Description: Defines how transactions are synchronized across replicas, with options for no synchronization, soft (non-blocking), or hard (blocking) synchronization.

[**sync\_transaction\_count**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_count)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 255
* Default: 1
* Description: Specifies the minimum number of backend servers required to understand a transaction before it is considered committed.

[**sync\_transaction\_max\_lag**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_max_lag)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s
* Description: Sets the maximum allowed transaction synchronization latency in soft mode before triggering synchronization.

[**sync\_transaction\_timeout**](maxscale-routers/maxscale-readwritesplit.md#sync_transaction_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s
* Description: Sets the maximum time a transaction waits for synchronization before returning or closing the connection.

[**transaction\_replay**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables replay of interrupted transactions, automatically retrying them on a replacement server if the current one fails.

[**transaction\_replay\_attempts**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_attempts)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5
* Description: Determines the maximum number of times a transaction will be retried during replay before failing.

[**transaction\_replay\_checksum**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_checksum)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`&#x20;
* Description:  Specifies the method for calculating transaction checksums to verify replayed transactions; `full` ensures complete consistency. &#x20;

[**transaction\_replay\_max\_size**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_max_size)

* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB
* Description: Sets the maximum transaction size (in bytes) that can be replayed; larger transactions are not replayed.

[**transaction\_replay\_retry\_on\_deadlock**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_retry_on_deadlock)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Automatically retries transactions that encounter a deadlock until they succeed or a checksum error occurs.

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
* Description: Prevents replaying transactions that are about to commit to avoid duplicates; enabled by default.

[**transaction\_replay\_timeout**](maxscale-routers/maxscale-readwritesplit.md#transaction_replay_timeout)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)
* Description: Sets the maximum duration for attempting transaction replay; set to `0` to disable.

[**use\_sql\_variables\_in**](maxscale-routers/maxscale-readwritesplit.md#use_sql_variables_in)

* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`&#x20;
* Description: Controls which nodes handle SELECT statements using SQL user variables; defaults to all nodes.

#### [maxscale-schemarouter](maxscale-routers/maxscale-schemarouter.md)

**Settings**

[**allow\_duplicates**](maxscale-routers/maxscale-schemarouter.md#allow_duplicates)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Disables the detection of duplicate tables on shards while it is enabled.

[**ignore\_tables**](maxscale-routers/maxscale-schemarouter.md#ignore_tables)

* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`&#x20;
* Description: Specifies a list of full table names to ignore when checking for duplicate tables.

[**ignore\_tables\_regex**](maxscale-routers/maxscale-schemarouter.md#ignore_tables_regex)

* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`&#x20;
* Description: Defines a PCRE2 regular expression to ignore specific tables when checking for duplicate databases.

[**max\_staleness**](maxscale-routers/maxscale-schemarouter.md#max_staleness)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 150s
* Description: Specifies how long stale database map entries can be used by new connections while an update is in progress.

[**refresh\_databases**](maxscale-routers/maxscale-schemarouter.md#refresh_databases)

* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`&#x20;
* Description: Allows the database map to be refreshed when a `USE...` query fails during a session.

[**refresh\_interval**](maxscale-routers/maxscale-schemarouter.md#refresh_interval)

* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`&#x20;
* Description: Sets the minimum interval between database map refreshes to maintain cluster metadata up to date.

#### [maxscale-smartrouter](maxscale-routers/maxscale-smartrouter.md)

**Settings**

[**master**](maxscale-routers/maxscale-smartrouter.md#master)

* Type: target
* Mandatory: Yes
* Dynamic: No
* Description: Identifies the primary target cluster to which all write operations are directed.

***

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
