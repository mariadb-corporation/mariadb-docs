---
description: >-
  How to deploy a GridGain cluster on RedHat OpenShift using the oc
  command-line tool.
---

# RedHat OpenShift Deployment

This guide is a step-by-step instruction on deploying a GridGain cluster on RedHat OpenShift.

{% hint style="info" %}
This guide covers the provider-specific steps. It builds on the shared [Generic Kubernetes Instruction](generic-configuration.md), which explains the concepts, prerequisites, and configuration common to all Kubernetes deployments.
{% endhint %}
## Before You Begin

We assume that you have already installed RedHat OpenShift and configured the command-line tool `oc`.
Visit [this page](https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html) for detailed instructions.

## OpenShift Configuration

The namespace, service, cluster role, ConfigMap, and node configuration file are the same for every Kubernetes deployment. Follow the [Generic Kubernetes Instruction](generic-configuration.md#kubernetes-configuration) to create these resources.

On OpenShift, use the `oc` command-line tool instead of `kubectl`, and create a project instead of a namespace. Run the following commands in place of the `kubectl` commands in the generic instruction:

```shell
oc new-project gridgain
oc create -f service.yaml
oc create sa gridgain -n gridgain
oc create -f cluster-role.yaml
oc create configmap gridgain-config -n gridgain --from-file=node-configuration.xml
oc create configmap gridgain-license -n gridgain --from-file=gridgain-license.xml
oc create -f statefulset.yaml
```

Replace `kubectl` with `oc` in the remaining commands as well, for example `oc get pods -n gridgain`.
