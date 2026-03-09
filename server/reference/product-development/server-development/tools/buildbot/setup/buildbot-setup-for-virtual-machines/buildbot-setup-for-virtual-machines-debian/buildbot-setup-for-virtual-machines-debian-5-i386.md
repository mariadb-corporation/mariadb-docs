---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Debian 5 i386

## Base install

Download netinst CD image debian-503-i386-netinst.iso and install:

```
cd /kvm
qemu-img create -f qcow2 vms/vm-debian5-i386-base.qcow2 8G
kvm -m 2047 -hda /kvm/vms/vm-debian5-i386-base.qcow2 -cdrom /kvm/debian-503-i386-netinst.iso -redir 'tcp:2226::22' -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user
```

## Serial port console

From base install, setup for serial port, and setup accounts for passwordless\
ssh login and sudo:

```
qemu-img create -b vm-debian5-i386-base.qcow2 -f qcow2 vm-debian5-i386-serial.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian5-i386-serial.qcow2 -redir 'tcp:2226::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic
su
apt-get install sudo openssh-server emacs22-nox
visudo
# uncomment %sudo ALL=NOPASSWD: ALL
# add user account to group sudo.
# Copy in public ssh key.

# Add in /etc/inittab:
S0:2345:respawn:/sbin/agetty -h -L ttyS0 19200 vt100
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

Add user buildbot, with disabled password. Add as sudo, and add ssh key.

```
sudo adduser --disabled-password buildbot
sudo adduser buildbot sudo
sudo su - buildbot
mkdir .ssh
# Paste all necessary keys.
cat >.ssh/authorized_keys
chmod -R go-rwx .ssh
```

## Image for .deb build

```
qemu-img create -b vm-debian5-i386-serial.qcow2 -f qcow2 vm-debian5-i386-build.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian5-i386-build.qcow2 -redir 'tcp:2226::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic

sudo apt-get build-dep mysql-server-5.0
sudo apt-get install devscripts hardening-wrapper doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libreadline5-dev
```

## Image for install testing

```
qemu-img create -b vm-debian5-i386-serial.qcow2 -f qcow2 vm-debian5-i386-install.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian5-i386-install.qcow2 -redir 'tcp:2226::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic

# No packages mostly!
sudo apt-get install debconf-utils

cat >>/etc/apt/sources.list <<END
deb file:///home/buildbot/buildbot/debs binary/
deb-src file:///home/buildbot/buildbot/debs source/
END

sudo debconf-set-selections /tmp/my.seed
```

See the [General Principles](../buildbot-setup-for-virtual-machines-general-principles.md) article how to obtain the `my.seed` file.

## Image for upgrade testing

```
qemu-img create -b vm-debian5-i386-install.qcow2 -f qcow2 vm-debian5-i386-upgrade.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian5-i386-upgrade.qcow2 -redir 'tcp:2226::22' -boot c -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user -nographic

sudo apt-get install mysql-server-5.0
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
