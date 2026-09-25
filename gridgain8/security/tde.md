---
description: >-
  Transparent Data Encryption in GridGain: encrypt data at rest per cache,
  generate a master key, and rotate master and cache keys.
---

# Transparent Data Encryption

## Overview

Transparent data encryption (TDE) allows users to encrypt their data on disk at rest.

When [Ignite persistence](../architecture/storage/native-persistence.md) is turned on, encryption can be enabled per cache/table, in which case the following data will be encrypted:

- Data on disk
- WAL records

Other data, such as data stored in memory, will not be encrypted.

If you enable cache/table encryption, the cluster will generate a key (called _cache encryption key_) and will use this key to encrypt/decrypt the cache's data. The cache encryption key is held in the system internal memory and cannot be accessed by users. When the key needs to be sent to other nodes or saved to disk (when the node goes down), it is encrypted using the user-provided key — the _master key_.

The master key must be specified via the configuration in every server node. One way to ensure you are using the same key is to copy the JKS file from one node to the other nodes. In an attempt to enable TDE, the node with a different key will not be able to join the cluster.

The GridGain cluster supports a single Encryption SPI implementation that is `KeystoreEncryptionSPI`, which uses the running JVM's default keystore format. On JDK 8 (or earlier), the default is JKS, while on JDK 9 and later it defaults to PKCS12. You can also explicitly set the `keystore.type` system property by using the `-Dkeystore.type`. It supports `AES/CBC/PKCS5Padding` for encrypting WAL records and `AES/CBC/NoPadding` for encrypting data pages on disk.

## Master Key Generation Example

A keystore with a master key can be created using `keytool` as follows:

{% code title="Master Key Generation Example" %}
```shell
user:~/tmp:[]$ java -version
java version "17.0.12" 2024-07-16 LTS
Java(TM) SE Runtime Environment (build 17.0.12+8-LTS-286)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.12+8-LTS-286, mixed mode, sharing)

user:~/tmp:[]$ keytool -genseckey -alias ignite.master.key -keystore ./ignite_keystore.p12 -storetype PKCS12 -keyalg aes -storepass mypassw0rd -keysize 256 && keytool -storepass mypassw0rd -storetype PKCS12 -keystore ./ignite_keystore.p12 -list

Generated 256-bit AES secret key
Keystore type: PKCS12
Keystore provider: SUN

Your keystore contains 1 entry

ignite.master.key, Mar 21, 2025, SecretKeyEntry,
```
{% endcode %}

## Configuration

To enable encryption in the cluster, you should determine an Encryption SPI through Ignite configuration and enable encryption at the last one cache that will be encrypted. A configuration example is shown below.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <!-- We need to configure EncryptionSpi to enable encryption feature. -->
    <property name="encryptionSpi">
        <!-- Using EncryptionSpi implementation based on java keystore. -->
        <bean class="org.apache.ignite.spi.encryption.keystore.KeystoreEncryptionSpi">
            <!-- Path to the keystore file. -->
            <property name="keyStorePath" value="ignite_keystore.p12"/>
            <!-- Password for keystore file. -->
            <property name="keyStorePassword" value="mypassw0rd"/>
            <!-- Name of the key in keystore to be used as a master key. -->
            <property name="masterKeyName" value="ignite.master.key"/>
            <!-- Size of the cache encryption keys in bits. Can be 128, 192, or 256 bits.-->
            <property name="keySize" value="256"/>
        </bean>
    </property>
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="encrypted-cache"/>
            <property name="encryptionEnabled" value="true"/>
        </bean>
    </property>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

KeystoreEncryptionSpi encSpi = new KeystoreEncryptionSpi();

encSpi.setKeyStorePath("/home/user/ignite-keystore.p12");
encSpi.setKeyStorePassword("secret".toCharArray());

cfg.setEncryptionSpi(encSpi);
```
{% endtab %}
{% endtabs %}

When the master key is configured, you can enable encryption for a cache as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<property name="cacheConfiguration">
    <bean class="org.apache.ignite.configuration.CacheConfiguration">
        <property name="name" value="encrypted-cache"/>
        <property name="encryptionEnabled" value="true"/>
    </bean>
</property>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration<Long, String> ccfg = new CacheConfiguration<Long, String>("encrypted-cache");

ccfg.setEncryptionEnabled(true);

ignite.createCache(ccfg);
```
{% endtab %}

{% tab title="SQL" %}
```sql
CREATE TABLE encrypted(
  ID BIGINT,
  NAME VARCHAR(10),
  PRIMARY KEY (ID))
WITH "ENCRYPTED=true";
```
{% endtab %}
{% endtabs %}

## Master Key Rotation

Master key rotation is required at the end of the crypto period (key validity period) or if the master key has been compromised.

**Prerequisites**:

* A new master key must be available to EncryptionSPI for each server node.
* The cluster must be active.

### Available Interfaces

The GridGain cluster enables you to rotate the master key via the following interfaces:

* Command-line utility

To start master key rotation:

```
control.sh --encryption change_master_key newMasterKeyName
```

To display the cluster's current master key name:

```
control.sh --encryption get_master_key_name
```

* JMX

To start master key rotation:

```
changeMasterKey(String masterKeyName)
```

Get the current master key name:

```
String getMasterKeyName()
```

* Java API

To start master key rotation:

```
ignite.encryption().changeMasterKey(String masterKeyName)
```

Get the current master key name:

```
String ignite.encryption().getMasterKeyName()
```

### Master Key Change Procedure

Each server node performs the following actions:

1. A node checks that the cluster is active. Otherwise, the process completes with an error.
2. It verifies that the master key name and digest are the same as those taken from the prepare phase. Otherwise, the process is canceled.
3. The creation of encrypted group keys is blocked.
4. All cache group keys are re-encrypted with the new master key in a temporary data structure. No changes in MetaStore are made.
5. The node creates a WAL logical record (ChangeMasterKeyRecord ) that consist of:
* New master key name
* Re-encrypted cache group keys
6. The node writes cache group keys to MetaStore.
7. The creation of encrypted group keys is unblocked.

### Cache Key Rotation

Cache encryption key rotation is required if the key is compromised or at the end of the crypto period (key validity period).
This feature is also needed to provide support for encrypting and decrypting existing caches in the future.

Note that the old keys will no longer be used to write new data to the storage. Reading can be done using the old key.

The process of cache encryption key rotation consists of the following steps:

1. Rotate cache group key - add a new encryption key on each node and set it for writing.
2. Schedule background re-encryption for archived data and clean up the old key when it completes.

You can manage the process of cache key rotation (and cache re-encryption) through the command line by executing the following commands:

* Launch cache key rotation:

```
control.(sh|bat) --encryption change_cache_key cacheGroupName
```

* View key identifiers of the cache group:

```
control.(sh|bat) --encryption cache_key_ids cacheGroupName
```

* View re-encryption status for the cache group:

```
control.(sh|bat) --encryption reencryption_status cacheGroupName
```

* Suspend/resume the cache group re-encryption:

```
control.(sh|bat) --encryption suspend_reencryption cacheGroupName
```

* View/change the re-encryption rate limit:

```
control.(sh|bat) --encryption reencryption_rate [--limit limit]
Parameters:
limit  - Decimal value to change the re-encryption rate limit (MB/s).
```

**Note**: Old cache group encryption key will be removed when:

* The cache group's re-encryption process is finished, and then at least one checkpoint is successfully completed as well.
* The last WAL segment, in which the encryption key was used, is removed.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
