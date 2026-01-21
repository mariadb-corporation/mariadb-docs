---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Installing the Boost Library Needed for the OQGraph Storage Engine

The OQGraph storage engine needs a newer version of Boost that what is\
available on (most) distributions. The version installed is 1.42.0, available\
from.

The boost library is installed in all the builder virtual machine images with\
the following single command:

```bash
for i in "vm-hardy-amd64-build qemu64" "vm-hardy-i386-build qemu32,-nx" \
        "vm-intrepid-amd64-build qemu64" "vm-intrepid-i386-build qemu32,-nx" \
        "vm-karmic-amd64-build qemu64" "vm-karmic-i386-build qemu32,-nx" \
        "vm-jaunty-amd64-build qemu64" "vm-jaunty-i386-deb-build qemu32,-nx" \
        "vm-lucid-amd64-build qemu64" "vm-lucid-i386-build qemu32,-nx" \
        "vm-maverick-amd64-build qemu64" "vm-maverick-i386-build qemu32,-nx" \
        "vm-natty-amd64-build qemu64" "vm-natty-i386-build qemu64" \
        "vm-oneiric-amd64-build qemu64" "vm-oneiric-i386-build qemu64" \
        "vm-debian5-amd64-build qemu64" "vm-debian5-i386-build qemu32,-nx" \
        "vm-debian4-amd64-build qemu64 --netdev=e1000" "vm-debian4-i386-build qemu32,-nx --netdev=e1000" \
        "vm-centos5-i386-build qemu32,-nx" "vm-centos5-amd64-build qemu64" \
        "vm-hardy-amd64-build qemu64" "vm-hardy-i386-build qemu32,-nx" \
        "vm-jaunty-i386-deb-tarbake qemu32,-nx" ; do \
  set $i; \
  runvm -m 512 --smp=1 --port=2200 --user=buildbot --cpu=$2 $3 $1.qcow2 \
    "= scp -P 2200 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no /kvm/boost_1_42_0.tar.gz buildbot@localhost:/dev/shm/" \
    "sudo mkdir -p /usr/local/src /usr/local/include" \
    "cd /usr/local/src && sudo tar zxf /dev/shm/boost_1_42_0.tar.gz" \
    "cd /usr/local/include && sudo ln -s ../src/boost_1_42_0/boost ." ; \
done
```

## Upgrade Boost to 1.49

To upgrade boost on the VMs to 1.49 I performed the following steps:

_I initially tried to upgrade the VMs using a script like the one at the top of the page which was used to install boost 1.42, but I ran into issues with getting it to work on all of the VMs (it worked on some, but not on others). So I ended up using the steps below._

1. Copy the VM (keeping the original as a backup, in case something goes wrong):

```
oldvm="vm-debian6-i386-build.qcow2"
newvm="vm-debian6-i386-build.upd.qcow2"
cp -avi ${oldvm} ${newvm}
```

1. Start the VM:

```
kvm -m 1024 -hda /kvm/vms/${newvm} -redir 'tcp:22775::22' -boot c -smp 1 -cpu qemu64 -net nic,model=virtio -net user -nographic
```

1. Copy the boost tar.gz file over to the VM:

```
scp -i /kvm/vms/ssh-keys/id_dsa -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P 22775 /kvm/boost_1_49_0.tar.gz buildbot@localhost:/dev/shm/
```

1. ssh into the VM:

```
ssh -i /kvm/vms/ssh-keys/id_dsa -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22775 buildbot@localhost
```

1. once inside the VM, perform the following steps:

```
cd /usr/local/src
sudo tar zxf /dev/shm/boost_1_49_0.tar.gz 
cd /usr/local/include/
sudo rm boost
sudo ln -s ../src/boost_1_49_0/boost .
sudo /sbin/shutdown -h now
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
