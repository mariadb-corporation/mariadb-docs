---
description: >-
  How to download the GridGain Operator bundle and an overview of the YAML files
  it contains.
---

# Download GridGain Operator

The GridGain Operator bundle contains templates and resources for deploying GridGain 
Operator and GridGain components to your Kubernetes cluster. As a first step, you need to download the GridGain Operator bundle.

Find the download link on the `Extensions` tab of the official [GridGain download webpage](https://www.gridgain.com/resources/download#extensions).

## Operator Bundle

Operator bundle is just an archive with a set of *.yaml files:

```
bundle
├── crds
│   ├── crds.yaml
│   ├── ignite.yaml
│   └── ignite_config.yaml
├── operator.yaml
└── rbac.yaml
```

### Files Overview

#### crds.yaml

Describes the Ignite [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/). You do not need to change this file.

#### ignite.yaml

Describes the Ignite Custom Resource and contains a set of high-level cluster settings, please see the [Ignite Resource](operator-configuration.md#ignite-resource) section for more details.

#### ignite_config.yaml

Describes the IgniteConfig [Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) and contains a set of internal cluster settings, please see the [IgniteConfig Resource](operator-configuration.md#igniteconfig-resource) section for more details.

#### operator.yaml

Describes Operator deployment. Most of the time you will not change this file.

#### rbac.yaml

Describes the [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) settings. Most of the time you will not change this file.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
