# Migrate to Graceful Shutdown Switchover in 26.06

The MariaDB Enterprise Operator 26.06 introduces a new feature: **Graceful Shutdown Switchover**. This feature is enabled by default and automatically triggers a primary switchover when a primary Pod is gracefully terminated (e.g., during a node drain).

If you are upgrading from a version prior to 26.06 and wish to maintain the previous behavior (i.e., you do not want switchovers to happen automatically on graceful shutdown), you must update your MariaDB Custom Resources (CRs).

## Migration Steps

1. **Upgrade the CRDs:** First, upgrade the MariaDB Enterprise Operator CRDs to version 26.06 or later to make the new configuration fields available. Please refer to the [installation guide](../installation/helm.md) for detailed instructions on upgrading via Helm.
2. **Update MariaDB CRs:** After updating the CRDs, edit the `spec` of all your `MariaDB` Custom Resources to explicitly disable the feature. This ensures the new behavior is not triggered once the operator controller is upgraded. Add the following configuration under `spec.replication.primary`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb-repl
spec:
  # [...]
  replication:
    enabled: true
    primary:
      autoSwitchoverOnGracefulShutdown: false
  # [...]
```

You can achieve this imperatively using `kubectl patch`:

```bash
kubectl patch mariadb mariadb-repl \
  --type='merge' \
  -p '{"spec":{"replication":{"primary":{"autoSwitchoverOnGracefulShutdown":false}}}}'
```

3. **Update the Operator:** Once the CRs have been updated, you can safely upgrade the operator controller to version 26.06.

## More Information

For more details about the Graceful Shutdown Switchover feature and its implications, please refer to the [Primary Graceful Shutdown Switchover](../topologies/replication.md#primary-graceful-shutdown-switchover) section in the Replication documentation.