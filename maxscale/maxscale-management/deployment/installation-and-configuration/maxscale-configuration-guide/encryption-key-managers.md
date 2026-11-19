---
description: >-
  How MaxScale retrieves encryption keys with the file-based, KMIP, and
  HashiCorp Vault key managers, with their settings and limitations.
---

# MaxScale Encryption Key Managers

This page describes the key managers MaxScale can use to retrieve encryption keys.

The encryption key managers are how MaxScale retrieves symmetric encryption keys from a key management system. Some parts of MaxScale require the `key_manager` to be configured in order to work. The key manager that is used is selected with the [key\_manager](global-settings.md#key_manager) parameter and the key manager itself is configured by placing the parameters in the `[maxscale]` section.

The encryption key managers can be enabled at runtime using `maxctrl alter maxscale` but cannot be disabled once enabled. To disable the encryption key management, stop Maxscale, remove any persisted configuration files and remove `key_manager` as well as any key manager options from the static configuration files.

## File-based Key Manager

The encryption keys are stored in a text file stored on a local filesystem.

The file uses the same format as the MariaDB server [File Key Management Encryption Plugin](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md): a file consisting of an encryption key ID number and the hex-encoded encryption key separated by a semicolon. Read [Creating the Key File](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md#creating-the-key-file) for more details on how to create the file.

For example, to configure encryption for the `nosqlprotocol` shared credentials using the file-based encryption key:

1. Create the key file with `(echo -n '1;' ; openssl rand -hex 32) | cat > /var/lib/maxscale/encryption.key`
2. Give MaxScale read permissions on it with `chown maxscale:maxscale /var/lib/maxscale/encryption.key`
3. Configure MaxScale with the following:

```
[maxscale]
key_manager=file
file.keyfile=/var/lib/maxscale/encryption.key

[NoSQL-Listener]
type=listener
service=My-Service
protocol=nosqlprotocol
nosqlprotocol.authentication_key_id=1
nosqlprotocol.authentication_user=my_user
nosqlprotocol.authentication_password=my_password

# Add services, servers, monitors etc.
```

1. Start MaxScale

### Limitations

* Key versioning is not supported

### Settings for File-based Key Manager

**`file.keyfile`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Path to file containing encryption keys.

Path to the file that contains the encryption keys. The user MaxScale runs as (almost always `maxscale`) must be able to read this file. Encryption keys are read from disk only during startup or when any global MaxScale parameter is modified at runtime.

## KMIP Key Manager

Encryption keys are read from a KMIP server.

The KMIP key manager has been verified to work with the PyKMIP server.

### Limitations

* Key versioning is not supported
* Encryption keys are not cached locally: whenever MaxScale needs an encryption key, it retrieves it from the KMIP server.

### Settings for KMIP Key Manager

**`kmip.host`**

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the host where the KMIP server is.

The host where the KMIP server is.

**`kmip.port`**

* Type: integer
* Mandatory: Yes
* Dynamic: Yes
* Description: Defines the port on which the KMIP server listens.

The port on which the KMIP server listens on.

**`kmip.cert`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Client certificate for KMIP authentication.

The client public certificate used when connecting to the KMIP server.

**`kmip.key`**

* Type: path
* Mandatory: Yes
* Dynamic: Yes
* Description: Specifies the client private key used for connecting to the KMIP server.

The client private key used when connecting to the KMIP server.

**`kmip.ca`**

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: CA ceritficate for KMIP server.

The CA certificate to use. By default the system default certificates are used.

## HashiCorp Vault Key Manager

Encryption keys are read from a local or remote Vault server using the secret engine included in the Vault. This key manager supports versioned keys. Only version 2 key-value stores are supported.

The encryption keys use the same format as the MariaDB [HashiCorp Vault Key Management Plugin](../../../../../server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md) The key-value secret for each encryption key ID must contain the field `data` which must contain a hex-encoded string that is either 32, 48 or 64 characters long.

An easy way to generate a correct encryption key is to use the `vault` and `openssl` command line clients. The following command creates a 256-bit encryption key using `openssl` and stores it using the key ID `1`:

```
$ openssl rand -hex 32|vault kv put secret/1 data=-
== Secret Path ==
secret/data/1

======= Metadata =======
Key                Value
---                -----
created_time       2022-06-23T06:50:55.29063873Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1
```

### Limitations

* Encryption keys are not cached locally: whenever MaxScale needs an encryption key, it retrieves it from the Vault server.

### Settings for HashiCorp Vault Key Manager

**`vault.token`**

* Type: password
* Mandatory: Yes
* Dynamic: Yes
* Description: Provides the authentication token to access the Vault server.

The authentication token used to connect to the Vault server. This can be encrypted using `maxpasswd`, similar to how other passwords are encrypted.

**`vault.host`**

* Type: string
* Default: `localhost`
* Dynamic: Yes
* Description: Specifies the hostname of the Vault server.

The host where the Vault server is.

**`vault.port`**

* Type: integer
* Default: `8200`
* Dynamic: Yes
* Description: Defines the port on which the Vault server listens.

The port on which the Vault server listens on.

**`vault.ca`**

* Type: path
* Default: `""`
* Dynamic: Yes
* Description: Defines the CA certificate used for validating Vault server connections.

The CA certificate to use. By default the system default certificates are used.

**`vault.tls`**

* Type: [boolean](README.md#booleans)
* Default: true
* Dynamic: Yes
* Description: Manages whether encrypted (HTTPS) or unencrypted (HTTP) connections are used when communicating with the Vault server.

Whether to use encrypted connections (i.e. HTTPS or HTTP) when communicating with the Vault server.

**`vault.mount`**

* Type: string
* Default: `secret`
* Dynamic: Yes
* Description: Provides the Key-Value mount path in Vault where secrets are stored.

The Key-Value mount where the secret is stored. By default the `secret` mount is used which is present by default in most Vault installations.

**`vault.timeout`**

* Type: [duration](README.md#durations)
* Default: 30s
* Dynamic: Yes
* Description: Sets the timeout for requests and connections to the Vault server.

The connection and request timeout used with the Vault server.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
