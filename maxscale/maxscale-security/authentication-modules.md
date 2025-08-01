# Authentication Modules

## Authentication Modules

This document describes general MySQL protocol authentication in MaxScale. For\
REST-api authentication, see the [configuration guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md) and the [REST-api guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-rest-api/mariadb-maxscale-2501-maxscale-2501-rest-api.md).

Similar to the MariaDB Server, MaxScale uses authentication plugins to implement\
different authentication schemes for incoming clients. The same plugins also\
handle authenticating the clients to backend servers. The authentication plugins\
available in MaxScale are [standard MySQL password](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md),[GSSAPI](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md) and [pluggable authentication modules (PAM)](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md).

Most of the authentication processing is performed on the protocol level, before\
handing it over to one of the plugins. This shared part is described in this\
document. For information on an individual plugin, see its documentation.

### User account management

Every MaxScale service with a MariaDB protocol listener requires knowledge of\
the user accounts defined on the backend databases. The service maintains this\
information in an internal component called the _user account manager_ (UAM).\
The UAM queries relevant data from the _mysql_-database of the backends and\
stores it. Typically, only the current primary server is queried, as all servers\
are assumed to have the same users. The service settings _user_ and _password_\
define the credentials used when fetching user accounts.

The service uses the stored data when authenticating clients, checking their\
passwords and database access rights. This results in an authentication process\
very similar to the MariaDB Server itself. Unauthorized users are generally\
detected already at the MaxScale level instead of the backend servers. This may\
not apply in some cases, for example if MaxScale is using old user account data.

If authentication fails, the UAM updates its data from a backend. MaxScale may\
attempt authenticating the client again with the refreshed data without\
communicating the first failure to the client. This transparent user data update\
does not always work, in which case the client should try to log in again.

As the UAM is shared between all listeners of a service, its settings are\
defined in the service configuration. For more information, search the [configuration guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)\
for _users\_refresh\_time_, _users\_refresh\_interval_ an&#x64;_&#x61;uth\_all\_servers_. Other settings which affect how the UAM connects to backends are the global settings _auth\_connect\_timeout_ and _local\_address_, and the various server-level ssl-settings.

#### Required grants

To properly fetch user account information, the MaxScale service user must be\
able to read from various tables in the _mysql_-database: _user_, _db_,_tables\_priv_, _columns\_priv_, _procs\_priv_, _proxies\_priv_ and _roles\_mapping_.\
The user should also have the _SHOW DATABASES_-grant.

```sql
CREATE USER 'maxscale'@'maxscalehost' IDENTIFIED BY 'maxscale-password';
GRANT SELECT ON mysql.user TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.db TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.tables_priv TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.columns_priv TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.procs_priv TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.proxies_priv TO 'maxscale'@'maxscalehost';
GRANT SELECT ON mysql.roles_mapping TO 'maxscale'@'maxscalehost';
GRANT SHOW DATABASES ON *.* TO 'maxscale'@'maxscalehost';
```

If using MariaDB ColumnStore, the following grant is required:

```sql
GRANT ALL ON infinidb_vtable.* TO 'maxscale'@'maxscalehost';
```

### Limitations and troubleshooting

When a client logs in to MaxScale, MaxScale sees the client's IP address. When\
MaxScale then connects the client to backends (using the client's username and\
password), the backends see the connection coming from the IP address of\
MaxScale. If the client user account is to a wildcard host (`'alice'@'%'`), this\
is not an issue. If the host is restricted (`'alice'@'123.123.123.123'`),\
authentication to backends will fail.

There are two primary ways to deal with this:

1. Duplicate user accounts. For every user account with a restricted hostname an\
   equivalent user account for MaxScale is added (`'alice'@'maxscale-ip'`).
2. Use [proxy protocol](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

Option 1 limits the passwords for user accounts with shared usernames. Such\
accounts must use the same password since they will effectively share the\
MaxScale-to-backend user account. Option 2 requires server support.

See [MaxScale Troubleshooting](../maxscale-management/maxscale-troubleshooting.md)\
for additional information on how to solve authentication issues.

#### Wildcard database grants

MaxScale supports wildcards `_` and `%` for database-level grants. As with\
MariaDB Server, `grant select on test_.* to 'alice'@'%';` gives access t&#x6F;_&#x74;est\__ as well as _test1_, _test2_ and so on. If the GRANT command escapes the\
wildcard (`grant select on` test\_`.* to 'alice'@'%';`) both MaxScale and the\
MariaDB Server interpret it as only allowing access to _test\__. `_` and `%`\
are only interpreted as wildcards when the grant is to a database:`grant select on` test\_`.t1 to 'alice'@'%';` only grants access to th&#x65;_&#x74;est\_.t1_-table, not to _test1.t1_.

### Settings

The listener configuration defines authentication options which only affect the\
listener. _authenticator_ defines the authentication plugins to use._authenticator\_options_ sets various options. These options may affect an\
individual authentication plugin or the authentication as a whole. The latter\
are explained below. Multiple options can be given as a comma-separated list.

```
authenticator_options=skip_authentication=true,lower_case_table_names=1
```

#### `skip_authentication`

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

If enabled, MaxScale will not check the\
passwords of incoming clients and just assumes that they are correct.\
Wrong passwords are instead detected when MaxScale tries to authenticate to the\
backend servers.

This setting is mainly meant for failure tolerance in situations where the\
password check is performed outside of MaxScale. If, for example, MaxScale\
cannot use an LDAP-server but the backend databases can, enabling this setting\
allows clients to log in. Even with this setting enabled, a user account\
matching the incoming client username and IP must exist on the backends for\
MaxScale to accept the client.

This setting is incompatible with standard MariaDB/MySQL authentication plugin\
(_MariaDBAuth_ in MaxScale). If enabled, MaxScale cannot authenticate clients to\
backend servers using standard authentication.

```
authenticator_options=skip_authentication=true
```

#### `match_host`

* Type: [boolean](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

If disabled, MaxScale does not require that a\
valid user account entry for incoming clients exists on the backends.\
Specifically, only the client username needs to match a user account,\
hostname/IP is ignored.

This setting may be used to force clients to connect through MaxScale. Normally,\
creating the user _jdoe@%_ will allow the user _jdoe_ to connect from any\
IP-address. By disabling _match\_host_ and replacing the user wit&#x68;_&#x6A;doe@maxscale-IP_, the user can still connect from any client IP but will be\
forced to go through MaxScale.

```
authenticator_options=match_host=false
```

#### `lower_case_table_names`

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `0`

Controls database name matching for authentication\
when an incoming client logs in to a non-empty database. The setting functions\
similar to the MariaDB Server setting [lower\_case\_table\_names](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables)\
and should be set to the value used by the backends.

The setting accepts the values 0, 1 or 2:

* `0`: case-sensitive matching (default)
* `1`: convert the requested database name to lower case before using case-insensitive\
  matching. Assumes that database names on the server are stored in lower case.
* `2`: use case-insensitive matching.

_true_ and _false_ are also accepted for backwards compatibility. These map to 1\
and 0, respectively.

The identifier names are converted using an ASCII-only function. This means that\
non-ASCII characters will retain their case-sensitivity.

Starting with MaxScale versions 2.5.25, 6.4.6, 22.08.5 and 23.02.2, the behavior\
of `lower_case_table_names=1` is identical with how the MariaDB server\
behaves. In older releases the comparisons were done in a case-sensitive manner\
after the requested database name was converted into lowercase. Using`lower_case_table_names=2` will behave identically in all versions which makes\
it a safe alternative to use when a mix of older and newer MaxScale versions is\
being used.

```
authenticator_options=lower_case_table_names=0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
