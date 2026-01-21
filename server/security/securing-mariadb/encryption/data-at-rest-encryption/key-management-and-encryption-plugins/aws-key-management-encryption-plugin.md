---
description: >-
  Introduction to the AWS Key Management plugin, which uses Amazon KMS to
  generate and store master keys, decrypting them at startup to enable
  data-at-rest encryption with key rotation support.
---

# AWS Key Management Encryption Plugin

Due to license incompatibilities between the MariaDB server source code and the Amazon AWS C++ SDK, we can only distribute the plugin in source code form, and not as ready-to-use binaries. See [Installing the Plugin's Package](aws-key-management-encryption-plugin.md#installing-the-plugins-package) for details.

MariaDB's [data-at-rest encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) requires the use of a [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.

MariaDB supports the use of [multiple encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#key-rotation), then encryption keys can also be rotated, which creates a new version of the encryption key.

The AWS Key Management plugin is a [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) that uses the [Amazon Web Services (AWS) Key Management Service (KMS)](https://aws.amazon.com/kms/).

## Overview

The AWS Key Management plugin uses the [Amazon Web Services (AWS) Key Management Service (KMS)](https://aws.amazon.com/kms/) to generate and store AES keys on disk, in encrypted form, using the Customer Master Key (CMK) kept in AWS KMS. When MariaDB Server starts, the plugin will decrypt the encrypted keys, using the AWS KMS "Decrypt" API function. MariaDB data will then be encrypted and decrypted using the AES key. It supports multiple encryption keys. It supports key rotation.

## Tutorials

Tutorials related to the AWS Key Management plugin can be found at the following pages:

* [Amazon Web Services (AWS) Key Management Service (KMS) Encryption Plugin Setup Guide](aws-key-management-encryption-plugin-setup-guide.md)
* [Amazon Web Services (AWS) Key Management Service (KMS) Encryption Plugin Advanced Usage](aws-key-management-encryption-plugin-advanced-usage.md)

## Preparation

* Before you use the plugin, you need to create a Customer Master Key (CMK). Create a key using the AWS Console as described in the [AMS KMS developer guide](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).
* The easiest way to give the AWS key management plugin access to the key is to create an IAM Role with access to the key, and to apply that IAM Role to an EC2 instance where MariaDB Server runs.
* Make sure that MariaDB Server runs under the correct AWS identity that has access to the above key. For example, you can store the AWS credentials in an AWS credentials file for the user who runs `mysqld`. More information about the credentials file can be found in [the AWS CLI Getting Started Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-file).

## Installing the Plugin's Package

The AWS Key Management plugin depends on the [AWS SDK for C++](https://github.com/aws/aws-sdk-cpp), which uses the [Apache License, Version 2.0](https://github.com/aws/aws-sdk-cpp/blob/master/LICENSE). This license is not compatible with MariaDB Server's [GPL 2.0 license](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/licensing-questions/licensing-faq#licenses-used-by-mariadb), so we are not able to distribute packages that contain the AWS Key Management plugin. Therefore, the only way to currently obtain the plugin is to install it from source.

### Installing from Source

When [compiling MariaDB from source](../../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/), the AWS Key Management plugin is built by default, on systems that support it.

Compilation is controlled by the following [cmake](../../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) arguments:

* `-DPLUGIN_AWS_KEY_MANAGEMENT=DYNAMIC` to build a loadable plugin library
* `-DAWS_SDK_EXTERNAL_PROJECT=ON` to download the AWS C++ SDK code
* `-DNOT_FOR_DISTRIBUTION=ON` to confirm that you know to not distribute the resulting binaries

The plugin uses [AWS C++ SDK](https://github.com/awslabs/aws-sdk-cpp), which introduces the following restrictions:

* The plugin can only be built on Windows, Linux, and macOS.
* The plugin requires that one of the following compilers is used: `gcc` 4.8 or later, `clang` 3.3 or later, Visual Studio 2013 or later.
* On Unix, the `libcurl` development package (e.g. `libcurl3-dev` on Debian Jessie), `uuid` development package, and `openssl` need to be installed.
* You may need to use a newer version of [cmake](../../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) than is provided by default in your OS.

You do not need to download/install the AWS C++ SDK yourself; the correct version of the SDK GitHub repository will be cloned into the build directory at build time, and only the libraries for AWS components actually needed by the key management plugin will be built, which takes much less time than building the full AWS C++ SDK.

#### Building on Linux

With all prerequisites installed, the actual build process pretty much comes down to:

```bash
# clone the MariaDB Server source code repository
git clone https://github.com/MariaDB/server.git
cd server

# prepare the build
mkdir _build
cd _build
cmake .. -DNOT_FOR_DISTRIBUTION=ON \
  -DPLUGIN_AWS_KEY_MANAGEMENT=DYNAMIC \
  -DAWS_SDK_EXTERNAL_PROJECT=1

# build the plugin only
cd plugin/aws_key_management
make
```

Cmake will print the following warning as part of its output. Please take it seriously and do not distribute the `aws_key_management.so` file to any third parties: **You have linked MariaDB with Apache 2.0 libraries! You may not distribute the resulting binary. If you do, you will put yourself into a legal problem with the Free Software Foundation.**

After `make` succeeded you can copy the created `aws_key_management.so` plugin library file to the plugin directory of your actual MariaDB Server machines installation, e.g. `/usr/lib64/mysql/plugin` on RedHat/Fedora based systems or `/usr/lib/mysql/plugin` on Debian-based systems.

## Installing the Plugin

Even after the package that contains the plugin's shared library is installed on the operating system, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```sql
INSTALL SONAME 'aws_key_management';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = aws_key_management
```

## Uninstalling the Plugin

Before you uninstall the plugin, you should ensure that [data-at-rest encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) is completely disabled, and that MariaDB no longer needs the plugin to decrypt tables or other files.

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'aws_key_management';
```

If you installed the plugin by providing the [--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Configuring the AWS Key Management Plugin

To enable the AWS Key Management plugin, you also need to set the plugin's system variables. The [aws\_key\_management\_master\_key\_id](aws-key-management-encryption-plugin.md#aws_key_management_master_key_id) system variable is the primary one to set. These system variables can be specified as command-line arguments to [mysqld](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or they can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
aws_key_management_master_key_id=alias/<your key's alias>
```

Once you've updated the configuration file, restart the MariaDB server to apply the changes and make the key management and encryption plugin available for use.

## Using the AWS Key Management Plugin

Once the AWS Key Management Plugin is enabled, you can use it by creating an encrypted table:

```sql
CREATE TABLE t (i INT) ENGINE=InnoDB ENCRYPTED=YES
```

Now, table `t` will be encrypted using the encryption key generated by AWS.

For more information on how to use encryption, see [Data at Rest Encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md).

## Using Multiple Encryption Keys

The AWS Key Management Plugin supports [using multiple encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key can be defined with a different 32-bit integer as a key identifier. If a previously unused identifier is used, then the plugin will automatically generate a new key.

When [encrypting InnoDB tables](../innodb-encryption/), the key that is used to encrypt tables [can be changed](../innodb-encryption/innodb-encryption-keys.md).

When [encrypting Aria tables](../aria-encryption/), the key that is used to encrypt tables [cannot currently be changed](../aria-encryption/aria-encryption-keys.md).

## Key Rotation

The AWS Key Management plugin does support [key rotation](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#key-rotation). To rotate a key, set the [aws\_key\_management\_rotate\_key](aws-key-management-encryption-plugin.md#aws_key_management_rotate_key) system variable. For example, to rotate key with ID 2:

```sql
SET GLOBAL aws_key_management_rotate_key=2;
```

Or to rotate all keys, set the value to -1:

```sql
SET GLOBAL aws_key_management_rotate_key=-1;
```

## Versions

| Version | Status       | Introduced                                                                                                                                                                                                                                                                                                                 |
| ------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Stable       | [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes), [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes) |
| 1.0     | Beta         | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes)                                                                                                                                                              |
| 1.0     | Experimental | [MariaDB 10.1.13](https://github.com/mariadb-corporation/docs-server/blob/test/server/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/broken-reference/README.md)                                                                           |

## System Variables

### `aws_key_management_key_spec`

* Description: Encryption algorithm used to create new keys
* Commandline: `--aws-key-management-key-spec=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `AES_128`
* Valid Values: `AES_128`, `AES_256`

### `aws_key_management_log_level`

* Description: Dump log of the AWS SDK to MariaDB error log. Permitted values, in increasing verbosity, are Off (default), Fatal, Error, Warn, Info, Debug, and Trace.
* Commandline: `--aws-key-management-log-level=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value: `Off`
* Valid Values: `Off`, `Fatal`, `Warn`, `Info`, `Debug` and `Trace`

### `aws_key_management_master_key_id`

* Description: AWS KMS Customer Master Key ID (ARN or alias prefixed by alias/) for the master encryption key. Used to create new data keys. If not set, no new data keys will be created.
* Commandline: `--aws-key-management-master-key-id=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value:

### `aws_key_management_mock`

* Description: Mock AWS KMS calls (for testing). Must be enabled at compile-time.
* Commandline: `--aws-key-management-mock`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Valid Values: `OFF`, `ON`

### `aws_key_management_region`

* Description: AWS region name, e.g us-east-1 . Default is SDK default, which is us-east-1.
* Commandline: `--aws-key-management-region=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `'us-east-1'`

### `aws_key_management_request_timeout`

* Description: Timeout in milliseconds for create HTTPS connection or execute AWS request. Specify 0 to use SDK default.
* Commandline: `--aws-key-management-request-timeout=value`
* Scope: Global
* Dynamic: No
* Data Type: `integer`
* Default Value: 0

### `aws_key_management_rotate_key`

* Description: Set this variable to a data key ID to perform rotation of the key to the master key given in `aws_key_management_master_key_id`. Specify -1 to rotate all keys.
* Commandline: `--aws-key-management-rotate-key=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `integer`
* Default Value:

## Options

### `aws_key_management`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../../../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--aws-key-management=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
