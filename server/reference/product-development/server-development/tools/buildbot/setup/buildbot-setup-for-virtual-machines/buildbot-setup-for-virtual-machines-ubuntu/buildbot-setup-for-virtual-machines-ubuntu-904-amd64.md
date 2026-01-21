---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 9.04 amd64

## Base Install

```
qemu-img create -f qcow2 vm-jaunty-amd64-serial.qcow2 8G
kvm -m 1024 -hda vm-jaunty-amd64-serial.qcow2 -cdrom /kvm/ubuntu-9.04-server-amd64.iso -redir tcp:2227::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
```

## Serial port and passwordless login/sudo

```
kvm -m 1024 -hda vm-jaunty-amd64-serial.qcow2 -cdrom /kvm/ubuntu-9.04-server-amd64.iso -redir tcp:2227::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user

sudo apt-get install emacs22-nox
```

Add to /boot/grub/menu.lst:

```
serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1
terminal --timeout=3 serial console
```

also add in menu.lst to kernel line (after removing \`quiet splash'):

```
console=tty0 console=ttyS0,115200n8
```

Create /etc/event.d/ttyS0:

```
# ttyS0 - getty
#
# This service maintains a getty on ttyS0 from the point the system is
# started until it is shut down again.

start on stopped rc2
start on stopped rc3
start on stopped rc4
start on stopped rc5

stop on runlevel 0
stop on runlevel 1
stop on runlevel 6

respawn
exec /sbin/getty 115200 ttyS0
```

Add account and allow passwordless sudo:

```
sudo adduser --disabled-password buildbot
sudo adduser buildbot sudo
sudo EDITOR=emacs visudo
# uncomment `%sudo ALL=NOPASSWD: ALL' line in `visudo`, and move to end.

sudo su -s /bin/bash - buildbot
mkdir .ssh
cat >.ssh/authorized_keys
# Paste public key for buildbot user on host system.
chmod -R go-rwx .ssh
# Do manual login from host to guest once, to make sure .ssh/known_hosts is updated.
```

## VM for .deb building

```
qemu-img create -b vm-jaunty-amd64-serial.qcow2 -f qcow2 vm-jaunty-amd64-build.qcow2
kvm -m 1024 -hda vm-jaunty-amd64-build.qcow2 -cdrom /kvm/ubuntu-9.04-server-amd64.iso -redir tcp:2227::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic

sudo apt-get build-dep mysql-server-5.1
```

## VM for install testing

```
qemu-img create -b vm-jaunty-amd64-serial.qcow2 -f qcow2 vm-jaunty-amd64-install.qcow2
kvm -m 1024 -hda vm-jaunty-amd64-install.qcow2 -cdrom /kvm/ubuntu-9.04-server-amd64.iso -redir tcp:2227::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic

sudo adduser --system --group mysql
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
