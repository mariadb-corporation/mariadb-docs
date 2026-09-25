---
description: >-
  How to create, restore, and remove GridGain network backups on NAS, NFS, or
  SFTP storage, including SFTP location configuration and JKS key setup.
---

# Network Backups

GridGain provides a way to create network backups, allowing you to back up your cluster data to a network location such as NAS, NFS or SFTP for recovery purposes. Since the data is stored on a different physical device, network backups provide security against disk failures. The network location is used as a centralized storage where all cluster nodes can save data and then use it for recovery. Using centralized storage also lets you restore the cluster to a different physical location or even in the cloud.

{% hint style="info" %}
If you want to restore the cluster to a different topology, refer to the [Heterogeneous Recovery](heterogeneous-recovery.md) page.
{% endhint %}

## Prerequisites

- Snapshot functionality has to be enabled. Please refer to [Snapshots & Recovery](full-incremental-snapshots.md) for instructions.
- *NAS* or *NFS* storage: centralized storage has to be mounted to all machines hosting the cluster nodes and have the same path.
- *SFTP* location: an SFTP server needs to be accessible from all GridGain cluster nodes. Follow
[this section to enable an SFTP location](#configuring-sftp-location) for GridGain backups.

## Creating Network Backup

There are two ways to create a network backup:

- Create a local (regular) snapshot and move it to a shared folder. This operation is unsupported for SFTP-based backups.
- Create a snapshot directly into a shared folder.

These two approaches are discussed below.

### Saving Snapshots Directly to Centralized Storage

{% hint style="info" %}
This approach is not recommended if your NFS storage is slow (i.e. based on HDD disks). Instead, create local
snapshots to a fast SSD and copy/move them to a remote folder afterwards.
{% endhint %}

You can tell GridGain to create a snapshot directly into the centralized storage by specifying a path:

{% tabs %}
{% tab title="Shell" %}
```shell
snapshot-utility.sh snapshot -type=full -dest=/shared/folder
```
{% endtab %}
{% tab title="Java" %}
```java
// Get a reference to the GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots interface.
GridSnapshot snapshots = gg.snapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
SnapshotFuture<Void> snapshotFuture = snapshots.createFullSnapshot(null,
        new File("/shared/folder/path/"), new SnapshotCreateParams(),
        "Snapshot has been created!");

// Wait until the snapshot is created.
snapshotFuture.get();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Moving Snapshots to Centralized Storage

If you do not specify a snapshot location when creating a snapshot, each node will save its data to a local folder.
In this case, the snapshot is stored on local drives of the cluster nodes. To move the data to a centralized storage,
use either the `move` command of the Snapshots Management Tool or the Java API.

{% tabs %}
{% tab title="Shell" %}
```shell
# Example with shared folder such as NFS or NAS
snapshot-utility.sh move -id=123456 -dest=/shared/folder

# Example with an SFTP location that requires user credentials
snapshot-utility.sh move -id=123456 -dest=sftp://login:password@address:port/relativePath

# Example with an SFTP location that requires a key alias
snapshot-utility.sh move -id=123456 -dest=sftp://login@address:port/relativePath -key_alias=sftpKeyAlias
```
{% endtab %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot snapshot = gg.snapshot();

// Get the first snapshot from the list.
SnapshotInfo info = snapshot.list().get(0);

// Get the snapshot ID.
long snapshotId = info.snapshotId();

snapshot.moveSnapshot(snapshotId,
    new File("/shared/folder/path"), true, "Snapshot Moved");

SnapshotPath destination = sftpDestination
    ? SnapshotPath.sftp().uri(new URI("sftp://login@address:port/relativePath"))
    .keyAlias("keyAlias")
    .build()
    : SnapshotPath.file().path(new File("/shared/folder/path")).build();

// Move the snapshot with given ID to a shared folder.
SnapshotFuture<Void> future = snapshot.move(
    new MoveSnapshotParams()
        .snapshotId(snapshotId)
        .destinationPath(destination)
        .skipWalMove(true)
        .singleFileCopy(true)
).get()

    .move(snapshotId,
        new File("/shared/folder/path"), true, "Snapshot Moved");

// Wait for the operation to finish.
future.get();

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var snapshot = ignite.GetSnapshot();

// Get the first snapshot from the list.
var en = snapshot.GetSnapshots(null).GetEnumerator();
en.MoveNext();
var info = en.Current;

// Get the snapshot ID.
long snapshotId = info.SnapshotId;

// Move the snapshot with given ID to a shared folder.
var task = snapshot.MoveSnapshotAsync(snapshotId, "/shared/folder/path", "Snapshot Moved");

// Wait for the operation to finish.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Restoring from Network Backup

To restore a cluster from a network backup, use the centralized storage as a snapshot location:

{% tabs %}
{% tab title="Shell" %}
```shell
# Example with shared folder
snapshot-utility.sh restore -id=123456 -src=/shared/folder

# Example with sftp server with login-password auth
snapshot-utility.sh restore -id=123456 -src=sftp://login:password@address:port/relativePath

# Example with sftp server with login-key auth
snapshot-utility.sh restore -id=123456 -src=sftp://login@address:port/relativePath -key_alias=sftpKeyAlias
```
{% endtab %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to GridSnapshot.
GridSnapshot storage = gg.snapshot();

// Get the first snapshot from the list.
SnapshotInfo info = storage.listSnapshots(null).get(0);

// Get the snapshot ID.
long snapshotId = info.snapshotId();

SnapshotPath location = sftpLocation
    ? SnapshotPath.sftp().uri(new URI("sftp://login@address:port/relativePath"))
    .keyAlias("keyAlias")
    .build()
    : SnapshotPath.file().path(new File("/shared/folder/path")).build();

// Replace content of all the caches with the content from the snapshot.
SnapshotFuture<Void> future = storage
    .restore(new RestoreSnapshotParams()
        .snapshotId(snapshotId)
        .optionalSearchPaths(Arrays.asList(location))
        .message("Cluster Restored!")
    );

// Wait until the operation finishes.
future.get();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var snapshot = ignite.GetSnapshot();

// Get the first snapshot from the list.
var en = snapshot.GetSnapshots(null).GetEnumerator();
en.MoveNext();
var info = en.Current;

// Get the snapshot ID.
long snapshotId = info.SnapshotId;

// Replace content of all the caches with the content from the snapshot.
var task = snapshot.RestoreSnapshotAsync(snapshotId, new[] { "/shared/folder/path" }, null, "Cluster Restored!");

// Wait for the operation to finish.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Each node computes which partitions belong to the local node and restores corresponding partitions from the centralized storage to the local storage.

## Removing Network Backups

To remove a network backup use the means of the centralized storage, for example a file manager, an SFTP client, or a
retention policy of the storage itself.

To see which snapshots the centralized storage holds, run the `list` command against that storage:

{% code title="Shell" %}
```shell
# Example with shared folder
snapshot-utility.sh list -src=/shared/folder

# Example with sftp server with login-password auth
snapshot-utility.sh list -src=sftp://login:password@address:port/relativePath
```
{% endcode %}

Each snapshot occupies one folder whose name ends with `_<snapshot ID>.snapshot`, with one folder per cluster node
inside it. Removing that folder removes the snapshot from the centralized storage.

GridGain cannot remove network backups itself. The `delete` command only removes a snapshot from the local snapshot
folder of each cluster node. The same applies to scheduled deletion: a schedule created with `-command=delete` prunes
local snapshots only.

## Configuring SFTP Location

To enable an SFTP location for GridGain backups, you need to provide `org.gridgain.grid.persistentstore.snapshot.file.SftpConfiguration` that includes several connectivity-related settings:

{% code title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

   <!-- Enabling the Ignite Native Persistence. -->
  <property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <property name="defaultDataRegionConfiguration">
        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
          <property name="persistenceEnabled" value="true"/>
        </bean>
      </property>
    </bean>
  </property>

  <!-- Enabling the snapshots. -->
  <property name="pluginConfigurations">
    <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
      <property name="snapshotConfiguration">
        <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
            <property name="sftpConfiguration">
                <!-- Enabling the SFTP location with keys access. -->
                <bean class="org.gridgain.grid.configuration.SftpConfiguration">
                    <!-- Java KeyStore (JKS) path. -->
                    <property name="keyPath" value="path" />

                    <!-- JKS passphrase (optional). -->
                    <property name="passphrase" value="password" />

                    <!-- Whether to verify the SFTP server's SSH host key (optional). -->
                    <property name="strictHostKeyChecking" value="true" />

                    <!-- Known hosts file used for verification (optional). -->
                    <property name="knownHostsPath" value="/path/to/known_hosts" />
                </bean>
            </property>
        </bean>
      </property>
    </bean>
  </property>
</bean>
```
{% endcode %}

`strictHostKeyChecking` controls whether GridGain verifies the SFTP server's SSH host key before transferring
snapshot data. When enabled, the host key must match an entry in the file set by `knownHostsPath`. If
`knownHostsPath` isn't set, GridGain uses `~/.ssh/known_hosts` of the account running the node instead. The
connection fails if the key isn't found, or if `knownHostsPath` points to a file that doesn't exist or can't
be read.

Follow the steps below to create a Java KeyStore (JKS) with the keys that Ignite can use to authenticate on your
SFTP server:

1. Generate certificates:

   {% code title="Shell" %}
   ```shell
openssl req -x509 -newkey rsa:4096 -keyout myKey.pem -out cert.pem -days 365 -nodes
   ```
   {% endcode %}
2. Convert the certificates to the PKCS12 format:

   {% code title="Shell" %}
   ```shell
openssl pkcs12 -export -out node.p12 -inkey myKey.pem -in cert.pem -name sftp
   ```
   {% endcode %}
3. Add a private key with its alias to the JKS:

   {% code title="Shell" %}
   ```shell
keytool -v -importkeystore -srckeystore node.p12 -srcstoretype PKCS12 -destkeystore example.jks -deststoretype JKS -alias example_alias
   ```
   {% endcode %}
4. (Optional) Create a public key for your SFTP server:

   {% code title="Shell" %}
   ```shell
ssh-keygen -y -f myKey.pem > myKey.pub
   ```
   {% endcode %}
5. Confirm the following files are generated:
   * `example.jks` - the JKS file with `alias=example_alias`
   * `myKey.pub` - a public key to authenticate on the SFTP server

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
