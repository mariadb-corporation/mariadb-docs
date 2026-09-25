---
description: >-
  How to limit the CPU and memory a GridGain node uses on Linux with systemd,
  Docker, and taskset/cpuset to control the licensed core footprint.
---

# GridGain Resource Control

It is sometimes required to run a GridGain node with less resources than available on a machine. For example, your machine might have 8 cores, and you might want to use 4 for GridGain and - for another application. This would let you use a smaller license because GridGain is licensed for the number of cores it uses.

Typical cases where you would wang to limit (control) the number of cores GridGain uses are:

* Running CPU- and memory-constrained licensed GridGain editions on hardware that exceeds the per-node budget
* Running a sandbox cluster with multiple nodes sharing a single host for testing.
* Running efficiently on large hardware with multiple [NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access) nodes.

On linux machines, you can control the number of GridGain cores using [CGROUPS](https://man7.org/linux/man-pages/man7/cgroups.7.html) via:

* [Systemd](#systemd)
* [Docker](#docker)
* [Taskset/Cpuset](#taskset-cpuset)

## Systemd

[Systemd](https://systemd.io/) is a software suite that provides an array of system components for Linux operating systems.

When starting GridGain nodes as a service on Linux hosts, systemd is probably the best way to manage the host resources available to the JVM. It is the standard service scheduler and control stack for most mainstream Linux distributions. It helps you define resource limits via `AllowedCPUs` and `MemoryMax` settings. It is also desirable to use the systemd `OOMPolicy` setting to prevent killing GridGain JVMs if other processes could be sacrificed instead.

The required systemd settings are:

* [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html) — resource control unit settings systemd.resource-control
* [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — service unit configuration systemd.service
* [systemd-oomd.service](https://man7.org/linux/man-pages/man8/systemd-oomd.service.8.html) — a userspace out-of-memory killer

Here is an example of using systemd to run a node as a service with limited CPU and memory:

```shell
[Unit]
Description=GridGain cluster server
Documentation=https://www.gridgain.com/docs/index.html 
After=network.target auditd.service

[Service]
EnvironmentFile=-/etc/default/gridgain
ExecStart=/opt/gridgain/bin/ignite.sh $NODE_CONFIG
KillMode=process
Restart=on-failure
Type=simple
AllowedCPUs=4-7
MemoryMax=16G

[Install]
WantedBy=multi-user.target
Alias=gridgain.service
```

## Docker

[Docker](https://docs.docker.com/config/containers/resource_constraints/) provides resource controls similar to [Systemd](#systemd), which apply to all processes in the container runtime.

An example of using Docker to run nodes with limited CPUs:

```shell
docker run -it --cpus="4" gridgain /opt/gridgain/bin/ignite.sh
```

## Taskset/Cpuset

When starting GridGain as a standalone process outside of [Systemd](#systemd) or [Docker](#docker) control:

* The Linux [taskset](https://man7.org/linux/man-pages/man1/taskset.1.html) command can be used to assign certain CPUs on the host system. The JVM process will only see those CPUs assigned by `taskset`.
* The linux [cpuset](https://man7.org/linux/man-pages/man7/cpuset.7.html) feature can be used to assign certain CPUs on the host system, as well as set up memory and other limits. It may also be used to give GridGain JVMs exclusive access to the assigned CPUs for better isolation. 

In the following example, the `taskset` command runs the ignite.sh node startup script “pinned” to CPUs 0, 1, 2, and 3. GridGain will only see four CPUs for this node when calculating the license footprint.

```shell
taskset --cpu-list 0-3 bin/ignite.sh
```

The following example sandboxes multiple small nodes on a single machine. These nodes can be run on a single host using `taskset` to pin them to distinct sets of CPUs.

```shell
taskset --cpu-list 0-3 bin/ignite.sh; taskset --cpu-list 4-7 bin/ignite.sh
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
