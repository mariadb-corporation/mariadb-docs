---
description: >-
  Reference for every nosqlprotocol listener setting, in alphabetical order:
  credentials, authentication and authorization, auto-creation, and caching.
---

# MaxScale NoSQL Protocol Settings

The settings are listed in alphabetical order. For how to configure a nosqlprotocol listener, see [Configuring](README.md#configuring).

Using the following parameters, the behavior of _nosqlprotocol_ can be adjusted. As they are not generic listener parameters, but specific to _nosqlprotocol_ they must be qualified with the `nosqlprotocol`-prefix.

For instance:

```
[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
nosqlprotocol.on_unknown_command=return_error
...
```

## `authentication_db`

* Type: string
* Mandatory: No
* Default: `"NoSQL"`
* Description: Specifies the database that stores NoSQL account information for authentication.

Specifies the database of the table where the NoSQL account information is stored, if `authentication_shared` is `true`. If the database does not exist, nosqlprotocol will attempt to create it, so either is should be manually created or the used specified with `authentication_user` should have the grants required to do so.

## `authentication_key_id`

* Type: string
* Mandatory: No
* Default: `""`
* Description: Specifies the encryption key ID used to encrypt NoSQL account information in the database.

The encryption key ID, using which the NoSQL account information should be encrypted with when stored in the MariaDB server. If an encryption key ID is given, the encryption key manager in MaxScale must also be enabled.

The encryption key must be a 256-bit key. Keys of shorter length are rejected as invalid encryption keys.

## `authentication_password`

* Type: string
* Mandatory: No
* Default: `""`
* Description: Specifies the password for the NoSQL authentication user.

Specifies the _password_ of `authentication_user`.

## `authentication_required`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `false`
* Description: Determines whether clients are required to authenticate before accessing the service.

Specifies whether the client always must authenticate. If authentication is required, it does not matter whether `user` and `password` have been specified, the client must authenticate.

Authentication should not be required before users have been created with [createUser](nosql-protocol-database-commands.md#createuser) or added with [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser), with authentication being optional and authorization being disabled.

NOTE: All client activity is _always_ subject to authorization performed by the MariaDB server.

## `authentication_shared`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `false`
* Description: Controls whether NoSQL account information is stored in a shared or private manner.

Specifies whether the NoSQL account information should be stored in a shared manner or privately.

## `authentication_user`

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.
* Description: Specifies the user used to access and manage shared NoSQL account information.

Specifies the _user_ to be used when modifying and accessing the NoSQL account information stored in the MariaDB server.

## `authorization_enabled`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `false`
* Description: Enables or disables NoSQL protocol–level authorization for user management commands.

Specifies whether nosqlprotocol itself should perform authorization in the context of the commands [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser), [mxsRemoveUser](nosql-protocol-database-commands.md#mxsremoveuser) and [mxsUpdateUser](nosql-protocol-database-commands.md#mxsupdateuser). Authorization should not be enabled before users have been created with [createUser](nosql-protocol-database-commands.md#createuser) or added with [mxsAddUser](nosql-protocol-database-commands.md#mxsadduser) with authorization being disabled.

NOTE: All client activity is _always_ subject to authorization performed by the MariaDB server.

## `auto_create_databases`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `true`
* Description: Controls whether databases are automatically created when required.

Specifies whether databases should automatically be created, as needed.

Note that setting this parameter to `true`, without also setting`auto_create_tables` to `true`, has no effect at all.

## `auto_create_tables`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `true`
* Description: Controls whether tables are automatically created within existing databases when required.

Specifies whether tables should automatically be created, as needed.

Note that this applies only if the relevant database already exists. If a database should also be created if needed, then `auto_create_databases` must also be set to `true`.

## `cursor_timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#durations)
* Mandatory: No
* Default: `60s`
* Description: Sets the maximum idle time before an inactive cursor is automatically closed.

Specifies how long a cursor can be idle, that is, not accessed, before it is automatically closed.

## `debug`

* Type: [enum\_mask](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`
* Description: Manages which protocol events are logged, including incoming commands, backend SQL, and client responses.

Specifies what should be logged as _notice_ messages.

Enumeration values:

* `none`: Nothing is logged.
* `in`: The incoming protocol command is logged.
* `out`: The outgoing SQL sent to the backend is logged.
* `back`: The response sent back to the client is logged.

So, specify

```
nosqlprotocol.debug=in,out,back
```

to have the incoming command, the corresponding SQL sent to the backend and the resulting response sent to the client logged.

## `host`

* Type: string
* Mandatory: No
* Default: `"%"`
* Description: Specifies the host portion of the MariaDB user account created via the NoSQL protocol.

Specifies the _host_ to be used when a MariaDB user is created via nosqlprotocol. By default all users are created as `...@'%'`, which means that it is possible to connect to the MariaDB server from any host using the credentials of the created user. For tighter security, the IP-address of the MaxScale host can be specified.

NOTE: This value does **not** specify from which host it is allowed to connect to MaxScale.

## `id_length`

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`
* Description: Sets the length of the `id` column for automatically created tables.

Specifies the length of the id column in tables that are automatically created.

## `internal_cache`

* Type: string
* Mandatory: No
* Default: ''
* Description: Specifies the internal cache to use. Only the `cache` filter is supported. 

Specifies what internal cache to use if any. The only permissible value is `cache`, which refers to the [cache filter](../../maxscale-filters/maxscale-cache/README.md).

Please see [caching](README.md#caching) for more information.

## `log_unknown_command`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#booleans)
* Mandatory: No
* Default: `false`
* Description: Determines whether unsupported or unknown client commands are logged for debugging.

Specifies whether an unknown command should be logged. This is primarily for debugging purposes, to find out whether a client uses a command that is not supported.

## `on_unknown_command`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`
* Description: Defines how the system responds to unrecognized client commands, either with an error or an empty result.

Specifies what should happen in case a clients sends an unrecognized command.

Enumeration values:

* `return_error`: An error document is returned.
* `return_empty`: An empty document is returned.

## `ordered_insert_behavior`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`
* Description: Controls whether multi-document inserts are performed completely or individually based on the `ordered` setting. 

Enumeration values:

* `default`: Each document is inserted using a separate `INSERT`, either in a multi-statement or in a compound statement. Whether an error causes the remaining insertions to be aborted, depends on the value of `ordered` specified in the insert command.
* `atomic`: If the value of `ordered` in the insert command is `true` (the default) then all documents are inserted using a single `INSERT` statement, that is, either all insertions succeed or none will. If `ordered` is false, then the behavior is as in the `default` case.

What combination of `ordered_insert_behavior` and `ordered` (in the insert command document) is used, has an impact on the performance. Please see the discussion at [insert](nosql-protocol-database-commands.md#insert).

## `password`

* Type: string
* Mandatory: No
* Default: `""`
* Description: Specifies the password used for backend connections when the MongoDB client is unauthenticated.

Specifies the _password_ to be used when connecting to the backend, is the MongoDB® client is not authenticated. Note that the same _user_/_password_ combination will be used for all unauthenticated MongoDB® clients connecting to the same listener port.

## `transactions`

* Type:
  [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#enumerations)
* Mandatory: No
* Values: `error`, `ignore`
* Default: `error`
* Description: Controls whether the transaction related commands result in
  an error or are silently ignored.

_Nosqlprotocol_ does not support transactions. The setting specifies what
happens when a client attempts to use them.

Enumeration values:

* `error`: An error is returned when a transaction is started, committed or
  aborted.
* `ignore`: Starting a transaction is ignored and the commands that
  otherwise would be executed within the transaction are executed
  immediately and independently. The `commitTransaction` and
  `abortTransaction` commands return success, but note that an aborted
  transaction does _not_ roll back anything.

The default is `error`, as `ignore` may cause the application to believe
that its changes are atomic when they are not. Please see [transaction
support](README.md#transaction-support) for more
information.

The value can be changed for the current session with
[mxsSetConfig](nosql-protocol-database-commands.md#mxssetconfig).

## `user`

* Type: string
* Mandatory: No
* Default: `""`
* Description: Specifies the username used for backend connections when the MongoDB client is unauthenticated.

Specifies the _user_ to be used when connecting to the backend, if the MongoDB® client is not authenticated.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
