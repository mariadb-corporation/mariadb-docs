---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Debian 4 amd64

```
cd /kvm/vms
qemu-img create -f qcow2 vm-debian4-amd64-serial.qcow2 8G
kvm -m 2047 -hda /kvm/vms/vm-debian4-amd64-serial.qcow2 -cdrom /kvm/debian-40r8-amd64-netinst.iso -redir 'tcp:2240::22' -boot d -smp 2 -cpu qemu64 -net nic,model=e1000 -net user
```

## Serial console and account setup

From base install, setup for serial port, and setup accounts for passwordless\
ssh login and sudo:

```
kvm -m 2047 -hda /kvm/vms/vm-debian4-amd64-serial.qcow2 -cdrom /kvm/debian-40r8-amd64-netinst.iso -redir 'tcp:2240::22' -boot c -smp 2 -cpu qemu64 -net nic,model=e1000 -net user

su
apt-get install sudo openssh-server
VISUAL=vi visudo
# Add at the end:t %sudo ALL=NOPASSWD: ALL

# Add account <USER> to group sudo
# Copy in public ssh key.

# Add in /etc/inittab:
S0:2345:respawn:/sbin/getty -L ttyS0 19200 vt100
```

Add to /boot/grub/menu.lst:

```
serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1
terminal --timeout=3 serial console
```

also add in menu.lst to kernel line:

```
console=tty0 console=ttyS0,115200n8

# Add user buildbot, with disabled password. Add as sudo, and add ssh key.
sudo /usr/sbin/adduser --disabled-password buildbot
sudo /usr/sbin/adduser buildbot sudo
sudo su - buildbot
mkdir .ssh
# Add all necessary keys.
cat >.ssh/authorized_keys
chmod -R go-rwx .ssh
```

## VM for build

```
qemu-img create -b vm-debian4-amd64-serial.qcow2 -f qcow2 vm-debian4-amd64-build.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian4-amd64-build.qcow2 -cdrom /kvm/debian-40r8-amd64-netinst.iso -redir 'tcp:2240::22' -boot c -smp 2 -cpu qemu64 -net nic,model=e1000 -net user -nographic

sudo apt-get build-dep mysql-server-5.0
# Some latex packages fail to install because they complain that the
# source is more than 5 years old! I solved by setting back the clock a
# couple of years temporarily ...
sudo apt-get install devscripts doxygen texlive-latex-base gs lsb-release fakeroot libevent-dev libssl-dev zlib1g-dev libreadline5-dev
```

## VM for install testing

```
qemu-img create -b vm-debian4-amd64-serial.qcow2 -f qcow2 vm-debian4-amd64-install.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian4-amd64-install.qcow2 -cdrom /kvm/debian-40r8-amd64-netinst.iso -redir 'tcp:2240::22' -boot c -smp 2 -cpu qemu64 -net nic,model=e1000 -net user -nographic
```

See the [General Principles](../buildbot-setup-for-virtual-machines-general-principles.md)\
article for how to make the '`my.seed`' file.

```
# No packages mostly!
sudo apt-get install debconf-utils

cat >>/etc/apt/sources.list <<END
deb file:///home/buildbot/buildbot/debs binary/
deb-src file:///home/buildbot/buildbot/debs source/
END

sudo debconf-set-selections /tmp/my.seed
```

## VM for upgrade testing

```
qemu-img create -b vm-debian4-amd64-install.qcow2 -f qcow2 vm-debian4-amd64-upgrade.qcow2
kvm -m 2047 -hda /kvm/vms/vm-debian4-amd64-upgrade.qcow2 -cdrom /kvm/debian-40r8-amd64-netinst.iso -redir 'tcp:2240::22' -boot c -smp 2 -cpu qemu64 -net nic,model=e1000 -net user -nographic

sudo apt-get install mysql-server-5.0
mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
