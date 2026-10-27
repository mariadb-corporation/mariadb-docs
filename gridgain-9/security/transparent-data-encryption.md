---
description: >-
  Encrypt GridGain 9 data at rest with transparent data encryption (TDE), using
  a Java keystore or AWS KMS key encryption key provider.
---

# Transparent Data Encryption

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

## Overview

Transparent data encryption (TDE) allows users to encrypt their data at rest.

When [Ignite persistence](../architecture/storage/engines/native-persistent-storage.md) is turned on, all data in the cluster will be encrypted, including:

- Data on disk
- [Data snapshots](../gridgain9-management/snapshots/data-snapshots.md)
- RAFT log
- Meta storage

If you enable cluster encryption, the cluster will generate a data encryption key and will use this key to encrypt/decrypt the data. This key is held in the internal memory and cannot be accessed by users. When the cluster needs save it to disk (for example, when the node goes down), it is encrypted by using the user-provided key — the key encryption key.

The key encryption key provider must be specified in the cluster configuration.

## Key Generation Example

A keystore with a key can be created by using `keytool`:

{% code title="Key Generation Example" %}
```bash
user:~/tmp:[]$ keytool -genseckey \
-alias ignite.key \
-keystore ./ignite_keystore.jks \
-storetype PKCS12 \
-keyalg aes \
-storepass mypassw0rd \
-keysize 256

user:~/tmp:[]$ keytool \
-storepass mypassw0rd \
-storetype PKCS12 \
-keystore ./ignite_keystore.jks \
-list

Keystore type: PKCS12
Keystore provider: SunJSSE

Your keystore contains 1 entry

ignite.key, 12.01.2020, SecretKeyEntry,
```
{% endcode %}

The generated keystore can be provided to the cluster as

## Configuration

GridGain 9 supports two types of encryption providers: Java keystore (`.jks` or `.p12` files) and  [AWS KMS](https://docs.aws.amazon.com/kms/).

### Keystore Configuration

To enable encryption in the cluster, specify the path to your keystore in the cluster configuration by using the [CLI tool](../reference/cli-tool.md).

```json
{
    "ignite" : {
        "encryption" : {
            "enabled" : true,
            "activeProvider" : "keystore",
            "providers" : [{
                "name" : "keystore",
                "type" : "keystore",
                "keyStoreType" : "PKCS12",
                "path" : "/var/gridgain/keystore.jks",
                "password" : "mypassword",
                "activeKeyName" : "ignite.key",
                "cipher" : "AES/CBC/PKCS5Padding"
            }]
        }
    }
}
```

|Property Name|Default|Description|
|---|---|---|
|enabled|false|Determines if data encryption is enabled on the cluster.|
|activeProvider||The name of the currently used provider.|
|providers.keyStoreType|PKCS12|Type of the keystore.|
|providers.name||Name of the provider. This name is used in the `activeProvider` field.|
|providers.password||Password for opening the keystore and extracting the active key.|
|providers.path||The path to the keystore file.|
|providers.activeKeyName||Name or alias for the active key.|
|providers.cipher|AES/CBC/PKCS5Padding|The algorithm used to encrypt DEK keys. Once set, this value cannot be changed for the provider.<br><br>Supported algorithms:<br>- AES<br>- Chacha20<br><br>Supported modes:<br>- CBC<br>- GCM<br>- CTR<br>- OFB<br>- ECB<br>- CFB8<br><br>Supported paddings:<br>- NoPadding<br>- PKCS5Padding<br>- ISO10126Padding|

### AWS KMS Configuration

The following example shows how to configure AWS KMS provider.

```json
{
    "ignite" : {
        "encryption" : {
            "enabled" : true,
            "activeProvider" : "aws",
            "providers" : [{
                "name" : "aws",
                "type" : "aws_kms",
                "keyId" : "95e6cab1-2f34-47a9-8a79-52b3b3b79352"
            }]
        }
    }
}
```

You also need to set the following properties **for each node**:

- `aws.accessKeyId`
- `aws.secretAccessKey`
- `aws.region`

This can be done via environment variables, credentials file, or any other method that the AWS SDK supports. For more details, refer to the [AWS documentation](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html).

## Key Rotation

You may need to change the encryption key at the end of your key's validity period, or if the currently used key is compromised.

To change the key, first create a new provider with a different key in the cluster configuration. The example below is in the JSON format.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
{
    "ignite" : {
        "encryption" : {
            "enabled" : true,
            "activeProvider" : "keystore",
            "providers" : [{
                "name" : "otherKeystore",
                "type" : "keystore",
                "keyStoreType" : "PKCS12",
                "path" : "/var/gridgain/keystore_new.jks",
                "password" : "newPass",
                "activeKeyName" : "ignite.key.new",
                "cipher" : "AES/CBC/PKCS5Padding"
            },{
                "name" : "keystore",
                "type" : "keystore",
                "keyStoreType" : "PKCS12",
                "path" : "/var/gridgain/keystore.jks",
                "password" : "mypassword",
                "activeKeyName" : "ignite.key",
                "cipher" : "AES/CBC/PKCS5Padding"
            }]
        }
    }
}
```

Then, change the currently used provider to a provider with the new key.
