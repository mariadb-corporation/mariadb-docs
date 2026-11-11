---
description: >-
  Reference for every MaxScale global setting in the [maxscale] section, in
  alphabetical order: threads, logging, directories, REST API, sync, telemetry.
---

# MaxScale Global Settings

These settings go in the `[maxscale]` section of the MaxScale configuration file and are listed in alphabetical order. For what this section is and its diagnostic options, see [Global Settings](README.md#global-settings). For value types such as durations and sizes, see [Special Parameter Types](README.md#special-parameter-types).

## `admin_audit`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables the logging of incoming REST API requests for auditing and monitoring purposes.

Enable logging of incoming REST API calls.

## `admin_audit_exclude_methods`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions
* Description: Provides a list of HTTP methods to be excluded from REST API audit logging, separated by commas.

List of comma separated HTTP methods to exclude from logging. MaxScale does not use `CONNECT` or `TRACE`.

Resetting to log all methods can be done in the configuration file by writing `admin_audit_exclude_methods=` or at runtime with `maxctrl alter maxscale admin_audit_exclude_methods=`. Remember that once a runtime change has been made, the entry for that setting is ignored in the main configuration file (usually maxscale.cnf).

## `admin_audit_file`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`
* Description: Defines the location of the REST API audit logs.

The file where the REST API auditing information is logged.

If a non-default value is used, the directory where the file resides must exist. For example, with `/var/log/maxscale/audit_files/audit.csv`, the directory `/var/log/maxscale/audit_files` must exist.

## `admin_auth`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Allows HTTP Basic authentication for the REST API.

Enable REST API authentication using HTTP Basic Access authentication. This is not a secure method of authentication without HTTPS but it does add a small layer of security.

For more information, read the [REST API documentation](../../../../reference/maxscale-rest-api/maxscale-rest-api.md).

## `admin_enabled`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Enables or disables the MaxScale admin interface.

Enable or disable the admin interface. This allows the admin interface to be completely disabled to prevent access to it.

## `admin_gui`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Enables or disables the graphical user interface (GUI) for the admin interface.

Enable or disable the admin graphical user interface.

MaxScale provides a GUI for administrative operations via the REST API. When the GUI is enabled, the root REST API resource (i.e. `http://localhost:8989/`) will serve the GUI. When disabled, the REST API will respond with a 200 OK to the request. By disabling the GUI, the root resource can be used as a low overhead health check.

## `admin_host`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`
* Description: Provides the network interface address that the REST API is listening to.

The network interface where the REST API listens on. The default value is the IPv4 address `127.0.0.1` which only listens for local connections.

## `admin_jwt_algorithm`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`
* Description: Specifies the algorithm for signing JSON Web Tokens (JWTs) for the REST API.

The signature algorithm used by the MaxScale REST API when generating JSON Web Tokens.

For more information about the tokens and how they work, refer to [the REST API documentation](../../../../reference/maxscale-rest-api/maxscale-rest-api.md).

If a symmetric algorithm is used (i.e. `HS256`, `HS384` or `HS512`), MaxScale will generate a random encryption key on startup and use that to sign the messages. The symmetric key can also be retrieved from an [Encryption Key Manager](README.md#encryption-key-managers) if the `admin_jwt_key` parameter is defined.

If an asymmetric algorithm (i.e. public key authentication) is used, both the `admin_ssl_cert` and `admin_ssl_key` parameters must be defined and they must contain a private key and a public certificate of the correct type. If the wrong key type, key length or elliptic curve is used, MaxScale will refuse to start.

Asymmetric key algorithms make it possible for the clients of the REST API to validate that the token was indeed generated by the correct entity.

Symmetric algorithms make it easy to share the same tokens between multiple MaxScale instances as the shared secret can be stored in a key management system.

The possible values for this parameter are:

* `auto`
  * MaxScale will attempt to detect the best algorithm to use for signatures. The algorithm used depends on the private key type: RSA keys use `PS256`, EC keys use the `ES256`, `ES384` or `ES512` depending on the curve, Ed25519 keys use `ED25519` and Ed448 keys uses `ED448`. If MaxScale cannot auto-detect the key type, it falls back to `HS256` as the default algorithm.
* `HS256`, `HS384` or `HS512`
  * [HMAC with SHA-2 Functions](https://datatracker.ietf.org/doc/html/rfc7518#section-3.2). If `admin_jwt_key` is not defined, uses a random encryption key of the correct size.
* `RS256`, `RS384` or `RS512`
  * [Digital Signature with RSASSA-PKCS1-v1\_5](https://datatracker.ietf.org/doc/html/rfc7518#section-3.3). Requires at least a 2048-bit RSA key.
* `PS256`, `PS384` or `PS512`
  * [Digital Signature with RSASSA-PSS](https://datatracker.ietf.org/doc/html/rfc7518#section-3.5). Requires at least a 2048-bit RSA key.
* `ES256`, `ES384` or `ES512`
  * [Digital Signature with ECDSA](https://datatracker.ietf.org/doc/html/rfc7518#section-3.4). Requires an EC key with the correct curve: P-256 for `ES256`, P-384 for `ES384` and P-512 for `ES512`.
* `ED25519` or `ED448`
  * [Edwards-curve Digital Signature Algorithm (EdDSA)](https://www.rfc-editor.org/rfc/rfc8037#section-3). Requires a Ed25519 key for `ED25519` or a Ed448 key for `ED448`.

## `admin_jwt_issuer`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`
* Description: Specifies the issuer ("iss") claim in the REST API-generated JSON Web Tokens.

The issuer (`"iss"`) claim of all JWTs generated by MaxScale. This can be set to a custom value to uniquely identify which MaxScale issued a JWT. This is especially useful for cases where the MaxScale GUI is used from behind a reverse proxy.

## `admin_jwt_key`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Identifies the encryption key that is used to sign JSON Web Tokens.

The ID for the encryption key used to sign the JSON Web Tokens. If configured, an [Encryption Key Manager](README.md#encryption-key-managers) must also be configured and it must contain the key with the given ID. If no key is defined, MaxScale will use a random encryption key whenever a symmetric signature algorithm is used.

The encryption key is only read on startup. This means that the tokens will be signed by the latest key version that is available on startup: rotating the encryption key in the key management system will not cause the JWTs to be signed with newer versions of the key.

## `admin_jwt_max_age`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `24h`
* Description: Specifies the maximum duration of JWTs issued by the REST API.

The maximum lifetime of a token generated by the `/auth` endpoint.

If a client requests for a token with a lifetime that exceeds the configured value, the token lifetime is silently truncated to this value. This can be used to control the maximum length of a MaxGUI session.

This also acts as the effective maximum age of any database connection created from the `/sql` endpoint.

## `admin_log_auth_failures`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Enables logging of authentication failures for the admin interface.

Log authentication failures for the admin interface.

## `admin_oidc_client_id`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the client ID for OpenID Connect (OIDC) login authentication requests.

The client ID that's used when doing OpenID Connect requests. When using another MaxScale as the authorization server, this is the REST-API username that's used.

If `client_id` is not configured, the value of `admin_jwt_issuer` is used as the client\_id for all OpenID Connect requests.

## `admin_oidc_client_secret`

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the client secret used for OIDC authentication requests.

The client secret that's used when doing OpenID Connect requests. When using another MaxScale as the authorization server, this is the REST-API password that's used.

## `admin_oidc_extra_options`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines additional parameters that should be included in authorization requests for OIDC. 

Extra options that are added to the initial authorization request. These options are sometimes needed to pass extra information to the identity provider service.

For [Auth0](https://auth0.com/), the API that is used must be defined with this setting. For example, if the API name is `my-api` then `admin_oidc_extra_options=audience=my-api` should be used.

## `admin_oidc_flow`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `auto`, `implicit`, `code`
* Default: `auto`
* Description: Describes the OIDC authentication flow used for SSO.

The OpenID Connect authentication flow that's used for authenticating clients when Single Sing-On is being used.

By default, the choice of the flow is made based on the supported capabilities of the authorization server. The code flow is preferred if it is supported by the authorization server and if it doesn't, the implicit flow is used as a fallback.

## `admin_oidc_ssl_insecure`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Disables TLS certificate validation while retrieving OIDC certificates.

Disable TLS certificate validation when fetching OIDC certificates. This should only be enabled when testing with a local OpenID Connect provider with self-signed certificates.

## `admin_oidc_url`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the OIDC provider's URL, which is needed to validate JWT.

The URL to a OpenID Connect server that is used for JWT validation.

If defined, any tokens signed by this server are accepted as valid bearer tokens for the MaxScale REST API. The `"sub"` field of the token is assumed to be the username of an administrative user in MaxScale and the `"account"` claim is assumed to be the type of the user: `"admin"` for administrative users with full access to the REST-API and `"basic"` for users with read-only access to the REST-API. This means that all users must be first created with `maxctrl create user` before the tokens are accepted if the OIDC provider is not able to add the `"account"` claim.

Modifying `admin_oidc_url` will cause the certificates to be fetched again. They are also fetched when the `maxctrl reload tls` command is executed or when the `admin_ssl_cert` and `admin_ssl_key` settings are modified.

MaxScale versions 22.08.16 and earlier only fetched the new certificates when the `maxctrl reload tls` command was executed.

## `admin_pam_readonly_service`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the PAM service that is used to verify read-only REST API users.

See [admin\_pam\_readwrite\_service](#admin_pam_readwrite_service).

## `admin_pam_readwrite_service`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Specifies the PAM service used for authentication REST API users with read and write access.

Use Pluggable Authentication Modules (PAM) for REST API authentication. This setting and `admin_pam_readonly_service` accept a PAM service name which is used during authentication if normal authentication fails. `admin_pam_readwrite_service` should accept users who can do any MaxCtrl/REST-API-operation. `admin_pam_readonly_service` should accept users who can only do read operations. Because REST-API does not support back and forth communication between the client and MaxScale, the PAM services must be simple. They should only ask for the password and nothing else.

If only `admin_pam_readwrite_service` is configured, both read and write operations can be authenticated by PAM. If only `admin_pam_readonly_service` is configured, only read operations can be authenticated by PAM. If both are set, the service used is determined by the requested operation. Leave or set both empty to disable PAM for REST-API.

## `admin_port`

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`
* Description: Defines the port at which the REST API waits for incoming connections.

The port where the REST API listens on. The default value is port 8989.

## `admin_readonly_hosts`

Works similar to `admin_readwrite_hosts`. Lists the hosts from which only read operations are allowed. An admin client can do a read operation if their source address matches either `admin_readwrite_hosts` or `admin_readonly_hosts`.

This setting was added in MaxScale 24.02.0.

```
admin_readonly_hosts=mydomain%.com
```

## `admin_readwrite_hosts`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`
* Description: Hosts can perform any REST API operation with read and write access.

Limit REST-API logins to specific source addresses/hosts. Supports a comma-separated list of addresses and hostnames. Addresses can be given in CIDR-notation. Admin clients still need to supply credentials as usual. By default, all source addresses are allowed. `admin_readwrite_hosts` lists the hosts from which any operation is allowed.

This setting was added in MaxScale 24.02.0.

```
admin_readwrite_hosts=192.168.1.1,127.0.0.1/21
```

When listing hostnames, `%` and `_` act as wildcards, similar to the hostname component in MariaDB Server user accounts. `localhost` is a reserved hostname and will not match any connection (use `127.0.0.1` for loopback connections).

When checking the source host of the incoming REST-API client, MaxScale first compares against addresses and address masks. If a match was not found and the setting values contain hostnames, reverse name lookup is performed on the client address. The lookup can take a while in rare cases. To prevent such slowdown, use only IP-addresses in the host lists.

`skip_name_resolve` cannot be enabled if `admin_readwrite_hosts` or `admin_readonly_hosts` includes hostname patterns, as these would not work.

## `admin_root_url`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Prefix path added to all links generated by the REST API.

A prefix path that is added to all links generated by the REST API. This is useful when MaxScale is served behind a reverse proxy under a sub-path, so that the links the REST API returns resolve correctly on the client side. When left empty, no prefix is added.

This parameter was added in MaxScale 25.10.

## `admin_secure_gui`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Manages whether the GUI are accessible only over secure HTTPS.

Whether to serve the GUI only over secure HTTPS connections.

To be secure by default, the GUI is only served over HTTPS connections as it uses a token authentication scheme. This also controls whether the `/auth` endpoint requires an encrypted connection.

To allow use of the GUI without having to configure TLS certificates for the MaxScale REST API, set this parameter to false.

## `admin_ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Path to the CA certificate for outgoing HTTPS requests.

The path to the TLS CA certificate in PEM format.

If defined, the certificate is used as an additional CA certificate for all outbound HTTP request that are done when e.g. `admin_oidc_url` is defined. This can be used when the OIDC server either uses self-signed certificates or the CA is not trusted by default by the operating system.

This does not enable mTLS in the REST-API which means that client TLS certificates are not validated even if a CA is specified.

## `admin_ssl_ca_cert`

Deprecated since MariaDB MaxScale 22.08. See `admin_ssl_ca`.

## `admin_ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Provides the path of the TLS public certificate in PEM format used by the REST API.

The path to the TLS public certificate in PEM format. See `admin_ssl_key` documentation for more details.

## `admin_ssl_cipher`

* Type: string
* Mandatory: No
* Dynamic: No
* Description: Defines additional TLS cipher configuration for the REST API.

Additional TLS cipher settings. The configured value is prepended to [admin\_ssl\_version](#admin_ssl_version) and the resulting string is given as is to [gnutls\_priority\_init](https://gitlab.com/gnutls/gnutls/-/blob/3.8.13/doc/cha-gtls-app.texi#L1271). If left undefined, `NORMAL` is used.

Adding unrecognized elements to this setting will cause REST-API startup to fail with the error:

```
REST API HTTP daemon error: Setting priorities to ... failed: The request is invalid.
```

The value should typically start with a collection of ciphersuites, such as "NORMAL" or "SECURE256". Then, add or remove algorithms with more specific cipher definitions such as "+AES-128-GCM" or "-AES-128-GCM".

```
admin_ssl_cipher=SECURE256:-ECDHE-RSA:-AES-256-CCM:+AES-128-GCM
```

## `admin_ssl_key`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Indicates the location of the TLS private key in PEM format that the admin interface uses.

The path to the TLS private key in PEM format for the admin interface.

If the `admin_ssl_key` and `admin_ssl_cert` options are all defined, the admin interface will use encrypted HTTPS instead of plain HTTP.

The REST-API only supports PKCS#8 PEM private keys and using a PKCS#1 PEM private key will result in an error. If your private key is in PKCS#1 PEM format, convert it to PKCS#8 PEM format first before starting up MaxScale.

If the key is protected by a password, the password must be provided with [admin\_ssl\_passphrase](#admin_ssl_passphrase).

## `admin_ssl_passphrase`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Provides the passphrase needed to decrypt the admin interface's TLS private key.

For details, please see [ssl\_passphrase](README.md#ssl_passphrase) that behaves exactly like `admin_ssl_passphrase`.

## `admin_ssl_verify_peer_certificate`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the client TLS certificate for REST-API connections (REST-API counterpart of `ssl_verify_peer_certificate`).

Verify the peer (client) TLS certificate for REST-API connections. This is the REST-API counterpart to the listener [ssl\_verify\_peer\_certificate](README.md#ssl_verify_peer_certificate) parameter.

When enabled, clients connecting to the REST API must present a certificate, and that certificate is verified against the CA configured with [admin\_ssl\_ca](#admin_ssl_ca). If `admin_ssl_ca` is not set, verification is not performed.

This parameter was added in MaxScale 25.10.

## `admin_ssl_verify_peer_host`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the client host against its certificate for REST-API TLS connections (REST-API counterpart of `ssl_verify_peer_host`).

Verify the peer host for REST-API TLS connections. This is the REST-API counterpart to the listener [ssl\_verify\_peer\_host](README.md#ssl_verify_peer_host) parameter.

When enabled, the client's hostname or IP address is verified against the certificate it presents; if they do not match, the connection is closed. If the client does not provide a certificate, host verification is skipped. To require client certificates, also enable [admin\_ssl\_verify\_peer\_certificate](#admin_ssl_verify_peer_certificate).

This parameter was added in MaxScale 25.10.

## `admin_ssl_version`

* Type: [enum\_mask](README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`
* Description: Specifies the allowed TLS protocol versions for the REST API.

This parameter controls the enabled TLS versions in the REST API. Accepted values are:

* `TLSv10`
* `TLSv11`
* `TLSv12`
* `TLSv13` (not supported on OpenSSL 1.0)
* `MAX`

MaxScale versions 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2 and all newer releases accept also the following alias values:

* `TLSv1.0`
* `TLSv1.1`
* `TLSv1.2`
* `TLSv1.3` (not supported on OpenSSL 1.0)

The default value is `MAX` which negotiates the highest level of encryption that both the client and server support. The list of supported TLS versions depends on the operating system and what TLS versions the GnuTLS library supports.

For example, to enable only TLSv1.1 and TLSv1.3, use `admin_ssl_version=TLSv1.1,TLSv1.3`.

This parameter was added in MaxScale 2.5.7.

Older versions of MaxScale interpreted `admin_ssl_version` as the minimum allowed TLS version. In those versions, `admin_ssl_version=TLSv1.2` allowed both TLSv1.2 and TLSv1.3. In MaxScale 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2 and all newer versions, the value is a enumeration of accepted TLS protocol versions. In these versions, `admin_ssl_version=TLSv1.2` only allows TLSv1.2. To retain the old behavior, specify all the accepted values with `admin_ssl_version=TLSv1.2,TLSv1.3`

## `admin_verify_url`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Delegate the validation of tokens to an external server.

URL to a server to which the REST API token verification is delegated.

If the URL is defined, any tokens passed to the REST API will be validated by doing a GET request to the URL with the client's token as a bearer token. The `Referer` header of the request is set to the URL being requested by the client and the custom `X-Referrer-Method` header is set to the HTTP method being used (PUT, GET etc.).

**Note**: When `admin_verify_url` is used and the remote server cannot be accessed, all REST API access that uses tokens will be disabled. The only way to use the REST API with tokens is to remove `admin_verify_url` from the configuration which requires restarting MaxScale. The REST API still accepts HTTP Basic Access authentication even if the remote server cannot be reached.

By delegating the authentication and authorization of the REST API to an external server, users can implement custom access control systems for the MaxScale REST API.

## `auth_connect_timeout`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`
* Description: Sets the connection timeout for retrieving user authentication data from backend servers.

Duration, default 10s. This setting defines the connection timeout when attempting to fetch MariaDB/MySQL users from a backend server. The same value is also used for read and write timeouts. Increasing this value causes MaxScale to wait longer for a response from a server before user fetching fails. Other servers may then be attempted.

```
auth_connect_timeout=10s
```

The value is given as [a duration](README.md#durations). If no explicit unit is provided, the value is interpreted as seconds. In subsequent versions a value without a unit may be rejected. Since the granularity of the timeout is seconds, a timeout specified in milliseconds will be rejected even if the given value is longer than a second.

## `auth_read_timeout`

Deprecated and ignored as of MaxScale 2.5.0. See _auth\_connect\_timeout_ above.

## `auth_write_timeout`

Deprecated and ignored as of MaxScale 2.5.0. See _auth\_connect\_timeout_ above.

## `auto_tune`

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No
* Description: Allows automatic tuning of specified configuration parameters based on backend server values.

An _auto tunable_ parameter is a parameter whose value can be derived from a particular server variable. With this parameter it can be specified whether `all` or a specific set of parameters should automatically be set.

The current auto tunable parameters are:

| MaxScale Parameter                                                            | Server Variable Dependency                                                                                                                                                                    |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [connection\_keepalive](service-settings.md#connection_keepalive) | 80% of the smallest value of the servers used by the service                                                                                                                                  |
| [wait\_timeout](service-settings.md#wait_timeout)                 | The smallest [wait\_timeout](../../../../../server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#wait_timeout) value of the servers used by the service |

The values of the server variables are collected by monitors, which means that if the servers of a service are not monitored by a monitor, then the parameters of that service will not be auto tuned.

Note that even if `auto_tune` is set to `all`, the auto tunable parameters can still be set in the configuration file and modified with _maxctrl_. However, the specified value will be overwritten at the next auto tuning round, but only if the servers of the service are monitored by a monitor.

## `cachedir`

Removed in MaxScale 25.08. In MaxScale 1, this controlled the location where the database users were cached when access to the servers was not possible. This directory has not been used since the MaxScale 2.0 release.

## `config_sync_cluster`

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Monitor name used for configuration synchronization

This parameter controls which cluster (i.e. monitor) is used to synchronize configuration changes between MaxScale instances. The first server labeled `Master` will be used for the synchronization.

By default configuration synchronization is not enabled and it must be explicitly enabled by defining a monitor name for `config_sync_cluster`.

When `config_sync_cluster` is defined, `config_sync_user` and `config_sync_password` must also be defined.

For a detailed description of this feature, refer to the [Configuration Synchronization](README.md#configuration-synchronization) section.

## `config_sync_db`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`
* Description: Identifies the database that contains the `maxscale_config` table, which is used to synchronize configurations.

The database where the `maxscale_config` table is created. By default the table is created in the `mysql` database. This parameter was added in MaxScale versions 6.4.6 and 22.08.5.

As tables in the `mysql` database cannot have triggers on them, the database must be changed to a user-created one in order to create triggers on the table. An example use-case for triggers on this table is to track all configuration changes done to MaxScale by inserting them into a separate table.

## `config_sync_interval`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`
* Description: Specifies how often MaxScale synchronizes configuration changes with the cluster.

How often to synchronize the configuration with the cluster.

As the synchronization involves selecting the configuration version from the database, this value should not be set to an unreasonably low value. The default value of 5 second should provide a good compromise between responsiveness and how much load it places on the database.

## `config_sync_password`

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: 

The password for `config_sync_user`. Both this parameter and `config_sync_user` are required if `config_sync_cluster` is configured. This password can optionally be encrypted using `maxpasswd`.

## `config_sync_timeout`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`
* Description: Timeout for config sync SQL operations.

Timeout for all SQL operations done during the configuration synchronization. If an operation exceeds this timeout, the configuration change is treated as failed and an error is reported to the client that did the change.

## `config_sync_user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Username used for configuration sync database access across MaxScale instances.

The username for the account that is used to synchronize configuration changes across MaxScale instances. Both this parameter and `config_sync_password` are required if `config_sync_cluster` is configured.

This account must have the following grants:

```
GRANT SELECT, INSERT, UPDATE, CREATE ON `mysql`.`maxscale_config`
```

The `mysql.maxscale_config` table can be pre-created in which case the `CREATE` grant is not needed by the user configured in `config_sync_user`. The following SQL is used to create the table.

```
CREATE TABLE IF NOT EXISTS mysql.maxscale_config(
  cluster VARCHAR(256) PRIMARY KEY,
  version BIGINT NOT NULL,
  config JSON NOT NULL,
  origin VARCHAR(254) NOT NULL,
  nodes JSON NOT NULL
) ENGINE=InnoDB;
```

If the database where the table is created is changed with `config_sync_db`, the grants must be adjusted to target that database instead.

## `connector_plugindir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent
* Description: Specifies the ditrectory that contains MaxScale's MariaDB Connector-C authentication plugins.

Location of the MariaDB Connector-C plugin directory. The MariaDB Connector-C used in MaxScale can use this directory to load authentication plugins. The versions of the plugins must be binary compatible with the connector version that MaxScale was built with.

Starting with version 6.2.0, the plugins are bundled with MaxScale and the default value now points to the bundled plugins. The location where the plugins are stored depends on the operating system. For RHEL versions the value is `/usr/lib64/maxscale/plugin/`. For Debian and Ubuntu it is `/usr/lib/x86_64-linux-gnu/maxscale/plugin/`.

Older versions of MaxScale used `/usr/lib/mysql/plugin/` as the default value.

```
connector_plugindir=/usr/lib64/maxscale/plugin/
```

## `core_file`

* Type: [boolean](README.md#booleans)
* Default: false
* Dynamic: No
* Description: Specifies whether a core dump file is generated in the event that MaxScale crashes.

This parameter specifies whether a core file should be generated if MaxScale crashes. Since 25.10 the default is `false` because usually a core file is not needed, as MaxScale is capable of logging the full stack trace of all threads when it crashes.

## `datadir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`
* Description: Specifies the location of MaxScale's data files directory.

Set the directory where the data files used by MariaDB MaxScale are stored. Modules can write to this directory and for example the binlogrouter uses this folder as the default location for storing binary logs.

This is also the directory where the password encryption key is read from that is generated by `maxkeys`.

```
datadir=/var/lib/maxscale/
```

## `debug`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines debug options equivalent to the `--debug` command line argument.

Define debug options from the --debug command line option. Either the command line option or the parameter should be used, not both. The debug options are only for testing purposes and are not to be used in production.

Separate several options with commas. An option that takes a value is written as `option=value`, for example `debug=disable-module-unloading,sql-batch-size=20Mi`. MaxScale doesn't start if an option is not recognized.

* `allow-duplicate-servers`: Allows several servers to use the same address and port.
* `cors-allow-origin=origin`: Enables CORS support in the REST API and sets the `Access-Control-Allow-Origin` header to the given value.
* `disable-fcrdns`: Disables forward-confirmed reverse DNS lookups for client connections.
* `disable-module-unloading`: Doesn't unload modules at exit. This gives more accurate Valgrind leak reports when leaked memory was allocated in a shared library.
* `disable-statement-logging`: Disables the logging of the SQL statements that monitors and authenticators send to the servers.
* `dump-network-traffic`: Logs all network traffic as `info` level messages.
* `enable-cors`: Enables CORS support in the REST API.
* `enable-module-unloading`: Cancels `disable-module-unloading`.
* `enable-statement-logging`: Enables the logging of the SQL statements that monitors and authenticators send to the servers.
* `exception-frequency=N`: Sets the frequency of generated API exceptions. Available only in debug builds of MaxScale.
* `gdb-stacktrace`: Uses GDB to generate stack traces, if it is available. Disable with `gdb-stacktrace=false`.
* `redirect-output-to-file=path`: Redirects standard output and standard error to the given file.
* `sql-batch-size=size`: Sets the maximum batch size for the REST API. The default is 10 MiB.

## `dump_last_statements`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`
* Description: Manages when MaxScale logs the last statements executed by a client session.

With this configuration item it is specified in what circumstances MaxScale
should write the last statements that a client sent to the log.

If the statements end up being logged, they are logged into the MaxScale
log as notice level log messages well as the system journal, if
enabled.

* `never`: the statements are never logged and are only kept in memory. The
  statements are only shown in the REST-API output as well as in `maxctrl show
  sessions`.

* `on_error`: the statements are logged if the client closes the connection
  improperly or disconnects unexpectedly.

* `on_close`: the statements are always logged when a client session is
  closed. This may produce large amounts of log messages which may affect
  performance if used in environments where there are lots of client
  connections.

Note that you need to specify with `retain_last_statements` how many statements
MaxScale should retain for each session. Unless it has been set to another value
than `0`, this configuration setting will not have an effect.

## `execdir`

Removed in MaxScale 25.10.

## `host_cache_size`

* Type: integer
* Default: 128
* Dynamic: Yes
* Description: Sets the number of entries in the reverse DNS lookup cache for client hostnames.

How many hostname entries are stored in the reverse name lookup cache. Each thread in MaxScale has a cache for the reverse name resolution of client IP addresses to hostnames. Whenever the client authentication requires that a hostname lookup is done, the cache is consulted first. If an entry is found and it was updated less than 300 seconds ago, the cached result is used.

With `host_cache_size=0`, the cache is disabled and a fresh reverse name lookup is always done.

## `key_manager`

* Type: [enum](README.md#enumerations)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`
* Description: Defines the encryption key manager that MaxScale uses.

The encryption key manager to use. The available encryption key managers are:

* `none` - No key manager, encryption keys are not available.
* `file` - [File-based key manager](README.md#file-based-key-manager)
* `kmip` - [KMIP key manager](README.md#kmip-key-manager)
* `vault` - [HashiCorp Vault key manager](README.md#hashicorp-vault-key-manager). This key manager is only included on systems with GCC 9 or newer which means it cannot be used on Ubuntu 18.04.

Refer to the [Encryption Key Managers](README.md#encryption-key-managers) section for more information on how to configure the key managers. The key managers each have their configuration in their own namespace and must have their name as a prefix.

For example to configure the `file` key manager, the following must be used:

```
key_manager=file
file.keyfile=/path/to/keyfile
```

## `language`

Removed in MaxScale 25.08. In MaxScale 1, this controlled the location of an internal data file which has not been used since the MaxScale 2.0 release.

## `libdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent
* Description: Specifies the directory that MaxScale uses to locate modules.

Set the directory where MariaDB MaxScale looks for modules. The library directory is the only directory that MariaDB MaxScale uses when it searches for modules. If you have custom modules for MariaDB MaxScale, make sure you have them in this folder.

The default value depends on the operating system. For RHEL versions the value is `/usr/lib64/maxscale/`. For Debian and Ubuntu it is `/usr/lib/x86_64-linux-gnu/maxscale/`

```
libdir=/usr/lib64/maxscale/
```

## `load_persisted_configs`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Loads saved runtime changes at startup.

Load persisted runtime changes on startup. This parameter was added in MaxScale 2.3.6.

All runtime configuration changes are persisted in generated configuration files located by default in `/var/lib/maxscale/maxscale.cnf.d/` and are loaded on startup after main configuration files have been read. To make runtime configurations volatile (i.e. they are lost when maxscale is restarted), use `load_persisted_configs=false`. All changes are still persisted since it stores the current runtime state of MaxScale. This makes problem analysis easier if an unexpected outage happens.

## `local_address`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines what specific local interface to use when connecting to servers.

What specific local address/interface to use when connecting to servers.

This can be used for ensuring that MaxScale uses a particular interface when connecting to servers, in case the computer MaxScale is running on has multiple interfaces.

```
local_address=192.168.1.254
```

If given as a hostname, MaxScale will perform name lookup on the address when starting and reuse the result.

## `log_augmentation`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`
* Description: Includes function names to logged messages.

Enable or disable the augmentation of messages. If this is enabled, then each logged message is appended with the name of the function where the message was logged. This is primarily for development purposes and hence is disabled by default.

```
# Valid options are:
#       log_augmentation=<0|1>
log_augmentation=1
```

To disable the augmentation use the value 0 and to enable it use the value 1.

## `log_debug`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Log debug messages when enabled.

Log messages whose syslog priority is _debug_.

These messages are intended for development purposes and are disabled by default. These are rarely useful outside of debugging core MaxScale issues.

**Note:** If MariaDB MaxScale has been built in release mode, then debug messages are excluded from the build and this setting will not have any effect. If an attempt to enable these is made, a warning is logged.

## `log_info`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Log detailed info messages when enabled.

Log messages whose syslog priority is _info_.

These messages provide detailed information about the internal workings of MariaDB MaxScale. These messages should only be enabled when there is a need to inspect the internal logic of MaxScale. A common use-case is to see why a particular query was handled in a certain way. Almost all modules log some messages on the info level and this can be very helpful when trying to solve routing related problems.

## `log_notice`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Log notice level messages when enabled.

Log messages whose syslog priority is _notice_.

These messages contain information that is helpful for the user and they usually do not indicate a problem. These are logged whenever something worth nothing happens in either MaxScale or in the servers it monitors.

## `log_throttling`

* Type: number, [duration](README.md#durations), [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`
* Description: Manages how frequently repeated errors or warnings are logged.

It is possible that a particular error (or warning) is logged over and over again, if the cause for the error persistently remains. To prevent the log from flooding, it is possible to specify how many times a particular error may be logged within a time period, before the logging of that error is suppressed for a while.

```
# A valid value looks like
#       log_throttling = X, Y, Z
#
# where the first value X is a positive integer and means the number of times
# a specific error may be logged within a duration of Y, before the logging
# of that error is suppressed for a duration of Z.
log_throttling=8, 2s, 15000ms
```

In the example above, the logging of a particular error will be suppressed for 15 seconds if the error has been logged 8 times in 2 seconds.

The default is `10, 1000ms, 10000ms`, which means that if the same error is logged 10 times in one second, the logging of that error is suppressed for the following 10 seconds.

Whenever an error message that is being throttled is logged within the triggering window (the second argument), the suppression window is extended. This continues until there is a pause in the messages that is longer than the triggering window.

For example, with the default configuration the messages must pause for at least one second in order for the throttling to eventually stop. This mechanism prevents long-lasting error conditions from slowly filling up the log with short bursts of messages.

To disable log throttling, add an entry with an empty value

```
log_throttling=
```

or one where any of the integers is 0.

```
log_throttling=0, 0, 0
```

The durations can be specified as documented [here](README.md#durations). If no explicit unit is provided, the value is interpreted as milliseconds in MaxScale 2.4. In subsequent versions a value without a unit may be rejected.

Note that _notice_, _info_ and _debug_ messages are never throttled.

## `log_timestamp_format`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `datetime`, `iso_8601`
* Default: `default`
* Description: Selects the timestamp format used in log messages.

The log timestamp format to use. The `default` and `iso_8601` values use ISO
8601 timestamps with UTC timezone offset. The `datetime` is the legacy timestamp
format. The formats, where the millisecond part is optional, are:

* `iso_8601`: `YYYY-MM-DDTHH:MM:SS[.sss]+HH:MM`
* `datetime`: `YYYY-MM-DD HH:MM:SS[.sss]`

By default, if there are legacy log messages found in the first 100 lines of the
MaxScale log, a warning is logged. To disable this warning, use `iso_8601`.

## `log_warn_super_user`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Log warning when a client with SUPER privilege connects.

When enabled, a warning is logged whenever a client with SUPER-privilege successfully authenticates. This also applies to COM\_CHANGE\_USER-commands. The setting is intended for diagnosing situations where a client interferes with a primary server switchover. Super-users bypass the _read\_only_-flag which switchover uses to block writes to the primary.

## `log_warning`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Enable service-level warning logging.

Log messages whose syslog priority is _warning_.

MaxScale logs warning level messages whenever a condition is encountered that the user should be notified of but does not require immediate action or it indicates a minor problem.

## `logdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`
* Description: Defines the directory where log files are stored.

Set the directory where the logfiles are stored. The folder needs to be both readable and writable by the user running MariaDB MaxScale.

```
logdir=/var/log/maxscale/
```

## `max_auth_errors_until_block`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0` from 26.10.0, `10` until 25.10
* Description: Maximum number of authentication failures before temporarily blocking a host.

{% hint style="info" %}
In MaxScale 26.10, the default changes to `0`, which disables this feature. Hosts are blocked by [max\_connect\_errors](#max_connect_errors) instead.
{% endhint %}

The maximum number of authentication failures that are tolerated before a host is temporarily blocked.

The block applies to the whole host, not to the user whose authentication failed. Every client that connects from that host is rejected, including applications that use other accounts. After a host is blocked, connections from it are rejected until no connection has been attempted from it for 60 seconds. Each attempt during the block restarts the 60 seconds. A successful authentication from the host resets its failure count.

Note that the configured value is not a hard limit. The number of tolerated failures is between `max_auth_errors_until_block` and `threads * max_auth_errors_until_block` where `max_auth_errors_until_block` is the configured value of this parameter and `threads` is the number of configured threads.

## `max_connect_errors`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `100` from 26.10.0, `0` until 25.10.
* Description: Maximum number of aborted connection attempts before temporarily blocking a host.

{% hint style="info" %}
This parameter is available from MaxScale 25.10.4. In MaxScale 26.10, its default changes to `100`, and it replaces [max\_auth\_errors\_until\_block](#max_auth_errors_until_block) as the default way of blocking hosts.
{% endhint %}

The maximum number of aborted connection attempts that are tolerated before a host is temporarily blocked. A connection attempt counts as aborted when the handshake fails, or when the client disconnects before authentication completes without having failed authentication. Failed authentications are counted by `max_auth_errors_until_block` instead. The default value is 0, which disables this feature.

This is similar to the [max\_connect\_errors](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connect_errors) system variable of MariaDB Server, with two differences:

* MaxScale doesn't block the host until `FLUSH HOSTS` is run. It rejects connections from the host until no connection has been attempted from it for 60 seconds. Each attempt during the block restarts the 60 seconds.
* The configured value is not a hard limit. The number of tolerated aborted attempts is between `max_connect_errors` and `threads * max_connect_errors`, where `threads` is the number of configured threads.

A successful authentication from the host resets its count.

## `maxlog`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Enables logging of messages to the MaxScale log file.

Log messages to MariaDB MaxScale's log file. The name of the log file is `maxscale.log` and it is located in the directory pointed by [logdir](#logdir).

## `module_configdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`
* Description: Directory for module-specific configuration files.

Configure the directory where module configurations are stored. Path arguments are resolved relative to this directory. This directory should be used to store module specific configurations.

Any configuration parameter that is not an absolute path will be interpreted as a relative path. The relative paths use the module configuration directory as the working directory.

For example, the configuration parameter `file=my_file.txt` would be interpreted as `/etc/maxscale.modules.d/my_file.txt` whereas `file=/home/user/my_file.txt` would be interpreted as `/home/user/my_file.txt`.

```
module_configdir=/etc/maxscale.modules.d/
```

## `ms_timestamp`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Adds millisecond precision to logfile timestamps.

Enable or disable the high precision timestamps in logfiles. Enabling this adds millisecond precision to all logfile timestamps.

## `passive`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Deprecated - use [cooperative monitoring](../../../../reference/maxscale-monitors/mariadb-monitor/README.md#cooperative-monitoring) instead.

Controls whether MaxScale is a passive node in a cluster of multiple MaxScale instances.

This parameter is intended to be used with multiple MaxScale instances that use failover functionality to manipulate the cluster in some form. Passive nodes only observe the clusters being monitored and take no direct actions.

The following functionality is disabled when passive mode is enabled:

* Automatic failover in the `mariadbmon` module
* Automatic rejoin in the `mariadbmon` module
* Launching of monitor scripts

**NOTE:** Even if MaxScale is in passive mode, it will still accept clients and route any traffic sent to it. The **only** operations affected by the passive mode are the ones listed above.

## `persist_runtime_changes`

* Type: [boolean](README.md#booleans)
* Default: true
* Dynamic: No
* Description: Save runtime configuration changes to disk.

Persist changes done at runtime. This parameter was added in MaxScale 22.08.0.

When `persist_runtime_changes` is enabled, runtime configuration changes done with the GUI, MaxCtrl or via the REST API cause a new configuration file to be saved in `/var/lib/maxscale/maxscale.cnf.d/`. If `load_persisted_configs` is enabled, these files will be applied on top of any existing values found in static configuration files whenever MaxScale is starting up.

## `persistdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`
* Description: Directory where runtime configuration changes are stored.

Configure the directory where persisted configurations are stored. When a new object is created via MaxCtrl, it will be stored in this directory. Do not use this directory for normal configuration files, use _/etc/maxscale.cnf.d/_ instead. The user MaxScale is running as must be able to write into this directory.

```
persistdir=/var/lib/maxscale/maxscale.cnf.d/
```

## `piddir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`
* Description: Specifies the directory containing the MaxScale process ID (PID) file.

Configure the directory for the PID file for MariaDB MaxScale. This file contains the Process ID for the running MariaDB MaxScale process.

MaxScale versions before 24.08.1 used the path `/var/run/maxscale/` for the PID files. This was a legacy path according to the Filesystem Hierarchy Standard and starting with MaxScale 24.08.1, the appropriate modern PID file path is used.

The value of `piddir` should not be changed when MaxScale is installed from a DEB/RPM package and is run as a SystemD service. The SystemD service file in `/lib/systemd/systemd/maxscale.service` depends on the PID file being stored at `/run/maxscale/maxscale.pid`. However, if `piddir` must be modified to point to a non-default location, it must also be modified in the SystemD service file configuration to point to the new location.

## `query_classifier`

Deprecated since MariaDB MaxScale 23.08.

## `query_classifier_args`

Deprecated since MariaDB MaxScale 23.08.

## `query_classifier_cache_size`

* Type: [size](README.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent
* Description: Sets the maximum size of the query classifier cache.

Specifies the maximum size of the query classifier cache. The default limit is 15% of _available_ system memory. The available system memory may be less than the _total_ system memory, if MaxScale is running in a container whose resources have been limited.

When the query classifier cache has been enabled, MaxScale will, after a statement has been parsed, store the classification result using the canonicalized version of the statement as the key.

If the classification result for a statement is needed, MaxScale will first canonicalize the statement and check whether the result can be found in the cache. If it can, the statement will not be parsed at all but the cached result is used.

The configuration parameter takes one integer that specifies the maximum size of the cache. The size of the cache can be specified as explained [here](README.md#sizes).

```
# 1MB query classifier cache
query_classifier_cache_size=1MB
```

Note that MaxScale uses a separate cache for each worker thread. To obtain the amount of memory available for each thread, divide the cache size with the value of `threads`. If statements are evicted from the cache (visible in the diagnostic output), consider increasing the cache size.

Note also that limit is not a hard limit, but an approximate one. Namely, although the memory needed for storing the canonicalized statement and the classification result is correctly accounted for, there is additional overhead whose size is not exactly known and over which we do not have direct control.

Using `maxctrl show threads` it is possible to check what the actual size of the cache is and to see performance statistics.

| Key                | Meaning                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| QC cache size      | The current size of the cache (bytes).                                                                                  |
| QC cache inserts   | How many entries have been inserted into the cache.                                                                     |
| QC cache hits      | How many times the classification result has been found from the cache.                                                 |
| QC cache misses    | How many times the classification result has not been found from the cache, but the classification had to be performed. |
| QC cache evictions | How many times a cache entry has had to be removed from the cache, in order to make place for another.                  |

## `query_retries`

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`
* Description: Deprecated and ignored.

Deprecated and ignored.

## `query_retry_timeout`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`
* Description: Deprecated and ignored.

Deprecated and ignored.

## `rebalance_period`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Description: Defines the interval for monitoring and rebalancing worker thread load. A value of `0` disables this function.

This duration parameter controls how often the load of the worker threads should be checked. The default value is 0, which means that no checks and no rebalancing will be performed.

```
rebalance_period=10s
```

Note that the value of `rebalance_period` should not be smaller than the value of `rebalance_window` whose default value is 10.

If the value of `rebalance_period` is significantly shorter than that of `rebalance_window`, it may lead to oscillation where work is constantly moved from one thread to another.

## `rebalance_threshold`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`
* Description: Load difference percentage that triggers thread rebalancing.

This integer parameter controls at which point MaxScale should start moving work from one worker thread to another.

If the difference in load between the thread with the maximum load and the thread with the minimum load is larger than the value of this parameter, then work will be moved from the former to the latter.

Although the load of a thread can vary between 0 and 100, the value of this parameter must be between 5 and 100.

```
rebalance_threshold=15
```

Note that rebalancing will not be performed unless `rebalance_period` has been specified.

## `rebalance_window`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`
* Description: Manages how many seconds of load to consider for rebalancing.

This integer parameter controls how many seconds of load should be taken into account when deciding whether work should be moved from one thread to another.

The default value is 10, which means that the load during the last 10 seconds is considered when deciding whether work should be moved.

The minimum value is 1 and the maximum 60.

## `require_secure_transport`

* Type: [boolean](README.md#booleans)
* Default: false
* Dynamic: No
* Description: Requires SSL for all listeners, servers, and the REST API.

If enabled, listeners, servers and REST-API must be configured to use SSL. Any static configuration or runtime configuration change that disables SSL will fail. Kafka connections created by the KafkaCDC and KafkaImporter modules must also be configured for SSL. ODBC connection strings used with the REST-API SQL Connection Interface are not affected. Listeners and servers that use Unix socket connections are ignored as they are considered secure even without SSL.

## `retain_last_statements`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`
* Description: Specifies how many statements MaxScale can store per session.

How many statements MaxScale should store in memory for each session. This is
for debugging purposes, as in case of problems it is often of value to be able
to find out exactly what statements were sent before a particular problem turned
up.

**Note:** See also `dump_last_statements` using which the actual logging of the
statements is enabled. Unless both of the parameters are defined, the statement
logging mechanism doesn't work.

This mechanism is also used to show the currently active queries for sessions in
`maxctrl show session` output as well as in `maxctrl list queries`.

```
retain_last_statements=20
```

## `secretsdir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Location of the .secrets file for password encryption.

The location where the `.secrets` file is read from. If `secretsdir` is not defined, the file is read from [datadir](#datadir).

This parameter was added in MaxScale 6.4.16, 22.08.13, 23.02.10, 23.08.6 and 24.02.2.

## `session_trace`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`
* Description: Defines how many log entries are stored in the session trace log.

How many log entries are stored in the session specific trace log. This log is written to disk when a session ends abnormally and can be used for debugging purposes. The session trace log is written to the log in the following situations:

* When MaxScale receives a fatal signal and is about to crash.
* Whenever an unexpected response is read from a server
* If the session is not closed gracefully (i.e. client doesn't send a COM\_QUIT packet)
* Whenever readwritesplit receives a response that is was not expecting.

It would be good to enable this if a session is disconnected and the log is not detailed enough. In this case the info log might reveal the true cause of why the connection was closed.

```
session_trace=20
```

Default is `0`.

The session trace log is also exposed by REST API and is shown with`maxctrl show sessions`.

The order in which the session trace messages are logged into the log changed in MaxScale 6.4.9 (MXS-4716). Newer versions will log the messages in the "normal log order" of older events coming first and newer events appearing later in the file. Older versions of MaxScale logged the trace dump in the reverse order with the newest messages first and oldest ones last.

## `session_trace_match`

* Type: [regex](README.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a refular expression pattern used to filter session trace logs.

If both `session_trace` and `session_trace_match` are defined, and a trace log entry of a session matches the regular expression, the trace log is written to disk and then cleared. This way subsequent matches will only write new log entries.

In MaxScale versions 24.08 and older, the check for the match was done only when the session was stopping.

The most effective way to debug MaxScale related issues is to turn on `log_info` and observe the events written into the MaxScale log. The only problem with this approach is that it can cause a severe performance bottleneck and can easily fill up the disk as the amount of data written to it is significant. With `session_trace` and `session_trace_match`, the content that actually gets logged can be filtered to only what is needed.

For example, the following configuration would only log the trace log messages from sessions that execute SQL queries with syntax errors:

```
session_trace=1000
session_trace_match=/You have an error in your SQL syntax/
```

This could be used to easily identify which applications execute the queries without having to gather the info level log output from all the sessions that connect to MaxScale. For every session that ends up logging a syntax error message, the last 1000 lines of log output done by that session is written into the MaxScale log.

## `sharedir`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`
* Description: Defines the directory where static data assets are loaded.

Sets the directory where static data assets are loaded.

The MaxScale GUI static files are located in the `gui/` subdirectory. If the GUI files have been manually moved somewhere else, this path must be configured to point to the parent directory of the `gui/` subdirectory.

The MaxScale REST API only serves files for the GUI that are located in the `gui/` subdirectory of the configured `sharedir`. Any files whose real path resolves to outside of this directory are not served by the MaxScale GUI: this is done to prevent other files from being accessible via the MaxScale REST API. This means that path to the GUI source directory can contain symbolic links but all parts after the `/gui/` directory must reside inside it.

## `skip_name_resolve`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Disables reverse DNS lookups of client IP addresses.

This parameter controls whether reverse domain name lookups are made to convert client IP addresses to hostnames. If enabled, client IP addresses will not be resolved to hostnames during authentication or for the REST API even if requested.

If you have database users that use a hostname in the host part of the user (i.e. `'user'@'my-hostname.org'`), a reverse lookup on the client IP address is done to see if it matches the host. Reverse DNS lookups can be very slow which is why it is recommended that they are disabled and that users are defined using an IP address.

## `sql_mode`

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`
* Description: Defines which SQL language mode the query classifier should expect.

Specifies whether the query classifier parser should initially expect _MariaDB_ or _PL/SQL_ kind of SQL.

The allowed values are: `default`: The parser expects regular _MariaDB_ SQL. `oracle` : The parser expects PL/SQL.

```
sql_mode=oracle
```

**NOTE** If `sql_mode` is set to `oracle`, then MaxScale will also assume that `autocommit` initially is off.

At runtime, MariaDB MaxScale will recognize statements like

```
set sql_mode=oracle;
```

and

```
set sql_mode=default;
```

and change mode accordingly.

**NOTE** If `set sql_mode=oracle;` is encountered, then MaxScale will also behave as if `autocommit` had been turned off and conversely, if `set sql_mode=default;` is encountered, then MaxScale will also behave as if `autocommit` had been turned on.

Note that MariaDB MaxScale is **not** explicitly aware of the sql mode of the server, so the value of `sql_mode` should reflect the sql mode used when the server is started.

## `statistics`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true
* Description: Enables tracking of query statistics such as query execution latency.

Enable tracking of query statistics.

By default MaxScale tracks the latency of each executed query and keeps a record
of the latency distribution. These latency measurements are then exported as
metrics via the telemetry. The values are also exposed in the REST-API and the
output of `maxctrl show qc_cache`. The `maxctrl show query_statistics` command
also displays them.

There is a cost to tracking the latency distribution. The most notable cost is
an increase in memory usage per query which causes more pressure on the query
classification cache. If the number of cache evictions reported in `maxctrl show
threads` steadily increases, increase the value of `query_classifier_cache_size`
from the default 15% of system memory to a value that's high enough that
evictions no longer take place.

There is also a CPU cost to tracking the latency but this is usually less of an
issue. However, if telemetry is not being exported and the query statistics are
not used, both the memory and CPU cost can be avoided by disabling the tracking
of the statistics with `statistics=false`.

## `substitute_variables`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Allows use of environment variables within MaxScale configuration files.

Enable or disable the substitution of environment variables in the MaxScale configuration file. If the substitution of variables is enabled and a configuration line like

```
some_parameter=$SOME_VALUE
```

is encountered, then `$SOME_VALUE` will be replaced with the actual value of the environment variable `SOME_VALUE`. Note:

* Variable substitution will be made _only_ if '$' is the first character of the value.
* _Everything_ following '$' is interpreted as the name of the environment variable.
* Referring to a non-existing environment variable is a fatal error.

```
substitute_variables=true
```

The setting of `substitute_variables` will have an effect on all parameters in the all other sections, irrespective of where the `[maxscale]` section is placed in the configuration file. However, in the `[maxscale]` section, to ensure that substitution will take place, place the `substitute_variables=true` line first.

## `syslog`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Writes log messages to the system journal via the system logging interface.

Log messages to the system journal. This logs messages using the native SystemD journal interface. The logs can be viewed with `journalctl`.

MaxScale 22.08 changed the default value of `syslog` from `true` to `false`. This was done to remove the redundant logging that it caused as both `syslog` and `maxlog` were enabled by default. This caused each message to be logged twice: once into the system journal and once into MaxScale's own logfile.

## `telemetry`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Enables sending metrics to OpenTelemetry Collector.

When enabled MaxScale sends telemetry to the OpenTelemetry Collector. For the list of exported metrics, see [MaxScale Telemetry](../../../../reference/maxscale-telemetry.md).

## `telemetry_attributes`

* Type: stringlist
* Default: empty
* Dynamic: Yes
* Mandatory: No
* Description: Global attributes to send with every metric.

Optional global attributes to send with every metric. Example `telemetry_attributes=project=default-project,cluster=mariadb1,instance=maxscale1`

## `telemetry_logs_url`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Defines the URL where OpenTelemetry logs are sent, overriding the one derived from `telemetry_url`.

URL where OpenTelemetry logs are sent. This overrides the value that's automatically derived from `telemetry_url`. Use this if you want to send logs to a separate or non-standard location.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

## `telemetry_metrics_url`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Defines the URL where OpenTelemetry metrics are sent, overriding the one derived from `telemetry_url`.

URL where OpenTelemetry metrics are sent. This overrides the value that's automatically derived from `telemetry_url`. Use this if you want to send metrics to a separate or non-standard location.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

## `telemetry_signals`

* Type: [enum\_mask](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `metrics`, `logs`
* Default: `metrics,logs`
* Description: Specifies which telemetry signals, metrics and logs, are sent.

The telemetry signals to send. By default both metrics and logs are sent if telemetry is enabled.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later. Older versions
only send metrics.
{% endtab %}
{% endtabs %}

## `telemetry_sql_count`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 50
* Description: Defines the maximum number of the most used SQL query digests that are sent as metrics.

How many of the most used SQL query digests are sent as metrics.

The metrics track the approximate 50th, 75th, 95th and 99th percentile query
execution latency for each unique query pattern as well as per server. By
default only the top 50 most used queries by frequency are sent. If there are
more than 50 different query digests that are of interest or you are not seeing
the query you're interested in, increase the value of `telemetry_sql_count` or
use `telemetry_sql_match` and `telemetry_sql_exclude` to filter the metrics to
the important ones.

For the full list of exported metrics, see
[MaxScale Telemetry](../../../../reference/maxscale-telemetry.md).

## `telemetry_sql_exclude`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [regex](README.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regular expression that excludes matching SQL query digests from the metrics.

Regular expression that's used to exclude SQL query digests from being sent over
as metrics.

This regular expression is matched against the SQL query digest which has all
the constant values replaced with question marks. If the query matches, the
digest is excluded from the metrics.

## `telemetry_sql_match`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [regex](README.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Defines a regular expression that selects the SQL query digests that are sent as metrics.

Regular expression that's used to select which SQL query digests are sent over
as metrics.

This regular expression is matched against the SQL query digest which has all
the constant values replaced with question marks. Only query digests that match
the pattern are included in the metrics.

## `telemetry_ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Path to trusted CA certificate (PEM) used for validating TLS connections in telemetry.

The path to a TLS CA certificate in PEM format.

## `telemetry_ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Specifies the file path to the TLS public certificate in PEM format for telemetry.

The path to the TLS public certificate in PEM format. See `telemetry_ssl_key` and `admin_ssl_key` for more documentation details.

## `telemetry_ssl_insecure`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false
* Description: Disable TLS certificate validation for telemetry.

When enable and SSL certificates are defined, MaxScale OpenTelemetry uses insecure HTTPS and doesn't validate certificates.

## `telemetry_ssl_key`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: TLS private key for encrypted telemetry.

The path to the TLS private key in PEM format for sending telemetry.

If the `telemetry_ssl_ca` and `telemetry_ssl_cert` options are all defined, the sending of metrics will use encrypted HTTPS instead of plain HTTP. If setting SSLm you also must to change the `telemetry_url` to `https` as in `https://localhost:4318/v1/metrics`.

## `telemetry_update_interval`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`
* Description: Defines the minimum interval between sending metrics to the telemetry collector.

Minimum interval to send metrics to the collector.

## `telemetry_url`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `http://localhost:4318`
* Description: Defines the OpenTelemetry endpoint where MaxScale pushes metrics.

{% tabs %}
{% tab title="Current" %}
The OpenTelemetry base URL where MaxScale pushes metrics and logs. The
metrics and logs paths are appended to this URL. If the value ends in
`/v1/metrics`, as the old default value `http://localhost:4318/v1/metrics`
does, the suffix is automatically dropped.
{% endtab %}

{% tab title="< 26.10" %}
The OpenTelemetry metrics URL where MaxScale pushes metrics. The default
value is `http://localhost:4318/v1/metrics`.
{% endtab %}
{% endtabs %}

## `threads`

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`
* Description: Manages the number of worker threads for routing client traffic.

This parameter controls the number of worker threads that are used for routing client traffic. The default is `auto` which uses as many threads as there are virtual CPU cores available to MaxScale, rounded up to the nearest integer. If no limitations have been set using CPU affinities or cgroup CPU quotas, this will be the same as the number of CPU cores. In general, as of 24.08, MaxScale will use the appropriate number of threads, also when it is running in a container.

The maximum value for `threads` is specified by [threads\_max](#threads_max).

```
# Valid options are:
#       threads=[<number of threads> | auto ]

[MaxScale]
threads=auto
```

From 23.02 onwards it is possible to change the number threads at runtime. Please see [Threads](README.md#threads) for more details.

Additional threads will be created to execute other internal services within MariaDB MaxScale. This setting is used to configure the number of threads that will be used to manage the user connections.

## `threads_max`

* Type: positive integer
* Default: 256
* Dynamic: No
* Description: Hard limit for the number of worker threads.

This parameter specifies the hard limit for the number of worker threads, which is specified using [threads](#threads).

At startup, if the value of `threads` is larger than that of `threads_max`, the value of `threads` will be reduced to that. At runtime, an attempt to increase the value of `threads` beyond that of `threads_max` is an error.

## `trace_file_dir`

* Type: path
* Mandatory: No
* Dynamic: No
* Description: Directory for low-overhead trace log files.

Path to a directory where trace files will be generated to.

The trace logging offers a low overhead alternative to `log_info` that is designed to be placed on a local in-memory file system. By placing the files in a location that is not persistent, the overhead of writing to the files is minimal while still allowing the trace logs to be processed as normal log files.

If this parameter is defined along with `trace_file_size`, MaxScale will write all log messages from all log levels into a set of trace files located in this directory. The files are named `maxscale.trace.N` where `N` is an increasing number and whenever a new file is created the oldest one is removed if there are more than 10 trace files.

Starting with MaxScale 24.08.1, the `maxscale.trace` symlink will be created in [the log directory](#logdir) that will point to the latest log file. This symlink can be used with `tail -F` to interactively monitor the trace stream or to copy the trace output directly into a compressed file:

```
# Note: to get a clean compressed file, kill the 'tail' process and instead of
# using Ctrl+C to kill 'gzip'.
tail -F /var/log/maxscale/maxscale.trace | gzip > maxscale.trace.gz
```

The trace files differ from the normal log file written by MaxScale in that they do not contain the local timestamp and instead contain a raw fractional UNIX timestamp. The format of the trace file is subject to change.

## `trace_file_size`

* Type: [size](README.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Description: Amount of log data to keep in trace files.

The desired amount of log data to keep in the trace files. Each individual trace file will be one tenth the size of `trace_file_size` and once they exceed this amount, a trace log rotation will occur. For example with `trace_file_size=100Mi`, roughly 100MiB of log data is kept in 10 files with about 10MiB of data in each file.

Individual trace files may sometimes exceed this limit and under heavy load the system may end up temporarily using more space than is intended.

## `users_refresh_interval`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Description: Defines the interval for automatically refreshing user accounts from backend servers.

How often, in seconds, MaxScale will automatically refresh the users from the backend server.

This configuration is used to periodically refresh the backend users, making sure they are up to date. The default value for this setting is 0, meaning the users are not periodically refreshed. However, they can still be refreshed in case of failed authentication depending on `users_refresh_time`.

```
users_refresh_interval=2h
```

## `users_refresh_time`

* Type: [duration](README.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`
* Description: Maximum frequency for refreshing user accounts from backend servers after authentication failures.

How often, in seconds, MaxScale at most may refresh the users from the backend server.

MaxScale will at startup load the users from the backend server, but if the authentication of a user fails, MaxScale assumes it is because a new user has been created and will thus refresh the users. By default, MaxScale will do that at most once per 30 seconds and with this configuration option that can be changed. A value of 0 allows infinite refreshes and a negative value disables the refreshing entirely.

```
users_refresh_time=120s
```

The value is specified as documented [here](README.md#durations). If no explicit unit is provided, the value is interpreted as seconds in MaxScale 2.4. In subsequent versions a value without a unit may be rejected. Note that since the granularity of the timeout is seconds, a timeout specified in milliseconds will be rejected, even if the duration is longer than a second.

In MaxScale 2.3.9 and older versions, the minimum allowed value was 10 seconds but, due to a bug, the default value was 0 which allowed infinite refreshes.

## `worker_assignment`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [enum](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `local`, `roundrobin`
* Default: `local`
* Description: Selects how new client connections are assigned to worker threads.

Set the thread assignment method for new connections.

Whenever MaxScale accepts a new connection, the client connection is assigned to
one of the worker threads. All threads attempt to accept new connections and
with the default `local` mode, the worker thread that accepts the connection is
the one that the connection is assigned to. The benefit of this mode is that
threads that are busy doing work have a smaller chance of accepting new
connections and under a constant stream of new connections, threads with less
work will naturally pick up more clients. Under bursty loads where connections
come in batches and stay alive for a long time, the distribution of the
connections may not be optimal. For workloads where the connections have short
to moderate lifetimes, the default `local` mode is the best choice as it
balances the load based on how busy each worker thread is.

With the `roundrobin` mode, all worker threads still accept connections but the
worker thread is assigned in a round-robin manner so that each thread gets an
equal number of connections. This mode works well when clients connect to
MaxScale in batches and the sessions stay alive for a long time. If the workload
consists of a small number of connections with very long lifetimes, for example
when client-side connection pooling is used, it guarantees an even distribution
of the connections. This is also a good mode for doing performance evaluations
with load generation frameworks that open up the connections on startup.

## `writeq_high_water`

* Type: [size](README.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`
* Description: High water mark for network write buffer throttling.

High water mark for network write buffer. When the size of the outbound network buffer in MaxScale for a single connection exceeds this value, network traffic throttling for that connection is started. The parameter accepts [size type values](README.md#sizes). The default value was 16777216 bytes before 22.08.4.

More specifically, if the client side write queue is above this value, it will block traffic coming from backend servers. If the backend side write queue is above this value, it will block traffic from client.

The buffer that this parameter controls is the buffer internal to MaxScale and is not the kernel TCP send buffer. This means that the total amount of buffered data is determined by both the kernel TCP buffers and the value of `writeq_high_water`.

Network throttling is only enabled when `writeq_high_water` is non-zero. In MaxScale 23.02 and earlier, also `writeq_low_water` had to be non-zero.

## `writeq_low_water`

* Type: [size](README.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`
* Description: Low water mark to disable network write throttling.

Low water mark for network write buffer. Once the traffic throttling is enabled, it will only be disabled when the network write buffer is below `writeq_low_water` bytes. The parameter accepts [size type values](README.md#sizes). The default value was 8192 bytes before 22.08.4.

The value of `writeq_high_water` must always be greater than the value of `writeq_low_water`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
