---
description: >-
  Operator and GridGain 8 images for the 1.0.0 release, including tags,
  architecture, and how to pin a digest.
---

# Docker Images

Pin published artifacts by **version and digest**, not by a branch or `latest`.

## Operator

| Component | Image | Tag | Architecture |
| --------- | ----- | --- | ------------ |
| GridGain 8 Kubernetes Operator | `docker.mariadb.com/gridgain8-operator` | `1.0.0` | `linux/amd64` |

Pull with the customer credentials described in [Customer Access to docker.mariadb.com](../mariadb-enterprise-operator/customer-access-to-docker-mariadb-com.md).

Resolve the digest after you can pull the tag:

```sh
docker pull docker.mariadb.com/gridgain8-operator:1.0.0
docker inspect --format='{{index .RepoDigests 0}}' docker.mariadb.com/gridgain8-operator:1.0.0
```

Set `image.tag` to that digest in Helm, or to `1.0.0` and record the digest in your change ticket.

## GridGain 8

The operator reconciles GridGain 8 server pods from `spec.image`. Minimum supported tag: **8.9.37** (probes and drain REST). Examples in this release use **8.9.38**.

| Component | Image | Supported tags | Architecture |
| --------- | ----- | -------------- | ------------ |
| GridGain 8 | `gridgain/ultimate` | `8.9.37`, `8.9.38` | follow the image you pull |

{% hint style="info" %}
The operator version (`1.0.0`) and the GridGain 8 tag are independent. Changing `spec.image.tag` is a version upgrade: scale the cluster to zero first. See [Updates](updates.md).
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
