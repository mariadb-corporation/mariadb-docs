# CSI Specific Configuration

## blob-csi-driver (Azure Blob Storage)

This section outlines a recommended `StorageClass` configuration for the [Azure Blob Storage CSI Driver](https://github.com/kubernetes-sigs/blob-csi-driver) that 
resolves common mounting and list operation issues encountered in Kubernetes environments.

The following [`StorageClass`](https://kubernetes.io/docs/concepts/storage/storage-classes/) is recommended when working with Azure Blob Storage (ABS).

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: blob-fuse
provisioner: blob.csi.azure.com
parameters:
  protocol: fuse2
reclaimPolicy: Retain
volumeBindingMode: Immediate
allowVolumeExpansion: true
mountOptions:
  # Resolves the issue where non-root containers cannot access the mounted blob container.
  - -o allow_other
  # Ensures list operations (critical for backups/deletion) work immediately upon mount.
  - --cancel-list-on-mount-seconds=0
```

Next, when defining your `PhysicalBackup` resource, make sure to use the new `StorageClass` we created.

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: PhysicalBackup
metadata:
  name: physicalbackup
spec:
  # ...
  storage:
    persistentVolumeClaim:
      # Specify your own class
      storageClassName: blob-fuse
```

### Issue 1: Access for Non-Root Containers (`-o allow_other`)

The default configuration prevents non-root Kubernetes containers from accessing the mounted blob container, resulting in an "unaccessible" volume.
By setting the mountOption `-o allow_other`, non-root containers are granted access to the volume, resolving this issue.

See [this issue](https://github.com/kubernetes-sigs/blob-csi-driver/issues/2078) for more information.

### Issue 2: Immediate List Operations and Backup Deletion (`--cancel-list-on-mount-seconds=0`)

When using the `blob-csi-driver` with its default settings, list operations (which are critical for cleaning up old backups) may not work immediately upon mount,
leading to issues like old physical backups never being deleted.
Setting the mountOption `--cancel-list-on-mount-seconds` to "0" ensures that list operations work as expected immediately after the volume is mounted.

See [this issue](https://github.com/kubernetes-sigs/blob-csi-driver/issues/558#issuecomment-961563722) for more information.

{% hint style="warning" %}
Setting `cancel-list-on-mount-seconds` to 0 forces the driver to perform an immediate list operation, which may increase both initial mount time and Azure transaction costs
(depending on the number of objects in the container). Operators should consider these performance and financial trade-offs and consult the official Azure Blob 
Storage documentation or an Azure representative for guidance.
{% endhint %}

---

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
