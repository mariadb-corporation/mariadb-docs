---
description: >-
  Browse the comprehensive list of MariaDB MaxScale configuration parameters.
  This reference details valid values, default settings, and dynamic
  capabilities for servers, services, and monitors.
---
# Configuration Settings
## General
### [MaxScale](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md)
#### Filter
##### [module](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#module)
* Type: filter
* Mandatory: Yes
* Dynamic: No


#### Global Settings
##### [admin_audit](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

##### [admin_audit_exclude_methods](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit_exclude_methods)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions

##### [admin_audit_file](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_audit_file)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`

##### [admin_auth](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_auth)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

##### [admin_enabled](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_enabled)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

##### [admin_gui](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_gui)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

##### [admin_host](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_host)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`

##### [admin_jwt_algorithm](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_algorithm)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`

##### [admin_jwt_issuer](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_issuer)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`

##### [admin_jwt_key](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_key)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_jwt_max_age](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_jwt_max_age)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `24h`

##### [admin_log_auth_failures](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_log_auth_failures)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [admin_oidc_client_id](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_id)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [admin_oidc_client_secret](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_client_secret)
* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [admin_oidc_extra_options](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_extra_options)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_oidc_flow](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_flow)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `auto`, `implicit`, `code`
* Default: `auto`

##### [admin_oidc_ssl_insecure](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_ssl_insecure)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

##### [admin_oidc_url](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_oidc_url)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [admin_pam_readonly_service](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_pam_readonly_service)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_pam_readwrite_service](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_pam_readwrite_service)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_port](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_port)
* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`

##### [admin_readwrite_hosts](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_readwrite_hosts)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`

##### [admin_secure_gui](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_secure_gui)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

##### [admin_ssl_ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_ca)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_ssl_cert](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cert)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_ssl_cipher](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_cipher)
* Type: string
* Mandatory: No
* Dynamic: No

##### [admin_ssl_key](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_key)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [admin_ssl_passphrase](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_passphrase)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [admin_ssl_version](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_ssl_version)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

##### [admin_verify_url](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_verify_url)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [auth_connect_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_connect_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

##### [auto_tune](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)
* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No

##### [config_sync_cluster](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_cluster)
* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [config_sync_db](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_db)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`

##### [config_sync_interval](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`

##### [config_sync_password](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_password)
* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [config_sync_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

##### [config_sync_user](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#config_sync_user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [connector_plugindir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connector_plugindir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

##### [core_file](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#core_file)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No

##### [datadir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#datadir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`

##### [debug](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#debug)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [dump_last_statements](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#dump_last_statements)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`

##### [host_cache_size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#host_cache_size)
* Type: integer
* Default: 128
* Dynamic: Yes

##### [key_manager](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#key_manager)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`

##### [libdir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#libdir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

##### [load_persisted_configs](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#load_persisted_configs)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

##### [local_address](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#local_address)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [log_augmentation](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_augmentation)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

##### [log_debug](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [log_info](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [log_notice](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [log_throttling](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_throttling)
* Type: number, [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations), [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`

##### [log_warn_super_user](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warn_super_user)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

##### [log_warning](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [logdir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#logdir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`

##### [max_auth_errors_until_block](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_auth_errors_until_block)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

##### [maxlog](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#maxlog)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [module_configdir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#module_configdir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`

##### [ms_timestamp](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ms_timestamp)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [passive](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [persist_runtime_changes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persist_runtime_changes)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: No

##### [persistdir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#persistdir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`

##### [piddir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#piddir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`

##### [query_classifier_cache_size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_classifier_cache_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent

##### [query_retries](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retries)
* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

##### [query_retry_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#query_retry_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

##### [rebalance_period](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_period)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

##### [rebalance_threshold](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_threshold)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`

##### [rebalance_window](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#rebalance_window)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

##### [require_secure_transport](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#require_secure_transport)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: No

##### [retain_last_statements](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

##### [secretsdir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#secretsdir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [session_trace](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

##### [session_trace_match](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_trace_match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [sharedir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sharedir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`

##### [skip_name_resolve](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#skip_name_resolve)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [sql_mode](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sql_mode)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`

##### [substitute_variables](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#substitute_variables)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

##### [syslog](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#syslog)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [telemetry](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

##### [telemetry_attributes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_attributes)
* Type: stringlist
* Default: empty
* Dynamic: Yes
* Mandatory: No

##### [telemetry_ssl_ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_ca)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [telemetry_ssl_cert](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_cert)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [telemetry_ssl_insecure](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_insecure)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

##### [telemetry_ssl_key](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_ssl_key)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [telemetry_update_interval](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_update_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

##### [telemetry_url](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_url)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `http://localhost:4318/v1/metrics`

##### [threads](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads)
* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`

##### [threads_max](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#threads_max)
* Type: positive integer
* Default: 256
* Dynamic: No

##### [trace_file_dir](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_dir)
* Type: path
* Mandatory: No
* Dynamic: No

##### [trace_file_size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#trace_file_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes

##### [users_refresh_interval](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

##### [users_refresh_time](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#users_refresh_time)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`

##### [writeq_high_water](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_high_water)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`

##### [writeq_low_water](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#writeq_low_water)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`


#### Service
##### [auth_all_servers](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auth_all_servers)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [cluster](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#cluster)
* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [connection_keepalive](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#connection_keepalive)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)

##### [disable_sescmd_history](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#disable_sescmd_history)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [enable_root_user](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enable_root_user)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [filters](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#filters)
* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [force_connection_keepalive](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#force_connection_keepalive)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

##### [idle_session_pool_time](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#idle_session_pool_time)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`

##### [log_auth_warnings](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_auth_warnings)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [log_debug](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_debug)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [log_info](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_info)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [log_notice](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_notice)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [log_warning](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#log_warning)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [max_connections](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_connections)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.

##### [max_sescmd_history](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#max_sescmd_history)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`

##### [multiplex_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#multiplex_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

##### [net_write_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#net_write_timeout)
* Type: [durations](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory No
* Dynamic: Yes
* Default: `0s`

##### [password](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

##### [prune_sescmd_history](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#prune_sescmd_history)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [retain_last_statements](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#retain_last_statements)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

##### [role](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#role)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [router](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#router)
* Type: router
* Mandatory: Yes
* Dynamic: No

##### [servers](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#servers)
* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [session_track_trx_state](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#session_track_trx_state)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [strip_db_esc](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#strip_db_esc)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

##### [targets](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#targets)
* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [user](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

##### [user_accounts_file](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [user_accounts_file_usage](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user_accounts_file_usage)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`

##### [version_string](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#version_string)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: None

##### [wait_timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#wait_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s` (>= MaxScale 24.02.5, 25.01.2), `0s` (<= MaxScale 24.02.4, 25.01.1)
* Auto tune: [Yes](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#auto_tune)


#### Settings for File-based Key Manager
##### [file.keyfile](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#file.keyfile)
* Type: path
* Mandatory: Yes
* Dynamic: Yes


#### Settings for HashiCorp Vault Key Manager
##### [vault.ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.ca)
* Type: path
* Default: `""`
* Dynamic: Yes

##### [vault.host](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.host)
* Type: string
* Default: `localhost`
* Dynamic: Yes

##### [vault.mount](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.mount)
* Type: string
* Default: `secret`
* Dynamic: Yes

##### [vault.port](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.port)
* Type: integer
* Default: `8200`
* Dynamic: Yes

##### [vault.timeout](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 30s
* Dynamic: Yes

##### [vault.tls](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.tls)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: Yes

##### [vault.token](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#vault.token)
* Type: password
* Mandatory: Yes
* Dynamic: Yes


#### Settings for KMIP Key Manager
##### [kmip.ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.ca)
* Type: path
* Default: `""`
* Dynamic: Yes

##### [kmip.cert](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.cert)
* Type: path
* Mandatory: Yes
* Dynamic: Yes

##### [kmip.host](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.host)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

##### [kmip.key](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.key)
* Type: path
* Mandatory: Yes
* Dynamic: Yes

##### [kmip.port](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#kmip.port)
* Type: integer
* Mandatory: Yes
* Dynamic: Yes


#### Settings for TLS/SSL Encryption
##### [ssl](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

##### [ssl_ca](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_ca)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_cert](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_cert_verify_depth](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cert_verify_depth)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`

##### [ssl_cipher](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_cipher)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_crl](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_crl)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_key](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_key)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_passphrase](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_passphrase)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [ssl_verify_peer_certificate](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_certificate)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [ssl_verify_peer_host](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_verify_peer_host)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

##### [ssl_version](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#ssl_version)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`



## reference
### [maxscale-listeners](../reference/maxscale-listeners.md)
#### Settings
##### [address](../reference/maxscale-listeners.md#address)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

##### [authenticator](../reference/maxscale-listeners.md#authenticator)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [authenticator_options](../reference/maxscale-listeners.md#authenticator_options)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

##### [connection_init_sql_file](../reference/maxscale-listeners.md#connection_init_sql_file)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [connection_metadata](../reference/maxscale-listeners.md#connection_metadata)
* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

##### [port](../reference/maxscale-listeners.md#port)
* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

##### [protocol](../reference/maxscale-listeners.md#protocol)
* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

##### [redirect_url](../reference/maxscale-listeners.md#redirect_url)
* Type: URL
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [service](../reference/maxscale-listeners.md#service)
* Type: service
* Mandatory: Yes
* Dynamic: No

##### [socket](../reference/maxscale-listeners.md#socket)
* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

##### [sql_mode](../reference/maxscale-listeners.md#sql_mode)
* Type: [enum](maxscale-listeners.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

##### [user_mapping_file](../reference/maxscale-listeners.md#user_mapping_file)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`



### [maxscale-servers](../reference/maxscale-servers.md)
#### Settings
##### [address](../reference/maxscale-servers.md#address)
* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

##### [disk_space_threshold](../reference/maxscale-servers.md#disk_space_threshold)
* Type: Custom
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [extra_port](../reference/maxscale-servers.md#extra_port)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

##### [initial_status](../reference/maxscale-servers.md#initial_status)
* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `down`, `up`, `read`, `write`
* Default: `down`

##### [labels](../reference/maxscale-servers.md#labels)
* Type: string list
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [max_routing_connections](../reference/maxscale-servers.md#max_routing_connections)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0 in MaxScale, 15 in MaxScale Trial.
* Minimum: 0 in MaxScale, 1 in MaxScale Trial.
* Maximum: Unlimited in MaxScale, 15 in MaxScale Trial.

##### [monitorpw](../reference/maxscale-servers.md#monitorpw)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [monitoruser](../reference/maxscale-servers.md#monitoruser)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

##### [persistmaxtime](../reference/maxscale-servers.md#persistmaxtime)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

##### [persistpoolmax](../reference/maxscale-servers.md#persistpoolmax)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

##### [port](../reference/maxscale-servers.md#port)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

##### [priority](../reference/maxscale-servers.md#priority)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

##### [private_address](../reference/maxscale-servers.md#private_address)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

##### [proxy_protocol](../reference/maxscale-servers.md#proxy_protocol)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

##### [rank](../reference/maxscale-servers.md#rank)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

##### [replication_custom_options](../reference/maxscale-servers.md#replication_custom_options)
* Type: string
* Default: None
* Dynamic: Yes

##### [socket](../reference/maxscale-servers.md#socket)
* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

##### [use_service_credentials](../reference/maxscale-servers.md#use_service_credentials)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`



### reference/maxscale-authenticators
#### [maxscale-gssapi-client-authenticator](../reference/maxscale-authenticators/maxscale-gssapi-client-authenticator.md)
##### Settings
###### [gssapi_keytab_path](../reference/maxscale-authenticators/maxscale-gssapi-client-authenticator.md#gssapi_keytab_path)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

###### [principal_name](../reference/maxscale-authenticators/maxscale-gssapi-client-authenticator.md#principal_name)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`



#### [maxscale-mariadb-mysql-authenticator](../reference/maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)
##### Settings
###### [log_password_mismatch](../reference/maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md#log_password_mismatch)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`



#### [maxscale-pam-authenticator](../reference/maxscale-authenticators/maxscale-pam-authenticator.md)
##### Settings
###### [pam_backend_mapping](../reference/maxscale-authenticators/maxscale-pam-authenticator.md#pam_backend_mapping)
* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`

###### [pam_mapped_pw_file](../reference/maxscale-authenticators/maxscale-pam-authenticator.md#pam_mapped_pw_file)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: None

###### [pam_mode](../reference/maxscale-authenticators/maxscale-pam-authenticator.md#pam_mode)
* Type: [enumeration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`

###### [pam_use_cleartext_plugin](../reference/maxscale-authenticators/maxscale-pam-authenticator.md#pam_use_cleartext_plugin)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`




### reference/maxscale-filters
#### [maxscale-binlog-filter](../reference/maxscale-filters/maxscale-binlog-filter.md)
##### Settings
###### [exclude](../reference/maxscale-filters/maxscale-binlog-filter.md#exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [match](../reference/maxscale-filters/maxscale-binlog-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [rewrite_dest](../reference/maxscale-filters/maxscale-binlog-filter.md#rewrite_dest)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [rewrite_src](../reference/maxscale-filters/maxscale-binlog-filter.md#rewrite_src)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None



#### [maxscale-cache](../reference/maxscale-filters/maxscale-cache.md)
##### Settings
###### [cache_in_transactions](../reference/maxscale-filters/maxscale-cache.md#cache_in_transactions)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`

###### [cached_data](../reference/maxscale-filters/maxscale-cache.md#cached_data)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`

###### [clear_cache_on_parse_errors](../reference/maxscale-filters/maxscale-cache.md#clear_cache_on_parse_errors)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

###### [debug](../reference/maxscale-filters/maxscale-cache.md#debug)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

###### [enabled](../reference/maxscale-filters/maxscale-cache.md#enabled)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

###### [hard_ttl](../reference/maxscale-filters/maxscale-cache.md#hard_ttl)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

###### [invalidate](../reference/maxscale-filters/maxscale-cache.md#invalidate)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`

###### [max_count](../reference/maxscale-filters/maxscale-cache.md#max_count)
* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

###### [max_resultset_rows](../reference/maxscale-filters/maxscale-cache.md#max_resultset_rows)
* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

###### [max_resultset_size](../reference/maxscale-filters/maxscale-cache.md#max_resultset_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

###### [max_size](../reference/maxscale-filters/maxscale-cache.md#max_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

###### [rules](../reference/maxscale-filters/maxscale-cache.md#rules)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)

###### [selects](../reference/maxscale-filters/maxscale-cache.md#selects)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`

###### [soft_ttl](../reference/maxscale-filters/maxscale-cache.md#soft_ttl)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

###### [storage](../reference/maxscale-filters/maxscale-cache.md#storage)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`

###### [storage_options](../reference/maxscale-filters/maxscale-cache.md#storage_options)
* Type: string
* Mandatory: No
* Dynamic: No
* Default:

###### [timeout](../reference/maxscale-filters/maxscale-cache.md#timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `5s`

###### [users](../reference/maxscale-filters/maxscale-cache.md#users)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`


##### `storage_memcached`
###### [max_value_size](../reference/maxscale-filters/maxscale-cache.md#max_value_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi

###### [server](../reference/maxscale-filters/maxscale-cache.md#server)
* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No


##### `storage_redis`
###### [password](../reference/maxscale-filters/maxscale-cache.md#password)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [server](../reference/maxscale-filters/maxscale-cache.md#server)
* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

###### [ssl](../reference/maxscale-filters/maxscale-cache.md#ssl)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [ssl_ca](../reference/maxscale-filters/maxscale-cache.md#ssl_ca)
* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [ssl_cert](../reference/maxscale-filters/maxscale-cache.md#ssl_cert)
* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [ssl_key](../reference/maxscale-filters/maxscale-cache.md#ssl_key)
* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [username](../reference/maxscale-filters/maxscale-cache.md#username)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`



#### [maxscale-comment-filter](../reference/maxscale-filters/maxscale-comment-filter.md)
##### Settings
###### [inject](../reference/maxscale-filters/maxscale-comment-filter.md#inject)
* Type: string
* Mandatory: Yes
* Dynamic: Yes



#### [maxscale-consistent-critical-read-filter](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md)
##### Settings
###### [count](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#count)
* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`

###### [global](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#global)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [ignore](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#ignore)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [match](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [options](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#options)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

###### [time](../reference/maxscale-filters/maxscale-consistent-critical-read-filter.md#time)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`



#### [maxscale-ldi-filter](../reference/maxscale-filters/maxscale-ldi-filter.md)
##### Settings
###### [host](../reference/maxscale-filters/maxscale-ldi-filter.md#host)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`

###### [key](../reference/maxscale-filters/maxscale-ldi-filter.md#key)
* Type: string
* Mandatory: No
* Dynamic: Yes

###### [no_verify](../reference/maxscale-filters/maxscale-ldi-filter.md#no_verify)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [port](../reference/maxscale-filters/maxscale-ldi-filter.md#port)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0

###### [protocol_version](../reference/maxscale-filters/maxscale-ldi-filter.md#protocol_version)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2

###### [region](../reference/maxscale-filters/maxscale-ldi-filter.md#region)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`

###### [secret](../reference/maxscale-filters/maxscale-ldi-filter.md#secret)
* Type: string
* Mandatory: No
* Dynamic: Yes

###### [use_http](../reference/maxscale-filters/maxscale-ldi-filter.md#use_http)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false



#### [maxscale-masking-filter](../reference/maxscale-filters/maxscale-masking-filter.md)
##### Settings
###### [check_subqueries](../reference/maxscale-filters/maxscale-masking-filter.md#check_subqueries)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [check_unions](../reference/maxscale-filters/maxscale-masking-filter.md#check_unions)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [check_user_variables](../reference/maxscale-filters/maxscale-masking-filter.md#check_user_variables)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [large_payload](../reference/maxscale-filters/maxscale-masking-filter.md#large_payload)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`

###### [prevent_function_usage](../reference/maxscale-filters/maxscale-masking-filter.md#prevent_function_usage)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [require_fully_parsed](../reference/maxscale-filters/maxscale-masking-filter.md#require_fully_parsed)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [rules](../reference/maxscale-filters/maxscale-masking-filter.md#rules)
* Type: path
* Mandatory: Yes
* Dynamic: Yes

###### [treat_string_arg_as_field](../reference/maxscale-filters/maxscale-masking-filter.md#treat_string_arg_as_field)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [warn_type_mismatch](../reference/maxscale-filters/maxscale-masking-filter.md#warn_type_mismatch)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`



#### [maxscale-maxrows-filter](../reference/maxscale-filters/maxscale-maxrows-filter.md)
##### Settings
###### [debug](../reference/maxscale-filters/maxscale-maxrows-filter.md#debug)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

###### [max_resultset_return](../reference/maxscale-filters/maxscale-maxrows-filter.md#max_resultset_return)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`

###### [max_resultset_rows](../reference/maxscale-filters/maxscale-maxrows-filter.md#max_resultset_rows)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)

###### [max_resultset_size](../reference/maxscale-filters/maxscale-maxrows-filter.md#max_resultset_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`



#### [maxscale-named-server-filter](../reference/maxscale-filters/maxscale-named-server-filter.md)
##### Settings
###### [matchXY](../reference/maxscale-filters/maxscale-named-server-filter.md#matchXY)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [options](../reference/maxscale-filters/maxscale-named-server-filter.md#options)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

###### [source](../reference/maxscale-filters/maxscale-named-server-filter.md#source)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [targetXY](../reference/maxscale-filters/maxscale-named-server-filter.md#targetXY)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [user](../reference/maxscale-filters/maxscale-named-server-filter.md#user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None



#### [maxscale-query-log-all-filter](../reference/maxscale-filters/maxscale-query-log-all-filter.md)
##### Settings
###### [append](../reference/maxscale-filters/maxscale-query-log-all-filter.md#append)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [duration_unit](../reference/maxscale-filters/maxscale-query-log-all-filter.md#duration_unit)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

###### [exclude](../reference/maxscale-filters/maxscale-query-log-all-filter.md#exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [filebase](../reference/maxscale-filters/maxscale-query-log-all-filter.md#filebase)
* Type: string
* Mandatory: Yes
* Dynamic: No

###### [flush](../reference/maxscale-filters/maxscale-query-log-all-filter.md#flush)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [log_data](../reference/maxscale-filters/maxscale-query-log-all-filter.md#log_data)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

###### [log_type](../reference/maxscale-filters/maxscale-query-log-all-filter.md#log_type)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

###### [match](../reference/maxscale-filters/maxscale-query-log-all-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [newline_replacement](../reference/maxscale-filters/maxscale-query-log-all-filter.md#newline_replacement)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

###### [options](../reference/maxscale-filters/maxscale-query-log-all-filter.md#options)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

###### [separator](../reference/maxscale-filters/maxscale-query-log-all-filter.md#separator)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

###### [source](../reference/maxscale-filters/maxscale-query-log-all-filter.md#source)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [source_exclude](../reference/maxscale-filters/maxscale-query-log-all-filter.md#source_exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

###### [source_match](../reference/maxscale-filters/maxscale-query-log-all-filter.md#source_match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

###### [use_canonical_form](../reference/maxscale-filters/maxscale-query-log-all-filter.md#use_canonical_form)
* Type: [bool](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [user](../reference/maxscale-filters/maxscale-query-log-all-filter.md#user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [user_exclude](../reference/maxscale-filters/maxscale-query-log-all-filter.md#user_exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

###### [user_match](../reference/maxscale-filters/maxscale-query-log-all-filter.md#user_match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes



#### [maxscale-regex-filter](../reference/maxscale-filters/maxscale-regex-filter.md)
##### Settings
###### [log_file](../reference/maxscale-filters/maxscale-regex-filter.md#log_file)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [log_trace](../reference/maxscale-filters/maxscale-regex-filter.md#log_trace)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [match](../reference/maxscale-filters/maxscale-regex-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: Yes
* Dynamic: Yes

###### [options](../reference/maxscale-filters/maxscale-regex-filter.md#options)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

###### [replace](../reference/maxscale-filters/maxscale-regex-filter.md#replace)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

###### [source](../reference/maxscale-filters/maxscale-regex-filter.md#source)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [user](../reference/maxscale-filters/maxscale-regex-filter.md#user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None



#### [maxscale-rewrite-filter](../reference/maxscale-filters/maxscale-rewrite-filter.md)
##### Settings
###### [case_sensitive](../reference/maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

###### [log_replacement](../reference/maxscale-filters/maxscale-rewrite-filter.md#log_replacement)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [regex_grammar](../reference/maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`

###### [template_file](../reference/maxscale-filters/maxscale-rewrite-filter.md#template_file)
* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value


##### Settings per template in the template file
###### [case_sensitive](../reference/maxscale-filters/maxscale-rewrite-filter.md#case_sensitive)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: From maxscale.cnf

###### [continue_if_matched](../reference/maxscale-filters/maxscale-rewrite-filter.md#continue_if_matched)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false

###### [ignore_whitespace](../reference/maxscale-filters/maxscale-rewrite-filter.md#ignore_whitespace)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: true

###### [regex_grammar](../reference/maxscale-filters/maxscale-rewrite-filter.md#regex_grammar)
* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf

###### [what_if](../reference/maxscale-filters/maxscale-rewrite-filter.md#what_if)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false



#### [maxscale-tee-filter](../reference/maxscale-filters/maxscale-tee-filter.md)
##### Settings
###### [exclude](../reference/maxscale-filters/maxscale-tee-filter.md#exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [match](../reference/maxscale-filters/maxscale-tee-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [options](../reference/maxscale-filters/maxscale-tee-filter.md#options)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

###### [service](../reference/maxscale-filters/maxscale-tee-filter.md#service)
* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none

###### [source](../reference/maxscale-filters/maxscale-tee-filter.md#source)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [sync](../reference/maxscale-filters/maxscale-tee-filter.md#sync)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [target](../reference/maxscale-filters/maxscale-tee-filter.md#target)
* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none

###### [user](../reference/maxscale-filters/maxscale-tee-filter.md#user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None



#### [maxscale-throttle-filter](../reference/maxscale-filters/maxscale-throttle-filter.md)
##### Settings
###### [continuous_duration](../reference/maxscale-filters/maxscale-throttle-filter.md#continuous_duration)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 2s

###### [max_qps](../reference/maxscale-filters/maxscale-throttle-filter.md#max_qps)
* Type: number
* Mandatory: Yes
* Dynamic: Yes

###### [sampling_duration](../reference/maxscale-filters/maxscale-throttle-filter.md#sampling_duration)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms

###### [throttling_duration](../reference/maxscale-filters/maxscale-throttle-filter.md#throttling_duration)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: Yes
* Dynamic: Yes



#### [maxscale-top-filter](../reference/maxscale-filters/maxscale-top-filter.md)
##### Settings
###### [count](../reference/maxscale-filters/maxscale-top-filter.md#count)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

###### [exclude](../reference/maxscale-filters/maxscale-top-filter.md#exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [filebase](../reference/maxscale-filters/maxscale-top-filter.md#filebase)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

###### [match](../reference/maxscale-filters/maxscale-top-filter.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [options](../reference/maxscale-filters/maxscale-top-filter.md#options)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`

###### [source](../reference/maxscale-filters/maxscale-top-filter.md#source)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [user](../reference/maxscale-filters/maxscale-top-filter.md#user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None



#### [maxscale-workload-capture-and-replay](../reference/maxscale-filters/maxscale-workload-capture-and-replay.md)
##### Settings
###### [capture_dir](../reference/maxscale-filters/maxscale-workload-capture-and-replay.md#capture_dir)
* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No

###### [capture_duration](../reference/maxscale-filters/maxscale-workload-capture-and-replay.md#capture_duration)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Default: 0s
* Maximum: Unlimited in MaxScale, 5min in MaxScale Lite.
* Mandatory: No
* Dynamic: No

###### [capture_size](../reference/maxscale-filters/maxscale-workload-capture-and-replay.md#capture_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Default: 0
* Maximum: Unlimited in MaxScale, 10MB in MaxScale Lite.
* Mandatory: No
* Dynamic: No

###### [start_capture](../reference/maxscale-filters/maxscale-workload-capture-and-replay.md#start_capture)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Mandatory: No
* Dynamic: No




### reference/maxscale-monitors
#### [common-monitor-parameters](../reference/maxscale-monitors/common-monitor-parameters.md)
##### Settings
###### [backend_connect_attempts](../reference/maxscale-monitors/common-monitor-parameters.md#backend_connect_attempts)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

###### [backend_connect_timeout](../reference/maxscale-monitors/common-monitor-parameters.md#backend_connect_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

###### [backend_read_timeout](../reference/maxscale-monitors/common-monitor-parameters.md#backend_read_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

###### [backend_write_timeout](../reference/maxscale-monitors/common-monitor-parameters.md#backend_write_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

###### [disk_space_check_interval](../reference/maxscale-monitors/common-monitor-parameters.md#disk_space_check_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

###### [disk_space_threshold](../reference/maxscale-monitors/common-monitor-parameters.md#disk_space_threshold)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [events](../reference/maxscale-monitors/common-monitor-parameters.md#events)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

###### [journal_max_age](../reference/maxscale-monitors/common-monitor-parameters.md#journal_max_age)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

###### [module](../reference/maxscale-monitors/common-monitor-parameters.md#module)
* Type: string
* Mandatory: Yes
* Dynamic: No

###### [monitor_interval](../reference/maxscale-monitors/common-monitor-parameters.md#monitor_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

###### [password](../reference/maxscale-monitors/common-monitor-parameters.md#password)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

###### [primary_state_sql](../reference/maxscale-monitors/common-monitor-parameters.md#primary_state_sql)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [replica_state_sql](../reference/maxscale-monitors/common-monitor-parameters.md#replica_state_sql)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [role](../reference/maxscale-monitors/common-monitor-parameters.md#role)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [script](../reference/maxscale-monitors/common-monitor-parameters.md#script)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [script_timeout](../reference/maxscale-monitors/common-monitor-parameters.md#script_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

###### [servers](../reference/maxscale-monitors/common-monitor-parameters.md#servers)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

###### [user](../reference/maxscale-monitors/common-monitor-parameters.md#user)
* Type: string
* Mandatory: Yes
* Dynamic: Yes



#### [galera-monitor](../reference/maxscale-monitors/galera-monitor.md)
##### Settings
###### [available_when_donor](../reference/maxscale-monitors/galera-monitor.md#available_when_donor)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

###### [disable_master_failback](../reference/maxscale-monitors/galera-monitor.md#disable_master_failback)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

###### [disable_master_role_setting](../reference/maxscale-monitors/galera-monitor.md#disable_master_role_setting)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

###### [root_node_as_master](../reference/maxscale-monitors/galera-monitor.md#root_node_as_master)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

###### [set_donor_nodes](../reference/maxscale-monitors/galera-monitor.md#set_donor_nodes)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

###### [use_priority](../reference/maxscale-monitors/galera-monitor.md#use_priority)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes



#### [mariadb-monitor](../reference/maxscale-monitors/mariadb-monitor.md)
##### Settings
###### [assume_unique_hostnames](../reference/maxscale-monitors/mariadb-monitor.md#assume_unique_hostnames)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [cooperative_monitoring_locks](../reference/maxscale-monitors/mariadb-monitor.md#cooperative_monitoring_locks)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`

###### [enforce_read_only_servers](../reference/maxscale-monitors/mariadb-monitor.md#enforce_read_only_servers)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [enforce_read_only_slaves](../reference/maxscale-monitors/mariadb-monitor.md#enforce_read_only_slaves)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [enforce_writable_master](../reference/maxscale-monitors/mariadb-monitor.md#enforce_writable_master)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [failcount](../reference/maxscale-monitors/mariadb-monitor.md#failcount)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`

###### [maintenance_on_low_disk_space](../reference/maxscale-monitors/mariadb-monitor.md#maintenance_on_low_disk_space)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [master_conditions](../reference/maxscale-monitors/mariadb-monitor.md#master_conditions)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`

###### [script_max_replication_lag](../reference/maxscale-monitors/mariadb-monitor.md#script_max_replication_lag)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

###### [slave_conditions](../reference/maxscale-monitors/mariadb-monitor.md#slave_conditions)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`


##### Settings for Backup operations
###### [backup_storage_address](../reference/maxscale-monitors/mariadb-monitor.md#backup_storage_address)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [backup_storage_path](../reference/maxscale-monitors/mariadb-monitor.md#backup_storage_path)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [mariadb_backup_parallel](../reference/maxscale-monitors/mariadb-monitor.md#mariadb_backup_parallel)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

###### [mariadb_backup_use_memory](../reference/maxscale-monitors/mariadb-monitor.md#mariadb_backup_use_memory)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `1G`

###### [rebuild_port](../reference/maxscale-monitors/mariadb-monitor.md#rebuild_port)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`

###### [ssh_check_host_key](../reference/maxscale-monitors/mariadb-monitor.md#ssh_check_host_key)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [ssh_keyfile](../reference/maxscale-monitors/mariadb-monitor.md#ssh_keyfile)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [ssh_port](../reference/maxscale-monitors/mariadb-monitor.md#ssh_port)
* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`

###### [ssh_timeout](../reference/maxscale-monitors/mariadb-monitor.md#ssh_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

###### [ssh_user](../reference/maxscale-monitors/mariadb-monitor.md#ssh_user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### Settings for Cluster manipulation operations
###### [auto_failover](../reference/maxscale-monitors/mariadb-monitor.md#auto_failover)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`

###### [auto_rejoin](../reference/maxscale-monitors/mariadb-monitor.md#auto_rejoin)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [demotion_sql_file](../reference/maxscale-monitors/mariadb-monitor.md#demotion_sql_file)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [enforce_simple_topology](../reference/maxscale-monitors/mariadb-monitor.md#enforce_simple_topology)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [failover_timeout](../reference/maxscale-monitors/mariadb-monitor.md#failover_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

###### [handle_events](../reference/maxscale-monitors/mariadb-monitor.md#handle_events)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [master_failure_timeout](../reference/maxscale-monitors/mariadb-monitor.md#master_failure_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

###### [promotion_sql_file](../reference/maxscale-monitors/mariadb-monitor.md#promotion_sql_file)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [replication_master_ssl](../reference/maxscale-monitors/mariadb-monitor.md#replication_master_ssl)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [replication_password](../reference/maxscale-monitors/mariadb-monitor.md#replication_password)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [replication_user](../reference/maxscale-monitors/mariadb-monitor.md#replication_user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [servers_no_promotion](../reference/maxscale-monitors/mariadb-monitor.md#servers_no_promotion)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

###### [switchover_on_low_disk_space`\*\*](../reference/maxscale-monitors/mariadb-monitor.md#switchover_on_low_disk_space`\*\*)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [switchover_timeout](../reference/maxscale-monitors/mariadb-monitor.md#switchover_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

###### [verify_master_failure](../reference/maxscale-monitors/mariadb-monitor.md#verify_master_failure)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### Settings for Primary server write test
###### [write_test_fail_action](../reference/maxscale-monitors/mariadb-monitor.md#write_test_fail_action)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes

###### [write_test_interval](../reference/maxscale-monitors/mariadb-monitor.md#write_test_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Dynamic: Yes
* Default: 0s

###### [write_test_table](../reference/maxscale-monitors/mariadb-monitor.md#write_test_table)
* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`




### reference/maxscale-protocols
#### [maxscale-mariadb-protocol-module](../reference/maxscale-protocols/maxscale-mariadb-protocol-module.md)
##### Settings
###### [allow_replication](../reference/maxscale-protocols/maxscale-mariadb-protocol-module.md#allow_replication)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true



#### [maxscale-nosql-protocol-module](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md)
##### Settings
###### [authentication_db](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_db)
* Type: string
* Mandatory: No
* Default: `"NoSQL"`

###### [authentication_key_id](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_key_id)
* Type: string
* Mandatory: No
* Default: `""`

###### [authentication_password](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_password)
* Type: string
* Mandatory: No
* Default: `""`

###### [authentication_required](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_required)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

###### [authentication_shared](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_shared)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

###### [authentication_user](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authentication_user)
* Type: string
* Mandatory: Yes, if `authentication_shared` is true.

###### [authorization_enabled](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#authorization_enabled)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

###### [auto_create_databases](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_databases)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

###### [auto_create_tables](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#auto_create_tables)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

###### [cursor_timeout](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#cursor_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Default: `60s`

###### [debug](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#debug)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`

###### [host](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#host)
* Type: string
* Mandatory: No
* Default: `"%"`

###### [id_length](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#id_length)
* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`

###### [internal_cache](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#internal_cache)
* Type: string
* Mandatory: No
* Default: ''

###### [log_unknown_command](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#log_unknown_command)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

###### [on_unknown_command](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#on_unknown_command)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`

###### [ordered_insert_behavior](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#ordered_insert_behavior)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`

###### [password](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#password)
* Type: string
* Mandatory: No
* Default: `""`

###### [user](../reference/maxscale-protocols/maxscale-nosql-protocol-module.md#user)
* Type: string
* Mandatory: No
* Default: `""`




### reference/maxscale-rest-api
#### [maxscale-filter-resource](../reference/maxscale-rest-api/maxscale-filter-resource.md)
##### Resource Operations
###### [Create a filter](../reference/maxscale-rest-api/maxscale-filter-resource.md#Create a filter)
* Type of the object, must be `filters`
* `data.attributes.module`
* The filter module to use



#### [maxscale-listener-resource](../reference/maxscale-rest-api/maxscale-listener-resource.md)
##### Resource Operations
###### [Create a new listener](../reference/maxscale-rest-api/maxscale-listener-resource.md#Create a new listener)
* Type of the object, must be `listeners`
* `data.attributes.parameters.port` OR `data.attributes.parameters.socket`
* The TCP port or UNIX Domain Socket the listener listens on. Only one of the fields can be defined.
* `data.relationships.services.data`
* The service relationships data, must define a JSON object with an `id` value that defines the service to use and a `type` value set to `services`.



#### [maxscale-monitor-resource](../reference/maxscale-rest-api/maxscale-monitor-resource.md)
##### Resource Operations
###### [Create a monitor](../reference/maxscale-rest-api/maxscale-monitor-resource.md#Create a monitor)
* Type of the object, must be `monitors`
* `data.attributes.module`
* The monitor module to use
* `data.attributes.parameters.user`
* The [`user`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user) to use
* `data.attributes.parameters.password`
* The [password](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password) to use



#### [maxscale-server-resource](../reference/maxscale-rest-api/maxscale-server-resource.md)
##### Resource Operations
###### [Create a server](../reference/maxscale-rest-api/maxscale-server-resource.md#Create a server)
* Type of the object, must be `servers`
* `data.attributes.parameters.address` OR `data.attributes.parameters.socket`
* The [`address`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#address) or [`socket`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#socket) to use. Only one of the fields can be defined.
* `data.attributes.parameters.port`
* The [`port`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#port) to use. Needs to be defined if the `address` field is defined.



#### [maxscale-service-resource](../reference/maxscale-rest-api/maxscale-service-resource.md)
##### Resource Operations
###### [Create a service](../reference/maxscale-rest-api/maxscale-service-resource.md#Create a service)
* Type of the object, must be `services`
* `data.attributes.router`
* The router module to use
* `data.attributes.parameters.user`
* The [`user`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#user) to use
* `data.attributes.parameters.password`
* The [`password`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#password) to use




### reference/maxscale-routers
#### [maxscale-binlogrouter](../reference/maxscale-routers/maxscale-binlogrouter.md)
##### Settings
###### [archivedir](../reference/maxscale-routers/maxscale-binlogrouter.md#archivedir)
* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No

###### [compression_algorithm](../reference/maxscale-routers/maxscale-binlogrouter.md#compression_algorithm)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`

###### [datadir](../reference/maxscale-routers/maxscale-binlogrouter.md#datadir)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`

###### [ddl_only](../reference/maxscale-routers/maxscale-binlogrouter.md#ddl_only)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: false

###### [encryption_cipher](../reference/maxscale-routers/maxscale-binlogrouter.md#encryption_cipher)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`

###### [encryption_key_id](../reference/maxscale-routers/maxscale-binlogrouter.md#encryption_key_id)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [expiration_mode](../reference/maxscale-routers/maxscale-binlogrouter.md#expiration_mode)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`

###### [expire_log_duration](../reference/maxscale-routers/maxscale-binlogrouter.md#expire_log_duration)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s`

###### [expire_log_minimum_files](../reference/maxscale-routers/maxscale-binlogrouter.md#expire_log_minimum_files)
* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`

###### [net_timeout](../reference/maxscale-routers/maxscale-binlogrouter.md#net_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `10s`

###### [number_of_noncompressed_files](../reference/maxscale-routers/maxscale-binlogrouter.md#number_of_noncompressed_files)
* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`

###### [rpl_semi_sync_slave_enabled](../reference/maxscale-routers/maxscale-binlogrouter.md#rpl_semi_sync_slave_enabled)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: false
* Dynamic: Yes

###### [select_master](../reference/maxscale-routers/maxscale-binlogrouter.md#select_master)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [server_id](../reference/maxscale-routers/maxscale-binlogrouter.md#server_id)
* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`



#### [maxscale-diff](../reference/maxscale-routers/maxscale-diff.md)
##### Settings
###### [explain](../reference/maxscale-routers/maxscale-diff.md#explain)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

###### [explain_entries](../reference/maxscale-routers/maxscale-diff.md#explain_entries)
* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

###### [explain_period](../reference/maxscale-routers/maxscale-diff.md#explain_period)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

###### [main](../reference/maxscale-routers/maxscale-diff.md#main)
* Type: server
* Mandatory: Yes
* Dynamic: No

###### [max_request_lag](../reference/maxscale-routers/maxscale-diff.md#max_request_lag)
* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

###### [on_error](../reference/maxscale-routers/maxscale-diff.md#on_error)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

###### [percentile](../reference/maxscale-routers/maxscale-diff.md#percentile)
* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

###### [qps_window](../reference/maxscale-routers/maxscale-diff.md#qps_window)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 15m

###### [report](../reference/maxscale-routers/maxscale-diff.md#report)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

###### [reset_replication](../reference/maxscale-routers/maxscale-diff.md#reset_replication)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

###### [retain_faster_statements](../reference/maxscale-routers/maxscale-diff.md#retain_faster_statements)
* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

###### [retain_slower_statements](../reference/maxscale-routers/maxscale-diff.md#retain_slower_statements)
* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

###### [samples](../reference/maxscale-routers/maxscale-diff.md#samples)
* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

###### [service](../reference/maxscale-routers/maxscale-diff.md#service)
* Type: service
* Mandatory: Yes
* Dynamic: No



#### [maxscale-exasolrouter](../reference/maxscale-routers/maxscale-exasolrouter.md)
##### Settings
###### [appearance](../reference/maxscale-routers/maxscale-exasolrouter.md#appearance)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `read_only`, `read_write`
* Default: `read_only`

###### [connection_string](../reference/maxscale-routers/maxscale-exasolrouter.md#connection_string)
* Type: string
* Mandatory: Yes
* Dynamic: No

###### [preprocessor](../reference/maxscale-routers/maxscale-exasolrouter.md#preprocessor)
* Type: String
* Mandatory: No
* Dynamic: No
* Values: `auto`, `activate-only`, `custom:<path>`, `disabled`
* Default: `auto`

###### [preprocessor_script](../reference/maxscale-routers/maxscale-exasolrouter.md#preprocessor_script)
* Type: String
* Mandatory: No
* Dynamic: No
* Default: "UTIL.maria_preprocessor"



#### [maxscale-kafkacdc](../reference/maxscale-routers/maxscale-kafkacdc.md)
##### Settings
###### [bootstrap_servers](../reference/maxscale-routers/maxscale-kafkacdc.md#bootstrap_servers)
* Type: string
* Mandatory: Yes
* Dynamic: No

###### [cooperative_replication](../reference/maxscale-routers/maxscale-kafkacdc.md#cooperative_replication)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [enable_idempotence](../reference/maxscale-routers/maxscale-kafkacdc.md#enable_idempotence)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [exclude](../reference/maxscale-routers/maxscale-kafkacdc.md#exclude)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [gtid](../reference/maxscale-routers/maxscale-kafkacdc.md#gtid)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [kafka_sasl_mechanism](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_mechanism)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

###### [kafka_sasl_password](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_password)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [kafka_sasl_user](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_sasl_user)
* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [kafka_ssl](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_ssl)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [kafka_ssl_ca](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_ca)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [kafka_ssl_cert](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_cert)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [kafka_ssl_key](../reference/maxscale-routers/maxscale-kafkacdc.md#kafka_ssl_key)
* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [match](../reference/maxscale-routers/maxscale-kafkacdc.md#match)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [read_gtid_from_kafka](../reference/maxscale-routers/maxscale-kafkacdc.md#read_gtid_from_kafka)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

###### [send_schema](../reference/maxscale-routers/maxscale-kafkacdc.md#send_schema)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

###### [server_id](../reference/maxscale-routers/maxscale-kafkacdc.md#server_id)
* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

###### [timeout](../reference/maxscale-routers/maxscale-kafkacdc.md#timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

###### [topic](../reference/maxscale-routers/maxscale-kafkacdc.md#topic)
* Type: string
* Mandatory: Yes
* Dynamic: No



#### [maxscale-kafkaimporter](../reference/maxscale-routers/maxscale-kafkaimporter.md)
##### Settings
###### [batch_size](../reference/maxscale-routers/maxscale-kafkaimporter.md#batch_size)
* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

###### [bootstrap_servers](../reference/maxscale-routers/maxscale-kafkaimporter.md#bootstrap_servers)
* Type: string
* Mandatory: Yes
* Dynamic: Yes

###### [engine](../reference/maxscale-routers/maxscale-kafkaimporter.md#engine)
* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

###### [kafka_sasl_mechanism](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_mechanism)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

###### [kafka_sasl_password](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_password)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [kafka_sasl_user](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_sasl_user)
* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [kafka_ssl](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

###### [kafka_ssl_ca](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_ca)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [kafka_ssl_cert](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_cert)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [kafka_ssl_key](../reference/maxscale-routers/maxscale-kafkaimporter.md#kafka_ssl_key)
* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [table_name_in](../reference/maxscale-routers/maxscale-kafkaimporter.md#table_name_in)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

###### [timeout](../reference/maxscale-routers/maxscale-kafkaimporter.md#timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

###### [topics](../reference/maxscale-routers/maxscale-kafkaimporter.md#topics)
* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes



#### [maxscale-mirror](../reference/maxscale-routers/maxscale-mirror.md)
##### Settings
###### [exporter](../reference/maxscale-routers/maxscale-mirror.md#exporter)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`

###### [file](../reference/maxscale-routers/maxscale-mirror.md#file)
* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

###### [kafka_broker](../reference/maxscale-routers/maxscale-mirror.md#kafka_broker)
* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

###### [kafka_topic](../reference/maxscale-routers/maxscale-mirror.md#kafka_topic)
* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

###### [main](../reference/maxscale-routers/maxscale-mirror.md#main)
* Type: target
* Mandatory: Yes
* Dynamic: Yes

###### [on_error](../reference/maxscale-routers/maxscale-mirror.md#on_error)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`

###### [report](../reference/maxscale-routers/maxscale-mirror.md#report)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`



#### [maxscale-readconnroute](../reference/maxscale-routers/maxscale-readconnroute.md)
##### Settings
###### [master_accept_reads](../reference/maxscale-routers/maxscale-readconnroute.md#master_accept_reads)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

###### [max_replication_lag](../reference/maxscale-routers/maxscale-readconnroute.md#max_replication_lag)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

###### [router_options](../reference/maxscale-routers/maxscale-readconnroute.md#router_options)
* Type: [enum\_mask](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`



#### [maxscale-readwritesplit](../reference/maxscale-routers/maxscale-readwritesplit.md)
##### Settings
###### [causal_reads](../reference/maxscale-routers/maxscale-readwritesplit.md#causal_reads)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`

###### [causal_reads_timeout](../reference/maxscale-routers/maxscale-readwritesplit.md#causal_reads_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

###### [delayed_retry](../reference/maxscale-routers/maxscale-readwritesplit.md#delayed_retry)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [delayed_retry_timeout](../reference/maxscale-routers/maxscale-readwritesplit.md#delayed_retry_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

###### [lazy_connect](../reference/maxscale-routers/maxscale-readwritesplit.md#lazy_connect)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [master_accept_reads](../reference/maxscale-routers/maxscale-readwritesplit.md#master_accept_reads)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [master_failure_mode](../reference/maxscale-routers/maxscale-readwritesplit.md#master_failure_mode)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)

###### [master_reconnection](../reference/maxscale-routers/maxscale-readwritesplit.md#master_reconnection)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)

###### [max_replication_lag](../reference/maxscale-routers/maxscale-readwritesplit.md#max_replication_lag)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

###### [max_slave_connections](../reference/maxscale-routers/maxscale-readwritesplit.md#max_slave_connections)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 0
* Max: 255
* Default: 255

###### [retry_failed_reads](../reference/maxscale-routers/maxscale-readwritesplit.md#retry_failed_reads)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

###### [slave_connections](../reference/maxscale-routers/maxscale-readwritesplit.md#slave_connections)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

###### [slave_selection_criteria](../reference/maxscale-routers/maxscale-readwritesplit.md#slave_selection_criteria)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`

###### [strict_multi_stmt](../reference/maxscale-routers/maxscale-readwritesplit.md#strict_multi_stmt)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [strict_sp_calls](../reference/maxscale-routers/maxscale-readwritesplit.md#strict_sp_calls)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [strict_tmp_tables](../reference/maxscale-routers/maxscale-readwritesplit.md#strict_tmp_tables)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)

###### [sync_transaction](../reference/maxscale-routers/maxscale-readwritesplit.md#sync_transaction)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `soft`, `hard`
* Default: `none`

###### [sync_transaction_count](../reference/maxscale-routers/maxscale-readwritesplit.md#sync_transaction_count)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 255
* Default: 1

###### [sync_transaction_max_lag](../reference/maxscale-routers/maxscale-readwritesplit.md#sync_transaction_max_lag)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

###### [sync_transaction_timeout](../reference/maxscale-routers/maxscale-readwritesplit.md#sync_transaction_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

###### [transaction_replay](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [transaction_replay_attempts](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_attempts)
* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

###### [transaction_replay_checksum](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_checksum)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`

###### [transaction_replay_max_size](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_max_size)
* Type: [size](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB

###### [transaction_replay_retry_on_deadlock](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_retry_on_deadlock)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [transaction_replay_retry_on_mismatch](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_retry_on_mismatch)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [transaction_replay_safe_commit](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_safe_commit)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

###### [transaction_replay_timeout](../reference/maxscale-routers/maxscale-readwritesplit.md#transaction_replay_timeout)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)

###### [use_sql_variables_in](../reference/maxscale-routers/maxscale-readwritesplit.md#use_sql_variables_in)
* Type: [enum](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`



#### [maxscale-schemarouter](../reference/maxscale-routers/maxscale-schemarouter.md)
##### Settings
###### [allow_duplicates](../reference/maxscale-routers/maxscale-schemarouter.md#allow_duplicates)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

###### [ignore_tables](../reference/maxscale-routers/maxscale-schemarouter.md#ignore_tables)
* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`

###### [ignore_tables_regex](../reference/maxscale-routers/maxscale-schemarouter.md#ignore_tables_regex)
* Type: [regex](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

###### [max_staleness](../reference/maxscale-routers/maxscale-schemarouter.md#max_staleness)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 150s

###### [refresh_databases](../reference/maxscale-routers/maxscale-schemarouter.md#refresh_databases)
* Type: [boolean](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

###### [refresh_interval](../reference/maxscale-routers/maxscale-schemarouter.md#refresh_interval)
* Type: [duration](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`



#### [maxscale-smartrouter](../reference/maxscale-routers/maxscale-smartrouter.md)
##### Settings
###### [master](../reference/maxscale-routers/maxscale-smartrouter.md#master)
* Type: target
* Mandatory: Yes
* Dynamic: No





---

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
