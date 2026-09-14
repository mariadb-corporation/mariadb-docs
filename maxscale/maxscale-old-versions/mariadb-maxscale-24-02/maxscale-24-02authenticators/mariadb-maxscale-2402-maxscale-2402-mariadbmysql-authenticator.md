# MaxScale 24.02 MariaDB/MySQL Authenticator

The _MariaDBAuth_-module implements the client and backend authentication for the
server plugin _mysql\_native\_password_. This is the default authentication
plugin used by both MariaDB and MySQL.

### Authenticator options

The following settings may be given in the _authenticator\_options_ of the
listener.

#### `clear_pw_passthrough`

Boolean, default value is "false". Activates passthrough-mode. In this mode,\
MaxScale does not check client credentials at all and defers authentication to
the backend server. This feature is primarily meant to be used with Xpand LDAP-
authentication, although it may be useful in any situation where MaxScale
cannot check the existence of client user account nor authenticate the client.

When a client connects to a listener with this setting enabled, MaxScale will
change authentication method to "mysql\_clear\_password", causing the client to
send their cleartext password to MaxScale. MaxScale will then attempt to use
the password to authenticate to backends. The authentication result of the
first backend to respond will be sent to the client. The backend may ask\
MaxScale for either cleartext password or standard ("mysql\_native\_password")
authentication token. MaxScale can work with both backend plugins since it has
the original password.

This feature is incompatible with service setting _lazy\_connect_. Either leave
it unspecified or set `lazy_connect=false` in the linked service. Also,
multiple client authenticators are not allowed on the listener when
passthrough-mode is on.

Because passwords are sent in cleartext, the listener should be configured for
ssl.

```
[MyListener]
type=listener
authenticator=mariadbauth
authenticator_options=clear_pw_passthrough=true
ssl=true
<other options>
```

#### `log_password_mismatch`

* Type: [boolean](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

The service setting _log\_auth\_warnings_ must
also be enabled for this setting to have effect. When both settings are enabled,
password hashes are logged if a client gives a wrong password. This feature may
be useful when diagnosing authentication issues. It should only be enabled on a
secure system as the logging of password hashes may be a security risk.

#### `cache_dir`

Deprecated and ignored.

#### `inject_service_user`

Deprecated and ignored.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
