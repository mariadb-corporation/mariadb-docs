# MaxScale PARSEC Aututhenticator

## PARSEC Authenticator

The [PARSEC](https://mariadb.com/docs/server/reference/plugins/authentication-plugins/authentication-plugin-parsec)
(Password Authentication using Response Signed with Elliptic Curve) authentication
plugin uses salted passwords, key derivation, extensible password storage format,
and both server-side and client-side scrambles.

Similarly to the ed25519 authentication plugin, it signs the response with a
ed25519 digital signature, but unlike the ed25519 authentication plugin, it uses
the stock unmodified ed25519 as provided by OpenSSL.

This authentication plugin is intended to be used with MariaDB version 12 or
later and requires that the service user has the `SET USER` grant.

MariaDB versions 11.6 or later that include the PARSEC authentication plugin are
supported but the passwords for the users must be provided via the [user mapping
file](../Getting-Started/Configuration-Guide.md#user_mapping_file). The
documentation for the [Ed25519
authenticator](Ed25519-Authenticator.md#using-a-mapping-file) contains an
example of how to configure the user mapping.

### Configuration

To enable PARSEC authentication on a listener, the `authenticator` list must
include `parsecauth`.

```
[Listener]
type=listener
address=127.0.0.1
port=3306
service=Service
authenticator=mariadbauth,parsecauth
```

To only allow PARSEC authentication, use `authenticator=parsecauth`.

{% @marketo/form formId="4316" %}
