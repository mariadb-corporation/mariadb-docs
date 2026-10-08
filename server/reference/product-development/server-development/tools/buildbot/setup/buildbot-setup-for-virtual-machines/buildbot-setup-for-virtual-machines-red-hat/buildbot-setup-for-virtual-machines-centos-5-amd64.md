---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Centos 5 amd64

## Base install

```
cd /kvm
wget http://ftp.klid.dk/ftp/centos/5.3/isos/x86_64/CentOS-5.3-x86_64-bin-DVD.iso
qemu-img create -f qcow2 vms/vm-centos5-amd64-serial.qcow2 8G
kvm -m 2047 -hda /kvm/vms/vm-centos5-amd64-serial.qcow2 -cdrom CentOS-5.3-x86_64-bin-DVD.iso -redir 'tcp:2237::22' -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user
```

## Serial port and account setup

```
kvm -m 2047 -hda /kvm/vms/vm-centos5-amd64-serial.qcow2 -cdrom CentOS-5.3-i386-bin-DVD.iso -redir 'tcp:2237::22' -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
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

Run these commands:

```
cat >>/etc/inittab <<END
 
# Serial console.
S0:2345:respawn:/sbin/agetty -h -L ttyS0 19200 vt100
END
```

```
useradd buildbot

# Password is disabled by default in Centos5.

usermod -a -G wheel buildbot
visudo

# Uncomment the line "%wheel        ALL=(ALL)       NOPASSWD: ALL"
# Comment out this line:
# Defaults    requiretty

# Put in public ssh key for own account and host buildbot account.
# Note that Centos5 seems to require .ssh/authorized_keys chmod go-rwx.

su - buildbot
mkdir .ssh
chmod go-rwx .ssh
cat >.ssh/authorized_keys
chmod go-rwx .ssh/authorized_keys
```

## Image for rpm build

```
qemu-img create -b vm-centos5-amd64-serial.qcow2 -f qcow2 vm-centos5-amd64-build.qcow2
kvm -m 2047 -hda /kvm/vms/vm-centos5-amd64-build.qcow2 -cdrom /kvm/CentOS-5.3-x86_64-bin-DVD.iso -redir 'tcp:2237::22' -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
```

Install compilers etc:

```
sudo yum groupinstall "Development Tools"
sudo yum install gperf readline-devel ncurses-devel libaio-devel openssl-devel zlib-devel perl perl\(DBI\)
```

Download 5.0 rpm for shared-compat:

```
sudo mkdir -p /srv/shared/yum/CentOS/5/x86_64/RPMS/
cd /srv/shared/yum/CentOS/5/x86_64/RPMS/
sudo wget http://mirror.ourdelta.org/yum/CentOS/5/x86_64/RPMS/MySQL-OurDelta-shared-5.0.87.d10-65.el5.x86_64.rpm
```

## Image for install/test

```
qemu-img create -b vm-centos5-amd64-serial.qcow2 -f qcow2 vm-centos5-amd64-install.qcow2
kvm -m 2047 -hda /kvm/vms/vm-centos5-amd64-install.qcow2 -cdrom /kvm/CentOS-5.3-x86_64-bin-DVD.iso -redir 'tcp:2237::22' -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
```

Install extra dependencies:

```
sudo yum install perl perl\(DBI\)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
