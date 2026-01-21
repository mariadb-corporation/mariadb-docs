---
description: >-
  Guide to using the HashiCorp Key Management plugin, which integrates MariaDB
  with HashiCorp Vault for centralized, secure key storage and lifecycle
  management.
---

# Hashicorp Key Management Plugin

{% hint style="info" %}
**Key Rotation and Cache Flushing**&#x20;

As of MariaDB 12.3, you can manually rotate keys and flush the cache without restarting the server. See [Key Rotation and Cache Flushing](hashicorp-key-management-plugin.md#key-rotation-and-cache-flushing) for details.
{% endhint %}

The Hashicorp Key Management Pugin is used to implement encryption using keys stored in the Hashicorp Vault KMS. For more information, see [Hashicorp Vault and MariaDB](../../../../../server-management/automated-mariadb-deployment-and-administration/hashicorp-vault-and-mariadb.md), and for how to install Vault, see [Install Vault](https://www.vaultproject.io/docs/install), as well as [MySQL/MariaDB Database Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/databases/mysql-maria).

The current version of this plugin implements the following features:

* Authentication is done using the Hashicorp Vault's token authentication method.
* If additional client authentication is required, then the path to the CA authentication bundle file may be passed\
  as a plugin parameter;
* The creation of the keys and their management is carried out using the Hashicorp Vault KMS and their tools.
* The plugin uses libcurl (https) as an interface to the HashiCorp Vault server;
* JSON parsing is performed through the JSON service (through the include/mysql/service\_json.h);
* HashiCorp Vault 1.2.4 was used for development and testing.
* As of MariaDB 10.6.24, the plugin is configured to use cached keys for all communication errors, not just for timeouts. This ensures continuous operation when the Vault server is temporarily unreachable.
* As of MariaDB 10.6.24, the default setting for cache usage on error is `ON`.

Since we require support for key versioning, the key-value storage must be configured in Hashicorp Vault as a key-value storage that uses the interface of the second version. For example, you can create it as follows:

```bash
~$ vault secrets enable -path /test -version=2 kv
```

Key names must correspond to their numerical identifiers. Key identifiers itself, their possible values and rules of use are described in more detail in the MariaDB main documentation.

From the point of view of the key-value storage (in terms of Hashicorp Vault), the key is a secret containing one key-value pair with the name "data" and a value representing a binary string\
containing the key value, for example:

```bash
~$ vault kv get /test/1

====== Metadata ======
Key              Value
---              -----
created_time     2019-12-14T14:19:19.42432951Z
deletion_time    n/a
destroyed        false
version          1

==== Data ====
Key     Value
---     -----
data    0123456789ABCDEF0123456789ABCDEF
```

Keys values are strings containing binary data. MariaDB currently uses the AES algorithm with 256-bit keys as the default encryption method. In this case, the keys that will be stored in the Hashicorp Vault should be 32-byte strings. Most likely you will use some utilities for creating and administering keys designed to work with Hashicorp Vault. But in the simplest case, keys can be created from the command line through the vault utility, for example, as follows:

```bash
~$ vault kv put /test/1 data="0123456789ABCDEF0123456789ABCDEF"
```

If you use default encryption (AES), you should ensure that the key length is 32 bytes, otherwise it may fail to use InnoDB as a data storage.

The plugin currently does not unseal Hashicorp Vault on its own, you must do this in advance and on your own.

To use Hashicorp Vault KMS, the plugin must be preloaded and activated on the server. Most of its parameters should not be changed during plugin operation and therefore must be preconfigured as part of the server configuration through configuration file or command line options:

```
--plugin-load-add=hashicorp_key_management.so
--loose-hashicorp-key-management
--loose-hashicorp-key-management-vault-url="$VAULT_ADDR/v1/test"
--loose-hashicorp-key-management-token="$VAULT_TOKEN"
```

### Options

The plugin supports the following parameters, which must be set in advance and cannot be changed during server operation:

#### `hashicorp-key-management-vault-url`

* Description: HTTP\[s] URL that is used to connect to the Hashicorp Vault server. It must include the name of the scheme (`https://` for a secure connection) and, according to the API rules for storages of the key-value type in Hashicorp Vault, after the server address, the path must begin with the "/v1/" string (as prefix), for example: `https://127.0.0.1:8200/v1/my_secrets`. By default, the path is not set, therefore you must replace with the correct path to your secrets.
* Command line: `--[loose-]hashicorp-key-management-vault-url="<url>"`

#### `hashicorp-key-management-token`

* Description: Authentication token that passed to the Hashicorp Vault in the request header. By default, this parameter contains an empty string, so you must specify the correct value for it, otherwise the Hashicorp Vault server will refuse authorization. Alternatively, you can define an environment variable `VAULT_TOKEN` and store the token there.
* Command line: `--[loose-]hashicorp-key-management-token="<token>"`

#### `hashicorp-key-management-vault-ca`

* Description: Path to the Certificate Authority (CA) bundle (is a file that contains root and intermediate certificates). By default, this parameter contains an empty string, which means no CA bundle.
* Command line: `--[loose-]hashicorp-key-management-vault-ca="<path>"`

#### `hashicorp-key-management-timeout`

* Description: Set the duration (in seconds) for the Hashicorp Vault server connection timeout. The default value is 15 seconds. The allowed range is from 1 to 86400 seconds. The user can also specify a zero value, which means the default timeout value set by the libcurl library (currently 300 seconds).
* Command line: `--[loose-]hashicorp-key-management-timeout=<timeout>`

#### `hashicorp-key-management-max-retries`

* Description: Number of server request retries in case of timeout. Default is three retries.
* Command line: `----[loose-]hashicorp-key-management-max-retries=<retries>`

#### `hashicorp-key-management-caching-enabled`

* Description: Enable key caching (storing key values received from the Hashicorp Vault server in the local memory). By default caching is enabled.
* Command line: `--[loose-]hashicorp-key-management-caching-enabled="on"|"off"`

#### `hashicorp-key-management-use-cache-on-timeout`

* Description: This parameter instructs the plugin to use the key values or version numbers taken from the cache in the event of a timeout when accessing the vault server. By default this option is disabled. Please note that key values or version numbers will be read from the cache when the timeout expires only after the number of attempts to read them from the storage server that specified by the [--\[loose-\]hashicorp-key-management-max-retries](hashicorp-key-management-plugin.md#hashicorp-key-management-max-retries) parameter has been exhausted.
* Command line: `--[loose-]hashicorp-key-management-use-cache-on-timeout="on"|"off"`

#### `hashicorp-key-management-cache-timeout`

* Description: The time (in milliseconds) after which the value of the key stored in the cache becomes invalid and an attempt to read this data causes a new request send to the vault server. By default, cache entries become invalid after 60,000 milliseconds (after one minute). If the value of this parameter is zero, then the keys will always be considered invalid, but they still can be used if the vault server is unavailable and the corresponding cache operating mode (`--[loose-]hashicorp-key-management-use-cache-on-timeout="on"`) is enabled.
* As of MariaDB 10.6.24, the default value is 1 year (specified in milliseconds).
* Command line: `--[loose-]hashicorp-key-management-cache-timeout=<timeout>`

#### `hashicorp-key-management-cache-version-timeout`

* Description: The time (in milliseconds) after which the information about latest version number of the key (which stored in the cache) becomes invalid and an attempt to read this information causes a new request send to the vault server. If the value of this parameter is zero, then information about latest key version numbers always considered invalid, unless there is no communication with the vault server and use of the cache is allowed when the server is unavailable. By default, this parameter is zero, that is, the latest version numbers for the keys stored in the cache are considered always invalid, except when the vault server is unavailable and use\
  of the cache is allowed on server failures.
* Command line: `--[loose-]hashicorp-key-management-cache-version-timeout=<timeout>`

#### `hashicorp-key-management-check-kv-version`

* Description: This parameter enables ("on", this is the default value) or disables ("off") checking the kv storage version during plugin initialization. The plugin requires storage to be version 2 or older in order for it to work properly.
* Command line: `--[loose-]hashicorp-key-management-check-kv-version="on"|"off"`

## Key Rotation and Cache Flushing

_Available as of MariaDB 12.3_

The HashiCorp Key Management plugin supports key versioning provided by the HashiCorp Vault Server. In previous versions, rotating keys required a server restart to clear the internal cache. As of MariaDB 12.3, you can flush the plugin cache manually while the server is running.

#### Flushing the Cache

To rotate keys, you must flush the cached keys using the `FLUSH` command. This clears the local cache, forcing the server to re-fetch the latest key versions from the HashiCorp Vault server upon the next access.

Executing this command requires the `RELOAD` privilege.

```sql
FLUSH HASHICORP_KEY_MANAGEMENT_CACHE;
```

#### Verifying Key Versions

To view the current Key IDs and Key Versions stored in the latest version cache, you can query the Information Schema table or use the `SHOW` command.

See [Information Schema HASHICORP\_KEY\_MANAGEMENT\_CACHE](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-hashicorp_key_management_cache.md) for table details.

Using the SHOW command:

```sql
SHOW HASHICORP_KEY_MANAGEMENT_CACHE;
```

## See Also

* [HashiCorp Vault and MariaDB](../../../../../server-management/automated-mariadb-deployment-and-administration/hashicorp-vault-and-mariadb.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
