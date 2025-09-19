# MaxScale GSSAPI Client Authenticator

## Overview

GSSAPI is an authentication protocol that is commonly implemented with Kerberos on Unix
or Active Directory on Windows. This document describes GSSAPI authentication in MaxScale. 
The authentication module name in MaxScale _SSAPIAuth_.

## Preparing the GSSAPI system

For Unix systems, the usual GSSAPI implementation is Kerberos. 
This is a short guide on how to set up Kerberos for MaxScale.

The first step is to configure MariaDB to use GSSAPI authentication. 
The MariaDB documentation for the [GSSAPI Authentication Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) 
is a good example on how to set it up.

The next step is to copy the keytab file from the server where MariaDB is installed 
to the server where MaxScale is located. The keytab file must be placed in the configured
default location which almost always is `/etc/krb5.keytab`. 
Alternatively, the keytab filepath can be given as an authenticator option.

The location of the keytab file can be changed with the `KRB5_KTNAME` environment variable: [keytab\_def.html](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html)

To take GSSAPI authentication into use, add the following to the listener.

```ini
authenticator=GSSAPIAuth
authenticator_options=principal_name=mariadb/localhost.localdomain@EXAMPLE.COM
```

The principal name should be the same as on the MariaDB servers.

## Settings

#### `principal_name`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`

The service principal name to send to the client. 
This parameter is a string parameter which is used by the client to request the token.

This parameter _must_ be the same as the principal name that the backend MariaDB server uses.

#### `gssapi_keytab_path`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

Keytab file location. This should be an absolute path to the file containing the keytab.
If not defined, Kerberos will search from a default location, usually `/etc/krb5.keytab`. 
This path is set to an environment variable. This means that multiple listeners with GSSAPIAuth overrides each other. 
If using multiple GSSAPI authenticators, either do not set this option or use the same value for all listeners.

```ini
authenticator_options=principal_name=mymariadb@EXAMPLE.COM,gssapi_keytab_path=/home/user/mymariadb.keytab
```

## Implementation Details

Read the [Authentication Modules](../../maxscale-security/authentication-modules.md) document 
for more details on how authentication modules work in MaxScale.

### GSSAPI authentication

The GSSAPI plugin authentication starts when the database server sends the service principal name 
in the `AuthSwitchRequest` packet. The principal name will usually be in the form `service@REALM.COM`.

The client searches its local cache for a token for the service or may request it from the GSSAPI server. 
If found, the client sends the token to the database server. The database server verifies the authenticity
of the token using its keytab file and sends the final OK packet to the client.

### Building the module

The GSSAPI authenticator modules require the GSSAPI development libraries (`krb5-devel` on CentOS 7).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
