---
description: >-
  Explains how to provision and configure virtual machine instances specifically
  for Buildbot testing.
---

# Buildbot Setup for Virtual Machines - Ubuntu 11.04 "natty"

## Base Install

```
qemu-img create -f qcow2 vm-natty-amd64-serial.qcow2 8G
kvm -m 1024 -hda vm-natty-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.04-server-amd64.iso -redir tcp:2255::22 -boot d -smp 2 -cpu qemu64 -net nic,model=virtio -net user

# Install, picking default options mostly, only adding openssh server.

kvm -m 1024 -hda vm-natty-amd64-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.04-server-amd64.iso -redir tcp:2255::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2255 localhost

# edit /boot/grub/menu.lst and visudo, see below

ssh -t -p 2255 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2255 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2255 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2255 ttyS0.conf buildbot@localhost:
ssh -p 2255 buildbot@localhost 'sudo cp ttyS0.conf /etc/init/; rm ttyS0.conf; sudo shutdown -h now'
```

```
qemu-img create -f qcow2 vm-natty-i386-serial.qcow2 8G
kvm -m 1024 -hda vm-natty-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.04-server-i386.iso -redir tcp:2256::22 -boot d -smp 2 -cpu qemu32,-nx -net nic,model=virtio -net user

# Install, picking default options mostly, only adding openssh server.

kvm -m 1024 -hda vm-natty-i386-serial.qcow2 -cdrom /kvm/iso/ubuntu-11.04-server-i386.iso -redir tcp:2256::22 -boot c -smp 2 -cpu qemu64 -net nic,model=virtio -net user -nographic
ssh -p 2256 localhost

# edit /boot/grub/menu.lst and visudo, see below

ssh -t -p 2256 localhost "mkdir .ssh; sudo addgroup $USER sudo"
scp -P 2256 authorized_keys localhost:.ssh/
echo $'Buildbot\n\n\n\n\ny' | ssh -p 2256 localhost 'chmod -R go-rwx .ssh; sudo adduser --disabled-password buildbot; sudo addgroup buildbot sudo; sudo mkdir ~buildbot/.ssh; sudo cp .ssh/authorized_keys ~buildbot/.ssh/; sudo chown -R buildbot:buildbot ~buildbot/.ssh; sudo chmod -R go-rwx ~buildbot/.ssh'
scp -P 2256 ttyS0.conf buildbot@localhost:
ssh -p 2256 buildbot@localhost 'sudo cp ttyS0.conf /etc/init/; rm ttyS0.conf; sudo shutdown -h now'
```

Enabling passwordless sudo:

```
sudo VISUAL=vi visudo
# Add line at end: `%sudo ALL=NOPASSWD: ALL'
```

Editing /boot/grub/menu.lst:

```
sudo vi /etc/default/grub

# Add/edit these entries:
    GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8"
    GRUB_TERMINAL="serial"
    GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200 --word=8 --parity=no --stop=1"

sudo update-grub
```

## VMs for building .debs

```
for i in 'vm-natty-amd64-serial.qcow2 2255 qemu64' 'vm-natty-i386-serial.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/build/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get -y build-dep mysql-server-5.1" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y devscripts hardening-wrapper fakeroot doxygen texlive-latex-base ghostscript libevent-dev libssl-dev zlib1g-dev libreadline6-dev" ; \
done
```

## VMs for install testing.

See above for how to obtain my.seed and sources.append.

```
for i in 'vm-natty-amd64-serial.qcow2 2255 qemu64' 'vm-natty-i386-serial.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/serial/install/')" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get update" \
    "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y debconf-utils" \
    "= scp -P $2 my.seed sources.append buildbot@localhost:/tmp/" \
    "sudo debconf-set-selections /tmp/my.seed" \
    "sudo sh -c 'cat /tmp/sources.append >> /etc/apt/sources.list'"; \
done
```

## VMs for upgrade testing

```
for i in 'vm-natty-amd64-install.qcow2 2255 qemu64' 'vm-natty-i386-install.qcow2 2256 qemu64' ; do \
  set $i; \
  runvm --user=buildbot --logfile=kernel_$2.log --base-image=$1 --port=$2 --cpu=$3 "$(echo $1 | sed -e 's/install/upgrade/')" \
    'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.1' \
    'mysql -uroot -prootpass -e "create database mytest; use mytest; create table t(a int primary key); insert into t values (1); select * from t"' ;\
done
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
