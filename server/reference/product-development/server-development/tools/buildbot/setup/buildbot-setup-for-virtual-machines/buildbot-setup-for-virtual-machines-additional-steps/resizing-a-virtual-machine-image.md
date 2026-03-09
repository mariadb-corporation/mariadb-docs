---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Resizing a Virtual Machine Image

Some KVM images end up not having enough space on them. In such cases, it is preferable to increase the size of the VM rather than to just delete an image and rebuild it from scratch. The steps outlined below document what was done to increase the size of the Red Hat 5 x86 VM and should be able to be easily adapted to other VMs, should they need the same treatment in the future.

1. Make a copy of the VM to work on (we don't want to change the original):

```
cp -avi vm-rhel5-x86-build.qcow2 vm-rhel5-x86-build-new.qcow2
```

1. Using the `qemu-img` command, resize the image:

```
qemu-img info vm-rhel5-x86-build-new.qcow2
qemu-img resize vm-rhel5-x86-build-new.qcow2 +10G
qemu-img info vm-rhel5-x86-build-new.qcow2
rsync -avP vm-rhel5-x86-build-new.qcow2 terrier:/kvm/vms/
```

Not all versions of `qemu-img` can resize VMs.

1. Boot the newly resized image with gparted:

```
vm=vm-rhel5-x86-build-new.qcow2
kvm -m 2048 -hda /kvm/vms/${vm} -cdrom /kvm/iso/gparted-live-0.14.1-6-i486.iso -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:22666-:22
```

1. Connect to the VM using VNC from your local machine:

```
vncviewer -via <vmhost> localhost
```

Midway through booting you'll have to reconnect

1. Use gparted to either expand the existing primary partition or, especially\
   on VMs with LVM, add a new partition (since GParted can't change LVM\
   partitions). Exit when finished and shutdown the VM.
2. Boot the VM again, this time without a VNC server:

```
kvm -m 2048 -hda /kvm/vms/${vm} -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user,hostfwd=tcp:127.0.0.1:22666-:22 -nographic
```

1. login to the VM:

```
ssh -t -p 22666 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/buildbot.id_dsa buildbot@localhost
```

1. if expanded an existing partition: verify the new size
2. else if you created a new partition:

* mount the new partition to tmp location

```
sudo mount /dev/hda3 /mnt
```

* rsync contents of /home/ to the new partition

```
sudo rsync -avP /home/ /mnt/
```

* edit fstab to mount new partition to /home

```
sudo vi /etc/fstab
```

* mv `/home` to `/home-old`, create `/home` dir, mount `/home`

```
sudo mv -vi /home /home-old;sudo mkdir -v /home;sudo mount /home
```

* (optional) unmount `/mnt`

```
sudo umount /mnt
```

* reboot and verify that things look good

```
sudo /sbin/shutdown -h now
```

* if things do look good (new drive mounted OK, accounts work, etc...), delete `/home-old`

1. Move the old VM to `-old` and the `-new` VM to what the old VM used to be named

```
sudo mv -vi /kvm/vms/vm-rhel5-x86-build.qcow2 vm-rhel5-x86-build-old.qcow2; sudo mv -vi /kvm/vms/vm-rhel5-x86-build-new.qcow2 /kvm/vms/vm-rhel5-x86-build.qcow2
```

1. on other VM hosts, make a copy of the old file then rsync over the updated files (the copy helps speed up the rsync):

```
sudo cp -avi /kvm/vms/vm-rhel5-x86-build.qcow2 /kvm/vms/vm-rhel5-x86-build-old.qcow2
sudo rsync -avP terrier.askmonty.org::kvm/vms/vm-rhel5-x86-build* /kvm/vms/
```

1. Test the new VM with a build to make sure it works

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
