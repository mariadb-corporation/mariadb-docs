{% hint style="warning" %}
Deactivation deallocates all memory resources, including your application data, on all cluster nodes and disables public cluster API. If you have in-memory caches that are not backed up by a persistent storage (neither [native persistent storage](../../architecture/storage/native-persistence.md) nor [external storage](../../gridgain8-usage/persistence/external-storage.md)), you will lose the data and will have to repopulate these caches.
{% endhint %}
