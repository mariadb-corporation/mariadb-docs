---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Buildbot Setup for Virtual Machines

This section documents the exact steps used to set up each virtual machine used\
in the MariaDB Buildbot for building packages and testing. There are lots of\
boring details, but the information here should be useful for reference, and as\
a help when installing new virtual images for additional distros and versions.

The articles here document how the virtual machine images were actually set up,\
not the most efficient way to recreate all of them. Thus, some historical\
artifacts remain, reflecting the order they were initially added and lessons\
learned along the way.

For example, the steps for the earliest VMs are somewhat overly enthusiastic\
about using the `qemu-img create -b` option to make one vm a copy-on-write copy\
on top of another image. This makes it harder to modify the images afterwards,\
since if the base image is modified, any copy-on-write vm on top of it needs to\
be re-created.

The descriptions do not go into painful detail about the installation procedure.\
Generally the .iso for the distro was downloaded, and the default,\
non-graphical installer started. Installing Linux these days is quite easy, and\
generally just defaults were picked. With respect to harddisk partitioning,\
generally an 8Gb image was configured, of which 1/2 Gb was reserved for swap\
and the rest for a single root partition "/".

For details on setting up a host server to run these VMs, see [Buildbot Setup for VM host](../buildbot-setup-for-vm-host.md).
