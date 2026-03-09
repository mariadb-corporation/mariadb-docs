# Authentication Plugin - caching\_sha2\_password

{% hint style="info" %}
This plugin is available from MariaDB Server 11.4.
{% endhint %}

## Overview

To aid migrations MariaDB provides MySQL compatible `caching_sha2_password` authentication plugin. It allows to move users from MySQL to MariaDB without requiring them to change their passwords. It should be only used for migration, otherwise a more secure and convenient PARSEC plugin is recommended.

## Installing the Plugin

The `caching_sha2_password` authentication plugin's shared library is included in MariaDB packages as the `auth_mysql_sha2.so` or `auth_mysql_sha2.dll` shared library on systems where it can be built.

Although the plugin's shared library is distributed with MariaDB, the plugin is not actually installed into MariaDB by default. There are two methods that can be used to install the plugin into MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md):

```sql
INSTALL SONAME 'auth_mysql_sha2';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = auth_mysql_sha2
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md):

```sql
UNINSTALL SONAME 'auth_mysql_sha2';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options must be removed to prevent the plugin from being loaded the next time the server is restarted.

## Using the Plugin

To create a user in MariaDB that was using `caching_sha2_password` plugin in MySQL, issue this statement:

```sql
CREATE USER user@host IDENTIFIED WITH caching_sha2_password USING 'authentication_string';
```

Here, `authentication_string` is taken from the `mysql.user` table for the corresponding user in MySQL installation. Beware that the authentication string for `caching_sha2_password` in MySQL can contain non-printable characters and copying it from the terminal window will likely not work.

## System Variables

### `caching_sha2_password_private_key_path`

* Description: A path to the private RSA key used for authentication.
* Command line: `--caching-sha2-password-private-key-path`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `private_key.pem`
* Introduced: MariaDB 11.4.9, MariaDB 11.8.4

### `caching_sha2_password_public_key_path`

* Description: A path to the public RSA key used for authentication.
* Command line: `--caching-sha2-password-public-key-path`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `public_key.pem`
* Introduced: MariaDB 11.4.9, MariaDB 11.8.4

### `caching_sha2_password_auto_generate_rsa_keys`

* Description: Auto generate RSA keys at server startup if key paths are not explicitly set and key files are not present at their default locations.
* Command line: `--caching-sha2-password-auto-generate-rsa-keys`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: MariaDB 11.4.9, MariaDB 11.8.4

### `caching_sha2_password_digest_rounds`

* Description: Number of SHA2 rounds to be performed when computing a password hash.
* Command line: `--caching-sha2-password-digest-rounds`
* Scope: Global
* Dynamic: No
* Data Type: `integer`
* Default Value: `5000`
* Introduced: MariaDB 11.4.9, MariaDB 11.8.4
