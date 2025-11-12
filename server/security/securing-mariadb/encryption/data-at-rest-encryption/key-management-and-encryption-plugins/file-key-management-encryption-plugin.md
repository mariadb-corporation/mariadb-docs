# File Key Management Encryption Plugin

MariaDB's [data-at-rest encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) requires the use of a [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.

MariaDB supports the use of [multiple encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#key-rotation), then encryption keys can also be rotated, which creates a new version of the encryption key.

The File Key Management plugin that ships with MariaDB is a [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) that reads encryption keys from a plain-text file.

## Overview

The File Key Management plugin is the [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) for users who want to use [data-at-rest encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md). Some of the plugin's primary features are:

* It reads encryption keys from a plain-text key file.
* As an extra protection mechanism, the plain-text key file can be encrypted.
* It supports multiple encryption keys.
* It supports key rotation with MariaDB Enterprise Server from MariaDB Enterprise Server 11.8.
* It supports two different algorithms for encrypting data.

It can also serve as an example and as a starting point when developing a key management and encryption plugin with the [encryption plugin API](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/encryption-plugin-api).

## Installing the File Key Management Plugin's Package

The File Key Management plugin is included in MariaDB packages as the `file_key_management.so` or `file_key_management.dll` shared library. The shared library is in the main server package, so no additional package installations are necessary. The plug-in must be installed into MariaDB however as follows.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. The plugin can be installed by providing the\
[--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../../../../../server-management/starting-and-stopping-mariadb/mariadbd.md) or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```ini
[mariadb]
...
plugin_load_add = file_key_management
```

## Uninstalling the Plugin

Before you uninstall the plugin, you should ensure that [data-at-rest encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) is completely disabled, and that MariaDB no longer needs the plugin to decrypt tables or other files.

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'file_key_management';
```

If you installed the plugin by providing the [--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#plugin-load-add) options in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Creating the Key File

In order to encrypt your tables with encryption keys using the File Key Management plugin, create the file containing the encryption keys. File name and location don't matter; see in the following what configuration is needed.

For each encryption key, the file contains these options, separated by a semicolon:

* The key identifier (format: 32-bit integer)
* The key version (optional, and only available as of Enterprise Server 11.8)
* The key itself (format: hex-encoded)

Entries look like this:

{% tabs %}
{% tab title="Current Enterprise Server" %}
```
<encryption_key_id>;<encryption_key_version>;<hex-encoded_encryption_key>
```
{% endtab %}

{% tab title="Community Server & Enterprise Server < 11.8" %}
```ini
<encryption_key_id>;<hex-encoded_encryption_key>
```
{% endtab %}
{% endtabs %}

You can also optionally encrypt the key file to make it less accessible from the file system. That is explained further in the section below.

The File Key Management plugin uses [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) to encrypt data. It supports 128-bit, 192-bit, and 256-bit encryption keys, just like the plugin does.

Generate random encryption keys using the [openssl rand](https://www.openssl.org/docs/man1.1.1/man1/rand.html) command. To create a random 256-bit (32-byte) encryption key, run the following command:

```sql
$ openssl rand -hex 32
a7addd9adea9978fda19f21e6be987880e68ac92632ca052e5bb42b1a506939a
```

The key file needs to have a key identifier for each encryption key added to the beginning of each line. Key identifiers do not have to be contiguous. For example, to append three new encryption keys to a new key file, issue this command:

```bash
mkdir -p /etc/mysql/encryption
echo $(echo -n "1;" ; openssl rand -hex 32) | sudo tee -a  /etc/mysql/encryption/keyfile
echo $(echo -n "2;" ; openssl rand -hex 32) | sudo tee -a  /etc/mysql/encryption/keyfile
echo $(echo -n "100;" ; openssl rand -hex 32) | sudo tee -a  /etc/mysql/encryption/keyfile
```

The resulting key file looks like this:

{% tabs %}
{% tab title="Current Enterprise Server" %}
```
1;1;a7addd9adea9978fda19f21e6be987880e68ac92632ca052e5bb42b1a506939a
2;1;49c16acc2dffe616710c9ba9a10b94944a737de1beccb52dc1560abfdd67388b
100;2;8db1ee74580e7e93ab8cf157f02656d356c2f437d548d5bf16bf2a56932954a3
```
{% endtab %}

{% tab title="Community Server & Enterprise Server < 11.8" %}
```sql
1;a7addd9adea9978fda19f21e6be987880e68ac92632ca052e5bb42b1a506939a
2;49c16acc2dffe616710c9ba9a10b94944a737de1beccb52dc1560abfdd67388b
100;8db1ee74580e7e93ab8cf157f02656d356c2f437d548d5bf16bf2a56932954a3
```
{% endtab %}
{% endtabs %}

The key identifiers give you a way to reference the encryption keys from MariaDB. In the example above, you could reference these encryption keys using the key identifiers `1`, `2` or `100` with the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option or with system variables such as [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id). You do not necessarily need multiple encryption keys; an encryption key with the key identifier `1` is the only mandatory one.

If the key file is left unencrypted, the File Key Management plugin only requires the [file\_key\_management\_filename](file-key-management-encryption-plugin.md#file_key_management_filename) system variable to be configured.

This system variable can be specified as a command-line argument to `mariadbd` , or it can be specified in a server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) of an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), like this:

```ini
[mariadb]
...
loose_file_key_management_filename = /etc/mysql/encryption/keyfile
```

{% include "../../../../../.gitbook/includes/to-avoid-startup-failures-....md" %}

## Encrypting the Key File

{% hint style="info" %}
This step is optional, but highly recommended.
{% endhint %}

If you use an unencrypted key file, keys are stored in plain text on your system, posing a security risk. It's recommended to encrypt the key file, with these hints in mind:

* MariaDB only supports the [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
* The encryption key size can be 128-bits, 192-bits, or 256-bits.
* The encryption key is created from the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the encryption password.
* The encryption password has a maximum length of 256 characters.

Generate a random encryption password using the [openssl rand](https://www.openssl.org/docs/man1.1.1/man1/rand.html) command. To create a random 256 character encryption password, execute the following:

```bash
$ sudo openssl rand -hex 128 > /etc/mysql/encryption/keyfile.key
```

Encrypt the key file using the [openssl enc](https://www.openssl.org/docs/man1.1.1/man1/enc.html) command. To encrypt the key file with the encryption password created in the previous step, execute the following:

```bash
$ sudo openssl enc -aes-256-cbc -md sha1 \
   -pass file:/etc/mysql/encryption/keyfile.key \
   -in /etc/mysql/encryption/keyfile \
   -out /etc/mysql/encryption/keyfile.enc
```

The resulting `keyfile.enc` file is the encrypted version of `keyfile`. Delete the unencrypted key file.

{% hint style="info" %}
Some more recent `openssl` versions may throw this warning:

```bash
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
```
{% endhint %}

Having the key file encrypted requires both the [file\_key\_management\_filename](file-key-management-encryption-plugin.md#file_key_management_filename) and the [file\_key\_management\_filekey](file-key-management-encryption-plugin.md#file_key_management_filekey) system variables to be configured.

The `file_key_management_filekey` variable can be provided in two forms:

* As a plain-text encryption password. This is not recommended, since the plain-text encryption password would be visible in the output of the [SHOW VARIABLES](../../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement.
* Prefixed with `FILE:`, it can be a path to a file that contains the plain-text encryption password.

These variables can be specified as command-line arguments to `mariadbd`, or they can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
loose_file_key_management_filename = /etc/mysql/encryption/keyfile.enc
loose_file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
```

{% include "../../../../../.gitbook/includes/to-avoid-startup-failures-....md" %}

## Choosing an Encryption Algorithm

The File Key Management plugin currently supports two encryption algorithms for encrypting data: `AES_CBC` and `AES_CTR`. Both of these algorithms use [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in different modes. AES uses 128-bit blocks, and supports 128-bit, 192-bit, and 256-bit keys. The modes are:

* The `AES_CBC` mode uses AES in the [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29) mode.
* The `AES_CTR` mode uses AES in two slightly different modes in different contexts. When encrypting tablespace pages (such as pages in InnoDB, XtraDB, and Aria tables), it uses AES in the [Counter (CTR)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29) mode. When encrypting temporary files (where the cipher text is allowed to be larger than the plain text), it uses AES in the authenticated [Galois/Counter Mode (GCM)](https://en.wikipedia.org/wiki/Galois/Counter_Mode).

The recommended algorithm is `AES_CTR`, but this algorithm is only available when MariaDB is built with [OpenSSL](https://www.openssl.org/). If the server is built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) then this algorithm is not available. See [TLS and Cryptography Libraries Used by MariaDB](../../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

### Configuring the Encryption Algorithm

The encryption algorithm can be configured by setting the [file\_key\_management\_encryption\_algorithm](file-key-management-encryption-plugin.md#file_key_management_encryption_algorithm) system variable.

This system variable can be set to one of the following values:

<table><thead><tr><th width="207">System Variable Value</th><th>Description</th></tr></thead><tbody><tr><td>AES_CBC</td><td>Data is encrypted using AES in the <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29">Cipher Block Chaining (CBC)</a> mode. This is the default value.</td></tr><tr><td>AES_CTR</td><td>Data is encrypted using AES either in the <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29">Counter (CTR)</a> mode or in the authenticated <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">Galois/Counter Mode (GCM)</a> mode, depending on context. This is only supported in some builds. See the previous section for more information.</td></tr></tbody></table>

This system variable can be specified as command-line arguments to [mysqld](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```sql
[mariadb]
...
loose_file_key_management_encryption_algorithm = AES_CTR
```

Note that the [loose](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option prefix is specified. This option prefix is used in case the plugin hasn't been installed yet.

Note that this variable does not affect the algorithm that MariaDB uses to decrypt the key file. This variable only affects the encryption algorithm that MariaDB uses to encrypt and decrypt data. The only algorithm that MariaDB currently supports to encrypt the key file is [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

## Using the File Key Management Plugin

Once the File Key Management Plugin is enabled, you can use it by creating an encrypted table:

```sql
CREATE TABLE t (i INT) ENGINE=InnoDB ENCRYPTED=YES
```

Now, table `t` will be encrypted using the encryption key from the key file. For more information on how to use encryption, see [Data at Rest Encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).

## Using Multiple Encryption Keys

The File Key Management Plugin supports [using multiple encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key can be defined with a different 32-bit integer as a key identifier.

When [encrypting InnoDB tables](../innodb-encryption/), the key that is used to encrypt tables [can be changed](../innodb-encryption/innodb-encryption-keys.md). When [encrypting Aria tables](../aria-encryption/), the key that is used to encrypt tables [cannot currently be changed](../aria-encryption/aria-encryption-keys.md).

## Key Rotation

{% tabs %}
{% tab title="Current Enterprise Server" %}
The plugin supports key rotation and allows an optional key version in the key file. The keys can be rotated using the `FLUSH FILE_KEY_MANAGEMENT_KEYS` statement, without needing to restart the server. The plugin remains compatible with old key file format, and when version is not specified, it defaults to version 1.

**Generation of New Key Versions**

How would new key versions be generated?

The plugin doesn't generate any encryption keys itself, and it doesn't have a backend KMS[^1] to generate encryption keys for it either.

Any encryption keys need to be generated by the user with external tools, such as OpenSSL. For example:

```bash
-- Generate a new 256-bit key
openssl rand -hex 32
```

Keys need to be manually saved to the key file. See [this section](file-key-management-encryption-plugin.md#creating-the-key-file).

The format of the key file is simplistic. It stores encryption keys in a plain-text file.
{% endtab %}

{% tab title="< 11.8" %}
The File Key Management plugin does not support [key rotation](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#key-rotation).
{% endtab %}
{% endtabs %}

## Versions

<table><thead><tr><th width="108">Version</th><th width="151">Status</th><th>Introduced</th></tr></thead><tbody><tr><td>1.0</td><td>Stable</td><td>From MariaDB 10.1.18</td></tr></tbody></table>

## System Variables

### `file_key_management_encryption_algorithm`

* This system variable is used to determine which algorithm the plugin will use to encrypt data.
  * The recommended algorithm is `AES_CTR`, but this algorithm is only available when MariaDB is built with [OpenSSL](https://www.openssl.org/). If the server is built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) then this algorithm is not available. See [TLS and Cryptography Libraries Used by MariaDB](../../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Command line: `--file-key-management-encryption-algorithm=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `AES_CBC`
* Valid Values: `AES_CBC`, `AES_CTR`

### `file_key_management_digest`

* Specifies the digest function to use in key derivation of the key used for decrypting the key file.
* Command line: --file-key-management-digest=_value_
* Scope: Global
* Dynamic: No
* Data type: enumerated
* Default value: sha1
* Valid values: sha1, sha224, sha256, sha384, sha512
* Available from MariaDB 12.0

### `file_key_management_filekey`

* Used to determine the encryption password that is used to decrypt the key file defined by [file\_key\_management\_filename](file-key-management-encryption-plugin.md#file_key_management_filename).
  * If this system variable's value is prefixed with `FILE:`, then it is interpreted as a path to a file that contains the plain-text encryption password.
  * If this system variable's value is not prefixed with `FILE:`, then it is interpreted as the plain-text encryption password. However, this is not recommended.
  * The encryption password has a max length of 256 characters.
  * The only algorithm that MariaDB currently supports when decrypting the key file is [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard). The encryption key size can be 128-bits, 192-bits, or 256-bits. The encryption key is calculated by taking a [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the encryption password.
* Command line: `--file-key-management-filekey=value`
* Scope: Global
* Dynamic: No
* Data type: `string`
* Default value: (empty)

### `file_key_management_filename`

* Used to determine the path to the file that contains the encryption keys. If [file\_key\_management\_filekey](file-key-management-encryption-plugin.md#file_key_management_filekey) is set, this file can be encrypted with [Cipher Block Chaining (CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CBC) mode of [Advanced Encryption Standard (AES)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
* Command line: `--file-key-management-filename=`_`value`_
* Scope: Global
* Dynamic: No
* Data type: `string`
* Default value: (empty)

### `file_key_management_use_pbkdf2`

* Specifies whether pbkdf2 is used in key derivation, and if so, how many iterations.
* Command line: `--file-key-management-use-pbkdf2=`_`number`_
* Scope: Global
* Dynamic: No
* Data type: `numeric`
* Default value: 0
* Valid values: integers ≥ 0 (reasonable value: 600000 for sha256, less for sha512)
* Available from MariaDB 12.0

## Options

### `file_key_management`

* Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--file-key-management=value`
* Data type: `enumerated`
* Default value: `ON`
* Valid values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: Key Management Service
