---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Update Debian 4 Mirrors for Buildbot VMs

Debian 4 has become so old that the apt repository has been moved out of the\
main Debian 4 mirror servers, and into the archive of old versions. This needs\
to be fixed by pointing the Debian 4 images to a different mirror:

64-bit:

```
kvm -m 512 -hda vm-debian4-amd64-install.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=e1000 -net user -nographic

sudo vi /etc/apt/sources.list
# replace http://ftp.dk.debian.org/debian/ with http://ftp.de.debian.org/archive/debian/
```

32-bit:

```
kvm -m 512 -hda vm-debian4-i386-install.qcow2 -redir 'tcp:2200::22' -boot c -smp 1 -cpu qemu64 -net nic,model=e1000 -net user -nographic

sudo vi /etc/apt/sources.list
# replace http://ftp.dk.debian.org/debian/ with http://ftp.de.debian.org/archive/debian/
```

After that, it is necessary to re-do from scratch the -update and -update2\
debian4 images (as these are built on top of the -install images).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
