---
description: >-
  Discusses security best practices for running MariaDB in containers,
  addressing topics like root user privileges, volume permissions, and network
  isolation.
---

# Container Security

When using containers in production, it is important to be aware of container security concerns.

## Host System Security

Depending on the container runtime, containers may be running on the host system's kernel or a kernel shared with other containers. If this kernel has security bugs, those bugs are also present in the containers. Malicious containers may attempt to explain a kernel vulnerability to impact the confidentiality, integrity or availability of other containers.

In particular, Linux based containers have a container runtime that can use the following features:

* Namespaces, to isolate containers from each other and make sure that a container can't establish unauthorized connections to another container.
* [Seccomp security profiles](https://docs.docker.com/engine/security/seccomp/).
* [Rootless operation in Docker](https://docs.docker.com/engine/security/rootless/), or [Rootless Podman](https://www.redhat.com/sysadmin/rootless-containers-podman)
* [cgroups](https://docs.kernel.org/admin-guide/cgroup-v2.html), to limit the resources (CPU, memory, IO) that each container can consume.

The administrators of a system should be particularly careful to upgrade the kernel whenever security bugs to these features are fixed.

It is important to note that when we upgrade the kernel, runC or Docker itself we cause downtime for all the containers running on the system.

## Images Security

Containers are built from images. If security is a major concern, you should make sure that the images you use are secure.

If you want to be sure that you are pulling authentic images, you should only pull images signed with [Docker Content Trust](creating-a-custom-container-image.md). Signing only ensure authenticity or origin, it doesn't dictate that entity is trustworthy.

Updated images should be used. An image usually downloads packages information at build time. If the image is not recently built, a newly created container will have old packages. Updating the packages on container creation and regularly re-updating them will ensure that the container uses packages with the most recent versions. Rebuilding an image often will reduce the time necessary to update the packages the first time.

Security bugs are usually important for a database server, so you don't want your version of MariaDB to contain known security bugs. But suppose you also have a bug in Docker, in runC, or in the kernel. A bug in a user-facing application may allow an attacker to exploit a bug in those lower level technologies. So, after gaining access to the container, an attacker may gain access to the host system. This is why system administrators should keep both the host system and the software running in the containers updated.

## References

For more information, see the following links:

* [Container Security](https://www.redhat.com/en/topics/security/container-security) from Red Hat.
* [Docker security](https://docs.docker.com/engine/security/) on Docker documentation.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
