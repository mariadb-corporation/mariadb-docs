---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 9.04 i386

This vm is used to build source tarball and for Ubuntu 9.04 32-bit .deb.

First create and install image:

```
qemu-img create -f qcow2 vm-jaunty-i386-base.qcow2 8G
kvm -m 2047 -hda vm-jaunty-i386-base.qcow2 -cdrom ubuntu-9.04-server-i386.iso -redir tcp:2222::22 -boot d -cpu qemu32,-nx
# Install
```

Create a vm, based on the first one, which is configured for serial port.

```
qemu-img create -b vm-jaunty-i386-base.qcow2 -f qcow2 vm-jaunty-i386-serial.qcow2
kvm -m 2047 -hda vm-jaunty-i386-base.qcow2 -redir tcp:2222::22 -boot c -cpu qemu32,-nx
```

To configure kernel and grub for serial console, add the following to /boot/grub/menu.lst:

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

Add an account:

```
sudo adduser --disabled-password buildbot
```

Copy public ssh key into /.ssh/authorized\_keys

Enable passwordless sudo:

```
sudo adduser buildbot sudo
# uncomment `%sudo ALL=NOPASSWD: ALL' line in `visudo`, and move to end.
```

Create a new vm for building source tarballs:

```
qemu-img create -b vm-jaunty-i386-serial.qcow2 -f qcow2 vm-jaunty-i386-deb-tarbake.qcow2
```

Install compilers:

```
sudo apt-get build-dep mysql-5.1-server
sudo apt-get install devscripts hardening-wrapper bzr
```

Copy in an existing bzr shared repository to buildbot/.bzr (or\
run bzr init-repo and bzr branch --no-tree lp:maria).

Create a new vm for building .debs:

```
qemu-img create -b vm-jaunty-i386-serial.qcow2 -f qcow2 vm-jaunty-i386-deb-build.qcow2
```

Install compilers:

```
sudo apt-get build-dep mysql-5.1-server
sudo apt-get install devscripts hardening-wrapper
```

Create a new VM for testing .deb installs:

```
qemu-img create -b vm-jaunty-i386-serial.qcow2 -f qcow2 vm-jaunty-i386-deb-install.qcow2
```

Install tools and local apt repository.

```
sudo apt-get install debconf-utils
cat >>/etc/apt/sources.list <<END
deb file:///home/buildbot/buildbot/debs binary/
deb-src file:///home/buildbot/buildbot/debs source/
END
```

Setup default package config for debconf to enable unattended install. Copy in\
my.seed (see above) to vm.

```
sudo debconf-set-selections /tmp/my.seed
```

Create a new VM for testing upgrades:

```
qemu-img create -b vm-jaunty-i386-deb-install.qcow2 -f qcow2 vm-jaunty-i386-deb-upgrade.qcow2
```

Prepare initial MySQL install with some test data.

```
sudo apt-get install mysql-server-5.1
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
