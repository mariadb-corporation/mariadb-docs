---
description: >-
  Mount a GridGain license from a Kubernetes Secret. The operator never ships a
  license file.
---

# License

Every `GridGainCluster` needs a license. Create a Secret in the cluster namespace before you apply the custom resource.

```sh
kubectl create secret generic gridgaincluster-license \
  --from-file=gridgain-license.xml=/path/to/your/gridgain-license.xml
```

```yaml
spec:
  license:
    mountPath: /opt/gridgain/license
    fromSecret:
      name: gridgaincluster-license
    secretKey: gridgain-license.xml
```

Rotating only the Secret **value** (same name and key) hot-reloads. The operator does not restart pods for that change.

Changing `mountPath` or the Secret **name** changes the pod template and restarts nodes one at a time. See [Updates](updates.md#change-configuration).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
