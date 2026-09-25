---
description: >-
  Troubleshooting GridGain Operator deployments: diagnosing pods that fail to
  start, inspecting operator logs, and handling a missing default StorageClass.
---

# Troubleshooting

## POD Does Not Start

Sometimes a POD could be stuck in a `CrashLoopBackOff` state and it is not obvious what happened behind this error. To understand the root cause, use the following command with the `-p` option to inspect the previous failed state:

```shell
kubectl logs -p  <pod name> -n apache-ignite
```

## Inspecting Operator Logs

For debugging common issues, inspect the operator's pod logs. You can retrieve a pods list by using the following command, assuming that the operator is deployed and running:

```
kubectl get pods -n <operator-namespace>
NAME                                      READY   STATUS    RESTARTS   AGE
apache-ignite-operator-868fb8bdcd-46xnh   1/1     Running   0          8d
```

Knowing a running pod's name, you can inspect the pod logs by using the following command:

```
kubectl logs apache-ignite-operator-868fb8bdcd-46xnh -n <operator-namespace>

--------------------------- Ansible Task Status Event StdOut -----------------

PLAY RECAP *********************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=14   rescued=0    ignored=0
```

The `<operator-namespace>` is `apache-ignite-operator` by default.

## Missing Default StorageClass

If you notice the following error in the logs, either add a default StorageClass or configure StorageClass manually by referring to the [Storage configuration](operator-configuration.md#storage-configuration) section.

```
TASK [create-statefulset : fail] *********************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "The system is unable to locate StorageClass with name 'myClassName'"
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
