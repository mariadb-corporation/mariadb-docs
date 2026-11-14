---
description: >-
  Operator and GridGain 8 images for the 1.0.0 release, including tags and
  architecture.
---

# Docker Images

Use these versions for the 1.0.0 release.

## Operator

| Component | Image | Tag | Digest | Architecture |
| --------- | ----- | --- | ------ | ------------ |
| MariaDB GridGain 8 Kubernetes Operator | `docker.mariadb.com/gridgain8-operator` | `1.0.0` | `sha256:<digest>` | `linux/amd64` |

Pull with the customer credentials described in [Customer Access to docker.mariadb.com](../mariadb-enterprise-operator/customer-access-to-docker-mariadb-com.md). Set Helm `image.tag` to `1.0.0`.

## GridGain 8

The operator reconciles GridGain 8 server pods from `spec.image`. Minimum supported tag: **8.9.37** (probes and drain REST). Examples in this release use **8.9.38**.

| Component | Image | Tag | Digest | Architecture |
| --------- | ----- | --- | ------ | ------------ |
| GridGain 8 | `gridgain/ultimate` | `8.9.37` | `sha256:<digest>` | follow the image you pull |
| GridGain 8 | `gridgain/ultimate` | `8.9.38` | `sha256:<digest>` | follow the image you pull |

{% hint style="info" %}
The operator version (`1.0.0`) and the GridGain 8 tag are independent. Changing `spec.image.tag` is a version upgrade: scale the cluster to zero first. See [Updates](updates.md).
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
