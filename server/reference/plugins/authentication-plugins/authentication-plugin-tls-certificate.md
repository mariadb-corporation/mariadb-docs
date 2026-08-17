---
description: >-
  The tls_certificate authentication plugin authenticates an account from its
  TLS client certificate alone, with no password, by requiring the certificate
  subject to match the account's REQUIRE SUBJECT clause.
---

# Authentication Plugin - tls\_certificate

{% hint style="info" %}
This plugin is available from MariaDB Enterprise Server 12.3. It is not included in MariaDB Community Server.
{% endhint %}

The `tls_certificate` authentication plugin authenticates a user from the TLS client certificate presented during the connection handshake. No password is involved at any point: the account holds no password, none is sent, and none is checked.

The account is identified by the certificate's subject Distinguished Name (DN), which must be pinned on the account with a [`REQUIRE SUBJECT`](../../sql-statements/account-management-sql-statements/create-user.md) clause. The plugin refuses to authenticate an account that was not created with `REQUIRE SUBJECT`.

Because the account has no password, [password validation plugins](../password-validation-plugins/simple-password-check-plugin.md) such as `simple_password_check` do not apply to it, and an account can be created while such a plugin is active.

### Description

`REQUIRE SUBJECT` alone is what makes this authentication rather than merely encryption. `REQUIRE SSL` guarantees only that the transport is encrypted, and `REQUIRE X509` only that the client presented some certificate signed by a trusted CA — neither identifies *which* client connected. Pinning the subject ties the account to one specific certificate identity.

`REQUIRE SUBJECT` implies `REQUIRE X509`, so there is no need to specify `REQUIRE X509` separately.

The plugin itself does no certificate validation. Signature checking, expiry, and revocation (CRL/OCSP) are all handled by the server's TLS layer during the handshake, before the plugin runs. The plugin's only check is that the account carries a `REQUIRE SUBJECT` clause; enforcing that clause is likewise the server's job.

### Installing

The plugin is built into MariaDB Enterprise Server and enabled by default. There is no `INSTALL SONAME` step, and no separate package to install.

No client-side change is needed either. The plugin accepts any standard client authentication plugin, so existing clients and connectors connect without modification — they simply need to present the certificate.

### Example

Create an account whose subject DN matches the client certificate, and grant it as usual:

```sql
CREATE USER 'alice'@'%'
  IDENTIFIED VIA tls_certificate
  REQUIRE SUBJECT '/CN=alice/O=Example Ltd/C=FI';
```

`IDENTIFIED WITH` is accepted as a synonym for `IDENTIFIED VIA`.

The client connects with its key pair and no password:

```bash
mariadb --user=alice \
        --ssl-ca=/etc/ssl/ca.pem \
        --ssl-cert=/etc/ssl/alice-cert.pem \
        --ssl-key=/etc/ssl/alice-key.pem
```

If the certificate subject does not match, or the account has no `REQUIRE SUBJECT` clause, the connection fails with a standard access-denied error — the plugin defines no error code of its own:

```
ERROR 1698 (28000): Access denied for user 'alice'@'localhost'
```

## Matching the Certificate Subject

The subject comparison is a byte-for-byte string comparison. Two consequences follow, and both bite in practice:

* **Case matters.** `/CN=alice` and `/CN=Alice` are different subjects.
* **Field order matters.** `/CN=alice/O=Example Ltd` and `/O=Example Ltd/CN=alice` are different subjects.

Copy the DN exactly as the server renders it rather than retyping it. You can read the subject of a certificate with:

```bash
openssl x509 -noout -subject -in alice-cert.pem
```

{% hint style="warning" %}
`REQUIRE SUBJECT` matches the subject only — not the issuer. An account therefore accepts any certificate with a matching subject signed by **any** CA the server trusts. If `--ssl-ca` trusts more than one CA, add a [`REQUIRE ISSUER`](../../sql-statements/account-management-sql-statements/create-user.md) clause to pin the issuer as well.

On OpenSSL builds, leaving `--ssl-ca` unset makes the server trust the operating system CA store, which widens this considerably. Set [`--ssl-ca`](../../../security/encryption/data-in-transit-encryption/ssltls-system-variables.md) explicitly to the CA that issues your client certificates.
{% endhint %}

## Account Management Behavior

Because these accounts authenticate with no password, several password-related features do not apply:

* [`PASSWORD EXPIRE`](../../sql-statements/account-management-sql-statements/alter-user.md) and `password_lifetime` have no effect — the expiry check is skipped for a connection that used no password. Use `ACCOUNT LOCK`, which is enforced normally, to disable such an account.
* A `USING` or `AS` clause is accepted and stored, but the plugin never reads it, so it has no effect. `SET PASSWORD` on these accounts is rejected.

{% hint style="warning" %}
An account created with `IDENTIFIED VIA tls_certificate` but **without** `REQUIRE SUBJECT` is created successfully and cannot connect. The plugin API offers no hook at `CREATE USER` time for a passwordless plugin, so no warning can be raised. Add the clause with [`ALTER USER`](../../sql-statements/account-management-sql-statements/alter-user.md) and the account works.
{% endhint %}

When several authentication methods are combined with `OR`, the first one that succeeds wins. An account given both `tls_certificate` and a password method can therefore log in with the password alone if `REQUIRE SUBJECT` is absent. Requiring *both* a valid certificate and a password needs multi-factor authentication (several plugins combined with `AND`), which is not yet available.

## Known Limitations on WolfSSL Builds

{% hint style="warning" %}
Builds that use WolfSSL rather than OpenSSL — which includes the Windows packages — are affected by two open issues. Neither is fixed in MariaDB Enterprise Server 12.3:

* [MDEV-40382](https://jira.mariadb.org/browse/MDEV-40382) — `--ssl-crl` is not enforced, so a revoked client certificate still authenticates.
* [MDEV-40398](https://jira.mariadb.org/browse/MDEV-40398) — the certificate subject separator is not escaped, so two different subjects can satisfy one `REQUIRE SUBJECT` account.

Both are scheduled for the Q4/2026 server maintenance sprint. MDEV-40382 may be resolved after retesting; MDEV-40398 depends on a fix in WolfSSL itself and will not be worked around in MariaDB code, so it may persist beyond 12.3.

Official MariaDB Enterprise Server builds on OpenSSL are not affected.
{% endhint %}

## Options

The plugin adds no system variables and no status variables. The only option is the standard plugin activation option.

### `tls_certificate`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugin](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--tls-certificate=value`, or equivalently `--plugin-tls-certificate=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`
* Introduced: MariaDB Enterprise Server 12.3

{% hint style="info" %}
On the command line and in configuration files, MariaDB treats `-` and `_` in an option name as equivalent, so `--plugin-tls_certificate` works as well. Option names are always printed with hyphens, which is why `mariadbd --help --verbose` lists `--plugin-tls-certificate` even though the plugin is named `tls_certificate` in SQL.
{% endhint %}

## See Also

* [Pluggable Authentication Overview](pluggable-authentication-overview.md)
* [CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md)
* [ALTER USER](../../sql-statements/account-management-sql-statements/alter-user.md)
* [Securing Connections for Client and Server](../../../security/encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md)
* [SSL/TLS System Variables](../../../security/encryption/data-in-transit-encryption/ssltls-system-variables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
